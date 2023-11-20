init python:

    import copy
    import math

    def saturating_exponential(x, limit):
        
        return limit*(1 - math.exp(-2*x/limit))

    def increase_Character_desire(Character, update, limit = 130):
        new = int(saturating_exponential(Character.desire + update, limit))

        if new > Character.desire:
            Character.desire = new

        return

label Character_orgasms(Character):
    $ has_progression_control = False
    $ has_Action_control = False
    $ has_position_control = False
    $ has_movement_control = False

    $ Character.orgasming = True

    call Character_orgasm_narrations(Character) from _call_Character_orgasm_narrations

    $ Character.orgasming = False

    $ Character.desire = 0

    $ Character.stamina -= 1 if Character.stamina > 0 else 0

    $ Character.status["horny"] = False

    $ has_progression_control = True
    $ has_Action_control = True
    $ has_position_control = True
    $ has_movement_control = True
    $ has_ejaculation_control = True

    if Character.stamina == 0 and Player.desire < 75:
        "Looks like [Character.name] is wiped out. You should take a break."

        $ speed = 0.001
        $ intensity = 0.001

        $ has_Action_control = False
        $ has_position_control = False
        $ has_movement_control = False
        $ has_ejaculation_control = False

    return

label Player_orgasms:
    $ has_progression_control = False
    $ has_Action_control = False
    $ has_position_control = False
    $ has_movement_control = False

    $ choice_disabled = False

    if focused_Girl in [Laura, Jean] and focused_Girl.quirk and not Player.History.check("orgasmed", tracker = "daily"):
        $ climax_choice = focused_Girl
    else:
        if has_ejaculation_control:
            call expression f"{focused_Girl.tag}_lets_Player_decide_cumshot" from _call_expression_130
            
            $ climax_choice = None

            $ _return = False

            while not _return:
                menu:
                    "Where do you want to cum?"
                    "Let [focused_Girl.name] decide":
                        $ climax_choice = focused_Girl
                    "On the floor":
                        $ climax_choice = "floor"
                    "Her belly" if "missionary" in focused_Girl.possible_poses:
                        $ climax_choice = "cumshot_belly"
                    "Her breasts" if "missionary" in focused_Girl.possible_poses:
                        $ climax_choice = "cumshot_breasts"
                    "Her face" if "hands_and_knees" in focused_Girl.possible_poses:
                        $ climax_choice = "cumshot_face"
                    "Her hair" if "hands_and_knees" in focused_Girl.possible_poses:
                        $ climax_choice = "cumshot_hair"
                    "Her back" if "doggy" in focused_Girl.possible_poses:
                        $ climax_choice = "cumshot_back"
                    "Her ass" if "doggy" in focused_Girl.possible_poses:
                        $ climax_choice = "cumshot_ass"
                    # "Her feet":
                    #     $ climax_choice = "cumshot_feet"
                    "Inside her" if focused_Girl.History.check("sex"):
                        $ climax_choice = "creampie"
                    "In her mouth" if focused_Girl.History.check("blowjob") or focused_Girl.History.check("deepthroat"):
                        $ climax_choice = "cum_in_mouth"
                    "Down her throat" if focused_Girl.History.check("deepthroat"):
                        $ climax_choice = "cum_down_throat"
                    "In her ass" if focused_Girl.History.check("anal"):
                        $ climax_choice = "anal_creampie"
                    "Delay" if Player.orgasm_control or (focused_Girl.History.check("made_Player_orgasm") >= 5 and Player.History.check("delayed_orgasm", tracker = "recent") < 3):
                        if not Player.History.check("delayed_orgasm", tracker = "recent"):
                            $ Player.desire -= 50
                        elif Player.History.check("delayed_orgasm", tracker = "recent") == 1:
                            $ Player.desire -= 25
                        elif Player.History.check("delayed_orgasm", tracker = "recent") == 2:
                            $ Player.desire -= 10

                        $ Player.History.update("delayed_orgasm")
                        
                        $ has_progression_control = True
                        $ has_Action_control = True
                        $ has_position_control = True
                        $ has_movement_control = True
                        $ has_ejaculation_control = True

                        $ choice_disabled = True
                        
                        return

                if climax_choice not in all_Girls and climax_choice != "floor":
                    call ask_Girl_for_cumshot(focused_Girl, climax_choice) from _call_ask_Girl_for_cumshot
                else:
                    $ _return = "floor"

    $ choice_disabled = True

    if not has_ejaculation_control or climax_choice in all_Girls:
        call expression f"{focused_Girl.tag}_decides_cumshot" from _call_expression_39

    if _return:
        $ cumshot_location = _return
    else:
        $ cumshot_location = "floor"

    $ focused_Girl.History.update("made_Player_orgasm")
    $ focused_Girl.History.update(cumshot_location)

    if cumshot_location == "cumshot_belly" and focused_Girl.position != "missionary":
        call request_position(focused_Girl, "missionary") from _call_request_position
    elif cumshot_location == "cumshot_breasts" and focused_Girl.position != "missionary":
        call request_position(focused_Girl, "missionary") from _call_request_position_1
    elif cumshot_location == "cumshot_face" and focused_Girl.position != "hands_and_knees":
        call request_position(focused_Girl, "hands_and_knees") from _call_request_position_2
    elif cumshot_location == "cumshot_hair" and focused_Girl.position != "hands_and_knees":
        call request_position(focused_Girl, "hands_and_knees") from _call_request_position_3
    elif cumshot_location == "cumshot_back" and focused_Girl.position != "doggy":
        call request_position(focused_Girl, "doggy") from _call_request_position_4
    elif cumshot_location == "cumshot_ass" and focused_Girl.position != "doggy":
        call request_position(focused_Girl, "doggy") from _call_request_position_5
    # elif cumshot_location == "cumshot_feet":
    #     call request_position(focused_Girl, "footjob")
    elif cumshot_location == "creampie" and focused_Girl.position not in ["missionary", "doggy"]:
        call request_position(focused_Girl, "missionary") from _call_request_position_6

        if _return:
            call expose(focused_Girl, "pussy") from _call_expose_18

            $ _return = True
    elif cumshot_location == "cum_in_mouth" and focused_Girl.position != "hands_and_knees":
        call request_position(focused_Girl, "hands_and_knees") from _call_request_position_7
    elif cumshot_location == "cum_down_throat" and focused_Girl.position != "hands_and_knees":
        call request_position(focused_Girl, "hands_and_knees") from _call_request_position_17
    elif cumshot_location == "anal_creampie":
        if focused_Girl.position not in ["missionary", "doggy"] and "doggy" in focused_Girl.available_poses:
            call request_position(focused_Girl, "doggy") from _call_request_position_8
        else:
            call request_position(focused_Girl, "missionary") from _call_request_position_9

        if _return:
            call expose(focused_Girl, "anus") from _call_expose_19

            $ _return = True

    if not _return:
        $ cumshot_location = "floor"

    if cumshot_location in ["floor"] or "cumshot" in cumshot_location:
        $ Player.orgasming = "cumshot"
    else:
        $ Player.orgasming = cumshot_location

    call Player_orgasm_narrations(focused_Girl, location = cumshot_location) from _call_Player_orgasm_narrations

    if cumshot_location == "cumshot_belly":
        $ focused_Girl.spunk["belly"] = True

        python:
            for Clothing_type in all_Clothing_types:
                if focused_Girl.Clothes[Clothing_type].string:
                    if "belly" in focused_Girl.Clothes[Clothing_type].covers[focused_Girl.position].keys() and focused_Girl.Clothes[Clothing_type].state in focused_Girl.Clothes[Clothing_type].covers[focused_Girl.position]["belly"]:
                        focused_Girl.Clothes[Clothing_type].soiled = True
                        
                        for covering_Clothing_type in all_Clothing_types:
                            if focused_Girl.Clothes[covering_Clothing_type].string:
                                if "belly" in focused_Girl.Clothes[covering_Clothing_type].covers[focused_Girl.position].keys() and focused_Girl.Clothes[covering_Clothing_type].state in focused_Girl.Clothes[covering_Clothing_type].covers[focused_Girl.position]["belly"]:
                                    if focused_Girl.Clothes[covering_Clothing_type].string in focused_Girl.Clothes[Clothing_type].covered_by.keys() and focused_Girl.Clothes[covering_Clothing_type].state in focused_Girl.Clothes[Clothing_type].covered_by[focused_Girl.Clothes[covering_Clothing_type].string]:
                                        focused_Girl.Clothes[Clothing_type].soiled = False
                                        focused_Girl.Clothes[covering_Clothing_type].soiled = True
    elif cumshot_location == "cumshot_breasts":
        $ focused_Girl.spunk["breasts"] = True

        python:
            for Clothing_type in all_Clothing_types:
                if focused_Girl.Clothes[Clothing_type].string:
                    if "breasts" in focused_Girl.Clothes[Clothing_type].covers[focused_Girl.position].keys() and focused_Girl.Clothes[Clothing_type].state in focused_Girl.Clothes[Clothing_type].covers[focused_Girl.position]["breasts"]:
                        focused_Girl.Clothes[Clothing_type].soiled = True
                        
                        for covering_Clothing_type in all_Clothing_types:
                            if focused_Girl.Clothes[covering_Clothing_type].string:
                                if "breasts" in focused_Girl.Clothes[covering_Clothing_type].covers[focused_Girl.position].keys() and focused_Girl.Clothes[covering_Clothing_type].state in focused_Girl.Clothes[covering_Clothing_type].covers[focused_Girl.position]["breasts"]:
                                    if focused_Girl.Clothes[covering_Clothing_type].string in focused_Girl.Clothes[Clothing_type].covered_by.keys() and focused_Girl.Clothes[covering_Clothing_type].state in focused_Girl.Clothes[Clothing_type].covered_by[focused_Girl.Clothes[covering_Clothing_type].string]:
                                        focused_Girl.Clothes[Clothing_type].soiled = False
                                        focused_Girl.Clothes[covering_Clothing_type].soiled = True
    elif cumshot_location == "cumshot_face":
        if focused_Girl.spunk["chin"]:
            $ focused_Girl.spunk["hair"] = True

        if focused_Girl.spunk["face"]:
            $ focused_Girl.spunk["chin"] = True

        $ focused_Girl.spunk["face"] = True
    elif cumshot_location == "cumshot_hair":
        $ focused_Girl.spunk["hair"] = True
    elif cumshot_location == "cumshot_back":
        $ focused_Girl.spunk["back"] = True

        python:
            for Clothing_type in all_Clothing_types:
                if focused_Girl.Clothes[Clothing_type].string:
                    if "back" in focused_Girl.Clothes[Clothing_type].covers[focused_Girl.position].keys() and focused_Girl.Clothes[Clothing_type].state in focused_Girl.Clothes[Clothing_type].covers[focused_Girl.position]["back"]:
                        focused_Girl.Clothes[Clothing_type].soiled = True
                        
                        for covering_Clothing_type in all_Clothing_types:
                            if focused_Girl.Clothes[covering_Clothing_type].string:
                                if "back" in focused_Girl.Clothes[covering_Clothing_type].covers[focused_Girl.position].keys() and focused_Girl.Clothes[covering_Clothing_type].state in focused_Girl.Clothes[covering_Clothing_type].covers[focused_Girl.position]["back"]:
                                    if focused_Girl.Clothes[covering_Clothing_type].string in focused_Girl.Clothes[Clothing_type].covered_by.keys() and focused_Girl.Clothes[covering_Clothing_type].state in focused_Girl.Clothes[Clothing_type].covered_by[focused_Girl.Clothes[covering_Clothing_type].string]:
                                        focused_Girl.Clothes[Clothing_type].soiled = False
                                        focused_Girl.Clothes[covering_Clothing_type].soiled = True
    elif cumshot_location == "cumshot_ass":
        $ focused_Girl.spunk["ass"] = True

        python:
            for Clothing_type in all_Clothing_types:
                if focused_Girl.Clothes[Clothing_type].string:
                    if "ass" in focused_Girl.Clothes[Clothing_type].covers[focused_Girl.position].keys() and focused_Girl.Clothes[Clothing_type].state in focused_Girl.Clothes[Clothing_type].covers[focused_Girl.position]["ass"]:
                        focused_Girl.Clothes[Clothing_type].soiled = True
                        
                        for covering_Clothing_type in all_Clothing_types:
                            if focused_Girl.Clothes[covering_Clothing_type].string:
                                if "ass" in focused_Girl.Clothes[covering_Clothing_type].covers[focused_Girl.position].keys() and focused_Girl.Clothes[covering_Clothing_type].state in focused_Girl.Clothes[covering_Clothing_type].covers[focused_Girl.position]["ass"]:
                                    if focused_Girl.Clothes[covering_Clothing_type].string in focused_Girl.Clothes[Clothing_type].covered_by.keys() and focused_Girl.Clothes[covering_Clothing_type].state in focused_Girl.Clothes[Clothing_type].covered_by[focused_Girl.Clothes[covering_Clothing_type].string]:
                                        focused_Girl.Clothes[Clothing_type].soiled = False
                                        focused_Girl.Clothes[covering_Clothing_type].soiled = True
    elif cumshot_location == "cumshot_feet":
        $ focused_Girl.spunk["feet"] = True

        python:
            for Clothing_type in all_Clothing_types:
                if focused_Girl.Clothes[Clothing_type].string:
                    if "feet" in focused_Girl.Clothes[Clothing_type].covers[focused_Girl.position].keys() and focused_Girl.Clothes[Clothing_type].state in focused_Girl.Clothes[Clothing_type].covers[focused_Girl.position]["feet"]:
                        focused_Girl.Clothes[Clothing_type].soiled = True
                        
                        for covering_Clothing_type in all_Clothing_types:
                            if focused_Girl.Clothes[covering_Clothing_type].string:
                                if "feet" in focused_Girl.Clothes[covering_Clothing_type].covers[focused_Girl.position].keys() and focused_Girl.Clothes[covering_Clothing_type].state in focused_Girl.Clothes[covering_Clothing_type].covers[focused_Girl.position]["feet"]:
                                    if focused_Girl.Clothes[covering_Clothing_type].string in focused_Girl.Clothes[Clothing_type].covered_by.keys() and focused_Girl.Clothes[covering_Clothing_type].state in focused_Girl.Clothes[Clothing_type].covered_by[focused_Girl.Clothes[covering_Clothing_type].string]:
                                        focused_Girl.Clothes[Clothing_type].soiled = False
                                        focused_Girl.Clothes[covering_Clothing_type].soiled = True
    elif cumshot_location == "creampie":
        $ focused_Girl.creampie["pussy"] = True
    elif cumshot_location == "cum_in_mouth":
        $ focused_Girl.spunk["mouth"] = True
    elif cumshot_location == "anal_creampie":
        $ focused_Girl.creampie["anus"] = True

    $ focused_Girl.persistent_spunk = copy.copy(focused_Girl.spunk)

    call Player_cumshot_narrations(focused_Girl, location = cumshot_location) from _call_Player_cumshot_narrations

    $ Player.History.update("orgasmed")

    $ Player.orgasming = None

    $ speed = 0.05
    $ intensity = 0.05

    $ Player.desire = 0

    $ Player.stamina -= 1 if Player.stamina > 0 else 0

    $ has_progression_control = True
    $ has_Action_control = True
    $ has_position_control = True
    $ has_movement_control = True
    $ has_ejaculation_control = True

    if Player.stamina == 0:
        "You are completely empty. You should take a break."

        $ speed = 0.001
        $ intensity = 0.001

        $ has_progression_control = True
        $ has_Action_control = False
        $ has_position_control = False
        $ has_movement_control = False
        $ has_ejaculation_control = False

    return

