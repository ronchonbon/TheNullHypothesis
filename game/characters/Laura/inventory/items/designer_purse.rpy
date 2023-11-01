label Laura_designer_purse_shopping_accept:
    $ Laura.change_face("confused1", eyes = "down")

    ch_Laura "Why is this bag so small and inconvenient?"

    $ Laura.change_face("confused1")

    ch_Player "It's a purse. . ."

    $ Laura.change_face("confused1", eyes = "down")

    pause 0.5

    $ Laura.change_face("confused1")

    ch_Laura ". . ."

    $ Laura.change_face("neutral")

    ch_Laura "I don't want it."

    return False

label Laura_designer_purse_shopping_reject:
    $ Laura.change_face("neutral")

    ch_Laura "I don't want it."

    return

label Laura_designer_purse_gift_accept:
    $ Laura.change_face("confused1", eyes = "down")

    ch_Laura "Why is this bag so small and inconvenient?"

    $ Laura.change_face("confused1")

    ch_Player "It's a purse. . ."

    $ Laura.change_face("confused1", eyes = "down")

    pause 0.5

    $ Laura.change_face("confused1")

    ch_Laura ". . ."

    $ Laura.change_face("neutral")

    ch_Laura "I don't want it."

    return False

label Laura_designer_purse_gift_reject:
    $ Laura.change_face("neutral")

    ch_Laura "I don't want it."

    return