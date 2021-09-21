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
    """Given a Blender 3D object, make it easy to do fade-in, fade-out, disappear,
    appear, and color change animations.

    Example usage:
        # Make an object with a material
        layer = make_layer("Test_Layer", xy_layer_size, xy_layer_size, z_layer_size, z)
        mat = make_material_Principled_BSDF("Test_Material", color_RGB_default)
        layer.data.materials.append(mat)

        # Try class animations
        test_layer = Animated3DObject(layer)
        start_frame, end_frame = 5, 25
        test_layer.fade_in(start_frame, end_frame)
        test_layer.disappear_at_frame(end_frame + 20)
        test_layer.appear_at_frame(end_frame + 40)
        test_layer.animate_change_color(color_RGBA_edge, end_frame + 50, end_frame + 65)
        start_frame, end_frame = end_frame + 80, end_frame + 95
        test_layer.fade_out(start_frame, end_frame)

    """

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
        # Color shortcut
        self.material_color_param = self.material_nodes["Principled BSDF"].inputs[
            "Base Color"
        ]
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

    def set_color(self, new_color):
        self.material_color_param.default_value = new_color

    def animate_change_color(self, new_color, start_frame, end_frame):
        current_color = self.material_color_param.default_value
        self.set_color(current_color)
        self.material_color_param.keyframe_insert("default_value", frame=start_frame)
        self.set_color(new_color)
        self.material_color_param.keyframe_insert("default_value", frame=end_frame)


# ----------------------------------------------------------------------------------------
# Layer objects
# ----------------------------------------------------------------------------------------


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


# ----------------------------------------------------------------------------------------
# Main code
# ----------------------------------------------------------------------------------------


# set_show_floor(False)

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
# Triadic color #1 - greenish
color_RGB_edge = (0.2, 1.0, 0.71)  # RGB (51, 255, 180) = HEX #33ffb4
color_RGBA_edge = (*color_RGB_edge, 1)  # Includes alpha channel
# Triadic color #2 - purple
# RGB (0.71, 0.2, 1.0) = (180, 51, 255) = HEX #b433ff

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
cam.location = (21.247, -19.997, 14.316)
cam.rotation_euler = [pi * 66.7 / 180, pi * 0.0 / 180, pi * 46.7 / 180]

# Select which case to run
case = "bulk"
# case = 'channel'
chan_layers = [2, 3, 4, 5]
# case = "channel with edge dose"
if case == "bulk":
    channel_layers = []
    secondary_image_channel_layers = []
elif case == "channel":
    channel_layers = chan_layers
    secondary_image_channel_layers = []
elif case == "channel with edge dose":
    channel_layers = []
    secondary_image_channel_layers = chan_layers

# Loop to create layers, materials, and keyframes
fadein_duration_seconds = 1.0
time_between_layer_fadeins_seconds = 0.5
start_time = 0.3
for i in range(num_layers):

    z = i * z_layer_size
    end_time = start_time + fadein_duration_seconds
    # print(i, z, start_time, end_time)

    layer_str = f"{i:02d}"
    layer_name = f"Layer_{layer_str}"
    material_name = f"Material_{layer_str}"

    if i in channel_layers:
        layer = make_channel_layer(
            layer_name, xy_layer_size, xy_layer_size, z_layer_size, z, channel_width
        )
        mat = make_material_Principled_BSDF(material_name, color_RGB_default)
        layer.data.materials.append(mat)
        animate_object_transparency(
            layer, frame_number(start_time), frame_number(end_time)
        )
    elif i in secondary_image_channel_layers:
        # Make primary image object with channel width = channel_width + edge_width
        # Make secondary image object
        #   Make layer object 2 with channel width = channel_width
        #   Make edge object as difference between layer object 2 and primary image object
        # Assign secondary color to primary and edge objects (or make identical materials with same color, one for each)
        # Keyframe animation fade-in for both objects by doing alpha keyframe for both materials
        # Assign primary color to primary object material
        # Keyframe animation primary object from secondary color to primary color

        # Create primary layer
        layer_primary = make_channel_layer(
            layer_name,
            xy_layer_size,
            xy_layer_size,
            z_layer_size,
            z,
            channel_width + 2 * edge_width,
        )

        # Create edge layer
        layer_edge = make_channel_layer(
            layer_name,
            xy_layer_size,
            xy_layer_size,
            z_layer_size,
            z,
            channel_width,
        )
        delta_xy = 0.3
        delta_z = 0.1
        object_to_delete = make_channel_layer(
            layer_name,
            xy_layer_size + delta_xy,
            xy_layer_size + delta_xy,
            z_layer_size + delta_z,
            z - delta_z / 2,
            channel_width + 2 * edge_width,
        )
        # Add modifier to do a boolean difference between layer and channel
        mod = layer_edge.modifiers.new("BoolDifferenceSecondary", type="BOOLEAN")
        mod.operation = "DIFFERENCE"
        mod.object = object_to_delete
        # layer_edge.select_set(True)
        bpy.context.view_layer.objects.active = layer_edge
        bpy.ops.object.modifier_apply(modifier=mod.name)
        # Make channel object not visible
        bpy.context.collection.objects.unlink(object_to_delete)

        mat_primary = make_material_Principled_BSDF(material_name, color_RGB_edge)
        layer_primary.data.materials.append(mat_primary)
        animate_object_transparency(
            layer_primary, frame_number(start_time), frame_number(end_time)
        )
        mat_secondary = make_material_Principled_BSDF(material_name, color_RGB_edge)
        layer_edge.data.materials.append(mat_secondary)
        animate_object_transparency(
            layer_edge, frame_number(start_time), frame_number(end_time)
        )

        start_time = end_time + time_between_layer_fadeins_seconds
        end_time = start_time + fadein_duration_seconds
        mat = layer_primary.active_material
        mat_nodes = mat.node_tree.nodes
        mat_color_param = mat_nodes["Principled BSDF"].inputs["Base Color"]
        mat_color_param.default_value = color_RGBA_edge
        mat_color_param.keyframe_insert("default_value", frame=frame_number(start_time))
        mat_color_param.default_value = color_RGBA_default
        mat_color_param.keyframe_insert("default_value", frame=frame_number(end_time))
    else:
        layer = make_layer(layer_name, xy_layer_size, xy_layer_size, z_layer_size, z)
        mat = make_material_Principled_BSDF(material_name, color_RGB_default)
        layer.data.materials.append(mat)
        layer = Animated3DObject(layer)
        layer.fade_in(frame_number(start_time), frame_number(end_time))
        # animate_object_transparency(
        #     layer, frame_number(start_time), frame_number(end_time)
        # )

    start_time = end_time + time_between_layer_fadeins_seconds

# Set last frame to be rendered for animation
last_frame = frame_number(end_time + 0.3)
print(f"Last frame: {last_frame}")
bpy.data.scenes["Scene"].frame_end = last_frame
