init python:

    import copy

    def stop_Action(Action):
        global ongoing_Actions

        for A in Action.Actors:
            for O in A.all_Organs:
                other_Actions = getattr(A, f"{O}_Actions")

                while Action in other_Actions:
                    other_Actions.remove(Action)

                while Action in A.all_Actions:
                    A.all_Actions.remove(Action)

                setattr(A, f"{O}_Actions", other_Actions)

            for T in Action.Targets:
                if T in A.Lovers.keys() and Action in A.Lovers[T]:
                    A.Lovers[T].remove(Action)

        for T in Action.Targets:
            for O in T.all_Organs:
                other_Actions = getattr(T, f"{O}_Actions")

                while Action in other_Actions:
                    other_Actions.remove(Action)

                while Action in T.all_Actions:
                    T.all_Actions.remove(Action)

                setattr(T, f"{O}_Actions", other_Actions)

            for A in Action.Actors:
                if A in T.Lovers.keys() and Action in T.Lovers[A]:
                    T.Lovers[A].remove(Action)

        if Action in ongoing_Actions:
            ongoing_Actions.remove(Action)

        del Action

        return

    def stop_Actions(Character, organ = None):
        if not organ:
            for O in Character.all_Organs:
                Actions = getattr(Character, f"{O}_Actions")

                for A in Actions:
                    stop_Action(A)
        else:
            Actions = getattr(Character, f"{organ}_Actions")

            for A in Actions:
                stop_Action(A)

        return

    def stop_conflicting_Actions(Action_type, Actors, Targets):
        if Action_type == "makeout":
            for A in Actors:
                stop_Actions(A, organ = "mouth")

            for T in Targets:
                stop_Actions(T, organ = "mouth")
        elif Action_type in ["choke"]:
            for A in Actors:
                if A.right_hand_Actions and A.left_hand_Actions:
                    stop_Actions(A, organ = "left_hand")

            for T in Targets:
                stop_Actions(T, organ = "neck")
        elif Action_type in ["touch_thighs_over_clothes", "touch_thighs_higher_over_clothes", "touch_thighs", "touch_thighs_higher"]:
            for A in Actors:
                if A.right_hand_Actions and A.left_hand_Actions:
                    stop_Actions(A, organ = "left_hand")

            for T in Targets:
                if T.right_thigh_Actions and T.left_thigh_Actions:
                    stop_Actions(T, organ = "left_thigh")
        elif Action_type in ["touch_breasts_over_clothes", "touch_breasts", "pinch_nipples"]:
            for A in Actors:
                if A.right_hand_Actions and A.left_hand_Actions:
                    stop_Actions(A, organ = "left_hand")

            for T in Targets:
                if T.right_breast_Actions and T.left_breast_Actions:
                    stop_Actions(T, organ = "left_breast")

                if T.right_nipple_Actions and T.left_nipple_Actions:
                    stop_Actions(T, organ = "left_nipple")
        elif Action_type == "suck_nipples":
            for A in Actors:
                stop_Actions(A, organ = "mouth")

            for T in Targets:
                if T.right_nipple_Actions and T.left_nipple_Actions:
                    stop_Actions(T, organ = "left_nipple")
        elif Action_type in ["grab_ass_over_clothes", "grab_ass"]:
            for A in Actors:
                if A.right_hand_Actions and A.left_hand_Actions:
                    stop_Actions(A, organ = "left_hand")

            for T in Targets:
                stop_Actions(T, organ = "ass")
        elif Action_type in ["touch_pussy_over_clothes", "touch_pussy", "vibrator"]:
            for A in Actors:
                if A.right_hand_Actions and A.left_hand_Actions:
                    stop_Actions(A, organ = "left_hand")

                if A.position not in ["69", "doggy"]:
                    for other_Action in A.cock_Actions:
                        stop_Action(other_Action)

                    for other_Action in A.balls_Actions:
                        stop_Action(other_Action)

            for T in Targets:
                stop_Actions(T, organ = "clitoris")

                T.remote_vibrator = False
        elif Action_type == "finger_pussy":
            for A in Actors:
                if Jean in Targets and Jean.position == "doggy":
                    stop_Actions(A, organ = "left_hand")
                elif A.right_hand_Actions and A.left_hand_Actions:
                    stop_Actions(A, organ = "left_hand")

                if A.position not in ["69", "doggy"]:
                    for other_Action in A.cock_Actions:
                        stop_Action(other_Action)

                    for other_Action in A.balls_Actions:
                        stop_Action(other_Action)

            for T in Targets:
                stop_Actions(T, organ = "vagina")

                T.remote_vibrator = False
        elif Action_type == "finger_ass":
            for A in Actors:
                if Jean in Targets and Jean.position == "doggy":
                    stop_Actions(A, organ = "left_hand")
                elif Rogue in Targets and Rogue.position == "doggy":
                    stop_Actions(A, organ = "right_hand")
                elif Laura in Targets and Laura.position == "doggy":
                    stop_Actions(A, organ = "right_hand")
                elif A.right_hand_Actions and A.left_hand_Actions:
                    stop_Actions(A, organ = "left_hand")

                if A.position not in ["69", "doggy"]:
                    for other_Action in A.cock_Actions:
                        stop_Action(other_Action)

                    for other_Action in A.balls_Actions:
                        stop_Action(other_Action)

            for T in Targets:
                stop_Actions(T, organ = "anus")

                T.buttplug = None
        elif Action_type == "eat_pussy":
            for A in Actors:
                stop_Actions(A, organ = "mouth")

                if A.position != "69":
                    for other_Action in A.cock_Actions:
                        stop_Action(other_Action)

                    for other_Action in A.balls_Actions:
                        stop_Action(other_Action)

            for T in Targets:
                stop_Actions(T, organ = "clitoris")
                stop_Actions(T, organ = "vagina")

                T.remote_vibrator = False
        elif Action_type == "eat_ass":
            for A in Actors:
                stop_Actions(A, organ = "mouth")

                if A.position != "69":
                    for other_Action in A.cock_Actions:
                        stop_Action(other_Action)

                    for other_Action in A.balls_Actions:
                        stop_Action(other_Action)

            for T in Targets:
                stop_Actions(T, organ = "anus")

                T.buttplug = None
        elif Action_type == "handjob":
            for A in Actors:
                stop_Actions(A, organ = "left_hand")

                for other_Action in A.all_Actions:
                    if other_Action.Action_type in job_Action_types:
                        stop_Action(other_Action)

                if A.position != "69":
                    for other_Action in A.vagina_Actions:
                        stop_Action(other_Action)

                    for other_Action in A.clitoris_Actions:
                        stop_Action(other_Action)

                    for other_Action in A.anus_Actions:
                        stop_Action(other_Action)

            for T in Targets:
                for other_Action in T.cock_Actions:
                    if other_Action.Action_type in insertion_Action_types or any(Target in Actors for Target in other_Action.Targets):
                        stop_Action(other_Action)

                if T.position != "69":
                    for other_Action in T.mouth_Actions:
                        stop_Action(other_Action)

                    stop_Actions(T, organ = "right_hand")
                    stop_Actions(T, organ = "left_hand")
        elif Action_type == "fondle_balls":
            for A in Actors:
                if A.right_hand_Actions and A.left_hand_Actions:
                    stop_Actions(A, organ = "left_hand")
                
                if A.position != "69":
                    for other_Action in A.vagina_Actions:
                        stop_Action(other_Action)

                    for other_Action in A.clitoris_Actions:
                        stop_Action(other_Action)

                    for other_Action in A.anus_Actions:
                        stop_Action(other_Action)

            for T in Targets:
                stop_Actions(T, organ = "balls")

                if T.position != "69":
                    for other_Action in T.mouth_Actions:
                        stop_Action(other_Action)

                    stop_Actions(T, organ = "right_hand")
                    stop_Actions(T, organ = "left_hand")
        elif Action_type in ["blowjob", "deepthroat"]:
            for A in Actors:
                stop_Actions(A, organ = "mouth")

                for other_Action in A.all_Actions:
                    if other_Action.Action_type in job_Action_types:
                        stop_Action(other_Action)

                if A.position != "69":
                    for other_Action in A.vagina_Actions:
                        stop_Action(other_Action)

                    for other_Action in A.clitoris_Actions:
                        stop_Action(other_Action)

                    for other_Action in A.anus_Actions:
                        stop_Action(other_Action)

                if A.position == "hands_and_knees":
                    stop_Actions(A, organ = "right_hand")

            for T in Targets:
                for other_Action in T.cock_Actions:
                    if other_Action.Action_type in insertion_Action_types or any(Target in Actors for Target in other_Action.Targets):
                        stop_Action(other_Action)

                if T.position != "69":
                    for other_Action in T.mouth_Actions:
                        stop_Action(other_Action)

                    stop_Actions(T, organ = "right_hand")
                    stop_Actions(T, organ = "left_hand")
        elif Action_type == "suck_balls":
            for A in Actors:
                stop_Actions(A, organ = "mouth")

                if A.position != "69":
                    for other_Action in A.vagina_Actions:
                        stop_Action(other_Action)

                    for other_Action in A.clitoris_Actions:
                        stop_Action(other_Action)

                    for other_Action in A.anus_Actions:
                        stop_Action(other_Action)

            for T in Targets:
                stop_Actions(T, organ = "balls")

                if T.position != "69":
                    for other_Action in T.mouth_Actions:
                        stop_Action(other_Action)

                stop_Actions(T, organ = "right_hand")
                stop_Actions(T, organ = "left_hand")
        elif Action_type in ["self_touch_pussy"]:
            for A in Actors:
                stop_Actions(A, organ = "right_hand")

            for T in Targets:
                stop_Actions(T, organ = "clitoris")
                # stop_Actions(T, organ = "vagina")

                T.remote_vibrator = False
        elif Action_type in ["self_finger_ass"]:
            for A in Actors:
                stop_Actions(A, organ = "right_hand")

            for T in Targets:
                stop_Actions(T, organ = "anus")

                T.buttplug = None
        elif Action_type in ["self_vibrator"]:
            for A in Actors:
                if A.right_hand_Actions and A.left_hand_Actions:
                    stop_Actions(A, organ = "left_hand")

            for T in Targets:
                stop_Actions(T, organ = "clitoris")

                T.remote_vibrator = False
        elif Action_type in ["self_dildo_pussy", "dildo_pussy"]:
            for A in Actors:
                if A.right_hand_Actions and A.left_hand_Actions:
                    stop_Actions(A, organ = "left_hand")

            for T in Targets:
                stop_Actions(T, organ = "clitoris")
                stop_Actions(T, organ = "vagina")

                T.remote_vibrator = False
        elif Action_type in ["self_dildo_ass", "dildo_ass"]:
            for A in Actors:
                if A.right_hand_Actions and A.left_hand_Actions:
                    stop_Actions(A, organ = "left_hand")

            for T in Targets:
                stop_Actions(T, organ = "anus")

                T.buttplug = None
        elif Action_type in ["grind_pussy"]:
            for A in Actors:
                stop_Actions(A, organ = "cock")
                stop_Actions(A, organ = "balls")

                if A.position != "69":
                    for other_Action in A.mouth_Actions:
                        stop_Action(other_Action)

            for T in Targets:
                stop_Actions(T, organ = "vagina")

                if T.position == "doggy":
                    stop_Actions(T, organ = "anus")

                T.remote_vibrator = False
        elif Action_type in ["sex"]:
            for A in Actors:
                stop_Actions(A, organ = "cock")
                stop_Actions(A, organ = "balls")

                if A.position != "69":
                    for other_Action in A.mouth_Actions:
                        stop_Action(other_Action)

            for T in Targets:
                stop_Actions(T, organ = "vagina")

                T.remote_vibrator = False
        elif Action_type in ["grind_ass"]:
            for A in Actors:
                stop_Actions(A, organ = "cock")
                stop_Actions(A, organ = "balls")

                if A.position != "69":
                    for other_Action in A.mouth_Actions:
                        stop_Action(other_Action)

            for T in Targets:
                stop_Actions(T, organ = "anus")

                if T.position == "doggy":
                    stop_Actions(T, organ = "vagina")
        elif Action_type in ["anal"]:
            for A in Actors:
                stop_Actions(A, organ = "cock")
                stop_Actions(A, organ = "balls")

                if A.position != "69":
                    for other_Action in A.mouth_Actions:
                        stop_Action(other_Action)

            for T in Targets:
                stop_Actions(T, organ = "anus")

                T.buttplug = None

        return

    def get_Action_Characters(Action, remove_Player = True):
        global Player

        Characters = list(set(Action.Actors[:] + Action.Targets[:]))

        if remove_Player and Player in Characters:
            Characters.remove(Player)

        return Characters

