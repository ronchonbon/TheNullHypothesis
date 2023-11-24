label Characters_arrive(arriving_Characters, invited = False, greetings = True, fade = True):
    $ temp_Character_picker_active = Character_picker_active
    $ temp_temp_belt_disabled = belt_disabled

    $ Character_picker_active = False
    $ belt_disabled = True

    if arriving_Characters in all_Characters:
        $ arriving_Characters = [arriving_Characters]

    python:
        for C in arriving_Characters:
            C.location = "nearby"

    $ temp_arriving_Characters = sort_Characters_by_approval(arriving_Characters[:])[:]

    while temp_arriving_Characters:
        $ grouped_Characters = group_Characters(temp_arriving_Characters)

        if greetings:
            python:
                in_Companions_bedroom = False

                for C in grouped_Characters:
                    if Player.location == C.home:
                        in_Companions_bedroom = True

            if invited or Player.location != Player.home:
                $ verb = "arrives"

                if Player.location in bedrooms or "bg_shower" in Player.location:
                    if in_Companions_bedroom:
                        if len(grouped_Characters) > 1:
                            "You hear some voices chatting outside the door, followed by the turn of the doorknob."
                        else:
                            "You hear someone at the door."
                    else:        
                        call knock_on_door(times = 2) from _call_knock_on_door_34

                        if len(grouped_Characters) > 1:
                            "You hear some voices chatting outside the door, followed by a quick knock."
                        else:
                            "You hear a quick knock at the door."

                if "bg_shower" in Player.location:
                    if in_Companions_bedroom or grouped_Characters[0].has_keys_to_Players_room:
                        "You hear them enter the room."

                        python:
                            for C in grouped_Characters:
                                C.destination = C.destination.replace("_shower", "")
                                C.location = C.location.replace("_shower", "")
                    else:
                        python:
                            for C in grouped_Characters:
                                C.destination = "bg_hallway"
                                C.location = "bg_hallway"

                        call set_the_scene(location = Player.home) from _call_set_the_scene_303

                        $ Character_picker_active = False
                        $ belt_disabled = True

                        "You get the door."

                        call add_Characters(grouped_Characters, fade = fade) from _call_add_Characters_77
                        
                        $ Character_picker_active = False
                        $ belt_disabled = True
                else:
                    call add_Characters(grouped_Characters, fade = fade) from _call_add_Characters_78

                    $ Character_picker_active = False
                    $ belt_disabled = True
            elif grouped_Characters[0].History.check("Player_rejected_knock", tracker = "daily"):
                $ verb = None
            else:
                $ verb = "knocks"
        
                call knock_on_door(times = 2) from _call_knock_on_door_35

                if "bg_shower" in Player.location:
                    ch_Player "One second!"

                    call set_the_scene(location = Player.location.replace("_shower", "")) from _call_set_the_scene_304

                    $ Character_picker_active = False
                    $ belt_disabled = True

            if verb and grouped_Characters[0].behavior != "teaching":
                if not invited:
                    if grouped_Characters[0] in all_Companions:    
                        $ status = grouped_Characters[0].get_status()
                            
                        if status:
                            call expression f"{grouped_Characters[0].tag}_{verb}_{status}" pass (arriving_Characters = grouped_Characters) from _call_expression_359
                        elif approval_check(grouped_Characters[0], threshold = "love"):
                            call expression f"{grouped_Characters[0].tag}_{verb}_love" pass (arriving_Characters = grouped_Characters) from _call_expression_360
                        elif grouped_Characters[0] in Partners:
                            call expression f"{grouped_Characters[0].tag}_{verb}_relationship" pass (arriving_Characters = grouped_Characters) from _call_expression_361
                        else:
                            call expression f"{grouped_Characters[0].tag}_{verb}" pass (arriving_Characters = grouped_Characters) from _call_expression_362
                    else:
                        call expression f"{grouped_Characters[0].tag}_{verb}" from _call_expression_363
                else:
                    call expression f"{grouped_Characters[0].tag}_simple_greeting" from _call_expression_364

                if grouped_Characters[0] in all_Companions and grouped_Characters[0].location == Player.location:
                    $ Characters_to_greet = []

                    python:
                        for C in Present:
                            if C not in grouped_Characters:
                                Characters_to_greet.append(C)
                                
                    while Characters_to_greet:
                        if Characters_to_greet[0] in all_Companions:
                            call expression f"{grouped_Characters[0].tag}_greets_{Characters_to_greet[0].tag}" from _call_expression_365

                        $ Characters_to_greet.remove(Characters_to_greet[0])

            if verb == "knocks" and grouped_Characters[0].location == "nearby":
                python:
                    for C in grouped_Characters:
                        C.History.update("Player_rejected_knock")

                call displace_Characters(grouped_Characters) from _call_displace_Characters

                $ Character_picker_active = False
                $ belt_disabled = True
        else:
            call add_Characters(grouped_Characters, fade = fade) from _call_add_Characters_79

            $ Character_picker_active = False
            $ belt_disabled = True

        python:
            for C in grouped_Characters:
                temp_arriving_Characters.remove(C)
                
    $ Character_picker_active = temp_Character_picker_active
    $ belt_disabled = temp_temp_belt_disabled

    return

