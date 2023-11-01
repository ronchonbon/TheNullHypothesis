label Laura_accept_study:
    $ Laura.change_face("neutral")

    ch_Laura "Fine."

    return

label Laura_reject_study:
    $ Laura.change_face("neutral")

    ch_Laura "Nah."

    return

label Laura_reject_study_asked_once:

    return

label Laura_reject_study_asked_twice:        
    call getting_kicked_out(Laura) from _call_getting_kicked_out_39

    return

label Laura_accept_study_text:
    call receive_text(Laura, "Fine") from _call_receive_text_295

    return

label Laura_reject_study_text:
    call receive_text(Laura, "Rather not") from _call_receive_text_296

    return

label Laura_reject_study_asked_once_text:

    return

label Laura_reject_study_asked_twice_text:

    return