label start_Action(Action):
    $ Actors = Action.Actors
    $ Targets = Action.Targets

    $ stop_conflicting_Actions(Action.Action_type, Actors, Targets)

    if Action.Action_type in active_Action_types:
        python:
            for T in Targets:
                if T.position in Action.available_poses:
                    Action.position = T.position
                else:
                    if approval_check(T, threshold = Action.available_poses[0]):
                        Action.position = Action.available_poses[0]
                    elif len(Action.available_poses) > 1 and approval_check(T, threshold = Action.available_poses[1]):
                        Action.position = Action.available_poses[1]
                    elif len(Action.available_poses) > 2 and approval_check(T, threshold = Action.available_poses[2]):
                        Action.position = Action.available_poses[2]
                    elif len(Action.available_poses) > 3 and approval_check(T, threshold = Action.available_poses[3]):
                        Action.position = Action.available_poses[3]
                    elif len(Action.available_poses) > 4 and approval_check(T, threshold = Action.available_poses[4]):
                        Action.position = Action.available_poses[4]
                    else:
                        Action.position = Action.available_poses[0]

        $ temp_showing_Characters = Targets[:]
    elif Action.Action_type in passive_Action_types:
        python:
            for A in Actors:
                if A.position in Action.available_poses:
                    Action.position = A.position
                else:
                    if approval_check(A, threshold = Action.available_poses[0]):
                        Action.position = Action.available_poses[0]
                    elif len(Action.available_poses) > 1 and approval_check(A, threshold = Action.available_poses[1]):
                        Action.position = Action.available_poses[1]
                    elif len(Action.available_poses) > 2 and approval_check(A, threshold = Action.available_poses[2]):
                        Action.position = Action.available_poses[2]
                    elif len(Action.available_poses) > 3 and approval_check(A, threshold = Action.available_poses[3]):
                        Action.position = Action.available_poses[3]
                    elif len(Action.available_poses) > 4 and approval_check(A, threshold = Action.available_poses[4]):
                        Action.position = Action.available_poses[4]
                    else:
                        Action.position = Action.available_poses[0]

        $ temp_showing_Characters = Actors[:]

    $ proceed = True

    if (not ongoing_Event or has_Action_control) and proceed:
        while temp_showing_Characters:
            $ Clothing_to_remove = []

            python:
                for Clothing_type in reversed(removable_Clothing_types):
                    if temp_showing_Characters[0].Clothes[Clothing_type].string and Action.position not in temp_showing_Characters[0].Clothes[Clothing_type].available_states.keys():
                        Clothing_to_remove.append(temp_showing_Characters[0].Clothes[Clothing_type])

            if Clothing_to_remove:
                call does_Girl_agree_to_change_Clothes(temp_showing_Characters[0], removed_Items = Clothing_to_remove, automatic = True) from _call_does_Girl_agree_to_change_Clothes_1

                $ proceed = _return

            if proceed:
                if temp_showing_Characters[0].position != Action.position:
                    call request_position(temp_showing_Characters[0], Action.position) from _call_request_position_10

                pause 0.5

                $ Clothing_to_remove = []
                $ Clothing_to_undress = []
                $ undressed_states = []

                python:
                    for Clothing_type in reversed(removable_Clothing_types):
                        if temp_showing_Characters[0].Clothes[Clothing_type].string and Action.position in temp_showing_Characters[0].Clothes[Clothing_type].available_states.keys():
                            if Action.Action_type in ["touch_thighs", "touch_thighs_higher"]:
                                if "thighs" in temp_showing_Characters[0].Clothes[Clothing_type].covers[Action.position].keys():
                                    current_state = temp_showing_Characters[0].Clothes[Clothing_type].state

                                    while current_state in temp_showing_Characters[0].Clothes[Clothing_type].covers[Action.position]["thighs"] and current_state <= temp_showing_Characters[0].Clothes[Clothing_type].available_states[Action.position][-1]:
                                        current_state += 1

                                    if current_state not in temp_showing_Characters[0].Clothes[Clothing_type].available_states[Action.position]:
                                        Clothing_to_remove.append(temp_showing_Characters[0].Clothes[Clothing_type])
                                    else:
                                        Clothing_to_undress.append(temp_showing_Characters[0].Clothes[Clothing_type])
                                        undressed_states.append(current_state)
                            elif Action.Action_type in ["touch_breasts", "pinch_nipples", "suck_nipples"]:
                                if "breasts" in temp_showing_Characters[0].Clothes[Clothing_type].covers[Action.position].keys():
                                    current_state = temp_showing_Characters[0].Clothes[Clothing_type].state

                                    while current_state in temp_showing_Characters[0].Clothes[Clothing_type].covers[Action.position]["breasts"] and current_state <= temp_showing_Characters[0].Clothes[Clothing_type].available_states[Action.position][-1]:
                                        current_state += 1

                                    if current_state not in temp_showing_Characters[0].Clothes[Clothing_type].available_states[Action.position]:
                                        Clothing_to_remove.append(temp_showing_Characters[0].Clothes[Clothing_type])
                                    else:
                                        Clothing_to_undress.append(temp_showing_Characters[0].Clothes[Clothing_type])
                                        undressed_states.append(current_state)
                            elif Action.Action_type in ["touch_pussy", "finger_pussy", "eat_pussy", "self_touch_pussy", "self_vibrator", "self_dildo_pussy", "sex", "vibrator", "dildo_pussy"]:
                                if "pussy" in temp_showing_Characters[0].Clothes[Clothing_type].covers[Action.position].keys():
                                    current_state = temp_showing_Characters[0].Clothes[Clothing_type].state

                                    while current_state in temp_showing_Characters[0].Clothes[Clothing_type].covers[Action.position]["pussy"] and current_state <= temp_showing_Characters[0].Clothes[Clothing_type].available_states[Action.position][-1]:
                                        current_state += 1

                                    if current_state not in temp_showing_Characters[0].Clothes[Clothing_type].available_states[Action.position]:
                                        Clothing_to_remove.append(temp_showing_Characters[0].Clothes[Clothing_type])
                                    else:
                                        Clothing_to_undress.append(temp_showing_Characters[0].Clothes[Clothing_type])
                                        undressed_states.append(current_state)
                            elif Action.Action_type in ["finger_ass", "eat_ass", "self_finger_ass", "self_dildo_ass", "anal", "dildo_ass"]:
                                if "anus" in temp_showing_Characters[0].Clothes[Clothing_type].covers[Action.position].keys():
                                    current_state = temp_showing_Characters[0].Clothes[Clothing_type].state

                                    while current_state in temp_showing_Characters[0].Clothes[Clothing_type].covers[Action.position]["anus"] and current_state <= temp_showing_Characters[0].Clothes[Clothing_type].available_states[Action.position][-1]:
                                        current_state += 1

                                    if current_state not in temp_showing_Characters[0].Clothes[Clothing_type].available_states[Action.position]:
                                        Clothing_to_remove.append(temp_showing_Characters[0].Clothes[Clothing_type])
                                    else:
                                        Clothing_to_undress.append(temp_showing_Characters[0].Clothes[Clothing_type])
                                        undressed_states.append(current_state)

                if Clothing_to_remove or Clothing_to_undress:
                    call does_Girl_agree_to_change_Clothes(temp_showing_Characters[0], removed_Items = Clothing_to_remove, undressed_Items = Clothing_to_undress, undressed_states = undressed_states, automatic = True) from _call_does_Girl_agree_to_change_Clothes_2

                    $ proceed = _return

            $ temp_showing_Characters.remove(temp_showing_Characters[0])

    if proceed:
        if Action.Action_type in cock_Action_types:
            $ Player.naked = True
            $ Player.cock_out = True

            $ temp_seeing_Characters = Present[:]
            
            while temp_seeing_Characters:
                if not temp_seeing_Characters[0].History.check("seen_Player_naked"):
                    $ EventScheduler.Events[f"{temp_seeing_Characters[0].tag}_seeing_penis"].start()

                $ temp_seeing_Characters[0].History.update("seen_Player_naked")
                
                $ temp_seeing_Characters.remove(temp_seeing_Characters[0])

        if Player in Action.Actors or Player in Action.Targets:
            $ Player.position = Action.position

        $ stop_conflicting_Actions(Action.Action_type, Actors, Targets)

        python:
            for A in Actors:
                for T in Targets:
                    if T != A:
                        if T in A.Lovers.keys():
                            if Action not in A.Lovers[T]:
                                A.Lovers[T].append(Action)
                        else:
                            A.Lovers[T] = [Action]

                for other_A in Actors:
                    if other_A != A:
                        if other_A in A.Lovers.keys():
                            if Action not in A.Lovers[other_A]:
                                A.Lovers[other_A].append(Action)
                        else:
                            A.Lovers[other_A] = [Action]

            for T in Targets:
                for A in Actors:
                    if A != T:
                        if A in T.Lovers.keys():
                            if Action not in T.Lovers[A]:
                                T.Lovers[A].append(Action)
                        else:
                            T.Lovers[A] = [Action]

                for other_T in Targets:
                    if other_T != T:
                        if other_T in T.Lovers.keys():
                            if Action not in T.Lovers[other_T]:
                                T.Lovers[other_T].append(Action)
                        else:
                            T.Lovers[other_T] = [Action]

            if Action.Action_type == "makeout":
                for A in Actors:
                    A.mouth_Actions = [Action]
                    A.all_Actions.append(Action)

                for T in Targets:
                    T.mouth_Actions = [Action]
                    T.all_Actions.append(Action)
            elif Action.Action_type in ["choke"]:
                for A in Actors:
                    if A.right_hand_Actions:
                        A.left_hand_Actions = [Action]
                    else:
                        A.right_hand_Actions = [Action]
                        
                    A.all_Actions.append(Action)

                for T in Targets:
                    T.neck_Actions = [Action]
                    T.all_Actions.append(Action)
            elif Action.Action_type in ["touch_thighs_over_clothes", "touch_thighs_higher_over_clothes", "touch_thighs", "touch_thighs_higher"]:
                for A in Actors:
                    if A.right_hand_Actions:
                        A.left_hand_Actions = [Action]
                    else:
                        A.right_hand_Actions = [Action]
                        
                    A.all_Actions.append(Action)

                for T in Targets:
                    if T.right_thigh_Actions:
                        T.left_thigh_Actions = [Action]
                    else:
                        T.right_thigh_Actions = [Action]
                        
                    T.all_Actions.append(Action)
            elif Action.Action_type in ["touch_breasts_over_clothes", "touch_breasts"]:
                for A in Actors:
                    if A.right_hand_Actions:
                        A.left_hand_Actions = [Action]
                    else:
                        A.right_hand_Actions = [Action]
                        
                    A.all_Actions.append(Action)

                for T in Targets:
                    if T.left_breast_Actions or T.left_nipple_Actions:
                        T.right_breast_Actions = [Action]
                    else:
                        T.left_breast_Actions = [Action]

                    T.all_Actions.append(Action)
            elif Action.Action_type == "pinch_nipples":
                for A in Actors:
                    if A.right_hand_Actions:
                        A.left_hand_Actions = [Action]
                    else:
                        A.right_hand_Actions = [Action]
                        
                    A.all_Actions.append(Action)

                for T in Targets:
                    if T.left_breast_Actions or T.left_nipple_Actions:
                        T.right_nipple_Actions = [Action]
                    else:
                        T.left_nipple_Actions = [Action]

                    T.all_Actions.append(Action)
            elif Action.Action_type == "suck_nipples":
                for A in Actors:
                    A.mouth_Actions = [Action]
                    A.all_Actions.append(Action)

                for T in Targets:
                    if T.left_breast_Actions or T.left_nipple_Actions:
                        T.right_nipple_Actions = [Action]
                    else:
                        T.left_nipple_Actions = [Action]

                    T.all_Actions.append(Action)
            elif Action.Action_type in ["grab_ass_over_clothes", "grab_ass"]:
                for A in Actors:
                    if A.right_hand_Actions:
                        A.left_hand_Actions = [Action]
                    else:
                        A.right_hand_Actions = [Action]
                        
                    A.all_Actions.append(Action)

                for T in Targets:
                    T.ass_Actions = [Action]
                    T.all_Actions.append(Action)
            elif Action.Action_type in ["touch_pussy_over_clothes", "touch_pussy", "self_vibrator", "vibrator"]:
                for A in Actors:
                    if A.right_hand_Actions:
                        A.left_hand_Actions = [Action]
                    else:
                        A.right_hand_Actions = [Action]

                    A.all_Actions.append(Action)

                for T in Targets:
                    T.clitoris_Actions = [Action]
                    T.all_Actions.append(Action)
            elif Action.Action_type in ["finger_pussy"]:
                for A in Actors:
                    if Jean in Targets and Action.position == "doggy":
                        A.left_hand_Actions = [Action]
                    elif A.right_hand_Actions:
                        A.left_hand_Actions = [Action]
                    else:
                        A.right_hand_Actions = [Action]

                    A.all_Actions.append(Action)

                for T in Targets:
                    T.vagina_Actions = [Action]
                    T.all_Actions.append(Action)
            elif Action.Action_type == "eat_pussy":
                for A in Actors:
                    A.mouth_Actions = [Action]
                    A.all_Actions.append(Action)

                for T in Targets:
                    T.clitoris_Actions = [Action]
                    T.all_Actions.append(Action)
            elif Action.Action_type in ["finger_ass"]:
                for A in Actors:
                    if Jean in Targets and Action.position == "doggy":
                        A.left_hand_Actions = [Action]
                    elif (Rogue in Targets or Laura in Targets) and Action.position == "doggy":
                        A.right_hand_Actions = [Action]
                    elif A.right_hand_Actions:
                        A.left_hand_Actions = [Action]
                    else:
                        A.right_hand_Actions = [Action]

                    A.all_Actions.append(Action)

                for T in Targets:
                    T.anus_Actions = [Action]
                    T.all_Actions.append(Action)
            elif Action.Action_type == "eat_ass":
                for A in Actors:
                    A.mouth_Actions = [Action]
                    A.all_Actions.append(Action)

                for T in Targets:
                    T.anus_Actions = [Action]
                    T.all_Actions.append(Action)
            elif Action.Action_type == "handjob":
                for A in Actors:
                    A.left_hand_Actions = [Action]
                    A.all_Actions.append(Action)

                for T in Targets:
                    T.cock_Actions = [Action]
                    T.all_Actions.append(Action)
            elif Action.Action_type == "fondle_balls":
                for A in Actors:
                    if A.right_hand_Actions:
                        A.left_hand_Actions = [Action]
                    else:
                        A.right_hand_Actions = [Action]
                        
                    A.all_Actions.append(Action)

                for T in Targets:
                    T.balls_Actions = [Action]
                    T.all_Actions.append(Action)
            elif Action.Action_type in ["blowjob", "deepthroat"]:
                for A in Actors:
                    A.mouth_Actions = [Action]
                    A.all_Actions.append(Action)

                for T in Targets:
                    T.cock_Actions = [Action]
                    T.all_Actions.append(Action)
            elif Action.Action_type == "suck_balls":
                for A in Actors:
                    A.mouth_Actions = [Action]
                    A.all_Actions.append(Action)

                for T in Targets:
                    T.balls_Actions = [Action]
                    T.all_Actions.append(Action)
            elif Action.Action_type in ["self_touch_pussy"]:
                for A in Actors:
                    A.right_hand_Actions = [Action]
                    A.all_Actions.append(Action)

                for T in Targets:
                    T.clitoris_Actions = [Action]
                    T.all_Actions.append(Action)
            elif Action.Action_type in ["self_finger_ass"]:
                for A in Actors:
                    A.right_hand_Actions = [Action]
                    A.all_Actions.append(Action)

                for T in Targets:
                    T.anus_Actions = [Action]
                    T.all_Actions.append(Action)
            elif Action.Action_type in ["self_dildo_pussy", "dildo_pussy"]:
                for A in Actors:
                    if A.right_hand_Actions:
                        A.left_hand_Actions = [Action]
                    else:
                        A.right_hand_Actions = [Action]

                    A.all_Actions.append(Action)

                for T in Targets:
                    T.vagina_Actions = [Action]
                    T.all_Actions.append(Action)
            elif Action.Action_type in ["self_dildo_ass", "dildo_ass"]:
                for A in Actors:
                    if A.right_hand_Actions:
                        A.left_hand_Actions = [Action]
                    else:
                        A.right_hand_Actions = [Action]

                    A.all_Actions.append(Action)

                for T in Targets:
                    T.anus_Actions = [Action]
                    T.all_Actions.append(Action)
            elif Action.Action_type in ["grind_pussy", "sex"]:
                for A in Actors:
                    A.cock_Actions = [Action]
                    A.all_Actions.append(Action)

                for T in Targets:
                    T.vagina_Actions = [Action]
                    T.all_Actions.append(Action)
            elif Action.Action_type in ["grind_ass", "anal"]:
                for A in Actors:
                    A.cock_Actions = [Action]
                    A.all_Actions.append(Action)

                for T in Targets:
                    T.anus_Actions = [Action]
                    T.all_Actions.append(Action)

        $ ongoing_Actions.append(Action)
        
        $ selected_Action_mode = Action.mode

        if Action.Action_type in ["sex", "anal"]:
            $ Player.dirty_cock = True

        $ temp_Action_Characters = list(set(Actors[:] + Targets[:]))

        python:
            for C in temp_Action_Characters:
                if not C.History.check(Action.Action_type, tracker = "recent"):
                    C.History.update(Action.Action_type)

                if C in all_Girls:
                    if C.History.check(Action.Action_type) % 10 == 1:
                        if Action.Action_type == "deepthroat" and C in Action.Actors:
                            C.throat_training += 1 if C.throat_training < 4 else 0
                        elif Action.Action_type in ["self_dildo_ass", "anal", "dildo_ass"] and C in Action.Targets:
                            C.anal_training += 1 if C.anal_training < 3 else 0

        if Action.Action_type == "deepthroat":
            $ Action.max_speed[0] *= Action.Actors[0].throat_training/4
            
            $ Action.max_intensity[0] *= Action.Actors[0].throat_training/4
        elif Action.Action_type in ["self_dildo_ass", "dildo_ass"]:
            $ Action.max_speed[0] *= Action.Targets[0].anal_training/3
        elif Action.Action_type == "anal":
            $ Action.max_speed[0] *= Action.Targets[0].anal_training/3
            $ Action.max_speed[1] *= Action.Targets[0].anal_training/3

            $ Action.max_intensity[1] *= Action.Targets[0].anal_training/3

        if not ongoing_Event or has_Action_control:
            call expression f"{Action.Action_type}_initiations" pass (Action = Action) from _call_expression_124

    return

