label Jean_rejects_touch_thighs_over_clothes:
    ch_Jean "You like my long legs, huh?" 

    $ Jean.change_face("smirk2", mouth = "lipbite", blush = 1)

    ch_Jean "Sorry, [Jean.Player_petname]." 

    $ Jean.change_face("smirk2", eyes = "down", mouth = "lipbite", blush = 1) 

    pause 0.5

    $ Jean.change_face("worried1", mouth = "lipbite", blush = 1)

    return

label Jean_accepts_touch_thighs_over_clothes_first_time:
    $ Jean.change_face("sly", mouth = "lipbite", blush = 1) 

    ch_Jean "You like my long legs huh?" 

    $ Jean.change_face("smirk2", mouth = "lipbite", blush = 1)

    ch_Jean "Okay, [Jean.Player_petname]." 

    $ Jean.change_face("smirk2", eyes = "down", mouth = "lipbite", blush = 1) 

    pause 1.0

    $ Jean.change_face("smirk2", mouth = "lipbite", blush = 1)

    return

label Jean_accepts_touch_thighs_over_clothes_second_time:

    return

label Jean_accepts_touch_thighs_over_clothes:
    $ Jean.change_face("sly", mouth = "lipbite", blush = 1) 

    ch_Jean "My legs again?" 

    $ Jean.change_face("smirk2", mouth = "lipbite", blush = 1)

    ch_Jean "Okay, [Jean.Player_petname]." 

    $ Jean.change_face("smirk2", eyes = "down", mouth = "lipbite", blush = 1) 

    pause 1.0

    $ Jean.change_face("smirk2", mouth = "lipbite", blush = 1)

    return

label Jean_accepts_touch_thighs_over_clothes_love:

    return

label Jean_rejects_touch_thighs_higher_over_clothes:
    ch_Jean "Right where you are is high enough." 

    $ Jean.change_face("smirk2", eyes = "down", mouth = "lipbite", blush = 2) 

    return

label Jean_accepts_touch_thighs_higher_over_clothes_first_time:
    $ Jean.change_face("smirk2", mouth = "lipbite", blush = 1)

    ch_Jean "Okay. . . you better not go {i}too{/i} high." 

    $ Jean.change_face("smirk2", eyes = "down", mouth = "lipbite", blush = 2)

    return

label Jean_accepts_touch_thighs_higher_over_clothes_second_time:

    return

label Jean_accepts_touch_thighs_higher_over_clothes:
    if Jean.quirk:
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    if dice_roll == 1:
        $ Jean.change_face("smirk2", mouth = "lipbite", blush = 1)

        ch_Jean "You can. . ." 

        $ Jean.change_face("smirk2", eyes = "down", mouth = "lipbite", blush = 2) 
    elif dice_roll == 2:
        $ Jean.change_face("smirk2", mouth = "lipbite", blush = 1)

        ch_Jean "Fine, [Jean.Player_petname]." 

        $ Jean.change_face("smirk2", eyes = "down", mouth = "lipbite", blush = 2)

        ch_Jean "But If you go too high, I'll have to punish you."

    return

label Jean_accepts_touch_thighs_higher_over_clothes_love:

    return

label Jean_rejects_touch_thighs:
    ch_Jean "You like my long legs, huh?" 

    $ Jean.change_face("smirk2", mouth = "lipbite", blush = 1)

    ch_Jean "Sorry, [Jean.Player_petname]." 

    $ Jean.change_face("smirk2", eyes = "down", mouth = "lipbite", blush = 1) 

    pause 1.0

    $ Jean.change_face("worried1", mouth = "lipbite", blush = 1)

    return

label Jean_accepts_touch_thighs_first_time:
    $ Jean.change_face("sly", mouth = "lipbite", blush = 1) 

    ch_Jean "You like my long legs huh?" 

    $ Jean.change_face("smirk2", mouth = "lipbite", blush = 1)

    ch_Jean "Okay, [Jean.Player_petname]." 

    $ Jean.change_face("smirk2", eyes = "down", mouth = "lipbite", blush = 1) 

    pause 1.0

    $ Jean.change_face("smirk2", mouth = "lipbite", blush = 1)

    return

label Jean_accepts_touch_thighs_second_time:

    return

label Jean_accepts_touch_thighs:
    $ Jean.change_face("sly", mouth = "lipbite", blush = 1) 

    ch_Jean "My legs again?" 

    $ Jean.change_face("smirk2", mouth = "lipbite", blush = 1)

    ch_Jean "Okay, [Jean.Player_petname]." 

    $ Jean.change_face("smirk2", eyes = "down", mouth = "lipbite", blush = 1) 

    pause 1.0

    $ Jean.change_face("smirk2", mouth = "lipbite", blush = 1)

    return

label Jean_accepts_touch_thighs_love:

    return

label Jean_rejects_touch_thighs_higher:
    ch_Jean "Right where you are is high enough." 

    $ Jean.change_face("smirk2", eyes = "down", mouth = "lipbite", blush = 2) 

    return

label Jean_accepts_touch_thighs_higher_first_time:
    $ Jean.change_face("smirk2", mouth = "lipbite", blush = 1)

    ch_Jean "Okay. . . you better not go {i}too{/i} high." 

    $ Jean.change_face("smirk2", eyes = "down", mouth = "lipbite", blush = 2)

    return

label Jean_accepts_touch_thighs_higher_second_time:

    return

label Jean_accepts_touch_thighs_higher:
    if Jean.quirk:
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    if dice_roll == 1:
        $ Jean.change_face("smirk2", mouth = "lipbite", blush = 1)

        ch_Jean "You can. . ." 

        $ Jean.change_face("smirk2", eyes = "down", mouth = "lipbite", blush = 2) 
    elif dice_roll == 2:
        $ Jean.change_face("smirk2", mouth = "lipbite", blush = 1)

        ch_Jean "Fine, [Jean.Player_petname]." 

        $ Jean.change_face("smirk2", eyes = "down", mouth = "lipbite", blush = 2)

        ch_Jean "But If you go too high, I'll have to punish you."
    
    return

label Jean_accepts_touch_thighs_higher_love:

    return