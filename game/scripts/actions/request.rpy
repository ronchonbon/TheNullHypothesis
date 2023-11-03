label request_hookup(Character):
    $ Character_picker_disabled = True

    $ NPCs_present = False
    
    python:
        for C in Present:
            if C in all_NPCs:
                NPCs_present = C

                break

    if NPCs_present:
        "Maybe not in front of [C.name]. . ."

        return

    if not Player.stamina:
        "You're empty, maybe later."

        return

    if not Character.stamina:
        "[Character.name] seems wiped out. Maybe later?"

        return

    ch_Player "Do you want to mess around?"

    if Character.status["miffed"] or Character.status["mad"]:
        if Character.History.check("rejected_hookup", tracker = "recent") >= 2:
            call change_Girl_stat(Character, "love", -5) from _call_change_Girl_stat_810
            call change_Girl_stat(Character, "trust", -5) from _call_change_Girl_stat_811

            call expression f"{Character.tag}_rejects_Action_asked_twice" from _call_expression_56
        elif Character.History.check("rejected_hookup", tracker = "recent") == 1:
            call change_Girl_stat(Character, "love", -2) from _call_change_Girl_stat_812

            call expression f"{Character.tag}_rejects_Action_asked_once" from _call_expression_57
        else:
            call expression f"{Character.tag}_rejects_hookup_mad" from _call_expression_58

        $ Character.History.update("rejected_hookup")

        if Character.location == Player.location:
            show screen interactions_screen(Character)

        return
    elif Player.location in public_locations and not approval_check(Character, threshold = "exhibitionism"):
        if Character.History.check("rejected_hookup", tracker = "recent") >= 2:
            call change_Girl_stat(Character, "love", -5) from _call_change_Girl_stat_813
            call change_Girl_stat(Character, "trust", -5) from _call_change_Girl_stat_814

            call expression f"{Character.tag}_rejects_Action_asked_twice" from _call_expression_59
        elif Character.History.check("rejected_hookup", tracker = "recent") == 1:
            call change_Girl_stat(Character, "love", -2) from _call_change_Girl_stat_815
            
            call expression f"{Character.tag}_rejects_Action_asked_once" from _call_expression_60
        else:
            call expression f"{Character.tag}_rejects_hookup_public" from _call_expression_61

        $ Character.History.update(f"rejected_hookup")

        if Character.location == Player.location:
            show screen interactions_screen(Character)

        return
    elif len(Present) > 1:#not are_Characters_in_Partners(Present):
        if Character.History.check("rejected_hookup", tracker = "recent") >= 2:
            call change_Girl_stat(Character, "love", -5) from _call_change_Girl_stat_816
            call change_Girl_stat(Character, "trust", -5) from _call_change_Girl_stat_817

            call expression f"{Character.tag}_rejects_Action_asked_twice" from _call_expression_62
        elif Character.History.check("rejected_hookup", tracker = "recent") == 1:
            call change_Girl_stat(Character, "love", -2) from _call_change_Girl_stat_818

            call expression f"{Character.tag}_rejects_Action_asked_once" from _call_expression_63
        else:
            call expression f"{Character.tag}_rejects_hookup_public" from _call_expression_64

        $ Character.History.update("rejected_hookup")

        if Character.location == Player.location:
            show screen interactions_screen(Character)

        return

    $ temp_hookup_Characters = Present[:]

    while temp_hookup_Characters:
        if approval_check(temp_hookup_Characters[0], threshold = "hookup"):
            if not temp_hookup_Characters[0].History.check("hookup", tracker = "recent"):
                if not temp_hookup_Characters[0].History.check("hookup"):
                    call expression f"{temp_hookup_Characters[0].tag}_accepts_hookup_first_time" from _call_expression_65\
                elif temp_hookup_Characters[0].History.check("hookup") == 1:
                    call expression f"{temp_hookup_Characters[0].tag}_accepts_hookup_second_time" from _call_expression_66
                elif approval_check(temp_hookup_Characters[0], threshold = "love"):
                    call expression f"{temp_hookup_Characters[0].tag}_accepts_hookup_love" from _call_expression_67
                else:
                    call expression f"{temp_hookup_Characters[0].tag}_accepts_hookup" from _call_expression_68
        else:
            if temp_hookup_Characters[0].History.check("rejected_hookup", tracker = "recent") >= 2:
                call change_Girl_stat(temp_hookup_Characters[0], "love", -5) from _call_change_Girl_stat_819
                call change_Girl_stat(temp_hookup_Characters[0], "trust", -5) from _call_change_Girl_stat_820

                call expression f"{temp_hookup_Characters[0].tag}_rejects_hookup_asked_twice" from _call_expression_69
            elif temp_hookup_Characters[0].History.check("rejected_hookup", tracker = "recent") == 1:
                call change_Girl_stat(temp_hookup_Characters[0], "love", -2) from _call_change_Girl_stat_821

                call expression f"{temp_hookup_Characters[0].tag}_rejects_hookup_asked_once" from _call_expression_70
            else:
                call expression f"{temp_hookup_Characters[0].tag}_rejects_hookup" from _call_expression_71

            $ temp_hookup_Characters[0].History.update("rejected_hookup")

            if Character.location == Player.location:
                show screen interactions_screen(Character)

            return

        $ temp_hookup_Characters.remove(temp_hookup_Characters[0])

    python:
        for C in Present:
            if not C.History.check("hookup", tracker = "recent"):
                C.History.update("hookup")

    $ Character_picker_disabled = False

    show screen Action_screen()

    return

