import bpy


def make_layer(name, x_layer_size, y_layer_size, z_layer_size, z_position):
    bpy.ops.mesh.primitive_cube_add(size=1)
    layer = bpy.context.object
    layer.scale = (x_layer_size, y_layer_size, z_layer_size)
    layer.location = (0, 0, z_layer_size / 2 + z_position)
    layer.name = name
    return layer


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


def make_edge_layer(
    name,
    x_layer_size,
    y_layer_size,
    z_layer_size,
    z_position,
    channel_width,
    edge_width,
):
    """Create 3D edge layer object (2 strips on either side of a channel) by creating
    a channel layer object and subtracting a channel layer object where the channel is
    wider by 2 * edge_width (edge_width is the erosion amount when doing secondary images).

    Args:
        name (str): Object name
        x_layer_size (float or int): layer size in x
        y_layer_size (float or int): layer size in y
        z_layer_size (float or int): layer thickness
        z_position (float or int): position of bottom of layer
        channel_width (float or int): width of channel
        edge_width (float or int): width of each edge
    """
    layer_edge = make_channel_layer(
        name, x_layer_size, y_layer_size, z_layer_size, z_position, channel_width,
    )
    # Oversize the object to delete so that difference operation doesn't have to
    # deal with co-located surfaces.
    delta_xy = 0.3
    delta_z = 0.1
    object_to_delete = make_channel_layer(
        name,
        x_layer_size + delta_xy,
        y_layer_size + delta_xy,
        z_layer_size + delta_z,
        z_position - delta_z / 2,
        channel_width + 2 * edge_width,
    )
    # Add modifier to layer object to do a boolean difference between channel
    mod = layer_edge.modifiers.new("BoolDifferenceSecondary", type="BOOLEAN")
    mod.operation = "DIFFERENCE"
    mod.object = object_to_delete
    # Make layer_edge active to have right context to apply modifier
    bpy.context.view_layer.objects.active = layer_edge
    # Apply modifier, which performs difference operation
    bpy.ops.object.modifier_apply(modifier=mod.name)
    # Ensure object_to_delete is not visible
    bpy.context.collection.objects.unlink(object_to_delete)
    return layer_edge

