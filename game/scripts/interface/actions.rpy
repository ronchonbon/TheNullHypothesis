init -1:
    
    default Action_screen_showing = False
    default Action_screen_hidden = False

    default Action_screen_chat_open = False

    default Action_type_tab = None

    default selected_Action_index = 0
    default selected_Action_mode = 0

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
        SetVariable("Action_screen_chat_open", False),
        SetVariable("Action_type_tab", None),
        SetVariable("belt_hidden", True),
        Hide("interactions_screen"),
        SetVariable("choice_disabled", True)]

    if not black_screen:
        $ focused_Girl_index = 0

        for g, G in enumerate(Present):
            if G == focused_Girl:
                $ focused_Girl_index = g

        if has_progression_control:
            fixed anchor (1.0, 1.0) pos (1.0, 1.0) xysize (191, 557):
                add "images/interface/Action_menu/main_menu.webp"

                imagebutton anchor (0.5, 0.5) pos (0.5, 0.8):
                    idle "images/interface/Action_menu/exit_idle.webp" hover "images/interface/Action_menu/exit.webp"

                    if automatic:
                        action [
                            SetVariable("Action_screen_showing", False),
                            Call("stop_all_Actions", close_interface = True),
                            Return()]
                    else:
                        action [
                            SetVariable("Action_screen_showing", False),
                            Call("stop_all_Actions", close_interface = True, from_current = True)]

                    tooltip "Exit"

                bar value focused_Girl.desire + 24 range 127 anchor (0.5, 0.5) pos (0.5, 0.25) xysize (178, 49):
                    left_bar Frame("images/interface/Action_menu/climax_female.webp")
                    right_bar Frame("images/interface/Action_menu/climax_female_empty.webp")

                    thumb None
                    thumb_offset 0

                    tooltip f"{focused_Girl.name}'s Desire"

                bar value Player.desire + 24 range 127 anchor (0.5, 0.5) pos (0.5, 0.35) xysize (178, 49):
                    left_bar Frame("images/interface/Action_menu/climax_male.webp")
                    right_bar Frame("images/interface/Action_menu/climax_male_empty.webp")

                    thumb None
                    thumb_offset 0

                    tooltip f"{Player.first_name}'s Desire"

        if has_Action_control:
            fixed anchor (0.0, 1.0) pos (0.0, 1.0) xysize (191, 1083):
                if Action_screen_chat_open:
                    add "images/interface/Action_menu/chat_menu.webp" anchor (0.5, 1.0) pos (0.5, 1.0) xzoom -1.0

                    imagebutton anchor (0.5, 0.5) pos (0.615, 0.1):
                        idle "images/interface/Action_menu/mouth_idle.webp" hover "images/interface/Action_menu/mouth.webp" selected_idle "images/interface/Action_menu/mouth_selected.webp"

                        selected Action_type_tab == "mouth"

                        if Action_type_tab == "mouth":
                            action SetVariable("Action_type_tab", None)
                        else:
                            action SetVariable("Action_type_tab", "mouth")

                        tooltip "Mouth Actions"

                    imagebutton anchor (0.5, 0.5) pos (0.615, 0.2333):
                        idle "images/interface/Action_menu/hand_idle.webp" hover "images/interface/Action_menu/hand.webp" selected_idle "images/interface/Action_menu/hand_selected.webp"

                        selected Action_type_tab == "hand"

                        if Action_type_tab == "hand":
                            action SetVariable("Action_type_tab", None)
                        else:
                            action SetVariable("Action_type_tab", "hand")

                        tooltip "Hand Actions"

                    imagebutton anchor (0.5, 0.5) pos (0.615, 0.3666):
                        idle "images/interface/Action_menu/upper_idle.webp" hover "images/interface/Action_menu/upper.webp" selected_idle "images/interface/Action_menu/upper_selected.webp"

                        selected Action_type_tab == "upper"

                        if Action_type_tab == "upper":
                            action SetVariable("Action_type_tab", None)
                        else:
                            action SetVariable("Action_type_tab", "upper")

                        tooltip "Upper Body Actions"

                    imagebutton anchor (0.5, 0.5) pos (0.615, 0.5):
                        idle "images/interface/Action_menu/lower_idle.webp" hover "images/interface/Action_menu/lower.webp" selected_idle "images/interface/Action_menu/lower_selected.webp"

                        selected Action_type_tab == "lower"

                        if Action_type_tab == "lower":
                            action SetVariable("Action_type_tab", None)
                        else:
                            action SetVariable("Action_type_tab", "lower")

                        tooltip "Lower Body Actions"

                    imagebutton anchor (0.5, 0.5) pos (0.615, 0.6333):
                        idle "images/interface/Action_menu/undress_idle.webp" hover "images/interface/Action_menu/undress.webp"

                        action [
                            SetVariable("Action_screen_chat_open", False),
                            SetVariable("Action_type_tab", None),
                            Call("ask_to_undress", focused_Girl, from_current = True)]

                        tooltip "Undress"

                    imagebutton anchor (0.5, 0.5) pos (0.615, 0.7666):
                        idle "images/interface/Action_menu/spank_idle.webp" hover "images/interface/Action_menu/spank.webp"

                        action Call("spank", focused_Girl, from_current = True)

                        tooltip "Spank"
                else:
                    add "images/interface/Action_menu/chat_menu_closed.webp" anchor (0.5, 1.0) pos (0.5, 1.0) xzoom -1.0

                imagebutton anchor (0.5, 0.5) pos (0.615, 0.9):
                    idle "images/interface/Action_menu/chat_idle.webp" hover "images/interface/Action_menu/chat.webp" selected_idle "images/interface/Action_menu/chat_selected.webp"

                    selected Action_screen_chat_open

                    if Action_screen_chat_open:
                        action [
                            SetVariable("Action_type_tab", None),
                            SetVariable("Action_screen_chat_open", False)]
                    else:
                        action SetVariable("Action_screen_chat_open", True)

                    tooltip "Choose an Action"

            if Action_screen_chat_open and Action_type_tab:
                fixed anchor (0.0, 0.0) pos (0.11, 0.01) xysize (507, 629):
                    add "images/interface/Action_menu/selection_window.webp"
                    
                    viewport id "Action_viewport" anchor (0.5, 0.0) pos (0.475, 0.03) xysize (431, 525):
                        draggable True
                        mousewheel True

                        vbox xalign 0.5:
                            spacing 1

                            $ current_Action_list = eval(f"{Action_type_tab}_Action_types")[:]

                            for Action_type in all_Action_types:
                                if Action_type in current_Action_list:
                                    if focused_Girl.available_Actions and Action_type not in focused_Girl.available_Actions:
                                        $ current_Action_list.remove(Action_type)
                                    elif focused_Girl.possible_Actions and Action_type not in focused_Girl.possible_Actions:
                                        $ current_Action_list.remove(Action_type)
                                    elif "touch_thighs" in Action_type:
                                        if focused_Girl.thighs_covered and "over_clothes" not in Action_type:
                                            $ current_Action_list.remove(Action_type)
                                        elif not focused_Girl.thighs_covered and "over_clothes" in Action_type:
                                            $ current_Action_list.remove(Action_type)
                                    elif "touch_breasts" in Action_type:
                                        if focused_Girl.breasts_covered and "over_clothes" not in Action_type:
                                            $ current_Action_list.remove(Action_type)
                                        elif not focused_Girl.breasts_covered and "over_clothes" in Action_type:
                                            $ current_Action_list.remove(Action_type)
                                    elif "grab_ass" in Action_type:
                                        if focused_Girl.ass_covered and "over_clothes" not in Action_type:
                                            $ current_Action_list.remove(Action_type)
                                        elif not focused_Girl.ass_covered and "over_clothes" in Action_type:
                                            $ current_Action_list.remove(Action_type)
                                    elif "touch_pussy" in Action_type and Action_type != "self_touch_pussy":
                                        if focused_Girl.pussy_covered and "over_clothes" not in Action_type:
                                            $ current_Action_list.remove(Action_type)
                                        elif not focused_Girl.pussy_covered and "over_clothes" in Action_type:
                                            $ current_Action_list.remove(Action_type)

                            for Action_type in toy_Action_types:
                                if Action_type in current_Action_list:
                                    if Action_type in dildo_Action_types and not ("dildo" in Player.inventory.keys() or "dildo" in focused_Girl.inventory.keys()):
                                        $ current_Action_list.remove(Action_type)
                                    elif Action_type in ["self_vibrator", "vibrator"] and not ("vibrator" in Player.inventory.keys() or "vibrator" in focused_Girl.inventory.keys()):
                                        $ current_Action_list.remove(Action_type)

                            for Action_type in current_Action_list:
                                $ Action_name = Action_names[Action_type]

                                $ ongoing_Action = False

                                for A in Player.all_Actions:
                                    if A.Action_type == Action_type:
                                        $ ongoing_Action = A

                                if not ongoing_Action:
                                    for A in focused_Girl.all_Actions:
                                        if A.Action_type == Action_type:
                                            $ ongoing_Action = A

                                button align (0.5, 0.5) xysize (431, 71):
                                    if Action_type in active_Action_types:
                                        idle_background "images/interface/Action_menu/male_idle.webp" hover_background "images/interface/Action_menu/male.webp" selected_background "images/interface/Action_menu/male_selected.webp"
                                    elif Action_type in passive_Action_types:
                                        idle_background "images/interface/Action_menu/female_idle.webp" hover_background "images/interface/Action_menu/female.webp" selected_background "images/interface/Action_menu/female_selected.webp"

                                    selected ongoing_Action

                                    text f"{Action_name}" anchor (0.5, 0.5) pos (0.55, 0.5):
                                        size 32

                                    if ongoing_Action:
                                        action [
                                            Function(stop_Action, ongoing_Action),
                                            SetVariable("selected_Action_index", 0)]
                                    else:
                                        if Action_type in ["self_touch_pussy", "self_finger_ass", "self_vibrator", "self_dildo_pussy", "self_dildo_ass"]:
                                            action [
                                                SetVariable("speed", 1.0),
                                                SetVariable("intensity", 1.0),
                                                SetVariable("starting_depth", 0.0),
                                                SetVariable("Action_screen_chat_open", False),
                                                Call("request_Action", Action_type, focused_Girl, focused_Girl, from_current = True)]
                                        elif Action_type in active_Action_types:
                                            action [
                                                SetVariable("speed", 1.0),
                                                SetVariable("intensity", 1.0),
                                                SetVariable("starting_depth", 0.0),
                                                SetVariable("Action_screen_chat_open", False),
                                                Call("request_Action", Action_type, Player, focused_Girl, from_current = True)]
                                        elif Action_type in passive_Action_types:
                                            action [
                                                SetVariable("speed", 1.0),
                                                SetVariable("intensity", 1.0),
                                                SetVariable("starting_depth", 0.0),
                                                SetVariable("Action_screen_chat_open", False),
                                                Call("request_Action", Action_type, focused_Girl, Player, from_current = True)]

                    vbar value YScrollValue("Action_viewport") anchor (0.0, 0.0) pos (0.925, 0.03) xysize (22, 525):
                        base_bar Frame("images/interface/Action_menu/scrollbar.webp")

                        thumb "images/interface/Action_menu/scrollbar_thumb.webp"
                        thumb_offset 10

                        unscrollable "hide"

                    if len(Present) > 1:
                        imagebutton anchor (0.5, 0.5) pos (0.3, 0.94):
                            idle "images/interface/Action_menu/left_idle.webp" hover "images/interface/Action_menu/left.webp"

                            action [
                                SetVariable("focused_Girl_index", (focused_Girl_index - 1) % len(Present)),
                                SetVariable("focused_Girl", Present[(focused_Girl_index - 1) % len(Present)])]

                    text f"{focused_Girl.name}" anchor (0.5, 0.5) pos (0.5, 0.94):
                        size 32

                    if len(Present) > 1:
                        imagebutton anchor (0.5, 0.5) pos (0.7, 0.94):
                            idle "images/interface/Action_menu/right_idle.webp" hover "images/interface/Action_menu/right.webp"

                            action [
                                SetVariable("focused_Girl_index", (focused_Girl_index + 1) % len(Present)),
                                SetVariable("focused_Girl", Present[(focused_Girl_index + 1) % len(Present)])]

        if ongoing_Actions and (has_Action_control or has_movement_control or has_position_control):
            fixed anchor (1.0, 0.0) pos (0.995, 0.01) xysize (607, 409):
                if len(ongoing_Actions) == 1:
                    add "images/interface/Action_menu/action1.webp"
                elif len(ongoing_Actions) == 2:
                    if selected_Action_index == 0:
                        imagebutton anchor (0.5, 1.0) pos (0.5, 1.0) xysize (607, 409):
                            idle "images/interface/Action_menu/action2_idle.webp" hover "images/interface/Action_menu/action2.webp"

                            hover_sound None

                            action SetVariable("selected_Action_index", 1)

                            focus_mask True

                        imagebutton anchor (0.5, 1.0) pos (0.5, 1.0) xysize (607, 409):
                            idle "images/interface/Action_menu/action1.webp" hover "images/interface/Action_menu/action1.webp"

                            hover_sound None

                            action NullAction()

                            focus_mask True
                    else:
                        imagebutton anchor (0.5, 1.0) pos (0.5, 1.0) xysize (607, 409):
                            idle "images/interface/Action_menu/action1_idle.webp" hover "images/interface/Action_menu/action1.webp"

                            hover_sound None

                            action SetVariable("selected_Action_index", 0)

                            focus_mask True

                        imagebutton anchor (0.5, 1.0) pos (0.5, 1.0) xysize (607, 409):
                            idle "images/interface/Action_menu/action2.webp" hover "images/interface/Action_menu/action2.webp"

                            hover_sound None

                            action NullAction()

                            focus_mask True
                elif len(ongoing_Actions) == 3:
                    if selected_Action_index == 0:
                        imagebutton anchor (0.5, 1.0) pos (0.5, 1.0) xysize (607, 409):
                            idle "images/interface/Action_menu/action2_idle.webp" hover "images/interface/Action_menu/action2.webp"

                            hover_sound None

                            action SetVariable("selected_Action_index", 1)

                            focus_mask True

                        imagebutton anchor (0.5, 1.0) pos (0.5, 1.0) xysize (607, 409):
                            idle "images/interface/Action_menu/action3_idle.webp" hover "images/interface/Action_menu/action3.webp"

                            hover_sound None

                            action SetVariable("selected_Action_index", 2)

                            focus_mask True

                        imagebutton anchor (0.5, 1.0) pos (0.5, 1.0) xysize (607, 409):
                            idle "images/interface/Action_menu/action1.webp" hover "images/interface/Action_menu/action1.webp"

                            hover_sound None

                            action NullAction()

                            focus_mask True
                    elif selected_Action_index == 1:
                        imagebutton anchor (0.5, 1.0) pos (0.5, 1.0) xysize (607, 409):
                            idle "images/interface/Action_menu/action1_idle.webp" hover "images/interface/Action_menu/action1.webp"

                            hover_sound None

                            action SetVariable("selected_Action_index", 0)

                            focus_mask True

                        imagebutton anchor (0.5, 1.0) pos (0.5, 1.0) xysize (607, 409):
                            idle "images/interface/Action_menu/action3_idle.webp" hover "images/interface/Action_menu/action3.webp"

                            hover_sound None

                            action SetVariable("selected_Action_index", 2)

                            focus_mask True

                        imagebutton anchor (0.5, 1.0) pos (0.5, 1.0) xysize (607, 409):
                            idle "images/interface/Action_menu/action2.webp" hover "images/interface/Action_menu/action2.webp"

                            hover_sound None

                            action NullAction()

                            focus_mask True
                    elif selected_Action_index == 2:
                        imagebutton anchor (0.5, 1.0) pos (0.5, 1.0) xysize (607, 409):
                            idle "images/interface/Action_menu/action1_idle.webp" hover "images/interface/Action_menu/action1.webp"

                            hover_sound None

                            action SetVariable("selected_Action_index", 0)

                            focus_mask True

                        imagebutton anchor (0.5, 1.0) pos (0.5, 1.0) xysize (607, 409):
                            idle "images/interface/Action_menu/action2_idle.webp" hover "images/interface/Action_menu/action2.webp"

                            hover_sound None

                            action SetVariable("selected_Action_index", 1)

                            focus_mask True

                        imagebutton anchor (0.5, 1.0) pos (0.5, 1.0) xysize (607, 409):
                            idle "images/interface/Action_menu/action3.webp" hover "images/interface/Action_menu/action3.webp"

                            hover_sound None

                            action NullAction()

                            focus_mask True
                elif len(ongoing_Actions) > 3:
                    if selected_Action_index == 0:
                        imagebutton anchor (0.5, 1.0) pos (0.5, 1.0) xysize (607, 409):
                            idle "images/interface/Action_menu/action2_idle.webp" hover "images/interface/Action_menu/action2.webp"

                            hover_sound None

                            action SetVariable("selected_Action_index", 1)

                            focus_mask True

                        imagebutton anchor (0.5, 1.0) pos (0.5, 1.0) xysize (607, 409):
                            idle "images/interface/Action_menu/action3_idle.webp" hover "images/interface/Action_menu/action3.webp"

                            hover_sound None

                            action SetVariable("selected_Action_index", 2)

                            focus_mask True

                        imagebutton anchor (0.5, 1.0) pos (0.5, 1.0) xysize (607, 409):
                            idle "images/interface/Action_menu/action4_idle.webp" hover "images/interface/Action_menu/action4.webp"

                            hover_sound None

                            action SetVariable("selected_Action_index", 3)

                            focus_mask True

                        imagebutton anchor (0.5, 1.0) pos (0.5, 1.0) xysize (607, 409):
                            idle "images/interface/Action_menu/action1.webp" hover "images/interface/Action_menu/action1.webp"

                            hover_sound None

                            action NullAction()

                            focus_mask True
                    elif selected_Action_index == 1:
                        imagebutton anchor (0.5, 1.0) pos (0.5, 1.0) xysize (607, 409):
                            idle "images/interface/Action_menu/action1_idle.webp" hover "images/interface/Action_menu/action1.webp"

                            hover_sound None

                            action SetVariable("selected_Action_index", 0)

                            focus_mask True

                        imagebutton anchor (0.5, 1.0) pos (0.5, 1.0) xysize (607, 409):
                            idle "images/interface/Action_menu/action3_idle.webp" hover "images/interface/Action_menu/action3.webp"

                            hover_sound None

                            action SetVariable("selected_Action_index", 2)

                            focus_mask True

                        imagebutton anchor (0.5, 1.0) pos (0.5, 1.0) xysize (607, 409):
                            idle "images/interface/Action_menu/action4_idle.webp" hover "images/interface/Action_menu/action4.webp"

                            hover_sound None

                            action SetVariable("selected_Action_index", 3)

                            focus_mask True

                        imagebutton anchor (0.5, 1.0) pos (0.5, 1.0) xysize (607, 409):
                            idle "images/interface/Action_menu/action2.webp" hover "images/interface/Action_menu/action2.webp"

                            hover_sound None

                            action NullAction()

                            focus_mask True
                    elif selected_Action_index == 2:
                        imagebutton anchor (0.5, 1.0) pos (0.5, 1.0) xysize (607, 409):
                            idle "images/interface/Action_menu/action1_idle.webp" hover "images/interface/Action_menu/action1.webp"

                            hover_sound None

                            action SetVariable("selected_Action_index", 0)

                            focus_mask True

                        imagebutton anchor (0.5, 1.0) pos (0.5, 1.0) xysize (607, 409):
                            idle "images/interface/Action_menu/action2_idle.webp" hover "images/interface/Action_menu/action2.webp"

                            hover_sound None

                            action SetVariable("selected_Action_index", 1)

                            focus_mask True

                        imagebutton anchor (0.5, 1.0) pos (0.5, 1.0) xysize (607, 409):
                            idle "images/interface/Action_menu/action4_idle.webp" hover "images/interface/Action_menu/action4.webp"

                            hover_sound None

                            action SetVariable("selected_Action_index", 3)

                            focus_mask True

                        imagebutton anchor (0.5, 1.0) pos (0.5, 1.0) xysize (607, 409):
                            idle "images/interface/Action_menu/action3.webp" hover "images/interface/Action_menu/action3.webp"

                            hover_sound None

                            action NullAction()

                            focus_mask True
                    elif selected_Action_index > 2:
                        imagebutton anchor (0.5, 1.0) pos (0.5, 1.0) xysize (607, 409):
                            idle "images/interface/Action_menu/action1_idle.webp" hover "images/interface/Action_menu/action1.webp"

                            hover_sound None

                            action SetVariable("selected_Action_index", 0)

                            focus_mask True

                        imagebutton anchor (0.5, 1.0) pos (0.5, 1.0) xysize (607, 409):
                            idle "images/interface/Action_menu/action2_idle.webp" hover "images/interface/Action_menu/action2.webp"

                            hover_sound None

                            action SetVariable("selected_Action_index", 1)

                            focus_mask True

                        imagebutton anchor (0.5, 1.0) pos (0.5, 1.0) xysize (607, 409):
                            idle "images/interface/Action_menu/action3_idle.webp" hover "images/interface/Action_menu/action3.webp"

                            hover_sound None

                            action SetVariable("selected_Action_index", 2)

                            focus_mask True

                        if len(ongoing_Actions) > 4:
                            imagebutton anchor (0.5, 1.0) pos (0.5, 1.0) xysize (607, 409):
                                idle "images/interface/Action_menu/action4.webp" hover "images/interface/Action_menu/action4.webp"

                                hover_sound None

                                action SetVariable("selected_Action_index", (selected_Action_index + 1) % len(ongoing_Actions))

                                focus_mask True
                        else:
                            imagebutton anchor (0.5, 1.0) pos (0.5, 1.0) xysize (607, 409):
                                idle "images/interface/Action_menu/action4.webp" hover "images/interface/Action_menu/action4.webp"

                                hover_sound None

                                action NullAction()

                                focus_mask True

                $ count = 0

                for a, A in enumerate(ongoing_Actions):
                    $ count += 1
                
                    if count < 4:
                        $ Action_name = Action_names[A.Action_type]
                    
                        text Action_name anchor (0.5, 0.5) pos (0.146 + 0.278*a, 0.0875):
                            if len(Action_name) > 15:
                                size 24
                            else:
                                size 28

                            xmaximum 150
                    else:
                        text ". . ." anchor (0.5, 0.5) pos (0.915, 0.063):
                            size 36

                if has_movement_control:
                    if selected_Action_index > len(ongoing_Actions) - 1:
                        $ selected_Action_index = 0

                    if selected_Action_mode:
                        if selected_Action_mode not in ongoing_Actions[selected_Action_index].modes:
                            $ selected_Action_mode = ongoing_Actions[selected_Action_index].modes[0]

                        $ mode_index = ongoing_Actions[selected_Action_index].modes.index(selected_Action_mode)

                        if ongoing_Actions[selected_Action_index].speed is not None and ongoing_Actions[selected_Action_index].max_speed[mode_index] != ongoing_Actions[selected_Action_index].min_speed[mode_index]:
                            bar value VariableValue("speed", ongoing_Actions[selected_Action_index].max_speed[mode_index], offset = ongoing_Actions[selected_Action_index].min_speed[mode_index]) anchor (0.5, 0.5) pos (0.16, 0.585) xysize (116, 15):
                                base_bar Frame("images/interface/Action_menu/control_scrollbar.webp")

                                thumb "images/interface/Action_menu/control_scrollbar_thumb.webp"
                                thumb_offset 9

                            text "Speed" anchor (0.5, 0.5) pos (0.16, 0.5):
                                size 24

                        if ongoing_Actions[selected_Action_index].intensity is not None and ongoing_Actions[selected_Action_index].max_intensity[mode_index] != ongoing_Actions[selected_Action_index].min_intensity[mode_index]:
                            bar value VariableValue("intensity", ongoing_Actions[selected_Action_index].max_intensity[mode_index], offset = ongoing_Actions[selected_Action_index].min_intensity[mode_index]) anchor (0.5, 0.5) pos (0.16, 0.805) xysize (116, 15):
                                base_bar Frame("images/interface/Action_menu/control_scrollbar.webp")

                                thumb "images/interface/Action_menu/control_scrollbar_thumb.webp"
                                thumb_offset 9

                            text "Intensity" anchor (0.5, 0.5) pos (0.16, 0.72):
                                size 24
                    elif changing_speed or changing_intensity:
                        if ongoing_Actions[selected_Action_index].speed is not None and ongoing_Actions[selected_Action_index].max_speed[mode_index] != ongoing_Actions[selected_Action_index].min_speed[mode_index]:
                            bar value VariableValue("speed", ongoing_Actions[selected_Action_index].max_speed[mode_index], offset = ongoing_Actions[selected_Action_index].min_speed[mode_index]) anchor (0.5, 0.5) pos (0.16, 0.585) xysize (116, 15):
                                base_bar Frame("images/interface/Action_menu/control_scrollbar.webp")

                                thumb "images/interface/Action_menu/control_scrollbar_thumb.webp"
                                thumb_offset 9

                            text "Speed" anchor (0.5, 0.5) pos (0.16, 0.5):
                                size 24

                        if ongoing_Actions[selected_Action_index].intensity is not None and ongoing_Actions[selected_Action_index].max_intensity[mode_index] != ongoing_Actions[selected_Action_index].min_intensity[mode_index]:
                            bar value VariableValue("intensity", ongoing_Actions[selected_Action_index].max_intensity[mode_index], offset = ongoing_Actions[selected_Action_index].min_intensity[mode_index]) anchor (0.5, 0.5) pos (0.16, 0.805) xysize (116, 15):
                                base_bar Frame("images/interface/Action_menu/control_scrollbar.webp")

                                thumb "images/interface/Action_menu/control_scrollbar_thumb.webp"
                                thumb_offset 9

                            text "Intensity" anchor (0.5, 0.5) pos (0.16, 0.72):
                                size 24

                if has_Action_control:
                    imagebutton anchor (0.5, 0.5) pos (0.72, 0.585):
                        idle "images/interface/Action_menu/pause_idle.webp" hover "images/interface/Action_menu/pause.webp"

                        action [
                            SetVariable("selected_Action_mode", 0),
                            SetField(ongoing_Actions[selected_Action_index], "mode", 0)]

                        tooltip "Pause Action"

                    imagebutton anchor (0.5, 0.5) pos (0.72, 0.805):
                        idle "images/interface/Action_menu/stop_idle.webp" hover "images/interface/Action_menu/stop.webp"

                        action [
                            Function(stop_Action, ongoing_Actions[selected_Action_index]),
                            SetVariable("selected_Action_index", 0)]

                        tooltip "Stop Action"

                imagebutton anchor (0.5, 0.5) pos (0.87, 0.695):
                    idle "images/interface/Action_menu/continue_idle.webp" hover "images/interface/Action_menu/continue.webp"

                    action Call("continue_Actions", from_current = True)

                    tooltip "Keep Going"

                if has_Action_control:
                    vpgrid anchor (0.5, 0.5) pos (0.46, 0.695) xysize (180, 180):
                        cols 2

                        spacing 1

                        for mode in ongoing_Actions[selected_Action_index].modes:
                            button align (0.5, 0.5) xysize (89, 88):
                                idle_background "images/interface/Action_menu/mode_idle.webp" hover_background "images/interface/Action_menu/mode.webp" selected_background "images/interface/Action_menu/mode_selected.webp"

                                selected selected_Action_mode == mode

                                if len(ongoing_Actions[selected_Action_index].modes) == 1:
                                    text "1" align (0.5, 0.5):
                                        size 32
                                else:
                                    text f"{mode}" align (0.5, 0.5):
                                        size 32

                                if selected_Action_mode != mode:
                                    action Call("request_mode", ongoing_Actions[selected_Action_index], mode, from_current = True)
                                else:
                                    action NullAction()

                                tooltip "Change Mode"

                if has_position_control:
                    $ pose_list = ongoing_Actions[selected_Action_index].available_poses[:]

                    for pose in pose_names.keys():
                        if pose in pose_list:
                            if focused_Girl.available_poses and pose not in focused_Girl.available_poses:
                                $ pose_list.remove(pose)
                            elif focused_Girl.possible_poses and pose not in focused_Girl.possible_poses:
                                $ pose_list.remove(pose)

                    hbox anchor (0.5, 0.5) pos (0.5, 0.275) xysize (600, 88):
                        spacing -100

                        for pose in pose_list:
                            $ pose_name = pose_names[pose]

                            button align (0.5, 0.5) xysize (200, 88):
                                background None

                                hover_sound None

                                selected ongoing_Actions[selected_Action_index].position == pose

                                text f"{pose_name}" align (0.5, 0.5):
                                    if len(pose_name) > 12:
                                        size 26
                                    else:
                                        size 32

                                    text_align 0.5

                                    idle_color "#000000" hover_color "#ffffff" selected_color "#ffffff"

                                if ongoing_Actions[selected_Action_index].position != pose:
                                    action Call("request_position", focused_Girl, pose, ongoing_Actions[selected_Action_index], from_current = True)
                                else:
                                    action NullAction()

                                # tooltip "Change Position"

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