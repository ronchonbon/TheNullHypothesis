default current_bedroom = None

label girls_hallway:
    $ lights_on = True
    $ door_locked = False

    if Player.destination != Player.location:
        call check_for_Events(traveling = True) from _call_check_for_Events_4

        if Player.destination != Player.location:
            call set_the_scene(location = Player.destination, greetings = True) from _call_set_the_scene_306

    call set_music from _call_set_music_2

    while Player.location == "bg_girls_hallway":
        if clock <= 0:
            if time_index > 2:
                "You're getting tired, you head back to your room."

                call travel(Player.home) from _call_travel_3
            else:
                call wait_around from _call_wait_around_5
                
        menu(menu_location = "bg_girls_hallway"):
            "Enter [Rogue.name]'s room" if Rogue in active_Companions and Rogue in Present:
                call travel(Rogue) from _call_travel_4
            "Knock on [Rogue.name]'s room" if Rogue in active_Companions and Rogue not in Present:
                call travel(Rogue) from _call_travel_5
            "Enter [Laura.name]'s room" if Laura in active_Companions and Laura in Present:
                call travel(Laura) from _call_travel_6
            "Knock on [Laura.name]'s room" if Laura in active_Companions and Laura not in Present:
                call travel(Laura) from _call_travel_35
            "Enter [Jean.name]'s room" if Jean in active_Companions and Jean in Present:
                call travel(Jean) from _call_travel_36
            "Knock on [Jean.name]'s room" if Jean in active_Companions and Jean not in Present:
                call travel(Jean) from _call_travel_37
            "Your hallway":
                call travel("bg_hallway") from _call_travel_7
            "Wait" if time_index < 3:
                call wait_around from _call_wait_around_6
            "Wait (locked)" if time_index > 2:
                pass
        
    call move_location(Player.location) from _call_move_location_2

label hallway:
    $ lights_on = True
    $ door_locked = False

    if Player.destination != Player.location:
        call check_for_Events(traveling = True) from _call_check_for_Events_5

        if Player.destination != Player.location:
            call set_the_scene(location = Player.destination, greetings = True) from _call_set_the_scene_307

    call set_music from _call_set_music_3

    while Player.location == "bg_hallway":
        if clock <= 0:
            if time_index > 2:
                "You're getting tired, you head back to your room."

                call travel(Player.home) from _call_travel_8
            else:
                call wait_around from _call_wait_around_7
                
        menu(menu_location = "bg_hallway"):
            "Enter your room":
                call travel(Player.home) from _call_travel_9
            "Girls' hallway":
                call travel("bg_girls_hallway") from _call_travel_10
            "Wait" if time_index < 3:
                call wait_around from _call_wait_around_8
            "Wait (locked)" if time_index > 2:
                pass
                
    call move_location(Player.location) from _call_move_location_3

label Player_room:
    $ lights_on = True
    $ door_locked = False

    $ current_bedroom = Player

    if Player.destination != Player.location:
        call check_for_Events(traveling = True) from _call_check_for_Events_6

        if Player.destination != Player.location:
            if Player.location == "bg_shower_Player":
                call set_the_scene(location = Player.home, greetings = False) from _call_set_the_scene_308
            else:
                call set_the_scene(location = Player.home, greetings = True) from _call_set_the_scene_309

    call set_music from _call_set_music_4

    while Player.location == Player.home:
        if clock <= 0:
            if time_index < 3:
                call wait_around from _call_wait_around_9
            else:
                call get_ready_for_bed from _call_get_ready_for_bed_2
            
        menu(menu_location = Player.home):
            "Study" if clock > 0:
                call study_session from _call_study_session
            "Study (locked)" if clock <= 0:
                pass
            "Lock the door" if not door_locked:
                $ door_locked = True
            "Unlock the door" if door_locked:
                $ door_locked = False
            "Turn on lights" if time_index > 2 and not lights_on:
                $ lights_on = True

                $ lighting = "night"

                call set_the_scene(fade = False, fade_Characters = False) from _call_set_the_scene_310
            "Turn off lights" if time_index > 2 and lights_on:
                $ lights_on = False

                $ lighting = "moonlight"

                call set_the_scene(fade = False, fade_Characters = False) from _call_set_the_scene_311
            "Bathroom":
                call travel("bg_shower_Player") from _call_travel_11
            "Hallway":
                call travel("bg_hallway") from _call_travel_12
            "Wait" if time_index < 3:
                call wait_around from _call_wait_around_10
            "Sleep" if time_index > 2:
                call get_ready_for_bed from _call_get_ready_for_bed_3
            "Sleep and progress story" if season_completed:
                call progress_story from _call_progress_story
                
    call move_location(Player.location) from _call_move_location_4

