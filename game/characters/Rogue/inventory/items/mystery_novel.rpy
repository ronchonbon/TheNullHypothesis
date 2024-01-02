label Rogue_mystery_novel_shopping_accept:
    $ Rogue.change_face("surprised1", eyes = "down")

    pause 1.0

    $ Rogue.change_face("pleased2")

    ch_Rogue "How'd ya know ah was thinkin' about reading this one?"

    $ Rogue.change_face("worried1", mouth = "smirk", blush = 1)

    ch_Player "It just felt like something you'd be into. . ."

    $ Rogue.change_face("worried1", eyes = "down", mouth = "smirk", blush = 1)

    ch_Rogue "Ya sure got that right."

    $ Rogue.change_face("worried1", mouth = "smirk", blush = 1)

    ch_Rogue "Thanks, [Rogue.Player_petname], ah really appreciate it."

    return True

label Rogue_mystery_novel_shopping_reject:
    $ Rogue.change_face("confused1")

    ch_Rogue "Ah think ah have enough books actually. . ."

    return

label Rogue_mystery_novel_gift_accept:
    $ Rogue.change_face("surprised1", eyes = "down")

    pause 1.0

    $ Rogue.change_face("pleased2")

    ch_Rogue "How'd ya know ah was thinkin' about reading this one?"

    $ Rogue.change_face("worried1", mouth = "smirk", blush = 1)

    ch_Player "It just felt like something you'd be into. . ."

    $ Rogue.change_face("worried1", eyes = "down", mouth = "smirk", blush = 1)

    ch_Rogue "Ya sure got that right."

    $ Rogue.change_face("worried1", mouth = "smirk", blush = 1)

    ch_Rogue "Thanks, [Rogue.Player_petname], ah really appreciate it."

    return True

label Rogue_mystery_novel_gift_reject:
    $ Rogue.change_face("confused1")

    ch_Rogue "Ah think ah have enough books actually. . ."

    return