label Characters_leave(leaving_Characters, farewells = True, fade = True):
    $ temp_Character_picker_active = Character_picker_active
    $ temp_temp_belt_disabled = belt_disabled

    $ Character_picker_active = False
    $ belt_disabled = True

    if leaving_Characters in all_Characters:
        $ stable_leaving_Characters = [leaving_Characters]
    else:
        $ stable_leaving_Characters = leaving_Characters[:]

    $ temp_leaving_Characters = sort_Characters_by_approval(stable_leaving_Characters[:])[:]

    $ also_leaving = False
    $ Player_has_to_leave = False

    while temp_leaving_Characters:
        $ grouped_Characters = group_Characters(temp_leaving_Characters)

        if farewells:
            if grouped_Characters[0] in all_Companions:  
                $ status = grouped_Characters[0].get_status()
                    
                if status:
                    call expression f"{grouped_Characters[0].tag}_leaves_{status}" pass (leaving_Characters = grouped_Characters, also_leaving = also_leaving) from _call_expression_366
                elif approval_check(grouped_Characters[0], threshold = "love"):
                    call expression f"{grouped_Characters[0].tag}_leaves_love" pass (leaving_Characters = grouped_Characters, also_leaving = also_leaving) from _call_expression_367
                elif grouped_Characters[0] in Partners:
                    call expression f"{grouped_Characters[0].tag}_leaves_relationship" pass (leaving_Characters = grouped_Characters, also_leaving = also_leaving) from _call_expression_368
                else:
                    call expression f"{grouped_Characters[0].tag}_leaves" pass (leaving_Characters = grouped_Characters, also_leaving = also_leaving) from _call_expression_369
            else:
                call expression f"{grouped_Characters[0].tag}_leaves" from _call_expression_370

        $ temp_grouped_Characters = grouped_Characters[:]

        python:
            for C in all_Characters:
                if C in temp_grouped_Characters and C.destination == C.location:
                    temp_grouped_Characters.remove(C)

        if temp_grouped_Characters:
            $ temp_hiding_Characters = temp_grouped_Characters[:]

            while temp_hiding_Characters:
                if temp_hiding_Characters[0] in all_Companions:
                    if sandbox and not ongoing_Event and not temp_hiding_Characters[0].Outfit.wear_in_public and not ((temp_hiding_Characters[0].Outfit.activewear or temp_hiding_Characters[0].Outfit.superwear) and temp_hiding_Characters[0].destination in ["bg_danger", "bg_lockers"]) and not (temp_hiding_Characters[0].Outfit.swimwear and temp_hiding_Characters[0].destination in ["bg_pool"]):                       
                        call set_Character_Outfits(temp_hiding_Characters[0], instant = False) from _call_set_Character_Outfits_21

                        pause 1.0

                call hide_Character(temp_hiding_Characters[0], fade = fade) from _call_hide_Character_46

                if Player.location == temp_hiding_Characters[0].home and temp_hiding_Characters[0] not in Keys:
                    $ Player_has_to_leave = True

                $ temp_hiding_Characters.remove(temp_hiding_Characters[0])

            $ also_leaving = True
            
        python:
            for C in grouped_Characters:
                temp_leaving_Characters.remove(C)

    call remove_Characters(stable_leaving_Characters, fade = False) from _call_remove_Characters_238

    if Player_has_to_leave:
        call move_location("bg_girls_hallway") from _call_move_location_57

    $ Character_picker_active = temp_Character_picker_active
    $ belt_disabled = temp_temp_belt_disabled

    return