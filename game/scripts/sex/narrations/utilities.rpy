init python:
    
    import math

    def desire_increases(Characters):
        for C in Characters:
            if not C.stamina:
                if C == Player and C.cock_Actions:
                    renpy.say(None, "Looks like you're running on empty - maybe give yourself a break.")
            
                continue
            elif hookup_length < max_hookup_length*math.sqrt(C.max_stamina) or C.desire > 75:
                pass
            else:
                continue

            for A in C.all_Actions:
                base = eval(f"{C.tag}_base_Action_desire")*eval(f"{C.tag}_Action_desires['{A.Action_type}'][{int(C.desire/20 % 5)}]")

                modifier = 1.0

                if len(A.modes) > 1:
                    modifier *= (A.modes.index(A.mode) + 1)/len(A.modes)

                if A.speed:
                    modifier *= speed

                if C.History.check(A.Action_type, tracker = "weekly") >= boredom_threshold:
                    modifier *= boredom_penalty

                C.desire += base*modifier

            if C in all_Companions:
                if C.remote_vibrator is not None:
                    C.desire += int(2*C.remote_vibrator)

                C.check_statuses()

        return