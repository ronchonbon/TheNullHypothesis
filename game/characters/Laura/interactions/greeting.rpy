label Laura_greets_Player:
    if Laura.History.check("seen_Player", tracker = "recent") or Laura.History.check("seen_Player", tracker = "last"):
        $ modifier = " again"
    else:
        $ modifier = ""

    $ dice_roll = renpy.random.randint(1, 5)

    if dice_roll == 1:
        $ Laura.change_face("neutral")

        pause 1.0

        $ Laura.change_face("surprised1")

        ch_Laura "Hi[modifier]."

        $ Laura.eyes = "squint"
    elif dice_roll == 2:
        $ Laura.change_face("confused1")

        ch_Laura "Hey[modifier]. . ."
    elif dice_roll == 3:
        $ Laura.change_face("neutral")

        pause 1.0

        $ Laura.change_face("angry1", blush = 1)

        ch_Laura "I thought I heard you[modifier]. . ."

        $ Laura.change_face("smirk2", blush = 0)
    elif dice_roll == 4:
        $ Laura.change_face("surprised2")

        pause 1.0

        $ Laura.change_face("neutral")

        ch_Laura "So, it was you[modifier]. . ."

        $ Laura.eyes = "squint"
    elif dice_roll == 5:
        $ Laura.change_face("neutral")

        pause 1.0

        $ Laura.change_face("angry1")

    return

label Laura_greets_Player_relationship:
    if Laura.History.check("seen_Player", tracker = "recent") or Laura.History.check("seen_Player", tracker = "last"):
        $ modifier = " again"
    else:
        $ modifier = ""

    $ dice_roll = renpy.random.randint(1, 5)

    if dice_roll == 1:
        $ Laura.change_face("smirk2")

        ch_Laura "Hey[modifier]."
    elif dice_roll == 2:
        $ Laura.change_face("neutral")

        pause 1.0

        $ Laura.change_face("pleased2")

        if modifier == " again" and Laura.History.check("seen_Player", tracker = "recent"):
            ch_Laura "Good, you're back."
        else:
            ch_Laura "Good, you're here."

        $ Laura.change_face("smirk2")
    elif dice_roll == 3:
        $ Laura.change_face("smirk2", blush = 1)

        ch_Laura "You smell. . . good."
    elif dice_roll == 4:
        $ Laura.change_face("confused1")

        if modifier == " again" and Laura.History.check("seen_Player", tracker = "recent"):
            ch_Laura "Where did you go?"
        else:
            ch_Laura "Where were you?"
        
        $ Laura.change_face("smirk2")
    elif dice_roll == 5:
        $ Laura.change_face("smirk2")

        ch_Laura "There you are[modifier]."

    return

label Laura_greets_Player_love:
    if Laura.History.check("seen_Player", tracker = "recent") or Laura.History.check("seen_Player", tracker = "last"):
        $ modifier = " again"
    else:
        $ modifier = ""
        
    if Laura.check_traits("quirk"):
        $ dice_roll = renpy.random.randint(1, 5)
    else:
        $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        $ Laura.change_face("surprised2", blush = 1)

        pause 1.0

        $ Laura.change_face("pleased1")

        if modifier == " again" and Laura.History.check("seen_Player", tracker = "recent"):
            ch_Laura "I. . . I'm glad you're back."
        else:
            ch_Laura "I. . . I'm glad you're here[modifier]."

        $ Laura.change_face("smirk2")
    elif dice_roll == 2:
        $ Laura.change_face("surprised2")

        pause 1.0

        $ Laura.change_face("smirk2")

        if modifier == " again" and Laura.History.check("seen_Player", tracker = "recent"):
            ch_Laura "Came back for me?"
        else:
            ch_Laura "Trying to find me?"

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

        ch_Laura "Now I don't have to track you down. . ."
    elif dice_roll == 5:
        $ Laura.change_face("pleased2")

        pause 1.0

        $ Laura.change_face("smirk2")

        ch_Laura "Good, now you're staying with me."

        $ Laura.change_face("sly")

    return

