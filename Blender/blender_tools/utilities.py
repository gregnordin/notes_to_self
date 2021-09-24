import bpy
import mathutils


def clean_up(keep_materials=None, keep_objects=None):
    """Delete materials and objects not in specified lists.

    Args:
        keep_materials ([type], optional): List of materials to not delete. Defaults to None.
        keep_objects ([type], optional): List of objects to not delete. Defaults to None.

    Example:
        clean_up(keep_materials=["Dots Stroke", "Material"], keep_objects=["Camera", "Light"])
    """
    print("Now in clean_up()...", keep_materials, keep_objects)

    if keep_materials is None:
        keep_materials = []
    if keep_objects is None:
        keep_objects = []

    # Delete materials not in list
    for mat in bpy.data.materials:
        print(mat.name)
        if mat.name not in keep_materials:
            bpy.data.materials.remove(mat)

    # print()
    # print(bpy.data.scenes[0].view_layers)
    # print(bpy.data.scenes[0].view_layers[0])
    # print()

    # Delete objects not in list
    for obj in bpy.data.objects:
        print(obj.name, obj)
        if obj.name not in keep_objects:
            # pass
            obj.select_set(
                True
            )  # , view_layer=bpy.data.scenes[0].view_layers[0]) # https://developer.blender.org/T66725
            bpy.ops.object.delete(use_global=True)  # False)


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
    """Show floor grid or not.

    Args:
        visibility (bool, optional): Whether to show the floor grid. Defaults to True.

    See https://blender.stackexchange.com/questions/39631/hide-blenders-grid-floor-programmatically
    """
    for a in bpy.data.window_managers[0].windows[0].screen.areas:
        if a.type == "VIEW_3D":
            for space in a.spaces:
                if space.type == "VIEW_3D":
                    space.show_floor = visibility
