label Laura_motorcycle_helmet_shopping_accept:
    $ Laura.change_face("confused1", eyes = "down")

    ch_Laura "A. . . helmet?"

    $ Laura.change_face("surprised2")

    ch_Player "It's for riding motorcycles."

    $ Laura.change_face("angry1", eyes = "right", blush = 1)

    ch_Player "Doesn't Logan have one?"
    ch_Player "Now you can go for a ride. Your eyes always light up with this kind of stuff."
    ch_Laura "But you don't have a motorcycle."

    $ Laura.change_face("angry1", eyes = "squint", blush = 1)

    ch_Laura "I don't want to ride with Logan. . ."

    $ Laura.change_face("confused1", eyes = "down", blush = 1)

    ch_Laura "Thank you."

    $ Laura.change_face("angry1", eyes = "right", blush = 1)

    ch_Laura "I have been wondering what it's like."

    call change_Girl_stat(Laura, "love", 0) from _call_change_Girl_stat_1465
    call change_Girl_stat(Laura, "trust", 0) from _call_change_Girl_stat_1466

    return True

label Laura_motorcycle_helmet_shopping_reject:

    return

label Laura_motorcycle_helmet_gift_accept:
    $ Laura.change_face("confused1", eyes = "down")

    ch_Laura "A. . . helmet?"

    $ Laura.change_face("surprised2")

    ch_Player "It's for riding motorcycles."

    $ Laura.change_face("angry1", eyes = "right", blush = 1)

    ch_Player "Doesn't Logan have one?"
    ch_Player "Now you can go for a ride. Your eyes always light up with this kind of stuff."
    ch_Laura "But you don't have a motorcycle."

    $ Laura.change_face("angry1", eyes = "squint", blush = 1)

    ch_Laura "I don't want to ride with Logan. . ."

    $ Laura.change_face("confused1", eyes = "down", blush = 1)

    ch_Laura "Thank you."

    $ Laura.change_face("angry1", eyes = "right", blush = 1)

    ch_Laura "I have been wondering what it's like."

    call change_Girl_stat(Laura, "love", 0) from _call_change_Girl_stat_1467
    call change_Girl_stat(Laura, "trust", 0) from _call_change_Girl_stat_1468

    return True

label Laura_motorcycle_helmet_gift_reject:

    return