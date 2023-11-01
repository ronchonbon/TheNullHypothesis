label Jean_rejects_touch_breasts_over_clothes:
    $ Jean.change_face("surprised2", blush = 2)

    ch_Jean "You really wanna touch my boobs?" 

    $ Jean.change_face("smirk2", blush = 1)

    ch_Jean "Cute, but no." 

    return

label Jean_accepts_touch_breasts_over_clothes_first_time:
    $ Jean.change_face("smirk2", eyes = "down", mouth = "lipbite", blush = 2)

    ch_Jean "I know you really like my boobs. . ." 

    $ Jean.change_face("smirk2", mouth = "lipbite", blush = 1)

    ch_Jean "Fine, you can touch." 

    return

label Jean_accepts_touch_breasts_over_clothes_second_time:

    return

label Jean_accepts_touch_breasts_over_clothes:
    if Jean.quirk:
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    if dice_roll == 1:
        $ Jean.change_face("smirk2", eyes = "down", mouth = "lipbite", blush = 2)

        ch_Jean "They have been missing you. . ." 

        $ Jean.change_face("sly", mouth = "lipbite", blush = 1) 
    elif dice_roll == 2:
        $ Jean.change_face("smirk2", eyes = "down", mouth = "lipbite", blush = 2)

        ch_Jean "You really are obsessed. . ." 

        $ Jean.change_face("sly", mouth = "lipbite", blush = 1)

        ch_Jean "It's adorable."

    return

label Jean_accepts_touch_breasts_over_clothes_love:

    return

label Jean_rejects_touch_breasts:
    $ Jean.change_face("surprised2", blush = 2)

    ch_Jean "You really wanna touch my boobs?" 

    $ Jean.change_face("smirk2", blush = 1)

    ch_Jean "Cute, but no." 

    return

label Jean_accepts_touch_breasts_first_time:
    $ Jean.change_face("smirk2", eyes = "down", mouth = "lipbite", blush = 2)

    ch_Jean "I know you really like my boobs. . ." 

    $ Jean.change_face("smirk2", mouth = "lipbite", blush = 1)

    ch_Jean "Fine, you can touch." 

    return

label Jean_accepts_touch_breasts_second_time:

    return

label Jean_accepts_touch_breasts:
    if Jean.quirk:
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    if dice_roll == 1:
        $ Jean.change_face("smirk2", eyes = "down", mouth = "lipbite", blush = 2)

        ch_Jean "They have been missing you. . ." 

        $ Jean.change_face("sly", mouth = "lipbite", blush = 1) 
    elif dice_roll == 2:
        $ Jean.change_face("smirk2", eyes = "down", mouth = "lipbite", blush = 2)

        ch_Jean "You really are obsessed. . ." 

        $ Jean.change_face("sly", mouth = "lipbite", blush = 1)

        ch_Jean "It's adorable."

    return

label Jean_accepts_touch_breasts_love:

    return

label Jean_rejects_pinch_nipples:
    $ Jean.change_face("neutral", eyes = "squint")

    ch_Jean "No pinching."

    return

label Jean_accepts_pinch_nipples_first_time:
    $ Jean.change_face("worried2", mouth = "lipbite", blush = 2)

    pause 0.5

    $ Jean.change_face("worried1", mouth = "lipbite", blush = 2)

    ch_Jean "Not so hard."

    $ Jean.change_face("sly", mouth = "lipbite", blush = 2)

    ch_Jean "That doesn't mean stop. . ."

    return

label Jean_accepts_pinch_nipples_second_time:

    return

label Jean_accepts_pinch_nipples:
    if Jean.quirk:
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    if dice_roll == 1:
        $ Jean.change_face("surprised2", mouth = "lipbite", blush = 2)

        pause 0.5

        $ Jean.change_face("confused1", mouth = "lipbite", blush = 2)

        ch_Jean "Enjoying yourself. . . ?"

        $ Jean.change_face("sly", mouth = "lipbite", blush = 2) 
    elif dice_roll == 2:
        $ Jean.change_face("surprised2", mouth = "lipbite", blush = 2)

        pause 0.5

        $ Jean.change_face("sly", mouth = "lipbite", blush = 2)

        ch_Jean "You naughty little. . ."
        ch_Jean "Harder. . ."

    return

label Jean_accepts_pinch_nipples_love:

    return

label Jean_rejects_suck_nipples:
    $ Jean.change_face("smirk2", eyes = "squint")

    ch_Jean "Be thankful I'm letting you use your hands."
    
    return

label Jean_accepts_suck_nipples_first_time:
    $ Jean.change_face("confused2", mouth = "lipbite", blush = 2)

    ch_Jean "You want to suck on my boobs?" 

    $ Jean.change_face("sly", mouth = "lipbite", blush = 2)

    ch_Jean "Fine, I'm feeling generous."

    return

label Jean_accepts_suck_nipples_second_time:

    return

label Jean_accepts_suck_nipples:
    if Jean.quirk:
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    if dice_roll == 1:
        $ Jean.change_face("sexy", blush = 2)

        ch_Jean "Please do. . ." 
    elif dice_roll == 2:
        $ Jean.change_face("sexy", blush = 2)

        ch_Jean "Mmm. . . like [Jean.Player_petname] even has to ask." 

        $ Jean.change_face("sly", mouth = "lipbite", blush = 2) 

    return

label Jean_accepts_suck_nipples_love:

    return