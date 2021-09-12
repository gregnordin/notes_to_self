import bpy

# Add blender file directory to the python path
import sys

blender_file_path = str(bpy.path.abspath("//"))
if blender_file_path not in sys.path:
    sys.path.append(blender_file_path)
# print()
# print(sys.path)

from my_blender_package.utilities import clean_up, update_camera


def make_material(name, diffuse_color, specular_color):
    mat = bpy.data.materials.new(name)
    mat.diffuse_color = diffuse_color
    mat.specular_color = specular_color
    mat.blend_method = "BLEND"
    mat.use_backface_culling = True
    return mat


def make_layer(name, xy_layer_size, z_layer_size, z_position):
    layer_scale = (1, 1, z_layer_size / xy_layer_size)
    layer = bpy.ops.mesh.primitive_cube_add(
        size=xy_layer_size,
        scale=layer_scale,
        location=(0, 0, z_layer_size / 2 + z_position),
    )
    bpy.context.object.name = name
    return layer


def make_inner_corner(name, xy_layer_size, z_layer_size, z_position, channel_width):
    inner_corner_size = (xy_layer_size - channel_width) / 2
    layer_scale = (1, 1, z_layer_size / inner_corner_size)  # xy_layer_size)
    inner_corner_location = inner_corner_size + channel_width
    layer = bpy.ops.mesh.primitive_cube_add(
        size=inner_corner_size,
        scale=layer_scale,
        location=(
            inner_corner_location / 2,
            -inner_corner_location / 2,
            z_layer_size / 2 + z_position,
        ),
    )
    bpy.context.object.name = name
    return layer


clean_up(keep_materials=["Dots Stroke", "Material"], keep_objects=["Camera", "Light"])
update_camera(bpy.data.objects["Camera"], distance=25.0)
# set_show_floor(False)

xy_layer_size = 10
z_layer_size = 0.5
channel_width = 3

# Define color with transparent and opaque RGBA versions
color_RGB = (1, 0.7, 0.2)  # golden
start_color_RGBA = (*color_RGB, 0)  # transparent
final_color_RGBA = (*color_RGB, 1)  # opaque

# Create list of pairs of frames where keyframes will be inserted.
# The first frame in each pair is when a layer starts with alpha = 0
# and the second is when it finishes with alpha = 1.
start_frame = 5
num_fadein_frames = 15
num_frames_between_fadeins = 10
num_layers = 6
frame_pairs_for_layers = []
for i in range(num_layers):
    base_frame = start_frame + i * (num_fadein_frames + num_frames_between_fadeins)
    frame_pairs_for_layers.append((base_frame, base_frame + num_fadein_frames))
print(frame_pairs_for_layers)
# frame_pairs_for_layers = [(10, 25), (50, 65), (90, 105), (130, 145)]

channel_layer_indices = [1, 2, 3, 4]

for i, fp in enumerate(frame_pairs_for_layers):

    # Make layer object and material
    layer_str = f"{i:02d}"
    layer_name = f"Layer_{layer_str}"
    z = i * z_layer_size
    if i in channel_layer_indices:
        layer = make_inner_corner(
            layer_name, xy_layer_size, z_layer_size, z, channel_width
        )
    else:
        layer = make_layer(layer_name, xy_layer_size, z_layer_size, z)
    mat = make_material(f"Material_{layer_str}", final_color_RGBA, color_RGB)
    current_layer = bpy.data.objects[layer_name]
    current_layer.active_material = mat

    # Start frame for layer
    mat.diffuse_color = start_color_RGBA
    mat.keyframe_insert(data_path="diffuse_color", frame=fp[0], index=-1)
    # End frame for layer
    mat.diffuse_color = final_color_RGBA
    mat.keyframe_insert(data_path="diffuse_color", frame=fp[1], index=-1)

print("Finished")
