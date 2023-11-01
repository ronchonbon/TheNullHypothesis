label danger_room:
    if time_index < 3:
        $ lights_on = True
    else:
        $ lights_on = False

    $ door_locked = False

    if Player.destination != Player.location:
        call check_for_Events(traveling = True) from _call_check_for_Events_10

        if Player.destination != Player.location:
            call set_the_scene(location = Player.destination, greetings = True) from _call_set_the_scene_320

    call set_music from _call_set_music_9

    while Player.location == "bg_danger":
        if time_index > 2:
            $ lights_on = False

        if clock <= 0:
            if time_index > 2:
                "It's getting late, you head back to your room."

                call travel(Player.home) from _call_travel_26
            else:
                call wait_around from _call_wait_around_19
                
        menu(menu_location = "bg_danger"):
            "Train" if clock > 0 and time_index < 3:
                call train from _call_train
            "Train (locked)" if clock <= 0 or time_index > 2:
                pass
            "Locker room":
                call travel("bg_lockers") from _call_travel_27
            "Wait" if time_index < 3:
                call wait_around from _call_wait_around_20
            "Wait (locked)" if time_index > 2:
                pass
            
    call move_location(Player.location) from _call_move_location_11