label Jean_rejects_choke:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Jean.change_face("worried1", blush = 1) 

        ch_Jean "No choking. . . I'm not ready for that."
    elif dice_roll == 2:
        $ Jean.change_face("neutral", eyes = "squint", blush = 1)

        ch_Jean "No choking, [Jean.Player_petname]."
    
    return

label Jean_accepts_choke_first_time:
    $ Jean.change_face("worried2", mouth = "lipbite", blush = 1)

    ch_Jean "Choking?" 

    $ Jean.change_face("worried1", mouth = "lipbite", blush = 1)

    ch_Jean "I guess we can try it. . ."
    ch_Jean "Not too hard."

    return

label Jean_accepts_choke_second_time:

    return

label Jean_accepts_choke:
    if Jean.quirk:
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    if dice_roll == 1:
        $ Jean.change_face("sexy", blush = 1)

        ch_Jean "You can. . ." 

        $ Jean.change_face("worried1", mouth = "lipbite", blush = 2)

        ch_Jean "Just not too tight."
    elif dice_roll == 2:
        $ Jean.change_face("sly", mouth = "lipbite", blush = 1)

        ch_Jean "You're such a pervert, [Jean.Player_petname]." 

        $ Jean.change_face("sexy", blush = 2)

        ch_Jean "Well. . . ?"
        ch_Jean "You gonna start?"

    return

label Jean_accepts_choke_love:

    return