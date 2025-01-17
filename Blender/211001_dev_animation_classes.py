import bpy
from math import pi
from functools import partial

# Add blender file directory to the python path
import sys

blender_file_path = str(bpy.path.abspath("//"))
if blender_file_path not in sys.path:
    sys.path.append(blender_file_path)
# print()
# print(sys.path)

# Import things from my Blender package
from blender_tools.lights import sun_light
from blender_tools.materials import (
    make_material_Principled_BSDF,
    make_semitransparent_emission_shader,
)
from blender_tools.layer_objects import (
    make_bulk_layer,
    make_channel_layer,
    make_channelfill_layer,
    make_channel_eroded_layer,
    make_channel_edge_layer,
)
from blender_tools.animation import frame_number

# ----------------------------------------------------------------------------------------
# Animation helpers
# ----------------------------------------------------------------------------------------


class MixinScale:
    """Methods to set the visibility of an object on and off by changing its
    scale from its original value to (0, 0, 0) (turn visibility off) or vice 
    versa (turn visibility on).
    """

    def _initialize_scale(self):
        self.original_scale = self.object.scale.copy()
        self._invisible_scale_value = (0.0, 0.0, 0.0)
        self.set_visible(False)

    def set_scale(self, value):
        self.object.scale = value

    def set_visible(self, visibility_flag):
        """Set whether object is visible or not.

        Args:
            visibility_flag (Boolean): True = visible, False = not visible.
        """
        # TODO: check for existence of self.original_scale and give helpful error message if doesn't exist
        if visibility_flag:
            self.set_scale(self.original_scale)
        else:
            self.set_scale(self._invisible_scale_value)

    def is_visible(self):
        if self.object.scale == self._invisible_scale_value:
            return False
        return True

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


class MixinGrowInZ:
    """Relies on MixinScale so new class must inherit from MixinScale and
    MixinGrowInZ. Grows a layer in -z direction starting from a 2D layer at
    z = 0.0, ending up with a 3D layer with thickness z_layer_size
    positioned at z = z_layer_size/2 such that the layer extends in z from
    0.0 to -z_layer_size
    """

    def _initialize_grow_in_z(self):
        self._initialize_scale()
        self.original_location = self.object.location.copy()
        self.z_layer_size = self.original_scale[2]
        self.starting_location = (
            self.original_location[0],
            self.original_location[1],
            0.0,
        )
        self.ending_location = (
            self.original_location[0],
            self.original_location[1],
            -self.z_layer_size / 2.0,
        )
        self.starting_scale = (self.original_scale[0], self.original_scale[1], 0)
        self.ending_scale = self.original_scale

        # Must set location to final location so that objects that do not
        # grow in negative z will be in correct position when they appear
        self.object.location = self.ending_location

    def grow_in_negative_z(self, start_frame, end_frame):

        # Make layer appear at frame start_frame with zero thickness
        self.object.location = self.starting_location
        self.object.keyframe_insert(data_path="scale", frame=start_frame - 1)
        self.set_scale(self.starting_scale)
        self.object.keyframe_insert(data_path="scale", frame=start_frame)

        # Set up keyframes to start growing in -z
        self.object.keyframe_insert(data_path="scale", frame=start_frame)
        self.object.keyframe_insert(data_path="location", frame=start_frame)

        # Set up values and keyframes to define end of growth in -z
        self.set_scale(self.ending_scale)
        self.object.location = self.ending_location
        self.object.keyframe_insert(data_path="scale", frame=end_frame)
        self.object.keyframe_insert(data_path="location", frame=end_frame)


class MixinColorAnimation:
    def _initialize_color_for_animation(self):
        self.material = self.object.active_material
        self.nodes = self.material.node_tree.nodes
        self.material_color = self.nodes["Principled BSDF"].inputs["Base Color"]

    def set_color(self, new_color):
        # If receive an RGB color, convert to RGBA
        if len(new_color) == 3:
            new_color = (*new_color, 1.0)
        # Make sure we have an RGBA color
        assert len(new_color) == 4
        self.material_color.default_value = new_color

    def animate_change_color(self, new_color, start_frame, end_frame):
        current_color = self.material_color.default_value
        self.set_color(current_color)
        self.material_color.keyframe_insert("default_value", frame=start_frame)
        self.set_color(new_color)
        self.material_color.keyframe_insert("default_value", frame=end_frame)


