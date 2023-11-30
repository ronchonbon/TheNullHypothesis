label Rogue_occult_posters_shopping_accept:
    $ Rogue.change_face("confused1", eyes = "down")

    ch_Rogue "Ya got me posters to put up?"
    "She unravels a couple to look at the art."

    $ Rogue.change_face("worried1", mouth = "smirk")

    ch_Player "Did I choose well?"
    ch_Player "Tried to pick things I know you like."

    $ Rogue.change_face("worried1", eyes = "down", mouth = "smirk")

    ch_Rogue "Ya sure did."

    $ Rogue.change_face("smirk2")

    ch_Rogue "Ah'll put 'em up right away."

    call change_Companion_stat(Rogue, "love", 0) from _call_change_Companion_stat_1565
    call change_Companion_stat(Rogue, "trust", 0) from _call_change_Companion_stat_1566

    return True

label Rogue_occult_posters_shopping_reject:

    return

label Rogue_occult_posters_gift_accept:
    $ Rogue.change_face("confused1", eyes = "down")

    ch_Rogue "Ya got me posters to put up?"
    "She unravels a couple to look at the art."

    $ Rogue.change_face("worried1", mouth = "smirk")

    ch_Player "Did I choose well?"
    ch_Player "Tried to pick things I know you like."

    $ Rogue.change_face("worried1", eyes = "down", mouth = "smirk")

    ch_Rogue "Ya sure did."

    $ Rogue.change_face("smirk2")

    ch_Rogue "Ah'll put 'em up right away."

    call change_Companion_stat(Rogue, "love", 0) from _call_change_Companion_stat_1567
    call change_Companion_stat(Rogue, "trust", 0) from _call_change_Companion_stat_1568

    return True

label Rogue_occult_posters_gift_reject:

    return