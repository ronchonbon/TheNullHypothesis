label Laura_rejects_choke:
    if not Laura.History.check("choke"):
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    if dice_roll == 1:
        $ Laura.change_face("angry1", blush = 1)

        ch_Laura "No, but you can get choked." 
        "She starts choking you." 
    elif dice_roll == 2:
        $ Laura.change_face("confused2", blush = 1) 

        pause 1.0

        $ Laura.change_face("angry1", blush = 1) 

        ch_Laura "Why would I let you incapacitate me?"

    return

label Laura_accepts_choke_first_time:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Laura.change_face("confused1", blush = 1)  

        ch_Laura "It's supposed to feel good?" 

        $ Laura.change_face("sly", mouth = "lipbite", blush = 1) 

        ch_Laura "Fine, only if I get to choke you too."
    elif dice_roll == 2:
        $ Laura.change_face("confused1", mouth = "smirk", blush = 1)

        ch_Laura "You're really into this choking thing?" 

        $ Laura.change_face("sly", mouth = "lipbite", blush = 2)

        "She lets you, but also starts choking you."

    return

label Laura_accepts_choke_second_time:

    return

label Laura_accepts_choke:
    if Laura.quirk:
        $ dice_roll = renpy.random.randint(1, 3)
    else:
        $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Laura.change_face("sexy", blush = 1)

        ch_Laura "Fine. . ."

        $ Laura.change_face("sexy", blush = 2)

        ch_Laura "Make it tight."
    elif dice_roll == 2:
        $ Laura.change_face("sly", mouth = "lipbite", blush = 1)

        ch_Laura "If you squeeze hard enough."
    elif dice_roll == 3:
        $ Laura.change_face("sly", mouth = "lipbite", blush = 1)

        ch_Laura "Fine, [Laura.Player_petname]."
        ch_Laura "Go ahead."

        $ Laura.change_face("sly", mouth = "lipbite", blush = 2)

    return

label Laura_accepts_choke_love:

    return