label request_Action(Action_type, Actors, Targets):
    if Actors in all_Characters or Actors == Player:
        $ Actors = [Actors]

    if Targets in all_Characters or Targets == Player:
        $ Targets = [Targets]

    $ Action = ActionClass(Action_type, Actors, Targets)

    if not focused_Girl.History.check(Action_type, tracker = "recent"):
        $ Player.voice(Action.line)

    if approval_check(focused_Girl, threshold = Action_type):
        if not focused_Girl.History.check(Action_type, tracker = "recent"):
            if not focused_Girl.History.check(Action_type):
                call expression f"{focused_Girl.tag}_accepts_{Action_type}_first_time" from _call_expression_72\
            # elif focused_Girl.History.check(Action_type) == 1:
            #     call expression f"{focused_Girl.tag}_accepts_{Action_type}_second_time"
            # elif approval_check(focused_Girl, threshold = "love"):
            #     call expression f"{focused_Girl.tag}_accepts_{Action_type}_love"

                $ focused_Girl.unlocked_Actions.append(Action_type)
            else:
                call expression f"{focused_Girl.tag}_accepts_{Action_type}" from _call_expression_73
        else:
            call expression f"{focused_Girl.tag}_accepts_Action_again" from _call_expression_74

        call check_double_penetration(focused_Girl, Action_type) from _call_check_double_penetration

        if _return:
            $ selected_Action_index = 0

            call start_Action(Action) from _call_start_Action_4
        else:
            $ focused_Girl.History.update(f"rejected_double_penetrate")
    else:
        if focused_Girl.History.check(f"rejected_{Action_type}", tracker = "recent") >= 2:
            call change_Girl_stat(focused_Girl, "love", -5) from _call_change_Girl_stat_822
            call change_Girl_stat(focused_Girl, "trust", -5) from _call_change_Girl_stat_823

            call expression f"{focused_Girl.tag}_rejects_Action_asked_twice" from _call_expression_75
        elif focused_Girl.History.check(f"rejected_{Action_type}", tracker = "recent") == 1:
            call change_Girl_stat(focused_Girl, "love", -2) from _call_change_Girl_stat_824

            call expression f"{focused_Girl.tag}_rejects_Action_asked_once" from _call_expression_76
        else:
            call expression f"{focused_Girl.tag}_rejects_{Action_type}" from _call_expression_77

        $ focused_Girl.History.update(f"rejected_{Action_type}")

    return

label request_mode(Action, mode):
    $ temp_speed = speed
    $ temp_intensity = intensity

    $ speed = 0.001
    $ intensity = 0.001

    $ Action.mode = mode

    $ selected_Action_mode = mode

    if not ongoing_Event or has_Action_control:
        call expression f"{Action.Action_type}_initiations" pass (Action = Action) from _call_expression_131

    $ speed = temp_speed
    $ intensity = temp_intensity

    return

