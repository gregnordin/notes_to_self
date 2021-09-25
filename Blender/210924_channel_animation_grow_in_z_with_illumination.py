import bpy
from math import pi
from functools import partial

# Add blender file directory to the python path
import sys

blender_file_path = str(bpy.path.abspath("//"))
if blender_file_path not in sys.path:
    sys.path.append(blender_file_path)
# print()
# print(sys.path)

from blender_tools.lights import point_light, sun_light, area_light
from blender_tools.materials import (
    make_material_Principled_BSDF,
    make_material_Principled_and_Transparent_BSDF,
    make_semitransparent_emission_shader,
)
from blender_tools.layer_objects import make_layer, make_channel_layer, make_edge_layer
from blender_tools.animation import animate_object_transparency, frame_number


# ----------------------------------------------------------------------------------------
# Animation helpers
# ----------------------------------------------------------------------------------------


class Animated3DObject:
    """Given a Blender 3D object, make it easy to do fade-in, fade-out, disappear,
    appear, and color change animations.

    Example usage:
        # Make an object with a material
        layer = make_layer("Test_Layer", xy_layer_size, xy_layer_size, z_layer_size, z)
        mat = make_material("Test_Material", color_RGB_bulk)
        layer.data.materials.append(mat)

        # Try class animations
        test_layer = Animated3DObject(layer)
        start_frame, end_frame = 5, 25
        test_layer.fade_in(start_frame, end_frame)
        test_layer.disappear_at_frame(end_frame + 20)
        test_layer.appear_at_frame(end_frame + 40)
        test_layer.animate_change_color(color_RGB_edge, end_frame + 50, end_frame + 65)
        start_frame, end_frame = end_frame + 80, end_frame + 95
        test_layer.fade_out(start_frame, end_frame)

    """

    def __init__(self, obj):
        # Specify which type of layer object (bulk, channel, channel with edge, roof with reduced exposure region)
        # Use Factory Method design pattern to create objects?? And then initialize object with whatever parameters it needs?
        # Build layer object:
        self.object = obj
        self.material = self.object.active_material
        self.material_nodes = self.material.node_tree.nodes
        self.material_alpha_param = self.material_nodes["Principled BSDF"].inputs[
            "Alpha"
        ]
        # self.set_fully_transparent()
        # Color shortcut
        self.material_color_param = self.material_nodes["Principled BSDF"].inputs[
            "Base Color"
        ]
        # Record scale value. Must make a copy, otherwise self.save_scale just points to the object's scale:
        self.save_scale = self.object.scale.copy()
        self.save_location = self.object.location.copy()

    def set_scale(self, value):
        # print(f"in set_scale...")
        # print("Before", self.object.scale, value)
        self.object.scale = value
        # print("After", self.object.scale, value)

    def set_visible(self, visibility_flag):
        """Set whether object is visible or not.

        Args:
            visibility_flag (Boolean): True = visible, False = not visible.
        """
        if visibility_flag:
            self.set_scale(self.save_scale)
        else:
            new_scale = (0.0, 0.0, 0.0)
            self.set_scale(new_scale)

    def appear_at_frame(self, frame):
        # print(f"Appear at frame {frame}")
        self.set_visible(False)
        self.object.keyframe_insert(data_path="scale", frame=frame - 1)
        self.set_visible(True)
        self.object.keyframe_insert(data_path="scale", frame=frame)

    def disappear_at_frame(self, frame):
        # print(f"Disappear at frame {frame}")
        self.set_visible(True)
        self.object.keyframe_insert(data_path="scale", frame=frame - 1)
        self.set_visible(False)
        self.object.keyframe_insert(data_path="scale", frame=frame)

    def fade_in(self, start_frame, end_frame, initial_value=0.0, final_value=1.0):
        self.set_transparency_value(initial_value)
        self.material_alpha_param.keyframe_insert("default_value", frame=start_frame)
        self.set_transparency_value(final_value)
        self.material_alpha_param.keyframe_insert("default_value", frame=end_frame)

    def fade_out(self, start_frame, end_frame):
        self.fade_in(start_frame, end_frame, initial_value=1.0, final_value=0.0)

    def set_transparency_value(self, value):
        self.material_alpha_param.default_value = value

    def set_fully_transparent(self):
        self.set_transparency_value(0.0)

    def set_opaque(self):
        self.set_transparency_value(1.0)

    def set_color(self, new_color):
        # If receive an RGB color, convert to RGBA
        if len(new_color) == 3:
            new_color = (*new_color, 1.0)
        # Make sure we have an RGBA color
        assert len(new_color) == 4
        self.material_color_param.default_value = new_color

    def animate_change_color(self, new_color, start_frame, end_frame):
        current_color = self.material_color_param.default_value
        self.set_color(current_color)
        self.material_color_param.keyframe_insert("default_value", frame=start_frame)
        self.set_color(new_color)
        self.material_color_param.keyframe_insert("default_value", frame=end_frame)

    def grow_in_negative_z(self, start_frame, end_frame, z_position):
        # Assumes self.object.scale is already (0, 0, 0)

        # Make layer appear at frame start_frame
        self.object.keyframe_insert(data_path="scale", frame=start_frame - 1)
        xy_scale = (self.save_scale[0], self.save_scale[1], 0)
        self.set_scale(xy_scale)
        self.object.keyframe_insert(data_path="scale", frame=start_frame)

        # Set up keyframes to start growing in -z
        self.object.keyframe_insert(data_path="scale", frame=start_frame)
        self.object.keyframe_insert(data_path="location", frame=start_frame)

        # Set up values and keyframes to define end of growth in -z
        self.set_scale(self.save_scale)
        new_location = (
            self.save_location[0],
            self.save_location[1],
            z_position,  # - self.save_scale[2] / 2,
        )
        self.object.location = new_location
        self.object.keyframe_insert(data_path="scale", frame=end_frame)
        self.object.keyframe_insert(data_path="location", frame=end_frame)


