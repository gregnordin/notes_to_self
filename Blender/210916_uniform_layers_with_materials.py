import bpy
from math import pi

# Add blender file directory to the python path
import sys

blender_file_path = str(bpy.path.abspath("//"))
if blender_file_path not in sys.path:
    sys.path.append(blender_file_path)
# print()
# print(sys.path)

from my_blender_package.utilities import clean_up, update_camera


# ----------------------------------------------------------------------------------------
# Different types of light objects
# ----------------------------------------------------------------------------------------

light_location = (4.0762, 1.0055, 5.9039)
light_rotation = [pi * 37.3 / 180, pi * 3.16 / 180, pi * 107 / 180]


def point_light(
    power=1000.0, name="Light_pt", location=light_location, rotation=light_rotation
):
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
    light.location = light_location
    light.rotation_euler = light_rotation
    light.data.energy = power
    return light


def sun_light(
    power=2.5,
    angle=135,
    name="Light_sun",
    location=light_location,
    rotation=light_rotation,
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
    light.location = light_location
    light.rotation_euler = light_rotation
    light.data.energy = power
    light.data.specular_factor = 0.4
    light.data.angle = angle * pi / 180.0
    return light


def area_light(
    power=800,
    size=5.0,
    name="Light_area",
    location=light_location,
    rotation=light_rotation,
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
    light.location = light_location
    light.rotation_euler = light_rotation
    light.data.energy = power
    light.data.specular_factor = 0.2
    light.data.shape = "SQUARE"
    light.data.size = size
    return light


# ----------------------------------------------------------------------------------------
# Materials
# ----------------------------------------------------------------------------------------


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


# ----------------------------------------------------------------------------------------
# Animation helpers
# ----------------------------------------------------------------------------------------


def animate_object_transparency(
    obj, start_frame, end_frame, initial_value=0.0, final_value=1.0
):
    """Given an object with an active material that uses nodes and has a Principled BSDF node,
    create keyframes to animate the object's transparency (alpha value) from an initial to a
    final value.

    Args:
        obj (Blender object - bpy_types.Object): Object to animate transparency
        start_frame (int): Frame on which to start animation
        end_frame (int): Frame on which to end animation
        initial_value (float, optional): Starting alpha value. Defaults to 0.0.
        final_value (float, optional): Ending alpha value. Defaults to 1.0.
    """
    mat = obj.active_material
    mat_nodes = mat.node_tree.nodes
    mat_alpha_param = mat_nodes["Principled BSDF"].inputs["Alpha"]
    mat_alpha_param.default_value = initial_value
    mat_alpha_param.keyframe_insert("default_value", frame=start_frame)
    mat_alpha_param.default_value = final_value
    mat_alpha_param.keyframe_insert("default_value", frame=end_frame)


frames_per_second = 24


def frame_number(time_seconds, frames_per_second=frames_per_second):
    """Utility function to calculate the frame number for a particular time
    given the anticipated frames per second for the animation.

    Args:
        time_seconds (float or int): time in seconds to convert to frames
        frames_per_second (float or int): number of frames per second in animation
    """
    return round(frames_per_second * time_seconds)


# ----------------------------------------------------------------------------------------
# Layer objects
# ----------------------------------------------------------------------------------------


def make_layer(name, x_layer_size, y_layer_size, z_layer_size, z_position):
    bpy.ops.mesh.primitive_cube_add(size=1)
    layer = bpy.context.object
    layer.scale = (x_layer_size, y_layer_size, z_layer_size)
    layer.location = (0, 0, z_layer_size / 2 + z_position)
    layer.name = name
    print("layer from context object:", layer)
    return layer


# ----------------------------------------------------------------------------------------
# Main code
# ----------------------------------------------------------------------------------------


# set_show_floor(False)

# Layers
xy_layer_size = 10
z_layer_size = 0.5
channel_width = 3
num_layers = 6

# Define colors
color_RGB_default = (1, 0.7, 0.2)  # golden

# Lights
light_sun = sun_light()
# light_pt = point_light()
# light_area = area_light()
# light_area2 = area_light(power=1000, size=2.5, name="Light_area2")

# Camera
# create the camera object
cam_data = bpy.data.cameras.new("camera")
cam = bpy.data.objects.new("camera", cam_data)
bpy.context.collection.objects.link(cam)
# add camera to scene
scene = bpy.context.scene
scene.camera = cam
# position and rotate camera
cam.location = (16.344, -15.382, 11.012)
cam.rotation_euler = [pi * 63.9 / 180, pi * 0.0 / 180, pi * 46.7 / 180]

# Single layer
layer = make_layer(
    "Test_layer", xy_layer_size, xy_layer_size, z_layer_size, z_position=0.0
)
layer.data.materials.append(
    make_material_Principled_BSDF("Material_00", color_RGB_default)
)

start_frame = 1
end_time_seconds = 1.0
end_frame = frame_number(end_time_seconds)
print(start_frame, end_time_seconds, frames_per_second, end_frame)
animate_object_transparency(layer, start_frame, end_frame)
