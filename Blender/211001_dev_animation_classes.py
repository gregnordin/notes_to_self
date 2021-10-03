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

# Import things from my Blender package
from blender_tools.lights import sun_light
from blender_tools.materials import (
    make_material_Principled_BSDF,
    make_semitransparent_emission_shader,
)
from blender_tools.layer_objects import (
    make_bulk_layer,
    make_channel_layer,
    make_channelfill_layer,
    make_channel_eroded_layer,
    make_channel_edge_layer,
)
from blender_tools.animation import frame_number

# ----------------------------------------------------------------------------------------
# Animation helpers
# ----------------------------------------------------------------------------------------


class MixinScale:
    """Methods to set the visibility of an object on and off by changing its
    scale from its original value to (0, 0, 0) (turn visibility off) or vice 
    versa (turn visibility on).
    """

    def _initialize_scale(self):
        self.original_scale = self.object.scale.copy()
        self._invisible_scale_value = (0.0, 0.0, 0.0)
        self.set_visible(False)

    def set_scale(self, value):
        self.object.scale = value

    def set_visible(self, visibility_flag):
        """Set whether object is visible or not.

        Args:
            visibility_flag (Boolean): True = visible, False = not visible.
        """
        # TODO: check for existence of self.original_scale and give helpful error message if doesn't exist
        if visibility_flag:
            self.set_scale(self.original_scale)
        else:
            self.set_scale(self._invisible_scale_value)

    def is_visible(self):
        if self.object.scale == self._invisible_scale_value:
            return False
        return True

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


class MixinGrowInZ:
    """Relies on MixinScale so new class must inherit from both.
    """

    def _initialize_location(self):
        self.original_location = self.object.location.copy()

    def grow_in_negative_z(self, start_frame, end_frame, z_position=0.0):
        # Assumes self.object.scale is already (0, 0, 0). Double check to make sure it's true.
        if not self.is_visible():
            raise ValueError(
                f"Before growing layer in z, it must be invisible (scale={self._invisible_scale_value})"
            )

        # Make layer appear at frame start_frame with zero thickness
        self.object.keyframe_insert(data_path="scale", frame=start_frame - 1)
        xy_scale = (self.original_scale[0], self.original_scale[1], 0)
        self.set_scale(xy_scale)
        self.object.keyframe_insert(data_path="scale", frame=start_frame)

        # Set up keyframes to start growing in -z
        self.object.keyframe_insert(data_path="scale", frame=start_frame)
        self.object.keyframe_insert(data_path="location", frame=start_frame)

        # Set up values and keyframes to define end of growth in -z
        self.set_scale(self.original_scale)
        new_location = (
            self.original_location[0],
            self.original_location[1],
            z_position,  # - self.original_location[2] / 2,
        )
        self.object.location = new_location
        self.object.keyframe_insert(data_path="scale", frame=end_frame)
        self.object.keyframe_insert(data_path="location", frame=end_frame)


class MixinColorAnimation:
    def _initialize_color_for_animation(self):
        self.material = self.object.active_material
        self.nodes = self.material.node_tree.nodes
        self.material_color = self.nodes["Principled BSDF"].inputs["Base Color"]

    def set_color(self, new_color):
        # If receive an RGB color, convert to RGBA
        if len(new_color) == 3:
            new_color = (*new_color, 1.0)
        # Make sure we have an RGBA color
        assert len(new_color) == 4
        self.material_color.default_value = new_color

    def animate_change_color(self, new_color, start_frame, end_frame):
        current_color = self.material_color.default_value
        self.set_color(current_color)
        self.material_color.keyframe_insert("default_value", frame=start_frame)
        self.set_color(new_color)
        self.material_color.keyframe_insert("default_value", frame=end_frame)


# ----------------------------------------------------------------------------------------
# Animation classes
# ----------------------------------------------------------------------------------------


class AnimateLayer(MixinScale, MixinGrowInZ):
    def __init__(self, obj):
        self.object = obj
        self._initialize_scale()
        self._initialize_location()


class AnimateZMotion:
    def __init__(self, obj):
        self.object = obj

    def animate_z_move(self, start_time, end_time, delta_z):
        # Start and end locations
        current_location = self.object.location
        new_location = (
            current_location[0],
            current_location[1],
            current_location[2] + delta_z,
        )

        # Keyframe current location to begin move
        self.object.keyframe_insert(data_path="location", frame=frame_num(start_time))

        # Keyframe new location to end move
        self.object.location = new_location
        self.object.keyframe_insert(data_path="location", frame=frame_num(end_time))


# ----------------------------------------------------------------------------------------
# Main code
# ----------------------------------------------------------------------------------------


# Set up Rendering to use bloom
bpy.context.scene.eevee.use_bloom = True
bpy.data.scenes["Scene"].eevee.bloom_intensity = 0.1

# Layers
xy_layer_size = 10
z_layer_size = 0.5
layer_size = (xy_layer_size, xy_layer_size, z_layer_size)
z_size_illum = 15
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
cam.rotation_euler = [pi * 59.9 / 180, pi * 0.0 / 180, pi * 46.7 / 180]

# Materials
make_material = make_material_Principled_BSDF
# Emissive material
make_LED_material = partial(
    make_semitransparent_emission_shader, strength=5, mix_fac=0.6
)


# Select which case to run by uncommenting one of the following 5 lines
# case = "bulk"
# case = "channel"
case = "channel with edge dose"
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

# Set up timing parameters
timings = {
    "start time": 0.3,
    "end time": None,
    "grow duration": 0.4,
    "extra time LED is on": 0.3,
    "move down delay after LED": 0.2,
    "move down duration": 0.6,
    "between layer delay": 0.2,
}
t = timings  # Need shorthand for timings to reduce clutter

# Loop to create layers and corresponding animation
for i in range(num_layers):
    t["end time"] = t["start time"] + t["grow duration"]
    # Make layer
    layer_str = f"{i:02d}"
    layer_name = f"Layer_{layer_str}"
    if i == 0:
        # Parent layer
        layer = make_bulk_layer(layer_name, layer_size, color_RGB_bulk)
        z_animation = AnimateZMotion(layer)
    elif i in channel_layers:
        layer = make_channel_layer(
            layer_name,
            layer_size,
            channel_width,
            color_RGB_bulk,
            parent=z_animation.object,
        )
    elif i in secondary_image_channel_layers:
        layer = make_channel_edge_layer(
            layer_name,
            layer_size,
            channel_width,
            edge_width,
            color_RGB_edge,
            parent=z_animation.object,
        )
    else:
        layer = make_bulk_layer(
            layer_name, layer_size, color_RGB_bulk, parent=z_animation.object
        )
    # Animate layer
    layer_animator = AnimateLayer(layer)
    layer_animator.grow_in_negative_z(
        frame_num(t["start time"]), frame_num(t["end time"])
    )

    # New start & end time for moving layers down
    t["start time"] = (
        t["end time"] + t["extra time LED is on"] + t["move down delay after LED"]
    )
    t["end time"] = t["start time"] + t["move down duration"]

    z_animation.animate_z_move(t["start time"], t["end time"], -z_layer_size)

    t["start time"] = t["end time"] + t["between layer delay"]

# Set last frame to be rendered for animation
last_frame = frame_num(t["end time"] + 0.3)
print(f"Last frame: {last_frame}")
bpy.data.scenes["Scene"].frame_end = last_frame
