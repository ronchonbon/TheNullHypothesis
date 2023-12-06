label Jean_box_of_chocolates_shopping_accept:
    $ Jean.change_face("happy")

    ch_Jean "Is that for me?!"

    $ Jean.change_face("confused1", eyes = "down", mouth = "smirk", blush = 1)

    ch_Jean "An actual box of chocolates. . ."

    $ Jean.change_face("worried1", mouth = "smirk", blush = 1)

    ch_Jean "That's such a cliche, but I love it, thank you."

    $ Jean.change_face("worried1", eyes = "down", mouth = "smirk", blush = 1)

    ch_Player "I'm pretty good at cliches. . ."

    $ Jean.change_face("confused1", mouth = "smirk", blush = 1)

    ch_Jean "You're cute, so it gets a pass."

    call change_Character_stat(Jean, "love", 0) from _call_change_Character_stat_1291
    call change_Character_stat(Jean, "trust", 0) from _call_change_Character_stat_1292

    return True

label Jean_box_of_chocolates_shopping_reject:
    $ Jean.change_face("confused1")

    ch_Jean "Sorry, I don't just accept random gifts. . ."

    return

label Jean_box_of_chocolates_gift_accept:
    $ Jean.change_face("happy")

    ch_Jean "Is that for me?!"

    $ Jean.change_face("confused1", eyes = "down", mouth = "smirk", blush = 1)

    ch_Jean "An actual box of chocolates. . ."

    $ Jean.change_face("worried1", mouth = "smirk", blush = 1)

    ch_Jean "That's such a cliche, but I love it, thank you."

    $ Jean.change_face("worried1", eyes = "down", mouth = "smirk", blush = 1)

    ch_Player "I'm pretty good at cliches. . ."

    $ Jean.change_face("confused1", mouth = "smirk", blush = 1)

    ch_Jean "You're cute, so it gets a pass."

    call change_Character_stat(Jean, "love", 0) from _call_change_Character_stat_1293
    call change_Character_stat(Jean, "trust", 0) from _call_change_Character_stat_1294

    return True

label Jean_box_of_chocolates_gift_reject:
    $ Jean.change_face("confused1")

    ch_Jean "Sorry, I don't just accept random gifts. . ."

    return