# ----------------------------------------------------------------------------------------
# Main code
# ----------------------------------------------------------------------------------------


# Set up Rendering to use bloom
bpy.context.scene.eevee.use_bloom = True
bpy.data.scenes["Scene"].eevee.bloom_intensity = 0.1

# Layers
xy_layer_size = 10
z_layer_size = 0.5
channel_width = 3
edge_width = 1
num_layers = 9
num_small_layers_per_layer = 3
z_small_layer_size = z_layer_size / num_small_layers_per_layer
# Specify channel and roof layers
chan_layers = [2, 3, 4, 5]
roof_layers = [6, 7]

# Define colors
# Primary color - golden
color_RGB_bulk = (1, 0.71, 0.2)  # RGB (255, 180, 51) = HEX #FFB433
# Triadic color #1 - greenish
color_RGB_edge = (0.2, 1.0, 0.71)  # RGB (51, 255, 180) = HEX #33ffb4
# Triadic color #2 - purple
color_RGB_small_edge = (0.71, 0.2, 1.0)  # RGB (180, 51, 255) = HEX #b433ff
# LED emission color
color_emission = (0.08, 0.03, 1.0)  # RGB (20, 8, 255) = HEX #1408FF


# Animation setup
frames_per_second = bpy.data.scenes["Scene"].render.fps
# # Change to 60 fps
# bpy.data.scenes["Scene"].render.fps = 60
# frames_per_second = bpy.data.scenes["Scene"].render.fps
# Set up function to return frame number given time in seconds
frame_num = partial(frame_number, frames_per_second=frames_per_second)

# Lights
light_location = (8.1524, 2.0110, 11.808)
light_rotation = [pi * 37.3 / 180, pi * 3.16 / 180, pi * 107 / 180]
light_sun = sun_light(location=light_location, rotation=light_rotation)
# light_pt = my_point_light(location=light_location, rotation=light_rotation)
# light_area = my_area_light(location=light_location, rotation=light_rotation)
# light_area2 = my_area_light(location=light_location, rotation=light_rotation. power=1000, size=2.5, name="Light_area2")

# Camera
# create the camera object
cam_data = bpy.data.cameras.new("camera")
cam = bpy.data.objects.new("camera", cam_data)
bpy.context.collection.objects.link(cam)
# add camera to scene
scene = bpy.context.scene
scene.camera = cam
# position and rotate camera
cam.location = (21.247, -19.997, 14.316)
cam.rotation_euler = [pi * 66.7 / 180, pi * 0.0 / 180, pi * 46.7 / 180]

# Materials
# Select which layer material type by uncommenting one of the following 2 lines
make_material = make_material_Principled_BSDF
# make_material = make_material_Principled_and_Transparent_BSDF
# Emissive material
make_LED_material = partial(
    make_semitransparent_emission_shader, strength=5, mix_fac=0.6
)


# Select which case to run by uncommenting one of the following 5 lines
case = "bulk"
# case = "channel"
# case = "channel with edge dose"
# case = "channel with edge dose and roof dose"
# case = "channel with small edge layers and roof dose"

