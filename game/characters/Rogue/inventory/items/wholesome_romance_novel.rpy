label Rogue_wholesome_romance_novel_shopping_accept:
    $ Rogue.change_face("worried1", mouth = "smirk", eyes = "down")

    "She looks over the cover."
    ch_Rogue "Ah've heard real good things about this author."

    $ Rogue.change_face("worried1", blush = 1)

    ch_Rogue "Always writes a happy endin'." 

    $ Rogue.change_face("worried1", mouth = "smirk", blush = 1)

    ch_Rogue "Been thinkin' 'bout tryin' one of their books."

    $ Rogue.change_face("worried1", mouth = "smirk", eyes = "down", blush = 1)

    ch_Rogue "Now ah can. . ."

    $ Rogue.change_face("worried1", mouth = "smirk", blush = 1)

    ch_Rogue "Thank you."

    return True

label Rogue_wholesome_romance_novel_shopping_reject:
    $ Rogue.change_face("confused1")

    ch_Rogue "Ah think ah have enough books actually. . ."

    return

label Rogue_wholesome_romance_novel_gift_accept:
    $ Rogue.change_face("worried1", mouth = "smirk", eyes = "down")

    "She looks over the cover."
    ch_Rogue "Ah've heard real good things about this author."

    $ Rogue.change_face("worried1", blush = 1)

    ch_Rogue "Always writes a happy endin'." 

    $ Rogue.change_face("worried1", mouth = "smirk", blush = 1)

    ch_Rogue "Been thinkin' 'bout tryin' one of their books."

    $ Rogue.change_face("worried1", mouth = "smirk", eyes = "down", blush = 1)

    ch_Rogue "Now ah can. . ."

    $ Rogue.change_face("worried1", mouth = "smirk", blush = 1)

    ch_Rogue "Thank you."

    return True

label Rogue_wholesome_romance_novel_gift_reject:
    $ Rogue.change_face("confused1")

    ch_Rogue "Ah think ah have enough books actually. . ."

    return