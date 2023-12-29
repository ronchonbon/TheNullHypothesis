init -1:
    
    default Action_screen_showing = False
    default Action_screen_hidden = False

    default Action_screen_tab = "pose"

    default Action_auto_progress = False
    default Action_auto_progress_timer = 0.0

    default Action_hover_type = None
    default Action_hover_size = 1.0

style Action_screen is default

style Action_screen_text:
    font "agency_fb.ttf"
    
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
        $ focused_Character_index = 0

        for g, G in enumerate(Present):
            if G == focused_Character:
                $ focused_Character_index = g

        add "images/interface/Action_menu/background.webp" zoom interface_new_adjustment

        text f"{Player.stamina}" anchor (0.5, 0.5) pos (0.839, 0.03752):
            size 35

        text f"{focused_Character.stamina}" anchor (0.5, 0.5) pos (0.839, 0.0952):
            size 35

        if Action_hover_type:
            add At(At(At("images/interface/Action_menu/popup.webp", change_anchor(0.5, 0.5)), change_pos(0.825, 0.28)), zoom_sprite(0.5))

            if hookup_length >= max_hookup_length*math.sqrt(focused_Character.max_stamina) and focused_Character.desire <= 75:
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
            left_bar At("images/interface/Action_menu/climax_full_male.webp", interface)
            right_bar At("images/interface/Action_menu/climax_empty.webp", interface)

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

        if focused_Character.desire >= 90:
            add At("images/interface/Action_menu/lightning_female.webp", pulse(intensity = 1.0)) zoom interface_new_adjustment
        elif focused_Character.desire >= 80:
            add At("images/interface/Action_menu/lightning_female.webp", pulse(intensity = 0.8)) zoom interface_new_adjustment
        elif focused_Character.desire >= 70:
            add At("images/interface/Action_menu/lightning_female.webp", pulse(intensity = 0.6)) zoom interface_new_adjustment
        elif focused_Character.desire >= 60:
            add At("images/interface/Action_menu/lightning_female.webp", pulse(intensity = 0.4)) zoom interface_new_adjustment
        elif focused_Character.desire >= 50:
            add At("images/interface/Action_menu/lightning_female.webp", pulse(intensity = 0.2)) zoom interface_new_adjustment

        bar value focused_Character.desire range 100 anchor (0.5, 0.5) pos (0.94, 0.0851) xysize (int(291*interface_new_adjustment), int(37*interface_new_adjustment)):
            left_bar At("images/interface/Action_menu/climax_full_female.webp", interface)
            right_bar At("images/interface/Action_menu/climax_empty.webp", interface)

            thumb None
            thumb_offset 0

            tooltip f"{focused_Character.name}'s Desire"

        if focused_Character.desire >= 90:
            add At("images/interface/Action_menu/glow_female.webp", pulse(intensity = 1.0)) zoom interface_new_adjustment
        elif focused_Character.desire >= 80:
            add At("images/interface/Action_menu/glow_female.webp", pulse(intensity = 0.8)) zoom interface_new_adjustment
        elif focused_Character.desire >= 70:
            add At("images/interface/Action_menu/glow_female.webp", pulse(intensity = 0.6)) zoom interface_new_adjustment
        elif focused_Character.desire >= 60:
            add At("images/interface/Action_menu/glow_female.webp", pulse(intensity = 0.4)) zoom interface_new_adjustment
        elif focused_Character.desire >= 50:
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

            if has_Action_control:
                imagebutton:
                    idle At("images/interface/Action_menu/action_idle.webp", interface) hover At("images/interface/Action_menu/action.webp", interface) selected_idle At("images/interface/Action_menu/action.webp", interface)

                    selected Action_screen_tab == "action"

                    if has_Action_control:
                        action SetVariable("Action_screen_tab", "action")
                    else:
                        action None

                    tooltip "Open Action Menu"

            if has_Action_control:
                imagebutton:
                    idle At("images/interface/Action_menu/strip_idle.webp", interface) hover At("images/interface/Action_menu/strip.webp", interface) selected_idle At("images/interface/Action_menu/strip.webp", interface)

                    selected Action_screen_tab == "strip"

                    if has_Action_control:
                        action [
                            SetVariable("Action_auto_progress", False),
                            SetVariable("Action_auto_progress_timer", 0.0),
                            Call("ask_to_undress", focused_Character, from_current = True)]
                    else:
                        action None

                    tooltip "Open Undressing Menu"

            if Action_screen_tab == "pose":
                if has_position_control:
                    $ pose_list = all_poses[:]

                    for pose in pose_names.keys():
                        if pose in pose_list:
                            if focused_Character.available_poses and pose not in focused_Character.available_poses:
                                $ pose_list.remove(pose)
                            elif focused_Character.possible_poses and pose not in focused_Character.possible_poses:
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

                            button xysize (int(447*interface_new_adjustment), int(177*interface_new_adjustment)):
                                idle_background At("images/interface/Action_menu/button_off.webp", interface) 
                                hover_background At("images/interface/Action_menu/button_on.webp", interface) 
                                selected_idle_background At("images/interface/Action_menu/button_on.webp", interface)

                                selected focused_Character.position == pose

                                text f"{pose_name}":
                                    if len(pose_name) > 18:
                                        size 22
                                    elif len(pose_name) > 15:
                                        size 28
                                    elif len(pose_name) > 12:
                                        size 32
                                    else:
                                        size 35

                                if focused_Character.position != pose:
                                    action [
                                        SetVariable("Action_auto_progress", False),
                                        SetVariable("Action_auto_progress_timer", 0.0),
                                        Call("request_position", focused_Character, pose, from_current = True)]
                                else:
                                    action NullAction()

                    vbar value YScrollValue("pose_viewport") anchor (0.0, 0.0) pos (0.98, 0.276) xysize (int(29*interface_new_adjustment), int(980*interface_new_adjustment)):
                        base_bar Frame(At("images/interface/Action_menu/scrollbar.webp", interface))

                        thumb At("images/interface/Action_menu/scrollbar_thumb.webp", interface)
                        thumb_offset 10

                        unscrollable "hide"
            if Action_screen_tab == "action":
                if has_Action_control:
                    $ current_Action_list = all_Action_types[:]

                    for Action_type in all_Action_types:
                        if Action_type in current_Action_list:
                            if focused_Character.available_Actions and Action_type not in focused_Character.available_Actions:
                                $ current_Action_list.remove(Action_type)
                            elif focused_Character.possible_Actions and Action_type not in focused_Character.possible_Actions:
                                $ current_Action_list.remove(Action_type)
                            elif "touch_thighs" in Action_type:
                                if focused_Character.thighs_covered and "over_clothes" not in Action_type:
                                    $ current_Action_list.remove(Action_type)
                                elif not focused_Character.thighs_covered and "over_clothes" in Action_type:
                                    $ current_Action_list.remove(Action_type)
                            elif "touch_breasts" in Action_type:
                                if focused_Character.breasts_covered and "over_clothes" not in Action_type:
                                    $ current_Action_list.remove(Action_type)
                                elif not focused_Character.breasts_covered and "over_clothes" in Action_type:
                                    $ current_Action_list.remove(Action_type)
                            elif "grab_ass" in Action_type:
                                if focused_Character.ass_covered and "over_clothes" not in Action_type:
                                    $ current_Action_list.remove(Action_type)
                                elif not focused_Character.ass_covered and "over_clothes" in Action_type:
                                    $ current_Action_list.remove(Action_type)
                            elif "touch_pussy" in Action_type and Action_type != "self_touch_pussy":
                                if focused_Character.pussy_covered and "over_clothes" not in Action_type:
                                    $ current_Action_list.remove(Action_type)
                                elif not focused_Character.pussy_covered and "over_clothes" in Action_type:
                                    $ current_Action_list.remove(Action_type)

                    for Action_type in toy_Action_types:
                        if Action_type in current_Action_list:
                            if Action_type in dildo_Action_types and not ("dildo" in Player.inventory.keys() or "dildo" in focused_Character.inventory.keys()):
                                $ current_Action_list.remove(Action_type)
                            elif Action_type in ["self_vibrator", "vibrator"] and not ("vibrator" in Player.inventory.keys() or "vibrator" in focused_Character.inventory.keys()):
                                $ current_Action_list.remove(Action_type)

                    for Action_type in all_Action_types:
                        if Action_type in current_Action_list:
                            $ test_Action = ActionClass(Action_type, None)

                            if focused_Character.position not in test_Action.available_poses:
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
                                            
                        button xysize (int(447*interface_new_adjustment), int(177*interface_new_adjustment)):
                            idle_background At("images/interface/Action_menu/button_off.webp", interface) 
                            hover_background At("images/interface/Action_menu/button_on.webp", interface) 
                            selected_idle_background At("images/interface/Action_menu/button_on.webp", interface)

                            if focused_Character.History.check(Action_type) < unknown_threshold:
                                hovered [
                                    SetVariable("Action_hover_type", "unknown"),
                                    SetVariable("Action_hover_size", 1.0)]
                            elif focused_Character.History.check(Action_type, tracker = "weekly") >= boredom_threshold:
                                hovered [
                                    SetVariable("Action_hover_type", "low"),
                                    SetVariable("Action_hover_size", 0.2)]
                            else:
                                hovered [
                                    SetVariable("Action_hover_type", "high"),
                                    SetVariable("Action_hover_size", eval(f"{focused_Character.tag}_base_Action_desire")*eval(f"{focused_Character.tag}_Action_desires['{Action_type}'][{int(focused_Character.desire/20 % 5)}]"))]
                            
                            unhovered [
                                SetVariable("Action_hover_type", None),
                                SetVariable("Action_hover_size", 1.0)]

                            text "Spank":
                                size 35

                            action Call("spank", focused_Character, from_current = True)

                        for Action_type in current_Action_list:
                            $ Action_name = Action_names[Action_type]

                            $ ongoing_Action = False

                            for A in Player.all_Actions:
                                if A.Action_type == Action_type:
                                    $ ongoing_Action = A

                            if not ongoing_Action:
                                for A in focused_Character.all_Actions:
                                    if A.Action_type == Action_type:
                                        $ ongoing_Action = A

                            button xysize (int(447*interface_new_adjustment), int(177*interface_new_adjustment)):
                                idle_background At("images/interface/Action_menu/button_off.webp", interface) 
                                hover_background At("images/interface/Action_menu/button_on.webp", interface) 
                                selected_idle_background At("images/interface/Action_menu/button_on.webp", interface)

                                selected ongoing_Action

                                if focused_Character.History.check(Action_type) < unknown_threshold:
                                    hovered [
                                        SetVariable("Action_hover_type", "unknown"),
                                        SetVariable("Action_hover_size", 1.0)]
                                elif focused_Character.History.check(Action_type, tracker = "weekly") >= boredom_threshold:
                                    hovered [
                                        SetVariable("Action_hover_type", "low"),
                                        SetVariable("Action_hover_size", 0.2)]
                                else:
                                    hovered [
                                        SetVariable("Action_hover_type", "high"),
                                        SetVariable("Action_hover_size", eval(f"{focused_Character.tag}_base_Action_desire")*eval(f"{focused_Character.tag}_Action_desires['{Action_type}'][{int(focused_Character.desire/20 % 5)}]"))]
                                
                                unhovered [
                                    SetVariable("Action_hover_type", None),
                                    SetVariable("Action_hover_size", 1.0)]

                                text f"{Action_name}":
                                    if len(Action_name) > 18:
                                        size 22
                                    elif len(Action_name) > 15:
                                        size 28
                                    elif len(Action_name) > 12:
                                        size 32
                                    else:
                                        size 35

                                if ongoing_Action:
                                    action [
                                        Function(stop_Action, ongoing_Action)]
                                else:
                                    if "self" in Action_type:
                                        action [
                                            SetVariable("speed", 1.0),
                                            SetVariable("intensity", 1.0),
                                            SetVariable("starting_depth", 0.0),
                                            Call("request_Action", Action_type, focused_Character, focused_Character, from_current = True)]
                                    elif Action_type in active_Action_types:
                                        action [
                                            SetVariable("speed", 1.0),
                                            SetVariable("intensity", 1.0),
                                            SetVariable("starting_depth", 0.0),
                                            Call("request_Action", Action_type, Player, focused_Character, from_current = True)]
                                    elif Action_type in passive_Action_types:
                                        action [
                                            SetVariable("speed", 1.0),
                                            SetVariable("intensity", 1.0),
                                            SetVariable("starting_depth", 0.0),
                                            Call("request_Action", Action_type, focused_Character, Player, from_current = True)]

                    vbar value YScrollValue("Action_viewport") anchor (0.0, 0.0) pos (0.98, 0.276) xysize (int(29*interface_new_adjustment), int(980*interface_new_adjustment)):
                        base_bar Frame(At("images/interface/Action_menu/scrollbar.webp", interface))

                        thumb At("images/interface/Action_menu/scrollbar_thumb.webp", interface)
                        thumb_offset 10

                        unscrollable "hide"

            if ongoing_Actions:
                imagebutton:
                    idle At("images/interface/Action_menu/continue_idle.webp", interface) hover At("images/interface/Action_menu/continue.webp", interface)

                    action [
                        SetVariable("Action_auto_progress", False),
                        SetVariable("Action_auto_progress_timer", 0.0),
                        Call("continue_Actions", from_current = True)]

                    tooltip "Keep Going"

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

                imagebutton:
                    idle At("images/interface/Action_menu/auto_idle.webp", interface) hover At("images/interface/Action_menu/auto.webp", interface) selected_idle At("images/interface/Action_menu/auto.webp", interface)

                    selected Action_auto_progress

                    action [
                        ToggleVariable("Action_auto_progress"),
                        SetVariable("Action_auto_progress_timer", 0.0)]

                    tooltip "Auto Progress"

                bar value Action_auto_progress_timer range 5.0 anchor (0.5, 0.5) pos (0.9281, 0.825) xysize (int(419*interface_new_adjustment), int(78*interface_new_adjustment)):
                    left_bar Frame(At("images/interface/Action_menu/progress_full.webp", interface))
                    right_bar Frame(At("images/interface/Action_menu/progress_empty.webp", interface))

                    thumb None
                    thumb_offset 0

                    tooltip "Auto Progress Timer"

            if has_Action_control and Player.cock_Actions and len(Player.cock_Actions[0].modes) > 1:
                hbox anchor (0.5, 0.5) pos (0.9281, 0.88) xysize (int(475*interface_new_adjustment), int(177*interface_new_adjustment)):
                    spacing -14

                    for mode in Player.cock_Actions[0].modes:
                        button xysize (int(191*interface_new_adjustment), int(177*interface_new_adjustment)):
                            idle_background At("images/interface/Action_menu/mode_idle.webp", interface) 
                            hover_background At("images/interface/Action_menu/mode.webp", interface) 
                            selected_background At("images/interface/Action_menu/mode.webp", interface)

                            selected Player.cock_Actions[0].mode == mode

                            if len(Player.cock_Actions[0].modes) == 1:
                                text "1":
                                    size 32
                            else:
                                text f"{mode}":
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
                        Call("stop_all_Actions", summary = True, from_current = True)]

                tooltip "Finish"

    if black_screen or (renpy.get_screen("say") and not Action_auto_progress):
        button xysize (1.0, 1.0):
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

