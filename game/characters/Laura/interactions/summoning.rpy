label Laura_summon_in_love:
    if Laura.History.check("seen_Player", tracker = "recent"):
        $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            call receive_text(Laura, "I'll follow your scent") from _call_receive_text_878
        elif dice_roll == 2:
            call receive_text(Laura, "Yes, I'm following") from _call_receive_text_879
        elif dice_roll == 3:
            call receive_text(Laura, "Yes, I wanted to come with you anyways") from _call_receive_text_880
    elif Laura.History.check("seen_Player", tracker = "last"):
        $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            call receive_text(Laura, "You want to be together more?") from _call_receive_text_881
            call receive_text(Laura, "Good") from _call_receive_text_882
        elif dice_roll == 2:
            call receive_text(Laura, "More time together is good") from _call_receive_text_883
        elif dice_roll == 3:
            call receive_text(Laura, "Sounds good") from _call_receive_text_884
    else:
        if Laura.check_traits("quirk"):
            $ dice_roll = renpy.random.randint(1, 4)
        else:
            $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            call receive_text(Laura, "Yes") from _call_receive_text_299
            call receive_text(Laura, "Wait for me, I'll be right there") from _call_receive_text_300
        elif dice_roll == 2:
            call receive_text(Laura, "Of course") from _call_receive_text_885
        elif dice_roll == 3:
            call receive_text(Laura, "Be right there") from _call_receive_text_886
        elif dice_roll == 4:
            call receive_text(Laura, "I know where you are") from _call_receive_text_297
            call receive_text(Laura, "Don't move") from _call_receive_text_298

    return

label Laura_summon_in_relationship:
    if Laura.History.check("seen_Player", tracker = "recent"):
        $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            call receive_text(Laura, "I'll follow your trail") from _call_receive_text_887
        elif dice_roll == 2:
            call receive_text(Laura, "Yes, I'm following") from _call_receive_text_888
        elif dice_roll == 3:
            call receive_text(Laura, "Yes, I wanted to come with you anyways") from _call_receive_text_889
    elif Laura.History.check("seen_Player", tracker = "last"):
        $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            call receive_text(Laura, "You want to be together more?") from _call_receive_text_890
            call receive_text(Laura, "Good") from _call_receive_text_891
        elif dice_roll == 2:
            call receive_text(Laura, "More time together is good") from _call_receive_text_892
        elif dice_roll == 3:
            call receive_text(Laura, "Sounds good") from _call_receive_text_893
    else:
        $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            call receive_text(Laura, "Be right there") from _call_receive_text_894
        elif dice_roll == 2:
            call receive_text(Laura, "Of course") from _call_receive_text_895
        elif dice_roll == 3:
            call receive_text(Laura, "Yes, I want to") from _call_receive_text_301
            call receive_text(Laura, "On my way") from _call_receive_text_302

    return

label Laura_summon_love_and_trust:
    if Laura.History.check("seen_Player", tracker = "recent"):
        $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            call receive_text(Laura, "Where are you leading me?") from _call_receive_text_896
            call receive_text(Laura, "Fine, coming") from _call_receive_text_897
        elif dice_roll == 2:
            call receive_text(Laura, "What?") from _call_receive_text_898
            call receive_text(Laura, "Fine, I will follow") from _call_receive_text_899
        elif dice_roll == 3:
            call receive_text(Laura, "Coming") from _call_receive_text_900
    elif Laura.History.check("seen_Player", tracker = "last"):
        $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            call receive_text(Laura, "Coming") from _call_receive_text_901
        elif dice_roll == 2:
            call receive_text(Laura, "Sure") from _call_receive_text_902
        elif dice_roll == 3:
            call receive_text(Laura, "Sounds good") from _call_receive_text_903
    else:
        $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            call receive_text(Laura, "Coming") from _call_receive_text_904
        elif dice_roll == 2:
            call receive_text(Laura, "Be right there") from _call_receive_text_905
        elif dice_roll == 3:
            call receive_text(Laura, "Fine, I'm coming") from _call_receive_text_303

    return

label Laura_summon_love:
    if Laura.History.check("seen_Player", tracker = "recent"):
        $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            call receive_text(Laura, "Where are you leading me?") from _call_receive_text_906
            call receive_text(Laura, "Fine, coming") from _call_receive_text_907
        elif dice_roll == 2:
            call receive_text(Laura, "What?") from _call_receive_text_908
            call receive_text(Laura, "Fine, I will follow") from _call_receive_text_909
        elif dice_roll == 3:
            call receive_text(Laura, "Coming") from _call_receive_text_910
    elif Laura.History.check("seen_Player", tracker = "last"):
        $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            call receive_text(Laura, "Coming") from _call_receive_text_911
        elif dice_roll == 2:
            call receive_text(Laura, "Sure") from _call_receive_text_912
        elif dice_roll == 3:
            call receive_text(Laura, "Sounds good") from _call_receive_text_913
    else:
        $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            call receive_text(Laura, "Coming") from _call_receive_text_914
        elif dice_roll == 2:
            call receive_text(Laura, "Be right there") from _call_receive_text_915
        elif dice_roll == 3:
            call receive_text(Laura, "Okay") from _call_receive_text_304
            call receive_text(Laura, "Coming") from _call_receive_text_305

    return

