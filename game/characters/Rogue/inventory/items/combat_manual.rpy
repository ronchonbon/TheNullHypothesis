label Rogue_combat_manual_shopping_accept:
    $ Rogue.change_face("confused1", eyes = "down")

    "She reads the cover."

    $ Rogue.change_face("confused1", mouth = "smirk", blush = 1)

    ch_Rogue "A combat manual?"

    $ Rogue.change_face("confused1", eyes = "squint", mouth = "smirk", blush = 1)

    ch_Rogue "You tryin' to say somethin' 'bout my combat ability?"
    ch_Player "What?! No, nothing like that. . ."

    $ Rogue.change_face("worried1", mouth = "smirk", blush = 1)

    ch_Rogue "Ah'm just messin' with ya."

    $ Rogue.change_face("worried1", eyes = "down", mouth = "smirk", blush = 1)

    ch_Player "With how dangerous everything is, I thought you'd find it interesting."
    ch_Rogue "Ah appreciate the thought, thank you."

    $ Rogue.change_face("worried1", mouth = "smirk", blush = 1)

    ch_Rogue "Ah'll put it to good use."

    call change_Character_stat(Rogue, "love", 0) from _call_change_Character_stat_1549
    call change_Character_stat(Rogue, "trust", 0) from _call_change_Character_stat_1550

    return True

label Rogue_combat_manual_shopping_reject:
    $ Rogue.change_face("confused1")

    ch_Rogue "Ah think ah can handle myself, thanks. . ."

    return

label Rogue_combat_manual_gift_accept:
    $ Rogue.change_face("confused1", eyes = "down")

    "She reads the cover."

    $ Rogue.change_face("confused1", mouth = "smirk", blush = 1)

    ch_Rogue "A combat manual?"

    $ Rogue.change_face("confused1", eyes = "squint", mouth = "smirk", blush = 1)

    ch_Rogue "You tryin' to say somethin' 'bout my combat ability?"
    ch_Player "What?! No, nothing like that. . ."

    $ Rogue.change_face("worried1", mouth = "smirk", blush = 1)

    ch_Rogue "Ah'm just messin' with ya."

    $ Rogue.change_face("worried1", eyes = "down", mouth = "smirk", blush = 1)

    ch_Player "With how dangerous everything is, I thought you'd find it interesting."
    ch_Rogue "Ah appreciate the thought, thank you."

    $ Rogue.change_face("worried1", mouth = "smirk", blush = 1)

    ch_Rogue "Ah'll put it to good use."

    call change_Character_stat(Rogue, "love", 0) from _call_change_Character_stat_1551
    call change_Character_stat(Rogue, "trust", 0) from _call_change_Character_stat_1552

    return True

label Rogue_combat_manual_gift_reject:
    $ Rogue.change_face("confused1")

    ch_Rogue "Ah think ah can handle myself, thanks. . ."

    return