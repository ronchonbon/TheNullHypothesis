label set_the_scene(location = None, show_Characters = True, show_Party = True, greetings = False, fade = True, fade_Characters = True, silent = False):
    # $ temp_Character_picker_disabled = Character_picker_disabled
    # $ temp_belt_disabled = belt_disabled

    $ Character_picker_disabled = True
    $ belt_disabled = True

    if silent:
        $ fade = False
        $ fade_Characters = False
    
    if fade and not black_screen:
        $ fade_to_black(0.4)

    if Player.location != Player.destination:
        $ traveling = True
    elif location and location != Player.location:
        $ traveling = True
    else:
        $ traveling = False

    if location:
        $ Player.destination = location
        $ Player.location = location
    else:
        $ location = Player.location

    if not ongoing_Event:
        call set_music from _call_set_music_14

    python:
        for G in Party:
            G.destination = Player.location
            G.location = Player.location

    $ temp_Characters = all_Characters[:]

    while temp_Characters:
        if (not show_Characters or temp_Characters[0].location != Player.location) and renpy.showing(f"{temp_Characters[0].tag}_sprite"):
            call hide_Character(temp_Characters[0], fade = fade_Characters) from _call_hide_Character_47

        $ temp_Characters.remove(temp_Characters[0])

    $ Present = get_Present(location = Player.location)

    $ temp_Professor = None
    
    if show_Characters and Present:
        python:
            number_of_Girls = 0
            number_of_NPCs = 0

            temp_Girls = []
            temp_NPCs = []

            for C in Present:
                if C.teaching and C.location == "bg_classroom":
                    temp_Professor = C
                else:
                    if C in all_Girls and C != focused_Girl:
                        number_of_Girls += 1

                        temp_Girls.append(C)
                    elif C in all_NPCs:
                        number_of_NPCs += 1

                        temp_NPCs.append(C)

                if C.location in ["bg_campus", "bg_pool"] and weather == "rain":
                    C.wet = True
    elif show_Party and Party:
        python:
            number_of_Girls = 0
            number_of_NPCs = 0

            temp_Girls = []
            temp_NPCs = []

            for C in Party:
                if C.teaching and C.location == "bg_classroom":
                    temp_Professor = C
                else:
                    if C in all_Girls and C != focused_Girl:
                        number_of_Girls += 1

                        temp_Girls.append(C)
                    elif C in all_NPCs:
                        number_of_NPCs += 1

                        temp_NPCs.append(C)

                if C.location in ["bg_campus", "bg_pool"] and weather == "rain":
                    C.wet = True

    if (show_Characters and Present) or (show_Party and Party):
        if number_of_Girls:
            if number_of_Girls > 2:
                $ Girl_offset = (stage_far_far_right - stage_center)/number_of_Girls
            else:
                $ Girl_offset = (stage_far_right - stage_center)/number_of_Girls

            $ total_Girl_offset = Girl_offset*number_of_Girls

        if number_of_NPCs:
            if number_of_Girls or (focused_Girl and focused_Girl.location == Player.location):
                $ NPC_offset = (stage_center - stage_far_left)/number_of_NPCs

                if number_of_NPCs > 1:
                    $ total_NPC_offset = NPC_offset*number_of_NPCs
                else:
                    $ total_NPC_offset = stage_center - stage_left
            else:
                $ NPC_offset = (stage_center - stage_far_far_left)/number_of_NPCs

                if number_of_NPCs > 1:
                    $ total_NPC_offset = NPC_offset*(number_of_NPCs - 1)
                else:
                    $ total_NPC_offset = 0

        $ temp_Girls.sort(key = get_sprite_position)
                
        if focused_Girl in temp_Girls:
            $ temp_Girls.remove(focused_Girl)

        $ temp_NPCs.sort(key = get_sprite_position)
        $ temp_NPCs.reverse()

        $ temp_Characters = temp_NPCs + temp_Girls

        $ color_transform = get_color_transform(location = Player.location)

        while temp_Characters:
            if temp_Characters[0].location == Player.location:
                if temp_Characters[0] in all_Girls:
                    call show_Character(temp_Characters[0], sprite_anchor = eval(f"{temp_Characters[0].tag}_standing_anchor"), x = stage_center + total_Girl_offset, y = eval(f"{temp_Characters[0].tag}_standing_height"), sprite_layer = 5, color_transform = color_transform, fade = fade_Characters) from _call_show_Character_11

                    $ total_Girl_offset -= Girl_offset
                elif temp_Characters[0] in all_NPCs:
                    call show_Character(temp_Characters[0], sprite_anchor = eval(f"{temp_Characters[0].tag}_standing_anchor"), x = stage_center - total_NPC_offset, y = eval(f"{temp_Characters[0].tag}_standing_height"), sprite_layer = 5, color_transform = color_transform, fade = fade_Characters) from _call_show_Character_12

                    $ total_NPC_offset -= NPC_offset
            elif renpy.showing(f"{temp_Characters[0].tag}_sprite"):
                call hide_Character(temp_Characters[0], fade = fade_Characters) from _call_hide_Character_48

            $ temp_Characters.remove(temp_Characters[0])

        if focused_Girl and not focused_Girl.teaching:
            if focused_Girl.location == Player.location:
                if number_of_NPCs == 0 or (number_of_NPCs > 0 and number_of_Girls > 1):
                    call show_Character(focused_Girl, sprite_anchor = eval(f"{focused_Girl.tag}_standing_anchor"), x = stage_center, y = eval(f"{focused_Girl.tag}_standing_height"), sprite_layer = 6, color_transform = color_transform, fade = fade_Characters) from _call_show_Character_13
                else:
                    call show_Character(focused_Girl, sprite_anchor = eval(f"{focused_Girl.tag}_standing_anchor"), x = stage_right, y = eval(f"{focused_Girl.tag}_standing_height"), sprite_layer = 6, color_transform = color_transform, fade = fade_Characters) from _call_show_Character_14
            elif renpy.showing(f"{focused_Girl.tag}_sprite"):
                call hide_Character(focused_Girl, fade = fade_Characters) from _call_hide_Character_49

    if temp_Professor:
        $ color_transform = get_color_transform(location = Player.location)

        if temp_Professor.location == Player.location:
            call show_Character(temp_Professor, sprite_anchor = [eval(f"{temp_Professor.tag}_standing_anchor")[0], 1.0], x = 0.4215, y = 0.72, sprite_zoom = 0.3*eval(f"{temp_Professor.tag}_standing_zoom"), sprite_layer = 3, color_transform = color_transform, fade = fade_Characters) from _call_show_Character_15
        elif renpy.showing(f"{temp_Professor.tag}_sprite"):
            call hide_Character(temp_Professor, fade = fade_Characters) from _call_hide_Character_50

    if not silent and black_screen:
        $ fade_in_from_black(0.4)

    if greetings and traveling and Present:
        $ temp_Characters = Present[:]

        python:
            for C in Party:
                if C in temp_Characters:
                    temp_Characters.remove(C)

        if temp_Characters:
            call Characters_greet_Player(temp_Characters) from _call_Characters_greet_Player_13

    # $ Character_picker_disabled = temp_Character_picker_disabled
    # $ belt_disabled = temp_belt_disabled

    $ Character_picker_disabled = False
    $ belt_disabled = False

    return

