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


def make_layer(name, x_layer_size, y_layer_size, z_layer_size, z_position):
    bpy.ops.mesh.primitive_cube_add(size=1)
    layer = bpy.context.object
    layer.scale = (x_layer_size, y_layer_size, z_layer_size)
    layer.location = (0, 0, z_layer_size / 2 + z_position)
    layer.name = name
    print("layer from context object:", layer)
    return layer


# print("Starting...")
# print(bpy.data.scenes)
# print(bpy.context.window.scene)
# print(bpy.context.window.scene.view_layers)
# for i, s in enumerate(bpy.data.scenes):
#     print(i, s)
# print()
# print(bpy.data.scenes[0].view_layers)
# print(bpy.data.scenes[0].view_layers[0])
# print()

# print("Going into clean_up()...")
# clean_up()
# update_camera(bpy.data.objects["Camera"], distance=25.0)
# set_show_floor(False)

xy_layer_size = 10
z_layer_size = 0.5
channel_width = 3

# Define color with transparent and opaque RGBA versions
color_RGB = (1, 0.7, 0.2)  # golden
start_color_RGBA = (*color_RGB, 0)  # transparent
final_color_RGBA = (*color_RGB, 1)  # opaque

# Lights
light_location = (4.0762, 1.0055, 5.9039)
light_rotation = [pi * 37.3 / 180, pi * 3.16 / 180, pi * 107 / 180]

# Point light
def point_light(
    power=1000.0, name="Light_pt", location=light_location, rotation=light_rotation
):
    light_data = bpy.data.lights.new(name, type="POINT")
    light = bpy.data.objects.new(name, light_data)
    bpy.context.collection.objects.link(light)
    light.location = light_location
    light.rotation_euler = light_rotation
    light.data.energy = power
    return light


# Sun light
def sun_light(
    power=2.5,
    angle=135,
    name="Light_sun",
    location=light_location,
    rotation=light_rotation,
):
    light_data = bpy.data.lights.new(name, type="SUN")
    light = bpy.data.objects.new(name, light_data)
    bpy.context.collection.objects.link(light)
    light.location = light_location
    light.rotation_euler = light_rotation
    light.data.energy = power
    light.data.specular_factor = 0.4
    light.data.angle = angle * pi / 180.0
    return light


# Area light
def area_light(
    power=800,
    size=5.0,
    name="Light_area",
    location=light_location,
    rotation=light_rotation,
):
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


light_sun = sun_light()
# light_pt = point_light()
# light_area = area_light()
# light_area2 = area_light(power=1000, size=2.5, name="Light_area2")

# Camera
# we first create the camera object
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

# Material
mat = bpy.data.materials.new(name="Layer_material")
# Assign to layer
layer.data.materials.append(mat)
mat.use_nodes = True
# let's create a variable to store our list of nodes
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
