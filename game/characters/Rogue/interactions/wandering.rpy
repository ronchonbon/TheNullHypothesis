label Rogue_arrives(arriving_Characters):
    $ dice_roll = renpy.random.randint(1, 5)

    if dice_roll == 1:
        $ Rogue.change_face("surprised1")

        ch_Rogue "Oh! Howdy."

        $ Rogue.change_face("smirk2")
    elif dice_roll == 2:
        $ Rogue.change_face("smirk2", blush = 1)

        if len(arriving_Characters) > 1:
            ch_Rogue "We were hopin' we'd find you here. . ."
        else:
            ch_Rogue "Was hopin' ah'd find you here. . ."
    elif dice_roll == 3:
        $ Rogue.change_face("surprised2")

        pause 1.0

        $ Rogue.change_face("pleased2")

        ch_Rogue "Hey sugar!"

        $ Rogue.change_face("smirk2")
    elif dice_roll == 4:
        $ Rogue.change_face("smirk2")

        ch_Rogue "Nice to see ya, hon'."
    elif dice_roll == 5:
        $ Rogue.change_face("pleased1")

        ch_Rogue "Howdy, [Player.first_name]."

    return

label Rogue_arrives_relationship(arriving_Characters):
    $ dice_roll = renpy.random.randint(1, 5)

    if dice_roll == 1:
        $ Rogue.change_face("surprised1")

        pause 1.0

        $ Rogue.change_face("pleased1")

        if len(arriving_Characters) > 1:
            ch_Rogue "There ya are, we were lookin' for ya."
        else:
            ch_Rogue "There ya are, ah was lookin' for ya."

        $ Rogue.change_face("smirk2")
    elif dice_roll == 2:
        $ Rogue.change_face("pleased2")

        ch_Rogue "Hey sugar."

        $ Rogue.change_face("smirk2", mouth = "lipbite")
    elif dice_roll == 3:
        $ Rogue.change_face("surprised2")

        pause 1.0

        $ Rogue.change_face("pleased2")

        ch_Rogue "Fancy seein' you here, handsome!"

        $ Rogue.change_face("smirk2")
    elif dice_roll == 4:
        $ Rogue.change_face("surprised2")

        pause 1.0

        $ Rogue.change_face("pleased2")

        ch_Rogue "Hey stud-muffin."

        $ Rogue.change_face("smirk2")

        ch_Rogue "We gotta hang out later."
    elif dice_roll == 5:
        $ Rogue.change_face("pleased2")

        ch_Rogue "Hey handsome. . ."
        ch_Rogue "Glad yer here."

        $ Rogue.change_face("smirk2")

    return

label Rogue_arrives_love(arriving_Characters):
    $ dice_roll = renpy.random.randint(1, 5)

    if dice_roll == 1:
        $ Rogue.change_face("surprised2")

        pause 1.0

        $ Rogue.change_face("pleased1")

        if len(arriving_Characters) > 1:
            ch_Rogue "Hey there. . . we missed ya."
        else:
            ch_Rogue "Hey there. . . ah missed ya."
    elif dice_roll == 2:
        $ Rogue.change_face("pleased2")

        $ temp = Rogue.Player_petname.capitalize()

        ch_Rogue "[temp]! Always happy to see ya."
    elif dice_roll == 3:
        $ Rogue.change_face("pleased2")

        ch_Rogue "Hey beau! Aren't you a sight for sore eyes."
    elif dice_roll == 4:
        $ Rogue.change_face("surprised2")

        pause 1.0

        $ Rogue.change_face("pleased2")

        ch_Rogue "There ya are."

        $ Rogue.change_face("smirk2")

        if len(arriving_Characters) > 1:
            ch_Rogue "We've been lookin' for ya."
        else:
            ch_Rogue "Ah've been lookin' for ya."
    elif dice_roll == 5:
        $ Rogue.change_face("pleased2")

        if len(arriving_Characters) > 1:
            ch_Rogue "We knew you'd be here."
        else:
            ch_Rogue "Ah knew you'd be here."

        $ Rogue.change_face("smirk2")

    return

