label Laura_rejects_titjob:
    $ Laura.change_face("confused2", blush = 1) 

    ch_Laura "In between my tits?" 
    ch_Laura "That's a thing?"

    $ Laura.change_face("neutral", eyes = "squint", blush = 1) 

    ch_Laura "Nope."

    return

label Laura_accepts_titjob_first_time:
    $ Laura.change_face("surprised2", blush = 1)

    ch_Laura "In between my tits?"

    $ Laura.change_face("sly", mouth = "lipbite", blush = 2)

    ch_Laura "You are always starting at them."
    ch_Laura "Fine."

    return

label Laura_accepts_titjob_second_time:

    return

label Laura_accepts_titjob:
    if Laura.check_traits("quirk"):
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    if dice_roll == 1:
        $ Laura.change_face("smirk2", mouth = "lipbite", blush = 1)

        ch_Laura "I'll never understand your obsession. . ."
    elif dice_roll == 2:
        $ Laura.change_face("sly", blush = 1)

        ch_Laura "Hmm. . ."

        $ Laura.change_face("sly", mouth = "lipbite", blush = 1)

        ch_Laura "Get over here, [Laura.Player_petname]."
        "She grabs you by the balls, pulling you down to her."

    return

label Laura_accepts_titjob_love:

    return