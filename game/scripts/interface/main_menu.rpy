image menu_foreground:
    "images/interface/main_menu/Ororo.webp" with Dissolve(0.5, alpha = True)
    pause 5.0
    "images/interface/main_menu/Rogue.webp" with Dissolve(0.5, alpha = True)
    pause 5.0
    "images/interface/main_menu/Laura.webp" with Dissolve(0.5, alpha = True)
    pause 5.0
    "images/interface/main_menu/Charles.webp" with Dissolve(0.5, alpha = True)
    pause 5.0
    "images/interface/main_menu/Jean.webp" with Dissolve(0.5, alpha = True)
    pause 5.0
    "images/interface/main_menu/Kurt.webp" with Dissolve(0.5, alpha = True)
    pause 5.0
    repeat

style main_menu is default

style main_menu_button:
    # hover_sound "sounds/interface/hover.ogg"
    activate_sound "sounds/interface/press.ogg"

style main_menu_image_button:
    # hover_sound "sounds/interface/hover.ogg"
    activate_sound "sounds/interface/press.ogg"

screen main_menu():
    tag menu

    style_prefix "main_menu"

    add "images/interface/main_menu/background.webp" align (0.5, 0.5) zoom background_adjustment

    add "menu_foreground" align (0.5, 0.5) zoom background_adjustment

    add "images/interface/main_menu/logo.webp" align (0.5, 0.5) zoom background_adjustment

    text "GAME VERSION: [config.version]" anchor (0.0, 1.0) pos (0.01, 0.99) size 30

    $ last_save = renpy.newest_slot()

    if last_save is not None:
        $ page, name = last_save.split("-")

    vbox anchor (0.0, 0.5) pos (0.0, 0.5):
        spacing 10

        imagebutton anchor (0.0, 0.0) pos (0.0, 0.0):
            idle "images/interface/main_menu/soundcloud_idle.webp" hover "images/interface/main_menu/soundcloud.webp"

            action OpenURL("https://soundcloud.com/grey_scale")

        imagebutton anchor (0.0, 0.0) pos (0.0, 0.0):
            idle "images/interface/main_menu/discord_idle.webp" hover "images/interface/main_menu/discord.webp"

            action OpenURL("https://discord.gg/kFjf49QVns")

        imagebutton anchor (0.0, 0.0) pos (0.0, 0.0):
            idle "images/interface/main_menu/patreon_idle.webp" hover "images/interface/main_menu/patreon.webp"

            action OpenURL("https://patreon.com/ronchon")

    button anchor (0.5, 0.5) pos (0.275, 0.48) xysize (428, 85):
        idle_background "images/interface/main_menu/button_idle.webp" hover_background "images/interface/main_menu/button.webp"

        text "New Game" align (0.5, 0.5):
            size 46

            color "#512908"

        action Start()

    button anchor (0.5, 0.5) pos (0.275, 0.595) xysize (428, 85):
        idle_background "images/interface/main_menu/button_idle.webp" hover_background "images/interface/main_menu/button.webp"

        text "Continue" align (0.5, 0.5):
            size 46

            color "#512908"

        if last_save is not None:
            action FileLoad(name, page = page)
        else:
            action NullAction()

    button anchor (0.5, 0.5) pos (0.275, 0.71) xysize (428, 85):
        idle_background "images/interface/main_menu/button_idle.webp" hover_background "images/interface/main_menu/button.webp"

        text "Options" align (0.5, 0.5):
            size 46

            color "#512908"

        action ShowMenu("preferences")

    imagebutton anchor (0.5, 1.0) pos (0.9, 1.0):
        idle "images/interface/main_menu/exit_idle.webp" hover "images/interface/main_menu/exit.webp"

        action Quit(confirm = False)