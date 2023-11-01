label Rogue_rejects_striptease:
    if not Rogue.History.check("seen_pussy"):
        $ Rogue.change_face("worried2", mouth = "lipbite", blush = 1) 

        ch_Rogue "Ah'm not ready for you to see me. . ." 

        $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1) 

        ch_Rogue ". . . yet."
    else:
        $ Rogue.change_face("confused1", blush = 1) 

        ch_Rogue "Ain't undressin' in front of you."

    return

label Rogue_accepts_striptease_first_time:
    $ Rogue.change_face("sexy", blush = 1) 

    ch_Rogue "Ah do enjoy seein' the look on your face. . ."

    return

label Rogue_accepts_striptease_second_time:

    return

label Rogue_accepts_striptease:
    $ Rogue.change_face("sexy", blush = 1) 

    ch_Rogue "Of course, you can watch me all ya want. . ."

    return

label Rogue_accepts_striptease_love:

    return