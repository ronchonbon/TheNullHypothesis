label Rogue_rejects_blowjob:
    $ Rogue.change_face("worried2", mouth = "lipbite", blush = 1)

    if not Rogue.History.check("blowjob"):
        ch_Rogue "You want to put your. . ."
        ch_Rogue "In my mouth?" 

        $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

        ch_Rogue "Let me get used to touchin' you with my hands first. . ."
    else:
        ch_Rogue "Ah don't think so, [Rogue.Player_petname]."

    return

label Rogue_accepts_blowjob_first_time:
    $ Rogue.change_face("worried2", mouth = "lipbite", blush = 1) 

    ch_Rogue "You want to put your. . ."

    $ Rogue.change_face("confused1", eyes = "down", mouth = "lipbite", blush = 1) 

    ch_Rogue "In my mouth?" 

    $ Rogue.change_face("worried1", mouth = "lipbite", blush = 2) 

    ch_Rogue "Ah kinda do wanna know what it tastes like. . ."

    return

label Rogue_accepts_blowjob_second_time:

    return

label Rogue_accepts_blowjob:
    if Rogue.check_traits("quirk"):
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    if dice_roll == 1:
        $ Rogue.change_face("sexy", blush = 1) 

        ch_Rogue "Sure. . ."

        $ Rogue.change_face("worried1", eyes = "down", mouth = "lipbite", blush = 1) 

        ch_Rogue "Ah like the way ya taste. . ." 
    elif dice_roll == 2:
        $ Rogue.change_face("worried2", mouth = "lipbite", blush = 1) 

        ch_Rogue "Of course. . ."

        $ Rogue.change_face("worried1", eyes = "down", mouth = "lipbite", blush = 1) 

        ch_Rogue "My mouth is yours to use however ya want." 

    return

label Rogue_accepts_blowjob_love:

    return

label Rogue_rejects_suck_balls:
    $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1) 

    if not Rogue.History.check("suck_balls"):
        ch_Rogue "Ah can't handle more than one thing at a time. . . yet, [Rogue.Player_petname]."
    else:
        ch_Rogue "Let's take it easy, [Rogue.Player_petname]."

    return

label Rogue_accepts_suck_balls_first_time:
    $ Rogue.change_face("confused1", mouth = "lipbite", blush = 1) 

    ch_Rogue "Ah'll try if ya want."

    return

label Rogue_accepts_suck_balls_second_time:

    return

label Rogue_accepts_suck_balls:
    $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1) 

    ch_Rogue "You like when ah do that?"

    return

label Rogue_accepts_suck_balls_love:

    return

label Rogue_rejects_deepthroat:
    $ Rogue.change_face("confused1", mouth = "lipbite", blush = 1) 

    if not Rogue.History.check("suck_balls"):
        ch_Rogue "Let me get used to your taste first."
    else:
        ch_Rogue "No thank you."

    return

label Rogue_accepts_deepthroat_first_time:
    $ Rogue.change_face("worried2", mouth = "lipbite", blush = 1) 

    ch_Rogue "You want to try goin' deeper?" 

    $ Rogue.change_face("worried1", mouth = "lipbite", blush = 2)  

    ch_Rogue "Alright, just don't force it. . ."

    return

label Rogue_accepts_deepthroat_second_time:

    return

label Rogue_accepts_deepthroat:
    $ Rogue.change_face("worried2", mouth = "lipbite", blush = 1) 

    ch_Rogue "Sure, we can try again." 

    $ Rogue.change_face("sexy", blush = 2)  

    ch_Rogue "Ah did pretty well last time. . . right?"

    return

label Rogue_accepts_deepthroat_love:

    return