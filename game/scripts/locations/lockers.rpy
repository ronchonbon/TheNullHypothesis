label lockers:
    $ lights_on = True
    $ door_locked = False

    if not Player.History.check("showered", tracker = "recent"):
        $ shower_steam = False

    if Player.destination != Player.location:
        call check_for_Events(traveling = True) from _call_check_for_Events_11

        if Player.destination != Player.location:
            call set_the_scene(location = Player.destination, greetings = True) from _call_set_the_scene_321

    call set_music from _call_set_music_10

    while Player.location == "bg_lockers":
        if clock <= 0:
            if time_index == 3:
                "You're getting tired, you head back to your room."

                call travel(Player.home) from _call_travel_28
            else:
                call wait_around from _call_wait_around_21
                
        menu(menu_location = "bg_lockers"):
            "Shower" if clock > 0:
                call take_a_shower from _call_take_a_shower_1
            "Shower (locked)" if clock <= 0:
                pass
            "Danger Room":
                call travel("bg_danger") from _call_travel_29
            "Wait" if time_index < 3:
                call wait_around from _call_wait_around_22
            "Wait (locked)" if time_index > 2:
                pass
            
    call move_location(Player.location) from _call_move_location_12