import bpy

# Add blender file directory to the python path
import sys

blender_file_path = str(bpy.path.abspath("//"))
if blender_file_path not in sys.path:
    sys.path.append(blender_file_path)
# print()
# print(sys.path)

from my_blender_package.utilities import clean_up, update_camera


def make_layer(name, x_layer_size, y_layer_size, z_layer_size, z_position):
    bpy.ops.mesh.primitive_cube_add(size=1)
    layer = bpy.context.object
    layer.scale = (x_layer_size, y_layer_size, z_layer_size)
    layer.location = (0, 0, z_layer_size / 2 + z_position)
    layer.name = name
    print("layer from context object:", layer)
    return layer


clean_up(keep_materials=[], keep_objects=[])
# update_camera(bpy.data.objects["Camera"], distance=25.0)
# set_show_floor(False)

xy_layer_size = 10
z_layer_size = 0.5
channel_width = 3

# Define color with transparent and opaque RGBA versions
color_RGB = (1, 0.7, 0.2)  # golden
start_color_RGBA = (*color_RGB, 0)  # transparent
final_color_RGBA = (*color_RGB, 1)  # opaque
