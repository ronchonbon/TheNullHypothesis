label Rogue_horror_novel_shopping_accept:
    $ Rogue.change_face("confused1", mouth = "smirk", eyes = "down")

    ch_Rogue "Well this one sure looks interestin'."

    $ Rogue.change_face("confused1", mouth = "smirk")

    ch_Rogue "Ah've been lookin' for a new series to read."

    $ Rogue.change_face("worried1", eyes = "right", mouth = "smirk", blush = 1)

    ch_Rogue "Already read through everythin' ah've got. . ."

    $ Rogue.change_face("worried1", mouth = "smirk", blush = 1)

    ch_Rogue "Thank you." 

    call change_Character_stat(Rogue, "love", 0) from _call_change_Character_stat_1553
    call change_Character_stat(Rogue, "trust", 0) from _call_change_Character_stat_1554

    return True

label Rogue_horror_novel_shopping_reject:
    $ Rogue.change_face("confused1")

    ch_Rogue "Ah think ah have enough books actually. . ."

    return

label Rogue_horror_novel_gift_accept:
    $ Rogue.change_face("confused1", mouth = "smirk", eyes = "down")

    ch_Rogue "Well this one sure looks interestin'."

    $ Rogue.change_face("confused1", mouth = "smirk")

    ch_Rogue "Ah've been lookin' for a new series to read."

    $ Rogue.change_face("worried1", eyes = "right", mouth = "smirk", blush = 1)

    ch_Rogue "Already read through everythin' ah've got. . ."

    $ Rogue.change_face("worried1", mouth = "smirk", blush = 1)

    ch_Rogue "Thank you." 

    call change_Character_stat(Rogue, "love", 0) from _call_change_Character_stat_1555
    call change_Character_stat(Rogue, "trust", 0) from _call_change_Character_stat_1556

    return True

label Rogue_horror_novel_gift_reject:
    $ Rogue.change_face("confused1")

    ch_Rogue "Ah think ah have enough books actually. . ."

    return