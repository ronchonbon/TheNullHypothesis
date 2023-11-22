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

                        if Action_screen_showing:
                            action [
                                SetVariable("focused_Girl", C), 
                                SetField(C, "hovered", False)]
                        else:
                            action [
                                SetVariable("focused_Girl", C), 
                                Show("interactions_screen", Character = C), 
                                SetField(C, "hovered", False)]

                if C in all_NPCs and renpy.showing(f"{C.tag}_sprite"):
                    button anchor (C.sprite_anchor[0], C.sprite_anchor[1]) pos (C.sprite_position[0], C.sprite_position[1]):  
                        background None

                        hovered SetField(C, "hovered", True)
                        unhovered SetField(C, "hovered", False)

                        focus_mask renpy.displayable(f"{C.tag}_sprite")

                        action [
                            Show("interactions_screen", Character = C), 
                            SetField(C, "hovered", False)]

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
        frame anchor (0.5, 1.0) pos (0.5, 0.75):
            if Character in all_Companions:
                background "images/interface/interactions/base_Girl.webp"

                xysize (758, 179)

                text f"{Character.love}" anchor (1.0, 0.5) pos (0.2, 0.145) size 30

                text f"{Character.trust}" anchor (1.0, 0.5) pos (0.385, 0.145) size 30 
            else:
                background "images/interface/interactions/base_NPC.webp"

                xysize (758, 125)

            hbox xysize (680, 80):
                if Character in all_Companions:
                    anchor (0.7, 0.5) pos (0.7, 0.7)

                    imagebutton:
                        idle "images/interface/interactions/talk_idle.webp" hover "images/interface/interactions/talk.webp"

                        action Call("chat", Character, from_current = True)

                        tooltip "Chat"

                    imagebutton:
                        idle "images/interface/interactions/gift_idle.webp" hover "images/interface/interactions/gift.webp"

                        action [
                            Hide("interactions_screen"),
                            SetVariable("giving_gift", True),
                            SetVariable("current_Player_menu_page", "inventory"),
                            Show("Player_menu")]

                        tooltip "Give Gift"

                    imagebutton:
                        idle "images/interface/interactions/follow_idle.webp" hover "images/interface/interactions/follow.webp"
                        
                        if Character not in Party:
                            action Call("start_following", Character, from_current = True)

                            tooltip "Start Following"
                        else:
                            action Call("stop_following", Character, from_current = True)

                            tooltip "Stop Following"

                    if approval_check(Character, threshold = "change_Outfit"):
                        imagebutton:
                            idle "images/interface/interactions/wardrobe_idle.webp" hover "images/interface/interactions/wardrobe.webp"

                            action [
                                Hide("interactions_screen"), 
                                Show("Wardrobe_screen", Girl = Character)]

                            tooltip "Open Wardrobe"
                    else:
                        imagebutton:
                            idle "images/interface/interactions/lock_idle.webp" hover "images/interface/interactions/lock.webp"

                            action NullAction()

                    if approval_check(Character, threshold = "hookup"):
                        imagebutton:
                            idle "images/interface/interactions/intimacy_idle.webp" hover "images/interface/interactions/intimacy.webp"

                            action [
                                Hide("interactions_screen"), 
                                Call("request_hookup", Character, from_current = True)]

                            tooltip "Ask to Hookup"
                    else:
                        imagebutton:
                            idle "images/interface/interactions/lock_idle.webp" hover "images/interface/interactions/lock.webp"

                            action NullAction()
                else:
                    anchor (0.7, 0.5) pos (0.7, 0.57)

                    imagebutton:
                        idle "images/interface/interactions/talk_idle.webp" hover "images/interface/interactions/talk.webp"

                        action Call("chat", Character, from_current = True)

                        tooltip "Chat"

                    if Character.is_shop and time_index < 3:
                        imagebutton:
                            idle "images/interface/interactions/shop_idle.webp" hover "images/interface/interactions/shop.webp"

                            action NullAction()

                            tooltip "Open Shop"
                                
                    if Character.gives_work:
                        imagebutton:
                            idle "images/interface/interactions/work_idle.webp" hover "images/interface/interactions/work.webp"

                            action Call("work", Character, from_current = True)

                            tooltip "Ask for Work"

                    if not Character.is_shop:
                        null width 95

                    if not Character.gives_work:
                        null width 95

                    null width 95

                imagebutton:
                    idle "images/interface/interactions/close_idle.webp" hover "images/interface/interactions/close.webp"

                    action [
                        Hide("interactions_screen"), 
                        SetVariable("belt_hidden", False)]

                    tooltip "Close"

    if tooltips_enabled:
        use tooltips