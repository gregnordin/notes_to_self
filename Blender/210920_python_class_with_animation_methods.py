import bpy
from math import pi

light_location = (8.1524, 2.0110, 11.808)
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


def make_layer(name, x_layer_size, y_layer_size, z_layer_size, z_position):
    bpy.ops.mesh.primitive_cube_add(size=1)
    layer = bpy.context.object
    layer.scale = (x_layer_size, y_layer_size, z_layer_size)
    layer.location = (0, 0, z_layer_size / 2 + z_position)
    layer.name = name
    return layer


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


class Layer3DObject:
    def __init__(self):
        # Specify which type of layer object (bulk, channel, channel with edge, roof with reduced exposure region)
        # Use Factory Method design pattern to create objects?? And then initialize object with whatever parameters it needs?
        # Build layer object:
        # self.obj = ...
        # Record scale values:
        # self.save_scale = obj.scale  # .scale
        # Is alpha 0?
        # Is visible at start of animation? If no, set alpha to 0.
        # Fade-in assumes object starting state is fully transparent
        # Fade-out assumes the opposite
        pass

    def invisible(self):
        # Set scale to 0
        pass

    def visible(self):
        # Set scale to saved values
        pass

    def appear_at_frame(self, frame):
        #
        pass

    def disappear_at_frame(self, frame):
        #
        pass

    def fade_in(self, start_frame, end_frame):
        #
        pass

    def fade_out(self, start_frame, end_frame):
        #
        pass

    def set_transparency_value(self, value):
        #
        pass

    def set_fully_transparent(self):
        self.set_transparency_value(0.0)
        pass

    def set_least_transparent(self):
        self.set_transparency_value(1.0)
        pass


# Layers
xy_layer_size = 10
z_layer_size = 0.5
channel_width = 3
edge_width = 1
num_layers = 9

# Define colors
# Primary color - golden
color_RGB_default = (1, 0.71, 0.2)  # RGB (255, 180, 51) = #FFB433 hex
color_RGBA_default = (*color_RGB_default, 1)  # Includes alpha channel

light_sun = point_light()

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
cam.rotation_euler = [pi * 66.7 / 180, pi * 0.0 / 180, pi * 46.7 / 180]

z = 0.0
layer = make_layer("Test_Layer", xy_layer_size, xy_layer_size, z_layer_size, z)
mat = make_material_Principled_BSDF("Test_Material", color_RGB_default)
layer.data.materials.append(mat)
