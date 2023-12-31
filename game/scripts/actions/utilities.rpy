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

    def get_conflicting_Actions(Action_type, Actors, Targets):
        if Action_type == "makeout":
            for A in Actors:
                if A.mouth_Actions:
                    return True

            for T in Targets:
                if T.mouth_Actions:
                    return True
        elif Action_type in ["choke"]:
            for A in Actors:
                if A.right_hand_Actions and A.left_hand_Actions:
                    return True

            for T in Targets:
                if T.neck_Actions:
                    return True
        elif Action_type in ["touch_thighs_over_clothes", "touch_thighs_higher_over_clothes", "touch_thighs", "touch_thighs_higher"]:
            for A in Actors:
                if A.right_hand_Actions and A.left_hand_Actions:
                    return True

            for T in Targets:
                if T.right_thigh_Actions and T.left_thigh_Actions:
                    return True
        elif Action_type in ["touch_breasts_over_clothes", "touch_breasts", "pinch_nipples"]:
            for A in Actors:
                if A.right_hand_Actions and A.left_hand_Actions:
                    return True

            for T in Targets:
                if T.right_breast_Actions and T.left_breast_Actions:
                    return True

                if T.right_nipple_Actions and T.left_nipple_Actions:
                    return True
        elif Action_type == "suck_nipples":
            for A in Actors:
                if A.mouth_Actions:
                    return True

            for T in Targets:
                if T.right_nipple_Actions and T.left_nipple_Actions:
                    return True
        elif Action_type in ["grab_ass_over_clothes", "grab_ass"]:
            for A in Actors:
                if A.right_hand_Actions and A.left_hand_Actions:
                    return True

            for T in Targets:
                if T.ass_Actions:
                    return True
        elif Action_type in ["touch_pussy_over_clothes", "touch_pussy", "vibrator"]:
            for A in Actors:
                if A.right_hand_Actions and A.left_hand_Actions:
                    return True

                if A.position not in ["69", "doggy"]:
                    for other_Action in A.cock_Actions:
                        return True

                    for other_Action in A.balls_Actions:
                        return True

            for T in Targets:
                if T.clitoris_Actions:
                    return True

                if T.remote_vibrator is not None:
                    return True
        elif Action_type == "finger_pussy":
            for A in Actors:
                if Jean in Targets and Jean.position == "doggy" and Jean.left_hand_Actions:
                    return True
                elif A.right_hand_Actions and A.left_hand_Actions:
                    return True

                if A.position not in ["69", "doggy"]:
                    for other_Action in A.cock_Actions:
                        return True

                    for other_Action in A.balls_Actions:
                        return True

            for T in Targets:
                if T.vagina_Actions:
                    return True

                if T.remote_vibrator is not None:
                    return True
        elif Action_type == "finger_ass":
            for A in Actors:
                if Jean in Targets and Jean.position == "doggy" and Jean.left_hand_Actions:
                    return True
                elif Rogue in Targets and Rogue.position == "doggy" and Rogue.right_hand_Actions:
                    return True
                elif Laura in Targets and Laura.position == "doggy" and Laura.right_hand_Actions:
                    return True
                elif A.right_hand_Actions and A.left_hand_Actions:
                    return True

                if A.position not in ["69", "doggy"]:
                    for other_Action in A.cock_Actions:
                        return True

                    for other_Action in A.balls_Actions:
                        return True

            for T in Targets:
                if T.anus_Actions:
                    return True

                if T.buttplug:
                    return True
        elif Action_type == "eat_pussy":
            for A in Actors:
                if A.mouth_Actions:
                    return True

                if A.position != "69":
                    for other_Action in A.cock_Actions:
                        return True

                    for other_Action in A.balls_Actions:
                        return True

            for T in Targets:
                if T.clitoris_Actions:
                    return True

                if T.vagina_Actions:
                    return True

                if T.remote_vibrator is not None:
                    return True
        elif Action_type == "eat_ass":
            for A in Actors:
                if A.mouth_Actions:
                    return True

                if A.position != "69":
                    for other_Action in A.cock_Actions:
                        return True

                    for other_Action in A.balls_Actions:
                        return True

            for T in Targets:
                if T.anus_Actions:
                    return True

                if T.buttplug:
                    return True
        elif Action_type == "handjob":
            for A in Actors:
                if A.left_hand_Actions:
                    return True

                for other_Action in A.all_Actions:
                    if other_Action.Action_type in job_Action_types:
                        return True

                if A.position != "69":
                    for other_Action in A.vagina_Actions:
                        return True

                    for other_Action in A.clitoris_Actions:
                        return True

                    for other_Action in A.anus_Actions:
                        return True

            for T in Targets:
                for other_Action in T.cock_Actions:
                    if other_Action.Action_type in insertion_Action_types or any(Target in Actors for Target in other_Action.Targets):
                        return True

                if T.position != "69":
                    for other_Action in T.mouth_Actions:
                        return True

                    if T.left_hand_Actions:
                        return True

                    if T.right_hand_Actions:
                        return True
        elif Action_type == "fondle_balls":
            for A in Actors:
                if A.right_hand_Actions and A.left_hand_Actions:
                    return True
                
                if A.position != "69":
                    for other_Action in A.vagina_Actions:
                        return True

                    for other_Action in A.clitoris_Actions:
                        return True

                    for other_Action in A.anus_Actions:
                        return True

            for T in Targets:
                if T.balls_Actions:
                    return True

                if T.position != "69":
                    for other_Action in T.mouth_Actions:
                        return True

                    if T.left_hand_Actions:
                        return True

                    if T.right_hand_Actions:
                        return True
        elif Action_type in ["blowjob", "deepthroat"]:
            for A in Actors:
                if A.mouth_Actions:
                    return True

                for other_Action in A.all_Actions:
                    if other_Action.Action_type in job_Action_types:
                        return True

                if A.position != "69":
                    for other_Action in A.vagina_Actions:
                        return True

                    for other_Action in A.clitoris_Actions:
                        return True

                    for other_Action in A.anus_Actions:
                        return True

                if A.position == "hands_and_knees":
                    if A.right_hand_Actions:
                        return True

            for T in Targets:
                for other_Action in T.cock_Actions:
                    if other_Action.Action_type in insertion_Action_types or any(Target in Actors for Target in other_Action.Targets):
                        return True

                if T.position != "69":
                    for other_Action in T.mouth_Actions:
                        return True

                    if T.left_hand_Actions:
                        return True

                    if T.right_hand_Actions:
                        return True
        elif Action_type == "suck_balls":
            for A in Actors:
                if A.mouth_Actions:
                    return True

                if A.position != "69":
                    for other_Action in A.vagina_Actions:
                        return True

                    for other_Action in A.clitoris_Actions:
                        return True

                    for other_Action in A.anus_Actions:
                        return True

            for T in Targets:
                if T.balls_Actions:
                    return True

                if T.position != "69":
                    for other_Action in T.mouth_Actions:
                        return True

                if T.left_hand_Actions:
                    return True

                if T.right_hand_Actions:
                    return True
        elif Action_type in ["self_touch_pussy"]:
            for A in Actors:
                if A.right_hand_Actions:
                    return True

            for T in Targets:
                if T.clitoris_Actions:
                    return True

                if T.remote_vibrator is not None:
                    return True
        elif Action_type in ["self_finger_ass"]:
            for A in Actors:
                if A.right_hand_Actions:
                    return True

            for T in Targets:
                if T.anus_Actions:
                    return True

                if T.buttplug:
                    return True
        elif Action_type in ["self_vibrator"]:
            for A in Actors:
                if A.right_hand_Actions and A.left_hand_Actions:
                    return True

            for T in Targets:
                if T.clitoris_Actions:
                    return True

                if T.remote_vibrator is not None:
                    return True
        elif Action_type in ["self_dildo_pussy", "dildo_pussy"]:
            for A in Actors:
                if A.right_hand_Actions and A.left_hand_Actions:
                    return True

            for T in Targets:
                if T.clitoris_Actions:
                    return True

                if T.vagina_Actions:
                    return True

                if T is not None:
                    return True
        elif Action_type in ["self_dildo_ass", "dildo_ass"]:
            for A in Actors:
                if A.right_hand_Actions and A.left_hand_Actions:
                    return True

            for T in Targets:
                if T.anus_Actions:
                    return True

                if T.buttplug:
                    return True
        elif Action_type in ["grind_pussy"]:
            for A in Actors:
                if A.cock_Actions:
                    return True

                if A.balls_Actions:
                    return True

                if A.position != "69":
                    for other_Action in A.mouth_Actions:
                        return True

            for T in Targets:
                if T.vagina_Actions:
                    return True

                if T.position == "doggy":
                    if T.anus_Actions:
                        return True

                T.remote_vibrator = None
        elif Action_type in ["sex"]:
            for A in Actors:
                if A.cock_Actions:
                    return True

                if A.balls_Actions:
                    return True

                if A.position != "69":
                    for other_Action in A.mouth_Actions:
                        return True

            for T in Targets:
                if T.vagina_Actions:
                    return True

                if T.remote_vibrator is not None:
                    return True
        elif Action_type in ["grind_ass"]:
            for A in Actors:
                if A.cock_Actions:
                    return True

                if A.balls_Actions:
                    return True

                if A.position != "69":
                    for other_Action in A.mouth_Actions:
                        return True

            for T in Targets:
                if T.anus_Actions:
                    return True

                if T.position == "doggy":
                    if T.vagina_Actions:
                        return True
        elif Action_type in ["anal"]:
            for A in Actors:
                if A.cock_Actions:
                    return True

                if A.balls_Actions:
                    return True

                if A.position != "69":
                    for other_Action in A.mouth_Actions:
                        return True

            for T in Targets:
                if T.anus_Actions:
                    return True

                if T.buttplug:
                    return True

        return False

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

                T.remote_vibrator = None
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

                T.remote_vibrator = None
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

                T.remote_vibrator = None
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

                T.remote_vibrator = None
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

                T.remote_vibrator = None
        elif Action_type in ["self_dildo_pussy", "dildo_pussy"]:
            for A in Actors:
                if A.right_hand_Actions and A.left_hand_Actions:
                    stop_Actions(A, organ = "left_hand")

            for T in Targets:
                stop_Actions(T, organ = "clitoris")
                stop_Actions(T, organ = "vagina")

                T.remote_vibrator = None
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

                T.remote_vibrator = None
        elif Action_type in ["sex"]:
            for A in Actors:
                stop_Actions(A, organ = "cock")
                stop_Actions(A, organ = "balls")

                if A.position != "69":
                    for other_Action in A.mouth_Actions:
                        stop_Action(other_Action)

            for T in Targets:
                stop_Actions(T, organ = "vagina")

                T.remote_vibrator = None
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
        Characters = list(set(Action.Actors[:] + Action.Targets[:]))

        if remove_Player and Player in Characters:
            Characters.remove(Player)

        return Characters

    def get_hookup_summary():
        total_Character_orgasms = 0
        total_Player_orgasms = 0
        total_unique_Actions = 0

        for C in Present:
            total_Character_orgasms += C.History.check("orgasmed_with_Player", tracker = "recent")

        total_Player_orgasms = Player.History.check("orgasmed", tracker = "recent")

        for Action_type in all_Action_types:
            if Player.History.check(Action_type, tracker = "recent"):
                total_unique_Actions += 1
            else:
                for C in Present:
                    if C.History.check(Action_type, tracker = "recent"):
                        total_unique_Actions += 1
                        
                        break

        score = total_Character_orgasms*(1.0 + 0.1*total_unique_Actions) + 0.5*total_Player_orgasms

        return total_Character_orgasms, total_Player_orgasms, total_unique_Actions, score

    def check_for_clothed_Actions(Character):
        for A in Character.all_Actions:
            if A.Action_type in ["touch_thighs_over_clothes", "touch_thighs_higher_over_clothes"] and not Character.thighs_covered:
                stop_Action(A)
            elif A.Action_type == "touch_breasts_over_clothes" and not Character.breasts_covered:
                stop_Action(A)
            elif A.Action_type == "touch_pussy_over_clothes" and not Character.pussy_covered:
                stop_Action(A)
            elif A.Action_type == "grab_ass_over_clothes" and not Character.ass_covered:
                stop_Action(A)
            elif A.Action_type in ["touch_thighs", "touch_thighs_higher"] and Character.thighs_covered:
                stop_Action(A)
            elif A.Action_type in ["touch_breasts", "pinch_nipples", "suck_nipples"] and Character.breasts_covered:
                stop_Action(A)
            elif A.Action_type in ["touch_pussy", "finger_pussy", "eat_pussy", "self_touch_pussy", "self_vibrator", "self_dildo_pussy", "sex", "vibrator", "dildo_pussy"] and Character.pussy_covered:
                stop_Action(A)
            elif A.Action_type in ["finger_ass", "eat_ass", "self_finger_ass", "self_dildo_ass", "anal", "dildo_ass"] and Character.anus_covered:
                stop_Action(A)

        return

