label Laura_rejects_touch_thighs_over_clothes:
    $ Laura.change_face("confused1", mouth = "smirk", blush = 1) 

    ch_Laura "You like my muscular legs, huh?" 

    $ Laura.change_face("smirk2", eyes = "down", blush = 1) 

    ch_Laura "Too bad." 

    $ Laura.change_face("smirk2", blush = 1)

    return

label Laura_accepts_touch_thighs_over_clothes_first_time:
    $ Laura.change_face("smirk2", eyes = "down", blush = 1)

    ch_Laura "You like my muscular legs huh?" 

    $ Laura.change_face("smirk2", mouth = "lipbite", blush = 2)

    ch_Laura "Fine."

    return

label Laura_accepts_touch_thighs_over_clothes_second_time:

    return

label Laura_accepts_touch_thighs_over_clothes:
    $ Laura.change_face("pleased1", mouth = "lipbite", blush = 1) 

    ch_Laura "The legs?"

    $ Laura.change_face("sly", mouth = "lipbite", blush = 1)

    ch_Laura "Can't get enough of them?"
    ch_Laura "Fine, [Laura.Player_petname]."

    $ Laura.change_face("sly", eyes = "down", mouth = "lipbite", blush = 1) 

    return

label Laura_accepts_touch_thighs_over_clothes_love:

    return

label Laura_rejects_touch_thighs_higher_over_clothes:
    $ Laura.change_face(eyes = "down", blush = 2) 

    ch_Laura "No."

    return

label Laura_accepts_touch_thighs_higher_over_clothes_first_time:
    $ Laura.change_face("neutral", eyes = "squint", mouth = "lipbite", blush = 1)

    ch_Laura "Just not too high."

    $ Laura.change_face("neutral", eyes = "down", mouth = "lipbite", blush = 2)

    return

label Laura_accepts_touch_thighs_higher_over_clothes_second_time:

    return

label Laura_accepts_touch_thighs_higher_over_clothes:
    if Laura.check_traits("quirk"):
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    if dice_roll == 1:
        $ Laura.change_face("smirk2", mouth = "lipbite", blush = 1)

        ch_Laura "Fine. . ."

        $ Laura.change_face("smirk2", eyes = "down", mouth = "lipbite", blush = 2) 
    elif dice_roll == 2:
        $ Laura.change_face("smirk2", mouth = "lipbite", blush = 1)

        ch_Laura "Yes."

        $ Laura.change_face("smirk2", eyes = "down", mouth = "lipbite", blush = 2)

        ch_Laura "You could go higher. . ."

    return

label Laura_accepts_touch_thighs_higher_over_clothes_love:

    return

label Laura_rejects_touch_thighs:
    $ Laura.change_face("confused1", mouth = "smirk", blush = 1) 

    ch_Laura "You like my muscular legs, huh?" 

    $ Laura.change_face("smirk2", eyes = "down", blush = 1) 

    ch_Laura "Too bad." 

    $ Laura.change_face("smirk2", blush = 1)

    return

label Laura_accepts_touch_thighs_first_time:
    $ Laura.change_face("smirk2", eyes = "down", blush = 1)

    ch_Laura "You like my muscular legs huh?" 

    $ Laura.change_face("smirk2", mouth = "lipbite", blush = 2)

    ch_Laura "Fine."

    return

label Laura_accepts_touch_thighs_second_time:

    return

label Laura_accepts_touch_thighs:
    $ Laura.change_face("pleased1", mouth = "lipbite", blush = 1) 

    ch_Laura "The legs?"

    $ Laura.change_face("sly", mouth = "lipbite", blush = 1)

    ch_Laura "Can't get enough of them?"
    ch_Laura "Fine, [Laura.Player_petname]."

    $ Laura.change_face("sly", eyes = "down", mouth = "lipbite", blush = 1) 

    return

label Laura_accepts_touch_thighs_love:

    return

label Laura_rejects_touch_thighs_higher:
    $ Laura.change_face(eyes = "down", blush = 2) 

    ch_Laura "No."

    return

label Laura_accepts_touch_thighs_higher_first_time:
    $ Laura.change_face("neutral", eyes = "squint", mouth = "lipbite", blush = 1)

    ch_Laura "Just not too high."

    $ Laura.change_face("neutral", eyes = "down", mouth = "lipbite", blush = 2)

    return

label Laura_accepts_touch_thighs_higher_second_time:

    return

label Laura_accepts_touch_thighs_higher:
    if Laura.check_traits("quirk"):
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    if dice_roll == 1:
        $ Laura.change_face("smirk2", mouth = "lipbite", blush = 1)

        ch_Laura "Fine. . ."

        $ Laura.change_face("smirk2", eyes = "down", mouth = "lipbite", blush = 2) 
    elif dice_roll == 2:
        $ Laura.change_face("smirk2", mouth = "lipbite", blush = 1)

        ch_Laura "Yes."

        $ Laura.change_face("smirk2", eyes = "down", mouth = "lipbite", blush = 2)

        ch_Laura "You could go higher. . ."

    return

label Laura_accepts_touch_thighs_higher_love:

    return