label ask_Girl_for_cumshot(Girl, orgasm_type):
    if approval_check(Girl, threshold = orgasm_type):
        if not Girl.History.check(orgasm_type):
            call expression f"{Girl.tag}_accepts_{orgasm_type}_first_time" from _call_expression_40
        elif Girl.History.check(orgasm_type) == 1:
            call expression f"{Girl.tag}_accepts_{orgasm_type}_second_time" from _call_expression_41
        elif approval_check(Girl, threshold = "love"):
            call expression f"{Girl.tag}_accepts_{orgasm_type}_love" from _call_expression_42
        else:
            call expression f"{Girl.tag}_accepts_{orgasm_type}" from _call_expression_43

        return orgasm_type
    else:
        if Girl.History.check(f"rejected_{orgasm_type}", tracker = "recent") >= 2:
            call change_Girl_stat(Girl, "love", -5) from _call_change_Girl_stat_804
            call change_Girl_stat(Girl, "trust", -5) from _call_change_Girl_stat_805

            call expression f"{Girl.tag}_rejects_Action_asked_twice" from _call_expression_44
        elif Girl.History.check(f"rejected_{orgasm_type}", tracker = "recent") == 1:
            call change_Girl_stat(Girl, "love", -2) from _call_change_Girl_stat_806

            call expression f"{Girl.tag}_rejects_Action_asked_once" from _call_expression_45
        else:
            call expression f"{Girl.tag}_rejects_{orgasm_type}" from _call_expression_46

        $ Girl.History.update(f"rejected_{orgasm_type}")

        return False

    return False

