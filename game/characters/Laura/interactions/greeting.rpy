label Laura_greets_Player:
    $ dice_roll = renpy.random.randint(1, 5)

    if dice_roll == 1:
        $ Laura.change_face("neutral")

        pause 1.0

        $ Laura.change_face("surprised1")

        ch_Laura "Hi."

        $ Laura.eyes = "squint"
    elif dice_roll == 2:
        $ Laura.change_face("confused1")

        ch_Laura "Hey. . ."
    elif dice_roll == 3:
        $ Laura.change_face("neutral")

        pause 1.0

        $ Laura.change_face("angry1", blush = 1)

        ch_Laura "I thought I heard you. . ."

        $ Laura.change_face("smirk2", blush = 0)
    elif dice_roll == 4:
        $ Laura.change_face("surprised2")

        pause 1.0

        $ Laura.change_face("neutral")

        ch_Laura "So it was you. . ."

        $ Laura.eyes = "squint"
    elif dice_roll == 5:
        $ Laura.change_face("neutral")

        pause 1.0

        $ Laura.change_face("angry1")

    return

label Laura_greets_Player_relationship:
    $ dice_roll = renpy.random.randint(1, 5)

    if dice_roll == 1:
        $ Laura.change_face("smirk2")

        ch_Laura "Hey."
    elif dice_roll == 2:
        $ Laura.change_face("neutral")

        pause 1.0

        $ Laura.change_face("pleased2")

        ch_Laura "Good, you're here."

        $ Laura.change_face("smirk2")
    elif dice_roll == 3:
        $ Laura.change_face("smirk2", blush = 1)

        ch_Laura "You smell. . . good."
    elif dice_roll == 4:
        $ Laura.change_face("confused1")

        ch_Laura "Where were you?"
        
        $ Laura.change_face("smirk2")
    elif dice_roll == 5:
        $ Laura.change_face("smirk2")

        ch_Laura "There you are."

    return

label Laura_greets_Player_love:
    if Laura.quirk:
        $ dice_roll = renpy.random.randint(1, 5)
    else:
        $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        $ Laura.change_face("surprised2", blush = 1)

        pause 1.0

        $ Laura.change_face("pleased1")

        ch_Laura "I. . . I'm glad you're here."

        $ Laura.change_face("smirk2")
    elif dice_roll == 2:
        $ Laura.change_face("surprised2")

        pause 1.0

        $ Laura.change_face("smirk2")

        ch_Laura "Came to find me?"

        $ Laura.eyes = "squint"

        ch_Laura "I would've just tracked you down myself."
    elif dice_roll == 3:
        $ Laura.change_face("surprised2")

        pause 1.0

        $ Laura.change_face("sexy", blush = 1)

        ch_Laura "You should. . . come over later."
    elif dice_roll == 4:
        $ Laura.mouth = "lipbite"
        $ Laura.blush = 1

        ch_Laura "Saved me the trouble of tracking you down. . ."
    elif dice_roll == 5:
        $ Laura.change_face("pleased2")

        pause 1.0

        $ Laura.change_face("smirk2")

        ch_Laura "Good, now you're staying with me."

        $ Laura.change_face("sly")

    return

label Laura_greets_Player_mad:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        $ Laura.change_face("angry1")

        pause 1.0

        $ Laura.change_face("appalled1")

        ch_Laura "It's you. . ."
        ch_Laura "{i}Grrrrr{/i}"

        if not Player.location == Laura.home:
            "[Laura.name] turns around and leaves."
        else:
            "[Laura.name] shoves you out the door."

        call getting_kicked_out(Laura) from _call_getting_kicked_out_34
    elif dice_roll == 2:
        $ Laura.change_face("angry1")

        ch_Laura "The fuck have you been up to?"

        $ Laura.eyes = "squint"
    elif dice_roll == 3:
        $ Laura.change_face("appalled2")

        pause 1.0

        $ Laura.change_face("angry1")

        ch_Laura "The fuck do you want?"

    return

label Laura_greets_Player_heartbroken:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        $ Laura.change_face("surprised2")

        pause 1.0

        $ Laura.change_face("worried2")

        pause 1.0

        $ Laura.change_face("appalled2")

        pause 1.0

        $ Laura.change_face("worried1", eyes = "down")

        ch_Laura "Hey. . ."
    elif dice_roll == 2:
        $ Laura.change_face("angry1")

        ch_Laura "I. . ."

        $ Laura.change_face("worried1")

        ch_Laura "{size=-5}fuck{/size}. . ."
    elif dice_roll == 3:
        $ Laura.change_face("worried3")

        pause 1.0

        $ Laura.change_face("angry1")

        ch_Laura "Hi. . ."

        $ Laura.eyes = "down"

    return

