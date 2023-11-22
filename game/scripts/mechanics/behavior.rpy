default temp_Outfit_Characters = []

init python:

    def reset_behavior(Characters = None):
        global all_Characters

        global Player

        if not Characters:
            Characters = all_Characters[:]

            Characters.append(Player)
        elif Characters == Player:
            Characters = [Characters]
        elif Characters in all_Characters:
            Characters = [Characters]

        for C in Characters:
            C.behavior = None

            if C == Player:
                C.behavior_Partners = []

        return
    
    def set_Character_locations(Characters = None):
        global all_Characters

        global Party

        global Player
        
        if not Characters:
            Characters = all_Characters[:]
        elif Characters in all_Characters:
            Characters = [Characters]

        leaving_Characters = []
        arriving_Characters = []

        traveling_Characters = Characters[:]
        renpy.random.shuffle(traveling_Characters)

        for C in traveling_Characters:
            if C not in Party:
                if time_index in C.schedule.keys():
                    C.destination = C.schedule[time_index][0]
                elif time_index == 2 and C in Player.date_planned.keys():
                    C.destination = C.home
                else:
                    C.travel()

        for C in traveling_Characters:
            if C in all_Companions and "hold" not in [C.location, C.destination] and time_index not in C.schedule.keys():
                for other_C in active_Companions:
                    if C != other_C and "hold" not in [other_C.location, other_C.destination]:
                        if C not in other_C.likes.keys():
                            other_C.likes[C] = 0
                        
                        if other_C not in C.likes.keys():
                            C.likes[other_C] = 0

                        if C.location != Player.location and C.likes[other_C] > eval(f"{C.tag}_thresholds['friendship'][1]") and other_C.likes[C] > eval(f"{other_C.tag}_thresholds['friendship'][1]"):
                            if renpy.random.random() > 0.9:
                                C.destination = other_C.destination

        for C in traveling_Characters:
            if C not in Party:
                if C.destination == C.location:
                    pass
                elif C.location == Player.location:
                    leaving_Characters.append(C)
                elif C.destination == Player.location:
                    arriving_Characters.append(C)

        return leaving_Characters, arriving_Characters

    def set_Character_behavior(Characters = None):
        global all_Characters
        global all_Companions
        global Students
        global Professors

        global Player

        global bedrooms

        global time_index
        global clock
        
        if not Characters:
            Characters = all_Characters[:]
        elif Characters in all_Characters:
            Characters = [Characters]

        for C in Party:
            if C in Characters:
                Characters.remove(C)

        reset_behavior(Characters)

        for C in Characters:
            Characters_present = get_Present(location = C.location)

            if clock > 0:
                if time_index in C.schedule.keys():
                    C.behavior = C.schedule[time_index][1]
                elif C.destination in bedrooms:
                    if C.destination in C.home and time_index == 3:
                        C.behavior = "getting_ready_for_bed"
                    elif C in all_Companions and C.destination != Player.location:
                        dice_roll = renpy.random.random()

                        if len(Characters_present) == 1 and dice_roll > 0.9 - 0.01*C.desire:
                            if C == Laura and not EventScheduler.Events["Rogue_Laura_asks_about_masturbation"].completed:
                                C.behavior = "changing"
                            else:
                                C.behavior = "masturbating"
                        elif len(Characters_present) == 1 and dice_roll > 0.5:
                            C.behavior = "changing"
                    elif C in Students:
                        C.behavior = "studying"
                elif C.destination == "bg_classroom" and time_index in [0, 1]:
                    if C in Students:
                        C.behavior = "in_class"
                    elif C in Professors:
                        C.behavior = "teaching"

                        for P in Professors:
                            if P != C and P.behavior == "teaching":
                                while C.location == "bg_classroom":
                                    set_Character_locations(C)
                                    set_Character_behavior(C)

                                break
                elif C.destination == "bg_danger" and time_index < 3:
                    C.behavior = "training"
                elif C.destination == "bg_pool" and time_index < 3:
                    if renpy.random.random() > 0.5 and temperature[time_index] > 25:
                        C.behavior = "swimming"
                    else:
                        C.behavior = "sunbathing"
                elif C.destination == "bg_lockers" or "bg_shower" in C.destination:
                    dice_roll = renpy.random.random()

                    if C.destination == "bg_shower" or dice_roll > 0.5: 
                        C.behavior = "showering"
                    else:
                        C.behavior = "changing"
            else:
                if C.destination == "bg_lockers" or "bg_shower" in C.destination:
                    dice_roll = renpy.random.random()

                    if C.destination == "bg_shower" or dice_roll > 0.5: 
                        C.behavior = "showering"
                    else:
                        C.behavior = "changing"
                elif C.destination in C.home and time_index == 3:
                    C.behavior = "getting_ready_for_bed"

        if C.behavior == "teaching":
            C.schedule[time_index] = [C.destination, "teaching"]
        elif C.behavior == "in_class":
            C.schedule[time_index] = [C.destination, "in_class"]

        return

