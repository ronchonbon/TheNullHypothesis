layeredimage bg_campus_background:
    always:
        "sky"

    if time_index == 2:
        "images/backgrounds/base/bg_campus_mansion_evening.webp"
    else:
        "images/backgrounds/base/bg_campus_mansion.webp"

    if campus_grass_cut:
        "images/backgrounds/base/bg_campus_grass.webp"
    else:
        "images/backgrounds/base/bg_campus_grass_uncut.webp"

    if not weather and time_index < 3:
        "images/backgrounds/base/bg_campus_lighting.webp"

    if not weather and time_index < 3:
        "images/backgrounds/base/bg_campus_lighting_linear_dodge.webp" at Transform(blend = "add")

    if weather == "snow" or snow_left:
        "images/backgrounds/base/bg_campus_snow.webp"

    if weather == "rain":
        "images/backgrounds/base/bg_campus_puddles_linear_dodge.webp" at Transform(blend = "add")
    elif weather == "snow":
        "images/backgrounds/base/bg_campus_steam_linear_dodge.webp" at Transform(blend = "add")

    if weather == "rain":
        "images/backgrounds/base/bg_campus_puddles.webp"
    elif weather == "snow":
        "images/backgrounds/base/bg_campus_steam.webp"

    if time_index in [0]:
        "images/backgrounds/base/bg_campus_mist.webp"

    if time_index >= 3:
        "images/backgrounds/base/bg_campus_night_hard_light.webp" at Transform(blend = "multiply")
    elif time_index == 2:
        "images/backgrounds/base/bg_campus_evening_hard_light.webp" at Transform(blend = "multiply")

    if time_index >= 3:
        "images/backgrounds/base/bg_campus_night_color_dodge.webp" at Transform(blend = "multiply")
    elif time_index == 2:
        "images/backgrounds/base/bg_campus_evening_color_dodge.webp" at Transform(blend = "add")

    if time_index >= 3:
        "images/backgrounds/base/bg_campus_night_linear_dodge.webp" at Transform(blend = "add")
    elif time_index == 2:
        "images/backgrounds/base/bg_campus_evening_linear_dodge.webp" at Transform(blend = "add")
    elif time_index == 0:
        "images/backgrounds/base/bg_campus_morning_linear_dodge.webp" at Transform(blend = "add")

    if weather == "rain":
        "images/backgrounds/base/bg_campus_rain_splashes.webp" at rain_splashes

layeredimage bg_campus_cover:
    if time_index >= 3:
        "images/backgrounds/base/bg_campus_left_tree_night.webp"
    elif time_index == 2:
        "images/backgrounds/base/bg_campus_left_tree_evening.webp"
    else:
        "images/backgrounds/base/bg_campus_left_tree.webp"

    if time_index >= 3:
        "images/backgrounds/base/bg_campus_right_tree_night.webp"
    elif time_index == 2:
        "images/backgrounds/base/bg_campus_right_tree_evening.webp"
    else:
        "images/backgrounds/base/bg_campus_right_tree.webp"

    if weather != "snow":
        Null()
    elif time_index >= 3:
        "images/backgrounds/base/bg_campus_snowstorm_night.webp"
    elif time_index == 2:
        "images/backgrounds/base/bg_campus_snowstorm_evening.webp"
    else:
        "images/backgrounds/base/bg_campus_snowstorm.webp"

    if weather == "snow" and time_index in [0, 1]:
        "images/backgrounds/base/bg_campus_snowstorm_linear_dodge.webp" at Transform(blend = "add")

    if weather != "rain":
        Null()
    elif time_index == 2:
        "images/backgrounds/base/bg_campus_rain_evening.webp" at Transform(alpha = 0.8)
    else:
        "images/backgrounds/base/bg_campus_rain.webp" at Transform(alpha = 0.8)

label campus:
    $ lights_on = True
    $ door_locked = False

    if Player.destination != Player.location:
        call check_for_Events(traveling = True) from _call_check_for_Events_8

        if Player.destination != Player.location:
            call set_the_scene(location = Player.destination, greetings = True) from _call_set_the_scene_317

    call set_music from _call_set_music_7

    while Player.location == "bg_campus":
        if clock <= 0:
            if time_index > 2:
                "You're getting tired, you head back to your room."

                call travel(Player.home) from _call_travel_20
            else:
                call wait_around from _call_wait_around_15

        menu(menu_location = "bg_campus"):
            "Classroom":
                call travel("bg_classroom") from _call_travel_21
            "Xavier's study":
                call travel("bg_study") from _call_travel_22
            "Approach. . ." if Offscreen:
                call approach_Characters from _call_approach_Characters_1
            "Wait" if time_index < 3:
                call wait_around from _call_wait_around_16
            "Wait (locked)" if time_index > 2:
                pass
            
    call move_location(Player.location) from _call_move_location_9