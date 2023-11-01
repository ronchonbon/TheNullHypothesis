label Jean_remote_vibrator_shopping_accept:
    $ Jean.change_face("surprised2")

    ch_Jean "Could be fun. . ."

    return True

label Jean_remote_vibrator_shopping_reject:
    $ Jean.change_face("appalled1")

    ch_Jean "Uhm, you're joking, right?"

    return

label Jean_remote_vibrator_gift_accept:
    $ Jean.change_face("surprised2")

    ch_Jean "Where's the remote. . . oh."
    
    $ Jean.change_face("smirk2")

    ch_Jean "Heh."

    return True

label Jean_remote_vibrator_gift_reject:
    $ Jean.change_face("appalled1")

    ch_Jean "This is a joke, right?"

    return

label Jean_remote_vibrator_change:
    $ Jean.change_face("sexy")

    ch_Jean "Tryna have some fun?"

    return

label Jean_remote_vibrator_change_reject:
    $ Jean.change_face("angry1")

    ch_Jean "No way."

    return