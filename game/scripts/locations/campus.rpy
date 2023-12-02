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
                call approach_Characters
            "Wait" if time_index < 3:
                call wait_around from _call_wait_around_16
            "Wait (locked)" if time_index > 2:
                pass
            
    call move_location(Player.location) from _call_move_location_9