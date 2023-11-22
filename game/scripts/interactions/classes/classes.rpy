init python:

    import math

label find_a_seat:            
    $ Character_picker_disabled = True
    $ belt_disabled = True

    $ temp_seated_Characters = sort_Characters_by_approval(Present[:])

    python:
        for C in Present:
            if C in Party:
                temp_seated_Characters.remove(C)

            if C in Professors:
                temp_seated_Characters.remove(C)

    if len(temp_seated_Characters) == 1:
        if clock >= math.ceil(0.9*Player.max_stamina):
            "You see [temp_seated_Characters[0].name] already seated, waiting for class to start."
        else:
            "You see [temp_seated_Characters[0].name] seated across the room, paying attention to the lecture."

        menu:
            extend ""
            "Sit next to [temp_seated_Characters[0].name]":
                if temp_seated_Characters[0] in all_Girls:
                    $ focused_Girl = temp_seated_Characters[0]

                if not renpy.showing(f"{temp_seated_Characters[0].tag}_sprite"):
                    call set_the_scene(location = "bg_classroom", fade = False) from _call_set_the_scene_287
                    
                    call Characters_greet_Player(temp_seated_Characters[0]) from _call_Characters_greet_Player
            "Find a random seat":
                "You find the nearest open chair and take a seat."

                $ temp_seated_Characters[0].location = "nearby"
    elif len(temp_seated_Characters) == 2:
        if are_Characters_friends(temp_seated_Characters):
            if clock >= math.ceil(0.9*Player.max_stamina):
                "You see [temp_seated_Characters[0].name] and [temp_seated_Characters[1].name] sitting together, waiting for class to start."
            else:
                "You see [temp_seated_Characters[0].name] and [temp_seated_Characters[1].name] seated together across the room, paying attention to the lecture."
        
            menu:
                extend ""
                "Sit next to [temp_seated_Characters[0].name]":
                    if temp_seated_Characters[0] in all_Girls:
                        $ focused_Girl = temp_seated_Characters[0]

                    $ temp_seated_Characters[1].location = "nearby"

                    if not renpy.showing(f"{temp_seated_Characters[0].tag}_sprite"):
                        call set_the_scene(location = "bg_classroom", fade = False) from _call_set_the_scene_288
                        
                        call Characters_greet_Player(temp_seated_Characters[0]) from _call_Characters_greet_Player_1
                "Sit next to [temp_seated_Characters[1].name]":
                    if temp_seated_Characters[1] in all_Girls:
                        $ focused_Girl = temp_seated_Characters[1]

                    $ temp_seated_Characters[0].location = "nearby"

                    if not renpy.showing(f"{temp_seated_Characters[1].tag}_sprite"):
                        call set_the_scene(location = "bg_classroom", fade = False) from _call_set_the_scene_289
                        
                        call Characters_greet_Player(temp_seated_Characters[1]) from _call_Characters_greet_Player_2
                "Sit between them":
                    $ sorted_Characters = sort_Characters_by_approval(temp_seated_Characters[:])[:]

                    if sorted_Characters[0] in all_Girls:
                        $ focused_Girl = sorted_Characters[0]

                    if not renpy.showing(f"{sorted_Characters[0].tag}_sprite") or not renpy.showing(f"{sorted_Characters[1].tag}_sprite"):
                        call set_the_scene(location = "bg_classroom", fade = False) from _call_set_the_scene_290
                        
                        call Characters_greet_Player(sorted_Characters[0]) from _call_Characters_greet_Player_3
                "Find a random seat":
                    "You find the nearest open chair and take a seat."

                    $ temp_seated_Characters[0].location = "nearby"
                    $ temp_seated_Characters[1].location = "nearby"
        else:
            if clock >= math.ceil(0.9*Player.max_stamina):
                "You see [temp_seated_Characters[0].name] and [temp_seated_Characters[1].name] sitting separately, waiting for class to start."
            else:
                "You see [temp_seated_Characters[0].name] and [temp_seated_Characters[1].name] seated separately, paying attention to the lecture."
        
            menu:
                extend ""
                "Sit next to [temp_seated_Characters[0].name]":
                    if temp_seated_Characters[0] in all_Girls:
                        $ focused_Girl = temp_seated_Characters[0]

                    $ temp_seated_Characters[1].location = "nearby"

                    if not renpy.showing(f"{temp_seated_Characters[0].tag}_sprite"):
                        call set_the_scene(location = "bg_classroom", fade = False) from _call_set_the_scene_291
                        
                        call Characters_greet_Player(temp_seated_Characters[0]) from _call_Characters_greet_Player_4
                "Sit next to [temp_seated_Characters[1].name]":
                    if temp_seated_Characters[1] in all_Girls:
                        $ focused_Girl = temp_seated_Characters[1]

                    $ temp_seated_Characters[0].location = "nearby"

                    if not renpy.showing(f"{temp_seated_Characters[1].tag}_sprite"):
                        call set_the_scene(location = "bg_classroom", fade = False) from _call_set_the_scene_292
                        
                        call Characters_greet_Player(temp_seated_Characters[1]) from _call_Characters_greet_Player_5
                "Find a random seat":
                    "You find the nearest open chair and take a seat."

                    $ temp_seated_Characters[0].location = "nearby"
                    $ temp_seated_Characters[1].location = "nearby"
    elif len(temp_seated_Characters) > 2:
        if are_Characters_friends(temp_seated_Characters):
            if clock >= math.ceil(0.9*Player.max_stamina):
                "You see [temp_seated_Characters[0].name] and a few others sitting together, waiting for class to start."
            else:
                "You see [temp_seated_Characters[0].name] and a few others seated together across the room, paying attention to the lecture."
        
            menu:
                extend ""
                "Sit next to [temp_seated_Characters[0].name]":
                    if temp_seated_Characters[0] in all_Girls:
                        $ focused_Girl = temp_seated_Characters[0]

                    $ temp_seated_Characters[1].location = "nearby"
                    $ temp_seated_Characters[2].location = "nearby"

                    if not renpy.showing(f"{temp_seated_Characters[0].tag}_sprite"):
                        call set_the_scene(location = "bg_classroom", fade = False) from _call_set_the_scene_293
                        
                        call Characters_greet_Player(temp_seated_Characters[0]) from _call_Characters_greet_Player_6
                "Sit next to [temp_seated_Characters[1].name]":
                    if temp_seated_Characters[1] in all_Girls:
                        $ focused_Girl = temp_seated_Characters[1]

                    $ temp_seated_Characters[0].location = "nearby"
                    $ temp_seated_Characters[2].location = "nearby"

                    if not renpy.showing(f"{temp_seated_Characters[1].tag}_sprite"):
                        call set_the_scene(location = "bg_classroom", fade = False) from _call_set_the_scene_294
                        
                        call Characters_greet_Player(temp_seated_Characters[1]) from _call_Characters_greet_Player_7
                "Sit next to [temp_seated_Characters[2].name]":
                    if temp_seated_Characters[2] in all_Girls:
                        $ focused_Girl = temp_seated_Characters[2]

                    $ temp_seated_Characters[0].location = "nearby"
                    $ temp_seated_Characters[1].location = "nearby"

                    if not renpy.showing(f"{temp_seated_Characters[2].tag}_sprite"):
                        call set_the_scene(location = "bg_classroom", fade = False) from _call_set_the_scene_295
                        
                        call Characters_greet_Player(temp_seated_Characters[2]) from _call_Characters_greet_Player_8
                "Sit in the middle of the group":
                    $ sorted_Characters = sort_Characters_by_approval(temp_seated_Characters[:])[:]

                    if sorted_Characters[0] in all_Girls:
                        $ focused_Girl = sorted_Characters[0]

                    if not renpy.showing(f"{sorted_Characters[0].tag}_sprite") or not renpy.showing(f"{sorted_Characters[1].tag}_sprite") or not renpy.showing(f"{sorted_Characters[2].tag}_sprite"):
                        call set_the_scene(location = "bg_classroom", fade = False) from _call_set_the_scene_296
                        
                        call Characters_greet_Player(sorted_Characters[0]) from _call_Characters_greet_Player_9
                "Find a random seat":
                    "You find the nearest open chair and take a seat."

                    $ temp_seated_Characters[0].location = "nearby"
                    $ temp_seated_Characters[1].location = "nearby"
                    $ temp_seated_Characters[2].location = "nearby"
        else:
            if clock >= math.ceil(0.9*Player.max_stamina):
                "You glance through the audience and spot a few of your friends waiting for class to start."
            else:
                "You glance through the audience and spot a few of your friends paying attention to the lecture."
        
            menu:
                extend ""
                "Sit next to [temp_seated_Characters[0].name]":
                    if temp_seated_Characters[0] in all_Girls:
                        $ focused_Girl = temp_seated_Characters[0]

                    $ temp_seated_Characters[1].location = "nearby"
                    $ temp_seated_Characters[2].location = "nearby"

                    if not renpy.showing(f"{temp_seated_Characters[0].tag}_sprite"):
                        call set_the_scene(location = "bg_classroom", fade = False) from _call_set_the_scene_297
                        
                        call Characters_greet_Player(temp_seated_Characters[0]) from _call_Characters_greet_Player_10
                "Sit next to [temp_seated_Characters[1].name]":
                    if temp_seated_Characters[1] in all_Girls:
                        $ focused_Girl = temp_seated_Characters[1]

                    $ temp_seated_Characters[0].location = "nearby"
                    $ temp_seated_Characters[2].location = "nearby"

                    if not renpy.showing(f"{temp_seated_Characters[1].tag}_sprite"):
                        call set_the_scene(location = "bg_classroom", fade = False) from _call_set_the_scene_298
                        
                        call Characters_greet_Player(temp_seated_Characters[1]) from _call_Characters_greet_Player_11
                "Sit next to [temp_seated_Characters[2].name]":
                    if temp_seated_Characters[2] in all_Girls:
                        $ focused_Girl = temp_seated_Characters[2]

                    $ temp_seated_Characters[0].location = "nearby"
                    $ temp_seated_Characters[1].location = "nearby"

                    if not renpy.showing(f"{temp_seated_Characters[2].tag}_sprite"):
                        call set_the_scene(location = "bg_classroom", fade = False) from _call_set_the_scene_299
                    
                        call Characters_greet_Player(temp_seated_Characters[2]) from _call_Characters_greet_Player_12
                "Find a random seat":
                    "You find the nearest open chair and take a seat."

                    $ temp_seated_Characters[0].location = "nearby"
                    $ temp_seated_Characters[1].location = "nearby"
                    $ temp_seated_Characters[2].location = "nearby"        
    else:
        call set_the_scene(location = "bg_classroom", fade = False) from _call_set_the_scene_383

    $ Character_picker_disabled = False
    $ belt_disabled = False

    return

label take_class:            
    $ Character_picker_disabled = True
    $ belt_disabled = True
    
    python:
        for C in Present:
            C.behavior = "in_class"

    $ Player.behavior = "in_class"

    $ selected_Event = EventScheduler.choose_Event()

    if selected_Event:
        call start_Event(selected_Event) from _call_start_Event_8
    else:
        $ fade_to_black(0.4)
        
        call expression f"chapter_{chapter}_season_{season}_class_narrations" from _call_expression_148

        pause 2.0

    if not black_screen:
        $ fade_to_black(0.4)

    $ clock = 0

    $ Player.History.update("attended_class")

    python:
        for C in Present:
            if C.behavior == "in_class":
                C.History.update("attended_class")
            elif C.behavior == "teaching":
                C.History.update("taught_class")
            
    $ gained_XP = int(20*Player.stat_modifier*Player.max_stamina)
    $ Player.XP += gained_XP

    $ update_messages.append("{color=%s}%s{/color} gained {color=%s}%s XP{/color} from {color=%s}Attending Class{/color}" % ("#feba00", Player.first_name, "#feba00", gained_XP, "#feba00"))

    call check_for_Events(only_automatic = True) from _call_check_for_Events_16
    call move_location(Player.location) from _call_move_location_48

    return