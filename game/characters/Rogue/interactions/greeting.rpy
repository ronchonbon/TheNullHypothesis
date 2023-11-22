label Rogue_greets_Player:
    $ dice_roll = renpy.random.randint(1, 5)

    if dice_roll == 1:
        $ Rogue.change_face("neutral")

        pause 1.0

        $ Rogue.change_face("pleased1")

        ch_Rogue "Howdy!"

        $ Rogue.change_face("smirk2")
    elif dice_roll == 2:
        $ Rogue.change_face("smirk2")

        ch_Rogue "Fancy seein' you 'round here."
    elif dice_roll == 3:
        $ Rogue.change_face("neutral")

        pause 1.0

        $ Rogue.change_face("pleased2", blush = 1)

        ch_Rogue "Hey, hon'. . ."

        $ Rogue.change_face("smirk2", blush = 0)
    elif dice_roll == 4:
        $ Rogue.change_face("surprised2")

        pause 1.0

        $ Rogue.change_face("smirk2")

        ch_Rogue "Hey, [Player.first_name]."
    elif dice_roll == 5:
        $ Rogue.change_face("pleased2")

        pause 1.0

        $ Rogue.change_face("smirk2")

        ch_Rogue "Glad to see ya, sugar."

    return

label Rogue_greets_Player_relationship:
    $ dice_roll = renpy.random.randint(1, 5)

    if dice_roll == 1:
        $ Rogue.change_face("smirk2")

        ch_Rogue "Howdy, sugar."
    elif dice_roll == 2:
        $ Rogue.change_face("neutral")

        pause 1.0

        $ Rogue.change_face("pleased2")

        ch_Rogue "Glad to see ya, darlin'."
    elif dice_roll == 3:
        $ Rogue.change_face("smirk2", blush = 1)
        
        ch_Rogue "Howdy, handsome. . ."
    elif dice_roll == 4:
        $ Rogue.change_face("confused1", mouth = "smirk")

        ch_Rogue "Were ya lookin' for me?"

        $ Rogue.change_face("smirk2")
    elif dice_roll == 5:
        $ Rogue.change_face("smirk2")

        ch_Rogue "Yer a sight for sore eyes. . ."

    return

label Rogue_greets_Player_love:
    $ dice_roll = renpy.random.randint(1, 5)

    if dice_roll == 1:
        $ Rogue.mouth = "lipbite"
        $ Rogue.blush = 1

        ch_Rogue "Boy, am ah glad to see you. . ."
    elif dice_roll == 2:
        $ Rogue.change_face("pleased2")

        pause 1.0

        $ Rogue.change_face("happy")

        $ temp = Rogue.Player_petname.capitalize()

        ch_Rogue "[temp]! How ya doin'?."

        $ Rogue.change_face("smirk2")
    elif dice_roll == 3:
        $ Rogue.change_face("surprised2")

        pause 1.0

        $ Rogue.change_face("pleased1", blush = 1)
        
        ch_Rogue "Hey. . . ah missed ya a lot."
    elif dice_roll == 4:
        $ Rogue.change_face("happy")

        pause 1.0

        $ Rogue.change_face("pleased1")

        ch_Rogue "Howdy, lover."
    elif dice_roll == 5:
        $ Rogue.change_face("surprised2")

        pause 1.0

        $ Rogue.change_face("sexy", blush = 1)

        ch_Rogue "Hey beau. . . ah might need some attention later."

    return

label Rogue_greets_Player_mad:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        $ Rogue.change_face("angry1")

        pause 1.0

        $ Rogue.change_face("worried1")

        ch_Rogue ". . ."
        "[Rogue.name] turns around and leaves."

        call remove_Characters(Rogue) from _call_remove_Characters_207
    elif dice_roll == 2:
        $ Rogue.change_face("angry1")

        ch_Rogue "Howdy. . ."

        $ Rogue.eyes = "right"
    elif dice_roll == 3:
        $ Rogue.change_face("appalled2")

        pause 1.0

        $ Rogue.change_face("worried2")

        ch_Rogue "Ah. . . never mind."

    return

label Rogue_greets_Player_heartbroken:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        $ Rogue.change_face("appalled2")

        pause 1.0

        $ Rogue.change_face("worried2")

        pause 1.0

        $ Rogue.eyes = "down"

        ch_Rogue "Hey. . ."

        $ Rogue.change_face("worried1")
    elif dice_roll == 2:
        $ Rogue.change_face("worried1")

        ch_Rogue "Ah. . ."

        $ Rogue.eyes = "down"

        ch_Rogue "{size=-5}damnit{/size}. . ."
    elif dice_roll == 3:
        $ Rogue.change_face("worried3")

        ch_Rogue "Howdy. . ."

        $ Rogue.eyes = "down"

    return

