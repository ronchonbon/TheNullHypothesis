init python:
    
    def send_Characters_Offscreen(Characters, location = None):
        global Present
        global left_Slot
        global middle_Slot
        global right_Slot
        global Offscreen

        if Characters in all_Characters:
            Characters = [Characters]

        if not location:
            location = Player.location

        Present = get_Present(location = location)[0]

        for C in Characters:
            if C in Present:
                C.destination = location
                C.location = location

                if C == left_Slot:
                    left_Slot = None

                if C == middle_Slot:
                    middle_Slot = None

                if C == right_Slot:
                    right_Slot = None

                if C not in Offscreen:
                    Offscreen.append(C)

        return

label set_the_scene(location = None, show_Characters = True, show_Party = True, show_Background = True, greetings = False, fade = True, fade_Characters = 0.5, silent = False, selected_Character = None):
    $ temp_Character_picker_disabled = Character_picker_disabled
    $ temp_belt_disabled = belt_disabled

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

    $ fade_at_end = False

    if selected_Character:
        if fade_Characters:
            $ fade_Characters = False
            $ fade_at_end = 0.25

        if selected_Character != middle_Slot:
            call hide_Character(selected_Character, fade = fade_Characters, send_Offscreen = False) from _call_hide_Character_49

        if selected_Character in Offscreen:
            $ Offscreen.remove(selected_Character)

        if selected_Character in Background:
            $ Background.remove(selected_Character)
    elif fade_Characters == "end":
        $ fade_Characters = False
        $ fade_at_end = 0.25

    $ renpy.dynamic(temp_Characters = Sprites[:])

    while temp_Characters:
        if not show_Characters or temp_Characters[0].location != Player.location:
            call hide_Character(temp_Characters[0], fade = fade_Characters) from _call_hide_Character_47

        $ temp_Characters.remove(temp_Characters[0])

    $ Present, left_Slot, middle_Slot, right_Slot, Offscreen = get_Present(location = Player.location, selected_Character = selected_Character, traveling = traveling)

    if traveling:
        $ Background = []
    else:
        if left_Slot in Background:
            $ Background.remove(left_Slot)

        if left_Slot in Background:
            $ Background.remove(middle_Slot)

        if left_Slot in Background:
            $ Background.remove(right_Slot)

        python:
            for C in Offscreen:
                if C in Background:
                    Background.remove(C)

    $ renpy.dynamic(temp_Characters = Offscreen[:])
    
    while temp_Characters:
        call hide_Character(temp_Characters[0], fade = fade_Characters) from _call_hide_Character_50

        $ temp_Characters.remove(temp_Characters[0])

    if (show_Characters and Present) or (show_Party and Party):
        python:
            for C in Present:
                if C.location in ["bg_campus", "bg_pool"] and weather == "rain":
                    C.wet = True

        $ color_transform = get_color_transform(location = Player.location)

        if show_Background and location in location_Slots.keys():
            $ renpy.dynamic(temp_Characters = Present[:])

            if left_Slot in temp_Characters:
                $ temp_Characters.remove(left_Slot)

            if middle_Slot in temp_Characters:
                $ temp_Characters.remove(middle_Slot)

            if right_Slot in temp_Characters:
                $ temp_Characters.remove(right_Slot)

            while temp_Characters:
                $ chosen_Slot = None

                python:
                    for S in location_Slots[location].values():
                        if S["position"] == temp_Characters[0].sprite_position:
                            chosen_Slot = S

                            break

                if chosen_Slot:
                    $ x = temp_Characters[0].sprite_position[0]
                    $ y = temp_Characters[0].sprite_position[1]
                    $ sprite_zoom = eval(f"{temp_Characters[0].tag}_standing_zoom")
                    $ sprite_layer = temp_Characters[0].sprite_layer

                    if chosen_Slot["anchor"][0] and chosen_Slot["anchor"][1]:    
                        $ anchor = [chosen_Slot["anchor"][0], chosen_Slot["anchor"][1]]

                    if chosen_Slot["anchor"][0]:
                        $ anchor = [chosen_Slot["anchor"][0], eval(f"{temp_Characters[0].tag}_standing_anchor")[1]]

                    if chosen_Slot["anchor"][1]:
                        $ anchor = [eval(f"{temp_Characters[0].tag}_standing_anchor")[0], chosen_Slot["anchor"][1]]

                    if chosen_Slot["position"][0]:
                        $ x = chosen_Slot["position"][0]

                    if chosen_Slot["position"][1]:
                        $ y = chosen_Slot["position"][1]

                    if chosen_Slot["zoom"]:
                        $ sprite_zoom = chosen_Slot["zoom"]*sprite_zoom
                        $ temp_Characters[0].sprite_zoom = sprite_zoom

                    if chosen_Slot["layer"]:
                        $ sprite_layer = chosen_Slot["layer"]

                    if chosen_Slot["color_transform"]:
                        $ background_color_transform = chosen_Slot["color_transform"]

                        call show_Character(temp_Characters[0], sprite_anchor = anchor, x = x, y = y, sprite_zoom = sprite_zoom, sprite_layer = sprite_layer, color_transforms = [color_transform, background_color_transform, depth_of_field], fade = fade_Characters) from _call_show_Character_11
                    else:
                        call show_Character(temp_Characters[0], sprite_anchor = anchor, x = x, y = y, sprite_zoom = sprite_zoom, sprite_layer = sprite_layer, color_transforms = [color_transform, depth_of_field], fade = fade_Characters) from _call_show_Character_12

                    if temp_Characters[0] not in Background:
                        $ Background.append(temp_Characters[0])

                $ temp_Characters.remove(temp_Characters[0])

        $ renpy.dynamic(temp_Characters = Present[:])

        while temp_Characters:
            if temp_Characters[0] not in [left_Slot, middle_Slot, right_Slot] and temp_Characters[0] not in Background:
                call hide_Character(temp_Characters[0], fade = fade_Characters) from _call_hide_Character_52

            $ temp_Characters.remove(temp_Characters[0])

        if right_Slot and (not renpy.showing(f"{right_Slot.tag}_sprite") or right_Slot.sprite_position[0] != stage_far_right or color_transform):
            $ renpy.dynamic(temp_Characters = Present[:])

            while temp_Characters:
                if temp_Characters[0] != right_Slot and temp_Characters[0].sprite_position[0] in [stage_far_right, stage_far_right - 0.05]:
                    call hide_Character(temp_Characters[0], fade = fade_Characters, send_Offscreen = False) from _call_hide_Character_53

                $ temp_Characters.remove(temp_Characters[0])

            call show_Character(right_Slot, x = stage_far_right, color_transforms = [color_transform], fade = fade_Characters) from _call_show_Character_13

        if left_Slot and (not renpy.showing(f"{left_Slot.tag}_sprite") or left_Slot.sprite_position[0] != stage_left or color_transform):
            $ renpy.dynamic(temp_Characters = Present[:])

            while temp_Characters:
                if temp_Characters[0] != left_Slot and temp_Characters[0].sprite_position[0] in [stage_left, stage_left + 0.05]:
                    call hide_Character(temp_Characters[0], fade = fade_Characters, send_Offscreen = False) from _call_hide_Character_54

                $ temp_Characters.remove(temp_Characters[0])

            call show_Character(left_Slot, x = stage_left, color_transforms = [color_transform], fade = fade_Characters) from _call_show_Character_14

        if left_Slot and right_Slot:
            $ x = (stage_left + stage_far_right)/2
        elif left_Slot:
            $ x = stage_far_right - 0.05
        elif right_Slot:
            $ x = stage_left + 0.05
        else:
            $ x = stage_center

        if middle_Slot and (not renpy.showing(f"{middle_Slot.tag}_sprite") or middle_Slot.sprite_position[0] != x or color_transform):
            $ renpy.dynamic(temp_Characters = Present[:])

            while temp_Characters:
                if temp_Characters[0] != middle_Slot and temp_Characters[0].sprite_position[0] in [(stage_left + stage_far_right)/2, stage_far_right - 0.05, stage_left + 0.05, stage_center]:
                    call hide_Character(temp_Characters[0], fade = fade_Characters, send_Offscreen = False) from _call_hide_Character_55

                $ temp_Characters.remove(temp_Characters[0])

            call show_Character(middle_Slot, x = x, color_transforms = [color_transform], fade = fade_Characters) from _call_show_Character_15

    $ renpy.dynamic(temp_Characters = Present[:])

    while temp_Characters:
        if temp_Characters[0] not in [left_Slot, middle_Slot, right_Slot] and temp_Characters[0] not in Background:
            call hide_Character(temp_Characters[0], fade = fade_Characters) from _call_hide_Character_56

        $ temp_Characters.remove(temp_Characters[0])

    if fade_at_end:
        with Dissolve(fade_at_end)

    if not silent and black_screen:
        $ fade_in_from_black(0.4)

    if Present and greetings:
        if traveling:
            $ renpy.dynamic(temp_Characters = [])

            if left_Slot:
                $ temp_Characters.append(left_Slot)

            if middle_Slot:
                $ temp_Characters.append(middle_Slot)

            if right_Slot:
                $ temp_Characters.append(right_Slot)

            python:
                for C in Party:
                    if C in temp_Characters:
                        temp_Characters.remove(C)

            if temp_Characters:
                call Characters_greet_Player(temp_Characters) from _call_Characters_greet_Player_13
        elif new_Characters:
            call Characters_greet_Player(new_Characters) from _call_Characters_greet_Player_14

            $ new_Characters = []

    $ Character_picker_disabled = temp_Character_picker_disabled
    $ belt_disabled = temp_belt_disabled

    # $ Character_picker_disabled = False
    # $ belt_disabled = False

    if selected_Character:
        show screen interactions_screen(Character = selected_Character)

    return