# ----------------------------------------------------------------------------------------
# Timings class
# ----------------------------------------------------------------------------------------
class Timings:
    def __init__(self):
        self.start_time = 0.3
        self.end_time = self.start_time
        self.duration_z_grow = 0.8
        self.color_c0_to_c1 = 0.5
        self.color_c1_to_c2 = 0.5
        self.delay_move_down_after_LED = 0.2
        self.duration_move_down = 0.6
        self.delay_between_layers = 0.4
        self.delay_between_switch_LED_patterns = 0.1
        self.duration_small_z_grow = self.duration_z_grow / 3.0  # 0.4
        self.delay_between_small_layers = 0.3
        self.duration_move_down_small_z = 0.3

    def update_start_time(self, delay_t=0.0):
        """Make new start time as sum of old end time and a time delay.

        Args:
            delay_t (float, optional): Delay time. Defaults to 0.0.
        """
        self.start_time = self.end_time + delay_t

    def update_end_time(self, delay_t=0.0):
        """Make new end time as sum of start time and a time delay.

        Args:
            delay_t (float, optional): Delay time. Defaults to 0.0.
        """
        self.end_time = self.start_time + delay_t

    def increase_end_time(self, delta_t=0.0):
        """Add delta_t to end_time.

        Args:
            delta_t (float, optional): time increment. Defaults to 0.0.
        """
        self.end_time = self.end_time + delta_t

    def set_delay_between_switch_LED_patterns(self):
        self.increase_end_time(self.delay_between_switch_LED_patterns)

    def update_start_and_end_time(self, delta_t_start=0.0, delta_t_end=0.0):
        self.update_start_time(delta_t_start)
        self.update_end_time(delta_t_end)

    def prep_grow_in_z(self):
        self.update_start_and_end_time(self.delay_between_layers, self.duration_z_grow)

    def prep_color_c0_to_c1(self):
        self.update_start_and_end_time(0.0, self.color_c0_to_c1)

    def prep_color_c1_to_c2(self):
        self.update_start_and_end_time(0.0, self.color_c1_to_c2)

    def prep_animate_z_move(self):
        self.update_start_and_end_time(
            self.delay_move_down_after_LED, self.duration_move_down
        )

    def prep_grow_in_z_small_layer(self):
        self.update_start_and_end_time(
            self.delay_between_small_layers, self.duration_small_z_grow
        )

    def prep_animate_z_move_small(self):
        self.update_start_and_end_time(
            self.delay_move_down_after_LED, self.duration_move_down_small_z
        )

    def prep_grow_in_z_last_small_layer(self):
        self.prep_grow_in_z_small_layer()
        self.save_start_time = self.start_time

    def prep_grow_in_z_last_small_layer_eroded_channel(self):
        self.start_time = self.save_start_time
        self.update_end_time(self.duration_z_grow)


# ----------------------------------------------------------------------------------------
# Animation classes
# ----------------------------------------------------------------------------------------


class AnimateAppearDisappear(MixinScale):
    def __init__(self, obj):
        self.object = obj
        self._initialize_scale()


class AnimateLayer(MixinScale, MixinGrowInZ, MixinColorAnimation):
    def __init__(self, obj):
        self.object = obj
        self._initialize_grow_in_z()
        self._initialize_color_for_animation()


