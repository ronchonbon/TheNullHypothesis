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
    $ renpy.start_predict("images/backgrounds/base/*.webp")
    $ renpy.start_predict("images/interface/*.webp")
    $ renpy.start_predict("images/interface/*/*.webp")
    $ renpy.start_predict("images/interface/*/*/*.webp")
    $ renpy.start_predict("images/effects/*.webp")
    $ renpy.start_predict("characters/Player/images/*.webp")

    python:
        for C in all_Characters:
            if f"bg_{C.tag}" in bedrooms:
                renpy.start_predict(f"characters/{C.tag}/images/bedroom/*.webp")

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
    call screen seizure_warning()

    return

label start:
    $ _skipping = False

    show expression "images/interface/main_menu/background.webp" as new_game_background:
        subpixel True
        transform_anchor True

        align (0.5, 0.5)

    show expression "images/interface/main_menu/comic.webp" as new_game_comic:
        subpixel True
        transform_anchor True

        anchor (2257, 1045)
        offset (1556, 399)
        zoom 0.5

    play music "sounds/music/Almost an Ending.ogg" fadeout 1.0 if_changed

    $ first_name = renpy.input("What is your first name?", default = "John", length = 10)
    $ first_name = first_name.strip()

    if not first_name:
        $ first_name = "John"

    $ last_name = renpy.input("What is your last name?", default = "Doe", length = 15)
    $ last_name = last_name.strip()

    if not last_name:
        $ last_name = "Doe"

    $ Player.first_name = first_name
    $ Player.last_name = last_name
    $ Player.full_name = f"{first_name} {last_name}"

    $ save_name = Player.full_name + "\nPrologue"

    $ Jean.Player_petname = Player.first_name
    $ Laura.Player_petname = Player.first_name
    $ Ororo.Player_petname = Player.first_name

    $ Clothes = default_Player_Clothes()

    while Clothes:
        $ Player.Outfits.append(Clothes[0])

        $ Clothes.remove(Clothes[0])

    $ Player.Outfit = Player.Outfits[Player.Outfit_index]

    show expression "images/interface/main_menu/comic.webp" as new_game_comic:
        subpixel True
        transform_anchor True

        anchor (2257, 1045)
        offset (1556, 399)
        zoom 0.5

        parallel:
            ease 2.0 rotate -21
        parallel:
            ease 2.0 zoom 1.95
        parallel:
            ease 2.0 pos (0.3875, 0.665)

    $ renpy.pause(2.0, hard = True)
    
    call get_ready from _call_get_ready

    $ game_started = True

    jump prologue

return

label after_load:
    call get_ready from _call_get_ready_1

    return

label get_ready:
    $ renpy.start_predict("images/backgrounds/base/*.webp")
    $ renpy.start_predict("images/interface/*.webp")
    $ renpy.start_predict("images/interface/*/*.webp")
    $ renpy.start_predict("images/interface/*/*/*.webp")
    $ renpy.start_predict("images/effects/*.webp")
    $ renpy.start_predict("characters/Player/images/*.webp")

    python:
        for C in all_Characters:
            if f"bg_{C.tag}" in bedrooms:
                renpy.start_predict(f"characters/{C.tag}/images/bedroom/*.webp")

    $ temp_all_Characters = all_Characters[:]

    while temp_all_Characters:
        call expression f"update_{temp_all_Characters[0].tag}" from _call_expression_102

        $ temp_all_Characters.remove(temp_all_Characters[0])

    $ check_predicted_images()
    
    call refresh_season_content from _call_refresh_season_content
    
    return