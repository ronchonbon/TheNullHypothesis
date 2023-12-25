label Rogue_rejects_choke:
    $ Rogue.change_face("worried1", blush = 1)

    ch_Rogue "Ah don't know 'bout doin' any of that, [Rogue.Player_petname]. . ."

    return

label Rogue_accepts_choke_first_time:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

        ch_Rogue "Alright. . ."
        ch_Rogue "But be gentle, [Rogue.Player_petname]."
    elif dice_roll == 2:
        $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

        ch_Rogue "Gently, [Rogue.Player_petname]."

    return

label Rogue_accepts_choke_second_time:

    return

label Rogue_accepts_choke:
    if Rogue.quirk:
        $ dice_roll = renpy.random.randint(1, 3)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    if dice_roll == 1:
        $ Rogue.change_face("sexy", blush = 1)

        ch_Rogue "Ah do kinda like it. . ." 
    elif dice_roll == 2:
        $ Rogue.change_face("worried2", mouth = "lipbite", blush = 1)

        ch_Rogue "Please do. . ." 
    elif dice_roll == 3:
        $ Rogue.change_face("sly", mouth = "lipbite", blush = 1) 

        ch_Rogue "Roughly please, [Rogue.Player_petname]."

    return

label Rogue_accepts_choke_love:

    return