class AnimateChannelWithSmallEdgesLayer:
    def __init__(self, layer_params, timings, colors, LED_animators, z_animator=None):

        self.layer_params = layer_params
        self.timings = timings
        self.colors = colors
        self.z_layer_size = self.layer_params["layer_size"][2]
        self.z_layer_size_small = self.z_layer_size / 3.0

        if z_animator:  # If parent object exists...
            # Move parent object down in z, which moves all of its children too
            self.z_animator = z_animator
            self.timings.prep_animate_z_move()
            self.z_animator.animate_z_move(
                self.timings.start_time,
                self.timings.end_time,
                -self.z_layer_size_small,
            )
        else:
            raise ValueError(
                "AnimateChannelWithEdgeLayer: must provide a z_animator function argument"
            )

        layer_size_small = (
            self.layer_params["layer_size"][0],
            self.layer_params["layer_size"][1],
            self.z_layer_size_small,
        )

        # Small edge LED
        self.channel_LED_animator = LED_animators["LED channel"]
        self.edge_LED_animator = LED_animators["LED channel edge"]
        self.eroded_LED_animator = LED_animators["LED eroded channel"]
        # self.eroded_LED_animator.set_visible(False)

        # Do first small edge layer -------------------------------------------------------
        # Small edge object
        self.chan_edge_1 = AnimateLayer(
            make_channel_edge_layer(
                name=self.layer_params["name"] + "_edge_small_1",
                layer_size=layer_size_small,
                channel_width=self.layer_params["channel_width"],
                edge_width=self.layer_params["edge_width"],
                color_RGB=self.layer_params["color_RGB"],
                parent=z_animator.object,
            )
        )
        # Animate first small edge layer
        self.chan_edge_1.set_color(self.colors[0])
        self.timings.prep_grow_in_z_small_layer()
        self.edge_LED_animator.appear_at_frame(frame_num(self.timings.start_time))
        self.chan_edge_1.grow_in_negative_z(
            frame_num(self.timings.start_time), frame_num(self.timings.end_time)
        )
        self.edge_LED_animator.disappear_at_frame(frame_num(self.timings.end_time))

        # Do second small edge layer -------------------------------------------------------
        # First move parent object down in z
        self.timings.prep_animate_z_move_small()
        self.z_animator.animate_z_move(
            self.timings.start_time, self.timings.end_time, -self.z_layer_size_small,
        )
        # Small edge object
        self.chan_edge_2 = AnimateLayer(
            make_channel_edge_layer(
                name=self.layer_params["name"] + "_edge_small_2",
                layer_size=layer_size_small,
                channel_width=self.layer_params["channel_width"],
                edge_width=self.layer_params["edge_width"],
                color_RGB=self.layer_params["color_RGB"],
                parent=z_animator.object,
            )
        )
        # Animate second small edge layer
        self.chan_edge_2.set_color(self.colors[0])
        self.timings.prep_grow_in_z_small_layer()
        self.edge_LED_animator.appear_at_frame(frame_num(self.timings.start_time))
        self.chan_edge_2.grow_in_negative_z(
            frame_num(self.timings.start_time), frame_num(self.timings.end_time)
        )
        self.edge_LED_animator.disappear_at_frame(frame_num(self.timings.end_time))

        # Do third small edge layer -------------------------------------------------------
        # First move parent object down in z
        self.timings.prep_animate_z_move_small()
        self.z_animator.animate_z_move(
            self.timings.start_time, self.timings.end_time, -self.z_layer_size_small,
        )
        # Small edge object
        self.chan_edge_3 = AnimateLayer(
            make_channel_edge_layer(
                name=self.layer_params["name"] + "_edge_small_3",
                layer_size=layer_size_small,
                channel_width=self.layer_params["channel_width"],
                edge_width=self.layer_params["edge_width"],
                color_RGB=self.layer_params["color_RGB"],
                parent=z_animator.object,
            )
        )
        # Eroded channel layer object
        name_save = layer_params["name"]
        layer_params["name"] = name_save + "_eroded"
        layer_chan_eroded = make_channel_eroded_layer(
            **layer_params, parent=z_animator.object
        )
        self.chan_eroded = AnimateLayer(layer_chan_eroded)
        layer_params["name"] = name_save

        # Animate small edge layer and eroded layer
        self.timings.prep_grow_in_z_last_small_layer()
        self.chan_edge_3.grow_in_negative_z(
            frame_num(self.timings.start_time), frame_num(self.timings.end_time)
        )
        self.chan_eroded.set_color(self.colors[0])
        self.timings.prep_grow_in_z_last_small_layer_eroded_channel()
        self.channel_LED_animator.appear_at_frame(frame_num(self.timings.start_time))
        self.chan_eroded.grow_in_negative_z(
            frame_num(self.timings.start_time), frame_num(self.timings.end_time)
        )
        self.channel_LED_animator.disappear_at_frame(frame_num(self.timings.end_time))

        self.timings.set_delay_between_switch_LED_patterns()

        self.timings.prep_color_c0_to_c1()
        self.eroded_LED_animator.appear_at_frame(frame_num(self.timings.start_time))
        self.chan_eroded.animate_change_color(
            self.colors[1],
            frame_num(self.timings.start_time),
            frame_num(self.timings.end_time),
        )
        # self.eroded_LED_animator.disappear_at_frame(frame_num(self.timings.end_time))

        self.timings.prep_color_c1_to_c2()
        # self.eroded_LED_animator.appear_at_frame(frame_num(self.timings.start_time))
        self.chan_eroded.animate_change_color(
            self.colors[2],
            frame_num(self.timings.start_time),
            frame_num(self.timings.end_time),
        )
        self.eroded_LED_animator.disappear_at_frame(frame_num(self.timings.end_time))