label add_Characters(Characters, direction = None, greetings = False, fade = True):
    if Characters in all_Characters:
        $ Characters = [Characters]

    python:
        for C in Characters:            
            C.destination = Player.location
            C.location = Player.location

            if direction:
                if C in Offscreen:
                    Offscreen.remove(C)

                if C in Background:
                    Background.remove(C)

            if direction == "right":
                if right_Slot:
                    left_Slot, middle_Slot, right_Slot = middle_Slot, right_Slot, C
                else:
                    right_Slot = C
            elif direction == "left":
                if left_Slot:
                    left_Slot, middle_Slot, right_Slot = C, left_Slot, middle_Slot
                else:
                    left_Slot = C
            elif direction == "middle":
                if middle_Slot:
                    left_Slot, middle_Slot, right_Slot = middle_Slot, C, left_Slot
                else:
                    middle_Slot = C
            elif direction == "offscreen":
                Offscreen.append(C)
            elif C not in [left_Slot, middle_Slot, right_Slot]:
                if not middle_Slot:
                    middle_Slot = C
                elif not left_Slot:
                    left_Slot = C
                elif not right_Slot:
                    right_Slot = C
                else:
                    Offscreen.append(C)

    $ new_Characters = Characters[:]

    if fade:
        call set_the_scene(greetings = greetings, fade = False, fade_Characters = "end") from _call_set_the_scene_325
    else:
        call set_the_scene(greetings = greetings, fade = False, fade_Characters = False) from _call_set_the_scene_328

    return

