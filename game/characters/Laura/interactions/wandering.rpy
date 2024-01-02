label Laura_arrives(arriving_Characters):
    $ dice_roll = renpy.random.randint(1, 5)

    if dice_roll == 1:
        $ Laura.change_face("surprised1")

        ch_Laura "Hello."

        $ Laura.change_face("neutral")
    elif dice_roll == 2:
        $ Laura.eyes = "squint"

        ch_Laura "You're here. . ."
    elif dice_roll == 3:
        $ Laura.change_face("surprised2")

        pause 1.0

        $ Laura.change_face("smirk1")

        ch_Laura "Hey."

        $ Laura.change_face("neutral")
    elif dice_roll == 4:
        $ Laura.change_face("angry1")

        ch_Laura ". . ."

        $ Laura.eyes = "down"

        pause 1.0

        $ Laura.eyes = "neutral"
    elif dice_roll == 5:
        $ Laura.eyes = "squint"

        ch_Laura "There you are."

    return

label Laura_arrives_relationship(arriving_Characters):
    $ dice_roll = renpy.random.randint(1, 5)

    if dice_roll == 1:
        $ Laura.change_face("pleased1")

        pause 1.0

        $ Laura.change_face("angry1")

        ch_Laura "Found you."

        $ Laura.eyes = "squint"
    elif dice_roll == 2:
        $ Laura.change_face("smirk2")

        ch_Laura "Hey."

        $ Laura.eyes = "down"

        pause 1.0

        $ Laura.eyes = "neutral"
        $ Laura.mouth = "lipbite"
    elif dice_roll == 3:
        $ Laura.change_face("surprised2")

        pause 1.0

        $ Laura.change_face("pleased2")

        ch_Laura "So that's where you were."

        $ Laura.change_face("smirk2")
    elif dice_roll == 4:
        $ Laura.change_face("pleased2")

        ch_Laura "Knew you were here. . ."

        $ Laura.change_face("smirk2")

        ch_Laura "I could {i}sense{/i} it."
    elif dice_roll == 5:
        $ Laura.change_face("confused1")

        ch_Laura "What are you doing here?"

        $ Laura.eyes = "squint"

    return

label Laura_arrives_love(arriving_Characters):
    if Laura.check_traits("quirk"):
        $ dice_roll = renpy.random.randint(1, 5)
    else:
        $ dice_roll = renpy.random.randint(1, 4)

    if dice_roll == 1:
        $ Laura.change_face("pleased2")

        pause 1.0

        $ Laura.eyes = "squint"

        ch_Laura "Hey. . ."
        ch_Laura "I think. . . I missed you. . ."

        $ Laura.change_face("worried1")

        pause 1.0

        $ Laura.change_face("angry1")
    elif dice_roll == 2:
        $ Laura.change_face("pleased2")
        
        ch_Laura "[Player.first_name], come here."

        $ Laura.change_face("smirk2")

        ch_Laura "I might've been following you. . ."
    elif dice_roll == 3:
        $ Laura.change_face("surprised2")

        pause 1.0

        $ Laura.change_face("pleased2")

        ch_Laura "Knew you'd be here."

        $ Laura.change_face("smirk2")

        ch_Laura "Not hard to track you down. . ."
    elif dice_roll == 4:
        $ Laura.change_face("pleased2")

        ch_Laura "Definitely didn't follow you here. . ."

        $ Laura.change_face("smirk2")
    elif dice_roll == 5:
        $ Laura.change_face("appalled1")

        ch_Laura "[Player.first_name], you trying to lose your tail?"

        $ Laura.change_face("angry1")

        ch_Laura "Don't make me lock you in my room or something."

    return

label Laura_arrives_mad(arriving_Characters):
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        $ Laura.change_face("surprised2")

        pause 1.0

        $ Laura.change_face("angry1")

        ch_Laura "{i}Grrrrr{i}"
    elif dice_roll == 2:
        $ Laura.change_face("appalled1")

        pause 1.0

        $ Laura.change_face("angry1", eyes = "right")

        ch_Laura "Don't speak. . ."
    elif dice_roll == 3:
        $ Laura.change_face("appalled2")

        ch_Laura "What are you doing here?"

        $ Laura.change_face("furious")

    return

label Laura_arrives_heartbroken(arriving_Characters):
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        $ Laura.change_face("worried1")

        pause 1.0

        $ Laura.change_face("appalled1")

        ch_Laura "You. . ."

        $ Laura.eyes = "left"

        pause 1.0

        $ Laura.eyes = "down"
        
        ch_Laura "Never mind."

        $ Laura.change_face("angry1")
    elif dice_roll == 2:
        $ Laura.change_face("sad")

        pause 1.0

        $ Laura.change_face("angry1")

        ch_Laura "Go away. . ."
    elif dice_roll == 3:
        $ Laura.change_face("worried2")

        pause 1.0

        $ Laura.change_face("appalled1")

        ch_Laura "Oh. . . it's you. . ."

        $ Laura.eyes = "right"

        ch_Laura "{size=-5}Go away{/size}. . ."

        $ Laura.change_face("worried1")

    return

