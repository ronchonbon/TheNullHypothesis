label Jean_candle_shopping_accept:
    $ Jean.change_face("pleased1", eyes = "down")

    "She brings the candle up to her nose, taking in the scent."

    $ Jean.change_face("pleased2")

    ch_Jean "This smells great!"

    $ Jean.change_face("confused1", mouth = "smirk")

    ch_Jean "How'd you know I like the smell of. . ."

    $ Jean.change_face("confused1", mouth = "smirk", eyes = "down")

    ch_Jean "This will be great to put in my room while studying."
    ch_Jean "Will help with the anxiety. . ."

    $ Jean.change_face("pleased2")

    pause 0.5

    $ Jean.change_face("worried1", eyes = "right", mouth = "smirk")

    ch_Jean "Heh, sorry, spaced out for a second. . ."

    call change_Girl_stat(Jean, "love", 25) from _call_change_Girl_stat_1295
    call change_Girl_stat(Jean, "trust", 10) from _call_change_Girl_stat_1296

    return True

label Jean_candle_shopping_reject:
    $ Jean.change_face("confused1", eyes = "down")

    ch_Jean "Not really my favorite scent, [Player.first_name]."
    
    $ Jean.change_face("confused1")

    return

label Jean_candle_gift_accept:
    $ Jean.change_face("pleased1", eyes = "down")

    "She brings the candle up to her nose, taking in the scent."

    $ Jean.change_face("pleased2")

    ch_Jean "This smells great!"

    $ Jean.change_face("confused1", mouth = "smirk")

    ch_Jean "How'd you know I like the smell of. . ."

    $ Jean.change_face("confused1", mouth = "smirk", eyes = "down")

    ch_Jean "This will be great to put in my room while studying."
    ch_Jean "Will help with the anxiety. . ."

    $ Jean.change_face("pleased2")

    pause 0.5

    $ Jean.change_face("worried1", eyes = "right", mouth = "smirk")

    ch_Jean "Heh, sorry, spaced out for a second. . ."

    call change_Girl_stat(Jean, "love", 25) from _call_change_Girl_stat_1297
    call change_Girl_stat(Jean, "trust", 10) from _call_change_Girl_stat_1298

    return True

label Jean_candle_gift_reject:
    $ Jean.change_face("confused1", eyes = "down")

    ch_Jean "Not really my favorite scent, [Player.first_name]."
    
    $ Jean.change_face("confused1")

    return