label Laura_greets_Player_mad:
    if Laura.History.check("seen_Player", tracker = "recent") or Laura.History.check("seen_Player", tracker = "last"):
        $ modifier = " again"
    else:
        $ modifier = ""

    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        $ Laura.change_face("angry1")

        pause 1.0

        $ Laura.change_face("appalled1")

        ch_Laura "It's you[modifier]. . ."
        ch_Laura "{i}Grrrrr{/i}"

        if not Player.location == Laura.home:
            "[Laura.name] turns around and leaves."
        else:
            "[Laura.name] shoves you out the door."

        call getting_kicked_out(Laura) from _call_getting_kicked_out_34
    elif dice_roll == 2:
        $ Laura.change_face("angry1")

        if modifier == " again":
            ch_Laura "What are up to now?"
        else:
            ch_Laura "What have you been up to?"

        $ Laura.eyes = "squint"
    elif dice_roll == 3:
        $ Laura.change_face("appalled2")

        pause 1.0

        $ Laura.change_face("angry1")

        if modifier == " again":
            ch_Laura "What do you want now?"
        else:
            ch_Laura "What do you want?"

    return

label Laura_greets_Player_heartbroken:
    if Laura.History.check("seen_Player", tracker = "recent") or Laura.History.check("seen_Player", tracker = "last"):
        $ modifier = " again"
    else:
        $ modifier = ""

    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        $ Laura.change_face("surprised2")

        pause 1.0

        $ Laura.change_face("worried2")

        pause 1.0

        $ Laura.change_face("appalled2")

        pause 1.0

        $ Laura.change_face("worried1", eyes = "down")

        ch_Laura "Hey[modifier]. . ."
    elif dice_roll == 2:
        $ Laura.change_face("angry1")

        ch_Laura "I. . ."

        $ Laura.change_face("worried1")

        ch_Laura "{size=-5}shit{/size}. . ."
    elif dice_roll == 3:
        $ Laura.change_face("worried3")

        pause 1.0

        $ Laura.change_face("angry1")

        ch_Laura "Hi[modifier]. . ."

        $ Laura.eyes = "down"

    return

label Laura_greets_Player_horny:
    if Laura.History.check("seen_Player", tracker = "recent") or Laura.History.check("seen_Player", tracker = "last"):
        $ modifier = " again"
    else:
        $ modifier = ""
        
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
    if Laura.History.check("seen_Player", tracker = "recent") or Laura.History.check("seen_Player", tracker = "last"):
        $ modifier = " again"
    else:
        $ modifier = ""
        
    if Laura.check_traits("quirk"):
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

        ch_Rogue "[Laura.public_name]!"
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
        ch_Rogue "Howdy, [Laura.public_name]."
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
            ch_Rogue "Glad to see ya, [Laura.public_name]."

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

        ch_Laura "Hey, [Jean.public_name]. . ."
        ch_Laura "[Player.first_name] is mine later, got it?"
        
        $ Jean.change_face("smirk2", eyes = Jean_eyes)

        ch_Jean "Hey, [Laura.public_name]."
        ch_Jean "We'll see about that. . ."
    elif Laura in Partners:
        "[Laura.name] walks up next to you."

        ch_Laura "Hi. . . Jean."
        ch_Jean "Looks like you two are getting close. . ."
        ch_Laura "We are."
        "[Laura.name] puts a hand on your shoulder."
    elif Jean in Partners:
        "[Jean.name] puts a hand on your shoulder."
        ch_Laura "Hello, [Jean.public_name]. . ."
        ch_Jean "Hey, [Laura.public_name]."
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
    if Laura.History.check("seen_Player", tracker = "recent") or Laura.History.check("seen_Player", tracker = "last"):
        $ modifier = " again"
    else:
        $ modifier = ""

    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        ch_Laura "Hey[modifier], [Player.first_name]."
    elif dice_roll == 2:
        ch_Laura "Hey[modifier]."

    return