# Set up layer lists for specific case chosen
channel_layers = []
secondary_image_channel_layers = []
secondary_image_small_channel_layers = []
secondary_image_roof_layers = []
if case == "bulk":
    pass
elif case == "channel":
    channel_layers = chan_layers
elif case == "channel with edge dose":
    secondary_image_channel_layers = chan_layers
elif case == "channel with edge dose and roof dose":
    secondary_image_channel_layers = chan_layers
    secondary_image_roof_layers = roof_layers
elif case == "channel with small edge layers and roof dose":
    secondary_image_small_channel_layers = chan_layers
    secondary_image_roof_layers = roof_layers

# Loop to create layers, materials, and animation keyframes
fadein_duration_seconds = 1.0
time_between_layer_fadeins_seconds = 0.5
fadein_duration_seconds_small_layer = 0.6
time_between_layer_fadeins_seconds_small_layer = 0.25
start_time = 0.3
for i in range(num_layers):

    z = i * z_layer_size - z_layer_size / 2
    end_time = start_time + fadein_duration_seconds
    # print(i, z, start_time, end_time)

    layer_str = f"{i:02d}"
    layer_name = f"Layer_{layer_str}"
    material_name = f"Material_{layer_str}"

    if i in channel_layers:

        layer = make_channel_layer(
            layer_name, xy_layer_size, xy_layer_size, z_layer_size, z, channel_width
        )
        mat = make_material(material_name, color_RGB_bulk)
        layer.data.materials.append(mat)
        layer = Animated3DObject(layer)
        layer.fade_in(frame_num(start_time), frame_num(end_time))

    elif i in secondary_image_channel_layers:
        # Create 3 layer objects:
        #     Channel (channel size = channel_width)
        #     Eroded Channel (channel size = channel_width + 2*edge_width)
        #     Edge (2 strips, each of width edge_width, on each side of channel)
        # Use Channel object and fade-in with edge dose color
        # Instantaneously replace Channel object with Eroded Channel and Edge objects just before starting next step
        #     Eroded Channel and Edge are already at full edge dose color
        # Animate Eroded Channel color from edge dose color to bulk color

        # Create Channel layer
        layer_channel = make_channel_layer(
            layer_name, xy_layer_size, xy_layer_size, z_layer_size, z, channel_width,
        )

        # Create Eroded Channel layer
        layer_eroded_channel = make_channel_layer(
            layer_name,
            xy_layer_size,
            xy_layer_size,
            z_layer_size,
            z,
            channel_width + 2 * edge_width,
        )

        # Create Edge layer
        layer_edge = make_edge_layer(
            layer_name,
            xy_layer_size,
            xy_layer_size,
            z_layer_size,
            z,
            channel_width,
            edge_width,
        )

        # Make materials. All layer objects begin with the edge dose color
        mat_channel = make_material(material_name, color_RGB_edge)
        mat_eroded = make_material(material_name, color_RGB_edge)
        mat_edge = make_material(material_name, color_RGB_edge)
        layer_channel.data.materials.append(mat_channel)
        layer_eroded_channel.data.materials.append(mat_eroded)
        layer_edge.data.materials.append(mat_edge)

        # Create animation objects for each layer object
        layer_channel = Animated3DObject(layer_channel)
        layer_eroded_channel = Animated3DObject(layer_eroded_channel)
        layer_edge = Animated3DObject(layer_edge)

        # Set initial conditions
        layer_eroded_channel.set_visible(False)
        layer_eroded_channel.set_opaque()
        layer_edge.set_visible(False)
        layer_edge.set_opaque()

        # Fade-in edge dose
        layer_channel.fade_in(frame_num(start_time), frame_num(end_time))

        # Adjust start and end times to do bulk dose
        start_time = end_time + time_between_layer_fadeins_seconds
        end_time = start_time + fadein_duration_seconds

        # Swap out layer channel for edge and eroded channel layers
        layer_channel.disappear_at_frame(frame_num(start_time))
        layer_eroded_channel.appear_at_frame(frame_num(start_time))
        layer_edge.appear_at_frame(frame_num(start_time))

        # Animate color change for bulk region
        layer_eroded_channel.animate_change_color(
            color_RGB_bulk, frame_num(start_time), frame_num(end_time)
        )

    elif i in secondary_image_small_channel_layers:

        # Do N-1 small layers (last small layer has to be treated separately)
        for j in range(num_small_layers_per_layer):
            end_time = start_time + fadein_duration_seconds_small_layer
            layer_small_edge = make_edge_layer(
                layer_name,
                xy_layer_size,
                xy_layer_size,
                z_small_layer_size,
                z + j * z_small_layer_size,
                channel_width,
                edge_width,
            )
            mat_small_edge = make_material(material_name, color_RGB_small_edge)
            layer_small_edge.data.materials.append(mat_small_edge)
            layer_small_edge = Animated3DObject(layer_small_edge)
            layer_small_edge.fade_in(frame_num(start_time), frame_num(end_time))
            if j < num_small_layers_per_layer - 1:
                start_time = end_time + time_between_layer_fadeins_seconds_small_layer

        # Create Eroded Channel layer
        layer_eroded_channel = make_channel_layer(
            layer_name,
            xy_layer_size,
            xy_layer_size,
            z_layer_size,
            z,
            channel_width + 2 * edge_width,
        )
        mat_eroded = make_material(material_name, color_RGB_small_edge)
        layer_eroded_channel.data.materials.append(mat_eroded)
        layer_eroded_channel = Animated3DObject(layer_eroded_channel)

        # Fade in eroded channel layer at the same time as last small edge layer
        layer_eroded_channel.fade_in(frame_num(start_time), frame_num(end_time))
        # Adjust start and end times to do bulk dose for eroded channel layer
        start_time = end_time
        end_time = start_time + fadein_duration_seconds
        # Animate color change for bulk region
        layer_eroded_channel.animate_change_color(
            color_RGB_bulk, frame_num(start_time), frame_num(end_time)
        )

    elif i in secondary_image_roof_layers:

        # Create layers
        layer_roof = make_layer(
            layer_name, xy_layer_size, xy_layer_size, z_layer_size, z
        )
        layer_roof_bulk = make_channel_layer(
            layer_name,
            xy_layer_size,
            xy_layer_size,
            z_layer_size,
            z,
            channel_width + 2 * edge_width,
        )
        layer_roof_reduced_dose = make_layer(
            layer_name, xy_layer_size, channel_width + 2 * edge_width, z_layer_size, z,
        )

        # Make materials. All layer objects begin with the edge dose color
        mat_roof = make_material(material_name, color_RGB_edge)
        mat_roof_bulk = make_material(material_name, color_RGB_edge)
        mat_roof_reduced_dose = make_material(material_name, color_RGB_edge)
        layer_roof.data.materials.append(mat_roof)
        layer_roof_bulk.data.materials.append(mat_roof_bulk)
        layer_roof_reduced_dose.data.materials.append(mat_roof_reduced_dose)

        # Create animation objects for each layer object
        layer_roof = Animated3DObject(layer_roof)
        layer_roof_bulk = Animated3DObject(layer_roof_bulk)
        layer_roof_reduced_dose = Animated3DObject(layer_roof_reduced_dose)

        # Set initial conditions
        layer_roof_bulk.set_visible(False)
        layer_roof_bulk.set_opaque()
        layer_roof_reduced_dose.set_visible(False)
        layer_roof_reduced_dose.set_opaque()

        # Fade-in edge dose
        layer_roof.fade_in(frame_num(start_time), frame_num(end_time))

        # Adjust start and end times to do bulk dose
        start_time = end_time + time_between_layer_fadeins_seconds
        end_time = start_time + fadein_duration_seconds

        # Swap out layer channel for edge and eroded channel layers
        layer_roof.disappear_at_frame(frame_num(start_time))
        layer_roof_bulk.appear_at_frame(frame_num(start_time))
        layer_roof_reduced_dose.appear_at_frame(frame_num(start_time))

        # Animate color change for bulk region
        layer_roof_bulk.animate_change_color(
            color_RGB_bulk, frame_num(start_time), frame_num(end_time)
        )

    else:

        layer = make_layer(layer_name, xy_layer_size, xy_layer_size, z_layer_size, z)
        mat = make_material(material_name, color_RGB_bulk)
        layer.data.materials.append(mat)
        layer = Animated3DObject(layer)
        layer.set_visible(False)
        layer.grow_in_negative_z(frame_num(start_time), frame_num(end_time), z)

    start_time = end_time + time_between_layer_fadeins_seconds

# Set last frame to be rendered for animation
last_frame = frame_num(end_time + 0.3)
print(f"Last frame: {last_frame}")
bpy.data.scenes["Scene"].frame_end = last_frame