label start_Action(Action, initiator = None):
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

        $ renpy.dynamic(temp_Characters = Targets[:])
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

        $ renpy.dynamic(temp_Characters = Actors[:])

    $ proceed = True

    if (not ongoing_Event or has_Action_control) and proceed:
        while temp_Characters:
            $ Clothing_to_remove = []

            python:
                for Clothing_type in reversed(removable_Clothing_types):
                    if temp_Characters[0].Clothes[Clothing_type].string and Action.position not in temp_Characters[0].Clothes[Clothing_type].available_states.keys():
                        Clothing_to_remove.append(temp_Characters[0].Clothes[Clothing_type])

            if Clothing_to_remove:
                call does_Character_agree_to_change_Clothes(temp_Characters[0], removed_Items = Clothing_to_remove, automatic = True) from _call_does_Character_agree_to_change_Clothes_1

                $ proceed = _return

            if proceed:
                if temp_Characters[0].position != Action.position:
                    call request_position(temp_Characters[0], Action.position) from _call_request_position_10

                pause 0.5

                $ Clothing_to_remove = []
                $ Clothing_to_undress = []
                $ undressed_states = []

                python:
                    for Clothing_type in reversed(removable_Clothing_types):
                        if temp_Characters[0].Clothes[Clothing_type].string and Action.position in temp_Characters[0].Clothes[Clothing_type].available_states.keys():
                            if Action.Action_type in ["touch_thighs", "touch_thighs_higher"]:
                                if "thighs" in temp_Characters[0].Clothes[Clothing_type].covers[Action.position].keys():
                                    current_state = temp_Characters[0].Clothes[Clothing_type].state

                                    while current_state in temp_Characters[0].Clothes[Clothing_type].covers[Action.position]["thighs"] and current_state <= temp_Characters[0].Clothes[Clothing_type].available_states[Action.position][-1]:
                                        current_state += 1

                                    if current_state not in temp_Characters[0].Clothes[Clothing_type].available_states[Action.position]:
                                        Clothing_to_remove.append(temp_Characters[0].Clothes[Clothing_type])
                                    else:
                                        Clothing_to_undress.append(temp_Characters[0].Clothes[Clothing_type])
                                        undressed_states.append(current_state)
                            elif Action.Action_type in ["touch_breasts", "pinch_nipples", "suck_nipples"]:
                                if "breasts" in temp_Characters[0].Clothes[Clothing_type].covers[Action.position].keys():
                                    current_state = temp_Characters[0].Clothes[Clothing_type].state

                                    while current_state in temp_Characters[0].Clothes[Clothing_type].covers[Action.position]["breasts"] and current_state <= temp_Characters[0].Clothes[Clothing_type].available_states[Action.position][-1]:
                                        current_state += 1

                                    if current_state not in temp_Characters[0].Clothes[Clothing_type].available_states[Action.position]:
                                        Clothing_to_remove.append(temp_Characters[0].Clothes[Clothing_type])
                                    else:
                                        Clothing_to_undress.append(temp_Characters[0].Clothes[Clothing_type])
                                        undressed_states.append(current_state)
                            elif Action.Action_type in ["touch_pussy", "finger_pussy", "eat_pussy", "self_touch_pussy", "self_vibrator", "self_dildo_pussy", "sex", "vibrator", "dildo_pussy"]:
                                if "pussy" in temp_Characters[0].Clothes[Clothing_type].covers[Action.position].keys():
                                    current_state = temp_Characters[0].Clothes[Clothing_type].state

                                    while current_state in temp_Characters[0].Clothes[Clothing_type].covers[Action.position]["pussy"] and current_state <= temp_Characters[0].Clothes[Clothing_type].available_states[Action.position][-1]:
                                        current_state += 1

                                    if current_state not in temp_Characters[0].Clothes[Clothing_type].available_states[Action.position]:
                                        Clothing_to_remove.append(temp_Characters[0].Clothes[Clothing_type])
                                    else:
                                        Clothing_to_undress.append(temp_Characters[0].Clothes[Clothing_type])
                                        undressed_states.append(current_state)
                            elif Action.Action_type in ["finger_ass", "eat_ass", "self_finger_ass", "self_dildo_ass", "anal", "dildo_ass"]:
                                if "anus" in temp_Characters[0].Clothes[Clothing_type].covers[Action.position].keys():
                                    current_state = temp_Characters[0].Clothes[Clothing_type].state

                                    while current_state in temp_Characters[0].Clothes[Clothing_type].covers[Action.position]["anus"] and current_state <= temp_Characters[0].Clothes[Clothing_type].available_states[Action.position][-1]:
                                        current_state += 1

                                    if current_state not in temp_Characters[0].Clothes[Clothing_type].available_states[Action.position]:
                                        Clothing_to_remove.append(temp_Characters[0].Clothes[Clothing_type])
                                    else:
                                        Clothing_to_undress.append(temp_Characters[0].Clothes[Clothing_type])
                                        undressed_states.append(current_state)

                if Clothing_to_remove or Clothing_to_undress:
                    call does_Character_agree_to_change_Clothes(temp_Characters[0], removed_Items = Clothing_to_remove, undressed_Items = Clothing_to_undress, undressed_states = undressed_states, automatic = True) from _call_does_Character_agree_to_change_Clothes_2

                    $ proceed = _return

            $ temp_Characters.remove(temp_Characters[0])

    if proceed:
        if Action.Action_type in cock_Action_types:
            $ Player.naked = True
            $ Player.cock_out = True

            $ renpy.dynamic(temp_Characters = Present[:])

            while temp_Characters:
                if not temp_Characters[0].History.check("seen_Player_naked"):
                    $ EventScheduler.Events[f"{temp_Characters[0].tag}_seeing_penis"].start()

                $ temp_Characters[0].History.update("seen_Player_naked")
                
                $ temp_Characters.remove(temp_Characters[0])

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

        if Action.Action_type == "deepthroat":
            $ Player.saliva = True

        if Action.Action_type == "sex":
            $ Player.grool = True

        if Action.Action_type == "anal":
            $ Player.dirty_cock = True

        if not Player.History.check(Action.Action_type, tracker = "recent"):
            $ Player.History.update(Action.Action_type)

        if Action.Action_type in ["blowjob", "deepthroat"] and Player.dirty_cock:
            $ Player.History.update("ass_to_mouth")

        $ renpy.dynamic(temp_Characters = list(set(Actors[:] + Targets[:])))

        python:
            for C in temp_Characters:
                if not C.History.check(Action.Action_type, tracker = "recent"):
                    C.History.update(Action.Action_type)

                if C in all_Companions:
                    if C.History.check(Action.Action_type) % 10 == 1:
                        if Action.Action_type == "deepthroat" and C in Action.Actors:
                            C.throat_training += 1 if C.throat_training < 4 else 0
                        elif Action.Action_type in ["self_dildo_ass", "anal", "dildo_ass"] and C in Action.Targets:
                            C.anal_training += 1 if C.anal_training < 3 else 0

                    check_for_clothed_Actions(C)

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
            $ has_stamina = True

            python:
                for C in temp_Characters:
                    if not C.stamina:
                        if C == Player and Action.Action_type in cock_Action_types:
                            has_stamina = False
                        elif C in all_Companions:
                            has_stamina = False 

            if has_stamina:
                call expression f"{Action.Action_type}_initiations" pass (Action = Action) from _call_expression_124

    return

