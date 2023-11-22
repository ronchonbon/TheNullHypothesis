init -3:
    
    default dialogue_hidden = False
    default say_obscured = False
    default choice_disabled = False

style choice_button:
    idle_background Frame("images/interface/text_boxes/red_idle.webp", 30, 30)
    hover_background Frame("images/interface/text_boxes/red.webp", 30, 30)

    minimum (int(config.screen_width*0.2), int(config.screen_height*0.07))
    xmaximum int(config.screen_width*0.2)

    # hover_sound "sounds/interface/hover.ogg"
    activate_sound "sounds/interface/press.ogg"

style confirm_frame:
    background Frame("images/interface/box1.webp", 30, 30)

style confirm_button:
    idle_background Frame("images/interface/box1.webp", 30, 30)
    hover_background Frame("images/interface/box2.webp", 30, 30)

    minimum (int(config.screen_width*0.1), int(config.screen_height*0.0))

    # hover_sound "sounds/interface/hover.ogg"
    activate_sound "sounds/interface/press.ogg"

style confirm_text:
    xalign 0.5

screen say(who, what, two_window = False, hide_after = None):
    on "show" action [
        SetVariable("interactions_screen_disabled", True)]
    on "hide" action [
        SetVariable("interactions_screen_disabled", False)]

    if hide_after:
        timer hide_after action Hide("say")

    $ dialogue_anchor = [0.5, 0.0]
    $ dialogue_position = [0.12, 0.08]

    if who == "Player":
        $ C = Player

        $ name = Player.first_name
    elif who in Cast or who in Cameos:
        $ C = eval(who)

        $ name = C.name

        if renpy.showing(f"{C.tag}_sprite") and not say_obscured:
            if C.behavior == "teaching":
                $ dialogue_anchor = [0.0, 0.0]
                $ dialogue_position = [C.sprite_position[0] - 0.02, C.sprite_position[1] - 0.4]
            elif C.sprite_position[0] < stage_far_far_right and C.position not in ["doggy", "masturbation", "missionary"]:
                $ dialogue_anchor = [0.0, 0.0]
                $ dialogue_position = [C.sprite_position[0] + 0.02, C.sprite_position[1] - 0.1]
            elif C.position in ["doggy", "masturbation"]:
                $ dialogue_anchor = [1.0, 0.0]
                $ dialogue_position = [C.sprite_position[0] - 0.08, C.sprite_position[1] - 0.1]
            elif C.position in ["missionary"]:
                $ dialogue_anchor = [0.0, 0.0]
                $ dialogue_position = [C.sprite_position[0] + 0.04, C.sprite_position[1] + 0.05]
            else:
                $ dialogue_anchor = [1.0, 0.0]
                $ dialogue_position = [C.sprite_position[0] - 0.04, C.sprite_position[1] - 0.1]
        elif renpy.get_screen("shop_screen"):
            $ dialogue_anchor = [0.5, 0.0]
            $ dialogue_position = [0.88, 0.05]
    elif who:
        $ C = None
            
    vbox anchor (dialogue_anchor[0], dialogue_anchor[1]) pos (dialogue_position[0], dialogue_position[1]) xsize int(config.screen_width*0.2):
        if who:
            frame:
                if who in ["Reporter", "Dr. Samson"]:
                    background Frame("images/interface/text_boxes/blue.webp", 30, 30)
                elif who in ["Cashier", "Protest Leader", "Protester", "???"]:
                    background Frame("images/interface/text_boxes/white.webp", 30, 30)
                elif C == Player:
                    background Frame("images/interface/text_boxes/red.webp", 30, 30)
                elif C.electronic or C.telepathic:
                    background Frame("images/interface/text_boxes/blue.webp", 30, 30)
                else:
                    background Frame("images/interface/text_boxes/white.webp", 30, 30)

                minimum (int(config.screen_width*0.05), int(config.screen_height*0.07))

                padding (15, 15, 15, 15)

                if C:
                    text name id "who" align (0.5, 0.5):
                        size 32

                        if C != Player and (C.electronic or C.telepathic):
                            color "#000000"
                        else:
                            color eval(f"{C.tag}_color")
                else:
                    text who id "who" align (0.5, 0.5):
                        size 32

                        color "#000000"

        frame:
            if not who:
                background Frame("images/interface/text_boxes/yellow.webp", 30, 30)
            elif who in ["Reporter", "Dr. Samson"]:
                background Frame("images/interface/text_boxes/blue.webp", 30, 30)
            elif who in ["Cashier", "Protest Leader", "Protester", "???"]:
                background Frame("images/interface/text_boxes/white.webp", 30, 30)
            elif C == Player:
                background Frame("images/interface/text_boxes/red.webp", 30, 30)
            elif C.electronic or C.telepathic:
                background Frame("images/interface/text_boxes/blue.webp", 30, 30)
            else:
                background Frame("images/interface/text_boxes/white.webp", 30, 30)

                if renpy.showing(f"{C.tag}_sprite"):
                    xmaximum int(config.screen_width*0.15)

            minimum (int(config.screen_width*0.05), int(config.screen_height*0.07))

            padding (15, 15, 15, 15)

            text what id "what" align (0.5, 0.5):
                text_align 0.5
                
                size 32

                if C == Player or who in Cast or who in Cameos:
                    if C != Player and (C.electronic or C.telepathic):
                        color "#000000"

                        italic True
                    else:
                        color eval(f"{C.tag}_color")
                else:
                    color "#000000"

                if who and C in all_Characters and C.telepathic:
                    italic True

    use quick_menu

