label Rogue_baseball_flag_shopping_accept:
    $ Rogue.change_face("confused1", eyes = "down", mouth = "smirk")

    ch_Rogue "The 'Mississippi Braves', huh?"

    $ Rogue.change_face("worried1", mouth = "smirk")

    ch_Player "Thought you could put it on your wall, remind you of home, ya'know?"
    ch_Rogue "Ah remember goin' to a game or two. . ."

    $ Rogue.change_face("worried1", eyes = "down", mouth = "smirk")

    ch_Rogue "Ah'll hang it up right away."

    $ Rogue.change_face("worried1", mouth = "smirk")

    ch_Rogue "Thank you, [Rogue.Player_petname], ah really appreciate it."

    call change_Companion_stat(Rogue, "love", 0) from _call_change_Companion_stat_1533
    call change_Companion_stat(Rogue, "trust", 0) from _call_change_Companion_stat_1534

    return True

label Rogue_baseball_flag_shopping_reject:

    return

label Rogue_baseball_flag_gift_accept:
    $ Rogue.change_face("confused1", eyes = "down", mouth = "smirk")

    ch_Rogue "The 'Mississippi Braves', huh?"

    $ Rogue.change_face("worried1", mouth = "smirk")

    ch_Player "Thought you could put it on your wall, remind you of home, ya'know?"
    ch_Rogue "Ah remember goin' to a game or two. . ."

    $ Rogue.change_face("worried1", eyes = "down", mouth = "smirk")

    ch_Rogue "Ah'll hang it up right away."

    $ Rogue.change_face("worried1", mouth = "smirk")

    ch_Rogue "Thank you, [Rogue.Player_petname], ah really appreciate it."

    call change_Companion_stat(Rogue, "love", 0) from _call_change_Companion_stat_1535
    call change_Companion_stat(Rogue, "trust", 0) from _call_change_Companion_stat_1536

    return True

label Rogue_baseball_flag_gift_reject:

    return