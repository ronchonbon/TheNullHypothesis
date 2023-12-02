label study:
    $ lights_on = True
    $ door_locked = False

    if Player.destination != Player.location:
        call check_for_Events(traveling = True) from _call_check_for_Events_14

        if Player.destination != Player.location:
            call set_the_scene(location = Player.destination, greetings = True) from _call_set_the_scene_324

    call set_music from _call_set_music_13

    while Player.location == "bg_study":
        if clock <= 0:
            if time_index > 2:
                "It's getting late, you head back to your room."

                call travel(Player.home) from _call_travel_32
            else:
                call wait_around from _call_wait_around_27
                
        menu(menu_location = "bg_study"):
            "Try to contact [Charles.name]" if Charles.gives_work and clock > 0 and time_index < 3 and Charles.location != Player.location and not Charles.History.check("Player_contacted_telepathically"):
                call work(Charles) from _call_work
            "Contact [Charles.name]" if Charles.gives_work and clock > 0 and time_index < 3 and Charles.location != Player.location and Charles.History.check("Player_contacted_telepathically"):
                call work(Charles) from _call_work_1
            "Classroom":
                call travel("bg_classroom") from _call_travel_33
            "Grounds":
                call travel("bg_campus") from _call_travel_34
            "Approach. . ." if Offscreen:
                call approach_Characters from _call_approach_Characters_7
            "Wait" if time_index < 3:
                call wait_around from _call_wait_around_28
            "Wait (locked)" if time_index > 2:
                pass
            
    call move_location(Player.location) from _call_move_location_20