label Character_room:
    $ lights_on = True
    $ door_locked = False

    if Player.destination != Player.location:
        $ selected_Event = EventScheduler.choose_Event(traveling = True)

        if selected_Event:
            call start_Event(selected_Event) from _call_start_Event_15

    if Player.destination != Player.location:
        if current_bedroom not in Present:
            if Player.destination != Player.location:
                if "bg_shower" not in Player.location:
                    if current_bedroom.wants_alone_time:
                        "She wants some alone time. Let's just come back later."

                        call travel("bg_girls_hallway") from _call_travel_13
                    else:
                        call Player_knocks(current_bedroom) from _call_Player_knocks
        elif current_bedroom.History.check("not_invited_in", tracker = "recent"):
            "Sounds like she wants you to stay outside."

            call travel("bg_girls_hallway") from _call_travel_38
        elif not approval_check(current_bedroom, threshold = "friendship"):
            call expression f"{current_bedroom.tag}_not_invited_in" from _call_expression_128

            $ current_bedroom.History.update("not_invited_in")

            call travel("bg_girls_hallway") from _call_travel_39

    if Player.destination != Player.location:
        if "bg_shower" in Player.location:
            call set_the_scene(location = current_bedroom.home, greetings = False) from _call_set_the_scene_312
        else:
            call set_the_scene(location = current_bedroom.home, greetings = True) from _call_set_the_scene_313

    call set_music from _call_set_music_5

    while Player.location == current_bedroom.home:
        if clock <= 0:
            if time_index < 3:
                call wait_around from _call_wait_around_11
            else:
                call get_ready_for_bed from _call_get_ready_for_bed_4
            
        menu(menu_location = current_bedroom.home):
            "Study" if clock > 0:
                call study_session from _call_study_session_1
            "Study (locked)" if clock <= 0:
                pass
            "Lock the door" if not door_locked:
                $ door_locked = True
            "Unlock the door" if door_locked:
                $ door_locked = False
            "Turn on lights" if time_index > 2 and not lights_on:
                $ lights_on = True

                $ lighting = "night"

                call set_the_scene(fade = False, fade_Characters = False) from _call_set_the_scene_314
            "Turn off lights" if time_index > 2 and lights_on:
                $ lights_on = False

                if Player.location == Rogue.home and "candle" in Rogue.inventory.keys() and "mirror" in Rogue.inventory.keys() and "camera" in Rogue.inventory.keys():
                    $ lighting = "candlelit"
                else:
                    $ lighting = "moonlight"

                call set_the_scene(fade = False, fade_Characters = False) from _call_set_the_scene_315
            "Bathroom" if approval_check(current_bedroom, threshold = "dating"):
                call travel(f"bg_shower_{current_bedroom.tag}") from _call_travel_14
            "Bathroom (locked)" if not approval_check(current_bedroom, threshold = "dating"):
                pass
            "Girls' hallway":
                call travel("bg_girls_hallway") from _call_travel_15
            "Wait" if time_index < 3:
                call wait_around from _call_wait_around_12
            "Sleep" if time_index > 2:
                call get_ready_for_bed from _call_get_ready_for_bed_5
                
    call move_location(Player.location) from _call_move_location_5

label shower:
    # $ lights_on = True
    $ door_locked = False
    $ shower_open = True

    if not Player.History.check("showered", tracker = "recent"):
        $ shower_steam = False

    if Player.destination != Player.location:
        call check_for_Events(traveling = True) from _call_check_for_Events_7

        if Player.destination != Player.location:
            call set_the_scene(location = Player.destination, greetings = True) from _call_set_the_scene_316

    call set_music from _call_set_music_6

    while Player.location == f"bg_shower_{current_bedroom.tag}":
        if clock <= 0:
            if time_index > 2:
                if current_bedroom == Player:
                    call travel(current_bedroom.home) from _call_travel_16
                else:
                    call travel(current_bedroom) from _call_travel_17
            else:
                call wait_around from _call_wait_around_13
            
        menu(menu_location = f"bg_shower_{current_bedroom.tag}"):
            "Look in the mirror" if current_bedroom == Player:
                call screen Player_customization_screen()
            "Shower" if clock > 0:
                call take_a_shower from _call_take_a_shower
            "Shower (locked)" if clock <= 0:
                pass
            "Bedroom":
                if current_bedroom == Player:
                    call travel(current_bedroom.home) from _call_travel_18
                else:
                    call travel(current_bedroom) from _call_travel_19
            "Approach. . ." if Offscreen:
                call approach_Characters from _call_approach_Characters
            "Wait" if time_index < 3:
                call wait_around from _call_wait_around_14
            "Wait (locked)" if time_index > 2:
                pass
                
    call move_location(Player.location) from _call_move_location_6