init -3:
    
    default dialogue_hidden = False
    default say_obscured = False
    default choice_disabled = False

style choice is default

style choice_button:
    idle_background Frame("images/interface/text_boxes/red_idle.webp", 5, 5)
    hover_background Frame("images/interface/text_boxes/red.webp", 5, 5)

    padding (15, 15, 15, 15)

    xsize 1.0
    yminimum 0.07

style choice_text:
    font "agency_fb.ttf"

    size 36

    color "#000000"

style confirm is default

style confirm_frame:
    background Frame("images/interface/box1.webp", 5, 5)

    padding (25, 25, 25, 25)

style confirm_button:
    idle_background Frame("images/interface/box1.webp", 5, 5)
    hover_background Frame("images/interface/box2.webp", 5, 5)

    padding (15, 15, 15, 15)

    minimum (0.1, 0.07)

screen say(who, what, two_window = False, hide_after = None):
    on "show" action [
        SetVariable("interactions_screen_disabled", True)]
    on "hide" action [
        SetVariable("interactions_screen_disabled", False)]

    if hide_after:
        timer hide_after action Hide("say")

    if Action_screen_showing and Action_auto_progress:
        timer 5.0/(len(ongoing_Actions) + 1) action Return()

    if Action_screen_showing:
        $ dialogue_anchor = [0.5, 0.0]
        $ dialogue_position = [0.12, 0.15]
    else:
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
            
    vbox anchor (dialogue_anchor[0], dialogue_anchor[1]) pos (dialogue_position[0], dialogue_position[1]) xsize 0.2:
        if who:
            frame:
                minimum (0.25, 0.07)

                padding (15, 15, 15, 15)

                if who in ["Reporter", "Dr. Samson"]:
                    background Frame("images/interface/text_boxes/blue.webp", 5, 5)
                elif who in ["Cashier", "Protest Leader", "Protester", "???"]:
                    background Frame("images/interface/text_boxes/white.webp", 5, 5)
                elif C == Player:
                    background Frame("images/interface/text_boxes/red.webp", 5, 5)
                elif C.electronic or C.telepathic:
                    background Frame("images/interface/text_boxes/blue.webp", 5, 5)
                else:
                    background Frame("images/interface/text_boxes/white.webp", 5, 5)

                if C:
                    text name id "who" align (0.5, 0.5):
                        font "agency_fb_bold.ttf"

                        size 32

                        text_align 0.5

                        if C != Player and (C.electronic or C.telepathic):
                            color "#000000"
                        else:
                            color eval(f"{C.tag}_color")

                        bold False
                else:
                    text who id "who" align (0.5, 0.5):
                        font "agency_fb_bold.ttf"

                        size 32

                        text_align 0.5

                        color "#000000"

                        bold False

        frame:
            minimum (0.25, 0.07)

            padding (15, 15, 15, 15)
            
            if not who:
                background Frame("images/interface/text_boxes/yellow.webp", 5, 5)
            elif who in ["Reporter", "Dr. Samson"]:
                background Frame("images/interface/text_boxes/blue.webp", 5, 5)
            elif who in ["Cashier", "Protest Leader", "Protester", "???"]:
                background Frame("images/interface/text_boxes/white.webp", 5, 5)
            elif C == Player:
                background Frame("images/interface/text_boxes/red.webp", 5, 5)
            elif C.electronic or C.telepathic:
                background Frame("images/interface/text_boxes/blue.webp", 5, 5)
            else:
                background Frame("images/interface/text_boxes/white.webp", 5, 5)

                if renpy.showing(f"{C.tag}_sprite"):
                    xmaximum 0.75

            text what id "what" align (0.5, 0.5):
                font "agency_fb.ttf"

                size 32

                text_align 0.5
                
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
        fixed anchor (0.5, 0.0) pos (0.12, 0.32) xysize (0.2, 0.45):
            viewport id "choice_viewport":
                draggable True
                mousewheel True
                xfill True

                vbox:
                    for caption, action, chosen in items:
                        $ caption = renpy.substitute(caption)

                        if " (locked)" in caption:
                            button:
                                hover_background Frame("images/interface/text_boxes/red_idle.webp", 5, 5)
                                
                                text caption.replace(" (locked)", ""):
                                    color "#666666"

                                action NullAction()
                        elif " (academic)" in caption:
                            button:
                                hbox xsize 1.0:
                                    null width 4

                                    fixed xysize (int(262*0.15), int(262*0.15)):
                                        add "images/interface/dialogue/academic.webp" zoom 0.15

                                    null width 4

                                    frame xsize 0.97:
                                        text caption.replace(" (academic)", "") xsize 1.0

                                action action
                        elif " (athletic)" in caption:
                            button:
                                hbox xsize 1.0:
                                    null width 4

                                    fixed xysize (int(262*0.15), int(262*0.15)):
                                        add "images/interface/dialogue/athletic.webp" zoom 0.15

                                    null width 4

                                    frame xsize 0.97:
                                        text caption.replace(" (athletic)", "") xsize 1.0

                                action action
                        elif " (artistic)" in caption:
                            button:
                                hbox xsize 1.0:
                                    null width 4

                                    fixed xysize (int(262*0.15), int(262*0.15)):
                                        add "images/interface/dialogue/artistic.webp" zoom 0.15

                                    null width 4

                                    frame xsize 0.97:
                                        text caption.replace(" (artistic)", "") xsize 1.0

                                action action
                        elif " (bitter)" in caption:
                            button:
                                hbox xsize 1.0:
                                    null width 4

                                    fixed xysize (int(262*0.15), int(262*0.15)):
                                        add "images/interface/dialogue/bitter.webp" zoom 0.15

                                    null width 4

                                    frame xsize 0.97:
                                        text caption.replace(" (bitter)", "") xsize 1.0

                                action action
                        elif " (determined)" in caption:
                            button:
                                hbox xsize 1.0:
                                    null width 4

                                    fixed xysize (int(262*0.15), int(262*0.15)):
                                        add "images/interface/dialogue/determined.webp" zoom 0.15

                                    null width 4

                                    frame xsize 0.97:
                                        text caption.replace(" (determined)", "") xsize 1.0

                                action action
                        elif " (reluctant)" in caption:
                            button:
                                hbox xsize 1.0:
                                    null width 4

                                    fixed xysize (int(262*0.15), int(262*0.15)):
                                        add "images/interface/dialogue/reluctant.webp" zoom 0.15

                                    null width 4

                                    frame xsize 0.97:
                                        text caption.replace(" (reluctant)", "") xsize 1.0

                                action action
                        elif " (encourage_quirk)" in caption:
                            button:
                                hbox xsize 1.0:
                                    null width 4

                                    fixed xysize (int(262*0.15), int(262*0.15)):
                                        add "images/interface/dialogue/encourage_quirk.webp" zoom 0.15

                                    null width 4

                                    frame xsize 0.97:
                                        text caption.replace(" (encourage_quirk)", "") xsize 1.0

                                action action
                        elif " (discourage_quirk)" in caption:
                            button:
                                hbox xsize 1.0:
                                    null width 4

                                    fixed xysize (int(262*0.15), int(262*0.15)):
                                        add "images/interface/dialogue/discourage_quirk.webp" zoom 0.15

                                    null width 4

                                    frame xsize 0.97:
                                        text caption.replace(" (discourage_quirk)", "") xsize 1.0

                                action action
                        else:
                            button:
                                text caption

                                action action

            vbar value YScrollValue("choice_viewport") anchor (0.0, 0.0) pos (1.0, 0.0) xsize 25:
                base_bar Frame("images/interface/red_scrollbar.webp")

                thumb "images/interface/red_scrollbar_thumb.webp"
                thumb_offset 5

                unscrollable "hide"

    use quick_menu

screen confirm(message, yes_action, no_action):
    style_prefix "confirm"

    modal True

    if message == "Are you sure you want to quit?":
        add At("images/interface/exit_popup.webp", interface) align (0.5, 0.5)
                    
        hbox anchor (0.5, 0.5) pos (0.5, 0.64):
            spacing 100

            textbutton _("YES"): 
                text_size 36

                text_color "#ffffff"

                action yes_action

            textbutton _("NO"): 
                text_size 36

                text_color "#ffffff"

                action no_action
    else:
        frame:
            vbox:
                spacing 10

                text _(message):
                    font "agency_fb.ttf"

                    size 40
                    
                hbox:
                    spacing 100

                    textbutton _("YES"): 
                        text_size 36

                        text_color "#ffffff"

                        action yes_action

                    textbutton _("NO"): 
                        text_size 36

                        text_color "#ffffff"

                        action no_action