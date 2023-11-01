label spank(Girl):
    show expression "images/effects/smack.webp" as smack onlayer effects:
        anchor (0.5, 0.5) pos (0.5, 0.6)

        zoom 0.0
        alpha 0.0
        ease 0.1 zoom 1.0 alpha 1.0
        ease 1.0 alpha 0.0

    with small_screenshake

    call spank_narrations(Girl) from _call_spank_narrations

    $ Girl.History.update("spank")

    if approval_check(Girl, threshold = "spank"):
        if not Girl.History.check("spank"):
            call expression f"{Girl.tag}_accepts_spank_first_time" from _call_expression_91
        elif Girl.History.check("spank") == 1:
            call expression f"{Girl.tag}_accepts_spank_second_time" from _call_expression_92
        elif approval_check(Girl, threshold = "love"):
            call expression f"{Girl.tag}_accepts_spank_love" from _call_expression_93
        else:
            call expression f"{Girl.tag}_accepts_spank" from _call_expression_94
    else:
        if Girl.History.check("rejected_spank", tracker = "recent") >= 2:
            call change_Girl_stat(Girl, "love", -5) from _call_change_Girl_stat_831
            call change_Girl_stat(Girl, "trust", -5) from _call_change_Girl_stat_832
            
            call expression f"{Girl.tag}_rejects_Action_asked_twice" from _call_expression_95
        elif Girl.History.check("rejected_spank", tracker = "recent") == 1:
            call change_Girl_stat(Girl, "love", -2) from _call_change_Girl_stat_833
            
            call expression f"{Girl.tag}_rejects_Action_asked_once" from _call_expression_96
        else:
            call expression f"{Girl.tag}_rejects_spank" from _call_expression_97

        $ Girl.History.update("rejected_spank")

    return

label spank_narrations(Girl):
    if Girl.History.check("spank") >= 10:
        $ increase_Character_desire(Girl, 5, limit = 75)

        $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            "You deftly smack her ass, causing her to jump, and leaving a neat handprint."
        elif dice_roll == 2:
            "She jumps and lets out a small moan as your hand sends a ripple through her ass."
        elif dice_roll == 3:
            "You give her ass a good smack, and she shudders in pleasure from the impact."
    else:
        $ increase_Character_desire(Girl, 3, limit = 75)

        $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            "You smack her ass, maybe a bit too hard. . ."
        elif dice_roll == 2:
            "Your hand connects with her ass and she stiffens - it might've been a bit too hard."
        elif dice_roll == 3:
            "As you spank her, you still can't tell if it was too hard or too soft. . ."

    return