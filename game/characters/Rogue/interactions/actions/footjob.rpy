label Rogue_rejects_footjob:
    $ Rogue.change_face("perplexed", blush = 1)

    if not Rogue.History.check("footjob"):
        ch_Rogue "You want me to rub your. . ."

        $ Rogue.change_face("worried1", eyes = "down", mouth = "lipbite", blush = 1)

        ch_Rogue "With my feet?" 

        $ Rogue.change_face("confused1", mouth = "lipbite", blush = 1)

    ch_Rogue "Ah think I'll keep my shoes on. . ."

    return

label Rogue_accepts_footjob_first_time:
    $ Rogue.change_face("worried2", mouth = "lipbite", blush = 1)

    ch_Rogue "You want me to rub your. . . with my feet?" 

    $ Rogue.change_face("sexy", blush = 2) 

    ch_Rogue "Ah wonder how it'll feel. . ."

    return

label Rogue_accepts_footjob_second_time:

    return

label Rogue_accepts_footjob:
    $ Rogue.change_face("worried2", mouth = "lipbite", blush = 1)

    ch_Rogue "You liked usin' my feet last time?" 

    $ Rogue.change_face("sexy", blush = 2) 

    ch_Rogue "It did feel nice. . ."

    return

label Rogue_accepts_footjob_love:

    return