label Rogue_designer_purse_shopping_accept:
    $ Rogue.change_face("worried1", eyes = "down")

    ch_Rogue "My lord. . ."

    $ Rogue.change_face("worried2")

    ch_Rogue "[Rogue.Player_petname], this is a {i}real{/i} nice purse. . ."

    $ Rogue.change_face("worried1", eyes = "down", blush = 1)

    ch_Rogue "Must've been expensive."

    $ Rogue.change_face("worried1", blush = 1)

    ch_Rogue "Ah don't want to sound ungrateful or nothin'. . ."
    ch_Rogue "And ah really do appreciate it, but ah can't accept this."

    $ Rogue.change_face("worried1", eyes = "down", blush = 1)

    ch_Rogue "Ah'm not really the purse wearin' type of gal, and lettin' such a nice one just collect dust in my room would be such a waste. . ."

    $ Rogue.change_face("worried1", mouth = "smirk", blush = 1)

    ch_Rogue "Someone else could put it to better use."

    return False

label Rogue_designer_purse_shopping_reject:
    $ Rogue.change_face("worried1", eyes = "down", blush = 1)

    ch_Rogue "Ah'm not really the purse wearin' type of gal. . ."

    $ Rogue.change_face("worried1")

    return

label Rogue_designer_purse_gift_accept:
    $ Rogue.change_face("worried1", eyes = "down")

    ch_Rogue "My lord. . ."

    $ Rogue.change_face("worried2")

    ch_Rogue "[Rogue.Player_petname], this is a {i}real{/i} nice purse. . ."

    $ Rogue.change_face("worried1", eyes = "down", blush = 1)

    ch_Rogue "Must've been expensive."

    $ Rogue.change_face("worried1", blush = 1)

    ch_Rogue "Ah don't want to sound ungrateful or nothin'. . ."
    ch_Rogue "And ah really do appreciate it, but ah can't accept this."

    $ Rogue.change_face("worried1", eyes = "down", blush = 1)

    ch_Rogue "Ah'm not really the purse wearin' type of gal, and lettin' such a nice one just collect dust in my room would be such a waste. . ."

    $ Rogue.change_face("worried1", mouth = "smirk", blush = 1)

    ch_Rogue "Someone else could put it to better use."

    return False

label Rogue_designer_purse_gift_reject:
    $ Rogue.change_face("worried1", eyes = "down", blush = 1)

    ch_Rogue "Ah'm not really the purse wearin' type of gal. . ."

    $ Rogue.change_face("worried1")

    return