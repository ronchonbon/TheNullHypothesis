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
            "Swim" if clock > 0 and not weather:
                call swim from _call_swim
            "Swim (locked)" if clock <= 0 or weather:
                pass
            "Sunbathe" if clock > 0 and time_index < 3 and not weather:
                call sunbathe from _call_sunbathe
            "Sunbathe (locked)" if clock <= 0 or time_index > 2 or weather:
                pass
            "Approach. . ." if Offscreen:
                call approach_Characters
            "Wait" if time_index < 3:
                call wait_around from _call_wait_around_26
            "Wait (locked)" if time_index > 2:
                pass
            
    call move_location(Player.location) from _call_move_location_14