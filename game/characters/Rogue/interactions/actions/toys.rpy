label Rogue_rejects_vibrator:
    $ Rogue.change_face("confused1", blush = 1) 

    if not Rogue.History.check("vibrator"):
        ch_Rogue "You want to do what?!" 

        $ Rogue.change_face("confused1", mouth = "lipbite", blush = 1) 

    ch_Rogue "Not happenin'."

    return

label Rogue_accepts_vibrator_first_time:
    $ Rogue.change_face("worried1", mouth = "lipbite", blush = 2) 

    ch_Rogue "Alright. . ."

    return

label Rogue_accepts_vibrator_second_time:

    return

label Rogue_accepts_vibrator:
    $ Rogue.change_face("sexy", blush = 2) 

    ch_Rogue "Ya like makin' me feel good?" 
    ch_Rogue "Sure." 

    return

label Rogue_accepts_vibrator_love:

    return

label Rogue_rejects_dildo_pussy:
    $ Rogue.change_face("perplexed", blush = 1) 

    if not Rogue.History.check("dildo_pussy"):
        ch_Rogue "You want to put that. . . inside me?!" 

        $ Rogue.change_face("confused1", mouth = "lipbite", blush = 1) 

    ch_Rogue "Not happenin'."

    return

label Rogue_accepts_dildo_pussy_first_time:
    $ Rogue.change_face("worried1", mouth = "lipbite", blush = 2) 

    ch_Rogue "Alright. . ."

    return

label Rogue_accepts_dildo_pussy_second_time:

    return

label Rogue_accepts_dildo_pussy:
    $ Rogue.change_face("sexy", blush = 2) 

    ch_Rogue "Kinky. . . " 
    ch_Rogue "Sure." 

    return

label Rogue_accepts_dildo_pussy_love:

    return

label Rogue_rejects_dildo_ass:
    $ Rogue.change_face("perplexed", blush = 1) 

    if not Rogue.History.check("dildo_ass"):
        ch_Rogue "You want to put that. . . in my butt?!" 

        $ Rogue.change_face("confused1", mouth = "lipbite", blush = 1) 

    ch_Rogue "Not happenin'."

    return

label Rogue_accepts_dildo_ass_first_time:
    $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1) 

    ch_Rogue "That's pretty. . . "

    pause 1.0

    $ Rogue.change_face("worried1", mouth = "lipbite", blush = 2) 

    pause 1.0

    ch_Rogue "Alright. . ."

    return

label Rogue_accepts_dildo_ass_second_time:

    return

label Rogue_accepts_dildo_ass:
    $ Rogue.change_face("sexy", blush = 2) 

    ch_Rogue "Kinky. . . " 
    ch_Rogue "Sure." 

    return

label Rogue_accepts_dildo_ass_love:

    return