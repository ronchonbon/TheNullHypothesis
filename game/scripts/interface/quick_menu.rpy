style quick_button:
    background None

    # hover_sound "sounds/interface/hover.ogg"
    activate_sound "sounds/interface/press.ogg"

style quick_button_text:
    font "agency_fb.ttf"

    size 32

    idle_color "#9c9b9b"
    hover_color "#ffffff"
    insensitive_color "#666666"

screen quick_menu():
    style_prefix "quick"

    hbox:
        if renpy.get_screen("Wardrobe_screen"):
            align (0.0, 1.0)
        elif Action_screen_showing:
            align (0.0, 1.0)
        else:
            align (1.0, 1.0)

        if config.rollback_enabled:
            textbutton _("Back"): 
                action [
                    SetVariable("speed", 0.001),
                    SetVariable("intensity", 0.001),
                    Rollback()]

        textbutton _("Pref"):
            action ShowMenu("preferences")

        textbutton _("Q.Save"):
            action QuickSave()

        textbutton _("Q.Load"):
            action QuickLoad()