label add_Characters(Characters, greetings = False, fade = True):
    if Characters in all_Characters:
        $ Characters = [Characters]

    python:
        for C in Characters:            
            C.destination = Player.location
            C.location = Player.location

    call set_the_scene(greetings = greetings, fade = False, fade_Characters = fade) from _call_set_the_scene_325

    return

label remove_Characters(Characters = None, location = None, fade = True):
    if Characters in all_Characters:
        $ Characters = [Characters]

    $ location = Player.location if not location else location
    
    if not Characters:
        $ Present = get_Present(location = location)

        $ Characters = Present[:]

    python:
        for C in Characters:
            C.original_location = location

            reset_behavior(C)

    $ temp_removing_Characters = Characters[:]

    while temp_removing_Characters:
        if temp_removing_Characters[0].location == location:
            if temp_removing_Characters[0] in Party:
                $ Party.remove(temp_removing_Characters[0])

            if temp_removing_Characters[0].destination == temp_removing_Characters[0].location:
                call displace_Characters(temp_removing_Characters[0]) from _call_displace_Characters_1

            $ temp_removing_Characters[0].location = temp_removing_Characters[0].destination

            call hide_Character(temp_removing_Characters[0], fade = fade)

        $ temp_removing_Characters.remove(temp_removing_Characters[0])

    if location == Player.location:
        call set_the_scene(fade = False, fade_Characters = True) from _call_set_the_scene_326
    
    if Characters:
        call set_Character_Outfits(Characters) from _call_set_Character_Outfits_23

    return