label Laura_greets_Player_horny:
    if Laura in Partners:
        $ dice_roll = renpy.random.randint(1, 4)
    else:
        $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Laura.change_face("sexy")

        pause 1.0

        $ Laura.change_face("angry1", mouth = "lipbite", blush = 1)

        ch_Laura "Why do you smell so good. . ."
    elif dice_roll == 2:
        $ Laura.change_face("surprised2", blush = 1)

        ch_Laura "The hell did you come from?"
        
        $ Laura.change_face("angry1", mouth = "lipbite")

        ch_Laura "I wasn't distracted. . ."
        ch_Laura "It's your fault anyway."

        $ Laura.change_face("furious")
    elif dice_roll == 3:
        $ Laura.change_face("surprised2")

        pause 1.0

        $ Laura.change_face("sexy", blush = 1)

        ch_Laura "I might jump you later."

        $ Laura.eyes = "squint"
    elif dice_roll == 4:
        $ Laura.change_face("pleased1")

        pause 1.0

        $ Laura.change_face("sexy", blush = 1)

        ch_Laura "You smell particularly good right now. . ."

    return

label Laura_greets_Player_nympho:
    if Laura.quirk:
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    if dice_roll == 1:
        $ Laura.change_face("angry1")

        pause 1.0

        $ Laura.mouth = "lipbite"
        $ Laura.blush = 1

        ch_Laura "You're the reason I'm like this."
        ch_Laura "I. . . need you later."

        $ Laura.blush = 2
    elif dice_roll == 2:
        $ Laura.change_face("surprised2")

        pause 1.0

        $ Laura.change_face("manic", blush = 2)

        ch_Laura "Save your energy for later. . ."

        $ Laura.change_face("sexy")

        ch_Laura "You'll need it."

        $ Laura.eyes = "down"

        pause 1.0

        $ Laura.eyes = "neutral"

    return

label Laura_greets_Rogue:
    if Laura.sprite_position[0] < Rogue.sprite_position[0]:
        $ Laura_eyes = "left"
        $ Rogue_eyes = "right"
    else:
        $ Laura_eyes = "right"
        $ Rogue_eyes = "left"

    $ Laura.eyes = Laura_eyes
    $ Rogue.eyes = Rogue_eyes

    if Laura in Partners and Rogue in Partners:
        $ Laura.change_face("smirk2", eyes = Laura_eyes)

        ch_Laura "Hello, Rogue."

        $ Rogue.change_face("pleased2", eyes = Rogue_eyes)

        ch_Rogue "X-23!"
        ch_Rogue "You two havin' fun without me?"

        $ Rogue.change_face("sly", eyes = Rogue_eyes)
        $ Laura.change_face("sly", eyes = Laura_eyes)

        ch_Laura "Not yet. . ."
    elif Laura in Partners:
        "[Laura.name] moves closer to you, butting a hand on your arm. . ."
        ch_Laura "Hey. . . Rogue."

        $ Rogue.change_face("confused1", eyes = Rogue_eyes)

        ch_Rogue "Hey. . ."
    elif Rogue in Partners:
        "[Rogue.name] presses herself up against you."
        ch_Laura "Hi, Rogue. . ."
        ch_Rogue "Howdy, X-23."
    else:
        $ dice_roll = renpy.random.randint(1, 2)

        if dice_roll == 1:
            ch_Laura "Hey, Rogue."
            
            $ Rogue.change_face("smirk2", eyes = Rogue_eyes)

            ch_Rogue "Howdy."
            ch_Rogue "Doin' alright, darlin'?"

            $ Laura.change_face("smirk1", eyes = Laura_eyes)

            ch_Laura "Yes. . ."
        elif dice_roll == 2:
            ch_Laura "Oh, hi. . . Rogue."
            ch_Rogue "Glad to see ya, X-23."

    $ Laura.eyes = "neutral"
    $ Rogue.eyes = "neutral"

    return

label Laura_greets_Jean:
    if Laura.sprite_position[0] < Jean.sprite_position[0]:
        $ Laura_eyes = "left"
        $ Jean_eyes = "right"
    else:
        $ Laura_eyes = "right"
        $ Jean_eyes = "left"

    $ Laura.eyes = Laura_eyes
    $ Jean.eyes = Jean_eyes

    if Laura in Partners and Jean in Partners:
        $ Laura.change_face("angry1", eyes = Laura_eyes)

        ch_Laura "Hey, Jean. . ."
        ch_Laura "[Player.first_name] is mine later, got it?"
        
        $ Jean.change_face("smirk2", eyes = Jean_eyes)

        ch_Jean "Hey, X-23."
        ch_Jean "We'll see about that. . ."
    elif Laura in Partners:
        "[Laura.name] walks up next to you."

        ch_Laura "Hi. . . Jean."
        ch_Jean "Looks like you two are getting close. . ."
        ch_Laura "We are."
        "[Laura.name] puts a hand on your shoulder."
    elif Jean in Partners:
        "[Jean.name] puts a hand on your shoulder."
        ch_Laura "Hello, Jean. . ."
        ch_Jean "Hey, X-23."
        ch_Jean "Need something?"
    else:
        $ dice_roll = renpy.random.randint(1, 2)

        if dice_roll == 1:
            ch_Laura "Oh, Jean's here. . ."
            ch_Jean "Hey!"
        elif dice_roll == 2:
            ch_Laura "Hi. . . Jean. . ."
            ch_Jean "Oh!"
            ch_Jean "I had some questions about your workout routine."
            ch_Laura "Later. . ."

    $ Laura.eyes = "neutral"
    $ Jean.eyes = "neutral"

    return

label Laura_simple_greeting:
    ch_Laura "Hey, [Player.first_name]."

    return