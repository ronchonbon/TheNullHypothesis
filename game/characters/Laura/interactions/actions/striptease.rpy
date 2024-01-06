label Laura_rejects_striptease:
    $ Laura.change_face("angry1", blush = 1)

    if not Laura.History.check("seen_pussy"):
        ch_Laura "You're not seeing me naked. . . yet."
    else:
        ch_Laura "Nope."

    return

label Laura_accepts_striptease_first_time:
    $ Laura.change_face("neutral", eyes = "squint", blush = 1)

    ch_Laura "You just want to see me naked. . ." 

    $ Laura.change_face("sly", blush = 2)

    ch_Laura "Fine. . ."

    return

label Laura_accepts_striptease_second_time:

    return

label Laura_accepts_striptease:
    $ Laura.change_face("sly", blush = 1)

    ch_Laura "As long as you get naked first. . ."

    if not Laura.History.check("seen_Player_naked"):
        call Laura_seeing_penis from _call_Laura_seeing_penis_5

    $ Laura.History.update("seen_Player_naked")

    return

label Laura_accepts_striptease_love:

    return