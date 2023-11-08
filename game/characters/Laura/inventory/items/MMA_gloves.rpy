label Laura_MMA_gloves_shopping_accept:
    $ Laura.change_face("pleased2")

    "As you show [Laura.name] your gift, her face lights up."

    $ Laura.change_face("confused2", mouth = "smirk", blush = 1)

    ch_Player "I saw your old pair was getting pretty torn up so. . ."

    $ Laura.change_face("confused1", eyes = "down", mouth = "smirk", blush = 1)

    ch_Laura "Thank you. . ."

    $ Laura.change_face("sly", blush = 1)

    ch_Laura "I will break them in during our training."
    ch_Player "Wait a minute."

    call change_Girl_stat(Laura, "love", 0) from _call_change_Girl_stat_1435
    call change_Girl_stat(Laura, "trust", 0) from _call_change_Girl_stat_1436

    return True

label Laura_MMA_gloves_shopping_reject:

    return

label Laura_MMA_gloves_gift_accept:
    $ Laura.change_face("pleased2")

    "As you show [Laura.name] your gift, her face lights up."

    $ Laura.change_face("confused2", mouth = "smirk", blush = 1)

    ch_Player "I saw your old pair was getting pretty torn up so. . ."

    $ Laura.change_face("confused1", eyes = "down", mouth = "smirk", blush = 1)

    ch_Laura "Thank you. . ."

    $ Laura.change_face("sly", blush = 1)

    ch_Laura "I will break them in during our training."
    ch_Player "Wait a minute."

    call change_Girl_stat(Laura, "love", 0) from _call_change_Girl_stat_1437
    call change_Girl_stat(Laura, "trust", 0) from _call_change_Girl_stat_1438

    return True

label Laura_MMA_gloves_gift_reject:

    return