label remove_Characters(Characters = None, location = None, fade = True):
    if Characters in all_Characters:
        $ Characters = [Characters]

    $ location = Player.location if not location else location
    
    if not Characters:
        $ Present = get_Present(location = location)[0]

        $ Characters = Present[:]

    python:
        for C in Characters:
            C.original_location = location

            reset_behavior(C)

    $ renpy.dynamic(temp_Characters = Characters[:])

    while temp_Characters:
        if temp_Characters[0].location == location:
            if temp_Characters[0] in Party:
                $ Party.remove(temp_Characters[0])

            if temp_Characters[0].destination == temp_Characters[0].location:
                call displace_Characters(temp_Characters[0]) from _call_displace_Characters_1

            $ temp_Characters[0].location = temp_Characters[0].destination

            if temp_Characters[0] in Offscreen:
                $ Offscreen.remove(temp_Characters[0])

            if temp_Characters[0] in Background:
                $ Background.remove(temp_Characters[0])

        $ temp_Characters.remove(temp_Characters[0])

    if location == Player.location:
        call set_the_scene(fade = False, fade_Characters = "end") from _call_set_the_scene_326
    
    if Characters:
        call set_Character_Outfits(Characters) from _call_set_Character_Outfits_23

    return

label remove_everyone_but(Characters, location = None, fade = True):
    if Characters in all_Characters:
        $ Characters = [Characters]

    $ location = Player.location if not location else location

    $ Present = get_Present(location = location)[0]

    $ renpy.dynamic(temp_Characters = Present[:])

    python:
        for C in Characters:
            if C in temp_Characters:
                temp_Characters.remove(C)

    if temp_Characters:
        call remove_Characters(temp_Characters, fade = fade) from _call_remove_Characters_239

    return

label send_Characters(Characters, location, behavior = None, farewells = False, greetings = False, fade = True):
    if Characters in all_Characters:
        $ Characters = [Characters]

    $ renpy.dynamic(leaving_Characters = [])
    $ renpy.dynamic(arriving_Characters = [])

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
                    C.behavior = behavior

    if leaving_Characters:
        call Characters_leave(leaving_Characters, farewells = farewells, fade = fade, remove = False) from _call_Characters_leave_6

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
                send_Characters_Offscreen(C)
            else:
                C.location = C.destination

        for C in Characters:
            if C in all_Companions:
                for other_C in active_Companions:
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

    $ renpy.dynamic(temp_Characters = Characters[:])

    while temp_Characters:
        if not renpy.showing(f"{temp_Characters[0].tag}_sprite"):
            call set_Character_Outfits(temp_Characters[0]) from _call_set_Character_Outfits_25

        $ temp_Characters.remove(temp_Characters[0])

    return

label swap_Slots(Character, new_Slot):
    $ renpy.dynamic(previous_Slot = None)

    if left_Slot == Character:
        $ previous_Slot = "left"
    elif middle_Slot == Character:
        $ previous_Slot = "middle"
    elif right_Slot == Character:
        $ previous_Slot = "right"

    if previous_Slot:
        $ exec(f"{previous_Slot}_Slot, {new_Slot}_Slot = {new_Slot}_Slot, {previous_Slot}_Slot")
    else:
        $ exec(f"{new_Slot}_Slot = Character")

    call set_the_scene(greetings = False, fade = False) from _call_set_the_scene_305

    return