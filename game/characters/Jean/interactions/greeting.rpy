label Jean_greets_Player:
    if Jean.History.check("seen_Player", tracker = "recent") > 1 or Jean.History.check("seen_Player", tracker = "last"):
        $ modifier = " again"
    else:
        $ modifier = ""

    $ dice_roll = renpy.random.randint(1, 5)

    if dice_roll == 1:
        $ Jean.change_face("neutral")

        pause 1.0

        $ Jean.change_face("pleased1")

        ch_Jean "Hey[modifier]!"

        $ Jean.change_face("smirk2")
    elif dice_roll == 2:
        $ Jean.change_face("smirk2", brows = "cocked")

        if modifier == " again":
            ch_Jean "Back for more?"
        else:
            ch_Jean "Trying to find me?"
    elif dice_roll == 3:
        $ Jean.change_face("neutral")

        pause 1.0

        $ Jean.change_face("pleased2", blush = 1)

        ch_Jean "Hey there. . ."

        if modifier == " again":
            ch_Jean ". . . again."

        $ Jean.change_face("smirk2", blush = 0)
    elif dice_roll == 4:
        $ Jean.change_face("surprised2")

        pause 1.0

        $ Jean.change_face("smirk2")

        ch_Jean "Oh, hey[modifier]."
    elif dice_roll == 5:
        $ Jean.change_face("pleased2")

        pause 1.0

        $ Jean.change_face("smirk2")

        ch_Jean "Hope you're glad to see me[modifier]."

    return

label Jean_greets_Player_relationship:
    if Jean.History.check("seen_Player", tracker = "recent") > 1 or Jean.History.check("seen_Player", tracker = "last"):
        $ modifier = " again"
    else:
        $ modifier = ""

    $ dice_roll = renpy.random.randint(1, 5)

    if dice_roll == 1:
        $ Jean.change_face("smirk2")

        if modifier == " again":
            ch_Jean "Oh, it's you again!"
        else:
            ch_Jean "Hey, I was wondering where you were."
    elif dice_roll == 2:
        $ Jean.change_face("neutral")

        pause 1.0

        $ Jean.change_face("pleased2")

        ch_Jean "Good, you're here[modifier]."

        $ Jean.change_face("smirk2")
    elif dice_roll == 3:
        $ Jean.change_face("smirk2", blush = 1)

        ch_Jean "Damn, you look. . ."
    elif dice_roll == 4:
        $ Jean.change_face("confused1", mouth = "smirk")

        if modifier == " again":
            if Jean.History.check("seen_Player", tracker = "recent") > 1:
                ch_Jean "Where'd you go?"
            else:
                ch_Jean "Here you are!"
        else:
            ch_Jean "Where've you been?"

        $ Jean.change_face("smirk2")
    elif dice_roll == 5:
        $ Jean.change_face("smirk2")

        if modifier == " again":
            if Jean.History.check("seen_Player", tracker = "recent") > 1:
                ch_Jean "I bet you came back just for me. . ."
            else:
                ch_Jean "I bet you missed me. . ."
        else:
            ch_Jean "I bet you're here just for me. . ."

    return

label Jean_greets_Player_love:
    if Jean.History.check("seen_Player", tracker = "recent") > 1 or Jean.History.check("seen_Player", tracker = "last"):
        $ modifier = " again"
    else:
        $ modifier = ""

    $ dice_roll = renpy.random.randint(1, 5)

    if dice_roll == 1:
        $ Jean.mouth = "lipbite"
        $ Jean.blush = 1

        if modifier == " again":
            ch_Jean "Hey[modifier], [Jean.Player_petname]. . ."
        else:
            ch_Jean "Hey there, [Jean.Player_petname]. . ."
    elif dice_roll == 2:
        $ Jean.change_face("pleased2")

        pause 1.0

        $ Jean.change_face("happy")

        $ temp = Jean.Player_petname.capitalize()

        if modifier == " again" and Jean.History.check("seen_Player", tracker = "recent") > 1:
            ch_Jean "[temp]! Missed me that much?"
        else:
            ch_Jean "[temp]! Miss me?"

        $ Jean.change_face("smirk2")
    elif dice_roll == 3:
        $ Jean.change_face("surprised2")

        pause 1.0

        $ Jean.change_face("pleased1", blush = 1)

        ch_Jean "Hey. . . missed you. . ."

        $ Jean.change_face("smirk2")
    elif dice_roll == 4:
        $ Jean.change_face("pleased1")

        if modifier == " again" and Jean.History.check("seen_Player", tracker = "recent") > 1:
            ch_Jean "Came back to find me, right?"
        else:
            ch_Jean "I'm so happy you're here!"
    elif dice_roll == 5:
        $ Jean.change_face("surprised2")

        pause 1.0

        $ Jean.change_face("sexy", blush = 1)

        if modifier == " again" and Jean.History.check("seen_Player", tracker = "recent") > 1:
            ch_Jean "Was just about to come find where you went."
        else:
            ch_Jean "Was just about to come find you."

    return