class AnimateRoofLayer:
    def __init__(self, layer_params, timings, colors, LED_animators, z_animator=None):

        self.layer_params = layer_params
        self.timings = timings
        self.colors = colors
        self.z_layer_size = self.layer_params["layer_size"][2]

        if z_animator:  # If parent object exists...
            # Move parent object down in z, which moves all of its children too
            self.z_animator = z_animator
            self.timings.prep_animate_z_move()
            self.z_animator.animate_z_move(
                self.timings.start_time, self.timings.end_time, -self.z_layer_size
            )
        else:
            raise ValueError(
                "AnimateRoofLayer: must provide a z_animator function argument"
            )

        # Make required animator objects
        name_save = layer_params["name"]
        layer_params["name"] = name_save + "_bulk"
        layer_bulk = make_bulk_layer(**layer_params, parent=z_animator.object)
        layer_params["name"] = name_save + "_chan"
        layer_chan = make_channel_layer(**layer_params, parent=z_animator.object)
        layer_params["name"] = name_save + "_chanfill"
        layer_chanfill = make_channelfill_layer(
            **layer_params, parent=z_animator.object
        )
        self.bulk = AnimateLayer(layer_bulk)
        self.chan = AnimateLayer(layer_chan)
        self.chanfill = AnimateLayer(layer_chanfill)
        layer_params["name"] = name_save

        # Set up LEDs
        self.bulk_LED_animator = LED_animators["LED bulk"]
        self.chan_LED_animator = LED_animators["LED channel"]

        # Create layer animations
        self.animate_layer()

    def animate_layer(self):
        # Set initial colors for all layer objects
        self.bulk.set_color(self.colors[0])
        self.chan.set_color(self.colors[1])
        self.chanfill.set_color(self.colors[1])

        # First animation series -> grow layer in z then transition color to c1
        self.timings.prep_grow_in_z()
        self.bulk_LED_animator.appear_at_frame(frame_num(self.timings.start_time))
        self.bulk.grow_in_negative_z(
            frame_num(self.timings.start_time), frame_num(self.timings.end_time)
        )
        self.timings.prep_color_c0_to_c1()
        self.bulk.animate_change_color(
            self.colors[1],
            frame_num(self.timings.start_time),
            frame_num(self.timings.end_time),
        )
        self.bulk_LED_animator.disappear_at_frame(frame_num(self.timings.end_time))

        # Swap layer objects to set up for next animation series
        self.bulk.disappear_at_frame(frame_num(self.timings.end_time))
        self.chan.appear_at_frame(frame_num(self.timings.end_time))
        self.chanfill.appear_at_frame(frame_num(self.timings.end_time))

        # Add a small time delay before beginning next animation series
        self.timings.set_delay_between_switch_LED_patterns()

        # Animate transition color to c2 in eroded layer (bulk) region
        self.timings.prep_color_c1_to_c2()
        self.chan_LED_animator.appear_at_frame(frame_num(self.timings.start_time))
        self.chan.animate_change_color(
            self.colors[2],
            frame_num(self.timings.start_time),
            frame_num(self.timings.end_time),
        )
        self.chan_LED_animator.disappear_at_frame(frame_num(self.timings.end_time))