label ask_Girl_for_clean_up(Girl, clean_up_type):
    if approval_check(Girl, threshold = clean_up_type):
        if not Girl.History.check(clean_up_type):
            call expression f"{Girl.tag}_accepts_{clean_up_type}_first_time" from _call_expression_47
        elif Girl.History.check(clean_up_type) == 1:
            call expression f"{Girl.tag}_accepts_{clean_up_type}_second_time" from _call_expression_48
        elif approval_check(Girl, threshold = "love"):
            call expression f"{Girl.tag}_accepts_{clean_up_type}_love" from _call_expression_49
        else:
            call expression f"{Girl.tag}_accepts_{clean_up_type}" from _call_expression_50

        return True
    else:
        if Girl.History.check(f"rejected_{clean_up_type}", tracker = "recent") >= 2:
            call change_Girl_stat(Girl, "love", -5) from _call_change_Girl_stat_807
            call change_Girl_stat(Girl, "trust", -5) from _call_change_Girl_stat_808

            call expression f"{Girl.tag}_rejects_Action_asked_twice" from _call_expression_51
        elif Girl.History.check(f"rejected_{clean_up_type}", tracker = "recent") == 1:
            call change_Girl_stat(Girl, "love", -2) from _call_change_Girl_stat_809
            
            call expression f"{Girl.tag}_rejects_Action_asked_once" from _call_expression_52
        else:
            call expression f"{Girl.tag}_rejects_{clean_up_type}" from _call_expression_53

        $ Girl.History.update(f"rejected_{clean_up_type}")

        return False

    return False

