label Rogue_rejects_titjob:
    $ Rogue.change_face("confused2", blush = 1) 

    if not Rogue.History.check("titjob"):
        ch_Rogue "You want to put your. . ." 
        ch_Rogue "In between my breasts?" 

        $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

    ch_Rogue "Ah don't think so. . ."

    return

label Rogue_accepts_titjob_first_time:
    $ Rogue.change_face("confused2", mouth = "lipbite", blush = 1)

    ch_Rogue "You want to put your. . . in between my breasts?" 

    $ Rogue.change_face("sexy", blush = 2)  

    ch_Rogue "Ah guess it could be nice. . ."

    return

label Rogue_accepts_titjob_second_time:

    return

label Rogue_accepts_titjob:
    $ Rogue.change_face("worried2", mouth = "lipbite", blush = 1)

    ch_Rogue "Wanna use my breasts again?" 

    $ Rogue.change_face("sexy", blush = 2)  

    ch_Rogue "It does feel real nice in there. . ."

    return

label Rogue_accepts_titjob_love:

    return