class AnimateChannelWithEdgeLayer:
    def __init__(self, layer_params, timings, colors, LED_animators, z_animator=None):

        self.layer_params = layer_params
        self.timings = timings
        self.colors = colors
        self.z_layer_size = self.layer_params["layer_size"][2]

        if z_animator:  # If parent object exists...
            # Move parent object down in z, which moves all of its children too
            self.z_animator = z_animator
            self.timings.prep_animate_z_move()
            self.z_animator.animate_z_move(
                self.timings.start_time, self.timings.end_time, -self.z_layer_size
            )
        else:
            raise ValueError(
                "AnimateChannelWithEdgeLayer: must provide a z_animator function argument"
            )

        # Make required animator objects
        name_save = layer_params["name"]
        layer_params["name"] = name_save + "_chan"
        layer_chan = make_channel_layer(**layer_params, parent=z_animator.object)
        layer_params["name"] = name_save + "_eroded"
        layer_chan_eroded = make_channel_eroded_layer(
            **layer_params, parent=z_animator.object
        )
        layer_params["name"] = name_save + "_edge"
        layer_chan_edge = make_channel_edge_layer(
            **layer_params, parent=z_animator.object
        )
        self.chan = AnimateLayer(layer_chan)
        self.chan_eroded = AnimateLayer(layer_chan_eroded)
        self.chan_edge = AnimateLayer(layer_chan_edge)
        layer_params["name"] = name_save

        # Set up LEDs
        self.chan_LED_animator = LED_animators["LED channel"]
        self.eroded_LED_animator = LED_animators["LED eroded channel"]

        # Create layer animations
        self.animate_layer()

    def animate_layer(self):
        # Set initial colors for all layer objects
        self.chan.set_color(self.colors[0])
        self.chan_eroded.set_color(self.colors[1])
        self.chan_edge.set_color(self.colors[1])

        # First animation series -> grow layer in z then transition color to c1
        self.timings.prep_grow_in_z()
        self.chan_LED_animator.appear_at_frame(frame_num(self.timings.start_time))
        self.chan.grow_in_negative_z(
            frame_num(self.timings.start_time), frame_num(self.timings.end_time)
        )
        self.timings.prep_color_c0_to_c1()
        self.chan.animate_change_color(
            self.colors[1],
            frame_num(self.timings.start_time),
            frame_num(self.timings.end_time),
        )
        self.chan_LED_animator.disappear_at_frame(frame_num(self.timings.end_time))

        # Swap layer objects to set up for next animation series
        self.chan.disappear_at_frame(frame_num(self.timings.end_time))
        self.chan_edge.appear_at_frame(frame_num(self.timings.end_time))
        self.chan_eroded.appear_at_frame(frame_num(self.timings.end_time))

        # Add a small time delay before beginning next animation series
        self.timings.set_delay_between_switch_LED_patterns()

        # Animate transition color to c2 in eroded layer (bulk) region
        self.timings.prep_color_c1_to_c2()
        self.eroded_LED_animator.appear_at_frame(frame_num(self.timings.start_time))
        self.chan_eroded.animate_change_color(
            self.colors[2],
            frame_num(self.timings.start_time),
            frame_num(self.timings.end_time),
        )
        self.eroded_LED_animator.disappear_at_frame(frame_num(self.timings.end_time))


