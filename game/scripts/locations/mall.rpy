label mall:
    $ lights_on = True
    $ door_locked = False

    if Player.destination != Player.location:
        call check_for_Events(traveling = True) from _call_check_for_Events_12

        if Player.destination != Player.location:
            call set_the_scene(location = Player.destination, greetings = True) from _call_set_the_scene_322

    call set_music from _call_set_music_11

    while Player.location == "bg_mall":
        if clock <= 0:
            if time_index > 2:
                "The mall is now closing, please make your way to the nearest exit."

                call travel("bg_campus") from _call_travel_30
            else:
                call wait_around from _call_wait_around_23

        menu(menu_location = "bg_mall"):
            "'Mutant Couture'" if time_index < 3:
                show screen shop_screen("clothing")
            "'Mutant Couture' (locked)" if time_index > 2:
                pass
            "'Bear With Me'" if time_index < 3:
                show screen shop_screen("gift")
            "'Bear With Me' (locked)" if time_index > 2:
                pass
            "'X-Treme Intimates'" if time_index < 3:
                show screen shop_screen("lingerie")
            "'X-Treme Intimates' (locked)" if time_index > 2:
                pass
            "'The Moaning of Life'" if time_index < 3:
                show screen shop_screen("sex")
            "'The Moaning of Life' (locked)" if time_index > 2:
                pass
            "Wait" if time_index < 3:
                call wait_around from _call_wait_around_24
            "Wait (locked)" if time_index > 2:
                pass

    call move_location(Player.location) from _call_move_location_13