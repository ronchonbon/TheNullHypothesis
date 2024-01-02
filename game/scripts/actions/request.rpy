label request_hookup(Character):
    $ Character_picker_disabled = True

    $ Present = get_Present()[0]

    $ NPCs_present = False
    
    python:
        for C in Present:
            if C in all_NPCs:
                NPCs_present = C

                break

    if NPCs_present:
        "Maybe not in front of [C.name]. . ."

        return

    ch_Player "Do you want to mess around?"

    if Character.status["miffed"] or Character.status["mad"]:
        if Character.History.check("rejected_hookup", tracker = "recent") >= 2:
            call change_Character_stat(Character, "love", -5) from _call_change_Character_stat_810
            call change_Character_stat(Character, "trust", -5) from _call_change_Character_stat_811

            call expression f"{Character.tag}_rejects_Action_asked_twice" from _call_expression_56
        elif Character.History.check("rejected_hookup", tracker = "recent") == 1:
            call change_Character_stat(Character, "love", -2) from _call_change_Character_stat_812

            call expression f"{Character.tag}_rejects_Action_asked_once" from _call_expression_57
        else:
            call expression f"{Character.tag}_rejects_hookup_mad" from _call_expression_58

        $ Character.History.update("rejected_hookup")

        if Character.location == Player.location:
            show screen interactions_screen(Character)

        return
    elif Player.location not in bedrooms:
        if Character.History.check("rejected_hookup", tracker = "recent") >= 2:
            call change_Character_stat(Character, "love", -5) from _call_change_Character_stat_813
            call change_Character_stat(Character, "trust", -5) from _call_change_Character_stat_814

            call expression f"{Character.tag}_rejects_Action_asked_twice" from _call_expression_59
        elif Character.History.check("rejected_hookup", tracker = "recent") == 1:
            call change_Character_stat(Character, "love", -2) from _call_change_Character_stat_815
            
            call expression f"{Character.tag}_rejects_Action_asked_once" from _call_expression_60
        else:
            call expression f"{Character.tag}_rejects_hookup_public" from _call_expression_61

        $ Character.History.update(f"rejected_hookup")

        if Character.location == Player.location:
            show screen interactions_screen(Character)

        return
    elif len(Present) > 1:
        if Character.History.check("rejected_hookup", tracker = "recent") >= 2:
            call change_Character_stat(Character, "love", -5) from _call_change_Character_stat_816
            call change_Character_stat(Character, "trust", -5) from _call_change_Character_stat_817

            call expression f"{Character.tag}_rejects_Action_asked_twice" from _call_expression_62
        elif Character.History.check("rejected_hookup", tracker = "recent") == 1:
            call change_Character_stat(Character, "love", -2) from _call_change_Character_stat_818

            call expression f"{Character.tag}_rejects_Action_asked_once" from _call_expression_63
        else:
            call expression f"{Character.tag}_rejects_hookup_public" from _call_expression_64

        $ Character.History.update("rejected_hookup")

        if Character.location == Player.location:
            show screen interactions_screen(Character)

        return

    $ renpy.dynamic(temp_Characters = Present[:])

    while temp_Characters:
        if approval_check(temp_Characters[0], threshold = "hookup") and Player.stamina and temp_Characters[0].stamina:
            if not temp_Characters[0].History.check("hookup"):
                call expression f"{temp_Characters[0].tag}_accepts_hookup_first_time" from _call_expression_65
            elif temp_Characters[0].History.check("hookup") == 1:
                call expression f"{temp_Characters[0].tag}_accepts_hookup_second_time" from _call_expression_66
            elif approval_check(temp_Characters[0], threshold = "love"):
                call expression f"{temp_Characters[0].tag}_accepts_hookup_love" from _call_expression_67
            else:
                call expression f"{temp_Characters[0].tag}_accepts_hookup" from _call_expression_68

            if temp_Characters[0].History.check("hookup") >= 3 and not temp_Characters[0].History.check("hookup", tracker = "recent"):
                if temp_Characters[0].History.check("hookup", tracker = "weekly"):
                    $ total_score = 0.0

                    python:
                        for d in Player.scores["sex"][temp_Characters[0]].keys():
                            if d > day - 6:
                                total_score += Player.scores["sex"][temp_Characters[0]][d]

                    $ average_score = total_score/temp_Characters[0].History.check("hookup", tracker = "weekly")
                else:
                    $ average_score = -1.0

                call expression f"{temp_Characters[0].tag}_weekly_summary" pass(average_score = average_score) from _call_expression_78
        else:
            if temp_Characters[0].History.check("rejected_hookup", tracker = "recent") >= 2:
                call change_Character_stat(temp_Characters[0], "love", -5) from _call_change_Character_stat_819
                call change_Character_stat(temp_Characters[0], "trust", -5) from _call_change_Character_stat_820

                call expression f"{temp_Characters[0].tag}_rejects_Action_asked_twice" from _call_expression_69
            elif temp_Characters[0].History.check("rejected_hookup", tracker = "recent") == 1:
                call change_Character_stat(temp_Characters[0], "love", -2) from _call_change_Character_stat_821

                call expression f"{temp_Characters[0].tag}_rejects_Action_asked_once" from _call_expression_70
            elif not Player.stamina and not temp_Characters[0].stamina:
                call expression f"{temp_Characters[0].tag}_rejects_hookup_later" from _call_expression_79
            else:
                call expression f"{temp_Characters[0].tag}_rejects_hookup" from _call_expression_71

            $ temp_Characters[0].History.update("rejected_hookup")

            if Character.location == Player.location:
                show screen interactions_screen(Character)

            return

        $ temp_Characters.remove(temp_Characters[0])

    python:
        for C in Present:
            C.History.update("hookup")

            hookup_length = 0

    $ Character_picker_disabled = False

    show screen Action_screen()

    return

