label Laura_candle_shopping_accept:
    $ Laura.change_face("confused1", eyes = "down")

    "Her nostrils flare as she brings the candle up to her nose."

    $ Laura.change_face("confused1")

    ch_Laura "It does smell pleasant. . ."
    ch_Laura "But, why? Does my room smell bad to you?"
    ch_Player "No, nothing like that."

    $ Laura.change_face("confused1", eyes = "down", blush = 1)

    ch_Player "I just thought you'd enjoy the smell."
    ch_Laura "I do. . ."
    ch_Laura "Thank you."

    call change_Companion_stat(Laura, "love", 0) from _call_change_Companion_stat_1451
    call change_Companion_stat(Laura, "trust", 0) from _call_change_Companion_stat_1452

    return True

label Laura_candle_shopping_reject:
    $ Laura.change_face("confused1", eyes = "down")

    pause 1.0
    
    $ Laura.change_face("suspicious1")

    ch_Laura "I don't like the smell."

    return

label Laura_candle_gift_accept:
    $ Laura.change_face("confused1", eyes = "down")

    "Her nostrils flare as she brings the candle up to her nose."

    $ Laura.change_face("confused1")

    ch_Laura "It does smell pleasant. . ."
    ch_Laura "But, why? Does my room smell bad to you?"
    ch_Player "No, nothing like that."

    $ Laura.change_face("confused1", eyes = "down", blush = 1)

    ch_Player "I just thought you'd enjoy the smell."
    ch_Laura "I do. . ."
    ch_Laura "Thank you."

    call change_Companion_stat(Laura, "love", 0) from _call_change_Companion_stat_1453
    call change_Companion_stat(Laura, "trust", 0) from _call_change_Companion_stat_1454

    return True

label Laura_candle_gift_reject:
    $ Laura.change_face("confused1", eyes = "down")

    pause 1.0
    
    $ Laura.change_face("suspicious1")

    ch_Laura "I don't like the smell."

    return