screen choice(items, menu_location = None):
    style_prefix "choice"

    if menu_location and menu_location != Player.location:
        on "show" action Call("move_location", Player.location)

    if not dialogue_hidden and not choice_disabled and (not current_phone_Character or not current_phone_Character.mandatory_text_options):
        fixed anchor (0.5, 0.0) pos (0.12, 0.32) xysize (int(config.screen_width*0.2), int(config.screen_height*0.45)):
            viewport id "choice_viewport":
                draggable True
                mousewheel True
                xfill True

                vbox:
                    for caption, action, chosen in items:
                        $ caption = renpy.substitute(caption)

                        if " (locked)" in caption:
                            button:
                                idle_background Frame("images/interface/text_boxes/red_idle.webp", 30, 30) hover_background Frame("images/interface/text_boxes/red_idle.webp", 30, 30)

                                padding (10, 10, 10, 10)
                                
                                text caption.replace(" (locked)", "") align (0.5, 0.5):
                                    size 36

                                    color "#666666"

                                action NullAction()
                        elif " (academic)" in caption:
                            button:
                                padding (10, 10, 10, 10)
                                
                                hbox align (0.5, 0.5) xsize 1.0:
                                    null width 4

                                    fixed yalign 0.5 xysize (int(262*0.15), int(262*0.15)):
                                        add "images/interface/dialogue/academic.webp" yalign 0.5 zoom 0.15

                                    null width 4

                                    frame yalign 0.5 xsize 0.97:
                                        background None

                                        text caption.replace(" (academic)", "") xalign 0.5 xsize 1.0:
                                            size 36

                                action action
                        elif " (athletic)" in caption:
                            button:
                                padding (10, 10, 10, 10)
                                
                                hbox align (0.5, 0.5) xsize 1.0:
                                    null width 4

                                    fixed yalign 0.5 xysize (int(262*0.15), int(262*0.15)):
                                        add "images/interface/dialogue/athletic.webp" yalign 0.5 zoom 0.15

                                    null width 4

                                    frame yalign 0.5 xsize 0.97:
                                        background None

                                        text caption.replace(" (athletic)", "") xalign 0.5 xsize 1.0:
                                            size 36

                                action action
                        elif " (artistic)" in caption:
                            button:
                                padding (10, 10, 10, 10)
                                
                                hbox align (0.5, 0.5) xsize 1.0:
                                    null width 4

                                    fixed yalign 0.5 xysize (int(262*0.15), int(262*0.15)):
                                        add "images/interface/dialogue/artistic.webp" yalign 0.5 zoom 0.15

                                    null width 4

                                    frame yalign 0.5 xsize 0.97:
                                        background None

                                        text caption.replace(" (artistic)", "") xalign 0.5 xsize 1.0:
                                            size 36

                                action action
                        elif " (bitter)" in caption:
                            button:
                                padding (10, 10, 10, 10)
                                
                                hbox align (0.5, 0.5) xsize 1.0:
                                    null width 4

                                    fixed yalign 0.5 xysize (int(262*0.15), int(262*0.15)):
                                        add "images/interface/dialogue/bitter.webp" yalign 0.5 zoom 0.15

                                    null width 4

                                    frame yalign 0.5 xsize 0.97:
                                        background None

                                        text caption.replace(" (bitter)", "") xalign 0.5 xsize 1.0:
                                            size 36

                                action action
                        elif " (determined)" in caption:
                            button:
                                padding (10, 10, 10, 10)
                                
                                hbox align (0.5, 0.5) xsize 1.0:
                                    null width 4

                                    fixed yalign 0.5 xysize (int(262*0.15), int(262*0.15)):
                                        add "images/interface/dialogue/determined.webp" yalign 0.5 zoom 0.15

                                    null width 4

                                    frame yalign 0.5 xsize 0.97:
                                        background None

                                        text caption.replace(" (determined)", "") xalign 0.5 xsize 1.0:
                                            size 36

                                action action
                        elif " (reluctant)" in caption:
                            button:
                                padding (10, 10, 10, 10)
                                
                                hbox align (0.5, 0.5) xsize 1.0:
                                    null width 4

                                    fixed yalign 0.5 xysize (int(262*0.15), int(262*0.15)):
                                        add "images/interface/dialogue/reluctant.webp" yalign 0.5 zoom 0.15

                                    null width 4

                                    frame yalign 0.5 xsize 0.97:
                                        background None

                                        text caption.replace(" (reluctant)", "") xalign 0.5 xsize 1.0:
                                            size 36

                                action action
                        elif " (encourage_quirk)" in caption:
                            button:
                                padding (10, 10, 10, 10)
                                
                                hbox align (0.5, 0.5) xsize 1.0:
                                    null width 4

                                    fixed yalign 0.5 xysize (int(262*0.15), int(262*0.15)):
                                        add "images/interface/dialogue/encourage_quirk.webp" yalign 0.5 zoom 0.15

                                    null width 4

                                    frame yalign 0.5 xsize 0.97:
                                        background None

                                        text caption.replace(" (encourage_quirk)", "") xalign 0.5 xsize 1.0:
                                            size 36

                                action action
                        elif " (discourage_quirk)" in caption:
                            button:
                                padding (10, 10, 10, 10)
                                
                                hbox align (0.5, 0.5) xsize 1.0:
                                    null width 4

                                    fixed yalign 0.5 xysize (int(262*0.15), int(262*0.15)):
                                        add "images/interface/dialogue/discourage_quirk.webp" yalign 0.5 zoom 0.15

                                    null width 4

                                    frame yalign 0.5 xsize 0.97:
                                        background None

                                        text caption.replace(" (discourage_quirk)", "") xalign 0.5 xsize 1.0:
                                            size 36

                                action action
                        else:
                            button:
                                padding (10, 10, 10, 10)

                                text caption align (0.5, 0.5):
                                    size 36

                                action action

            vbar value YScrollValue("choice_viewport") anchor (0.0, 0.0) pos (1.0, 0.0) xsize 25:
                base_bar Frame("images/interface/red_scrollbar.webp")

                thumb "images/interface/red_scrollbar_thumb.webp"
                thumb_offset 5

                unscrollable "hide"

    use quick_menu

screen input(prompt):
    style_prefix "confirm"

    frame anchor (0.5, 0.5) pos (0.5, 0.75):
        padding (25, 25, 25, 25)

        vbox:
            text prompt:
                size 42
                
            input id "input" xalign 0.5:
                size 50

                color "#ffffff"

    use quick_menu

screen confirm(message, yes_action, no_action):
    style_prefix "confirm"

    modal True

    frame anchor (0.5, 0.5) pos (0.5, 0.75):
        padding (25, 25, 25, 25)

        vbox:
            spacing 25

            text _(message):
                size 40
                
            hbox:
                spacing 100

                textbutton _("Yes"): 
                    action yes_action

                    text_size 36

                textbutton _("No"): 
                    action no_action

                    text_size 36

    use quick_menu
