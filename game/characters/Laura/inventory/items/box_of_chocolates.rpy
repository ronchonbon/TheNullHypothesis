label Laura_box_of_chocolates_shopping_accept:
    $ Laura.change_face("confused1", eyes = "down")

    ch_Laura "Chocolate?"

    $ Laura.change_face("confused1")

    if not Laura.History.check("tried_chocolate"):
        ch_Laura "I don't know if I've ever had chocolate. . ."

    $ Laura.change_face("confused1", eyes = "down")

    "She opens the box."
    ch_Laura "Which piece is for me?"

    $ Laura.change_face("confused2", blush = 1)

    ch_Player "Heh, they're all for you."

    $ Laura.change_face("confused1", eyes = "down", blush = 1)

    ch_Laura "Thank you. . ."

    call change_Character_stat(Laura, "love", 0) from _call_change_Character_stat_1443
    call change_Character_stat(Laura, "trust", 0) from _call_change_Character_stat_1444

    return True

label Laura_box_of_chocolates_shopping_reject:
    $ Laura.change_face("confused1", eyes = "down")

    pause 1.0

    $ Laura.change_face("confused1")

    ch_Laura "No thanks."

    return

label Laura_box_of_chocolates_gift_accept:
    $ Laura.change_face("confused1", eyes = "down")

    ch_Laura "Chocolate?"

    $ Laura.change_face("confused1")

    if not Laura.History.check("tried_chocolate"):
        ch_Laura "I don't know if I've ever had chocolate. . ."

    $ Laura.change_face("confused1", eyes = "down")

    "She opens the box."
    ch_Laura "Which piece is for me?"

    $ Laura.change_face("confused2", blush = 1)

    ch_Player "Heh, they're all for you."

    $ Laura.change_face("confused1", eyes = "down", blush = 1)

    ch_Laura "Thank you. . ."

    call change_Character_stat(Laura, "love", 0) from _call_change_Character_stat_1445
    call change_Character_stat(Laura, "trust", 0) from _call_change_Character_stat_1446

    return True

label Laura_box_of_chocolates_gift_reject:
    $ Laura.change_face("confused1", eyes = "down")

    pause 1.0

    $ Laura.change_face("confused1")

    ch_Laura "No thanks."

    return