label continue_Actions:
    $ selected_Event = EventScheduler.choose_Event(hooking_up = True)

    if selected_Event:
        call start_Event(selected_Event) from _call_start_Event_6
    else:
        python:
            unique_Actions = []

            for O in Player.all_Organs:
                Actions = getattr(Player, f"{O}_Actions")

                for A in Actions:
                    if Action not in unique_Actions:
                        unique_Actions.append(A)

            for G in active_Girls:
                for O in G.all_Organs:
                    Actions = getattr(G, f"{O}_Actions")

                    for A in Actions:
                        if Action not in unique_Actions:
                            unique_Actions.append(A)

        if ongoing_Actions:
            $ temp_sex_Characters = Present[:]

            call sex_faces(temp_sex_Characters) from _call_sex_faces

            $ temp_sex_Characters = Present[:]

            call sex_talk(temp_sex_Characters) from _call_sex_talk

            $ renpy.random.shuffle(unique_Actions)

            while unique_Actions:
                if unique_Actions[0].counter > 0:
                    call expression f"{unique_Actions[0].Action_type}_continuations" pass (Action = unique_Actions[0]) from _call_expression_101

                $ unique_Actions[0].counter += 1

                $ unique_Actions.remove(unique_Actions[0])

        $ temp_sex_Characters = Present[:]

        while temp_sex_Characters:            
            if temp_sex_Characters[0] in all_Girls and temp_sex_Characters[0].desire >= 100 and not temp_sex_Characters[0].orgasm_control:
                call Character_orgasms(temp_sex_Characters[0]) from _call_Character_orgasms
                
                return

            $ temp_sex_Characters.remove(temp_sex_Characters[0])

        if Player.desire >= 100 and not Player.orgasm_control:
            call Player_orgasms from _call_Player_orgasms
                
            return

    return