label request_Action(Action_type, Actors, Targets):
    if Action_type in cock_Action_types and not Player.stamina:
        "Looks like you're running on empty - maybe give yourself a break."

        return

    $ temp_speed = speed
    $ temp_intensity = intensity

    $ speed = 0.001
    $ intensity = 0.001

    if Actors in all_Companions or Actors == Player:
        $ Actors = [Actors]

    if Targets in all_Companions or Targets == Player:
        $ Targets = [Targets]

    $ Action = ActionClass(Action_type, Actors, Targets)

    if focused_Character.History.check(Action_type, tracker = "recent"):
        if focused_Character.History.check(Action_type) >= 10:
            $ Player.voice(Action.lines[2].replace(".", " again.").replace("?", " again?"))
        elif focused_Character.History.check(Action_type) >= 3:
            $ Player.voice(Action.lines[1].replace(".", " again.").replace("?", " again?"))
        else:
            $ Player.voice(Action.lines[0].replace(".", " again.").replace("?", " again?"))
    else:
        if focused_Character.History.check(Action_type) >= 10:
            $ Player.voice(Action.lines[2])
        elif focused_Character.History.check(Action_type) >= 3:
            $ Player.voice(Action.lines[1])
        else:
            $ Player.voice(Action.lines[0])

    if approval_check(focused_Character, threshold = Action_type):
        if not focused_Character.History.check(Action_type, tracker = "recent"):
            if not focused_Character.History.check(Action_type):
                call expression f"{focused_Character.tag}_accepts_{Action_type}_first_time" from _call_expression_72
            # elif focused_Character.History.check(Action_type) == 1:
            #     call expression f"{focused_Character.tag}_accepts_{Action_type}_second_time"
            # elif approval_check(focused_Character, threshold = "love"):
            #     call expression f"{focused_Character.tag}_accepts_{Action_type}_love"

                $ focused_Character.unlocked_Actions.append(Action_type)
            else:
                call expression f"{focused_Character.tag}_accepts_{Action_type}" from _call_expression_73
        else:
            call expression f"{focused_Character.tag}_accepts_Action_again" from _call_expression_74

        call check_double_penetration(focused_Character, Action_type) from _call_check_double_penetration

        if _return:
            call start_Action(Action) from _call_start_Action_4

            $ hookup_length += 0.25
        else:
            $ focused_Character.History.update(f"rejected_double_penetrate")
    else:
        if focused_Character.History.check(f"rejected_{Action_type}", tracker = "recent") >= 2:
            call change_Character_stat(focused_Character, "love", -5) from _call_change_Character_stat_822
            call change_Character_stat(focused_Character, "trust", -5) from _call_change_Character_stat_823

            call expression f"{focused_Character.tag}_rejects_Action_asked_twice" from _call_expression_75
        elif focused_Character.History.check(f"rejected_{Action_type}", tracker = "recent") == 1:
            call change_Character_stat(focused_Character, "love", -2) from _call_change_Character_stat_824

            call expression f"{focused_Character.tag}_rejects_Action_asked_once" from _call_expression_76
        else:
            call expression f"{focused_Character.tag}_rejects_{Action_type}" from _call_expression_77

        $ focused_Character.History.update(f"rejected_{Action_type}")

    $ speed = temp_speed
    $ intensity = temp_intensity

    call continue_Actions from _call_continue_Actions

    return