label Laura_arrives_horny(arriving_Characters):
    if Laura in Partners:
        $ dice_roll = renpy.random.randint(1, 4)
    else:
        $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Laura.change_face("surprised2")

        pause 1.0

        $ Laura.eyes = "squint"
        $ Laura.blush = 1

        ch_Laura "You. . ."

        $ Laura.mouth = "lipbite"

        ch_Laura "There you are."
    elif dice_roll == 2:
        $ Laura.change_face("surprised2")

        pause 1.0

        $ Laura.change_face("angry1", blush = 1)

        ch_Laura "Why do you. . ."

        $ Laura.eyes = "left"

        ch_Laura "Never mind."

        $ Laura.blush = 2
    elif dice_roll == 3:
        $ Laura.change_face("pleased2")

        pause 1.0

        $ Laura.change_face("sexy", blush = 1)

        ch_Laura "You smell {i}good{/i} right now. . ."

        $ Laura.eyes = "down"

        pause 1.0

        $ Laura.eyes = "sexy"
    elif dice_roll == 4:
        $ Laura.change_face("sexy", blush = 1)

        ch_Laura "Can't hide from me. . ."

    return

label Laura_arrives_nympho(arriving_Characters):
    if Laura.check_traits("quirk"):
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    if dice_roll == 1:
        $ Laura.change_face("sexy", blush = 1)

        ch_Laura "You better not waste anything before I get to you."

        $ Laura.eyes = "down"
        $ Laura.mouth = "lipbite"
    elif dice_roll == 2:
        $ Laura.change_face("manic")

        pause 1.0

        $ Laura.change_face("sexy", blush = 2)

        ch_Laura "You're not getting away from me. . ."
        ch_Laura "I {i}will{/i} have you later. . ."

        $ Laura.eyes = "down"

    return

label Laura_leaves(leaving_Characters, also_leaving = False):
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        ch_Laura ". . . bye."
    elif dice_roll == 2:
        ch_Laura "I'm leaving."
    elif dice_roll == 3:
        ch_Laura "I. . . might see you later."

        $ Laura.eyes = "squint"

        pause 1.0

    return

label Laura_leaves_relationship(leaving_Characters, also_leaving = False):
    if Laura.check_traits("quirk"):
        $ dice_roll = renpy.random.randint(1, 3)
    else:
        $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        ch_Laura "I have to go. You better not get into trouble."

        $ Laura.eyes = "squint"
    elif dice_roll == 2:
        ch_Laura "I'm leaving. Don't go anywhere."

        $ Laura.change_face("angry1")
    elif dice_roll == 3:
        ch_Laura "Bye. . . "
        ch_Laura "You're coming over later."
        ch_Laura "Got it?"

    return

label Laura_leaves_love(leaving_Characters, also_leaving = False):
    if Laura.check_traits("quirk"):
        $ dice_roll = renpy.random.randint(1, 3)
    else:
        $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Laura.change_face("angry1")

        ch_Laura "Don't want to leave you. . . but I have to."
    elif dice_roll == 2:
        ch_Laura "Bye, [Player.first_name]. You'll see me later."
    elif dice_roll == 3:
        ch_Laura "Have to go, but you will come see me later. . ."

        $ Laura.eyes = "down"

        pause 1.0

        $ Laura.eyes = "neutral"

    return

label Laura_leaves_mad(leaving_Characters, also_leaving = False):
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Laura.change_face("angry1")

        ch_Laura ". . ."
    elif dice_roll == 2:
        $ Laura.change_face("angry1")

        ch_Laura "{i}Grrrrr{/i}. . . I'm leaving."

        $ Laura.change_face("furious")

    return

label Laura_leaves_heartbroken(leaving_Characters, also_leaving = False):
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Laura.change_face("angry1")

        ch_Laura "Maybe. . . {size=-5}you{/size}. . ."
        ch_Laura "Never mind."

        $ Laura.change_face("worried1")
    elif dice_roll == 2:
        $ Laura.change_face("furious")

        ch_Laura "Goddamnit. I have to go. . ."

        $ Laura.change_face("worried1")

    return

label Laura_leaves_horny(leaving_Characters, also_leaving = False):
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        ch_Laura "I can't stay. . ."

        $ Laura.blush = 1
        $ Laura.eyes = "down"

        pause 1.0

        $ Laura.eyes = "sexy"
    elif dice_roll == 2:
        $ Laura.mouth = "lipbite"

        ch_Laura "I'm leaving. . . for now."

        $ Laura.change_face("sexy")

    return

label Laura_leaves_nympho(leaving_Characters, also_leaving = False):
    if Laura.check_traits("quirk"):
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    if dice_roll == 1:
        $ Laura.change_face("sexy", blush = 1)

        ch_Laura "Make time later."

        $ Laura.blush = 2

        ch_Laura "I need. . . attention. . ."
    elif dice_roll == 2:
        ch_Laura "You {i}will{/i} see me later. . ."

        $ Laura.change_face("angry1", mouth = "lipbite")

        ch_Laura "Prepare yourself."

    return