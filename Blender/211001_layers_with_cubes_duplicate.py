import bpy
from math import pi

# ----------------------------------------------------------------------------------------
# Start - copied functions
# ----------------------------------------------------------------------------------------


def sun_light(
    location, rotation, power=2.5, angle=135, name="Light_sun",
):
    """Sun light.

    Args:
        power (float, optional): [description]. Defaults to 2.5.
        angle (int, optional): [description]. Defaults to 135.
        name (str, optional): [description]. Defaults to "Light_sun".
        location ([type], optional): [description]. Defaults to light_location.
        rotation ([type], optional): [description]. Defaults to light_rotation.

    Returns:
        [type]: Light object
    """
    light_data = bpy.data.lights.new(name, type="SUN")
    light = bpy.data.objects.new(name, light_data)
    bpy.context.collection.objects.link(light)
    light.location = location
    light.rotation_euler = rotation
    light.data.energy = power
    light.data.specular_factor = 0.4
    light.data.angle = angle * pi / 180.0
    return light


def make_material_Principled_BSDF(name, color_RGB):
    """Create a Pincipled BSDF material.

    Args:
        name (str): Name to give new material
        color_RGB (3-element tuple or list of floats): RGB color (each element is in range of 0.0 to 1.0))

    Returns:
        [type]: [description]
    """
    mat = bpy.data.materials.new(name=name)
    mat.use_nodes = True
    mat_nodes = mat.node_tree.nodes
    # Set Principled BSDF values
    mat_nodes["Principled BSDF"].inputs["Metallic"].default_value = 0.0
    mat_nodes["Principled BSDF"].inputs["Roughness"].default_value = 0.4
    mat_nodes["Principled BSDF"].inputs["Base Color"].default_value = (
        *color_RGB,
        1.0,
    )
    # Change material settings for blend method, show backface, shadow mode
    mat.blend_method = "BLEND"
    mat.show_transparent_back = False
    mat.shadow_method = "NONE"
    return mat


def make_cube(name, size, position):
    """Make cube with specified size and position. Ensure that the
    bottom of the cube is at the specified z position.
    
    Args:
        name (str): Name for new cube
        size (3-element tuple or list of floats): desired size of cube
        position (3-element tuple or list of floats): position of center bottom of cube
    """
    z_layer_size = size[2]
    z_position = position[2]

    bpy.ops.mesh.primitive_cube_add(size=1)
    layer = bpy.context.object
    layer.scale = size
    layer.location = (position[0], position[1], z_layer_size / 2 + z_position)
    layer.name = name
    return layer


# ----------------------------------------------------------------------------------------
# New functions
# ----------------------------------------------------------------------------------------


def attach_to_parent(child_obj, parent_obj):
    child_obj.parent = parent_obj
    # Do not apply parent transforms to child object
    child_obj.matrix_parent_inverse = parent_obj.matrix_world.inverted()


def duplicate_object(obj, invert_y_position=True):
    bpy.ops.object.duplicate()  # linked=True)
    obj_dupl = bpy.context.selected_objects[0]
    position = obj.location
    obj_dupl.location = (position[0], -position[1], position[2])
    # Make original object the parent of the duplicate
    attach_to_parent(obj_dupl, obj)


def make_bulk_layer(name, layer_size, color_RGB, z_position=0.0, parent=None):
    position = (0.0, 0.0, z_position)
    layer = make_cube(name, layer_size, position)
    mat = make_material_Principled_BSDF(f"{name}_mat", color_RGB_bulk)
    layer.data.materials.append(mat)

    if parent:
        attach_to_parent(layer, parent)

    return layer


def make_channel_layer(
    name, layer_size, channel_width, color_RGB, z_position=0.0, parent=None
):
    lx, ly, lz = layer_size
    c = channel_width

    size = (lx, ly / 2.0 - c / 2.0, lz)
    position = (0, -((ly / 2.0 - c / 2.0) / 2.0 + c / 2.0), z_position)
    layer_chan = make_cube(name, size, position)
    mat = make_material_Principled_BSDF(f"{name}_mat", color_RGB)
    layer_chan.data.materials.append(mat)

    duplicate_object(layer_chan)

    if parent:
        attach_to_parent(layer_chan, parent)

    return layer_chan


def make_channel_eroded_layer(
    name, layer_size, channel_width, edge_width, color_RGB, z_position=0.0, parent=None
):
    return make_channel_layer(
        name,
        layer_size,
        channel_width + 2 * edge_width,
        color_RGB,
        z_position=z_position,
        parent=parent,
    )


def make_channel_edge_layer(
    name, layer_size, channel_width, edge_width, color_RGB, z_position=0.0, parent=None
):
    lx, ly, lz = layer_size
    c = channel_width
    e = edge_width

    # Make edges
    size = (lx, e, lz)
    position = (0, -(c / 2.0 + e / 2.0), z_position)
    edge_name = f"{name}_edge"
    layer_edge = make_cube(edge_name, size, position)
    mat = make_material_Principled_BSDF(f"{edge_name}_mat", color_RGB)
    layer_edge.data.materials.append(mat)

    duplicate_object(layer_edge)

    if parent:
        attach_to_parent(layer_edge, parent)

    return layer_edge


# ----------------------------------------------------------------------------------------
# Main code
# ----------------------------------------------------------------------------------------

# Lights
light_location = (8.1524, 2.0110, 11.808)
light_rotation = [pi * 37.3 / 180, pi * 3.16 / 180, pi * 107 / 180]
light_sun = sun_light(location=light_location, rotation=light_rotation)

xy_layer_size = 10
z_layer_size = 0.5
channel_width = 3
edge_width = 1
color_RGB_bulk = (1, 0.71, 0.2)
color_RGB_channel = (0.1, 0.4, 0.7)
color_RGB_edge = (0.7, 0.1, 0.4)
color_RGB_eroded = (0.4, 0.7, 0.1)

size = (xy_layer_size, xy_layer_size, z_layer_size)
position = (0, 0, 0)

layer = make_bulk_layer("First Layer", size, color_RGB_bulk, z_position=0.0)
layer_chan = make_channel_layer(
    "Chan01", size, channel_width, color_RGB_channel, z_layer_size, parent=layer
)
layer_chan = make_channel_layer(
    "Chan02", size, channel_width, color_RGB_channel, 2 * z_layer_size, parent=layer
)
layer_top = make_bulk_layer(
    "Top Layer", size, color_RGB_bulk, z_position=3 * z_layer_size, parent=layer
)

z = 4 * z_layer_size
layer_edge = make_channel_edge_layer(
    "Edge01", size, channel_width, edge_width, color_RGB_edge, z, parent=layer
)
layer_eroded = make_channel_eroded_layer(
    "Eroded01", size, channel_width, edge_width, color_RGB_eroded, z, parent=layer
)
