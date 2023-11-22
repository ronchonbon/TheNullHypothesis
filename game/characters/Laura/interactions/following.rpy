label Laura_follow_in_love:
    "She grabs your hand."

    $ Laura.change_face("smirk2")

    ch_Laura "I'm always following you. . ."

    return

label Laura_follow_in_relationship:
    $ Laura.change_face("smirk2")

    ch_Laura "Was planning on tailing you anyway. . ."

    return

label Laura_follow_love_and_trust:
    ch_Laura "Fine, I'll follow."

    return

label Laura_follow_love:
    ch_Laura "Let's go."

    return

label Laura_follow_trust:
    $ Laura.change_face("confused1")

    ch_Laura "Where are we going?"

    return

label Laura_follow_temporary:
    ch_Laura "Fine, only for now."
    ch_Laura "Still need to train later."

    return

label Laura_follow_busy:
    if Laura.behavior == "training":
        $ Laura.change_face("confused1")

        ch_Laura "Why?"

        $ Laura.change_face("neutral")

        ch_Laura "No, I'm in the middle of training."
    elif Laura.behavior == "studying":
        $ Laura.change_face("neutral")

        ch_Laura "Not leaving."
        ch_Laura "I'm busy."
    elif Laura.behavior == "in_class":
        $ Laura.change_face("angry1")

        ch_Laura "I wish I could skip this shitty class. . ."

    return

label Laura_follow_reject:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        ch_Laura "Why would I follow you?"
    elif dice_roll == 2:
        ch_Laura "I mind."

    return

label Laura_follow_reject_asked_once:
    $ Laura.change_face("angry1")

    ch_Laura "I said no."

    return

label Laura_follow_reject_asked_twice:
    $ Laura.change_face("appalled2")

    ch_Laura "I just said I'm not following you."
    
    if Player.location == Laura.home:
        ch_Laura "Get out, now."
    else:
        ch_Laura "This is absurd."
        
    call getting_kicked_out(Laura) from _call_getting_kicked_out_33

    return

label Laura_follow_reject_mad:
    $ Laura.change_face("appalled2")

    ch_Laura "{i}Grrrrrr{/i}."
    ch_Laura "I'm not in the mood."

    return

label Laura_stop_follow_love:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        ch_Laura "Bye."
    elif dice_roll == 2:
        ch_Laura "Fine, I'll be around."

    return

label Laura_stop_follow_love_stay:
    ch_Laura "Fine, I'll just stay here."

    return

label Laura_stop_follow:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        ch_Laura "Bye."
    elif dice_roll == 2:
        ch_Laura "Fine, I'll be around."

    return

label Laura_stop_follow_mad:
    $ Laura.change_face("angry1")

    ch_Laura "Trying to get rid of me?"

    return

label Laura_stop_follow_heartbroken:
    $ Laura.change_face("worried1")

    pause 1.0

    $ Laura.change_face("angry1")

    ch_Laura "Okay. . ."
    ch_Laura "I'll stop."

    return

label Laura_stop_follow_horny:
    $ Laura.mouth = "lipbite"

    ch_Laura "Fine, for now. . ."

    $ Laura.eyes = "down"

    pause 1.0

    $ Laura.eyes = "neutral"

    ch_Laura "I might come find you later."

    return

label Laura_stop_follow_nympho:
    $ Laura.change_face("angry1", blush = 2)

    ch_Laura "Fine, but I need. . ."

    $ Laura.eyes = "down"
    $ Laura.mouth = "lipbite"

    pause 1.0

    $ Laura.eyes = "sexy"

    ch_Laura ". . . {i}you{/i} later. . ."

    return