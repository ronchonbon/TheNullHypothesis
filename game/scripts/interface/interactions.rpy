init -1:
    
    default Character_picker_active = True
    default Character_picker_disabled = False

    default interactions_screen_disabled = False
                            
    default giving_gift = False

style interactions is default

style interactions_button:
    # hover_sound "sounds/interface/hover.ogg"
    activate_sound "sounds/interface/press.ogg"

style interactions_image_button:
    # hover_sound "sounds/interface/hover.ogg"
    activate_sound "sounds/interface/press.ogg"

screen Character_picker():
    layer "interface"

    if not black_screen and not Action_screen_showing and Character_picker_active and sandbox and not ongoing_Event and not Character_picker_disabled:
        for C in Present:
            if C.behavior != "teaching":
                if C in all_Companions and renpy.showing(f"{C.tag}_sprite standing"):
                    button anchor (C.sprite_anchor[0], C.sprite_anchor[1]) pos (C.sprite_position[0], C.sprite_position[1]):
                        background None
                        
                        hovered SetField(C, "hovered", True)
                        unhovered SetField(C, "hovered", False)

                        focus_mask renpy.displayable(f"{C.tag}_sprite standing")

                        if C == middle_Slot:
                            action [
                                SetVariable("focused_Companion", C),
                                SetField(C, "hovered", False),
                                Show("interactions_screen", Character = C)]
                        else:
                            action [
                                SetVariable("focused_Companion", C),
                                SetField(C, "hovered", False),
                                Call("set_the_scene", fade = False, selected_Character = C)]

                if C in all_NPCs and renpy.showing(f"{C.tag}_sprite"):
                    button anchor (C.sprite_anchor[0], C.sprite_anchor[1]) pos (C.sprite_position[0], C.sprite_position[1]):  
                        background None

                        hovered SetField(C, "hovered", True)
                        unhovered SetField(C, "hovered", False)

                        focus_mask renpy.displayable(f"{C.tag}_sprite")

                        if C == middle_Slot:
                            action [
                                SetField(C, "hovered", False),
                                Show("interactions_screen", Character = C)]
                        else:
                            action [
                                SetField(C, "hovered", False),
                                Call("set_the_scene", fade = False, selected_Character = C)]

