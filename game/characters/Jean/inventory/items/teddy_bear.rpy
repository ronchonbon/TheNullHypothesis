label Jean_teddy_bear_shopping_accept:
    $ Jean.change_face("worried1", mouth = "smirk", eyes = "down")

    ch_Jean "You got me a teddy bear?"

    $ Jean.change_face("worried1", mouth = "smirk", blush = 1)

    ch_Jean "That's {i}really{/i} cute. . ."

    $ Jean.change_face("worried1", mouth = "smirk", eyes = "down", blush = 1)

    ch_Jean "This little guy's going right on my bed. . ."

    call change_Girl_stat(Jean, "love", 20) from _call_change_Girl_stat_1321
    call change_Girl_stat(Jean, "trust", 10) from _call_change_Girl_stat_1322

    return True

label Jean_teddy_bear_shopping_reject:
    $ Jean.change_face("worried1", mouth = "smirk", eyes = "down")

    ch_Jean "Cute, but maybe a bit too personal, [Player.first_name]."

    $ Jean.change_face("worried1")

    return

label Jean_teddy_bear_gift_accept:
    $ Jean.change_face("worried1", mouth = "smirk", eyes = "down")

    ch_Jean "You got me a teddy bear?"

    $ Jean.change_face("worried1", mouth = "smirk", blush = 1)

    ch_Jean "That's {i}really{/i} cute. . ."

    $ Jean.change_face("worried1", mouth = "smirk", eyes = "down", blush = 1)

    ch_Jean "This little guy's going right on my bed. . ."

    call change_Girl_stat(Jean, "love", 20) from _call_change_Girl_stat_1323
    call change_Girl_stat(Jean, "trust", 10) from _call_change_Girl_stat_1324

    return True

label Jean_teddy_bear_gift_reject:
    $ Jean.change_face("worried1", mouth = "smirk", eyes = "down")

    ch_Jean "Cute, but maybe a bit too personal, [Player.first_name]."

    $ Jean.change_face("worried1")

    return