label Laura_summon_trust:
    if Laura.History.check("seen_Player", tracker = "recent"):
        $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            call receive_text(Laura, "Fine") from _call_receive_text_916
        elif dice_roll == 2:
            call receive_text(Laura, "Okay") from _call_receive_text_917
        elif dice_roll == 3:
            call receive_text(Laura, "Sure") from _call_receive_text_918
    elif Laura.History.check("seen_Player", tracker = "last"):
        $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            call receive_text(Laura, "Fine") from _call_receive_text_919
        elif dice_roll == 2:
            call receive_text(Laura, "Okay") from _call_receive_text_920
        elif dice_roll == 3:
            call receive_text(Laura, "Sure") from _call_receive_text_921
    else:
        $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            call receive_text(Laura, "Okay") from _call_receive_text_922
        elif dice_roll == 2:
            call receive_text(Laura, "Sure") from _call_receive_text_923
        elif dice_roll == 3:
            call receive_text(Laura, "Fine") from _call_receive_text_306
            call receive_text(Laura, "Wait for me") from _call_receive_text_307

    return

label Laura_summon_temporary:
    if Laura.History.check("seen_Player", tracker = "recent"):
        $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            call receive_text(Laura, "I suppose for a few minutes") from _call_receive_text_924
        elif dice_roll == 2:
            call receive_text(Laura, "Just for a sec") from _call_receive_text_925
        elif dice_roll == 3:
            call receive_text(Laura, "I can follow you for a little bit") from _call_receive_text_926
    elif Laura.History.check("seen_Player", tracker = "last"):
        $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            call receive_text(Laura, "I only have a few minutes") from _call_receive_text_927
        elif dice_roll == 2:
            call receive_text(Laura, "I can spare a little more time") from _call_receive_text_928
        elif dice_roll == 3:
            call receive_text(Laura, "Again? Quickly") from _call_receive_text_929
    else:
        $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            call receive_text(Laura, "Briefly") from _call_receive_text_930
        elif dice_roll == 2:
            call receive_text(Laura, "Just for a bit") from _call_receive_text_931
        elif dice_roll == 3:
            call receive_text(Laura, "For now") from _call_receive_text_308
            call receive_text(Laura, "Need to train later") from _call_receive_text_309

    return

label Laura_summon_busy:
    if Laura.behavior == "training":
        $ dice_roll = renpy.random.randint(1, 3)
    else:
        $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        call receive_text(Laura, "Busy") from _call_receive_text_310
    elif dice_roll == 2:
        call receive_text(Laura, "Can't") from _call_receive_text_932
    elif dice_roll == 3:
        call receive_text(Laura, "Not now, training") from _call_receive_text_311

    return

label Laura_summon_busy_late:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        call receive_text(Laura, "It's late") from _call_receive_text_312
    elif dice_roll == 2:
        call receive_text(Laura, "Too late") from _call_receive_text_933
    elif dice_roll == 3:
        call receive_text(Laura, "Tomorrow") from _call_receive_text_934

    return

label Laura_summon_reject:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        call receive_text(Laura, "I don't") from _call_receive_text_313
    elif dice_roll == 2:
        call receive_text(Laura, "Not right now") from _call_receive_text_314
    elif dice_roll == 3:
        call receive_text(Laura, "Can't") from _call_receive_text_315

    return

label Laura_summon_reject_asked_once:
    call receive_text(Laura, "Can't you read?") from _call_receive_text_316

    return

label Laura_summon_reject_asked_twice:
    call receive_text(Laura, "Stop.") from _call_receive_text_317

    return

label Laura_summon_reject_mad:
    call receive_text(Laura, "Leave me alone.") from _call_receive_text_318

    return
    
label Laura_dismiss_accept:
    menu:
        "Hey, you can leave if you want.":
            $ Laura.change_face("confused1")

            ch_Laura "No shit."

            $ Laura.change_face("neutral")

            ch_Laura "Bye."
        "I think you should leave.":
            call change_Character_stat(Laura, "love", -tiny_stat) from _call_change_Character_stat_498

            $ Laura.change_face("angry1")

            ch_Laura "Fine. . ."
        "Leave, give us some privacy." if len(Present) > 1:
            call change_Character_stat(Laura, "love", -tiny_stat) from _call_change_Character_stat_499

            $ Laura.change_face("appalled1")

            ch_Laura ". . ."
        "Back":
            return False

    return True

label Laura_dismiss_reject:
    menu:
        "Hey, you can leave if you want.":
            $ Laura.change_face("confused1")

            ch_Laura "Okay. . ."

            $ Laura.change_face("neutral")

            ch_Laura "Still not leaving.."
        "I think you should leave.":
            call change_Character_stat(Laura, "love", -tiny_stat) from _call_change_Character_stat_500

            $ Laura.change_face("angry1")

            ch_Laura "I'm fine right here."
        "Leave, give us some privacy." if len(Present) > 1:
            call change_Character_stat(Laura, "love", -tiny_stat) from _call_change_Character_stat_501

            $ Laura.change_face("appalled2")

            ch_Laura "Don't try and order me around."
        "Back":
            return False

    return True

label Laura_dismiss_reject_asked_once:
    $ Laura.change_face("angry1")

    ch_Laura "I'm not going anywhere."

    return

label Laura_dismiss_reject_asked_twice:
    $ Laura.change_face("appalled2")
    
    if Player.location == Laura.home:
        ch_Laura "You get out, now."

        call getting_kicked_out(Laura) from _call_getting_kicked_out_40
    else:
        ch_Laura "I'll make you leave if you keep asking."

    return

label Laura_dismiss_reject_mad:
    $ Laura.change_face("appalled2")

    ch_Laura "I'm not in the mood."

    return