label Rogue_arrives_mad(arriving_Characters):
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        $ Rogue.change_face("surprised2")

        pause 1.0

        $ Rogue.change_face("angry1")

        ch_Rogue "Ah see yer already here. . ."
    elif dice_roll == 2:
        $ Rogue.change_face("worried2")

        pause 1.0

        $ Rogue.change_face("angry1", eyes = "down")

        ch_Rogue "Ah don't wanna talk right now. . ."

        $ Rogue.eyes = "right"
    elif dice_roll == 3:
        $ Rogue.change_face("surprised2")

        ch_Rogue "Oh. . ."

        $ Rogue.change_face("angry1")

        ch_Rogue "Howdy. . ."

    return

label Rogue_arrives_heartbroken(arriving_Characters):
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        $ Rogue.change_face("surprised2")

        pause 1.0

        $ Rogue.change_face("worried1")

        ch_Rogue "Ah. . ."

        $ Rogue.eyes = "down"

        ch_Rogue "Never mind."
    elif dice_roll == 2:
        $ Rogue.change_face("worried2")

        pause 1.0

        $ Rogue.change_face("sad")

        ch_Rogue "Hey."

        $ Rogue.change_face("worried1")
    elif dice_roll == 3:
        $ Rogue.change_face("worried3")

        pause 1.0

        $ Rogue.change_face("worried1")

        ch_Rogue "Oh. . . why. . ."

        $ Rogue.eyes = "down"

        ch_Rogue "{size=-5}Never mind{/size}."

    return

label Rogue_arrives_horny(arriving_Characters):
    $ dice_roll = renpy.random.randint(1, 4)

    if dice_roll == 1:
        $ Rogue.change_face("pleased2")

        pause 1.0

        $ Rogue.change_face("sexy", blush = 1)

        if len(arriving_Characters) > 1:
            ch_Rogue "Mmm, we were lookin' for ya. . ."
        else:
            ch_Rogue "Mmm, ah was lookin' for ya. . ."

        $ Rogue.eyes = "down"
        
        pause 1.0

        $ Rogue.eyes = "sexy"
    elif dice_roll == 2:
        $ Rogue.change_face("sexy", blush = 1)

        ch_Rogue "There ya are. . ."
        ch_Rogue "Been thinkin' 'bout ya."
    elif dice_roll == 3:
        $ Rogue.change_face("surprised2", blush = 1)

        ch_Rogue "Hey, [Player.first_name]. . ."

        $ Rogue.mouth = "lipbite"

        ch_Rogue "Been wonderin' where ya were."
    elif dice_roll == 4:
        $ Rogue.change_face("surprised2")

        pause 1.0

        $ Rogue.change_face("worried2", blush = 1)

        ch_Rogue "Howdy, hunk. . ."

    return

label Rogue_arrives_nympho(arriving_Characters):
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Rogue.change_face("worried2")

        pause 1.0

        $ Rogue.change_face("manic", blush = 2)

        ch_Rogue "Hon'. . . good thing yer here. . ."
    elif dice_roll == 2:
        $ Rogue.change_face("sexy", blush = 1)

        ch_Rogue "There ya are."

        $ Rogue.change_face("manic")

        ch_Rogue "Could use some attention later. . ."

    return

label Rogue_leaves(leaving_Characters, also_leaving = False):
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        if also_leaving:
            ch_Rogue "Yeah, see ya around, hon'."
        else:
            ch_Rogue "See ya around, hon'."
    elif dice_roll == 2:
        if also_leaving:
            if len(leaving_Characters) > 1:
                ch_Rogue "Yeah, gotta head out too, we'll see ya around."
            else:
                ch_Rogue "Yeah, gotta head out too, ah'll see ya around."
        else:
            if len(leaving_Characters) > 1:
                ch_Rogue "Gotta head out, we'll see ya around."
            else:
                ch_Rogue "Gotta head out, ah'll see ya around."
    elif dice_roll == 3:
        ch_Rogue "Bye, [Player.first_name]!"

    return