label clean_cum_mess(Girl):
    $ Character_picker_disabled = True
    $ belt_disabled = True

    $ Girl.change_face("sexy", blush = 1)

    if approval_check(Girl, threshold = "clean_cum"):
        $ choice_disabled = False

        $ clean_up_choice = None

        menu:
            "What should [Girl.name] do with your cum?"
            "Let her decide":
                $ clean_up_choice = Girl
            "Ask her to clean it off":
                $ clean_up_choice = "clean_cum"
            "Ask her to swallow it":
                $ clean_up_choice = "swallow_cum"
            "Ask her to wear it":
                $ clean_up_choice = "wear_cum"

        $ choice_disabled = True
                
        if clean_up_choice not in all_Girls:
            call ask_Girl_for_clean_up(Girl, clean_up_choice) from _call_ask_Girl_for_clean_up

        if clean_up_choice in all_Girls or not _return:
            call expression f"{Girl.tag}_decides_clean_cum" from _call_expression_54

            $ clean_up_choice = _return
    else:
        call expression f"{Girl.tag}_decides_clean_cum" from _call_expression_55

        $ clean_up_choice = _return

    if clean_up_choice == "clean_cum":
        call clean_cum(Girl) from _call_clean_cum
    elif clean_up_choice == "swallow_cum":
        call swallow_cum(Girl) from _call_swallow_cum_12

    if clean_up_choice not in all_Characters:
        $ Girl.History.update(clean_up_choice)

    $ Character_picker_disabled = False
    $ belt_disabled = False

    return

