init python:

    import copy

label Character_orgasms(Character):
    $ Action_auto_progress = False
    $ Action_auto_progress_timer = 0.0

    $ has_progression_control = False
    $ has_Action_control = False
    $ has_position_control = False
    $ has_movement_control = False

    $ Character.orgasming = True

    call Character_orgasm_narrations(Character) from _call_Character_orgasm_narrations

    $ Character.History.update("orgasmed_with_Player")

    $ Character.orgasming = False

    $ Character.stamina -= 1 if Character.stamina > 0 else 0

    if Character.stamina:
        $ Character.desire = int(100 - 50/Character.History.check("orgasmed_with_Player", tracker = "recent"))
    else:
        $ Character.desire = 0

    $ Character.status["horny"] = False

    # if not Character.stamina or hookup_length >= max_hookup_length:
    #     python:
    #         for A in Character.all_Actions:
    #             if A not in Player.cock_Actions:
    #                 stop_Action(A)

    $ has_progression_control = True
    $ has_Action_control = True
    $ has_position_control = True
    $ has_movement_control = True
    $ has_ejaculation_control = True

    return

label Player_orgasms:
    $ Action_auto_progress = False
    $ Action_auto_progress_timer = 0.0
    
    $ has_progression_control = False
    $ has_Action_control = False
    $ has_position_control = False
    $ has_movement_control = False

    $ choice_disabled = False

    if focused_Character in [Laura, Jean] and focused_Character.quirk and not Player.History.check("orgasmed", tracker = "daily"):
        $ climax_choice = focused_Character
    else:
        if has_ejaculation_control:
            call expression f"{focused_Character.tag}_lets_Player_decide_cumshot" from _call_expression_130
            
            $ climax_choice = None

            $ _return = False

            while not _return:
                menu:
                    "Where do you want to cum?"
                    "Let [focused_Character.name] decide":
                        $ climax_choice = focused_Character
                    "On the floor":
                        $ climax_choice = "floor"
                    "Her belly" if "missionary" in focused_Character.possible_poses:
                        $ climax_choice = "cumshot_belly"
                    "Her breasts" if "missionary" in focused_Character.possible_poses:
                        $ climax_choice = "cumshot_breasts"
                    "Her face" if "hands_and_knees" in focused_Character.possible_poses:
                        $ climax_choice = "cumshot_face"
                    "Her hair" if "hands_and_knees" in focused_Character.possible_poses:
                        $ climax_choice = "cumshot_hair"
                    "Her back" if "doggy" in focused_Character.possible_poses:
                        $ climax_choice = "cumshot_back"
                    "Her ass" if "doggy" in focused_Character.possible_poses:
                        $ climax_choice = "cumshot_ass"
                    # "Her feet":
                    #     $ climax_choice = "cumshot_feet"
                    "Inside her" if focused_Character.History.check("sex"):
                        $ climax_choice = "creampie"
                    "In her mouth" if focused_Character.History.check("blowjob") or focused_Character.History.check("deepthroat"):
                        $ climax_choice = "cum_in_mouth"
                    "Down her throat" if focused_Character.History.check("deepthroat"):
                        $ climax_choice = "cum_down_throat"
                    "In her ass" if focused_Character.History.check("anal"):
                        $ climax_choice = "anal_creampie"
                    "Delay" if Player.orgasm_control or (focused_Character.History.check("made_Player_orgasm") >= 5 and Player.History.check("delayed_orgasm", tracker = "recent") < 3):
                        $ Player.History.update("delayed_orgasm")
                        $ Player.desire -= 50/Player.History.check("delayed_orgasm", tracker = "recent")

                        $ has_progression_control = True
                        $ has_Action_control = True
                        $ has_position_control = True
                        $ has_movement_control = True
                        $ has_ejaculation_control = True

                        $ choice_disabled = True
                        
                        return

                if climax_choice not in all_Companions and climax_choice != "floor":
                    call ask_Character_for_cumshot(focused_Character, climax_choice) from _call_ask_Character_for_cumshot
                else:
                    $ _return = "floor"

    $ choice_disabled = True

    if not has_ejaculation_control or climax_choice in all_Companions:
        call expression f"{focused_Character.tag}_decides_cumshot" from _call_expression_39

    if _return:
        $ cumshot_location = _return
    else:
        $ cumshot_location = "floor"

    $ focused_Character.History.update("made_Player_orgasm")
    $ focused_Character.History.update(cumshot_location)

    if cumshot_location == "cumshot_belly" and focused_Character.position != "missionary":
        call request_position(focused_Character, "missionary") from _call_request_position
    elif cumshot_location == "cumshot_breasts" and focused_Character.position != "missionary":
        call request_position(focused_Character, "missionary") from _call_request_position_1
    elif cumshot_location == "cumshot_face" and focused_Character.position != "hands_and_knees":
        call request_position(focused_Character, "hands_and_knees") from _call_request_position_2
    elif cumshot_location == "cumshot_hair" and focused_Character.position != "hands_and_knees":
        call request_position(focused_Character, "hands_and_knees") from _call_request_position_3
    elif cumshot_location == "cumshot_back" and focused_Character.position != "doggy":
        call request_position(focused_Character, "doggy") from _call_request_position_4
    elif cumshot_location == "cumshot_ass" and focused_Character.position != "doggy":
        call request_position(focused_Character, "doggy") from _call_request_position_5
    # elif cumshot_location == "cumshot_feet":
    #     call request_position(focused_Character, "footjob")
    elif cumshot_location == "creampie" and focused_Character.position not in ["missionary", "doggy"]:
        call request_position(focused_Character, "missionary") from _call_request_position_6

        if _return:
            call expose(focused_Character, "pussy") from _call_expose_18

            $ _return = True
    elif cumshot_location == "cum_in_mouth" and focused_Character.position != "hands_and_knees":
        call request_position(focused_Character, "hands_and_knees") from _call_request_position_7
    elif cumshot_location == "cum_down_throat" and focused_Character.position != "hands_and_knees":
        call request_position(focused_Character, "hands_and_knees") from _call_request_position_17
    elif cumshot_location == "anal_creampie":
        if focused_Character.position not in ["missionary", "doggy"] and "doggy" in focused_Character.available_poses:
            call request_position(focused_Character, "doggy") from _call_request_position_8
        else:
            call request_position(focused_Character, "missionary") from _call_request_position_9

        if _return:
            call expose(focused_Character, "anus") from _call_expose_19

            $ _return = True

    if not _return:
        $ cumshot_location = "floor"

    if cumshot_location in ["floor"] or "cumshot" in cumshot_location:
        $ Player.orgasming = "cumshot"
    else:
        $ Player.orgasming = cumshot_location

    call Player_orgasm_narrations(focused_Character, location = cumshot_location) from _call_Player_orgasm_narrations

    if cumshot_location == "cumshot_belly":
        $ focused_Character.spunk["belly"] = 1

        pause 0.5

        $ focused_Character.spunk["belly"] = 2

        python:
            for Clothing_type in all_Clothing_types:
                if focused_Character.Clothes[Clothing_type].string:
                    if "belly" in focused_Character.Clothes[Clothing_type].covers[focused_Character.position].keys() and focused_Character.Clothes[Clothing_type].state in focused_Character.Clothes[Clothing_type].covers[focused_Character.position]["belly"]:
                        focused_Character.Clothes[Clothing_type].soiled = True
                        
                        for covering_Clothing_type in all_Clothing_types:
                            if focused_Character.Clothes[covering_Clothing_type].string:
                                if "belly" in focused_Character.Clothes[covering_Clothing_type].covers[focused_Character.position].keys() and focused_Character.Clothes[covering_Clothing_type].state in focused_Character.Clothes[covering_Clothing_type].covers[focused_Character.position]["belly"]:
                                    if focused_Character.Clothes[covering_Clothing_type].string in focused_Character.Clothes[Clothing_type].covered_by.keys() and focused_Character.Clothes[covering_Clothing_type].state in focused_Character.Clothes[Clothing_type].covered_by[focused_Character.Clothes[covering_Clothing_type].string]:
                                        focused_Character.Clothes[Clothing_type].soiled = False
                                        focused_Character.Clothes[covering_Clothing_type].soiled = True
    elif cumshot_location == "cumshot_breasts":
        $ focused_Character.spunk["breasts"] = 1

        pause 0.5

        $ focused_Character.spunk["breasts"] = 2

        python:
            for Clothing_type in all_Clothing_types:
                if focused_Character.Clothes[Clothing_type].string:
                    if "breasts" in focused_Character.Clothes[Clothing_type].covers[focused_Character.position].keys() and focused_Character.Clothes[Clothing_type].state in focused_Character.Clothes[Clothing_type].covers[focused_Character.position]["breasts"]:
                        focused_Character.Clothes[Clothing_type].soiled = True
                        
                        for covering_Clothing_type in all_Clothing_types:
                            if focused_Character.Clothes[covering_Clothing_type].string:
                                if "breasts" in focused_Character.Clothes[covering_Clothing_type].covers[focused_Character.position].keys() and focused_Character.Clothes[covering_Clothing_type].state in focused_Character.Clothes[covering_Clothing_type].covers[focused_Character.position]["breasts"]:
                                    if focused_Character.Clothes[covering_Clothing_type].string in focused_Character.Clothes[Clothing_type].covered_by.keys() and focused_Character.Clothes[covering_Clothing_type].state in focused_Character.Clothes[Clothing_type].covered_by[focused_Character.Clothes[covering_Clothing_type].string]:
                                        focused_Character.Clothes[Clothing_type].soiled = False
                                        focused_Character.Clothes[covering_Clothing_type].soiled = True
    elif cumshot_location == "cumshot_face":
        $ focused_Character.spunk["face"] = 1

        pause 0.5

        $ focused_Character.spunk["face"] = 2
    elif cumshot_location == "cumshot_hair":
        $ focused_Character.spunk["hair"] = 1

        pause 0.5

        $ focused_Character.spunk["hair"] = 2
    elif cumshot_location == "cumshot_back":
        $ focused_Character.spunk["back"] = 1

        pause 0.5

        $ focused_Character.spunk["back"] = 2

        python:
            for Clothing_type in all_Clothing_types:
                if focused_Character.Clothes[Clothing_type].string:
                    if "back" in focused_Character.Clothes[Clothing_type].covers[focused_Character.position].keys() and focused_Character.Clothes[Clothing_type].state in focused_Character.Clothes[Clothing_type].covers[focused_Character.position]["back"]:
                        focused_Character.Clothes[Clothing_type].soiled = True
                        
                        for covering_Clothing_type in all_Clothing_types:
                            if focused_Character.Clothes[covering_Clothing_type].string:
                                if "back" in focused_Character.Clothes[covering_Clothing_type].covers[focused_Character.position].keys() and focused_Character.Clothes[covering_Clothing_type].state in focused_Character.Clothes[covering_Clothing_type].covers[focused_Character.position]["back"]:
                                    if focused_Character.Clothes[covering_Clothing_type].string in focused_Character.Clothes[Clothing_type].covered_by.keys() and focused_Character.Clothes[covering_Clothing_type].state in focused_Character.Clothes[Clothing_type].covered_by[focused_Character.Clothes[covering_Clothing_type].string]:
                                        focused_Character.Clothes[Clothing_type].soiled = False
                                        focused_Character.Clothes[covering_Clothing_type].soiled = True
    elif cumshot_location == "cumshot_ass":
        $ focused_Character.spunk["ass"] = 1

        pause 0.5

        $ focused_Character.spunk["ass"] = 2

        python:
            for Clothing_type in all_Clothing_types:
                if focused_Character.Clothes[Clothing_type].string:
                    if "ass" in focused_Character.Clothes[Clothing_type].covers[focused_Character.position].keys() and focused_Character.Clothes[Clothing_type].state in focused_Character.Clothes[Clothing_type].covers[focused_Character.position]["ass"]:
                        focused_Character.Clothes[Clothing_type].soiled = True
                        
                        for covering_Clothing_type in all_Clothing_types:
                            if focused_Character.Clothes[covering_Clothing_type].string:
                                if "ass" in focused_Character.Clothes[covering_Clothing_type].covers[focused_Character.position].keys() and focused_Character.Clothes[covering_Clothing_type].state in focused_Character.Clothes[covering_Clothing_type].covers[focused_Character.position]["ass"]:
                                    if focused_Character.Clothes[covering_Clothing_type].string in focused_Character.Clothes[Clothing_type].covered_by.keys() and focused_Character.Clothes[covering_Clothing_type].state in focused_Character.Clothes[Clothing_type].covered_by[focused_Character.Clothes[covering_Clothing_type].string]:
                                        focused_Character.Clothes[Clothing_type].soiled = False
                                        focused_Character.Clothes[covering_Clothing_type].soiled = True
    elif cumshot_location == "cumshot_feet":
        $ focused_Character.spunk["feet"] = 1

        pause 0.5

        $ focused_Character.spunk["feet"] = 2

        python:
            for Clothing_type in all_Clothing_types:
                if focused_Character.Clothes[Clothing_type].string:
                    if "feet" in focused_Character.Clothes[Clothing_type].covers[focused_Character.position].keys() and focused_Character.Clothes[Clothing_type].state in focused_Character.Clothes[Clothing_type].covers[focused_Character.position]["feet"]:
                        focused_Character.Clothes[Clothing_type].soiled = True
                        
                        for covering_Clothing_type in all_Clothing_types:
                            if focused_Character.Clothes[covering_Clothing_type].string:
                                if "feet" in focused_Character.Clothes[covering_Clothing_type].covers[focused_Character.position].keys() and focused_Character.Clothes[covering_Clothing_type].state in focused_Character.Clothes[covering_Clothing_type].covers[focused_Character.position]["feet"]:
                                    if focused_Character.Clothes[covering_Clothing_type].string in focused_Character.Clothes[Clothing_type].covered_by.keys() and focused_Character.Clothes[covering_Clothing_type].state in focused_Character.Clothes[Clothing_type].covered_by[focused_Character.Clothes[covering_Clothing_type].string]:
                                        focused_Character.Clothes[Clothing_type].soiled = False
                                        focused_Character.Clothes[covering_Clothing_type].soiled = True
    elif cumshot_location == "creampie":
        $ focused_Character.creampie["pussy"] = 1

        pause 0.5

        $ focused_Character.creampie["pussy"] = 2
    elif cumshot_location == "cum_in_mouth":
        $ focused_Character.spunk["mouth"] = 1

        pause 0.5

        $ focused_Character.spunk["mouth"] = 2
    elif cumshot_location == "anal_creampie":
        $ focused_Character.creampie["anus"] = 1

        pause 0.5

        $ focused_Character.creampie["anus"] = 2

    $ focused_Character.persistent_spunk = copy.copy(focused_Character.spunk)

    call Player_cumshot_narrations(focused_Character, location = cumshot_location) from _call_Player_cumshot_narrations

    $ Player.History.update("orgasmed")

    $ Player.orgasming = None

    $ Player.desire = 0

    $ Player.stamina -= 1 if Player.stamina > 0 else 0

    if Player.stamina:
        $ Player.cock_Actions[0].mode = 0
    else:
        $ stop_Actions(Player, organ = "cock")
        
        "Looks like you're running on empty - maybe give yourself a break."

    $ speed = 1.0
    $ intensity = 1.0

    $ has_progression_control = True
    $ has_Action_control = True
    $ has_position_control = True
    $ has_movement_control = True
    $ has_ejaculation_control = True

    return

