label Laura_teddy_bear_shopping_accept:
    $ Laura.change_face("confused1", eyes = "down")

    ch_Laura "A. . . stuffed animal?"

    $ Laura.change_face("confused3")

    ch_Player "Don't you know what a 'teddy bear' is?"

    $ Laura.change_face("angry1", eyes = "right", blush = 1)

    ch_Laura "I assume it's this thing."
    ch_Laura "I've never owned a stuffed animal before."

    $ Laura.change_face("confused2", blush = 1)

    ch_Laura "What are you supposed to do with it?"
    ch_Player "That's up to you."
    ch_Player "I figured you could snuggle with it in bed."

    $ Laura.change_face("confused1", eyes = "down", blush = 1)

    ch_Laura "'Snuggle'?"

    $ Laura.change_face("angry1", eyes = "right", blush = 1)

    ch_Laura "I don't snuggle. . ."
    ch_Laura "But, thank you."

    call change_Girl_stat(Laura, "love", 30) from _call_change_Girl_stat_1485
    call change_Girl_stat(Laura, "trust", 15) from _call_change_Girl_stat_1486

    return True

label Laura_teddy_bear_shopping_reject:
    $ Laura.change_face("confused1", eyes = "down")

    ch_Laura "A. . . stuffed animal?"

    $ Laura.change_face("confused3")

    ch_Laura "No."

    return

label Laura_teddy_bear_gift_accept:
    $ Laura.change_face("confused1", eyes = "down")

    ch_Laura "A. . . stuffed animal?"

    $ Laura.change_face("confused3")

    ch_Player "Don't you know what a 'teddy bear' is?"

    $ Laura.change_face("angry1", eyes = "right", blush = 1)

    ch_Laura "I assume it's this thing."
    ch_Laura "I've never owned a stuffed animal before."

    $ Laura.change_face("confused2", blush = 1)

    ch_Laura "What are you supposed to do with it?"
    ch_Player "That's up to you."
    ch_Player "I figured you could snuggle with it in bed."

    $ Laura.change_face("confused1", eyes = "down", blush = 1)

    ch_Laura "'Snuggle'?"

    $ Laura.change_face("angry1", eyes = "right", blush = 1)

    ch_Laura "I don't snuggle. . ."
    ch_Laura "But, thank you."

    call change_Girl_stat(Laura, "love", 30) from _call_change_Girl_stat_1487
    call change_Girl_stat(Laura, "trust", 15) from _call_change_Girl_stat_1488

    return True

label Laura_teddy_bear_gift_reject:
    $ Laura.change_face("confused1", eyes = "down")

    ch_Laura "A. . . stuffed animal?"

    $ Laura.change_face("confused3")

    ch_Laura "No."

    return