screen grade_screen(total_Character_orgasms, total_Player_orgasms, total_unique_Actions, score):
    layer "interface"
    
    modal True

    timer 0.5 repeat True action ToggleVariable("blinking")

    frame anchor (0.5, 0.5) pos (0.3, 0.5) xysize (int(878*interface_new_adjustment), int(1056*interface_new_adjustment)):
        background At("images/interface/Action_menu/grade.webp", interface)

        if blinking:
            text "FEEDBACK" + "{alpha=0.0}_{/alpha}" anchor (0.0, 0.5) pos (0.035, 0.067):
                font "agency_fb_bold.ttf"

                size 35
        else:
            text "FEEDBACK" + "_" anchor (0.0, 0.5) pos (0.035, 0.067):
                font "agency_fb_bold.ttf"

                size 35

        vbox anchor (0.5, 0.0) pos (0.482, 0.19) xysize (int(700*interface_new_adjustment), int(350*interface_new_adjustment)):
            spacing 10

            fixed xysize (int(700*interface_new_adjustment), 50):
                text "[focused_Character.name]'s Orgasms" anchor (0.0, 0.5) pos (0.0, 0.5):
                    size 30

                text "[total_Character_orgasms]" anchor (1.0, 0.5) pos (1.0, 0.5):
                    size 35

            fixed xysize (int(700*interface_new_adjustment), 50):
                text "[Player.first_name]'s Orgasms" anchor (0.0, 0.5) pos (0.0, 0.5):
                    size 30

                text "[total_Player_orgasms]" anchor (1.0, 0.5) pos (1.0, 0.5):
                    size 35

            fixed xysize (int(700*interface_new_adjustment), 50):
                text "Unique Actions" anchor (0.0, 0.5) pos (0.0, 0.5):
                    size 30

                text "[total_unique_Actions]" anchor (1.0, 0.5) pos (1.0, 0.5):
                    size 35

        fixed anchor (0.5, 0.5) pos (0.482, 0.755) xysize (int(700*interface_new_adjustment), 75):
            text "Final Grade" anchor (0.0, 0.5) pos (0.0, 0.5):
                size 35

            if score >= 8.0:
                add At("images/interface/Action_menu/A+.webp", interface) anchor (1.0, 0.5) pos (1.0, 0.5)
            elif score >= 4.0:
                add At("images/interface/Action_menu/A.webp", interface) anchor (1.0, 0.5) pos (1.0, 0.5)
            elif score >= 2.0:
                add At("images/interface/Action_menu/B.webp", interface) anchor (1.0, 0.5) pos (1.0, 0.5)
            else:
                add At("images/interface/Action_menu/C.webp", interface) anchor (1.0, 0.5) pos (1.0, 0.5)

        button anchor (0.5, 0.5) pos (0.5, 0.895) xysize (int(374*interface_new_adjustment), int(177*interface_new_adjustment)):
            idle_background At("images/interface/Action_menu/done_idle.webp", interface) 
            hover_background At("images/interface/Action_menu/done.webp", interface)

            text "DONE":
                size 35

            action Return()