class AnimateChannelLayer(MixinScale, MixinGrowInZ, MixinColorAnimation):
    def __init__(self, layer_params, timings, colors, LED_animators, z_animator=None):

        self.layer_params = layer_params
        self.timings = timings
        self.colors = colors
        self.z_layer_size = self.layer_params["layer_size"][2]

        if z_animator:  # If parent object exists...
            # Move parent object down in z, which moves all of its children too
            self.z_animator = z_animator
            self.timings.prep_animate_z_move()
            self.z_animator.animate_z_move(
                self.timings.start_time, self.timings.end_time, -self.z_layer_size
            )
            # Create new layer and make it a child of the parent object
            self.object = make_channel_layer(**layer_params, parent=z_animator.object)
        else:  # If parent object does not exist, this object will be the parent object
            self.object = make_channel_layer(**layer_params)
            self.z_animator = AnimateZMotion(self.object)

        self._initialize_grow_in_z()
        self._initialize_color_for_animation()

        # Set up LED
        self.LED_animator = LED_animators["LED channel"]

        self.animate_layer()

    def animate_layer(self):
        self.set_color(self.colors[0])
        self.timings.prep_grow_in_z()
        self.LED_animator.appear_at_frame(frame_num(self.timings.start_time))
        self.grow_in_negative_z(
            frame_num(self.timings.start_time), frame_num(self.timings.end_time)
        )

        self.timings.prep_color_c0_to_c1()
        self.animate_change_color(
            self.colors[1],
            frame_num(self.timings.start_time),
            frame_num(self.timings.end_time),
        )

        self.timings.prep_color_c1_to_c2()
        end_time_LED = self.timings.end_time
        self.animate_change_color(
            self.colors[2],
            frame_num(self.timings.start_time),
            frame_num(self.timings.end_time),
        )
        self.LED_animator.disappear_at_frame(frame_num(self.timings.end_time))


class AnimateBulkLayer(MixinScale, MixinGrowInZ, MixinColorAnimation):
    def __init__(self, layer_params, timings, colors, LED_animators, z_animator=None):

        self.layer_params = layer_params
        self.timings = timings
        self.colors = colors
        self.z_layer_size = self.layer_params["layer_size"][2]

        if z_animator:  # If parent object exists...
            # Move parent object down in z, which moves all of its children too
            self.z_animator = z_animator
            self.timings.prep_animate_z_move()
            self.z_animator.animate_z_move(
                self.timings.start_time, self.timings.end_time, -self.z_layer_size
            )
            # Create new layer and make it a child of the parent object
            self.object = make_bulk_layer(**layer_params, parent=z_animator.object)
        else:  # If parent object does not exist, this object will be the parent object
            self.object = make_bulk_layer(**layer_params)
            self.z_animator = AnimateZMotion(self.object)

        self._initialize_grow_in_z()
        self._initialize_color_for_animation()

        # Set up LED
        self.LED_animator = LED_animators["LED bulk"]

        self.animate_layer()

    def animate_layer(self):

        self.set_color(self.colors[0])
        self.timings.prep_grow_in_z()
        self.LED_animator.appear_at_frame(frame_num(self.timings.start_time))
        self.grow_in_negative_z(
            frame_num(self.timings.start_time), frame_num(self.timings.end_time)
        )

        self.timings.prep_color_c0_to_c1()
        self.animate_change_color(
            self.colors[1],
            frame_num(self.timings.start_time),
            frame_num(self.timings.end_time),
        )

        self.timings.prep_color_c1_to_c2()
        end_time_LED = self.timings.end_time
        self.animate_change_color(
            self.colors[2],
            frame_num(self.timings.start_time),
            frame_num(self.timings.end_time),
        )
        self.LED_animator.disappear_at_frame(frame_num(self.timings.end_time))