label remove_everyone_but(Characters, location = None, fade = True):
    if Characters in all_Characters:
        $ Characters = [Characters]

    $ location = Player.location if not location else location

    $ Present = get_Present(location = location)

    $ temp_removing_Characters = Present[:]

    python:
        for C in Characters:
            while C in temp_removing_Characters:
                temp_removing_Characters.remove(C)

    if temp_removing_Characters:
        call remove_Characters(temp_removing_Characters, fade = fade) from _call_remove_Characters_239

    return

label send_Characters(Characters, location, behavior = None, farewells = False, greetings = False, fade = True):
    if Characters in all_Characters:
        $ Characters = [Characters]

    $ leaving_Characters = []
    $ arriving_Characters = []

    python:
        for C in Characters:
            C.original_location = C.location
            C.destination = location

            if C.destination != C.location:
                if C in Party and C.destination != Player.location:
                    Party.remove(C)

                if C.location == Player.location:
                    leaving_Characters.append(C)
                elif C.destination == Player.location:
                    arriving_Characters.append(C)

    if behavior is None:
        $ set_Character_behavior(Characters)
    else:
        $ reset_behavior(Characters)

        if behavior:
            python:
                for C in Characters:
                    setattr(C, behavior, True)

    if leaving_Characters:
        call Characters_leave(leaving_Characters, farewells = farewells, fade = fade) from _call_Characters_leave_6

    call set_Character_Outfits(Characters) from _call_set_Character_Outfits_24

    if arriving_Characters:
        call Characters_arrive(arriving_Characters, greetings = greetings, fade = fade) from _call_Characters_arrive_3

    python:
        for C in Characters:
            C.location = C.destination

    return

label displace_Characters(Characters):
    if Characters in all_Characters:
        $ Characters = [Characters]

    python:
        for C in Characters:
            count = 0

            while C.destination in [Player.location, C.location] and count < 20:
                C.travel()

                count += 1

            if count >= 20:
                C.location = "nearby"
            else:
                C.location = C.destination

        for C in Characters:
            if C in all_Girls:
                for other_C in active_Girls:
                    if C != other_C and other_C.location not in ["hold", Player.location]:
                        if C not in other_C.likes.keys():
                            other_C.likes[C] = 0
                        
                        if other_C not in C.likes.keys():
                            C.likes[other_C] = 0
                            
                        if C.likes[other_C] > eval(f"{C.tag}_thresholds['friendship'][1]") and other_C.likes[C] > eval(f"{other_C.tag}_thresholds['friendship'][1]"):
                            if renpy.random.random() > 0.9:
                                C.destination = other_C.location

        for C in Characters:
            set_Character_behavior(C)

    $ temp_displacing_Characters = Characters[:]

    while temp_displacing_Characters:
        if not renpy.showing(f"{temp_displacing_Characters[0].tag}_sprite"):
            call set_Character_Outfits(temp_displacing_Characters[0]) from _call_set_Character_Outfits_25

        $ temp_displacing_Characters.remove(temp_displacing_Characters[0])

    return