label ask_Character_for_cumshot(Character, orgasm_type):
    if approval_check(Character, threshold = orgasm_type):
        if not Character.History.check(orgasm_type):
            call expression f"{Character.tag}_accepts_{orgasm_type}_first_time" from _call_expression_40
        elif Character.History.check(orgasm_type) == 1:
            call expression f"{Character.tag}_accepts_{orgasm_type}_second_time" from _call_expression_41
        elif approval_check(Character, threshold = "love"):
            call expression f"{Character.tag}_accepts_{orgasm_type}_love" from _call_expression_42
        else:
            call expression f"{Character.tag}_accepts_{orgasm_type}" from _call_expression_43

        return orgasm_type
    else:
        if Character.History.check(f"rejected_{orgasm_type}", tracker = "recent") >= 2:
            call change_Character_stat(Character, "love", -5) from _call_change_Character_stat_804
            call change_Character_stat(Character, "trust", -5) from _call_change_Character_stat_805

            call expression f"{Character.tag}_rejects_Action_asked_twice" from _call_expression_44
        elif Character.History.check(f"rejected_{orgasm_type}", tracker = "recent") == 1:
            call change_Character_stat(Character, "love", -2) from _call_change_Character_stat_806

            call expression f"{Character.tag}_rejects_Action_asked_once" from _call_expression_45
        else:
            call expression f"{Character.tag}_rejects_{orgasm_type}" from _call_expression_46

        $ Character.History.update(f"rejected_{orgasm_type}")

        return False

    return False