label request_mode(Action, mode):
    $ temp_speed = speed
    $ temp_intensity = intensity

    $ speed = 0.001
    $ intensity = 0.001

    $ Action.mode = mode

    if not ongoing_Event or has_Action_control:
        call expression f"{Action.Action_type}_initiations" pass (Action = Action) from _call_expression_131

    $ speed = temp_speed
    $ intensity = temp_intensity

    return

label request_position(Character, new_position, Action = None, automatic = False):
    if not automatic:
        if not Character.History.check(new_position, tracker = "recent"):
            if new_position == "standing":
                ch_Player "Can you stand back up for me?"
            elif new_position == "masturbation":
                ch_Player "Can you lean back?"
            elif new_position == "hands_and_knees":
                ch_Player "Can you get on your hands and knees?"
            elif new_position == "missionary":
                ch_Player "Can you lay on your back?"
            elif new_position == "doggy":
                ch_Player "Can you turn around?"
        else:
            if new_position == "standing":
                ch_Player "Stand back up for me."
            elif new_position == "masturbation":
                ch_Player "Lean back again."
            elif new_position == "hands_and_knees":
                ch_Player "Get on your hands and knees again."
            elif new_position == "missionary":
                ch_Player "Lay on your back again."
            elif new_position == "doggy":
                ch_Player "Turn back around for me."

    if new_position != "standing":
        $ proceed = True    

        $ Clothing_to_remove = []

        python:
            for Clothing_type in reversed(removable_Clothing_types):
                if Character.Clothes[Clothing_type].string and new_position not in Character.Clothes[Clothing_type].available_states.keys():
                    Clothing_to_remove.append(Character.Clothes[Clothing_type])
        
        if Clothing_to_remove:
            call does_Character_agree_to_change_Clothes(Character, removed_Items = Clothing_to_remove, automatic = True) from _call_does_Character_agree_to_change_Clothes

            $ proceed = _return

        if automatic or (proceed and approval_check(Character, threshold = new_position)):
            # if not automatic:
            #     if not Character.History.check(new_position, tracker = "recent"):
            #         if not Character.History.check(new_position):
            #             call expression f"{Character.tag}_accepts_{new_position}_first_time" from _call_expression_78

            #         elif Character.History.check(new_position) == 1:
            #             call expression f"{Character.tag}_accepts_{new_position}_second_time" from _call_expression_79
            #         elif approval_check(Character, threshold = "love"):
            #             call expression f"{Character.tag}_accepts_{new_position}_love" from _call_expression_80
            #         else:
            #             call expression f"{Character.tag}_accepts_{new_position}" from _call_expression_81

            python:
                for A in Character.all_Actions:
                    if new_position not in A.available_poses:
                        stop_Action(A)

                    A.position = new_position

            if Character == Jean and new_position == "doggy" and Player.right_hand_Actions and Jean in Player.right_hand_Actions[0].Targets:
                $ stop_Actions(Player, organ = "right_hand")
            elif Character in [Rogue, Laura] and new_position == "doggy" and Player.left_hand_Actions and Character in Player.left_hand_Actions[0].Targets:
                $ stop_Actions(Player, organ = "left_hand")

            $ renpy.dynamic(temp_Clothing_types = removable_Clothing_types[:])

            while temp_Clothing_types:
                if Character.Clothes[temp_Clothing_types[0]].string:
                    if new_position in Character.Clothes[temp_Clothing_types[0]].available_states.keys():
                        if Character.Clothes[temp_Clothing_types[0]].state not in Character.Clothes[temp_Clothing_types[0]].available_states[new_position]:
                            call fix(Character, temp_Clothing_types[0], state = 0, instant = False) from _call_fix_5

                $ temp_Clothing_types.remove(temp_Clothing_types[0])

            if Action:
                $ Action.position = new_position

            $ check_for_clothed_Actions(Character)

            call show_pose(Character, new_position) from _call_show_pose

            $ Character.History.update(new_position)

            $ hookup_length += 0.25

            if new_position == "hands_and_knees":
                $ Player.give_trait("naked")
                $ Player.give_trait("cock_out")

                $ renpy.dynamic(temp_Characters = Present[:])

                while temp_Characters:
                    if not temp_Characters[0].History.check("seen_Player_naked"):
                        $ EventScheduler.Events[f"{temp_Characters[0].tag}_seeing_penis"].start()

                    $ temp_Characters[0].History.update("seen_Player_naked")
                    
                    $ temp_Characters.remove(temp_Characters[0])

            return True
        else:
            if Character.History.check(f"rejected_{new_position}", tracker = "recent") >= 2:
                call change_Character_stat(Character, "love", -5) from _call_change_Character_stat_825
                call change_Character_stat(Character, "trust", -5) from _call_change_Character_stat_826
                
                call expression f"{Character.tag}_rejects_Action_asked_twice" from _call_expression_82
            elif Character.History.check(f"rejected_{new_position}", tracker = "recent") == 1:
                call change_Character_stat(Character, "love", -2) from _call_change_Character_stat_827

                call expression f"{Character.tag}_rejects_Action_asked_once" from _call_expression_83
            else:
                call expression f"{Character.tag}_rejects_{new_position}" from _call_expression_84

            $ Character.History.update(f"rejected_{new_position}")
    else:
        python:
            for A in Character.all_Actions:
                if new_position not in A.available_poses:
                    stop_Action(A)

                A.position = new_position

        if Action:
            $ Action.position = new_position

        $ check_for_clothed_Actions(Character)

        call show_pose(Character, new_position) from _call_show_pose_1

        $ Character.History.update(new_position)

        $ hookup_length += 0.25

        if new_position == "hands_and_knees":
            $ Player.give_trait("naked")
            $ Player.give_trait("cock_out")
            
            $ renpy.dynamic(temp_Characters = Present[:])

            while temp_Characters:
                if not temp_Characters[0].History.check("seen_Player_naked"):
                    $ EventScheduler.Events[f"{temp_Characters[0].tag}_seeing_penis"].start()

                $ temp_Characters[0].History.update("seen_Player_naked")
                
                $ temp_Characters.remove(temp_Characters[0])

        return True

    return False

