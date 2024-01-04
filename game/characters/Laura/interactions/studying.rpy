label Laura_accept_study:
    $ Laura.change_face("neutral")

    ch_Laura "Fine."

    return

label Laura_reject_study:
    $ Laura.change_face("neutral")

    ch_Laura "Nah."

    return

label Laura_reject_study_asked_once:
    call Laura_asked_once("busy")

    return

label Laura_reject_study_asked_twice:
    call Laura_asked_twice("busy")
    call Laura_kicking_out
    call getting_kicked_out(Laura) from _call_getting_kicked_out_39

    return

label Laura_accept_study_text:
    call receive_text(Laura, "Fine") from _call_receive_text_295

    return

label Laura_reject_study_text:
    call receive_text(Laura, "Rather not") from _call_receive_text_296

    return

label Laura_reject_study_asked_once_text:
    call Laura_asked_once_text("busy")

    return

label Laura_reject_study_asked_twice_text:
    call Laura_asked_twice_text("busy")

    return