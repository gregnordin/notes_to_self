import bpy
from math import pi


def point_light(location, rotation, power=1000.0, name="Light_pt"):
    """Point light.

    Args:
        power (float, optional): [description]. Defaults to 1000.0.
        name (str, optional): [description]. Defaults to "Light_pt".
        location ([type], optional): [description]. Defaults to light_location.
        rotation ([type], optional): [description]. Defaults to light_rotation.

    Returns:
        [type]: Light object
    """
    light_data = bpy.data.lights.new(name, type="POINT")
    light = bpy.data.objects.new(name, light_data)
    bpy.context.collection.objects.link(light)
    light.location = location
    light.rotation_euler = rotation
    light.data.energy = power
    return light


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


def area_light(
    location, rotation, power=800, size=5.0, name="Light_area",
):
    """Area light.

    Args:
        power (int, optional): [description]. Defaults to 800.
        size (float, optional): [description]. Defaults to 5.0.
        name (str, optional): [description]. Defaults to "Light_area".
        location ([type], optional): [description]. Defaults to light_location.
        rotation ([type], optional): [description]. Defaults to light_rotation.

    Returns:
        [type]: Light object
    """
    light_data = bpy.data.lights.new(name, type="AREA")
    light = bpy.data.objects.new(name, light_data)
    bpy.context.collection.objects.link(light)
    light.location = location
    light.rotation_euler = rotation
    light.data.energy = power
    light.data.specular_factor = 0.2
    light.data.shape = "SQUARE"
    light.data.size = size
    return light