label Rogue_greets_Player_horny:
    if Rogue in Partners:
        $ dice_roll = renpy.random.randint(1, 4)
    else:
        $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Rogue.change_face("sexy")

        pause 1.0

        $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

        ch_Rogue "Could ah maybe. . . see you later?"
    elif dice_roll == 2:
        $ Rogue.change_face("surprised2", blush = 1)

        ch_Rogue "Oh!"

        $ Rogue.change_face("worried1", mouth = "lipbite")

        ch_Rogue "Howdy. . ."
    elif dice_roll == 3:
        $ Rogue.change_face("surprised2")

        pause 1.0

        $ Rogue.change_face("manic", blush = 1)

        ch_Rogue "Hey. . . ah could use some lovin' sometime soon. . ."
    elif dice_roll == 4:
        $ Rogue.change_face("pleased1")

        pause 1.0

        $ Rogue.change_face("sexy", blush = 1)

        ch_Rogue "Well don't you look like a snack right now. . ."

    return

label Rogue_greets_Player_nympho:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Rogue.change_face("surprised2")

        pause 1.0

        $ Rogue.change_face("manic", blush = 2)

        ch_Rogue "Ah hope you're feelin'. . . energetic today."
    elif dice_roll == 2:
        $ Rogue.change_face("worried1")

        pause 1.0

        $ Rogue.mouth = "lipbite"
        $ Rogue.blush = 1

        ch_Rogue "Please don't leave me hangin'. . . ah need. . . {i}you{/i}."

    return

label Rogue_greets_Laura:
    if Rogue.sprite_position[0] < Laura.sprite_position[0]:
        $ Rogue_eyes = "left"
        $ Laura_eyes = "right"
    else:
        $ Rogue_eyes = "right"
        $ Laura_eyes = "left"

    $ Rogue.eyes = Rogue_eyes
    $ Laura.eyes = Laura_eyes

    if Rogue in Partners and Laura in Partners:
        $ Rogue.change_face("happy", eyes = Rogue_eyes)
        
        ch_Rogue "[Laura.name]!"
        ch_Rogue "Glad to see ya."

        $ Rogue.change_face("smirk2", eyes = Rogue_eyes)

        ch_Rogue "You two havin' fun without me?"

        $ Laura.change_face("smirk2", eyes = Laura_eyes)

        ch_Laura "Hey, [Rogue.name]."

        $ Laura.blush = 1

        ch_Laura "Not yet. . ."
    elif Rogue in Partners:
        $ dice_roll = renpy.random.randint(1, 2)

        if dice_roll == 1:
            "[Rogue.name] moves in between you and [Laura.name]."
            ch_Rogue "Howdy, [Laura.public_name]."
            ch_Laura "Hi."
        elif dice_roll == 2:
            "[Rogue.name] brushes up against you."
            ch_Rogue "Oh!"
            ch_Rogue "Hey, [Laura.public_name]."
            ch_Laura ". . ."
    elif Laura in Partners:
        "[Laura.name] gets in between you and [Rogue.name]."
        ch_Rogue "Oh, hey [Laura.public_name]. . ."
    else:
        $ dice_roll = renpy.random.randint(1, 2)

        if dice_roll == 1:
            ch_Rogue "Hey, [Laura.public_name]."
            ch_Rogue "How ya doin'?"
            ch_Laura "Good."
            ch_Rogue "Glad to hear. . ."
        elif dice_roll == 2:
            ch_Rogue "Oh, howdy, [Laura.public_name]."
            ch_Laura "Hello."

    $ Rogue.eyes = "neutral"
    $ Laura.eyes = "neutral"

    return

label Rogue_greets_Jean:
    if Rogue.sprite_position[0] < Jean.sprite_position[0]:
        $ Rogue_eyes = "left"
        $ Jean_eyes = "right"
    else:
        $ Rogue_eyes = "right"
        $ Jean_eyes = "left"

    $ Rogue.eyes = Rogue_eyes
    $ Jean.eyes = Jean_eyes

    if Rogue in Partners and Jean in Partners:
        $ Rogue.change_face("worried1", eyes = Rogue_eyes)

        ch_Rogue "Hey, Jean. . ."
        ch_Rogue "Could ah have some alone time with [Player.first_name]?"

        $ Jean.change_face("smirk2", eyes = Jean_eyes)

        ch_Jean "Hey, Rogue!"
        ch_Jean "Maybe. . . you can hang with both of us for now."
    elif Rogue in Partners:
        "[Rogue.name] walks up next to you."
        ch_Rogue "Howdy, Jean. How's it going?"
        ch_Jean "I'm fine."

        $ Rogue.blush = 1

        ch_Jean "Looks like you two are getting close. . ."
    elif Jean in Partners:
        "[Jean.name] puts a hand on your shoulder."
        ch_Rogue "Howdy, Jean. . . What's up?"
        ch_Jean "Hey, Rogue."
        ch_Jean "Just hanging out with {i}my{/i} boyfriend."
    else:
        $ dice_roll = renpy.random.randint(1, 2)

        if dice_roll == 1:
            ch_Rogue "Hey, Jean."
            ch_Rogue "Nice to see ya."
            ch_Jean "Hey!"
        elif dice_roll == 2:
            ch_Rogue "Jean!"
            ch_Rogue "Could ah get some help with that assignment later?"
            ch_Jean "Got some stuff to do, but afterwards sure!"

    $ Rogue.eyes = "neutral"
    $ Jean.eyes = "neutral"

    return

label Rogue_simple_greeting:
    ch_Rogue "Hey, [Player.first_name]!"

    return