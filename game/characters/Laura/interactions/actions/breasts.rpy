label Laura_rejects_touch_breasts_over_clothes:
    $ Laura.change_face("confused1", blush = 1) 

    ch_Laura "My chest?" 

    $ Laura.change_face("suspicious1", blush = 1) 

    ch_Laura "Not happening."

    return

label Laura_accepts_touch_breasts_over_clothes_first_time:
    $ Laura.change_face("confused1", blush = 1)

    ch_Laura "My chest?" 

    $ Laura.change_face("sly", mouth = "lipbite", blush = 1) 

    ch_Laura "Yeah, okay." 

    return

label Laura_accepts_touch_breasts_over_clothes_second_time:

    return

label Laura_accepts_touch_breasts_over_clothes:
    if Laura.quirk:
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    if dice_roll == 1:
        $ Laura.change_face("confused1", eyes = "down", mouth = "lipbite", blush = 2)

        ch_Laura "Sure."
        ch_Laura "I didn't expect it to feel so good when you. . ."

        $ Laura.change_face("sly", mouth = "lipbite", blush = 1) 
    elif dice_roll == 2:
        $ Laura.change_face("confused1", eyes = "down", mouth = "lipbite", blush = 1)

        ch_Laura "You really do have an obsession with them. . ."

        $ Laura.change_face("sly", mouth = "lipbite", blush = 2)

        ch_Laura "Weirdo."

    return

label Laura_accepts_touch_breasts_over_clothes_love:

    return

label Laura_rejects_touch_breasts:
    $ Laura.change_face("confused1", blush = 1) 

    ch_Laura "My chest?" 

    $ Laura.change_face("suspicious1", blush = 1) 

    ch_Laura "Not happening."

    return

label Laura_accepts_touch_breasts_first_time:
    $ Laura.change_face("confused1", blush = 1)

    ch_Laura "My tits?" 

    $ Laura.change_face("sly", mouth = "lipbite", blush = 1) 

    ch_Laura "Yeah, okay." 

    return

label Laura_accepts_touch_breasts_second_time:

    return

label Laura_accepts_touch_breasts:
    if Laura.quirk:
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    if dice_roll == 1:
        $ Laura.change_face("confused1", eyes = "down", mouth = "lipbite", blush = 2)

        ch_Laura "Sure."
        ch_Laura "I didn't expect it to feel so good when you. . ."

        $ Laura.change_face("sly", mouth = "lipbite", blush = 1) 
    elif dice_roll == 2:
        $ Laura.change_face("confused1", eyes = "down", mouth = "lipbite", blush = 1)

        ch_Laura "You really do have an obsession with them. . ."

        $ Laura.change_face("sly", mouth = "lipbite", blush = 2)

        ch_Laura "Weirdo."

    return

label Laura_accepts_touch_breasts_love:

    return

label Laura_rejects_pinch_nipples:
    $ Laura.change_face("neutral", eyes = "squint", blush = 1)

    ch_Laura "Not allowed."

    return

label Laura_accepts_pinch_nipples_first_time:
    $ Laura.change_face("confused2", blush = 1)

    pause 1.0 

    $ Laura.change_face("sexy", blush = 2)

    ch_Laura ". . . harder."

    return

label Laura_accepts_pinch_nipples_second_time:

    return

label Laura_accepts_pinch_nipples:
    if Laura.quirk:
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    if dice_roll == 1:
        $ Laura.change_face("surprised2", mouth = "lipbite", blush = 2)

        pause 1.0

        $ Laura.change_face("sexy", blush = 2)

        ch_Laura "You don't have to be so gentle. . ."

        $ Laura.change_face("sly", mouth = "lipbite", blush = 2) 
    elif dice_roll == 2:
        $ Laura.change_face("appalled2", mouth = "lipbite", blush = 2)

        pause 1.0

        $ Laura.change_face("angry1", mouth = "lipbite", blush = 2)

        ch_Laura "That's it. . . ?"
        ch_Laura "Harder."
        ch_Laura "Or else."

    return

label Laura_accepts_pinch_nipples_love:

    return

label Laura_rejects_suck_nipples:
    $ Laura.change_face("confused1", blush = 1) 

    ch_Laura "You're lucky I let you use your hand."

    return

label Laura_accepts_suck_nipples_first_time:
    $ Laura.change_face("confused1", blush = 1)

    ch_Laura "With your mouth?" 

    $ Laura.change_face("confused1", mouth = "lipbite", blush = 2)

    ch_Laura "Kinda weird, but fine."

    return

label Laura_accepts_suck_nipples_second_time:

    return

label Laura_accepts_suck_nipples:
    if Laura.quirk:
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    if dice_roll == 1:
        $ Laura.change_face("sexy", blush = 2)

        ch_Laura "Yeah. . ."
    elif dice_roll == 2:
        $ Laura.change_face("sexy", blush = 2)

        ch_Laura "You can bite them too. . ."

        $ Laura.change_face("sly", mouth = "lipbite", blush = 2) 

    return

label Laura_accepts_suck_nipples_love:

    return