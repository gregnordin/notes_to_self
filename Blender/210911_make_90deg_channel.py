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


def make_layer(name, x_layer_size, y_layer_size, z_layer_size, z_position):
    bpy.ops.mesh.primitive_cube_add(size=1)
    layer = bpy.context.object
    layer.scale = (x_layer_size, y_layer_size, z_layer_size)
    layer.location = (0, 0, z_layer_size / 2 + z_position)
    layer.name = name
    print("layer from context object:", layer)
    return layer


# First try, but channel object is visible
def make_channel_layer(
    name, x_layer_size, y_layer_size, z_layer_size, z_position, channel_width
):
    # Make base layer object
    layer = make_layer(name, x_layer_size, y_layer_size, z_layer_size, z_position)

    # Create channel object. Oversize it a bit in x and z so we get a
    # clean difference operation because surfaces are not coincident.
    delta_x = 0.5
    delta_z = 0.2
    channel = make_layer(
        name + "_chan",
        x_layer_size + delta_x,
        channel_width,
        z_layer_size + delta_z,
        z_position - delta_z / 2,
    )

    # Add modifier to do a boolean difference between layer and channel
    mod = layer.modifiers.new("BoolDifference", type="BOOLEAN")
    mod.operation = "DIFFERENCE"
    mod.object = channel
    bpy.ops.object.modifier_apply(modifier=mod.name)

    # Make channel object not visible
    bpy.context.collection.objects.unlink(channel)

    return layer


def make_channel_layer2(
    name, x_layer_size, y_layer_size, z_layer_size, z_position, channel_width
):
    # Make base layer object
    layer = make_layer(name, x_layer_size, y_layer_size, z_layer_size, z_position)

    # Create channel object. Oversize it a bit in x and z so we get a
    # clean difference operation because surfaces are not coincident.
    delta_x = 0.5
    delta_z = 0.2
    bpy.ops.mesh.primitive_cube_add(size=1)
    channel = bpy.context.object
    channel.scale = (x_layer_size + delta_x, channel_width, z_layer_size + delta_z)
    channel.location = (0, 0, z_layer_size / 2 + z_position)
    channel.name = name + "_chan"

    # Add modifier to do a boolean difference between layer and channel
    mod = layer.modifiers.new("SomeName", type="BOOLEAN")
    mod.operation = "DIFFERENCE"
    mod.object = channel
    bpy.ops.object.modifier_apply(modifier=mod.name)

    # Make channel object to not be visible
    bpy.context.collection.objects.unlink(channel)

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
# channel_layer_indices = []

print()
for i, fp in enumerate(frame_pairs_for_layers):

    # Make layer object and material
    layer_str = f"{i:02d}"
    layer_name = f"Layer_{layer_str}"
    z = i * z_layer_size
    if i in channel_layer_indices:
        layer = make_channel_layer(
            layer_name, xy_layer_size, xy_layer_size, z_layer_size, z, channel_width
        )
    else:
        layer = make_layer(layer_name, xy_layer_size, xy_layer_size, z_layer_size, z)
    mat = make_material(f"Material_{layer_str}", start_color_RGBA, color_RGB)
    print(layer)
    # current_layer = layer  # bpy.data.objects[layer_name]
    layer.active_material = mat
    print(i, z, layer.scale, layer.location)

    # Start frame for layer
    mat.diffuse_color = start_color_RGBA
    mat.keyframe_insert(data_path="diffuse_color", frame=fp[0], index=-1)
    # End frame for layer
    mat.diffuse_color = final_color_RGBA
    mat.keyframe_insert(data_path="diffuse_color", frame=fp[1], index=-1)
print()
print("Finished")