class AnimateZMotion:
    def __init__(self, obj):
        self.object = obj

    def animate_z_move(self, start_time, end_time, delta_z):
        # Start and end locations
        current_location = self.object.location
        new_location = (
            current_location[0],
            current_location[1],
            current_location[2] + delta_z,
        )

        # Keyframe current location to begin move
        self.object.keyframe_insert(data_path="location", frame=frame_num(start_time))

        # Keyframe new location to end move
        self.object.location = new_location
        self.object.keyframe_insert(data_path="location", frame=frame_num(end_time))


# ----------------------------------------------------------------------------------------
# LED illumination
# ----------------------------------------------------------------------------------------


def create_LED_animators(layer_params, LED_material):
    LED_animators = {}

    layer_size = (
        layer_params["layer_size"][0],
        layer_params["layer_size"][1],
        layer_params["z_size_illum"],
    )

    name = "LED bulk"
    LED_animators[name] = AnimateAppearDisappear(
        make_bulk_layer(name=name, layer_size=layer_size, material=LED_material,)
    )

    name = "LED channel"
    LED_animators[name] = AnimateAppearDisappear(
        make_channel_layer(
            name=name,
            layer_size=layer_size,
            channel_width=layer_params["channel_width"],
            material=LED_material,
        )
    )

    name = "LED eroded channel"
    LED_animators[name] = AnimateAppearDisappear(
        make_channel_eroded_layer(
            name=name,
            layer_size=layer_size,
            channel_width=layer_params["channel_width"],
            edge_width=layer_params["edge_width"],
            material=LED_material,
        )
    )

    name = "LED channel edge"
    LED_animators[name] = AnimateAppearDisappear(
        make_channel_edge_layer(
            name=name,
            layer_size=layer_size,
            channel_width=layer_params["channel_width"],
            edge_width=layer_params["edge_width"],
            material=LED_material,
        )
    )

    return LED_animators


# ----------------------------------------------------------------------------------------
# Main code
# ----------------------------------------------------------------------------------------


# Set up Rendering to use bloom
bpy.context.scene.eevee.use_bloom = True
bpy.data.scenes["Scene"].eevee.bloom_intensity = 0.1

# Animation setup
# frames_per_second = bpy.data.scenes["Scene"].render.fps
# # Change to 60 fps
bpy.data.scenes["Scene"].render.fps = 60
frames_per_second = bpy.data.scenes["Scene"].render.fps
# Set up function to return frame number given time in seconds
frame_num = partial(frame_number, frames_per_second=frames_per_second)


# Layer parameters
xy_layer_size = 10
x_layer_size, y_layer_size, z_layer_size = xy_layer_size, xy_layer_size, 0.5
layer_size = (xy_layer_size, xy_layer_size, z_layer_size)
z_size_illum = 15
channel_width = 3
edge_width = 1
num_layers = 8  # 9
num_small_layers_per_layer = 3
z_small_layer_size = z_layer_size / num_small_layers_per_layer
# Specify channel and roof layers
# chan_layers = [2, 3, 4, 5]
# roof_layers = [6, 7]
chan_layers = [1, 2, 3, 4]
roof_layers = [5, 6]

# Define colors
# color_RGB_small_edge = (0.906, 0.96, 0.87)  # HEX #e7f5de
# color_RGB_edge = (0.36, 0.53, 0.55)  # HEX #5C878C
# color_RGB_bulk = (0.09, 0.135, 0.14)  # HEX #172224

color_RGB_small_edge = (0.988, 0.835, 0.533)  # HEX #fcd588
color_RGB_edge = (0.800, 0.588, 0.161)  # HEX #cc9629
color_RGB_bulk = (0.549, 0.424, 0.129)  # HEX #8c6c21

# LED emission color
color_emission = (0.08, 0.03, 1.0)  # RGB (20, 8, 255) = HEX #1408FF

# Color sequence for layer exposure
colors = {
    0: color_RGB_small_edge,
    1: color_RGB_edge,
    2: color_RGB_bulk,
    "LED": color_emission,
}