label Jean_greets_Player_mad:
    if Jean.History.check("seen_Player", tracker = "recent") > 1 or Jean.History.check("seen_Player", tracker = "last"):
        $ modifier = " again"
    else:
        $ modifier = ""

    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        $ Jean.change_face("worried1")

        pause 1.0

        $ Jean.change_face("angry1")

        ch_Jean "I can't be around you right now. . ."

        call Jean_kicking_out from _call_Jean_kicking_out_12
        call getting_kicked_out(Jean) from _call_getting_kicked_out_12
    elif dice_roll == 2:
        $ Jean.change_face("angry1")

        ch_Jean "Ugh, hey[modifier]. . ."

        $ Jean.change_face("right")
    elif dice_roll == 3:
        $ Jean.change_face("appalled2")

        pause 1.0

        $ Jean.change_face("angry1")

        ch_Jean "You're just walking around all nonchalant?!"

    return

label Jean_greets_Player_heartbroken:
    if Jean.History.check("seen_Player", tracker = "recent") > 1 or Jean.History.check("seen_Player", tracker = "last"):
        $ modifier = " again"
    else:
        $ modifier = ""

    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        $ Jean.change_face("surprised3")

        pause 1.0

        $ Jean.change_face("worried2")

        pause 1.0

        $ Jean.eyes = "down"

        ch_Jean "Hey[modifier]. . ."

        $ Jean.change_face("worried1")
    elif dice_roll == 2:
        $ Jean.change_face("angry1")

        pause 1.0

        $ Jean.change_face("worried1")

        ch_Jean "Think you can just. . ."

        $ Jean.eyes = "left"

        ch_Jean ". . . {size=-5}fuck{/size}. . ."
    elif dice_roll == 3:
        $ Jean.change_face("worried3")

        pause 1.0

        $ Jean.change_face("worried1")

        ch_Jean "Hi[modifier]. . ."

        $ Jean.eyes = "right"

    return

label Jean_greets_Player_horny:
    if Jean.History.check("seen_Player", tracker = "recent") > 1 or Jean.History.check("seen_Player", tracker = "last"):
        $ modifier = " again"
    else:
        $ modifier = ""

    if Jean in Partners:
        $ dice_roll = renpy.random.randint(1, 4)
    else:
        $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Jean.change_face("smirk2", mouth = "lipbite", blush = 1)

        ch_Jean "Wanna. . . come over and study later?"
    elif dice_roll == 2:
        $ Jean.change_face("surprised2", blush = 1)

        ch_Jean "Hey[modifier]!"

        $ Jean.change_face("smirk2", mouth = "lipbite")

        ch_Jean "You look. . ."
        ch_Jean ". . . great."
    elif dice_roll == 3:
        $ Jean.change_face("surprised2")

        pause 1.0

        $ Jean.change_face("sexy", blush = 1)

        ch_Jean "Damn. . . are you trying to tempt me?"
    elif dice_roll == 4:
        $ Jean.change_face("pleased1")

        pause 1.0

        $ Jean.change_face("sexy", blush = 1)

        if modifier == " again":
            ch_Jean "Oh, it's you again. . ."
        else:
            ch_Jean "There you are. . ."

        ch_Jean "God, we make a hot couple."

    return

label Jean_greets_Player_nympho:
    if Jean.History.check("seen_Player", tracker = "recent") > 1 or Jean.History.check("seen_Player", tracker = "last"):
        $ modifier = " again"
    else:
        $ modifier = ""

    $ dice_roll = renpy.random.randint(1, 5)

    if dice_roll == 1:
        $ Jean.change_face("surprised2")

        pause 1.0

        $ Jean.change_face("manic", blush = 2)

        if modifier == " again":
            ch_Jean ". . . I might need to steal you later."
        else:
            ch_Jean "There you are. . . I might need to steal you later."
    elif dice_roll == 2:
        $ Jean.change_face("smirk2")

        pause 1.0

        $ Jean.change_face("sexy", blush = 1)

        ch_Jean "You can't just walk around looking that good and expect me to behave."
        
        show expression "images/effects/smack.webp" as smack onlayer effects:
            anchor (0.5, 0.5) pos (0.5, 0.7)

            zoom 0.0
            alpha 0.0
            ease 0.1 zoom 1.0 alpha 1.0
            ease 1.0 alpha 0.0

        with small_screenshake
        
        "She gives your ass a light smack."

    return

