label Rogue_rejects_touch_thighs_over_clothes:
    $ Rogue.change_face("worried2", blush = 1)

    ch_Rogue "My thighs?" 

    $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

    ch_Rogue ". . . That's a bit too intimate, [Rogue.Player_petname]." 

    $ Rogue.change_face("worried1", eyes = "down", mouth = "lipbite", blush = 1)

    return

label Rogue_accepts_touch_thighs_over_clothes_first_time:
    $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

    ch_Rogue "Alright." 

    $ Rogue.change_face("smirk2", mouth = "lipbite", blush = 1)

    ch_Rogue ". . . Just not too high, [Rogue.Player_petname]." 

    $ Rogue.change_face("smirk2", eyes = "down", mouth = "lipbite", blush = 2)

    return

label Rogue_accepts_touch_thighs_over_clothes_second_time:

    return

label Rogue_accepts_touch_thighs_over_clothes:
    if Rogue.check_traits("quirk"):
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    if dice_roll == 1:
        $ Rogue.change_face("sexy", blush = 1)

        ch_Rogue "Sure ya can."

        $ Rogue.change_face("sexy", eyes = "down", blush = 1) 
    elif dice_roll == 2:
        $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

        "She just takes your hand and places it on her thigh for you."

        $ Rogue.change_face("sexy", eyes = "down", blush = 1) 

    return

label Rogue_accepts_touch_thighs_over_clothes_love:

    return

label Rogue_rejects_touch_thighs_higher_over_clothes:
    $ Rogue.change_face("worried1", eyes = "down", mouth = "lipbite", blush = 1)

    ch_Rogue "That's a bit too close to my. . ."

    $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

    ch_Rogue "No, sorry. . ."

    return

label Rogue_accepts_touch_thighs_higher_over_clothes_first_time:
    $ Rogue.change_face("worried1", eyes = "down", mouth = "lipbite", blush = 1)

    ch_Rogue "Alright. . ." 

    return

label Rogue_accepts_touch_thighs_higher_over_clothes_second_time:

    return

label Rogue_accepts_touch_thighs_higher_over_clothes:
    if Rogue.check_traits("quirk"):
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    if dice_roll == 1:
        $ Rogue.change_face("worried1", eyes = "down", mouth = "lipbite", blush = 1)

        ch_Rogue "You can. . ." 
    elif dice_roll == 2:
        $ Rogue.change_face("worried1", eyes = "down", mouth = "lipbite", blush = 1)

        ch_Rogue "Please do, [Rogue.Player_petname]. . ." 

    return

label Rogue_accepts_touch_thighs_higher_over_clothes_love:

    return

label Rogue_rejects_touch_thighs:
    $ Rogue.change_face("worried2", blush = 1)

    ch_Rogue "My thighs?" 

    $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

    ch_Rogue ". . . That's a bit too intimate, [Rogue.Player_petname]." 

    $ Rogue.change_face("worried1", eyes = "down", mouth = "lipbite", blush = 1)

    return

label Rogue_accepts_touch_thighs_first_time:
    $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

    ch_Rogue "Alright." 

    $ Rogue.change_face("smirk2", mouth = "lipbite", blush = 1)

    ch_Rogue ". . . Just not too high, [Rogue.Player_petname]." 

    $ Rogue.change_face("smirk2", eyes = "down", mouth = "lipbite", blush = 2)

    return

label Rogue_accepts_touch_thighs_second_time:

    return

label Rogue_accepts_touch_thighs:
    if Rogue.check_traits("quirk"):
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    if dice_roll == 1:
        $ Rogue.change_face("sexy", blush = 1)

        ch_Rogue "Sure ya can."

        $ Rogue.change_face("sexy", eyes = "down", blush = 1) 
    elif dice_roll == 2:
        $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

        "She just takes your hand and places it on her thigh for you."

        $ Rogue.change_face("sexy", eyes = "down", blush = 1) 

    return

label Rogue_accepts_touch_thighs_love:

    return

label Rogue_rejects_touch_thighs_higher:
    $ Rogue.change_face("worried1", eyes = "down", mouth = "lipbite", blush = 1)

    ch_Rogue "That's a bit too close to my. . ."

    $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

    ch_Rogue "No, sorry. . ."

    return

label Rogue_accepts_touch_thighs_higher_first_time:
    $ Rogue.change_face("worried1", eyes = "down", mouth = "lipbite", blush = 1)

    ch_Rogue "Alright. . ." 

    return

label Rogue_accepts_touch_thighs_higher_second_time:

    return

label Rogue_accepts_touch_thighs_higher:
    if Rogue.check_traits("quirk"):
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    if dice_roll == 1:
        $ Rogue.change_face("worried1", eyes = "down", mouth = "lipbite", blush = 1)

        ch_Rogue "You can. . ." 
    elif dice_roll == 2:
        $ Rogue.change_face("worried1", eyes = "down", mouth = "lipbite", blush = 1)

        ch_Rogue "Please do, [Rogue.Player_petname]. . ." 

    return

label Rogue_accepts_touch_thighs_higher_love:

    return