label Rogue_candle_shopping_accept:
    if EventScheduler.Events["Rogue_gifts"].completed:
        $ Rogue.change_face("worried1", eyes = "down", mouth = "smirk")

        "[Rogue.name] brings the candles up to her nose to smell them."

        $ Rogue.change_face("pleased2")

        ch_Rogue "How'd ya know these were my favorite scent?"

        $ Rogue.change_face("confused1", mouth = "smirk")

        ch_Player "They are? Heh, yeah, I definitely knew that. . ."
        ch_Rogue "It's alright, [Rogue.Player_petname]."

        $ Rogue.change_face("worried1", mouth = "smirk")

        ch_Rogue "Ah'd love it even if it wasn't."
        ch_Rogue "Ah appreciate everythin' ya get me."

        call change_Girl_stat(Rogue, "love", 0) from _call_change_Girl_stat_1545
        call change_Girl_stat(Rogue, "trust", 0) from _call_change_Girl_stat_1546

        return True
    else:
        $ Rogue.change_face("worried1", eyes = "down")

        ch_Rogue "Candles?"

        $ Rogue.change_face("worried1")

        ch_Rogue "It's not that ah don't appreciate it or nothin'. . ."

        $ Rogue.change_face("worried1", eyes = "down")

        ch_Rogue "Just don't know if ah should decorate my room. . ."

        $ Rogue.change_face("worried1")

    return False

label Rogue_candle_shopping_reject:
    $ Rogue.change_face("worried1", eyes = "down")

    ch_Rogue "Ah don't know if ah should decorate my room. . ."

    $ Rogue.change_face("worried1")

    return

label Rogue_candle_gift_accept:
    if EventScheduler.Events["Rogue_gifts"].completed:
        $ Rogue.change_face("worried1", eyes = "down", mouth = "smirk")

        "[Rogue.name] brings the candles up to her nose to smell them."

        $ Rogue.change_face("pleased2")

        ch_Rogue "How'd ya know these were my favorite scent?"

        $ Rogue.change_face("confused1", mouth = "smirk")

        ch_Player "They are? Heh, yeah, I definitely knew that. . ."
        ch_Rogue "It's alright, [Rogue.Player_petname]."

        $ Rogue.change_face("worried1", mouth = "smirk")

        ch_Rogue "Ah'd love it even if it wasn't."
        ch_Rogue "Ah appreciate everythin' ya get me."

        call change_Girl_stat(Rogue, "love", 0) from _call_change_Girl_stat_1547
        call change_Girl_stat(Rogue, "trust", 0) from _call_change_Girl_stat_1548

        return True
    else:
        $ Rogue.change_face("worried1", eyes = "down")

        ch_Rogue "Candles?"

        $ Rogue.change_face("worried1")

        ch_Rogue "It's not that ah don't appreciate it or nothin'. . ."

        $ Rogue.change_face("worried1", eyes = "down")

        ch_Rogue "Just don't know if ah should decorate my room. . ."

        $ Rogue.change_face("worried1")

    return False

label Rogue_candle_gift_reject:
    $ Rogue.change_face("worried1", eyes = "down")

    ch_Rogue "Ah don't know if ah should decorate my room. . ."

    $ Rogue.change_face("worried1")

    return