label Rogue_box_of_chocolates_shopping_accept:
    $ Rogue.change_face("surprised1", eyes = "down")

    ch_Rogue "Ya got me a box of chocolates?"

    $ Rogue.change_face("worried2", mouth = "lipbite", blush = 1)

    pause 1.0

    $ Rogue.change_face("worried1", eyes = "right", mouth = "lipbite", blush = 1) 

    ch_Rogue "Nobody's ever given me chocolates before."
    ch_Rogue "That's real sweet of you. . ."

    $ Rogue.change_face("worried1", mouth = "smirk", blush = 1)

    ch_Player "I'm sure the chocolate will be even sweeter."

    $ Rogue.change_face("confused1", mouth = "smirk", blush = 1)

    ch_Rogue "Ah reckon yer probably right. . ."

    return True

label Rogue_box_of_chocolates_shopping_reject:
    $ Rogue.change_face("surprised1", eyes = "down")

    pause 1.0

    $ Rogue.change_face("worried2")

    ch_Rogue "That's sweet of you, but no thanks. . ."

    return

label Rogue_box_of_chocolates_gift_accept:
    $ Rogue.change_face("surprised1", eyes = "down")

    ch_Rogue "Ya got me a box of chocolates?"

    $ Rogue.change_face("worried2", mouth = "lipbite", blush = 1)

    pause 1.0

    $ Rogue.change_face("worried1", eyes = "right", mouth = "lipbite", blush = 1) 

    ch_Rogue "Nobody's ever given me chocolates before."
    ch_Rogue "That's real sweet of you. . ."

    $ Rogue.change_face("worried1", mouth = "smirk", blush = 1)

    ch_Player "I'm sure the chocolate will be even sweeter."

    $ Rogue.change_face("confused1", mouth = "smirk", blush = 1)

    ch_Rogue "Ah reckon yer probably right. . ."

    return True

label Rogue_box_of_chocolates_gift_reject:
    $ Rogue.change_face("surprised1", eyes = "down")

    pause 1.0

    $ Rogue.change_face("worried2")

    ch_Rogue "That's sweet of you, but no thanks. . ."

    return