label check_double_penetration(Character, Action_type):
    # $ double_penetration = False

    # if Action_type in anal_insertion_Action_types or Character.buttplug:
    #     if Character.remote_vibrator:
    #         $ double_penetration = True

    #     if not double_penetration:
    #         python:
    #             for A in Character.all_Actions:
    #                 if A.Action_type in vaginal_insertion_Action_types:
    #                     double_penetration = True

    #                     break
    # elif Action_type in vaginal_insertion_Action_types or Character.remote_vibrator:
    #     if Character.buttplug:
    #         $ double_penetration = True

    #     if not double_penetration:
    #         python:
    #             for A in Character.all_Actions:
    #                 if A.Action_type in anal_insertion_Action_types:
    #                     double_penetration = True

    #                     break

    # if double_penetration:
    #     if approval_check(Character, threshold = "double_penetrate"):
    #         if not Character.History.check("double_penetrate", tracker = "recent"):
    #             if not Character.History.check("double_penetrate"):
    #                 call expression f"{Character.tag}_accepts_double_penetrate_first_time" from _call_expression_85
    #             # elif Character.History.check("double_penetrate") == 1:
    #             #     call expression f"{Character.tag}_accepts_{"double_penetrate"}_second_time"
    #             # elif approval_check(Character, threshold = "love"):
    #             #     call expression f"{Character.tag}_accepts_{"double_penetrate"}_love"
    #             else:
    #                 call expression f"{Character.tag}_accepts_double_penetrate" from _call_expression_86
    #         else:
    #             call expression f"{Character.tag}_accepts_Action_again" from _call_expression_87
    #     else:
    #         if Character.History.check(f"rejected_{Action_type}", tracker = "recent") >= 2:
    #             call change_Character_stat(Character, "love", -5) from _call_change_Character_stat_828
    #             call change_Character_stat(Character, "trust", -5) from _call_change_Character_stat_829
                
    #             call expression f"{Character.tag}_rejects_Action_asked_twice" from _call_expression_88
    #         elif Character.History.check(f"rejected_{Action_type}", tracker = "recent") == 1:
    #             call change_Character_stat(Character, "love", -2) from _call_change_Character_stat_830
                
    #             call expression f"{Character.tag}_rejects_Action_asked_once" from _call_expression_89
    #         else:
    #             call expression f"{Character.tag}_rejects_double_penetrate" from _call_expression_90

    #         return False

    return True