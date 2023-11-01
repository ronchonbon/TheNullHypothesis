label Jean_arrives(arriving_Characters):
    $ dice_roll = renpy.random.randint(1, 5)

    if dice_roll == 1:
        $ Jean.change_face("surprised1")

        ch_Jean "Oh! Hey."

        $ Jean.change_face("smirk2")
    elif dice_roll == 2:
        $ Jean.change_face("smirk2", blush = 1)

        ch_Jean "I've been trying to find you. . ."
    elif dice_roll == 3:
        $ Jean.change_face("surprised2")

        pause 1.0

        $ Jean.change_face("pleased2")

        ch_Jean "Hey, [Player.first_name]!"

        $ Jean.change_face("smirk2")
    elif dice_roll == 4:
        $ Jean.change_face("smirk2")

        ch_Jean "Hey, good to see you."
    elif dice_roll == 5:
        $ Jean.change_face("pleased1")

        ch_Jean "Hi!"
        ch_Jean "Just let me know if you need anything."

        $ Jean.change_face("smirk2")

    return

label Jean_arrives_relationship(arriving_Characters):
    $ dice_roll = renpy.random.randint(1, 5)

    if dice_roll == 1:
        $ Jean.change_face("surprised1")

        pause 1.0

        $ Jean.change_face("pleased1")

        ch_Jean "So this is where you were."

        $ Jean.change_face("smirk2")
    elif dice_roll == 2:
        $ Jean.change_face("pleased2")

        ch_Jean "Hey, [Player.first_name]."

        $ Jean.change_face("smirk2", eyes = "down")

        pause 1.0

        $ Jean.eyes = "sexy"
        $ Jean.mouth = "lipbite"
    elif dice_roll == 3:
        $ Jean.change_face("surprised2")

        pause 1.0

        $ Jean.change_face("pleased2")

        ch_Jean "Hey there, hottie."

        $ Jean.change_face("smirk2")
    elif dice_roll == 4:
        $ Jean.change_face("surprised2")

        pause 1.0

        $ Jean.change_face("pleased2")

        ch_Jean "Hey, [Player.first_name]."

        $ Jean.change_face("smirk2")

        ch_Jean "We are totally hanging out later."
    elif dice_roll == 5:
        $ Jean.change_face("pleased2")

        ch_Jean "Happy to see me?"
        ch_Jean "I'm definitely happy to see you."

        $ Jean.change_face("smirk2")

    return

label Jean_arrives_love(arriving_Characters):
    $ dice_roll = renpy.random.randint(1, 5)

    if dice_roll == 1:
        $ Jean.change_face("surprised2")

        pause 1.0

        $ Jean.change_face("happy")

        $ temp = Jean.Player_petname.capitalize()

        ch_Jean "[temp]!"

        $ Jean.change_face("smirk2")

        ch_Jean "I bet you missed me."
    elif dice_roll == 2:
        $ Jean.change_face("pleased2")

        $ temp = Jean.Player_petname.capitalize()

        ch_Jean "[temp]!"

        $ Jean.change_face("smirk2", eyes = "down", mouth = "lipbite")

        pause 1.0

        $ Jean.eyes = "neutral"

        ch_Jean "Man, is it always good to see you."
    elif dice_roll == 3:
        $ Jean.change_face("surprised1")

        pause 1.0

        $ Jean.change_face("pleased2")

        ch_Jean "Damn, looking good."

        $ Jean.change_face("smirk2", mouth = "lipbite")
    elif dice_roll == 4:
        $ Jean.change_face("surprised2")

        pause 1.0

        $ Jean.change_face("pleased2")

        ch_Jean "There you are."

        $ Jean.change_face("smirk2")

        ch_Jean "Better not have been trying to hide from me. . ."
    elif dice_roll == 5:
        $ Jean.change_face("pleased2")

        ch_Jean "Knew I'd find you here."

        $ Jean.change_face("smirk2")

    return

label Jean_arrives_mad(arriving_Characters):
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        $ Jean.change_face("surprised2")

        pause 1.0

        $ Jean.change_face("angry1")

        ch_Jean "Oh, you're already here. . ."
    elif dice_roll == 2:
        $ Jean.change_face("worried2")

        pause 1.0

        $ Jean.change_face("angry1", eyes = "right")

        ch_Jean "Ugh, don't even talk to me. . ."

        $ Jean.change_face("furious")
    elif dice_roll == 3:
        $ Jean.change_face("surprised2")

        ch_Jean "Oh. . ."
        
        $ Jean.change_face("angry1")

        pause 1.0

        $ Jean.change_face("worried1")
        
        ch_Jean "It's you. . ."

        $ Jean.change_face("furious")

    return

label Jean_arrives_heartbroken(arriving_Characters):
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        $ Jean.change_face("surprised2")

        pause 1.0

        $ Jean.change_face("worried1")

        ch_Jean "Why. . ."

        $ Jean.eyes = "down"

        ch_Jean "Goddamnit, never mind."
    elif dice_roll == 2:
        $ Jean.change_face("worried2")

        pause 1.0

        $ Jean.change_face("sad")

        ch_Jean ". . . didn't realize you were here."

        $ Jean.change_face("worried1")
    elif dice_roll == 3:
        $ Jean.change_face("worried3")

        pause 1.0

        $ Jean.change_face("worried1")

        ch_Jean "Oh. . . you. . ."
        
        $ Jean.change_face("angry1", eyes = "right")

        pause 1.0

        ch_Jean "{size=-5}Never mind{/size}. . ."

        $ Jean.change_face("worried1")

    return

