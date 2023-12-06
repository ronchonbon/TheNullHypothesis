label Jean_summon_in_love:
    if Jean.quirk:
        call receive_text(Jean, "Missed your big sis?") from _call_receive_text_69
        call receive_text(Jean, "Of course you did") from _call_receive_text_70
        call receive_text(Jean, "I'll be right there <3") from _call_receive_text_71
    else:
        call receive_text(Jean, "Missed me?") from _call_receive_text_72
        call receive_text(Jean, "Of course I want to") from _call_receive_text_73
        call receive_text(Jean, "Be right there <3") from _call_receive_text_74

    return

label Jean_summon_in_relationship:
    call receive_text(Jean, "Duh I wanna hang out") from _call_receive_text_75
    call receive_text(Jean, "Omw") from _call_receive_text_76

    return

label Jean_summon_love_and_trust:
    call receive_text(Jean, "Okayyy") from _call_receive_text_77
    call receive_text(Jean, "Wasnt doing much anyway") from _call_receive_text_78

    return

label Jean_summon_love:
    call receive_text(Jean, "Want to hang with me?") from _call_receive_text_79
    call receive_text(Jean, "I guess I can head over <3") from _call_receive_text_80

    return

label Jean_summon_trust:
    call receive_text(Jean, "Well maybeee") from _call_receive_text_81
    call receive_text(Jean, "Fine, don't go anywhere") from _call_receive_text_82

    return

label Jean_summon_temporary:
    call receive_text(Jean, "For a little") from _call_receive_text_83
    call receive_text(Jean, "Got too much studying to do later") from _call_receive_text_84

    return

label Jean_summon_busy:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        call receive_text(Jean, "Studying") from _call_receive_text_85
        call receive_text(Jean, "Can't </3") from _call_receive_text_86
    elif dice_roll == 2:
        call receive_text(Jean, "Too much stuff to do today") from _call_receive_text_87
        call receive_text(Jean, "Sorry </3") from _call_receive_text_88

    return

label Jean_summon_busy_late:
    call receive_text(Jean, "Mmm, it's a bit late?") from _call_receive_text_89

    return

label Jean_summon_reject:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        call receive_text(Jean, "Not right now") from _call_receive_text_90
        call receive_text(Jean, "Sorryyy </3") from _call_receive_text_91
    elif dice_roll == 2:
        call receive_text(Jean, "Maybe after I study a bit more") from _call_receive_text_92
    elif dice_roll == 3:
        call receive_text(Jean, "If only") from _call_receive_text_93
        call receive_text(Jean, "Too much to do") from _call_receive_text_94

    return

label Jean_summon_reject_asked_once:
    call receive_text(Jean, "Read up, dummy") from _call_receive_text_95

    return

label Jean_summon_reject_asked_twice:
    call receive_text(Jean, "Okay now you're doing it on purpose") from _call_receive_text_96
    call receive_text(Jean, "Stop") from _call_receive_text_97

    return

label Jean_summon_reject_mad:
    call receive_text(Jean, "NO") from _call_receive_text_98
    call receive_text(Jean, ">:((((") from _call_receive_text_99

    return
    
label Jean_dismiss_accept:
    menu:
        "Hey, you can leave if you want.":
            $ Jean.change_face("confused1")

            ch_Jean "I know. . ."

            $ Jean.change_face("neutral")

            ch_Jean "I'm gonna head out for unrelated reasons. . ."
        "I think you should leave.":
            $ Jean.change_face("confused1")

            ch_Jean "Rude. . ."

            $ Jean.change_face("neutral")

            ch_Jean "Whatever, bye." 

            call change_Character_stat(Jean, "love", 0) from _call_change_Character_stat_251
        "Leave, give us some privacy." if len(Present) > 1:
            $ Jean.change_face("worried1") 

            ch_Jean "Don't have to be such an ass about it. . ." 

            call change_Character_stat(Jean, "love", 0) from _call_change_Character_stat_252
        "Back":
            return False

    return True

label Jean_dismiss_reject:
    menu:
        "Hey, you can leave if you want.":
            $ Jean.change_face("confused1") 

            ch_Jean "Why are you telling me that?" 

            $ Jean.change_face("neutral")

            ch_Jean "I still have stuff to do here."
        "I think you should leave.":
            $ Jean.change_face("confused1")

            ch_Jean "I think you should be nicer." 

            call change_Character_stat(Jean, "love", 0) from _call_change_Character_stat_253
        "Leave, give us some privacy." if len(Present) > 1:
            $ Jean.change_face("angry1") 

            ch_Jean "Really thought being rude would work?"

            call change_Character_stat(Jean, "love", 0) from _call_change_Character_stat_254
        "Back":
            return False

    return True

label Jean_dismiss_reject_asked_once:
    $ Jean.change_face("angry1") 

    ch_Jean "Don't ignore me."

    return

label Jean_dismiss_reject_asked_twice:
    $ Jean.change_face("appalled2")

    ch_Jean "I already said no!"
    
    if Player.location == Jean.home:
        ch_Jean "{i}You{/i} get out!"
        
        call getting_kicked_out(Jean) from _call_getting_kicked_out_18

    return

label Jean_dismiss_reject_mad:

    return