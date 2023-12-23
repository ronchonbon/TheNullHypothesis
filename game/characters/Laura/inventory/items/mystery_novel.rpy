label Laura_mystery_novel_shopping_accept:
    $ Laura.change_face("confused1", eyes = "down")

    pause 1.0

    $ Laura.change_face("suspicious1")

    ch_Laura "Are you still trying to make me read more?"
    ch_Laura "No thanks."

    return False

label Laura_mystery_novel_shopping_reject:
    $ Laura.change_face("confused1", eyes = "down")

    ch_Laura "A book?"

    $ Laura.change_face("suspicious1")

    ch_Laura "I don't want it."

    return

label Laura_mystery_novel_gift_accept:
    $ Laura.change_face("confused1", eyes = "down")

    pause 1.0

    $ Laura.change_face("suspicious1")

    ch_Laura "Are you still trying to make me read more?"
    ch_Laura "No thanks."

    return False

label Laura_mystery_novel_gift_reject:
    $ Laura.change_face("confused1", eyes = "down")

    ch_Laura "A book?"

    $ Laura.change_face("suspicious1")

    ch_Laura "I don't want it."

    return