label Rogue_leaves_relationship(leaving_Characters, also_leaving = False):
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        $ Rogue.change_face("worried1")

        if also_leaving:
            ch_Rogue "Can't stick around either, sorry sugar."
        else:
            ch_Rogue "Can't stick around, sorry sugar."
    elif dice_roll == 2:
        $ Rogue.change_face("worried1")

        if also_leaving:
            ch_Rogue "Gotta go for now too, ah'm sorry."
        else:
            ch_Rogue "Gotta go for now, ah'm sorry."
    elif dice_roll == 3:
        if also_leaving:
            if len(leaving_Characters) > 1:
                ch_Rogue "Sorry, [Player.first_name], we're headin' out too."
            else:
                ch_Rogue "Sorry, [Player.first_name], ah'm headin' out too."
        else:
            if len(leaving_Characters) > 1:
                ch_Rogue "Sorry, [Player.first_name], we're headin' out."
            else:
                ch_Rogue "Sorry, [Player.first_name], ah'm headin' out."

    return

label Rogue_leaves_love(leaving_Characters, also_leaving = False):
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        if also_leaving:
            if len(leaving_Characters) > 1:
                ch_Rogue "Gotta go too, but we'll see ya later. Right?"
            else:
                ch_Rogue "Gotta go too, but ah'll see ya later. Right?"
        else:
            if len(leaving_Characters) > 1:
                ch_Rogue "Gotta go, but we'll see ya later. Right?"
            else:
                ch_Rogue "Gotta go, but ah'll see ya later. Right?"
    elif dice_roll == 2:
        $ Rogue.change_face("worried1")

        if also_leaving:
            if len(leaving_Characters) > 1:
                ch_Rogue "We gotta go too. . . ah'll be missin' ya."
            else:
                ch_Rogue "Ah gotta go too. . . ah'll be missin' ya."
        else:
            if len(leaving_Characters) > 1:
                ch_Rogue "We gotta go. . . ah'll be missin' ya."
            else:
                ch_Rogue "Ah gotta go. . . ah'll be missin' ya."
    elif dice_roll == 3:
        if len(leaving_Characters) > 1:
            ch_Rogue "Bye, [Player.first_name]! Hopefully we'll see ya later."
        else:
            ch_Rogue "Bye, [Player.first_name]! Hopefully ah'll see ya later."

    return

label Rogue_leaves_mad(leaving_Characters, also_leaving = False):
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Rogue.change_face("angry1")

        ch_Rogue "Gotta go."
    elif dice_roll == 2:
        ch_Rogue ". . ."

        $ Rogue.change_face("angry1")

    return

label Rogue_leaves_heartbroken(leaving_Characters, also_leaving = False):
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Rogue.change_face("worried1")

        ch_Rogue "Maybe we. . . {size=-5}never mind{/size}. . . bye."

        $ Rogue.change_face("sad")
    elif dice_roll == 2:
        if also_leaving:
            ch_Rogue "Ah. . . gotta go."
        else:
            ch_Rogue "Ah. . . gotta go too."

        $ Rogue.change_face("worried1")

    return

label Rogue_leaves_horny(leaving_Characters, also_leaving = False):
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        if len(leaving_Characters) > 1:
            ch_Rogue "Wish we could stick around. . ."
        else:
            ch_Rogue "Wish ah could stick around. . ."

        $ Rogue.blush = 1
        $ Rogue.eyes = "down"

        pause 1.0

        $ Rogue.eyes = "sexy"
    elif dice_roll == 2:
        $ Rogue.mouth = "lipbite"

        if len(leaving_Characters) > 1:
            ch_Rogue "Wish we could stick with ya. . . but we gotta go."
        else:
            ch_Rogue "Wish ah could stick with ya. . . but ah gotta go."

    return

label Rogue_leaves_nympho(leaving_Characters, also_leaving = False):
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        if also_leaving:
            ch_Rogue "Gotta go, but ah need some attention later. . ."
        else:
            ch_Rogue "Gotta go too, but ah need some attention later. . ."

        $ Rogue.change_face("worried1", mouth = "lipbite")
    elif dice_roll == 2:
        if also_leaving:
            ch_Rogue "Can't stay, but ah hope you'll have time for me later. . ."
        else:
            ch_Rogue "Can't stay either, but ah hope you'll have time for me later. . ."

        $ Rogue.mouth = "lipbite"

    return