label Jean_greets_Rogue:
    if Jean.sprite_position[0] < Rogue.sprite_position[0]:
        $ Jean_eyes = "left"
        $ Rogue_eyes = "right"
    else:
        $ Jean_eyes = "right"
        $ Rogue_eyes = "left"

    $ Jean.eyes = Jean_eyes
    $ Rogue.eyes = Rogue_eyes

    if Jean in Partners and Rogue in Partners:
        $ Jean.change_face("smirk2", eyes = Jean_eyes)

        ch_Jean "Hey, Rogue."
        ch_Jean "Sorry, but I want to hang with [Player.first_name] now."

        $ Rogue.change_face("worried1", eyes = Rogue_eyes)

        ch_Rogue "Oh. . ."
        ch_Rogue "Maybe. . . ah could stay with both of you?"
        
        $ Jean.change_face("smirk2", eyes = Jean_eyes)

        ch_Jean "Oh, okay, fine."
        ch_Jean "I'm feeling generous."
    elif Jean in Partners:
        "[Jean.name] presses against you."
        ch_Jean "Hey, Rogue."

        $ Rogue.change_face("worried1", eyes = Rogue_eyes)

        ch_Rogue "Hi. . ."
        ch_Rogue "You two look. . ."

        $ Rogue.blush = 1
    elif Rogue in Partners:
        "[Rogue.name] presses herself up against you."
        ch_Rogue "Howdy, Jean. . ."
        ch_Jean "Hey, Rogue."
        ch_Jean "Hanging out with your boyfriend?"

        $ Jean.change_face("confused1", eyes = Jean_eyes)
    else:
        $ dice_roll = renpy.random.randint(1, 2)

        if dice_roll == 1:
            ch_Jean "Hey, Rogue!"
            ch_Rogue "Howdy!"
        elif dice_roll == 2:
            ch_Jean "Rogue!"
            ch_Jean "You look cute today."
            ch_Rogue "Aw, thanks darlin'."

    $ Jean.eyes = "neutral"
    $ Rogue.eyes = "neutral"

    return

label Jean_greets_Laura:
    if Jean.sprite_position[0] < Laura.sprite_position[0]:
        $ Jean_eyes = "left"
        $ Laura_eyes = "right"
    else:
        $ Jean_eyes = "right"
        $ Laura_eyes = "left"

    $ Jean.eyes = Jean_eyes
    $ Laura.eyes = Laura_eyes

    if Jean in Partners and Laura in Partners:
        $ Jean.change_face("neutral", eyes = Jean_eyes)

        ch_Jean "[Laura.public_name]."
        ch_Jean "You better not be having too much fun with [Player.first_name]."
        
        $ Laura.change_face("smirk2", eyes = Laura_eyes)

        ch_Laura "That's not up to you."

        $ Laura.change_face("sly")
    elif Jean in Partners:
        $ dice_roll = renpy.random.randint(1, 2)

        if dice_roll == 1:
            "[Jean.name] moves in between you and [Laura.name]."

            $ Jean.change_face("sly", eyes = Jean_eyes)

            ch_Jean "Hey, [Laura.public_name]."
            ch_Laura "Hi."
        elif dice_roll == 2:
            "[Jean.name] loops her arm around yours."
            ch_Jean "Oh!"
            ch_Jean "Hey, [Laura.public_name]."
            ch_Jean "Didn't see you there."
            ch_Laura "Right. . ."
    elif Laura in Partners:
        "[Laura.name] gets in between you and [Jean.name]."
        ch_Jean "[Laura.public_name]. . ."
        ch_Jean "Getting close with [Player.first_name]?"
    else:
        $ dice_roll = renpy.random.randint(1, 2)

        if dice_roll == 1:
            ch_Jean "Hey, [Laura.public_name]."
            ch_Jean "Come find me later."
            ch_Laura "Why?"
            ch_Jean "{size=-5}Because you almost failed the last exam{/size}. . ."
        elif dice_roll == 2:
            ch_Jean "Oh, hey [Laura.public_name]."
            ch_Laura "Hi."

    $ Jean.eyes = "neutral"
    $ Laura.eyes = "neutral"

    return

label Jean_simple_greeting:
    if Jean.History.check("seen_Player", tracker = "recent") > 1 or Jean.History.check("seen_Player", tracker = "last"):
        $ modifier = " again"
    else:
        $ modifier = ""

    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        ch_Jean "Hi[modifier], [Player.first_name]!"
    elif dice_roll == 2:
        ch_Jean "Hey[modifier]!"
    elif dice_roll == 3:
        ch_Jean "Hi[modifier]!"

    return