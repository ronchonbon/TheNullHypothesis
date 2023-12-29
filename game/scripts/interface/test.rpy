init -1:
    
    default first_name = "John"
    default last_name = "Doe"

    default first_name_value = VariableInputValue("first_name", default = True)
    default last_name_value = VariableInputValue("last_name", default = True)
    
style test is default

screen test_screen():
    layer "interface"

    style_prefix "test"

    add "images/interface/test/test.webp" zoom interface_new_adjustment

    frame anchor (0.0, 0.5) pos (0.41, 0.145) xysize (int(400*interface_new_adjustment), int(70*interface_new_adjustment)):
        input id "first_name_input" value first_name_value xalign 1.0:
            font "agency_fb.ttf"

            color "#806757"

            size 30

            length 10
    
    frame anchor (0.0, 0.5) pos (0.41, 0.185) xysize (int(400*interface_new_adjustment), int(70*interface_new_adjustment)):
        input id "last_name_input" value last_name_value xalign 1.0:
            font "agency_fb.ttf"

            color "#806757"

            size 30

            length 15

    button anchor (0.0, 0.5) pos (0.41, 0.15) xysize (int(400*interface_new_adjustment), int(70*interface_new_adjustment)):
        background None

        action first_name_value.Toggle()

    button anchor (0.0, 0.5) pos (0.41, 0.1905) xysize (int(400*interface_new_adjustment), int(70*interface_new_adjustment)):
        background None
        
        action last_name_value.Toggle()

    vbox anchor (0.5, 0.0) pos (0.51, 0.32):
        spacing 117

        for item in ["flashing_lights", "image_filter", "tooltips_enabled", "cinematic_bars"]:
            hbox anchor (0.0, 0.5) pos (0.0, 0.5):
                spacing 50

                imagebutton:
                    idle At("images/interface/test/yes_off.webp", interface) hover At("images/interface/test/yes_on.webp", interface) selected_idle At("images/interface/test/yes_on.webp", interface)

                    selected eval(item)

                    if item == "image_filter":
                        action SetVariable(item, "comic")
                    else:
                        action SetVariable(item, True)

                    focus_mask None

                imagebutton:
                    idle At("images/interface/test/no_off.webp", interface) hover At("images/interface/test/no_on.webp", interface) selected_idle At("images/interface/test/no_on.webp", interface)

                    selected not eval(item)

                    if item == "image_filter":
                        action SetVariable(item, None)
                    else:
                        action SetVariable(item, True)

                    focus_mask None

    imagebutton:
        idle At("images/interface/test/finish_idle.webp", interface) hover At("images/interface/test/finish.webp", interface)

        action Return()

    use quick_menu