label request_position(Girl, new_position, Action = None, automatic = False):
    if not automatic:
        if new_position == "standing":
            ch_Player "Can you stand up for me?"
        elif new_position == "masturbation":
            ch_Player "Can you lean back?"
        elif new_position == "hands_and_knees":
            ch_Player "Can you get on your hands and knees?"
        elif new_position == "missionary":
            ch_Player "Can you lay on your back?"
        elif new_position == "doggy":
            ch_Player "Can you turn around?"

    if new_position != "standing":
        $ proceed = True    

        $ Clothing_to_remove = []

        python:
            for Clothing_type in reversed(removable_Clothing_types):
                if Girl.Clothes[Clothing_type].string and new_position not in Girl.Clothes[Clothing_type].available_states.keys():
                    Clothing_to_remove.append(Girl.Clothes[Clothing_type])
        
        if Clothing_to_remove:
            call does_Girl_agree_to_change_Clothes(Girl, removed_Items = Clothing_to_remove, automatic = True) from _call_does_Girl_agree_to_change_Clothes

            $ proceed = _return

        if automatic or (proceed and approval_check(Girl, threshold = new_position)):
            if not automatic:
                if not Girl.History.check(new_position, tracker = "recent"):
                    if not Girl.History.check(new_position):
                        call expression f"{Girl.tag}_accepts_{new_position}_first_time" from _call_expression_78

                    elif Girl.History.check(new_position) == 1:
                        call expression f"{Girl.tag}_accepts_{new_position}_second_time" from _call_expression_79
                    elif approval_check(Girl, threshold = "love"):
                        call expression f"{Girl.tag}_accepts_{new_position}_love" from _call_expression_80
                    else:
                        call expression f"{Girl.tag}_accepts_{new_position}" from _call_expression_81

            python:
                for A in Girl.all_Actions:
                    if new_position not in A.available_poses:
                        stop_Action(A)

                    A.position = new_position

            if Girl == Jean and new_position == "doggy" and Player.right_hand_Actions and Jean in Player.right_hand_Actions[0].Targets:
                $ stop_Actions(Player, organ = "right_hand")
            elif Girl in [Rogue, Laura] and new_position == "doggy" and Player.left_hand_Actions and Girl in Player.left_hand_Actions[0].Targets:
                $ stop_Actions(Player, organ = "left_hand")

            $ temp_undressed_Clothing_types = removable_Clothing_types[:]

            while temp_undressed_Clothing_types:
                if Girl.Clothes[temp_undressed_Clothing_types[0]].string:
                    if new_position in Girl.Clothes[temp_undressed_Clothing_types[0]].available_states.keys():
                        if Girl.Clothes[temp_undressed_Clothing_types[0]].state not in Girl.Clothes[temp_undressed_Clothing_types[0]].available_states[new_position]:
                            call fix(Girl, temp_undressed_Clothing_types[0], state = 0, instant = False) from _call_fix_5

                $ temp_undressed_Clothing_types.remove(temp_undressed_Clothing_types[0])

            if Action:
                $ Action.position = new_position

            call show_pose(Girl, new_position) from _call_show_pose

            $ Girl.History.update(new_position)

            $ selected_Action_index = 0

            return True
        else:
            if Girl.History.check(f"rejected_{new_position}", tracker = "recent") >= 2:
                call change_Girl_stat(Girl, "love", -5) from _call_change_Girl_stat_825
                call change_Girl_stat(Girl, "trust", -5) from _call_change_Girl_stat_826
                
                call expression f"{Girl.tag}_rejects_Action_asked_twice" from _call_expression_82
            elif Girl.History.check(f"rejected_{new_position}", tracker = "recent") == 1:
                call change_Girl_stat(Girl, "love", -2) from _call_change_Girl_stat_827

                call expression f"{Girl.tag}_rejects_Action_asked_once" from _call_expression_83
            else:
                call expression f"{Girl.tag}_rejects_{new_position}" from _call_expression_84

            $ Girl.History.update(f"rejected_{new_position}")
    else:
        python:
            for A in Girl.all_Actions:
                if new_position not in A.available_poses:
                    stop_Action(A)

                A.position = new_position

        if Action:
            $ Action.position = new_position

        call show_pose(Girl, new_position) from _call_show_pose_1

        $ selected_Action_index = 0

        return True

    return False

label check_double_penetration(Girl, Action_type):
    # $ double_penetration = False

    # if Action_type in anal_insertion_Action_types or Girl.buttplug:
    #     if Girl.remote_vibrator:
    #         $ double_penetration = True

    #     if not double_penetration:
    #         python:
    #             for A in Girl.all_Actions:
    #                 if A.Action_type in vaginal_insertion_Action_types:
    #                     double_penetration = True

    #                     break
    # elif Action_type in vaginal_insertion_Action_types or Girl.remote_vibrator:
    #     if Girl.buttplug:
    #         $ double_penetration = True

    #     if not double_penetration:
    #         python:
    #             for A in Girl.all_Actions:
    #                 if A.Action_type in anal_insertion_Action_types:
    #                     double_penetration = True

    #                     break

    # if double_penetration:
    #     if approval_check(Girl, threshold = "double_penetrate"):
    #         if not Girl.History.check("double_penetrate", tracker = "recent"):
    #             if not Girl.History.check("double_penetrate"):
    #                 call expression f"{Girl.tag}_accepts_double_penetrate_first_time" from _call_expression_85
    #             # elif Girl.History.check("double_penetrate") == 1:
    #             #     call expression f"{Girl.tag}_accepts_{"double_penetrate"}_second_time"
    #             # elif approval_check(Girl, threshold = "love"):
    #             #     call expression f"{Girl.tag}_accepts_{"double_penetrate"}_love"
    #             else:
    #                 call expression f"{Girl.tag}_accepts_double_penetrate" from _call_expression_86
    #         else:
    #             call expression f"{Girl.tag}_accepts_Action_again" from _call_expression_87
    #     else:
    #         if Girl.History.check(f"rejected_{Action_type}", tracker = "recent") >= 2:
    #             call change_Girl_stat(Girl, "love", -5) from _call_change_Girl_stat_828
    #             call change_Girl_stat(Girl, "trust", -5) from _call_change_Girl_stat_829
                
    #             call expression f"{Girl.tag}_rejects_Action_asked_twice" from _call_expression_88
    #         elif Girl.History.check(f"rejected_{Action_type}", tracker = "recent") == 1:
    #             call change_Girl_stat(Girl, "love", -2) from _call_change_Girl_stat_830
                
    #             call expression f"{Girl.tag}_rejects_Action_asked_once" from _call_expression_89
    #         else:
    #             call expression f"{Girl.tag}_rejects_double_penetrate" from _call_expression_90

    #         return False

    return True