label stop_all_Actions(close_interface = False, automatic = False):
    if close_interface:
        hide screen Action_screen

        call closing_Action_interface from _call_closing_Action_interface_3

    $ belt_hidden = True
    $ Character_picker_disabled = True

    $ temp_Girls = Present[:]

    python:
        for C in all_NPCs:
            if C in temp_Girls:
                temp_Girls.remove(C)

    $ color_transform = get_color_transform(location = Player.location)

    while temp_Girls:
        $ stop_Actions(temp_Girls[0])

        if not automatic:
            call show_Character(temp_Girls[0], color_transform = color_transform) from _call_show_Character_2

        $ temp_Girls[0].Lovers = {}

        $ temp_Girls.remove(temp_Girls[0])

    $ stop_Actions(Player)

    $ Player.position = None

    $ Player.Lovers = {}

    if (not ongoing_Event or has_Action_control) and not automatic:
        $ needs_to_clean = False

        python:
            for location in focused_Girl.spunk.keys():
                if focused_Girl.spunk[location] and location != "mouth":
                    needs_to_clean = True

        if needs_to_clean:
            call clean_cum_mess(focused_Girl) from _call_clean_cum_mess

        $ renpy.pause(1.0, hard = True)

        $ temp_changing_Characters = Present[:]

        while temp_changing_Characters:
            call change_Outfit(temp_changing_Characters[0], temp_changing_Characters[0].Wardrobe.Outfits[temp_changing_Characters[0].Outfit.name]) from _call_change_Outfit_23

            $ temp_changing_Characters.remove(temp_changing_Characters[0])

    $ Player.naked = False
    $ Player.cock_out = False

    python:
        for C in Present:
            if C in all_Girls:
                if Player.location == C.home:
                    C.clothes_on_floor = False

            C.change_face()

    if Player.location == Player.home:
        $ Player.clothes_on_floor = False

    if black_screen:
        $ fade_in_from_black(0.4)

    $ belt_hidden = False
    $ Character_picker_disabled = False

    if close_interface:
        if not ongoing_Event and focused_Girl.location == Player.location:
            show screen interactions_screen(focused_Girl)
    else:
        $ belt_disabled = False

    return

label closing_Action_interface:
    $ Action_screen_showing = False

    $ has_progression_control = True
    $ has_Action_control = True
    $ has_position_control = True
    $ has_movement_control = True
    $ has_ejaculation_control = True

    $ speed = 1.0
    $ intensity = 1.0
    $ starting_depth = 0.0
    $ selected_Action_index = 0

    $ belt_hidden = False
    $ choice_disabled = False

    return