label ask_Character_for_clean_up(Character, clean_up_type):
    if approval_check(Character, threshold = clean_up_type):
        if not Character.History.check(clean_up_type):
            call expression f"{Character.tag}_accepts_{clean_up_type}_first_time" from _call_expression_47
        elif Character.History.check(clean_up_type) == 1:
            call expression f"{Character.tag}_accepts_{clean_up_type}_second_time" from _call_expression_48
        elif approval_check(Character, threshold = "love"):
            call expression f"{Character.tag}_accepts_{clean_up_type}_love" from _call_expression_49
        else:
            call expression f"{Character.tag}_accepts_{clean_up_type}" from _call_expression_50

        return True
    else:
        if Character.History.check(f"rejected_{clean_up_type}", tracker = "recent") >= 2:
            call change_Character_stat(Character, "love", -5) from _call_change_Character_stat_807
            call change_Character_stat(Character, "trust", -5) from _call_change_Character_stat_808

            call expression f"{Character.tag}_rejects_Action_asked_twice" from _call_expression_51
        elif Character.History.check(f"rejected_{clean_up_type}", tracker = "recent") == 1:
            call change_Character_stat(Character, "love", -2) from _call_change_Character_stat_809
            
            call expression f"{Character.tag}_rejects_Action_asked_once" from _call_expression_52
        else:
            call expression f"{Character.tag}_rejects_{clean_up_type}" from _call_expression_53

        $ Character.History.update(f"rejected_{clean_up_type}")

        return False

    return False

