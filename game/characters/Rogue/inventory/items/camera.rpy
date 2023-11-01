label Rogue_camera_shopping_accept:
    $ Rogue.change_face("worried1", eyes = "down", mouth = "smirk")

    ch_Rogue "Lord. . . is this really for me?"

    $ Rogue.change_face("worried1", mouth = "smirk")

    ch_Player "Well, yeah. . . haven't you talked about liking photography before?"

    $ Rogue.change_face("worried2", blush = 1)

    ch_Rogue "Ah have, but [Player.first_name], this must've cost a pretty penny. . ."

    $ Rogue.change_face("worried1", eyes = "down", blush = 1)

    ch_Rogue "Ah don't know what to say."

    $ Rogue.change_face("worried1", mouth = "smirk", blush = 1)

    ch_Rogue "Thank you. . ."

    call change_Girl_stat(Rogue, "love", 35) from _call_change_Girl_stat_1541
    call change_Girl_stat(Rogue, "trust", 20) from _call_change_Girl_stat_1542

    return True

label Rogue_camera_shopping_reject:

    return

label Rogue_camera_gift_accept:
    $ Rogue.change_face("worried1", eyes = "down", mouth = "smirk")

    ch_Rogue "Lord. . . is this really for me?"

    $ Rogue.change_face("worried1", mouth = "smirk")

    ch_Player "Well, yeah. . . haven't you talked about liking photography before?"

    $ Rogue.change_face("worried2", blush = 1)

    ch_Rogue "Ah have, but [Player.first_name], this must've cost a pretty penny. . ."

    $ Rogue.change_face("worried1", eyes = "down", blush = 1)

    ch_Rogue "Ah don't know what to say."

    $ Rogue.change_face("worried1", mouth = "smirk", blush = 1)

    ch_Rogue "Thank you. . ."

    call change_Girl_stat(Rogue, "love", 35) from _call_change_Girl_stat_1543
    call change_Girl_stat(Rogue, "trust", 20) from _call_change_Girl_stat_1544

    return True

label Rogue_camera_gift_reject:

    return