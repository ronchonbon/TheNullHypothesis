label spank(Character):
    show expression "images/effects/smack.webp" as smack onlayer effects:
        anchor (0.5, 0.5) pos (0.5, 0.6)

        zoom 0.0
        alpha 0.0
        ease 0.1 zoom 1.0 alpha 1.0
        ease 1.0 alpha 0.0

    with small_screenshake

    if approval_check(Character, threshold = "spank"):
        if Character.stamina:
            $ base = eval(f"{Character.tag}_base_Action_desire")*eval(f"{Character.tag}_Action_desires['spank'][{int(Character.desire/20 % 5)}]")

            call change_Character_stat(Character, "desire", base) from _call_change_Character_stat_23

        call spank_narrations(Character) from _call_spank_narrations

        if not Character.History.check("spank", tracker = "recent"):
            if not Character.History.check("spank"):
                call expression f"{Character.tag}_accepts_spank_first_time" from _call_expression_91
            elif Character.History.check("spank") == 1:
                call expression f"{Character.tag}_accepts_spank_second_time" from _call_expression_92
            elif approval_check(Character, threshold = "love"):
                call expression f"{Character.tag}_accepts_spank_love" from _call_expression_93
            else:
                call expression f"{Character.tag}_accepts_spank" from _call_expression_94
    else:
        call spank_narrations(Character) from _call_spank_narrations_1

        if Character.History.check("rejected_spank", tracker = "recent") >= 2:
            call change_Character_stat(Character, "love", -5) from _call_change_Character_stat_831
            call change_Character_stat(Character, "trust", -5) from _call_change_Character_stat_832
            
            call expression f"{Character.tag}_rejects_Action_asked_twice" from _call_expression_95
        elif Character.History.check("rejected_spank", tracker = "recent") == 1:
            call change_Character_stat(Character, "love", -2) from _call_change_Character_stat_833
            
            call expression f"{Character.tag}_rejects_Action_asked_once" from _call_expression_96
        else:
            call expression f"{Character.tag}_rejects_spank" from _call_expression_97

        $ Character.History.update("rejected_spank")

    $ Character.History.update("spank")

    return

label spank_narrations(Character):
    if approval_check(Character, threshold = "spank") and Character.History.check("spank") >= 10:
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