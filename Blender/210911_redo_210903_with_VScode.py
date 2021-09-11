import bpy


def clean_up():
    # Delete materials from last time script ran
    original_materials = ["Dots Stroke", "Material"]
    for mat in bpy.data.materials:
        print(mat.name)
        if mat.name not in original_materials:
            bpy.data.materials.remove(mat)
    # Delete objects from last time script ran
    keep_objects = ["Camera", "Light"]
    for obj in bpy.data.objects:
        if obj.name not in keep_objects:
            obj.select_set(True)
            bpy.ops.object.delete(use_global=False)


import mathutils


def update_camera(camera, focus_point=mathutils.Vector((0.0, 0.0, 0.0)), distance=10.0):
    """
    Focus the camera to a focus point and place the camera at a specific distance from that
    focus point. The camera stays in a direct line with the focus point. See
    https://blender.stackexchange.com/questions/100414/how-to-set-camera-location-in-the-scene-while-pointing-towards-an-object-with-a

    :param camera: the camera object
    :type camera: bpy.types.object
    :param focus_point: the point to focus on (default=``mathutils.Vector((0.0, 0.0, 0.0))``)
    :type focus_point: mathutils.Vector
    :param distance: the distance to keep to the focus point (default=``10.0``)
    :type distance: float
    """
    looking_direction = camera.location - focus_point
    rot_quat = looking_direction.to_track_quat("Z", "Y")

    camera.rotation_euler = rot_quat.to_euler()
    # Use * instead of @ for Blender <2.8
    camera.location = rot_quat @ mathutils.Vector((0.0, 0.0, distance))


def set_show_floor(visibility=True):
    # https://blender.stackexchange.com/questions/39631/hide-blenders-grid-floor-programmatically
    for a in bpy.data.window_managers[0].windows[0].screen.areas:
        if a.type == "VIEW_3D":
            for space in a.spaces:
                if space.type == "VIEW_3D":
                    space.show_floor = visibility


def make_material(name, diffuse_color, specular_color):
    mat = bpy.data.materials.new(name)
    mat.diffuse_color = diffuse_color
    mat.specular_color = specular_color
    mat.blend_method = "BLEND"
    mat.use_backface_culling = True
    return mat


def make_layer(name, xy_layer_size, z_layer_size, z_position):
    layer_scale = (1, 1, z_layer_size / xy_layer_size)
    layer = bpy.ops.mesh.primitive_cube_add(
        size=xy_layer_size,
        scale=layer_scale,
        location=(0, 0, z_layer_size / 2 + z_position),
    )
    bpy.context.object.name = name
    return layer


clean_up()
update_camera(bpy.data.objects["Camera"], distance=22.0)
# set_show_floor(False)

xy_layer_size = 10
z_layer_size = 0.5

# Define color with transparent and opaque RGBA versions
color_RGB = (1, 0.7, 0.2)  # golden
start_color_RGBA = (*color_RGB, 0)  # transparent
final_color_RGBA = (*color_RGB, 1)  # opaque

# Create list of pairs of frames where keyframes will be inserted.
# The first frame in each pair is when a layer starts with alpha = 0
# and the second is when it finishes with alpha = 1.
start_frame = 10
num_fadein_frames = 15
num_frames_between_fadeins = 20
num_layers = 5
frame_pairs_for_layers = []
for i in range(num_layers):
    base_frame = start_frame + i * (num_fadein_frames + num_frames_between_fadeins)
    frame_pairs_for_layers.append((base_frame, base_frame + num_fadein_frames))
print(frame_pairs_for_layers)
# frame_pairs_for_layers = [(10, 25), (50, 65), (90, 105), (130, 145)]

for i, fp in enumerate(frame_pairs_for_layers):

    # Make layer object and material
    layer_str = f"{i:02d}"
    layer_name = f"Layer_{layer_str}"
    layer = make_layer(layer_name, xy_layer_size, z_layer_size, i * z_layer_size)
    mat = make_material(f"Material_{layer_str}", final_color_RGBA, color_RGB)
    current_layer = bpy.data.objects[layer_name]
    current_layer.active_material = mat

    # Start frame for layer
    mat.diffuse_color = start_color_RGBA
    mat.keyframe_insert(data_path="diffuse_color", frame=fp[0], index=-1)
    # End frame for layer
    mat.diffuse_color = final_color_RGBA
    mat.keyframe_insert(data_path="diffuse_color", frame=fp[1], index=-1)

print("Finished")
