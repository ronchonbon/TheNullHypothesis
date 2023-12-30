image menu_background:
    # "images/interface/main_menu/Ororo.webp" with Dissolve(0.5, alpha = True)
    # pause 5.0
    "images/interface/main_menu/Rogue.webp" with Dissolve(0.5, alpha = True)
    pause 5.0
    # "images/interface/main_menu/Laura.webp" with Dissolve(0.5, alpha = True)
    # pause 5.0
    "images/interface/main_menu/Charles.webp" with Dissolve(0.5, alpha = True)
    pause 5.0
    "images/interface/main_menu/Jean.webp" with Dissolve(0.5, alpha = True)
    pause 5.0
    # "images/interface/main_menu/Kurt.webp" with Dissolve(0.5, alpha = True)
    # pause 5.0
    # repeat

image menu_comic:
    "images/interface/main_menu/comic.webp"

    subpixel True
    transform_anchor True

    anchor (2257, 1045)
    offset (2172, 398)

    zoom interface_adjustment

style main_menu is default

screen main_menu():
    tag menu

    style_prefix "main_menu"

    add "menu_background" zoom interface_adjustment

    add "images/interface/main_menu/small_elements.webp" zoom interface_adjustment

    add "images/interface/main_menu/big_elements.webp" zoom interface_adjustment

    add "images/interface/main_menu/game_version.webp" zoom interface_adjustment

    add "menu_comic"

    text "GAME VERSION" anchor (0.0, 0.5) pos (0.025, 0.96):
        size 25

    text f"{config.version}" anchor (1.0, 0.5) pos (0.157, 0.96):
        size 25

    imagebutton:
        idle At("images/interface/main_menu/patreon_idle.webp", interface) hover At("images/interface/main_menu/patreon.webp", interface)

        action OpenURL("https://patreon.com/ronchon")

    imagebutton:
        idle At("images/interface/main_menu/soundcloud_idle.webp", interface) hover At("images/interface/main_menu/soundcloud.webp", interface)

        action OpenURL("https://soundcloud.com/grey_scale")

    imagebutton:
        idle At("images/interface/main_menu/discord_idle.webp", interface) hover At("images/interface/main_menu/discord.webp", interface)

        action OpenURL("https://discord.gg/kFjf49QVns")

    imagebutton:
        idle At("images/interface/main_menu/quit_idle.webp", interface) hover At("images/interface/main_menu/quit.webp", interface)

        action Quit(confirm = True)

    imagebutton:
        idle At("images/interface/main_menu/new_game_idle.webp", interface) hover At("images/interface/main_menu/new_game.webp", interface)

        action Start()

    text "NEW GAME" anchor (0.5, 0.5) pos (0.272, 0.507):
        size 45

    $ last_save = renpy.newest_slot()

    if last_save is not None:
        $ page, name = last_save.split("-")

    imagebutton:
        idle At("images/interface/main_menu/continue_idle.webp", interface) hover At("images/interface/main_menu/continue.webp", interface)

        if last_save is not None:
            action FileLoad(name, page = page)
        else:
            action NullAction()

    text "CONTINUE" anchor (0.5, 0.5) pos (0.272, 0.613):
        size 45

    imagebutton:
        idle At("images/interface/main_menu/options_idle.webp", interface) hover At("images/interface/main_menu/options.webp", interface)

        action ShowMenu("preferences")

    text "OPTIONS" anchor (0.5, 0.5) pos (0.272, 0.718):
        size 45