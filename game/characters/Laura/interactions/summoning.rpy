label Laura_summon_in_love:
    if Laura.quirk:
        call receive_text(Laura, "I know where you are") from _call_receive_text_297
        call receive_text(Laura, "Don't move") from _call_receive_text_298
    else:
        call receive_text(Laura, "Yes") from _call_receive_text_299
        call receive_text(Laura, "Wait for me, I'll be right there") from _call_receive_text_300

    return

label Laura_summon_in_relationship:
    call receive_text(Laura, "Yes, I want to") from _call_receive_text_301
    call receive_text(Laura, "On my way") from _call_receive_text_302

    return

label Laura_summon_love_and_trust:
    call receive_text(Laura, "Fine, I'm coming") from _call_receive_text_303

    return

label Laura_summon_love:
    call receive_text(Laura, "Okay") from _call_receive_text_304
    call receive_text(Laura, "Coming") from _call_receive_text_305

    return

label Laura_summon_trust:
    call receive_text(Laura, "Fine") from _call_receive_text_306
    call receive_text(Laura, "Wait for me") from _call_receive_text_307

    return

label Laura_summon_temporary:
    call receive_text(Laura, "For now") from _call_receive_text_308
    call receive_text(Laura, "Need to train later") from _call_receive_text_309

    return

label Laura_summon_busy:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        call receive_text(Laura, "Busy") from _call_receive_text_310
    elif dice_roll == 2:
        call receive_text(Laura, "Not now, training") from _call_receive_text_311

    return

label Laura_summon_busy_late:
    call receive_text(Laura, "It's late") from _call_receive_text_312

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

    call change_Girl_stat(Laura, "love", -5) from _call_change_Girl_stat_497

    return

label Laura_summon_reject_asked_twice:
    call receive_text(Laura, "Stop.") from _call_receive_text_317

    return

label Laura_summon_reject_mad:
    call receive_text(Laura, "Fuck off.") from _call_receive_text_318

    return
    
label Laura_dismiss_accept:
    menu:
        "Hey, you can leave if you want.":
            $ Laura.change_face("confused1")

            ch_Laura "No shit."

            $ Laura.change_face("neutral")

            ch_Laura "Bye."
        "I think you should leave.":
            $ Laura.change_face("angry1")

            ch_Laura "Fine. . ."

            call change_Girl_stat(Laura, "love", -5) from _call_change_Girl_stat_498
        "Leave, give us some privacy." if len(Present) > 1:
            $ Laura.change_face("appalled1")

            ch_Laura ". . ."

            call change_Girl_stat(Laura, "love", -5) from _call_change_Girl_stat_499
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
            $ Laura.change_face("angry1")

            ch_Laura "I'm fine right here."

            call change_Girl_stat(Laura, "love", -5) from _call_change_Girl_stat_500
        "Leave, give us some privacy." if len(Present) > 1:
            $ Laura.change_face("appalled2")

            ch_Laura "Don't try and order me around."

            call change_Girl_stat(Laura, "love", -5) from _call_change_Girl_stat_501
        "Back":
            return False

    return True

label Laura_dismiss_reject_asked_once:
    $ Laura.change_face("angry1")

    ch_Laura "I'm not going anywhere."

    call change_Girl_stat(Laura, "love", -5) from _call_change_Girl_stat_502

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