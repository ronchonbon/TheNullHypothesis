init -1:
    
    default Action_screen_showing = False
    default Action_screen_hidden = False

    default Action_screen_tab = "pose"

    default Action_auto_progress = False
    default Action_auto_progress_timer = 0.0

    default Action_hover_type = None
    default Action_hover_size = 1.0

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

    if Action_auto_progress:
        if Action_auto_progress_timer < 5.0:
            timer 0.1 repeat True action SetVariable("Action_auto_progress_timer", Action_auto_progress_timer + 0.1)
        else:
            timer 0.1 repeat True action [
                SetVariable("Action_auto_progress_timer", 0.0),
                Call("continue_Actions", from_current = True),
                Return()]

    if not black_screen:
        $ focused_Companion_index = 0

        for g, G in enumerate(Present):
            if G == focused_Companion:
                $ focused_Companion_index = g

        add "images/interface/Action_menu/background.webp" zoom interface_new_adjustment

        text f"{Player.stamina}" anchor (0.5, 0.5) pos (0.839, 0.03752):
            size 35

            text_align 0.5

            color "#ffffff"

        text f"{focused_Companion.stamina}" anchor (0.5, 0.5) pos (0.839, 0.0952):
            size 35

            text_align 0.5

            color "#ffffff"

        if Action_hover_type:
            add At(At(At("images/interface/Action_menu/popup.webp", change_anchor(0.5, 0.5)), change_pos(0.825, 0.28)), zoom_sprite(0.5))

            if hookup_length >= max_hookup_length*math.sqrt(focused_Companion.max_stamina) and focused_Companion.desire <= 75:
                add At(At(At("images/interface/Action_menu/low.webp", change_anchor(0.5, 0.5)), change_pos(0.825, 0.283)), zoom_sprite(0.2))
            elif Action_hover_type in ["high", "low"] and Action_hover_size >= 0.9:
                add At(At(At("images/interface/Action_menu/[Action_hover_type].webp", change_anchor(0.5, 0.5)), change_pos(0.825, 0.283)), zoom_sprite(0.5))
            elif Action_hover_type in ["high", "low"] and Action_hover_size >= 0.8:
                add At(At(At("images/interface/Action_menu/[Action_hover_type].webp", change_anchor(0.5, 0.5)), change_pos(0.825, 0.283)), zoom_sprite(0.45))
            elif Action_hover_type in ["high", "low"] and Action_hover_size >= 0.7:
                add At(At(At("images/interface/Action_menu/[Action_hover_type].webp", change_anchor(0.5, 0.5)), change_pos(0.825, 0.283)), zoom_sprite(0.4))
            elif Action_hover_type in ["high", "low"] and Action_hover_size >= 0.6:
                add At(At(At("images/interface/Action_menu/[Action_hover_type].webp", change_anchor(0.5, 0.5)), change_pos(0.825, 0.283)), zoom_sprite(0.35))
            elif Action_hover_type in ["high", "low"] and Action_hover_size >= 0.5:
                add At(At(At("images/interface/Action_menu/[Action_hover_type].webp", change_anchor(0.5, 0.5)), change_pos(0.825, 0.283)), zoom_sprite(0.3))
            elif Action_hover_type in ["high", "low"] and Action_hover_size >= 0.4:
                add At(At(At("images/interface/Action_menu/[Action_hover_type].webp", change_anchor(0.5, 0.5)), change_pos(0.825, 0.283)), zoom_sprite(0.25))
            elif Action_hover_type in ["high", "low"] and Action_hover_size >= 0.3:
                add At(At(At("images/interface/Action_menu/[Action_hover_type].webp", change_anchor(0.5, 0.5)), change_pos(0.825, 0.283)), zoom_sprite(0.2))
            elif Action_hover_type in ["high", "low"] and Action_hover_size >= 0.2:
                add At(At(At("images/interface/Action_menu/[Action_hover_type].webp", change_anchor(0.5, 0.5)), change_pos(0.825, 0.283)), zoom_sprite(0.15))
            elif Action_hover_type in ["high", "low"] and Action_hover_size >= 0.1:
                add At(At(At("images/interface/Action_menu/[Action_hover_type].webp", change_anchor(0.5, 0.5)), change_pos(0.825, 0.283)), zoom_sprite(0.1))
            elif Action_hover_type in ["high", "low"] and Action_hover_size >= 0.0:
                add At(At(At("images/interface/Action_menu/[Action_hover_type].webp", change_anchor(0.5, 0.5)), change_pos(0.825, 0.283)), zoom_sprite(0.05))
            else:
                add At(At(At("images/interface/Action_menu/[Action_hover_type].webp", change_anchor(0.5, 0.5)), change_pos(0.825, 0.283)), zoom_sprite(0.5))

        if Player.desire >= 90:
            add At("images/interface/Action_menu/lightning_male.webp", pulse(intensity = 1.0)) zoom interface_new_adjustment
        elif Player.desire >= 80:
            add At("images/interface/Action_menu/lightning_male.webp", pulse(intensity = 0.8)) zoom interface_new_adjustment
        elif Player.desire >= 70:
            add At("images/interface/Action_menu/lightning_male.webp", pulse(intensity = 0.6)) zoom interface_new_adjustment
        elif Player.desire >= 60:
            add At("images/interface/Action_menu/lightning_male.webp", pulse(intensity = 0.4)) zoom interface_new_adjustment
        elif Player.desire >= 50:
            add At("images/interface/Action_menu/lightning_male.webp", pulse(intensity = 0.2)) zoom interface_new_adjustment

        bar value Player.desire range 100 anchor (0.5, 0.5) pos (0.94, 0.0478) xysize (int(291*interface_new_adjustment), int(37*interface_new_adjustment)):
            left_bar Frame("images/interface/Action_menu/climax_male.webp")
            right_bar Frame("images/interface/Action_menu/climax_empty.webp")

            thumb None
            thumb_offset 0

            tooltip f"{Player.first_name}'s Desire"

        if Player.desire >= 90:
            add At("images/interface/Action_menu/glow_male.webp", pulse(intensity = 1.0)) zoom interface_new_adjustment
        elif Player.desire >= 80:
            add At("images/interface/Action_menu/glow_male.webp", pulse(intensity = 0.8)) zoom interface_new_adjustment
        elif Player.desire >= 70:
            add At("images/interface/Action_menu/glow_male.webp", pulse(intensity = 0.6)) zoom interface_new_adjustment
        elif Player.desire >= 60:
            add At("images/interface/Action_menu/glow_male.webp", pulse(intensity = 0.4)) zoom interface_new_adjustment
        elif Player.desire >= 50:
            add At("images/interface/Action_menu/glow_male.webp", pulse(intensity = 0.2)) zoom interface_new_adjustment

        if focused_Companion.desire >= 90:
            add At("images/interface/Action_menu/lightning_female.webp", pulse(intensity = 1.0)) zoom interface_new_adjustment
        elif focused_Companion.desire >= 80:
            add At("images/interface/Action_menu/lightning_female.webp", pulse(intensity = 0.8)) zoom interface_new_adjustment
        elif focused_Companion.desire >= 70:
            add At("images/interface/Action_menu/lightning_female.webp", pulse(intensity = 0.6)) zoom interface_new_adjustment
        elif focused_Companion.desire >= 60:
            add At("images/interface/Action_menu/lightning_female.webp", pulse(intensity = 0.4)) zoom interface_new_adjustment
        elif focused_Companion.desire >= 50:
            add At("images/interface/Action_menu/lightning_female.webp", pulse(intensity = 0.2)) zoom interface_new_adjustment

        bar value focused_Companion.desire range 100 anchor (0.5, 0.5) pos (0.94, 0.0851) xysize (int(291*interface_new_adjustment), int(37*interface_new_adjustment)):
            left_bar Frame("images/interface/Action_menu/climax_female.webp")
            right_bar Frame("images/interface/Action_menu/climax_empty.webp")

            thumb None
            thumb_offset 0

            tooltip f"{focused_Companion.name}'s Desire"

        if focused_Companion.desire >= 90:
            add At("images/interface/Action_menu/glow_female.webp", pulse(intensity = 1.0)) zoom interface_new_adjustment
        elif focused_Companion.desire >= 80:
            add At("images/interface/Action_menu/glow_female.webp", pulse(intensity = 0.8)) zoom interface_new_adjustment
        elif focused_Companion.desire >= 70:
            add At("images/interface/Action_menu/glow_female.webp", pulse(intensity = 0.6)) zoom interface_new_adjustment
        elif focused_Companion.desire >= 60:
            add At("images/interface/Action_menu/glow_female.webp", pulse(intensity = 0.4)) zoom interface_new_adjustment
        elif focused_Companion.desire >= 50:
            add At("images/interface/Action_menu/glow_female.webp", pulse(intensity = 0.2)) zoom interface_new_adjustment

        if has_progression_control:
            if has_position_control:
                imagebutton:
                    idle At("images/interface/Action_menu/pose_idle.webp", interface) hover At("images/interface/Action_menu/pose.webp", interface) selected_idle At("images/interface/Action_menu/pose.webp", interface)

                    selected Action_screen_tab == "pose"

                    if has_position_control:
                        action SetVariable("Action_screen_tab", "pose")
                    else:
                        action None

                    tooltip "Open Position Menu"
                    
                    focus_mask True

            if has_Action_control:
                imagebutton:
                    idle At("images/interface/Action_menu/action_idle.webp", interface) hover At("images/interface/Action_menu/action.webp", interface) selected_idle At("images/interface/Action_menu/action.webp", interface)

                    selected Action_screen_tab == "action"

                    if has_Action_control:
                        action SetVariable("Action_screen_tab", "action")
                    else:
                        action None

                    tooltip "Open Action Menu"
                    
                    focus_mask True

            if has_Action_control:
                imagebutton:
                    idle At("images/interface/Action_menu/strip_idle.webp", interface) hover At("images/interface/Action_menu/strip.webp", interface) selected_idle At("images/interface/Action_menu/strip.webp", interface)

                    selected Action_screen_tab == "strip"

                    if has_Action_control:
                        action [
                            SetVariable("Action_auto_progress", False),
                            SetVariable("Action_auto_progress_timer", 0.0),
                            Call("ask_to_undress", focused_Companion, from_current = True)]
                    else:
                        action None

                    tooltip "Open Undressing Menu"
                    
                    focus_mask True

            if Action_screen_tab == "pose":
                if has_position_control:
                    $ pose_list = all_poses[:]

                    for pose in pose_names.keys():
                        if pose in pose_list:
                            if focused_Companion.available_poses and pose not in focused_Companion.available_poses:
                                $ pose_list.remove(pose)
                            elif focused_Companion.possible_poses and pose not in focused_Companion.possible_poses:
                                $ pose_list.remove(pose)

                    if len(pose_list) <= 6:
                        $ viewport_position = 0.9281
                    else:
                        $ viewport_position = 0.922

                    vpgrid id "pose_viewport" anchor (0.5, 0.0) pos (viewport_position, 0.276) xysize (int(447*interface_new_adjustment), int(980*interface_new_adjustment)):
                        cols 1

                        draggable True
                        mousewheel True

                        spacing -10

                        for pose in pose_list:
                            $ pose_name = pose_names[pose]

                            button align (0.5, 0.5) xysize (int(447*interface_new_adjustment), int(177*interface_new_adjustment)):
                                idle_background At("images/interface/Action_menu/button_off.webp", interface) hover_background At("images/interface/Action_menu/button_on.webp", interface) selected_idle_background At("images/interface/Action_menu/button_on.webp", interface)

                                selected focused_Companion.position == pose

                                text f"{pose_name}" align (0.5, 0.5):
                                    if len(pose_name) > 18:
                                        size 22
                                    elif len(pose_name) > 15:
                                        size 28
                                    elif len(pose_name) > 12:
                                        size 32
                                    else:
                                        size 35

                                    text_align 0.5

                                    color "#ffffff"

                                if focused_Companion.position != pose:
                                    action [
                                        SetVariable("Action_auto_progress", False),
                                        SetVariable("Action_auto_progress_timer", 0.0),
                                        Call("request_position", focused_Companion, pose, from_current = True)]
                                else:
                                    action NullAction()

                    vbar value YScrollValue("pose_viewport") anchor (0.0, 0.0) pos (0.98, 0.276) xysize (int(29*interface_new_adjustment), int(980*interface_new_adjustment)):
                        base_bar Frame("images/interface/Action_menu/scrollbar.webp")

                        thumb At("images/interface/Action_menu/scrollbar_thumb.webp", interface)
                        thumb_offset 10

                        unscrollable "hide"
            if Action_screen_tab == "action":
                if has_Action_control:
                    $ current_Action_list = all_Action_types[:]

                    for Action_type in all_Action_types:
                        if Action_type in current_Action_list:
                            if focused_Companion.available_Actions and Action_type not in focused_Companion.available_Actions:
                                $ current_Action_list.remove(Action_type)
                            elif focused_Companion.possible_Actions and Action_type not in focused_Companion.possible_Actions:
                                $ current_Action_list.remove(Action_type)
                            elif "touch_thighs" in Action_type:
                                if focused_Companion.thighs_covered and "over_clothes" not in Action_type:
                                    $ current_Action_list.remove(Action_type)
                                elif not focused_Companion.thighs_covered and "over_clothes" in Action_type:
                                    $ current_Action_list.remove(Action_type)
                            elif "touch_breasts" in Action_type:
                                if focused_Companion.breasts_covered and "over_clothes" not in Action_type:
                                    $ current_Action_list.remove(Action_type)
                                elif not focused_Companion.breasts_covered and "over_clothes" in Action_type:
                                    $ current_Action_list.remove(Action_type)
                            elif "grab_ass" in Action_type:
                                if focused_Companion.ass_covered and "over_clothes" not in Action_type:
                                    $ current_Action_list.remove(Action_type)
                                elif not focused_Companion.ass_covered and "over_clothes" in Action_type:
                                    $ current_Action_list.remove(Action_type)
                            elif "touch_pussy" in Action_type and Action_type != "self_touch_pussy":
                                if focused_Companion.pussy_covered and "over_clothes" not in Action_type:
                                    $ current_Action_list.remove(Action_type)
                                elif not focused_Companion.pussy_covered and "over_clothes" in Action_type:
                                    $ current_Action_list.remove(Action_type)

                    for Action_type in toy_Action_types:
                        if Action_type in current_Action_list:
                            if Action_type in dildo_Action_types and not ("dildo" in Player.inventory.keys() or "dildo" in focused_Companion.inventory.keys()):
                                $ current_Action_list.remove(Action_type)
                            elif Action_type in ["self_vibrator", "vibrator"] and not ("vibrator" in Player.inventory.keys() or "vibrator" in focused_Companion.inventory.keys()):
                                $ current_Action_list.remove(Action_type)

                    for Action_type in all_Action_types:
                        if Action_type in current_Action_list:
                            $ test_Action = ActionClass(Action_type, None)

                            if focused_Companion.position not in test_Action.available_poses:
                                $ current_Action_list.remove(Action_type)

                    if len(current_Action_list) <= 5:
                        $ viewport_position = 0.9281
                    else:
                        $ viewport_position = 0.922

                    vpgrid id "Action_viewport" anchor (0.5, 0.0) pos (viewport_position, 0.276) xysize (int(447*interface_new_adjustment), int(980*interface_new_adjustment)):
                        cols 1

                        draggable True
                        mousewheel True

                        spacing -10
                                            
                        button align (0.5, 0.5) xysize (int(447*interface_new_adjustment), int(177*interface_new_adjustment)):
                            idle_background At("images/interface/Action_menu/button_off.webp", interface) hover_background At("images/interface/Action_menu/button_on.webp", interface) selected_idle_background At("images/interface/Action_menu/button_on.webp", interface)

                            if focused_Companion.History.check(Action_type) < unknown_threshold:
                                hovered [
                                    SetVariable("Action_hover_type", "unknown"),
                                    SetVariable("Action_hover_size", 1.0)]
                            elif focused_Companion.History.check(Action_type, tracker = "weekly") >= boredom_threshold:
                                hovered [
                                    SetVariable("Action_hover_type", "low"),
                                    SetVariable("Action_hover_size", 0.2)]
                            else:
                                hovered [
                                    SetVariable("Action_hover_type", "high"),
                                    SetVariable("Action_hover_size", eval(f"{focused_Companion.tag}_base_Action_desire")*eval(f"{focused_Companion.tag}_Action_desires['{Action_type}'][{int(focused_Companion.desire/20 % 5)}]"))]
                            
                            unhovered [
                                SetVariable("Action_hover_type", None),
                                SetVariable("Action_hover_size", 1.0)]

                            text "Spank" align (0.5, 0.5):
                                size 35

                                text_align 0.5

                                color "#ffffff"

                            action Call("spank", focused_Companion, from_current = True)

                        for Action_type in current_Action_list:
                            $ Action_name = Action_names[Action_type]

                            $ ongoing_Action = False

                            for A in Player.all_Actions:
                                if A.Action_type == Action_type:
                                    $ ongoing_Action = A

                            if not ongoing_Action:
                                for A in focused_Companion.all_Actions:
                                    if A.Action_type == Action_type:
                                        $ ongoing_Action = A

                            button align (0.5, 0.5) xysize (int(447*interface_new_adjustment), int(177*interface_new_adjustment)):
                                idle_background At("images/interface/Action_menu/button_off.webp", interface) hover_background At("images/interface/Action_menu/button_on.webp", interface) selected_idle_background At("images/interface/Action_menu/button_on.webp", interface)

                                selected ongoing_Action

                                if focused_Companion.History.check(Action_type) < unknown_threshold:
                                    hovered [
                                        SetVariable("Action_hover_type", "unknown"),
                                        SetVariable("Action_hover_size", 1.0)]
                                elif focused_Companion.History.check(Action_type, tracker = "weekly") >= boredom_threshold:
                                    hovered [
                                        SetVariable("Action_hover_type", "low"),
                                        SetVariable("Action_hover_size", 0.2)]
                                else:
                                    hovered [
                                        SetVariable("Action_hover_type", "high"),
                                        SetVariable("Action_hover_size", eval(f"{focused_Companion.tag}_base_Action_desire")*eval(f"{focused_Companion.tag}_Action_desires['{Action_type}'][{int(focused_Companion.desire/20 % 5)}]"))]
                                
                                unhovered [
                                    SetVariable("Action_hover_type", None),
                                    SetVariable("Action_hover_size", 1.0)]

                                text f"{Action_name}" align (0.5, 0.5):
                                    if len(Action_name) > 18:
                                        size 22
                                    elif len(Action_name) > 15:
                                        size 28
                                    elif len(Action_name) > 12:
                                        size 32
                                    else:
                                        size 35

                                    text_align 0.5

                                    color "#ffffff"

                                if ongoing_Action:
                                    action [
                                        Function(stop_Action, ongoing_Action)]
                                else:
                                    if Action_type in ["self_touch_pussy", "self_finger_ass", "self_vibrator", "self_dildo_pussy", "self_dildo_ass"]:
                                        action [
                                            SetVariable("speed", 1.0),
                                            SetVariable("intensity", 1.0),
                                            SetVariable("starting_depth", 0.0),
                                            Call("request_Action", Action_type, focused_Companion, focused_Companion, from_current = True)]
                                    elif Action_type in active_Action_types:
                                        action [
                                            SetVariable("speed", 1.0),
                                            SetVariable("intensity", 1.0),
                                            SetVariable("starting_depth", 0.0),
                                            Call("request_Action", Action_type, Player, focused_Companion, from_current = True)]
                                    elif Action_type in passive_Action_types:
                                        action [
                                            SetVariable("speed", 1.0),
                                            SetVariable("intensity", 1.0),
                                            SetVariable("starting_depth", 0.0),
                                            Call("request_Action", Action_type, focused_Companion, Player, from_current = True)]

                    vbar value YScrollValue("Action_viewport") anchor (0.0, 0.0) pos (0.98, 0.276) xysize (int(29*interface_new_adjustment), int(980*interface_new_adjustment)):
                        base_bar Frame("images/interface/Action_menu/scrollbar.webp")

                        thumb At("images/interface/Action_menu/scrollbar_thumb.webp", interface)
                        thumb_offset 10

                        unscrollable "hide"
            #     elif Action_screen_tab == "strip":

            if ongoing_Actions:
                imagebutton:
                    idle At("images/interface/Action_menu/continue_idle.webp", interface) hover At("images/interface/Action_menu/continue.webp", interface)

                    action [
                        SetVariable("Action_auto_progress", False),
                        SetVariable("Action_auto_progress_timer", 0.0),
                        Call("continue_Actions", from_current = True)]

                    tooltip "Keep Going"
                    
                    focus_mask True

                if has_movement_control:
                    imagebutton:
                        idle At("images/interface/Action_menu/pause_idle.webp", interface) hover At("images/interface/Action_menu/pause.webp", interface)

                        if Player.cock_Actions:
                            action [
                                SetVariable("Action_auto_progress", False),
                                SetVariable("Action_auto_progress_timer", 0.0),
                                SetVariable("speed", 0.001),
                                SetVariable("intensity", 0.001),
                                SetField(Player.cock_Actions[0], "mode", 0)]
                        else:
                            action [
                                SetVariable("speed", 0.001),
                                SetVariable("intensity", 0.001)]

                        tooltip "Pause Action"
                        
                        focus_mask True

                imagebutton:
                    idle At("images/interface/Action_menu/auto_idle.webp", interface) hover At("images/interface/Action_menu/auto.webp", interface) selected_idle At("images/interface/Action_menu/auto.webp", interface)

                    selected Action_auto_progress

                    action [
                        ToggleVariable("Action_auto_progress"),
                        SetVariable("Action_auto_progress_timer", 0.0)]

                    tooltip "Auto Progress"
                    
                    focus_mask True

                bar value Action_auto_progress_timer range 5.0 anchor (0.5, 0.5) pos (0.9281, 0.825) xysize (int(419*interface_new_adjustment), int(78*interface_new_adjustment)):
                    left_bar Frame("images/interface/Action_menu/progress_full.webp")
                    right_bar Frame("images/interface/Action_menu/progress_empty.webp")

                    thumb None
                    thumb_offset 0

                    tooltip "Auto Progress Timer"

            if has_Action_control and Player.cock_Actions and len(Player.cock_Actions[0].modes) > 1:
                hbox anchor (0.5, 0.5) pos (0.9281, 0.88) xysize (int(475*interface_new_adjustment), int(177*interface_new_adjustment)):
                    spacing -14

                    for mode in Player.cock_Actions[0].modes:
                        button align (0.5, 0.5) xysize (int(191*interface_new_adjustment), int(177*interface_new_adjustment)):
                            idle_background At("images/interface/Action_menu/mode_idle.webp", interface) hover_background At("images/interface/Action_menu/mode.webp", interface) selected_background At("images/interface/Action_menu/mode.webp", interface)

                            selected Player.cock_Actions[0].mode == mode

                            if len(Player.cock_Actions[0].modes) == 1:
                                text "1" align (0.5, 0.5):
                                    size 32
                            else:
                                text f"{mode}" align (0.5, 0.5):
                                    size 32

                            if Player.cock_Actions[0].mode != mode:
                                action [
                                    SetVariable("speed", 1.0),
                                    SetVariable("intensity", 1.0),
                                    Call("request_mode", Player.cock_Actions[0], mode, from_current = True)]
                            else:
                                action NullAction()

                            tooltip f"{Player.cock_Actions[0].mode_names[Player.cock_Actions[0].modes.index(mode)]}"

            $ different_intensities_available = False

            for Action in ongoing_Actions:
                if Action.speed or Action.intensity:
                    $ different_intensities_available = True

                    break

            if has_movement_control and different_intensities_available:
                imagebutton:
                    idle At("images/interface/Action_menu/x1_idle.webp", interface) hover At("images/interface/Action_menu/x1.webp", interface) selected_idle At("images/interface/Action_menu/x1.webp", interface)

                    selected speed == 0.5 and intensity == 0.5

                    if Player.cock_Actions[0].mode == 0:
                        action [
                            SetVariable("speed", 0.5),
                            SetVariable("intensity", 0.5),
                            SetField(Player.cock_Actions[0], "mode", Player.cock_Actions[0].modes[0])]
                    else:
                        action [
                            SetVariable("speed", 0.5),
                            SetVariable("intensity", 0.5)]

                    tooltip "Set Intensity to 1"
                    
                    focus_mask True

                imagebutton:
                    idle At("images/interface/Action_menu/x2_idle.webp", interface) hover At("images/interface/Action_menu/x2.webp", interface) selected_idle At("images/interface/Action_menu/x2.webp", interface)

                    selected speed == 1.0 and intensity == 1.0

                    if Player.cock_Actions[0].mode == 0:
                        action [
                            SetVariable("speed", 1.0),
                            SetVariable("intensity", 1.0),
                            SetField(Player.cock_Actions[0], "mode", Player.cock_Actions[0].modes[0])]
                    else:
                        action [
                            SetVariable("speed", 1.0),
                            SetVariable("intensity", 1.0)]

                    tooltip "Set Intensity to 2"
                    
                    focus_mask True

                imagebutton:
                    idle At("images/interface/Action_menu/x3_idle.webp", interface) hover At("images/interface/Action_menu/x3.webp", interface) selected_idle At("images/interface/Action_menu/x3.webp", interface)

                    selected speed == 2.0 and intensity == 2.0

                    if Player.cock_Actions[0].mode == 0:
                        action [
                            SetVariable("speed", 2.0),
                            SetVariable("intensity", 2.0),
                            SetField(Player.cock_Actions[0], "mode", Player.cock_Actions[0].modes[0])]
                    else:
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
                        Call("stop_all_Actions"),
                        Return()]
                else:
                    action [
                        SetVariable("Action_screen_showing", False),
                        Call("stop_all_Actions", from_current = True)]

                tooltip "Finish"

                focus_mask True

    if black_screen or (renpy.get_screen("say") and not Action_auto_progress):
        button align (0.5, 0.5) xysize (config.screen_width, config.screen_height):
            background None

            hover_sound None
            activate_sound None
            
            if not renpy.get_screen("choice"):
                action Return()
            else:
                action NullAction()

    use quick_menu

    if tooltips_enabled:
        use tooltips