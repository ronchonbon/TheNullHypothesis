init -1:
    
    default first_name = "John"
    default last_name = "Doe"

    default first_name_value = VariableInputValue("first_name", default = True)
    default last_name_value = VariableInputValue("last_name", default = True)
    
style test is default

style test_image_button:
    # hover_sound "sounds/interface/hover.ogg"
    activate_sound "sounds/interface/press.ogg"

screen test_screen():
    layer "interface"

    style_prefix "test"

    add "images/interface/test/test.webp" align (0.5, 0.5)

    frame anchor (0.0, 0.5) pos (0.41, 0.145) xysize (int(400*interface_sampling), int(70*interface_sampling)):
        background None

        input id "first_name_input" value first_name_value xalign 1.0:
            color "#806757"

            size 30

            length 10
    
    frame anchor (0.0, 0.5) pos (0.41, 0.185) xysize (int(400*interface_sampling), int(70*interface_sampling)):
        background None

        input id "last_name_input" value last_name_value xalign 1.0:
            color "#806757"

            size 30

            length 15

    button anchor (0.0, 0.5) pos (0.41, 0.15) xysize (int(400*interface_sampling), int(70*interface_sampling)):
        background None

        action first_name_value.Toggle()

    button anchor (0.0, 0.5) pos (0.41, 0.1905) xysize (int(400*interface_sampling), int(70*interface_sampling)):
        background None
        
        action last_name_value.Toggle()

    vbox anchor (0.5, 0.0) pos (0.51, 0.32):
        spacing 117

        for item in ["flashing_lights", "comic_filter", "tooltips_enabled", "cinematic_bars"]:
            hbox anchor (0.0, 0.5) pos (0.0, 0.5):
                spacing 50

                imagebutton xysize (int(61*interface_adjustment), int(27*interface_adjustment)):
                    idle "images/interface/test/yes_off.webp" hover "images/interface/test/yes_on.webp" selected_idle "images/interface/test/yes_on.webp"

                    selected eval(item)

                    action SetVariable(item, True)

                imagebutton xysize (int(55*interface_adjustment), int(27*interface_adjustment)):
                    idle "images/interface/test/no_off.webp" hover "images/interface/test/no_on.webp" selected_idle "images/interface/test/no_on.webp"

                    selected not eval(item)

                    action SetVariable(item, False)

    imagebutton align (0.5, 0.5):
        idle "images/interface/test/finish_idle.webp" hover "images/interface/test/finish.webp"

        action Return()

        focus_mask True

    use quick_menu