label clean_cum_mess(Character):
    $ Character_picker_disabled = True
    $ belt_disabled = True

    $ Character.change_face("sexy", blush = 1)

    if approval_check(Character, threshold = "clean_cum"):
        $ choice_disabled = False

        $ clean_up_choice = None

        menu:
            "What should [Character.name] do with your cum?"
            "Let her decide":
                $ clean_up_choice = Character
            "Ask her to clean it off":
                $ clean_up_choice = "clean_cum"
            "Ask her to swallow it":
                $ clean_up_choice = "swallow_cum"
            "Ask her to wear it":
                $ clean_up_choice = "wear_cum"

        $ choice_disabled = True
                
        if clean_up_choice not in all_Companions:
            call ask_Character_for_clean_up(Character, clean_up_choice) from _call_ask_Character_for_clean_up

        if clean_up_choice in all_Companions or not _return:
            call expression f"{Character.tag}_decides_clean_cum" from _call_expression_54

            $ clean_up_choice = _return
    else:
        call expression f"{Character.tag}_decides_clean_cum" from _call_expression_55

        $ clean_up_choice = _return

    if clean_up_choice == "clean_cum":
        call clean_cum(Character) from _call_clean_cum
    elif clean_up_choice == "swallow_cum":
        call swallow_cum(Character) from _call_swallow_cum_12

    if clean_up_choice not in all_Companions:
        $ Character.History.update(clean_up_choice)

    $ Character_picker_disabled = False
    $ belt_disabled = False

    return

