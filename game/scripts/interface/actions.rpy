init -1:
    
    default Action_screen_showing = False
    default Action_screen_hidden = False

    default Action_screen_tab = "pose"

style Action_screen is default

style Action_screen_button:
    # hover_sound "sounds/interface/hover.ogg"
    activate_sound "sounds/interface/press.ogg"

style Action_screen_image_button:
    # hover_sound "sounds/interface/hover.ogg"
    activate_sound "sounds/interface/press.ogg"
    
screen Action_screen(automatic = False):
    layer "interface"

    style_prefix "Action_screen"

    on "show" action [
        SetVariable("Action_screen_showing", True),
        SetVariable("speed", 1.0),
        SetVariable("intensity", 1.0),
        SetVariable("starting_depth", 0.0),
        SetVariable("Action_screen_tab", "pose"),
        SetVariable("belt_hidden", True),
        Hide("interactions_screen"),
        SetVariable("choice_disabled", True)]

    if not black_screen:
        $ focused_Girl_index = 0

        for g, G in enumerate(Present):
            if G == focused_Girl:
                $ focused_Girl_index = g

        add "images/interface/Action_menu/background.webp" zoom interface_new_adjustment

        bar value Player.desire range 100 anchor (0.5, 0.5) pos (0.94, 0.0478) xysize (int(291*interface_new_adjustment), int(37*interface_new_adjustment)):
            left_bar Frame("images/interface/Action_menu/climax_male.webp")
            right_bar Frame("images/interface/Action_menu/climax_empty.webp")

            thumb None
            thumb_offset 0

            tooltip f"{Player.first_name}'s Desire"

        bar value focused_Girl.desire range 100 anchor (0.5, 0.5) pos (0.94, 0.0851) xysize (int(291*interface_new_adjustment), int(37*interface_new_adjustment)):
            left_bar Frame("images/interface/Action_menu/climax_female.webp")
            right_bar Frame("images/interface/Action_menu/climax_empty.webp")

            thumb None
            thumb_offset 0

            tooltip f"{focused_Girl.name}'s Desire"

        if has_progression_control:
            if has_position_control:
                imagebutton:
                    idle At("images/interface/Action_menu/pose_idle.webp", interface) hover At("images/interface/Action_menu/pose.webp", interface)

                    if has_position_control:
                        action SetVariable("Action_screen_tab", "pose")
                    else:
                        action None

                    tooltip "Open Position Menu"
                    
                    focus_mask True

            if has_Action_control:
                imagebutton:
                    idle At("images/interface/Action_menu/action_idle.webp", interface) hover At("images/interface/Action_menu/action.webp", interface)

                    if has_Action_control:
                        action SetVariable("Action_screen_tab", "action")
                    else:
                        action None

                    tooltip "Open Action Menu"
                    
                    focus_mask True

            if has_Action_control:
                imagebutton:
                    idle At("images/interface/Action_menu/strip_idle.webp", interface) hover At("images/interface/Action_menu/strip.webp", interface)

                    if has_Action_control:
                        action SetVariable("Action_screen_tab", "strip")
                    else:
                        action None

                    tooltip "Open Strip Menu"
                    
                    focus_mask True

            # if has_Action_control:
            #     if Action_screen_tab == "action":

            # # if has_Action_control:
            # #     fixed anchor (0.0, 1.0) pos (0.0, 1.0) xysize (191, 1083):

            # #             imagebutton anchor (0.5, 0.5) pos (0.615, 0.7666):
            # #                 idle "images/interface/Action_menu/spank_idle.webp" hover "images/interface/Action_menu/spank.webp"

            # #                 action Call("spank", focused_Girl, from_current = True)

            # #                 tooltip "Spank"

            # #     if Action_screen_chat_open and Action_type_tab:
            # #         fixed anchor (0.0, 0.0) pos (0.11, 0.01) xysize (507, 629):
            # #             add "images/interface/Action_menu/selection_window.webp"
                        
            # #             viewport id "Action_viewport" anchor (0.5, 0.0) pos (0.475, 0.03) xysize (431, 525):
            # #                 draggable True
            # #                 mousewheel True

            # #                 vbox xalign 0.5:
            # #                     spacing 1

            # #                     $ current_Action_list = eval(f"{Action_type_tab}_Action_types")[:]

            # #                     for Action_type in all_Action_types:
            # #                         if Action_type in current_Action_list:
            # #                             if focused_Girl.available_Actions and Action_type not in focused_Girl.available_Actions:
            # #                                 $ current_Action_list.remove(Action_type)
            # #                             elif focused_Girl.possible_Actions and Action_type not in focused_Girl.possible_Actions:
            # #                                 $ current_Action_list.remove(Action_type)
            # #                             elif "touch_thighs" in Action_type:
            # #                                 if focused_Girl.thighs_covered and "over_clothes" not in Action_type:
            # #                                     $ current_Action_list.remove(Action_type)
            # #                                 elif not focused_Girl.thighs_covered and "over_clothes" in Action_type:
            # #                                     $ current_Action_list.remove(Action_type)
            # #                             elif "touch_breasts" in Action_type:
            # #                                 if focused_Girl.breasts_covered and "over_clothes" not in Action_type:
            # #                                     $ current_Action_list.remove(Action_type)
            # #                                 elif not focused_Girl.breasts_covered and "over_clothes" in Action_type:
            # #                                     $ current_Action_list.remove(Action_type)
            # #                             elif "grab_ass" in Action_type:
            # #                                 if focused_Girl.ass_covered and "over_clothes" not in Action_type:
            # #                                     $ current_Action_list.remove(Action_type)
            # #                                 elif not focused_Girl.ass_covered and "over_clothes" in Action_type:
            # #                                     $ current_Action_list.remove(Action_type)
            # #                             elif "touch_pussy" in Action_type and Action_type != "self_touch_pussy":
            # #                                 if focused_Girl.pussy_covered and "over_clothes" not in Action_type:
            # #                                     $ current_Action_list.remove(Action_type)
            # #                                 elif not focused_Girl.pussy_covered and "over_clothes" in Action_type:
            # #                                     $ current_Action_list.remove(Action_type)

            # #                     for Action_type in toy_Action_types:
            # #                         if Action_type in current_Action_list:
            # #                             if Action_type in dildo_Action_types and not ("dildo" in Player.inventory.keys() or "dildo" in focused_Girl.inventory.keys()):
            # #                                 $ current_Action_list.remove(Action_type)
            # #                             elif Action_type in ["self_vibrator", "vibrator"] and not ("vibrator" in Player.inventory.keys() or "vibrator" in focused_Girl.inventory.keys()):
            # #                                 $ current_Action_list.remove(Action_type)

            # #                     for Action_type in current_Action_list:
            # #                         $ Action_name = Action_names[Action_type]

            # #                         $ ongoing_Action = False

            # #                         for A in Player.all_Actions:
            # #                             if A.Action_type == Action_type:
            # #                                 $ ongoing_Action = A

            # #                         if not ongoing_Action:
            # #                             for A in focused_Girl.all_Actions:
            # #                                 if A.Action_type == Action_type:
            # #                                     $ ongoing_Action = A

            # #                         button align (0.5, 0.5) xysize (431, 71):
            # #                             if Action_type in active_Action_types:
            # #                                 idle_background "images/interface/Action_menu/male_idle.webp" hover_background "images/interface/Action_menu/male.webp" selected_background "images/interface/Action_menu/male_selected.webp"
            # #                             elif Action_type in passive_Action_types:
            # #                                 idle_background "images/interface/Action_menu/female_idle.webp" hover_background "images/interface/Action_menu/female.webp" selected_background "images/interface/Action_menu/female_selected.webp"

            # #                             selected ongoing_Action

            # #                             text f"{Action_name}" anchor (0.5, 0.5) pos (0.55, 0.5):
            # #                                 size 32

            # #                             if ongoing_Action:
            # #                                 action [
            # #                                     Function(stop_Action, ongoing_Action),
            # #                                     SetVariable("selected_Action_index", 0)]
            # #                             else:
            # #                                 if Action_type in ["self_touch_pussy", "self_finger_ass", "self_vibrator", "self_dildo_pussy", "self_dildo_ass"]:
            # #                                     action [
            # #                                         SetVariable("speed", 1.0),
            # #                                         SetVariable("intensity", 1.0),
            # #                                         SetVariable("starting_depth", 0.0),
            # #                                         SetVariable("Action_screen_chat_open", False),
            # #                                         Call("request_Action", Action_type, focused_Girl, focused_Girl, from_current = True)]
            # #                                 elif Action_type in active_Action_types:
            # #                                     action [
            # #                                         SetVariable("speed", 1.0),
            # #                                         SetVariable("intensity", 1.0),
            # #                                         SetVariable("starting_depth", 0.0),
            # #                                         SetVariable("Action_screen_chat_open", False),
            # #                                         Call("request_Action", Action_type, Player, focused_Girl, from_current = True)]
            # #                                 elif Action_type in passive_Action_types:
            # #                                     action [
            # #                                         SetVariable("speed", 1.0),
            # #                                         SetVariable("intensity", 1.0),
            # #                                         SetVariable("starting_depth", 0.0),
            # #                                         SetVariable("Action_screen_chat_open", False),
            # #                                         Call("request_Action", Action_type, focused_Girl, Player, from_current = True)]

            # #             vbar value YScrollValue("Action_viewport") anchor (0.0, 0.0) pos (0.925, 0.03) xysize (22, 525):
            # #                 base_bar Frame("images/interface/Action_menu/scrollbar.webp")

            # #                 thumb "images/interface/Action_menu/scrollbar_thumb.webp"
            # #                 thumb_offset 10

            # #                 unscrollable "hide"
            #     elif Action_screen_tab == "pose":
            # #         if has_position_control:
            # #             $ pose_list = ongoing_Actions[selected_Action_index].available_poses[:]

            # #             for pose in pose_names.keys():
            # #                 if pose in pose_list:
            # #                     if focused_Girl.available_poses and pose not in focused_Girl.available_poses:
            # #                         $ pose_list.remove(pose)
            # #                     elif focused_Girl.possible_poses and pose not in focused_Girl.possible_poses:
            # #                         $ pose_list.remove(pose)

            # #             hbox anchor (0.5, 0.5) pos (0.5, 0.275) xysize (600, 88):
            # #                 spacing -100

            # #                 for pose in pose_list:
            # #                     $ pose_name = pose_names[pose]

            # #                     button align (0.5, 0.5) xysize (200, 88):
            # #                         background None

            # #                         hover_sound None

            # #                         selected ongoing_Actions[selected_Action_index].position == pose

            # #                         text f"{pose_name}" align (0.5, 0.5):
            # #                             if len(pose_name) > 12:
            # #                                 size 26
            # #                             else:
            # #                                 size 32

            # #                             text_align 0.5

            # #                             idle_color "#000000" hover_color "#ffffff" selected_color "#ffffff"

            # #                         if ongoing_Actions[selected_Action_index].position != pose:
            # #                             action Call("request_position", focused_Girl, pose, ongoing_Actions[selected_Action_index], from_current = True)
            # #                         else:
            # #                             action NullAction()

            # #                         # tooltip "Change Position"
            #     elif Action_screen_tab == "strip":

            imagebutton:
                idle At("images/interface/Action_menu/continue_idle.webp", interface) hover At("images/interface/Action_menu/continue.webp", interface)

                action Call("continue_Actions", from_current = True)

                tooltip "Keep Going"
                
                focus_mask True

            if has_movement_control:
                imagebutton:
                    idle At("images/interface/Action_menu/pause_idle.webp", interface) hover At("images/interface/Action_menu/pause.webp", interface)

                    action [
                        SetVariable("speed", 0.001),
                        SetVariable("intensity", 0.001)]

                    tooltip "Pause Action"
                    
                    focus_mask True

            # if ongoing_Actions and has_Action_control:
            #     vpgrid anchor (0.5, 0.5) pos (0.46, 0.695) xysize (180, 180):
            #         cols 2

            #         spacing 1

            #         for mode in ongoing_Actions[selected_Action_index].modes:
            #             button align (0.5, 0.5) xysize (89, 88):
            #                 idle_background "images/interface/Action_menu/mode_idle.webp" hover_background "images/interface/Action_menu/mode.webp" selected_background "images/interface/Action_menu/mode_selected.webp"

            #                 selected selected_Action_mode == mode

            #                 if len(ongoing_Actions[selected_Action_index].modes) == 1:
            #                     text "1" align (0.5, 0.5):
            #                         size 32
            #                 else:
            #                     text f"{mode}" align (0.5, 0.5):
            #                         size 32

            #                 if selected_Action_mode != mode:
            #                     action Call("request_mode", ongoing_Actions[selected_Action_index], mode, from_current = True)
            #                 else:
            #                     action NullAction()

            #                 tooltip "Change Mode"

                # imagebutton anchor (0.5, 0.5) pos (0.72, 0.805):
                #     idle "images/interface/Action_menu/stop_idle.webp" hover "images/interface/Action_menu/stop.webp"

                #     action [
                #         Function(stop_Action, ongoing_Actions[selected_Action_index]),
                #         SetVariable("selected_Action_index", 0)]

                #     tooltip "Stop Action"

            $ different_intensities_available = False

            for Action in ongoing_Actions:
                if Action.speed or Action.intensity:
                    $ different_intensities_available = True

                    break

            if has_movement_control and different_intensities_available:
                imagebutton:
                    idle At("images/interface/Action_menu/x1_idle.webp", interface) hover At("images/interface/Action_menu/x1.webp", interface)

                    action [
                        SetVariable("speed", 0.5),
                        SetVariable("intensity", 0.5)]

                    tooltip "Set Intensity to 1"
                    
                    focus_mask True

                imagebutton:
                    idle At("images/interface/Action_menu/x2_idle.webp", interface) hover At("images/interface/Action_menu/x2.webp", interface)

                    action [
                        SetVariable("speed", 1.0),
                        SetVariable("intensity", 1.0)]

                    tooltip "Set Intensity to 2"
                    
                    focus_mask True

                imagebutton:
                    idle At("images/interface/Action_menu/x3_idle.webp", interface) hover At("images/interface/Action_menu/x3.webp", interface)

                    action [
                        SetVariable("speed", 2.0),
                        SetVariable("intensity", 2.0)]

                    tooltip "Set Intensity to 3"
                    
                    focus_mask True

            imagebutton:
                idle At("images/interface/Action_menu/close_idle.webp", interface) hover At("images/interface/Action_menu/close.webp", interface)

                if automatic:
                    action [
                        SetVariable("Action_screen_showing", False),
                        Call("stop_all_Actions", close_interface = True),
                        Return()]
                else:
                    action [
                        SetVariable("Action_screen_showing", False),
                        Call("stop_all_Actions", close_interface = True, from_current = True)]

                tooltip "Finish"

                focus_mask True

    if black_screen or renpy.get_screen("say"):
        button align (0.5, 0.5) xysize (config.screen_width, config.screen_height):
            background None
            
            if not renpy.get_screen("choice"):
                action Return()
            else:
                action NullAction()

    use quick_menu

    if tooltips_enabled:
        use tooltips