label Jean_arrives_horny(arriving_Characters):
    if Jean in Partners:
        $ dice_roll = renpy.random.randint(1, 4)
    else:
        $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Jean.change_face("surprised2", blush = 1)

        ch_Jean "Oh! Heh, hey. . ."

        $ Jean.mouth = "lipbite"

        ch_Jean "Didn't expect. . ."

        $ Jean.eyes = "down"

        pause 1.0

        $ Jean.eyes = "neutral"

        ch_Jean "{i}Ahem{/i}. . ."
    elif dice_roll == 2:
        $ Jean.change_face("surprised2")

        pause 1.0

        $ Jean.change_face("pleased2", blush = 1)

        ch_Jean "Hey there. . ."

        $ Jean.mouth = "lipbite"
    elif dice_roll == 3:
        $ Jean.change_face("pleased2")

        pause 1.0

        $ Jean.change_face("sexy", blush = 1)

        ch_Jean "Mmm, have you always looked this good. . ."

        $ Jean.eyes = "down"

        pause 1.0

        $ Jean.eyes = "sexy"
    elif dice_roll == 4:
        $ Jean.change_face("sexy", blush = 1)

        ch_Jean "Ther you are."
        ch_Jean "Can't get you off my mind. . ."
        ch_Jean "In a good way."

        $ Jean.blush = 2

    return

label Jean_arrives_nympho(arriving_Characters):
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Jean.change_face("surprised2")

        pause 1.0

        $ Jean.change_face("manic", blush = 2)

        $ temp = Jean.Player_petname.capitalize()

        ch_Jean "[temp]. . . I'm getting a bit. . ."
        ch_Jean "I need. . ."

        $ Jean.eyes = "down"
    elif dice_roll == 2:
        $ Jean.change_face("sexy", blush = 1)

        ch_Jean "You're gonna come with me later."

        $ Jean.blush = 2

        ch_Jean "Better save your energy. . ."

    return

label Jean_leaves(leaving_Characters, also_leaving = False):
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        ch_Jean "Bye!"
    elif dice_roll == 2:
        ch_Jean "Gotta go, bye."
    elif dice_roll == 3:
        ch_Jean "See you later!"

    return

label Jean_leaves_relationship(leaving_Characters, also_leaving = False):
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        ch_Jean "God, I wish I could stay and hang with you. . ."
        ch_Jean "I gotta go."

        $ Jean.change_face("worried1")
    elif dice_roll == 2:
        ch_Jean "Gonna head out."

        $ Jean.change_face("sly")

        ch_Jean "Don't miss me too much."
    elif dice_roll == 3:
        ch_Jean "Sorry, [Jean.Player_petname]."
        ch_Jean "I got stuff to do."
        ch_Jean "See you later?"

        $ Jean.change_face("worried1")

    return

label Jean_leaves_love(leaving_Characters, also_leaving = False):
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        ch_Jean "Can't stay, but you'll come around tonight. . . right?"
        
        $ Jean.change_face("worried1")
    elif dice_roll == 2:
        $ Jean.change_face("smirk2")

        ch_Jean "Gotta go, you better miss me sooo much."

        $ Jean.change_face("sly")
    elif dice_roll == 3:
        ch_Jean "Bye, [Jean.Player_petname]."
        ch_Jean "You're definitely gonna see me later."

        $ Jean.change_face("sly")

    return

label Jean_leaves_mad(leaving_Characters, also_leaving = False):
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Jean.change_face("angry1")

        ch_Jean "Don't follow me."
    elif dice_roll == 2:
        ch_Jean "Ugh. . ."

        $ Jean.change_face("angry1")

    return

label Jean_leaves_heartbroken(leaving_Characters, also_leaving = False):
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Jean.change_face("worried1")

        ch_Jean "Why did you. . ."

        $ Jean.eyes = "right"

        ch_Jean "Never mind. . ."

        $ Jean.change_face("sad")
    elif dice_roll == 2:
        ch_Jean "I'm. . . leaving. . ."

        $ Jean.change_face("worried1")

    return

label Jean_leaves_horny(leaving_Characters, also_leaving = False):
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        ch_Jean "You better think dirty thoughts about me while I'm gone. . ."

        $ Jean.eyes = "down"
        $ Jean.blush = 1

        pause 1.0

        $ Jean.eyes = "sexy"
    elif dice_roll == 2:
        $ Jean.mouth = "lipbite"

        ch_Jean "Maybe we can spend some. . . quality time together later. . ."

    return

label Jean_leaves_nympho(leaving_Characters, also_leaving = False):
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        ch_Jean "You're taking care of me later, mister. . ."

        $ Jean.change_face("sexy", mouth = "lipbite")
    elif dice_roll == 2:
        $ Jean.change_face("manic", eyes = "down")

        pause 1.0

        $ Jean.eyes = "sexy"

        ch_Jean "God. . ."
        ch_Jean "You better look this {i}good{/i}when I see you later."

        $ Jean.mouth = "lipbite"

    return