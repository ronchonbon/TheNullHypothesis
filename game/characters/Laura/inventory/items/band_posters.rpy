label Laura_band_posters_shopping_accept:
    $ Laura.change_face("surprised2")

    ch_Laura "Band posters?"

    $ Laura.change_face("worried1", eyes = "down", blush = 1)

    ch_Player "I've been paying attention to what music you like."
    ch_Player "And your walls are kind of bare. . ."

    $ Laura.change_face("worried1", blush = 1)

    pause 1.0

    $ Laura.change_face("angry1", eyes = "right", blush = 1)

    ch_Laura "I have started to enjoy music more and more. . ."
    ch_Laura "Thank you."

    $ Laura.change_face("angry1", eyes = "squint", blush = 1)

    return True

label Laura_band_posters_shopping_reject:

    return

label Laura_band_posters_gift_accept:
    $ Laura.change_face("surprised2")

    ch_Laura "Band posters?"

    $ Laura.change_face("worried1", eyes = "down", blush = 1)

    ch_Player "I've been paying attention to what music you like."
    ch_Player "And your walls are kind of bare. . ."

    $ Laura.change_face("worried1", blush = 1)

    pause 1.0

    $ Laura.change_face("angry1", eyes = "right", blush = 1)

    ch_Laura "I have started to enjoy music more and more. . ."
    ch_Laura "Thank you."

    $ Laura.change_face("angry1", eyes = "squint", blush = 1)

    return True

label Laura_band_posters_gift_reject:

    return