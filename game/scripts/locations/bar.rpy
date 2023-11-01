label bar:
    $ lights_on = True
    $ door_locked = False

    if Player.destination != Player.location:
        call check_for_Events(traveling = True) from _call_check_for_Events_3

        if Player.destination != Player.location:
            call set_the_scene(location = Player.destination, greetings = True) from _call_set_the_scene_305

    call set_music from _call_set_music_1

    while Player.location == "bg_bar":
        if clock <= 0:
            if time_index > 2:
                "It's getting late, you head home."

                call travel(Player.home) from _call_travel_2
            else:
                call wait_around from _call_wait_around_3
                
        menu(menu_location = "bg_bar"):
            "Wait" if time_index < 3:
                call wait_around from _call_wait_around_4
            "Wait (locked)" if time_index > 2:
                pass
            
    call move_location(Player.location) from _call_move_location_1