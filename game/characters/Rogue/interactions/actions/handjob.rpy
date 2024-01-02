label Rogue_rejects_handjob:
    $ Rogue.change_face("worried2", blush = 1)

    if not Rogue.History.check("handjob"):
        ch_Rogue "You want me to grab your. . ."

        $ Rogue.change_face("worried1", eyes = "down", mouth = "lipbite", blush = 1)

        ch_Rogue "With my hand?"

        ch_Rogue "Ah'm not ready to touch that yet. . ."
    else:
        ch_Rogue "No thanks. . ."

    $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

    return

label Rogue_accepts_handjob_first_time:
    $ Rogue.change_face("worried2", mouth = "lipbite", blush = 1) 

    ch_Rogue "You want me to grab your. . . with my hand?" 

    $ Rogue.change_face("smirk2", mouth = "lipbite", blush = 2) 

    ch_Rogue "Ah've been wonderin' what it feels like. . ." 

    return

label Rogue_accepts_handjob_second_time:

    return

label Rogue_accepts_handjob:
    if Rogue.check_traits("quirk"):
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    if dice_roll == 1:
        $ Rogue.change_face("worried2", mouth = "lipbite", blush = 1) 

        ch_Rogue "If ya want me to."

        $ Rogue.change_face("sexy", blush = 1) 

        ch_Rogue "Ah really like how ya feel in my hands. . ."
    elif dice_roll == 2:
        $ Rogue.change_face("worried2", mouth = "lipbite", blush = 1) 

        ch_Rogue "Whatever you want, [Rogue.Player_petname]." 

        $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)  

    return

label Rogue_accepts_handjob_love:

    return

label Rogue_rejects_fondle_balls:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

        if not Rogue.History.check("fondle_balls"):
            ch_Rogue "Ain't even have a handle of your. . . thing, yet."
        else:
            ch_Rogue "Mmm, maybe not."
    elif dice_roll == 2:    
        $ Rogue.change_face("worried1", blush = 1)  

        ch_Rogue "Ah don't really know what to do with them. . ."

    return

label Rogue_accepts_fondle_balls_first_time:
    $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1) 

    ch_Rogue "Ah'll try."
    ch_Rogue "Let me know if ah hurt ya on accident."

    return

label Rogue_accepts_fondle_balls_second_time:

    return

label Rogue_accepts_fondle_balls:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1) 

        ch_Rogue "Ah'll do my best."
    elif dice_roll == 2:
        $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1) 

        ch_Rogue "Yes."
    elif dice_roll == 3:
        $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1) 

        ch_Rogue "Ah've been doin' a good job with them?"

    return

label Rogue_accepts_fondle_balls_love:

    return