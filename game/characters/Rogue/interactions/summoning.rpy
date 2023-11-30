label Rogue_summon_in_love:
    if Rogue.quirk:
        call receive_text(Rogue, "Yes!") from _call_receive_text_502
        call receive_text(Rogue, "I mean, of course I wanna") from _call_receive_text_503
        call receive_text(Rogue, "Be there as fast as I can") from _call_receive_text_504
    else:
        call receive_text(Rogue, "Sure!") from _call_receive_text_505
        call receive_text(Rogue, "Be there in a jiff") from _call_receive_text_506

    return

label Rogue_summon_in_relationship:
    call receive_text(Rogue, "Always down to hang with you") from _call_receive_text_507
    call receive_text(Rogue, "Be right there") from _call_receive_text_508

    return

label Rogue_summon_love_and_trust:
    call receive_text(Rogue, "Oh alright") from _call_receive_text_509
    call receive_text(Rogue, "Guess I can head over") from _call_receive_text_510

    return

label Rogue_summon_love:
    call receive_text(Rogue, "Well") from _call_receive_text_511
    call receive_text(Rogue, "Alright, I did wanna hang with ya") from _call_receive_text_512

    return

label Rogue_summon_trust:
    call receive_text(Rogue, "Sure") from _call_receive_text_513
    call receive_text(Rogue, "Heading over right now") from _call_receive_text_514

    return

label Rogue_summon_temporary:
    call receive_text(Rogue, "Guess I can") from _call_receive_text_515
    call receive_text(Rogue, "But not for long") from _call_receive_text_516

    return

label Rogue_summon_busy:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        call receive_text(Rogue, "Sorry [Rogue.Player_petname]") from _call_receive_text_517
        call receive_text(Rogue, "Bit busy right now") from _call_receive_text_518
    elif dice_roll == 2:
        call receive_text(Rogue, "Wish I could [Rogue.Player_petname]") from _call_receive_text_519
        call receive_text(Rogue, "Too busy") from _call_receive_text_520

    return

label Rogue_summon_busy_late:
    call receive_text(Rogue, "Bit late [Rogue.Player_petname]") from _call_receive_text_521

    return

label Rogue_summon_reject:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        call receive_text(Rogue, "Sorry") from _call_receive_text_522
        call receive_text(Rogue, "Not right now") from _call_receive_text_523
    elif dice_roll == 2:
        call receive_text(Rogue, "Maybe later?") from _call_receive_text_524
    elif dice_roll == 3:
        call receive_text(Rogue, "I wish") from _call_receive_text_525
        call receive_text(Rogue, "Sorry") from _call_receive_text_526

    return

label Rogue_summon_reject_asked_once:
    call receive_text(Rogue, "Did ya not see my last text?") from _call_receive_text_527

    return

label Rogue_summon_reject_asked_twice:
    call receive_text(Rogue, "The hell?") from _call_receive_text_528
    call receive_text(Rogue, "Just said no") from _call_receive_text_529

    return

label Rogue_summon_reject_mad:
    call receive_text(Rogue, "Ain't goin fuckin nowhere") from _call_receive_text_530

    return
    
label Rogue_dismiss_accept:
    menu:
        "Hey, you can leave if you want.":
            ch_Rogue "Alright, ah'll see you 'round then."
        "I think you should leave.":
            $ Rogue.change_face("worried1")

            ch_Rogue "But. . ."
            ch_Rogue "Okay, ah'll see you 'round. . ."

            call change_Companion_stat(Rogue, "love", 0) from _call_change_Companion_stat_779
        "Leave, give us some privacy." if len(Present) > 1:
            $ Rogue.change_face("worried1")

            ch_Rogue "Okay. . . sorry."

            call change_Companion_stat(Rogue, "love", 0) from _call_change_Companion_stat_780
        "Back":
            return False

    return True

label Rogue_dismiss_reject:
    menu:
        "Hey, you can leave if you want.":
            $ Rogue.change_face("confused1")

            ch_Rogue "Thanks. . ."

            $ Rogue.change_face("neutral")

            ch_Rogue "But ah think ah'll stick 'round."
        "I think you should leave.":
            $ Rogue.change_face("confused1")

            ch_Rogue "Ah'm good."

            call change_Companion_stat(Rogue, "love", 0) from _call_change_Companion_stat_781
        "Leave, give us some privacy." if len(Present) > 1:
            $ Rogue.change_face("angry1")

            ch_Rogue "Maybe if you asked polite-like."

            call change_Companion_stat(Rogue, "love", 0) from _call_change_Companion_stat_782
        "Back":
            return False

    return True

label Rogue_dismiss_reject_asked_once:
    $ Rogue.change_face("angry1")

    ch_Rogue "Ah already said ah'm not goin' anywhere."

    return

label Rogue_dismiss_reject_asked_twice:
    $ Rogue.change_face("appalled2")

    ch_Rogue "Are ya ignorin' me or somethin'?"

    if Player.location == Rogue.home:
        ch_Rogue "Get out."

        call getting_kicked_out(Rogue) from _call_getting_kicked_out_61

    return

label Rogue_dismiss_reject_mad:
    $ Rogue.change_face("appalled2")

    ch_Rogue "Ah'm already pissed off."
    ch_Rogue "Not goin' nowhere."

    return