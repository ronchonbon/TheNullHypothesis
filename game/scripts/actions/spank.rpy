label spank(Companion):
    show expression "images/effects/smack.webp" as smack onlayer effects:
        anchor (0.5, 0.5) pos (0.5, 0.6)

        zoom 0.0
        alpha 0.0
        ease 0.1 zoom 1.0 alpha 1.0
        ease 1.0 alpha 0.0

    with small_screenshake

    if approval_check(Companion, threshold = "spank"):
        if Companion.stamina:
            $ base = eval(f"{Companion.tag}_base_Action_desire")*eval(f"{Companion.tag}_Action_desires['spank'][{int(Companion.desire/20 % 5)}]")

            $ Companion.desire += base

        call spank_narrations(Companion)

        if not Companion.History.check("spank", tracker = "recent"):
            if not Companion.History.check("spank"):
                call expression f"{Companion.tag}_accepts_spank_first_time" from _call_expression_91
            elif Companion.History.check("spank") == 1:
                call expression f"{Companion.tag}_accepts_spank_second_time" from _call_expression_92
            elif approval_check(Companion, threshold = "love"):
                call expression f"{Companion.tag}_accepts_spank_love" from _call_expression_93
            else:
                call expression f"{Companion.tag}_accepts_spank" from _call_expression_94
    else:
        call spank_narrations(Companion)

        if Companion.History.check("rejected_spank", tracker = "recent") >= 2:
            call change_Companion_stat(Companion, "love", -5) from _call_change_Companion_stat_831
            call change_Companion_stat(Companion, "trust", -5) from _call_change_Companion_stat_832
            
            call expression f"{Companion.tag}_rejects_Action_asked_twice" from _call_expression_95
        elif Companion.History.check("rejected_spank", tracker = "recent") == 1:
            call change_Companion_stat(Companion, "love", -2) from _call_change_Companion_stat_833
            
            call expression f"{Companion.tag}_rejects_Action_asked_once" from _call_expression_96
        else:
            call expression f"{Companion.tag}_rejects_spank" from _call_expression_97

        $ Companion.History.update("rejected_spank")

    $ Companion.History.update("spank")

    return

label spank_narrations(Companion):
    if approval_check(Companion, threshold = "spank") and Companion.History.check("spank") >= 10:
        $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            "You deftly smack her ass, leaving a neat handprint."
        elif dice_roll == 2:
            "She jumps and lets out a small moan as your hand sends a ripple through her ass."
        elif dice_roll == 3:
            "You give her ass a good smack, and she shudders in pleasure from the impact."
    else:
        $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            "You give her ass a light smack."
        elif dice_roll == 2:
            "You gently slap her ass."

    return