label Laura_accept_study:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        $ Laura.change_face("neutral")

        ch_Laura "Fine."
    elif dice_roll == 2:
        $ Laura.change_face("neutral")

        ch_Laura "Must we?"

        $ Laura.mouth = "frown"

        ch_Laura ". . . Fine."
    elif dice_roll == 3:
        $ Laura.change_face("neutral", eyes = "right")

        ch_Laura "If we must."

    return

label Laura_reject_study:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        $ Laura.change_face("neutral")

        ch_Laura "Nah."
    elif dice_roll == 2:
        $ Laura.change_face("neutral")

        ch_Laura "Not interested."
    elif dice_roll == 3:
        $ Laura.change_face("neutral")

        ch_Laura "Sounds boring."

    return

label Laura_reject_study_asked_once:
    call Laura_asked_once("busy") from _call_Laura_asked_once_11

    return

label Laura_reject_study_asked_twice:
    call Laura_asked_twice("busy") from _call_Laura_asked_twice_11
    call Laura_kicking_out from _call_Laura_kicking_out_14
    call getting_kicked_out(Laura) from _call_getting_kicked_out_39

    return

label Laura_accept_study_text:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        call receive_text(Laura, "Fine") from _call_receive_text_295
    elif dice_roll == 2:
        call receive_text(Laura, "I guess") from _call_receive_text_1218
        call receive_text(Laura, "I'll meet you there") from _call_receive_text_1219
    elif dice_roll == 3:
        call receive_text(Laura, "Okay") from _call_receive_text_1220

    return

label Laura_reject_study_text:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        call receive_text(Laura, "Rather not") from _call_receive_text_296
    elif dice_roll == 2:
        call receive_text(Laura, "Why would I want to study right now?") from _call_receive_text_1221
    elif dice_roll == 3:
        call receive_text(Laura, "No") from _call_receive_text_1222

    return

label Laura_reject_study_asked_once_text:
    call Laura_asked_once_text("busy") from _call_Laura_asked_once_text

    return

label Laura_reject_study_asked_twice_text:
    call Laura_asked_twice_text("busy") from _call_Laura_asked_twice_text

    return