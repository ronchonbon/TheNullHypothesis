image menu_background:
    # "images/interface/main_menu/Ororo.webp" with Dissolve(0.5, alpha = True)
    # pause 5.0
    # "images/interface/main_menu/Rogue.webp" with Dissolve(0.5, alpha = True)
    # pause 5.0
    # "images/interface/main_menu/Laura.webp" with Dissolve(0.5, alpha = True)
    # pause 5.0
    "images/interface/main_menu/Charles.webp" with Dissolve(0.5, alpha = True)
    # pause 5.0
    # "images/interface/main_menu/Jean.webp" with Dissolve(0.5, alpha = True)
    # pause 5.0
    # "images/interface/main_menu/Kurt.webp" with Dissolve(0.5, alpha = True)
    # pause 5.0
    # repeat

image menu_comic:
    "images/interface/main_menu/comic.webp"

    subpixel True
    transform_anchor True

    anchor (2257, 1045)
    offset (2172, 398)

    zoom interface_new_adjustment

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

    add "menu_background" zoom interface_new_adjustment

    add "images/interface/main_menu/small_elements.webp" zoom interface_new_adjustment

    add "images/interface/main_menu/big_elements.webp" zoom interface_new_adjustment

    add "images/interface/main_menu/game_version.webp" zoom interface_new_adjustment

    add "menu_comic"

    text f"{config.version}" anchor (1.0, 0.5) pos (0.155, 0.96):
        font "agency_fb_bold.ttf"

        size 25

        color "#ffffff"

    imagebutton:
        idle At("images/interface/main_menu/patreon_idle.webp", interface) hover At("images/interface/main_menu/patreon.webp", interface)

        action OpenURL("https://patreon.com/ronchon")

        focus_mask True

    imagebutton:
        idle At("images/interface/main_menu/soundcloud_idle.webp", interface) hover At("images/interface/main_menu/soundcloud.webp", interface)

        action OpenURL("https://soundcloud.com/grey_scale")

        focus_mask True

    imagebutton:
        idle At("images/interface/main_menu/discord_idle.webp", interface) hover At("images/interface/main_menu/discord.webp", interface)

        action OpenURL("https://discord.gg/kFjf49QVns")

        focus_mask True

    imagebutton:
        idle At("images/interface/main_menu/quit_idle.webp", interface) hover At("images/interface/main_menu/quit.webp", interface)

        action Quit(confirm = False)

        focus_mask True

    imagebutton:
        idle At("images/interface/main_menu/new_game_idle.webp", interface) hover At("images/interface/main_menu/new_game.webp", interface)

        action Start()

        focus_mask True

    $ last_save = renpy.newest_slot()

    if last_save is not None:
        $ page, name = last_save.split("-")

    imagebutton:
        idle At("images/interface/main_menu/continue_idle.webp", interface) hover At("images/interface/main_menu/continue.webp", interface)

        if last_save is not None:
            action FileLoad(name, page = page)
        else:
            action NullAction()

        focus_mask True

    imagebutton:
        idle At("images/interface/main_menu/options_idle.webp", interface) hover At("images/interface/main_menu/options.webp", interface)

        action ShowMenu("preferences")

        focus_mask True