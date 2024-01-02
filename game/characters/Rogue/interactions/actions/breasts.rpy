label Rogue_rejects_touch_breasts_over_clothes:
    $ Rogue.change_face("surprised2", blush = 1)

    ch_Rogue "You wanna feel my breasts?" 

    $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

    ch_Rogue ". . . Ah don't think ah'm ready for that [Rogue.Player_petname]." 

    return

label Rogue_accepts_touch_breasts_over_clothes_first_time:
    $ Rogue.change_face("worried2", eyes = "down", mouth = "lipbite", blush = 1)

    ch_Rogue "Feel me up?" 

    $ Rogue.change_face("sexy", blush = 1) 

    ch_Rogue ". . . Sure, why not?" 

    return

label Rogue_accepts_touch_breasts_over_clothes_second_time:

    return

label Rogue_accepts_touch_breasts_over_clothes:
    if Rogue.check_traits("quirk"):
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    if dice_roll == 1:
        $ Rogue.change_face("sexy", blush = 1)

        ch_Rogue "Mmm. . ." 

        $ Rogue.change_face("sexy", blush = 2) 

        ch_Rogue "Ah'm real glad you want to." 
    elif dice_roll == 2:
        $ Rogue.change_face("worried1", eyes = "down", mouth = "lipbite", blush = 1)

        ch_Rogue "Ah was hopin' you'd wanna. . ." 

        $ Rogue.change_face("sexy", blush = 2) 

        ch_Rogue ". . . they're all yours." 

    return

label Rogue_accepts_touch_breasts_over_clothes_love:

    return

label Rogue_rejects_touch_breasts:
    $ Rogue.change_face("surprised2", blush = 1)

    ch_Rogue "You wanna touch my bare breasts?" 

    $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

    ch_Rogue ". . . Ah don't think ah'm ready for that [Rogue.Player_petname]." 

    return

label Rogue_accepts_touch_breasts_first_time:
    $ Rogue.change_face("worried2", eyes = "down", mouth = "lipbite", blush = 1)

    ch_Rogue "My bare breasts?" 

    $ Rogue.change_face("sexy", blush = 1) 

    ch_Rogue ". . . Ah don't think ah'd mind that." 

    return

label Rogue_accepts_touch_breasts_second_time:

    return

label Rogue_accepts_touch_breasts:
    if Rogue.check_traits("quirk"):
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    if dice_roll == 1:
        $ Rogue.change_face("sexy", blush = 1)

        ch_Rogue "Mmm. . ." 

        $ Rogue.change_face("sexy", blush = 2) 

        ch_Rogue "Ah'm real glad you want to." 
    elif dice_roll == 2:
        $ Rogue.change_face("worried1", eyes = "down", mouth = "lipbite", blush = 1)

        ch_Rogue "Ah was hopin' you'd wanna. . ." 

        $ Rogue.change_face("sexy", blush = 2) 

        ch_Rogue ". . . they're all yours." 

    return

label Rogue_accepts_touch_breasts_love:

    return

label Rogue_rejects_pinch_nipples:
    $ Rogue.change_face("surprised2", mouth = "lipbite", blush = 1) 

    pause 1.0

    $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

    ch_Rogue "That's too rough, [Rogue.Player_petname]."

    return

label Rogue_accepts_pinch_nipples_first_time:
    $ Rogue.change_face("worried2", mouth = "lipbite", blush = 1) 

    pause 1.0 

    $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

    ch_Rogue "You can. . ."
    ch_Rogue "But be gentle, [Rogue.Player_petname]."

    return

label Rogue_accepts_pinch_nipples_second_time:

    return

label Rogue_accepts_pinch_nipples:
    if Rogue.check_traits("quirk"):
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    if dice_roll == 1:
        $ Rogue.change_face("worried2", mouth = "lipbite", blush = 1) 

        pause 1.0

        $ Rogue.change_face("worried1", mouth = "lipbite", blush = 2)

        ch_Rogue "Pinch them harder. . ."
        ch_Rogue "Please, [Rogue.Player_petname]?"
    elif dice_roll == 2:
        $ Rogue.change_face("surprised2", mouth = "lipbite", blush = 1) 

        pause 1.0

        $ Rogue.change_face("sexy", blush = 1)

        ch_Rogue "Ah like that. . ." 

    return

label Rogue_accepts_pinch_nipples_love:

    return

label Rogue_rejects_suck_nipples:
    $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

    ch_Rogue "Hands only for now, [Rogue.Player_petname]. . ."

    return

label Rogue_accepts_suck_nipples_first_time:
    $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

    ch_Rogue "Oh, why not. . ."

    return

label Rogue_accepts_suck_nipples_second_time:

    return

label Rogue_accepts_suck_nipples:
    if Rogue.check_traits("quirk"):
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    if dice_roll == 1:
        $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

        ch_Rogue "Ah really. . . really enjoyed when ya did that last time. . ." 

        $ Rogue.change_face("sexy", blush = 2)
    elif dice_roll == 2:
        $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

        call expose(Rogue, "breasts") from _call_expose_10

        "She just pulls up her top, exposing her breasts, presenting them to you."

        $ Rogue.change_face("worried2", mouth = "lipbite", blush = 2)

    return

label Rogue_accepts_suck_nipples_love:

    return