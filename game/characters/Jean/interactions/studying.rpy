label Jean_accept_study:
    $ Jean.change_face("smirk2")

    ch_Jean "Okay!"

    return

label Jean_reject_study:
    $ Jean.change_face("worried1")

    ch_Jean "I wish. . ."
    ch_Jean "Another time?"

    return

label Jean_reject_study_asked_once:
    call Jean_asked_once("busy")
    
    return

label Jean_reject_study_asked_twice: 
    call Jean_asked_twice("busy")
    call Jean_kicking_out       
    call getting_kicked_out(Jean) from _call_getting_kicked_out_17

    return

label Jean_accept_study_text:
    call receive_text(Jean, "Ofc!") from _call_receive_text_65

    return

label Jean_reject_study_text:
    call receive_text(Jean, "Ugh I wish") from _call_receive_text_66
    call receive_text(Jean, "Maybe later?") from _call_receive_text_67
    call receive_text(Jean, "<3") from _call_receive_text_68

    return

label Jean_reject_study_asked_once_text:
    call Jean_asked_once_text("busy")

    return

label Jean_reject_study_asked_twice_text:
    call Jean_asked_twice_text("busy")

    return