label set_Character_Outfits(Characters = None, instant = True):
    if not Characters:
        $ Characters = all_Characters[:]
    elif Characters in all_Characters:
        $ Characters = [Characters]

    $ faded = False

    $ temp_Outfit_Characters = Characters[:]

    # this is a redundancy to protect saves made in the middle of this process
    $ temp_Outfit_Characters.append(temp_Outfit_Characters[-1])

    while len(temp_Outfit_Characters) > 1:
        if time_index > 0 or temp_Outfit_Characters[0].destination not in bedrooms:
            if temp_Outfit_Characters[0] in all_Companions:
                if temp_Outfit_Characters[0].location != Player.location:
                    $ temp_Outfit_Characters[0].wet = False
                
                if temp_Outfit_Characters[0].behavior == "on_date":
                    $ Outfit = temp_Outfit_Characters[0].Wardrobe.date_Outfit
                elif (temp_Outfit_Characters[0].behavior == "sleeping" or temp_Outfit_Characters[0].behavior == "getting_ready_for_bed") and (Player.location != temp_Outfit_Characters[0].destination or approval_check(temp_Outfit_Characters[0], threshold = "sleepover")):
                    $ Outfit = temp_Outfit_Characters[0].Wardrobe.sleeping_Outfit
                elif temp_Outfit_Characters[0].behavior == "training":
                    $ Outfit = temp_Outfit_Characters[0].Wardrobe.gym_Outfit
                elif temp_Outfit_Characters[0].behavior in ["swimming", "sunbathing"]:
                    $ Outfit = temp_Outfit_Characters[0].Wardrobe.swimming_Outfit
                elif temp_Outfit_Characters[0].destination == "bg_lockers" and temp_Outfit_Characters[0].behavior == "showering":
                    if Player.location == "bg_lockers":
                        if temp_Outfit_Characters[0].location == "bg_danger":
                            $ Outfit = temp_Outfit_Characters[0].Wardrobe.gym_Outfit
                        elif temp_Outfit_Characters[0].location == "bg_pool":
                            $ Outfit = temp_Outfit_Characters[0].Wardrobe.swimming_Outfit
                        elif temp_Outfit_Characters[0].location == "bg_lockers":
                            $ Outfit = temp_Outfit_Characters[0].Wardrobe.swimming_Outfit
                        elif temp_Outfit_Characters[0].location == "nearby":
                            $ Outfit = temp_Outfit_Characters[0].Wardrobe.swimming_Outfit
                        else:
                            $ Outfit = temp_Outfit_Characters[0].Wardrobe.indoor_Outfit
                    else:
                        $ Outfit = temp_Outfit_Characters[0].Wardrobe.swimming_Outfit
                elif temp_Outfit_Characters[0].destination == "bg_lockers" and temp_Outfit_Characters[0].behavior == "changing":
                    if temp_Outfit_Characters[0].location == "bg_danger":
                        $ Outfit = temp_Outfit_Characters[0].Wardrobe.gym_Outfit
                    elif temp_Outfit_Characters[0].location == "bg_pool":
                        $ Outfit = temp_Outfit_Characters[0].Wardrobe.swimming_Outfit
                    else:
                        $ Outfit = temp_Outfit_Characters[0].Wardrobe.indoor_Outfit
                elif "bg_shower" in temp_Outfit_Characters[0].destination and temp_Outfit_Characters[0].behavior == "showering":
                    $ Outfit = temp_Outfit_Characters[0].Wardrobe.Outfits["Nude"]
                elif temp_Outfit_Characters[0].destination in ["bg_campus", "bg_pool"]:
                    $ Outfit = temp_Outfit_Characters[0].Wardrobe.outdoor_Outfit
                elif temp_Outfit_Characters[0].destination in bedrooms:
                    $ Outfit = temp_Outfit_Characters[0].Wardrobe.private_Outfit
                else:
                    $ Outfit = temp_Outfit_Characters[0].Wardrobe.indoor_Outfit

                if temp_Outfit_Characters[0].location in public_locations and not Outfit.wear_in_public and (Outfit.wear_in_private or Outfit.sleepwear):
                    $ Outfit = temp_Outfit_Characters[0].Wardrobe.indoor_Outfit

                if renpy.showing(f"{temp_Outfit_Characters[0].tag}_sprite") and not black_screen and not instant:
                    $ Items_to_remove, Items_to_add = get_changed_Items(temp_Outfit_Characters[0], Outfit)

                    call does_Character_want_privacy(temp_Outfit_Characters[0], Items_to_add = Items_to_add, Items_to_remove = Items_to_remove) from _call_does_Character_want_privacy

                    if (Items_to_add or Items_to_remove) and _return:
                        $ fade_to_black(0.4)

                        $ faded = True

                if temp_Outfit_Characters:
                    if renpy.showing(f"{temp_Outfit_Characters[0].tag}_sprite") and not black_screen:
                        call change_Outfit(temp_Outfit_Characters[0], Outfit, instant = instant) from _call_change_Outfit_44
                    else:
                        call change_Outfit(temp_Outfit_Characters[0], Outfit, instant = True) from _call_change_Outfit_45

                if temp_Outfit_Characters:
                    # if temp_Outfit_Characters[0].behavior == "showering" and temp_Outfit_Characters[0].location == "nearby":
                    #     call try_on(temp_Outfit_Characters[0], temp_Outfit_Characters[0].Wardrobe.Clothes["towel"], instant = True) from _call_try_on_15
                    
                    if temp_Outfit_Characters[0].behavior == "showering" and Player.location not in [temp_Outfit_Characters[0].location, temp_Outfit_Characters[0].destination]:
                        if renpy.random.random() > 0.5:
                            $ temp_Outfit_Characters[0].behavior = None
                            $ temp_Outfit_Characters[0].wet = True
            elif temp_Outfit_Characters[0] in all_NPCs:
                if temp_Outfit_Characters[0] == Kurt:
                    if temp_Outfit_Characters[0].behavior == "training":
                        if temperature[0] < 10 and temp_Outfit_Characters[0].destination in ["bg_campus", "bg_pool"]:
                            if renpy.showing(f"{temp_Outfit_Characters[0].tag}_sprite") and not black_screen and not instant and temp_Outfit_Characters[0].outfit != "suit_coat":
                                $ fade_to_black(0.4)

                                $ faded = True

                            $ temp_Outfit_Characters[0].outfit = "suit_coat"
                        else:
                            if renpy.showing(f"{temp_Outfit_Characters[0].tag}_sprite") and not black_screen and not instant and temp_Outfit_Characters[0].outfit != "suit":
                                $ fade_to_black(0.4)

                                $ faded = True

                            $ temp_Outfit_Characters[0].outfit = "suit"
                    else:
                        if temperature[0] < 10 and temp_Outfit_Characters[0].destination in ["bg_campus", "bg_pool"]:
                            if renpy.showing(f"{temp_Outfit_Characters[0].tag}_sprite") and not black_screen and not instant and temp_Outfit_Characters[0].outfit != "winter":
                                $ fade_to_black(0.4)

                                $ faded = True

                            $ temp_Outfit_Characters[0].outfit = "winter"
                        else:
                            if renpy.showing(f"{temp_Outfit_Characters[0].tag}_sprite") and not black_screen and not instant and temp_Outfit_Characters[0].outfit != "casual":
                                $ fade_to_black(0.4)

                                $ faded = True

                            $ temp_Outfit_Characters[0].outfit = "casual"

        if temp_Outfit_Characters:
            $ temp_Outfit_Characters.remove(temp_Outfit_Characters[0])

    $ temp_Outfit_Characters = []

    if faded:
        pause 1.0

        $ fade_in_from_black(0.4)

    return