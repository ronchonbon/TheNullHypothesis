init -2:

    default game_started = False

    default chapter = 0

    default day = 0
    default weekday = 1
    default time_index = 0
    default clock = 0
    default season = 1
    default season_day = 1

label splashscreen:
    $ renpy.start_predict("characters/Player/images/*.webp")

    $ check_predicted_images()

    show expression "images/interface/splashscreen_bw.webp" as splashscreen_bw:
        subpixel True
        transform_anchor True

        align (0.5, 0.5)

    $ renpy.pause(1.0, hard = True)

    show expression "images/interface/splashscreen.webp" as splashscreen:
        subpixel True
        transform_anchor True

        align (0.5, 0.5)
        alpha 0.0

        ease 2.0 alpha 1.0

    $ renpy.pause(3.0, hard = True)

    hide splashscreen
    hide splashscreen_bw

    $ renpy.pause(1.0, hard = True)
    
    show screen credits()
    pause
    hide screen credits

    call screen disclaimer()

    return

label start:
    $ save_name = "Prologue"

    $ _skipping = False

    show expression "images/interface/main_menu/blank_background.webp" as new_game_background:
        subpixel True
        transform_anchor True

        align (0.5, 0.5)

        zoom interface_new_adjustment

    show expression "images/interface/preferences/spin.webp" as new_game_foreground:
        subpixel True
        transform_anchor True

        anchor (0.5, 0.5) 
        pos (0.502, 0.502)

        zoom interface_new_adjustment

    show expression "images/interface/main_menu/comic.webp" as new_game_comic:
        subpixel True
        transform_anchor True

        anchor (2257, 1045)
        offset (2172, 398)

        zoom interface_new_adjustment

    $ renpy.pause(0.2, hard = True)

    play music "sounds/music/Almost an Ending.ogg" fadeout 1.0 if_changed

    $ Clothes = default_Player_Clothes()

    while Clothes:
        $ Player.Outfits.append(Clothes[0])

        $ Clothes.remove(Clothes[0])

    $ Player.Outfit = Player.Outfits[Player.Outfit_index]

    show expression "images/interface/main_menu/comic.webp" as new_game_comic:
        subpixel True
        transform_anchor True

        anchor (2257, 1045)
        offset (2172, 398)

        zoom interface_new_adjustment

        parallel:
            ease 2.0 rotate -21
        parallel:
            ease 2.0 zoom 1.95
        parallel:
            ease 2.0 pos (0.895, 0.104)

    $ renpy.pause(2.0, hard = True)
    
    call get_ready from _call_get_ready

    $ game_started = True

    jump prologue

return

label after_load:
    call get_ready from _call_get_ready_1

    return

label get_ready:
    $ renpy.start_predict("characters/Player/images/*.webp")

    $ renpy.dynamic(temp_Characters = all_Characters[:])

    while temp_Characters:
        call expression f"update_{temp_Characters[0].tag}" from _call_expression_102

        $ temp_Characters.remove(temp_Characters[0])

    $ check_predicted_images(loading = True)
    
    call refresh_season_content from _call_refresh_season_content
    
    return