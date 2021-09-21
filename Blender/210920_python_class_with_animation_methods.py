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


# Get the render frames per second from the Blender file from which this python code file is executed
frames_per_second = bpy.data.scenes["Scene"].render.fps


def frame_number(time_seconds, frames_per_second=frames_per_second):
    """Utility function to calculate the frame number for a particular time
    given the anticipated frames per second for the animation.

    Args:
        time_seconds (float or int): time in seconds to convert to frames
        frames_per_second (float or int): number of frames per second in animation
    """
    return round(frames_per_second * time_seconds)


class Animated3DObject:
    def __init__(self, obj):
        # Specify which type of layer object (bulk, channel, channel with edge, roof with reduced exposure region)
        # Use Factory Method design pattern to create objects?? And then initialize object with whatever parameters it needs?
        # Build layer object:
        self.object = obj
        self.material = self.object.active_material
        self.material_nodes = self.material.node_tree.nodes
        self.material_alpha_param = self.material_nodes["Principled BSDF"].inputs[
            "Alpha"
        ]
        self.set_fully_transparent()
        # Record scale value. Must make a copy, otherwise self.save_scale just points to the object's scale:
        self.save_scale = self.object.scale.copy()

    def set_scale(self, value):
        # print(f"in set_scale...")
        # print("Before", self.object.scale, value)
        self.object.scale = value
        # print("After", self.object.scale, value)

    def set_visible(self, visibility_flag):
        if visibility_flag:
            self.set_scale(self.save_scale)
        else:
            new_scale = (0.0, 0.0, 0.0)
            self.set_scale(new_scale)

    def appear_at_frame(self, frame):
        # print(f"Appear at frame {frame}")
        self.set_visible(False)
        self.object.keyframe_insert(data_path="scale", frame=frame - 1)
        self.set_visible(True)
        self.object.keyframe_insert(data_path="scale", frame=frame)

    def disappear_at_frame(self, frame):
        # print(f"Disappear at frame {frame}")
        self.set_visible(True)
        self.object.keyframe_insert(data_path="scale", frame=frame - 1)
        self.set_visible(False)
        self.object.keyframe_insert(data_path="scale", frame=frame)

    def fade_in(self, start_frame, end_frame, initial_value=0.0, final_value=1.0):
        self.set_transparency_value(initial_value)
        self.material_alpha_param.keyframe_insert("default_value", frame=start_frame)
        self.set_transparency_value(final_value)
        self.material_alpha_param.keyframe_insert("default_value", frame=end_frame)

    def fade_out(self, start_frame, end_frame):
        self.fade_in(start_frame, end_frame, initial_value=1.0, final_value=0.0)

    def set_transparency_value(self, value):
        self.material_alpha_param.default_value = value

    def set_fully_transparent(self):
        self.set_transparency_value(0.0)

    def set_least_transparent(self):
        self.set_transparency_value(1.0)


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

test_layer = Animated3DObject(layer)

start_frame, end_frame = 5, 25
test_layer.fade_in(start_frame, end_frame)
test_layer.disappear_at_frame(end_frame + 20)
test_layer.appear_at_frame(end_frame + 40)
start_frame, end_frame = 80, 95
test_layer.fade_out(start_frame, end_frame)

# Set last frame to be rendered for animation
bpy.data.scenes["Scene"].frame_end = end_frame + 10
