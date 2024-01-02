label Rogue_rejects_touch_pussy_over_clothes:
    $ Rogue.change_face("surprised2", mouth = "lipbite", blush = 1) 

    ch_Rogue "My. . ."

    $ Rogue.change_face("worried2", mouth = "lipbite", blush = 1) 

    ch_Rogue "Ah'm definitely not ready for that, [Rogue.Player_petname]. . ."
    ch_Rogue "Even over my clothes."

    return

label Rogue_accepts_touch_pussy_over_clothes_first_time:
    $ Rogue.change_face("surprised2", mouth = "lipbite", blush = 2) 

    ch_Rogue "My. . ." 

    $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

    ch_Rogue "Yeah, okay."
    ch_Rogue "But just over my clothes."

    return

label Rogue_accepts_touch_pussy_over_clothes_second_time:

    return

label Rogue_accepts_touch_pussy_over_clothes:
    if Rogue.check_traits("quirk"):
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    if dice_roll == 1:
        $ Rogue.change_face("pleased2", mouth = "lipbite", blush = 1) 

        ch_Rogue "Ah love when you put your hand there. . ." 

        $ Rogue.change_face("sexy", blush = 2) 
    elif dice_roll == 2:
        $ Rogue.change_face("worried2", mouth = "lipbite", blush = 1) 

        ch_Rogue "Please do, [Rogue.Player_petname]."
        ch_Rogue "Are ya gonna touch me under my clothes too?"

        $ Rogue.change_face("worried1", mouth = "lipbite", blush = 2) 

    return

label Rogue_accepts_touch_pussy_over_clothes_love:

    return

label Rogue_rejects_touch_pussy:
    $ Rogue.change_face("surprised2", mouth = "lipbite", blush = 1) 

    ch_Rogue "My. . ."

    $ Rogue.change_face("worried2", mouth = "lipbite", blush = 1) 

    ch_Rogue "Ah'm definitely not ready for that, [Rogue.Player_petname]. . ."

    return

label Rogue_accepts_touch_pussy_first_time:
    $ Rogue.change_face("surprised2", mouth = "lipbite", blush = 2) 

    ch_Rogue "My. . ." 

    $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

    ch_Rogue "Yeah, okay."
    ch_Rogue "Ah think ah'm ready. . ."

    return

label Rogue_accepts_touch_pussy_second_time:

    return

label Rogue_accepts_touch_pussy:
    if Rogue.check_traits("quirk"):
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    if dice_roll == 1:
        $ Rogue.change_face("pleased2", mouth = "lipbite", blush = 1) 

        ch_Rogue "Ah could really use a release. . ." 

        $ Rogue.change_face("sexy", blush = 2) 
    elif dice_roll == 2:
        $ Rogue.change_face("worried2", mouth = "lipbite", blush = 1) 

        ch_Rogue "Please do, [Rogue.Player_petname]."
        ch_Rogue "Are ya gonna. . . let me go all the way this time?"

        $ Rogue.change_face("worried1", mouth = "lipbite", blush = 2) 

    return

label Rogue_accepts_touch_pussy_love:

    return
    
label Rogue_rejects_finger_pussy:
    $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

    if Rogue.check_traits("virgin"):
        ch_Rogue "Ah've never put anything in there before. . ."

        $ Rogue.change_face("worried1", eyes = "down", mouth = "lipbite", blush = 1)

    ch_Rogue ". . . sorry, no." 

    return

label Rogue_accepts_finger_pussy_first_time:
    $ Rogue.change_face("worried2", mouth = "lipbite", blush = 1)

    if Rogue.check_traits("virgin"):
        ch_Rogue "Ah've never put anything in there before. . ."

        $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

    ch_Rogue "Please be gentle." 

    return

label Rogue_accepts_finger_pussy_second_time:

    return

label Rogue_accepts_finger_pussy:
    $ Rogue.change_face("smirk2", mouth = "lipbite", blush = 1)

    ch_Rogue "You could. . ."

    $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

    ch_Rogue "Maybe use more than one finger too?" 

    return

label Rogue_accepts_finger_pussy_love:

    return

label Rogue_rejects_eat_pussy:
    $ Rogue.change_face("worried1", blush = 1)  

    ch_Rogue "That's too much."
    ch_Rogue "One step at a time, [Rogue.Player_petname]."

    return

label Rogue_accepts_eat_pussy_first_time:
    $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

    ch_Rogue "Ah've always wondered what that feels like. . ."

    return

label Rogue_accepts_eat_pussy_second_time:

    return

label Rogue_accepts_eat_pussy:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Rogue.change_face("worried2", mouth = "lipbite", blush = 1)

        ch_Rogue "Lord, ah would love if ya did. . ."
    elif dice_roll == 2:
        $ Rogue.change_face("surprised2", mouth = "lipbite", blush = 1)

        ch_Rogue "Yes please. . ."

        $ Rogue.change_face("sexy", blush = 2)

        ch_Rogue "Last time was amazin'."

    return

label Rogue_accepts_eat_pussy_love:

    return