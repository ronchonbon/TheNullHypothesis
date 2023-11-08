label Rogue_mirror_shopping_accept:
    $ Rogue.change_face("confused1", eyes = "down", mouth = "smirk")

    ch_Rogue "How'd ya know ah've been wantin' one of these?"

    $ Rogue.change_face("worried1", mouth = "smirk")

    ch_Rogue "It's hard to see my outfits only usin' the bathroom mirror. . ."
    ch_Player "You told me you're into fashion and stuff."
    ch_Player "Thought this would be useful when you want to dress up."

    $ Rogue.change_face("worried1", eyes = "down", mouth = "smirk")

    ch_Rogue "It sure will be."

    $ Rogue.change_face("worried1", mouth = "smirk")

    ch_Rogue "Ah'll start usin' it right away."
    ch_Rogue "Thank you."

    call change_Girl_stat(Rogue, "love", 0) from _call_change_Girl_stat_1557
    call change_Girl_stat(Rogue, "trust", 0) from _call_change_Girl_stat_1558

    return True

label Rogue_mirror_shopping_reject:

    return

label Rogue_mirror_gift_accept:
    $ Rogue.change_face("confused1", eyes = "down", mouth = "smirk")

    ch_Rogue "How'd ya know ah've been wantin' one of these?"

    $ Rogue.change_face("worried1", mouth = "smirk")

    ch_Rogue "It's hard to see my outfits only usin' the bathroom mirror. . ."
    ch_Player "You told me you're into fashion and stuff."
    ch_Player "Thought this would be useful when you want to dress up."

    $ Rogue.change_face("worried1", eyes = "down", mouth = "smirk")

    ch_Rogue "It sure will be."

    $ Rogue.change_face("worried1", mouth = "smirk")

    ch_Rogue "Ah'll start usin' it right away."
    ch_Rogue "Thank you."

    call change_Girl_stat(Rogue, "love", 0) from _call_change_Girl_stat_1559
    call change_Girl_stat(Rogue, "trust", 0) from _call_change_Girl_stat_1560

    return True

label Rogue_mirror_gift_reject:

    return