label continue_Actions:
    $ hookup_length += 1

    $ selected_Event = EventScheduler.choose_Event(hooking_up = True)

    if selected_Event:
        call start_Event(selected_Event) from _call_start_Event_6
    else:
        $ renpy.dynamic(temp_Actions = [])

        python:
            for A in Player.all_Actions:
                if A not in temp_Actions:
                    temp_Actions.append(A)

            for G in Present:
                for A in G.all_Actions:
                    if A not in temp_Actions:
                        temp_Actions.append(A)

        if not Player.stamina and Player.cock_Actions:
            $ temp_Actions.remove(Player.cock_Actions[0])

        python:
            for G in Present:
                if not G.stamina:
                    for A in G.all_Actions:
                        if A in temp_Actions and A not in Player.cock_Actions:
                            temp_Actions.remove(A)

        if ongoing_Actions:
            $ sex_faces(Present[:])
            $ desire_increases([Player] + Present[:])

            $ renpy.random.shuffle(temp_Actions)

            while temp_Actions:
                if temp_Actions[0].counter > 0:
                    $ not_warmed_up_Character = None
                    $ bored_Character = None

                    $ renpy.dynamic(temp_Characters = get_Action_Characters(temp_Actions[0]))

                    while temp_Characters:
                        if temp_Actions[0].counter % boredom_threshold == 0:
                            $ temp_Characters[0].History.update(temp_Actions[0].Action_type)

                        if temp_Characters[0] in all_Companions:
                            if temp_Characters[0].desire < eval(f"{temp_Characters[0].tag}_Action_desire_thresholds['{temp_Actions[0].Action_type}']"):
                                $ not_warmed_up_Character = temp_Characters[0]

                            if temp_Characters[0].History.check(temp_Actions[0].Action_type, tracker = "weekly") >= boredom_threshold:
                                $ bored_Character = temp_Characters[0]

                        $ temp_Characters.remove(temp_Characters[0])

                    if not_warmed_up_Character and renpy.random.random() > 0.25:
                        call expression f"{not_warmed_up_Character.tag}_not_warmed_up_for_Action" pass (Action = temp_Actions[0]) from _call_expression_80
                    elif bored_Character and renpy.random.random() > 0.75:
                        call expression f"{bored_Character.tag}_bored_by_Action" pass (Action = temp_Actions[0]) from _call_expression_81
                    else:
                        call expression f"{temp_Actions[0].Action_type}_continuations" pass (Action = temp_Actions[0]) from _call_expression_101

                $ temp_Actions[0].counter += 1

                $ temp_Actions.remove(temp_Actions[0])

            $ sex_faces(Present[:])
            $ sex_talk(Present[:])

        $ renpy.dynamic(temp_Characters = Present[:])

        while temp_Characters:            
            if temp_Characters[0] in all_Companions and temp_Characters[0].desire >= 100:
                call Character_orgasms(temp_Characters[0]) from _call_Character_orgasms
                
                return

            $ renpy.dynamic(temp_Action_types = passive_Action_types[:])

            python:
                for Action_type in toy_Action_types:
                    if Action_type in temp_Action_types:
                        if Action_type in dildo_Action_types and not ("dildo" in Player.inventory.keys() or "dildo" in temp_Characters[0].inventory.keys()):
                            temp_Action_types.remove(Action_type)
                        elif Action_type in ["self_vibrator", "vibrator"] and not ("vibrator" in Player.inventory.keys() or "vibrator" in temp_Characters[0].inventory.keys()):
                            temp_Action_types.remove(Action_type)

            while temp_Action_types:
                $ renpy.dynamic(temp_Action = None)

                if temp_Characters[0] in all_Companions and temp_Characters[0].desire >= eval(f"{temp_Characters[0].tag}_Action_desire_thresholds['{temp_Action_types[0]}']") and temp_Characters[0].History.check(temp_Action_types[0]):
                    if renpy.random.random() > 0.5:
                        if "self" in temp_Action_types[0] and not get_conflicting_Actions(temp_Action_types[0], [temp_Characters[0]], [temp_Characters[0]]):
                            $ temp_Action = ActionClass(temp_Action_types[0], temp_Characters[0], temp_Characters[0])
                        elif "self" not in temp_Action_types[0] and not get_conflicting_Actions(temp_Action_types[0], [temp_Characters[0]], [Player]):
                            $ temp_Action = ActionClass(temp_Action_types[0], temp_Characters[0], Player)

                        if temp_Action and temp_Characters[0].position in Action.available_poses:
                            call start_Action(temp_Action, initiator = temp_Characters[0]) from _call_start_Action

                $ temp_Action_types.remove(temp_Action_types[0])

            $ temp_Characters.remove(temp_Characters[0])

        if Player.desire >= 100:
            call Player_orgasms from _call_Player_orgasms
                
            return

    return

