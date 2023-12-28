layeredimage bg_pool_background:
    always:
        "sky"

    if time_index >= 3:
        "images/backgrounds/base/bg_pool_mountains_night.webp"
    elif weather in ["rain", "snow"]:
        "images/backgrounds/base/bg_pool_mountains_rain.webp"
    elif time_index == 2:
        "images/backgrounds/base/bg_pool_mountains_evening.webp"
    else:
        "images/backgrounds/base/bg_pool_mountains.webp"

    if weather == "rain":
        "images/backgrounds/base/bg_pool_water_rain.webp"
    else:
        "images/backgrounds/base/bg_pool_water.webp"

    if time_index >= 3:
        "images/backgrounds/base/bg_pool_mansion_night.webp"
    else:
        "images/backgrounds/base/bg_pool_mansion.webp"

    if weather == "snow" or snow_left:
        "images/backgrounds/base/bg_pool_protector.webp"
    
    always:
        "images/backgrounds/base/bg_pool_chairs_shadows.webp" at Transform(blend = "multiply")

    always:
        "images/backgrounds/base/bg_pool_chairs.webp"

    always:
        "images/backgrounds/base/bg_pool_diving_board_shadows.webp" at Transform(blend = "multiply")

    always:
        "images/backgrounds/base/bg_pool_diving_board.webp"

    always:
        "images/backgrounds/base/bg_pool_shadow_multiply.webp" at Transform(blend = "multiply")

    always:
        "images/backgrounds/base/bg_pool_lights_linear_dodge.webp" at Transform(blend = "add")

    if not weather and time_index in [1]:
        "images/backgrounds/base/bg_pool_sun_linear_dodge.webp" at Transform(blend = "add")

    if weather == "snow" or snow_left:
        "images/backgrounds/base/bg_pool_snow.webp"

    if weather == "snow" or snow_left:
        "images/backgrounds/base/bg_pool_snow_linear_dodge.webp" at Transform(blend = "add")

    if not weather and time_index in [0]:
        "images/backgrounds/base/bg_pool_mist.webp"

    if time_index >= 3:
        "images/backgrounds/base/bg_pool_night_multiply.webp" at Transform(blend = "multiply")
    elif time_index == 2:
        "images/backgrounds/base/bg_pool_evening_multiply.webp" at Transform(blend = "multiply")

    if time_index == 2:
        "images/backgrounds/base/bg_pool_evening_linear_dodge.webp" at Transform(blend = "add")

layeredimage bg_pool_cover:
    if weather != "snow":
        Null()
    elif time_index >= 3:
        "images/backgrounds/base/bg_pool_snowstorm_night.webp" at Transform(alpha = 0.8)
    elif time_index == 2:
        "images/backgrounds/base/bg_pool_snowstorm_evening.webp" at Transform(alpha = 0.8)
    else:
        "images/backgrounds/base/bg_pool_snowstorm.webp" at Transform(alpha = 0.8)

    if weather != "snow":
        Null()
    elif time_index >= 3:
        "images/backgrounds/base/bg_pool_snowstorm_night_linear_dodge.webp" at Transform(blend = "add", alpha = 0.2)
    elif time_index == 2:
        "images/backgrounds/base/bg_pool_snowstorm_evening_linear_dodge.webp" at Transform(blend = "add", alpha = 0.5)
    else:
        "images/backgrounds/base/bg_pool_snowstorm_linear_dodge.webp" at Transform(blend = "add", alpha = 0.5)

    if weather != "rain":
        Null()
    elif time_index >= 3:
        "images/backgrounds/base/bg_pool_rain_night.webp" at Transform(alpha = 0.8)
    elif time_index == 2:
        "images/backgrounds/base/bg_pool_rain_evening.webp" at Transform(alpha = 0.8)
    else:
        "images/backgrounds/base/bg_pool_rain.webp" at Transform(alpha = 0.8)

    if weather != "rain":
        Null()
    elif time_index >= 3:
        "images/backgrounds/base/bg_pool_rain_night_linear_dodge.webp" at Transform(blend = "add", alpha = 0.8)
    elif time_index == 2:
        "images/backgrounds/base/bg_pool_rain_evening_linear_dodge.webp" at Transform(blend = "add", alpha = 0.8)
    else:
        "images/backgrounds/base/bg_pool_rain_linear_dodge.webp" at Transform(blend = "add", alpha = 0.8)

label pool:
    $ lights_on = True
    $ door_locked = False

    if Player.destination != Player.location:
        call check_for_Events(traveling = True) from _call_check_for_Events_13

        if Player.destination != Player.location:
            call set_the_scene(location = Player.destination, greetings = True) from _call_set_the_scene_323

    call set_music from _call_set_music_12

    while Player.location == "bg_pool":
        if clock <= 0:
            if time_index > 2:
                "You're getting tired, you head back to your room."

                call travel(Player.home) from _call_travel_31
            else:
                call wait_around from _call_wait_around_25
                
        menu(menu_location = "bg_pool"):
            "Swim" if clock > 0 and not weather and not snow_left:
                call swim from _call_swim
            "Swim (locked)" if clock <= 0 or weather or snow_left:
                pass
            "Sunbathe" if clock > 0 and time_index < 3 and not weather:
                call sunbathe from _call_sunbathe
            "Sunbathe (locked)" if clock <= 0 or time_index > 2 or weather:
                pass
            "Approach. . ." if Offscreen:
                call approach_Characters from _call_approach_Characters_6
            "Wait" if time_index < 3:
                call wait_around from _call_wait_around_26
            "Wait (locked)" if time_index > 2:
                pass
            
    call move_location(Player.location) from _call_move_location_14