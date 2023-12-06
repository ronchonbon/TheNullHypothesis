label Laura_motorcycle_posters_shopping_accept:
    $ Laura.change_face("surprised1", eyes = "down")

    ch_Laura "These are. . ."

    $ Laura.change_face("surprised2", blush = 1)

    ch_Player "I've seen you get all excited about them."
    ch_Player "And thought they'd look good on your wall."

    $ Laura.change_face("angry1", eyes = "right", blush = 1)

    ch_Laura "They are. . . {i}cool{/i}. . ."

    $ Laura.change_face("neutral", blush = 1)

    ch_Laura "Thank you."

    $ Laura.change_face("angry1", eyes = "down", blush = 1)

    ch_Laura "I will put them up immediately." 

    call change_Character_stat(Laura, "love", 0) from _call_change_Character_stat_1469
    call change_Character_stat(Laura, "trust", 0) from _call_change_Character_stat_1470

    return True

label Laura_motorcycle_posters_shopping_reject:

    return

label Laura_motorcycle_posters_gift_accept:
    $ Laura.change_face("surprised1", eyes = "down")

    ch_Laura "These are. . ."

    $ Laura.change_face("surprised2", blush = 1)

    ch_Player "I've seen you get all excited about them."
    ch_Player "And thought they'd look good on your wall."

    $ Laura.change_face("angry1", eyes = "right", blush = 1)

    ch_Laura "They are. . . {i}cool{/i}. . ."

    $ Laura.change_face("neutral", blush = 1)

    ch_Laura "Thank you."

    $ Laura.change_face("angry1", eyes = "down", blush = 1)

    ch_Laura "I will put them up immediately." 

    call change_Character_stat(Laura, "love", 0) from _call_change_Character_stat_1471
    call change_Character_stat(Laura, "trust", 0) from _call_change_Character_stat_1472

    return True

label Laura_motorcycle_posters_gift_reject:

    return