label stop_all_Actions(close_interface = True, automatic = False, summary = False):
    if close_interface:
        hide screen Action_screen

        call closing_Action_interface from _call_closing_Action_interface_3

    $ belt_hidden = True
    $ Character_picker_disabled = True

    $ renpy.dynamic(temp_Characters = Present[:])

    python:
        for C in all_NPCs:
            if C in temp_Characters:
                temp_Characters.remove(C)

    while temp_Characters:
        $ stop_Actions(temp_Characters[0])

        if summary:
            $ temp_Characters[0].change_face("sexy")
            $ temp_Characters[0].change_arms("neutral")

        if not automatic:
            call show_Character(temp_Characters[0]) from _call_show_Character_2

        $ temp_Characters[0].Lovers = {}

        $ temp_Characters.remove(temp_Characters[0])

    $ stop_Actions(Player)

    $ Player.position = None

    $ Player.Lovers = {}

    if (not ongoing_Event or has_Action_control) and not automatic:
        $ needs_to_clean = []

        python:
            for C in Present:
                for location in C.spunk.keys():
                    if C.spunk[location] and location != "mouth":
                        needs_to_clean.append(C)

        while needs_to_clean:
            call clean_cum_mess(needs_to_clean[0]) from _call_clean_cum_mess

            $ needs_to_clean.remove(needs_to_clean[0])

        $ renpy.pause(1.0, hard = True)

        $ renpy.dynamic(temp_Characters = Present[:])

        while temp_Characters:
            call change_Outfit(temp_Characters[0], temp_Characters[0].Wardrobe.Outfits[temp_Characters[0].Outfit.name]) from _call_change_Outfit_23

            $ temp_Characters.remove(temp_Characters[0])

    $ Player.naked = False
    $ Player.cock_out = False

    python:
        for C in Present:
            if C in all_Companions:
                if Player.location == C.home:
                    C.clothes_on_floor = False

    if Player.location == Player.home:
        $ Player.clothes_on_floor = False

    # if black_screen:
    #     $ fade_in_from_black(0.4)

    $ belt_hidden = False
    $ Character_picker_disabled = False

    if close_interface:
        if not ongoing_Event:
            if focused_Character and focused_Character.location == Player.location:
                if summary:
                    $ total_Character_orgasms, total_Player_orgasms, total_unique_Actions, score = get_hookup_summary()

                    if "sex" not in Player.scores.keys():
                        $ Player.scores["sex"] = {}

                    if focused_Character not in Player.scores["sex"].keys():
                        $ Player.scores["sex"][focused_Character] = {}

                    if day in Player.scores["sex"][focused_Character].keys():
                        $ temp = Player.scores["sex"][focused_Character][day]
                    else:
                        $ temp = []

                    $ temp.append(score)
                    
                    $ Player.scores["sex"][focused_Character].update({day: temp})

                    call change_Character_stat(focused_Character, "love", orgasm_bonus*score) from _call_change_Character_stat_350
                    call expression f"{focused_Character.tag}_hookup_summary" pass (total_Character_orgasms = total_Character_orgasms, total_Player_orgasms = total_Player_orgasms, total_unique_Actions = total_unique_Actions, score = score) from _call_expression_87
                    
                    call screen grade_screen(total_Character_orgasms, total_Player_orgasms, total_unique_Actions, score)

                show screen interactions_screen(focused_Character)
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

    $ belt_hidden = False
    $ choice_disabled = False

    return