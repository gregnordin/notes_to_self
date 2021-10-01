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


class AnimateZMotion:
    def __init__(self, obj):
        self.object = obj

    def animate_z_move(
        self, start_time, end_time, delta_z, move_in_negative_z_direction=True
    ):
        sign = -1.0 if move_in_negative_z_direction else 1.0
        # Start and end locations
        current_location = self.object.location
        new_location = (
            current_location[0],
            current_location[1],
            current_location[2] + sign * delta_z,
        )

        # Keyframe current location to begin move
        self.object.keyframe_insert(data_path="location", frame=frame_num(start_time))

        # Keyframe new location to end move
        self.object.location = new_location
        self.object.keyframe_insert(data_path="location", frame=frame_num(end_time))


# class MixinZMotion:
#     def grow_in_negative_z(self, start_frame, end_frame, z_position=0.0):
#         # Assumes self.object.scale is already (0, 0, 0)

#         # Make layer appear at frame start_frame
#         self.object.keyframe_insert(data_path="scale", frame=start_frame - 1)
#         xy_scale = (self.save_scale[0], self.save_scale[1], 0)
#         self.set_scale(xy_scale)
#         self.object.keyframe_insert(data_path="scale", frame=start_frame)

#         # Set up keyframes to start growing in -z
#         self.object.keyframe_insert(data_path="scale", frame=start_frame)
#         self.object.keyframe_insert(data_path="location", frame=start_frame)

#         # Set up values and keyframes to define end of growth in -z
#         self.set_scale(self.save_scale)
#         new_location = (
#             self.save_location[0],
#             self.save_location[1],
#             z_position,  # - self.save_scale[2] / 2,
#         )
#         self.object.location = new_location
#         self.object.keyframe_insert(data_path="scale", frame=end_frame)
#         self.object.keyframe_insert(data_path="location", frame=end_frame)


# ----------------------------------------------------------------------------------------
# Animation classes
# ----------------------------------------------------------------------------------------


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
# Select which layer material type by uncommenting one of the following 2 lines
make_material = make_material_Principled_BSDF
# make_material = make_material_Principled_and_Transparent_BSDF
# Emissive material
make_LED_material = partial(
    make_semitransparent_emission_shader, strength=5, mix_fac=0.6
)


# Select which case to run by uncommenting one of the following 5 lines
# case = "bulk"
case = "channel"
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
grow_duration = 1.4
extra_time_LED_is_on = 0.5
move_down_delay = extra_time_LED_is_on + 0.2
move_down_duration = 0.6
between_layer_delay = 0.8
start_time = 0.3

for i in range(num_layers):

    z = i * z_layer_size - z_layer_size / 2
    end_time = start_time + grow_duration
    # print(i, z, start_time, end_time)

    layer_str = f"{i:02d}"
    layer_name = f"Layer_{layer_str}"
    if i == 0:
        parent_layer = make_bulk_layer(layer_name, layer_size, color_RGB_bulk)
        z_animation = AnimateZMotion(parent_layer)
    else:
        layer = make_bulk_layer(
            layer_name, layer_size, color_RGB_bulk, parent=parent_layer
        )

    z_animation.animate_z_move(start_time, end_time, z_layer_size)

    start_time = end_time + between_layer_delay

# Set last frame to be rendered for animation
last_frame = frame_num(end_time + 0.3)
print(f"Last frame: {last_frame}")
bpy.data.scenes["Scene"].frame_end = last_frame
