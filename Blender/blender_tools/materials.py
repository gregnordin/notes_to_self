import bpy


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


def make_material_Principled_and_Transparent_BSDF(name, color_RGB, mixing_factor=0.2):
    """Create a semi-transparent material with Pincipled BSDF, Transparent BSDF
    and a Mix Shader.

    Args:
        name (str): Name to give new material
        color_RGB (3-element tuple or list of floats): RGB color (each element is in range of 0.0 to 1.0))

    Returns:
        [type]: [description]
    """
    mat = bpy.data.materials.new(name=name)
    mat.use_nodes = True
    nodes = mat.node_tree.nodes
    node_prin = nodes["Principled BSDF"]
    node_output = nodes["Material Output"]

    # Set Principled BSDF values
    node_prin.inputs["Metallic"].default_value = 0.0
    node_prin.inputs["Roughness"].default_value = 0.4
    node_prin.inputs["Base Color"].default_value = (
        *color_RGB,
        1.0,
    )

    # Change material settings for blend method, show backface, shadow mode
    mat.blend_method = "BLEND"
    mat.show_transparent_back = False
    mat.shadow_method = "NONE"

    # Set up links shortcut & remove current links (there is only one)
    links = mat.node_tree.links
    links.remove(links[0])

    # Create new nodes
    node_tran = nodes.new(type="ShaderNodeBsdfTransparent")
    node_mix = nodes.new(type="ShaderNodeMixShader")

    # Position nodes so can easily see in Shading view in Blender
    node_prin.location = (-10, 350)
    node_tran.location = (50, 500)
    node_mix.location = (310, 430)
    node_output.location = (530, 300)

    # Create links between nodes
    link_mix_out = links.new(node_mix.outputs[0], node_output.inputs[0])
    link_prin_mix = links.new(node_prin.outputs[0], node_mix.inputs[1])
    link_tran_mix = links.new(node_tran.outputs[0], node_mix.inputs[2])

    # Set Mix Shader mixing factor
    # (0 is all Principled BSDF, 1 is all Transparent Shader)
    node_mix.inputs["Fac"].default_value = mixing_factor

    return mat