label clean_cum(Girl):
    # if Girl in [Laura]:
    #     $ Girl.left_arm_pose = 2

    # if Girl in [Rogue, Jean, Ororo]:
    #     $ Girl.right_arm_pose = 2

    pause 0.5

    python:
        for location in Girl.spunk.keys():
            Girl.spunk[location] = False
            Girl.persistent_spunk[location] = False

    $ Girl.spunk["hand"] = True

    pause 2.0

    $ Girl.spunk["hand"] = False

    # if Girl in [Laura]:
    #     $ Girl.left_arm_pose = 1

    # if Girl in [Rogue, Jean, Ororo]:
    #     $ Girl.right_arm_pose = 1

    return

label swallow_cum(Girl):
    # if Girl in [Laura]:
    #     $ Girl.left_arm_pose = 2

    # if Girl in [Rogue, Jean, Ororo]:
    #     $ Girl.right_arm_pose = 2

    pause 0.5

    python:
        for location in Girl.spunk.keys():
            Girl.spunk[location] = False
            Girl.persistent_spunk[location] = False

    $ Girl.spunk["hand"] = True

    pause 0.5

    $ Girl.mouth = "tongue"

    pause 0.5

    $ Girl.spunk["mouth"] = True
    $ Girl.spunk["hand"] = False

    pause 2.0

    $ Girl.brows = "raised"
    $ Girl.eyes = "closed"
    $ Girl.mouth = "neutral"

    pause 1.0

    $ Girl.change_face("sexy")

    # if Girl in [Laura]:
    #     $ Girl.left_arm_pose = 1

    # if Girl in [Rogue, Jean, Ororo]:
    #     $ Girl.right_arm_pose = 1

    return