layer_params = {
    "name": "",
    "layer_size": (x_layer_size, y_layer_size, z_layer_size),
    "channel_width": channel_width,
    "edge_width": edge_width,
    "color_RGB": color_RGB_small_edge,
    "z_size_illum": z_size_illum,
}

# Light
light_location = (8.1524, 2.0110, 11.808)
light_rotation = [pi * 37.3 / 180, pi * 3.16 / 180, pi * 107 / 180]
light_sun = sun_light(location=light_location, rotation=light_rotation)
# light_pt = my_point_light(location=light_location, rotation=light_rotation)
# light_area = my_area_light(location=light_location, rotation=light_rotation)
# light_area2 = my_area_light(location=light_location, rotation=light_rotation. power=1000, size=2.5, name="Light_area2")

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
cam.rotation_euler = [pi * 59.9 / 180, pi * 0.0 / 180, pi * 46.7 / 180]

# Materials
# Layer material
make_material = make_material_Principled_BSDF
# Emissive LED material
make_LED_material = partial(
    make_semitransparent_emission_shader, color=color_emission, strength=5, mix_fac=0.6
)

LED_animators = create_LED_animators(layer_params, make_LED_material("LED"))


# Select which case to run by uncommenting one of the following 5 lines
case = "bulk"
# case = "channel"
# case = "channel with edge dose"
# case = "channel with edge dose and roof dose"
# case = "channel with small edge layers and roof dose"

# Set up layer lists for specific case chosen
channel_layers = []
secondary_image_channel_layers = []
secondary_image_small_channel_layers = []
secondary_image_roof_layers = []
if case == "bulk":
    pass
elif case == "channel":
    channel_layers = chan_layers
elif case == "channel with edge dose":
    secondary_image_channel_layers = chan_layers
elif case == "channel with edge dose and roof dose":
    secondary_image_channel_layers = chan_layers
    secondary_image_roof_layers = roof_layers
elif case == "channel with small edge layers and roof dose":
    secondary_image_small_channel_layers = chan_layers
    secondary_image_roof_layers = roof_layers

# Set up timing parameters
z_grow_duration = 0.4
color_c0_to_c1 = 0.2
color_c1_to_c2 = 0.2
timings_dict = {
    "start time": 0.3,
    "end time": None,
    "z grow duration": z_grow_duration,
    "color c0 to c1": color_c0_to_c1,
    "color c1 to c2": color_c1_to_c2,
    "extra time LED is on": color_c0_to_c1 + color_c1_to_c2,
    "move down delay after LED": 0.2,
    "move down duration": 0.6,
    "between layer delay": 0.2,
}
tt = timings_dict  # Need shorthand for timings to reduce clutter


timings = Timings()

# Loop to create layers and corresponding animation
for i in range(num_layers):
    layer_params["name"] = f"Layer_{i:02d}"
    layer_params["color_RGB"] = color_RGB_small_edge
    layer_params["i"] = i
    if i == 0:
        overall_parent_layer = AnimateBulkLayer(
            layer_params, timings, colors, LED_animators
        )
        z_animator = overall_parent_layer.z_animator
    elif i in channel_layers:
        channel = AnimateChannelLayer(
            layer_params, timings, colors, LED_animators, z_animator
        )
    elif i in secondary_image_channel_layers:
        channel_with_edge = AnimateChannelWithEdgeLayer(
            layer_params, timings, colors, LED_animators, z_animator
        )
    elif i in secondary_image_small_channel_layers:
        channel_with_edge = AnimateChannelWithSmallEdgesLayer(
            layer_params, timings, colors, LED_animators, z_animator
        )
    elif i in secondary_image_roof_layers:
        roof = AnimateRoofLayer(
            layer_params, timings, colors, LED_animators, z_animator
        )
    else:
        bulk = AnimateBulkLayer(
            layer_params, timings, colors, LED_animators, z_animator
        )

# Set last frame to be rendered for animation
last_frame = frame_num(timings.end_time + 0.3)
print(f"Last frame: {last_frame}")
bpy.data.scenes["Scene"].frame_end = last_frame
