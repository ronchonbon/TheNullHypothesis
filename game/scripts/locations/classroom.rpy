init python:

    import math

label classroom:
    $ lights_on = True
    $ door_locked = False

    if Player.destination != Player.location:
        $ found_seat = False
        
        call check_for_Events(traveling = True) from _call_check_for_Events_9

        if Player.destination != Player.location:
            if time_index < 2 and weekday < 5:
                call set_the_scene(location = Player.destination, show_Characters = False, greetings = False) from _call_set_the_scene_318

                if clock < math.ceil(0.25*Player.max_stamina):
                    "Class is just about to finish by the time you arrive - what would be the point of joining now?"
                elif clock < math.ceil(0.75*Player.max_stamina):
                    "Class is well under way by the time you arrive - it would be rude to join now."
                elif clock < Player.max_stamina:
                    "Class has already started by the time you arrive."
                else:
                    "Class hasn't started yet."
            else:
                call set_the_scene(location = Player.destination, greetings = True) from _call_set_the_scene_319

    call set_music from _call_set_music_8

    while Player.location == "bg_classroom":
        if clock <= 0:
            if time_index > 2:
                "It's getting late, you head back to your room."

                call travel(Player.home) from _call_travel_23
            else:
                call wait_around from _call_wait_around_17
                
        menu(menu_location = "bg_classroom"):
            "Take morning class" if time_index == 0 and weekday < 5 and clock >= math.ceil(0.75*Player.max_stamina):
                if not found_seat:
                    call find_a_seat from _call_find_a_seat
                    
                    $ found_seat = True
                else:
                    call set_the_scene(location = "bg_classroom", fade = False) from _call_set_the_scene_384

                pause 1.5

                call take_class from _call_take_class
            "Take afternoon class" if time_index == 1 and weekday < 5 and clock >= math.ceil(0.75*Player.max_stamina):
                if not found_seat:
                    call find_a_seat from _call_find_a_seat_1
                    
                    $ found_seat = True
                else:
                    call set_the_scene(location = "bg_classroom", fade = False) from _call_set_the_scene_385

                pause 1.5
                    
                call take_class from _call_take_class_1
            "Take class (locked)" if time_index > 1 or weekday > 4 or clock < math.ceil(0.75*Player.max_stamina):
                pass
            "Grounds":
                call travel("bg_campus") from _call_travel_24
            "Xavier's study":
                call travel("bg_study") from _call_travel_25
            "Approach. . ." if Offscreen and clock == Player.max_stamina:
                call approach_Characters from _call_approach_Characters_2
            "Approach. . . (locked)" if Offscreen and clock < Player.max_stamina:
                call approach_Characters from _call_approach_Characters_8
            "Wait" if time_index < 3:
                call wait_around from _call_wait_around_18
            "Wait (locked)" if time_index > 2:
                pass

    call move_location(Player.location) from _call_move_location_10