label Laura_remote_vibrator_shopping_accept:
    $ Laura.change_face("confused1")

    ch_Laura "Is this for. . . oh."

    $ Laura.change_face("smirk2")

    return True

label Laura_remote_vibrator_shopping_reject:
    $ Laura.change_face("angry1")

    ch_Laura "What even is that?"
    ch_Laura "Don't need it."

    return

label Laura_remote_vibrator_gift_accept:
    $ Laura.change_face("confused1")

    ch_Laura "Is this. . . oh."

    $ Laura.change_face("smirk2")

    return True

label Laura_remote_vibrator_gift_reject:
    $ Laura.change_face("angry1")

    ch_Laura "Don't know what it is, don't need it."

    return

label Laura_remote_vibrator_change:
    $ Laura.change_face("sexy")

    ch_Laura "Turn it up already."

    return

label Laura_remote_vibrator_change_reject:
    $ Laura.change_face("angry1")

    ch_Laura "Not happening."

    return