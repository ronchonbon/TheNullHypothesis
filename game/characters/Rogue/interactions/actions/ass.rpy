label Rogue_rejects_grab_ass_over_clothes:
    $ Rogue.change_face("surprised2", blush = 1)

    ch_Rogue "You wanna grab my butt?" 

    $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

    ch_Rogue "Ah don't know. . . even clothed. . ."
    ch_Rogue "Let's start somewhere else, [Rogue.Player_petname]. . ."

    return

label Rogue_accepts_grab_ass_over_clothes_first_time:
    $ Rogue.change_face("confused1", mouth = "smirk", blush = 1)

    ch_Rogue "You really like my butt?" 

    return

label Rogue_accepts_grab_ass_over_clothes_second_time:

    return

label Rogue_accepts_grab_ass_over_clothes:
    $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

    ch_Rogue "Do whatever ya want to it. . ."

    return

label Rogue_accepts_grab_ass_over_clothes_love:

    return
    
label Rogue_rejects_grab_ass:
    $ Rogue.change_face("surprised2", blush = 1)

    ch_Rogue "You wanna touch my butt?" 

    $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

    ch_Rogue "Let's start somewhere else, [Rogue.Player_petname]. . ."

    return

label Rogue_accepts_grab_ass_first_time:
    $ Rogue.change_face("confused1", mouth = "smirk", blush = 1)

    ch_Rogue "You really like my butt?" 

    $ Rogue.change_face("sexy", blush = 2)

    ch_Rogue "It might be nice. . ."

    return

label Rogue_accepts_grab_ass_second_time:

    return

label Rogue_accepts_grab_ass:
    $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

    ch_Rogue "Do whatever ya want to it. . ."

    return

label Rogue_accepts_grab_ass_love:

    return
    
label Rogue_rejects_finger_ass:
    $ Rogue.change_face("perplexed", blush = 1)

    ch_Rogue "You want to put your finger in my butt?!" 

    $ Rogue.change_face("worried1", blush = 1)

    ch_Rogue "Ah ain't ready for somethin' like that yet. . ."

    return

label Rogue_accepts_finger_ass_first_time:
    $ Rogue.change_face("perplexed", blush = 1) 

    ch_Rogue "You want to put your finger in my butt?!" 

    $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1) 

    ch_Rogue "If you really wanna. . ."

    return

label Rogue_accepts_finger_ass_second_time:

    return

label Rogue_accepts_finger_ass:
    $ Rogue.change_face("worried2", mouth = "lipbite", blush = 1)

    ch_Rogue "Yes. . . you can."

    return

label Rogue_accepts_finger_ass_love:

    return

label Rogue_rejects_eat_ass:
    $ Rogue.change_face("surprised2", blush = 1)

    ch_Rogue "You want to lick it?!"

    $ Rogue.change_face("worried1", eyes = "down", mouth = "lipbite", blush = 1)

    ch_Rogue "Ah'll think about it. . ."

    return

label Rogue_accepts_eat_ass_first_time:
    $ Rogue.change_face("worried2", mouth = "lipbite", blush = 1)

    ch_Rogue "You want to lick it?!" 

    $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1) 

    ch_Rogue "Ah guess ah'm willin' to try it. . ."

    return

label Rogue_accepts_eat_ass_second_time:

    return

label Rogue_accepts_eat_ass:
    if Rogue.check_traits("quirk"):
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    if dice_roll == 1:
        $ Rogue.change_face("worried2", mouth = "lipbite", blush = 1)

        ch_Rogue "Wanna lick it?" 

        $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1) 

        ch_Rogue "Alright, ah do kinda like it."
    elif dice_roll == 2:
        $ Rogue.change_face("worried2", mouth = "lipbite", blush = 1)

        ch_Rogue "Wanna lick it again?" 

        $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1) 

        call expose(Rogue, "anus") from _call_expose_9

        "She exposes herself and presents her ass to you."

    return

label Rogue_accepts_eat_ass_love:

    return