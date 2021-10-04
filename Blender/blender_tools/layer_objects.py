import bpy
from .materials import make_material_Principled_BSDF


# ----------------------------------------------------------------------------------------
# Utility functions
# ----------------------------------------------------------------------------------------


def attach_to_parent(child_obj, parent_obj):
    """Make parent_obj the parent of child_obj.

    Args:
        child_obj (Blender object): Object to be the child
        parent_obj (Blender object): Object to be the parent
    """
    child_obj.parent = parent_obj
    # Prevent parent transforms from being applied to child object
    child_obj.matrix_parent_inverse = parent_obj.matrix_world.inverted()


def duplicate_object(obj, invert_y_position=True, parent_relationship=True):
    """Duplicate an object, move the duplicate in relation to the original,
    and make the original the parent object of the duplicate.

    Args:
        obj (Blender object): Object to duplicate
        invert_y_position (Boolean, optional): Whether to invert the y-position of
            the duplicated object. Defaults to True.
        parent (Boolean, optional): Make the original object the parent
            of the duplicate.
    """
    bpy.ops.object.duplicate()  # linked=True)
    obj_dupl = bpy.context.selected_objects[0]
    if invert_y_position:
        position = obj.location
        obj_dupl.location = (position[0], -position[1], position[2])
    if parent_relationship:
        attach_to_parent(obj_dupl, obj)


# ----------------------------------------------------------------------------------------
# General cube creation
# ----------------------------------------------------------------------------------------


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
# Specific layer creation
# ----------------------------------------------------------------------------------------


def make_bulk_layer(
    name,
    layer_size,
    color_RGB=None,
    z_position=0.0,
    parent=None,
    material=None,
    **kwargs,
):
    """Create a 3D print bulk layer.

    Args:
        name (str): Name to give the object.
        layer_size (3-element tuple or list of floats or ints): x,y,z size
        color_RGB (3-element tuple or list of floats): RGB color with each value
            in range 0.0-1.0.
        z_position (float, optional): Where to place object in z direction. 
            Defaults to 0.0.
        parent (Blender object, optional): Use this object as parent for new layer. 
            Defaults to None.

    Returns:
        Blender object: Newly created layer.
    """
    position = (0.0, 0.0, z_position)
    layer = make_cube(name, layer_size, position)
    if material is None:
        material = make_material_Principled_BSDF(f"{name}_mat", color_RGB)
    layer.data.materials.append(material)

    if parent:
        attach_to_parent(layer, parent)

    return layer


def make_channel_layer(
    name,
    layer_size,
    channel_width,
    color_RGB,
    z_position=0.0,
    parent=None,
    material=None,
    **kwargs,
):
    """Create a 3D print channel layer.

    Args:
        name (str): Name to give the object.
        layer_size (3-element tuple or list of floats or ints): x,y,z size
        channel_width (float or int): Width of channel.
        color_RGB (3-element tuple or list of floats): RGB color with each value
            in range 0.0-1.0.
        z_position (float, optional): Where to place object in z direction. 
            Defaults to 0.0.
        parent (Blender object, optional): Use this object as parent for new layer. 
            Defaults to None.

    Returns:
        Blender object: Newly created layer.
    """
    lx, ly, lz = layer_size
    c = channel_width

    size = (lx, ly / 2.0 - c / 2.0, lz)
    position = (0.0, -((ly / 2.0 - c / 2.0) / 2.0 + c / 2.0), z_position)
    layer_chan = make_cube(name, size, position)
    if material is None:
        material = make_material_Principled_BSDF(f"{name}_mat", color_RGB)
    layer_chan.data.materials.append(material)

    duplicate_object(layer_chan)

    if parent:
        attach_to_parent(layer_chan, parent)

    return layer_chan


def make_channelfill_layer(
    name, layer_size, channel_width, color_RGB, z_position=0.0, parent=None, **kwargs
):
    """Create a 3D print layer that consists of filled channel.

    Args:
        name (str): Name to give the object.
        layer_size (3-element tuple or list of floats or ints): x,y,z size
        channel_width (float or int): Width of channel.
        color_RGB (3-element tuple or list of floats): RGB color with each value
            in range 0.0-1.0.
        z_position (float, optional): Where to place object in z direction. 
            Defaults to 0.0.
        parent (Blender object, optional): Use this object as parent for new layer. 
            Defaults to None.

    Returns:
        Blender object: Newly created layer.
    """
    lx, ly, lz = layer_size
    c = channel_width

    size = (lx, c, lz)
    position = (0.0, 0.0, z_position)
    layer_chan = make_cube(name, size, position)
    mat = make_material_Principled_BSDF(f"{name}_mat", color_RGB)
    layer_chan.data.materials.append(mat)

    if parent:
        attach_to_parent(layer_chan, parent)

    return layer_chan


def make_channel_eroded_layer(
    name,
    layer_size,
    channel_width,
    edge_width,
    color_RGB,
    z_position=0.0,
    parent=None,
    **kwargs,
):
    """Create a 3D print eroded channel layer.

    Args:
        name (str): Name to give the object.
        layer_size (3-element tuple or list of floats or ints): x,y,z size
        channel_width (float or int): Width of channel.
        edge_width (float or int): Width of edge on each side of channel.
        color_RGB (3-element tuple or list of floats): RGB color with each value
            in range 0.0-1.0.
        z_position (float, optional): Where to place object in z direction. 
            Defaults to 0.0.
        parent (Blender object, optional): Use this object as parent for new layer. 
            Defaults to None.

    Returns:
        Blender object: Newly created layer.
    """
    return make_channel_layer(
        name,
        layer_size,
        channel_width + 2 * edge_width,
        color_RGB,
        z_position=z_position,
        parent=parent,
    )


def make_channel_edge_layer(
    name,
    layer_size,
    channel_width,
    edge_width,
    color_RGB,
    z_position=0.0,
    parent=None,
    **kwargs,
):
    """Create a 3D print layer with two edge objects at each side of a channel.

    Args:
        name (str): Name to give the object.
        layer_size (3-element tuple or list of floats or ints): x,y,z size
        channel_width (float or int): Width of channel.
        edge_width (float or int): Width of edge on each side of channel.
        color_RGB (3-element tuple or list of floats): RGB color with each value
            in range 0.0-1.0.
        z_position (float, optional): Where to place object in z direction. 
            Defaults to 0.0.
        parent (Blender object, optional): Use this object as parent for new layer. 
            Defaults to None.

    Returns:
        Blender object: Newly created layer.
    """
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