label clean_cum(Character):
    $ Character.change_arms("neutral", right_arm = "extended")

    pause 0.5

    python:
        for location in Character.spunk.keys():
            if Character.spunk[location] == 2:
                Character.spunk["hand"] = 1
                Character.spunk[location] = 1
                Character.persistent_spunk[location] = 1

                renpy.pause(0.1)

            Character.spunk[location] = 0
            Character.persistent_spunk[location] = 0

    pause 0.1

    $ Character.spunk["hand"] = 2

    pause 2.0

    $ Character.spunk["hand"] = 0

    $ Character.change_arms("neutral")

    return

label swallow_cum(Character):
    $ Character.change_arms("neutral", right_arm = "extended")

    pause 0.5

    python:
        for location in Character.spunk.keys():
            if Character.spunk[location] == 2:
                Character.spunk["hand"] = 1
                Character.spunk[location] = 1
                Character.persistent_spunk[location] = 1

                renpy.pause(0.1)

            Character.spunk[location] = 0
            Character.persistent_spunk[location] = 0

    pause 0.1

    $ Character.spunk["hand"] = 2

    pause 0.5

    $ Character.mouth = "tongue"

    pause 0.5

    $ Character.spunk["mouth"] = 1
    $ Character.spunk["hand"] = 1

    pause 0.1

    $ Character.spunk["mouth"] = 2
    $ Character.spunk["hand"] = 0

    pause 2.0

    $ Character.brows = "raised"
    $ Character.eyes = "closed"
    $ Character.mouth = "neutral"

    pause 1.0

    $ Character.change_face("sexy")
    $ Character.change_arms("neutral")

    return