screen interactions_screen(Character):
    layer "interface"
    
    style_prefix "interactions"

    on "show" action [
        SetVariable("belt_hidden", True),
        SetVariable("choice_disabled", True),
        SetVariable("Character_picker_disabled", True)]
    on "hide" action [
        SetVariable("choice_disabled", False),
        SetVariable("Character_picker_disabled", False)]

    if not interactions_screen_disabled:
        button xysize (config.screen_width, config.screen_height):
            background None

            hover_sound None
            activate_sound None
            
            action [
                Hide("interactions_screen"), 
                SetVariable("belt_hidden", False)]

        if Character.sprite_position[0] > stage_far_far_left:
            $ frame_anchor = [1.0, 0.0]
            $ frame_position = [Character.sprite_position[0] - 0.05, Character.sprite_position[1] - 0.1]
        else:
            $ frame_anchor = [0.0, 0.0]
            $ frame_position = [Character.sprite_position[0] + 0.05, Character.sprite_position[1] - 0.1]

        vbox anchor (frame_anchor[0], frame_anchor[1]) pos (frame_position[0], frame_position[1]) xysize (int(450*interface_new_adjustment), int(1100*interface_new_adjustment)):           
            if Character in all_Companions:
                button xalign 0.5 xysize (int(409*interface_new_adjustment), int(130*interface_new_adjustment)):
                    if Character.sprite_position[0] > stage_far_far_left:
                        idle_background At("images/interface/interactions/love_left.webp", interface) hover_background At("images/interface/interactions/love_left.webp", interface)
                    else:
                        idle_background At("images/interface/interactions/love_right.webp", interface) hover_background At("images/interface/interactions/love_right.webp", interface)

                    action NullAction()

                    if Character.sprite_position[0] > stage_far_far_left:
                        text f"{Character.love}" anchor (0.5, 0.5) pos (0.37, 0.52):
                            color "#000000"

                            size 30
                    else:
                        text f"{Character.love}" anchor (0.5, 0.5) pos (0.63, 0.52):
                            color "#000000"

                            size 30

                    tooltip "Love"

                button xalign 0.5 xysize (int(409*interface_new_adjustment), int(130*interface_new_adjustment)):
                    if Character.sprite_position[0] > stage_far_far_left:
                        idle_background At("images/interface/interactions/trust_left.webp", interface) hover_background At("images/interface/interactions/trust_left.webp", interface)
                    else:
                        idle_background At("images/interface/interactions/trust_right.webp", interface) hover_background At("images/interface/interactions/trust_right.webp", interface)

                    action NullAction()

                    if Character.sprite_position[0] > stage_far_far_left:
                        text f"{Character.trust}" anchor (0.5, 0.5) pos (0.37, 0.52):
                            color "#000000"

                            size 30
                    else:
                        text f"{Character.trust}" anchor (0.5, 0.5) pos (0.63, 0.52):
                            color "#000000"

                            size 30

                    tooltip "Trust"

            vpgrid:
                cols 2
                rows 3
            
                if Character in all_Companions:
                    imagebutton:
                        idle At("images/interface/interactions/follow_idle.webp", interface) hover At("images/interface/interactions/follow.webp", interface)
                        
                        if Character not in Party:
                            action Call("start_following", Character, from_current = True)

                            tooltip "Start Following"
                        else:
                            action Call("stop_following", Character, from_current = True)

                            tooltip "Stop Following"
                else:
                    if Character.gives_work:
                        imagebutton:
                            idle At("images/interface/interactions/work_idle.webp", interface) hover At("images/interface/interactions/work.webp", interface)

                            action Call("work", Character, from_current = True)

                            tooltip "Ask for Work"
                    else:
                        null width int(236*interface_new_adjustment) height int(238*interface_new_adjustment)

                imagebutton:
                    idle At("images/interface/interactions/chat_idle.webp", interface) hover At("images/interface/interactions/chat.webp", interface)

                    action Call("chat", Character, from_current = True)

                    tooltip "Chat"

                if Character in all_Companions:
                    imagebutton:
                        idle At("images/interface/interactions/gift_idle.webp", interface) hover At("images/interface/interactions/gift.webp", interface)

                        action [
                            Hide("interactions_screen"),
                            SetVariable("giving_gift", True),
                            SetVariable("current_Player_menu_page", "inventory"),
                            Show("Player_menu")]

                        tooltip "Give Gift"

                    if approval_check(Character, threshold = "change_Outfit"):
                        imagebutton:
                            idle At("images/interface/interactions/wardrobe_idle.webp", interface) hover At("images/interface/interactions/wardrobe.webp", interface)

                            action [
                                Hide("interactions_screen"), 
                                Show("Wardrobe_screen", Companion = Character)]

                            tooltip "Open Wardrobe"
                    else:
                        imagebutton:
                            idle At("images/interface/interactions/lock.webp", interface) hover At("images/interface/interactions/lock.webp", interface)

                            action NullAction()

                    if approval_check(Character, threshold = "hookup") and len(Present) == 1 and Player.location in bedrooms:
                        imagebutton:
                            idle At("images/interface/interactions/hookup_idle.webp", interface) hover At("images/interface/interactions/hookup.webp", interface)

                            action [
                                Hide("interactions_screen"), 
                                Call("request_hookup", Character, from_current = True)]

                            tooltip "Ask to Hookup"
                    else:
                        imagebutton:
                            idle At("images/interface/interactions/lock.webp", interface) hover At("images/interface/interactions/lock.webp", interface)

                            action NullAction()
                else:
                    null width int(236*interface_new_adjustment) height int(238*interface_new_adjustment)

                    null width int(236*interface_new_adjustment) height int(238*interface_new_adjustment)

                    null width int(236*interface_new_adjustment) height int(238*interface_new_adjustment)

                imagebutton:
                    idle At("images/interface/interactions/close_idle.webp", interface) hover At("images/interface/interactions/close.webp", interface)

                    action [
                        Hide("interactions_screen"), 
                        SetVariable("belt_hidden", False)]

                    tooltip "Close"

    if tooltips_enabled:
        use tooltips