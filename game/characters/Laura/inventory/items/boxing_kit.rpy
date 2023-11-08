label Laura_boxing_kit_shopping_accept:
    $ Laura.change_face("happy", eyes = "wide", brows = "raised")

    "As you show [Laura.name] your gift, her face lights up."

    $ Laura.change_face("confused2", mouth = "smirk")

    ch_Laura "This is. . . for my room. . . for me?"
    ch_Player "Yep."

    $ Laura.change_face("worried1", eyes = "right", blush = 1)

    ch_Player "Figured you'd appreciate being able to beat the shit out of something in the privacy of your own room."

    $ Laura.change_face("worried1", blush = 1)

    pause 0.5

    $ Laura.change_face("angry1", eyes = "right", blush = 1)

    ch_Laura "Thank you. . ."
    ch_Laura "I. . . do appreciate it. . ."

    call change_Girl_stat(Laura, "love", 0) from _call_change_Girl_stat_1447
    call change_Girl_stat(Laura, "trust", 0) from _call_change_Girl_stat_1448

    return True

label Laura_boxing_kit_shopping_reject:

    return

label Laura_boxing_kit_gift_accept:
    $ Laura.change_face("happy", eyes = "wide", brows = "raised")

    "As you show [Laura.name] your gift, her face lights up."

    $ Laura.change_face("confused2", mouth = "smirk")

    ch_Laura "This is. . . for my room. . . for me?"
    ch_Player "Yep."

    $ Laura.change_face("worried1", eyes = "right", blush = 1)

    ch_Player "Figured you'd appreciate being able to beat the shit out of something in the privacy of your own room."

    $ Laura.change_face("worried1", blush = 1)

    pause 0.5

    $ Laura.change_face("angry1", eyes = "right", blush = 1)

    ch_Laura "Thank you. . ."
    ch_Laura "I. . . do appreciate it. . ."

    call change_Girl_stat(Laura, "love", 0) from _call_change_Girl_stat_1449
    call change_Girl_stat(Laura, "trust", 0) from _call_change_Girl_stat_1450

    return True

label Laura_boxing_kit_gift_reject:

    return