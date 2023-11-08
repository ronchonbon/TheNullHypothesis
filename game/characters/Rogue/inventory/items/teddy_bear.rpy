label Rogue_teddy_bear_shopping_accept:
    $ Rogue.change_face("worried1", mouth = "smirk", eyes = "down")

    ch_Rogue "Aw, darlin', ya got me a teddy bear?"

    $ Rogue.change_face("worried1", mouth = "smirk", blush = 1)

    ch_Rogue "That's real sweet of you."

    $ Rogue.change_face("worried1", mouth = "smirk", eyes = "down", blush = 1)

    ch_Rogue "This is like one ah used to have back home, before. . ."

    $ Rogue.change_face("worried1", eyes = "right", blush = 1)

    ch_Rogue "Ah'll make sure to treasure this one."

    call change_Girl_stat(Rogue, "love", 0) from _call_change_Girl_stat_1579
    call change_Girl_stat(Rogue, "trust", 0) from _call_change_Girl_stat_1580

    return True

label Rogue_teddy_bear_shopping_reject:
    $ Rogue.change_face("worried1", eyes = "down")

    pause 1.0

    $ Rogue.change_face("worried1")

    ch_Rogue "That's uhm. . . sweet but. . ."
    ch_Rogue "Maybe not right this minute?"

    return

label Rogue_teddy_bear_gift_accept:
    $ Rogue.change_face("worried1", mouth = "smirk", eyes = "down")

    ch_Rogue "Aw, darlin', ya got me a teddy bear?"

    $ Rogue.change_face("worried1", mouth = "smirk", blush = 1)

    ch_Rogue "That's real sweet of you."

    $ Rogue.change_face("worried1", mouth = "smirk", eyes = "down", blush = 1)

    ch_Rogue "This is like one ah used to have back home, before. . ."

    $ Rogue.change_face("worried1", eyes = "right", blush = 1)

    ch_Rogue "Ah'll make sure to treasure this one."

    call change_Girl_stat(Rogue, "love", 0) from _call_change_Girl_stat_1581
    call change_Girl_stat(Rogue, "trust", 0) from _call_change_Girl_stat_1582

    return True

label Rogue_teddy_bear_gift_reject:
    $ Rogue.change_face("worried1", eyes = "down")

    pause 1.0

    $ Rogue.change_face("worried1")

    ch_Rogue "That's uhm. . . sweet but. . ."
    ch_Rogue "Maybe not right this minute?"

    return