import bpy


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


def frame_number(time_seconds, frames_per_second):
    """Utility function to calculate the frame number for a particular time
    given the anticipated frames per second for the animation.

    Args:
        time_seconds (float or int): time in seconds to convert to frames
        frames_per_second (float or int): number of frames per second in animation
    """
    return round(frames_per_second * time_seconds)
