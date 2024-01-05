label Jean_asked_once(context):
    $ dice_pool = []

    if context == "generic":
        $ dice_pool.append(1)
        $ dice_pool.append(2)
        $ dice_pool.append(3)
        $ dice_pool.append(4)
        $ dice_pool.append(5)
        $ dice_pool.append(6)
        $ dice_pool.append(7)
        $ dice_pool.append(8)
    elif context == "repeating":
        $ dice_pool.append(1)
        $ dice_pool.append(2)
        $ dice_pool.append(3)
        $ dice_pool.append(4)
        $ dice_pool.append(5)
        $ dice_pool.append(6)
        $ dice_pool.append(7)
        $ dice_pool.append(8)
    elif context == "busy":
        $ dice_pool.append(1)
        $ dice_pool.append(2)
        $ dice_pool.append(3)
        $ dice_pool.append(4)
        $ dice_pool.append(5)
        $ dice_pool.append(6)
        $ dice_pool.append(7)
        $ dice_pool.append(8)
        $ dice_pool.append(9)
        $ dice_pool.append(10)
        $ dice_pool.append(11)
        $ dice_pool.append(12)
        $ dice_pool.append(13)
        $ dice_pool.append(14)
        $ dice_pool.append(15)
        $ dice_pool.append(16)
    elif context == "late":
        $ dice_pool.append(1)
        $ dice_pool.append(2)
        $ dice_pool.append(3)
        $ dice_pool.append(4)
        $ dice_pool.append(5)
        $ dice_pool.append(6)
        $ dice_pool.append(7)
        $ dice_pool.append(8)
        $ dice_pool.append(17)
    elif context == "changing":
        $ dice_pool.append(1)
        $ dice_pool.append(2)
        $ dice_pool.append(3)
        $ dice_pool.append(4)
        $ dice_pool.append(5)
        $ dice_pool.append(6)
        $ dice_pool.append(7)
        $ dice_pool.append(8)
        $ dice_pool.append(9)
        $ dice_pool.append(10)
        $ dice_pool.append(11)
        $ dice_pool.append(12)
        $ dice_pool.append(13)
        $ dice_pool.append(14)
        $ dice_pool.append(15)
        $ dice_pool.append(16)
    elif context == "showing":
        $ dice_pool.append(1)
        $ dice_pool.append(2)
        $ dice_pool.append(3)
        $ dice_pool.append(4)
        $ dice_pool.append(5)
        $ dice_pool.append(6)
        $ dice_pool.append(7)
        $ dice_pool.append(8)
        $ dice_pool.append(9)
        $ dice_pool.append(10)
        $ dice_pool.append(11)
        $ dice_pool.append(12)
        $ dice_pool.append(13)
        $ dice_pool.append(14)
        $ dice_pool.append(15)
        $ dice_pool.append(16)
    elif context == "sex":
        $ dice_pool.append(1)
        $ dice_pool.append(2)
        $ dice_pool.append(3)
        $ dice_pool.append(4)
        $ dice_pool.append(5)
        $ dice_pool.append(6)
        $ dice_pool.append(7)
        $ dice_pool.append(8)
        $ dice_pool.append(9)
        $ dice_pool.append(10)
        $ dice_pool.append(11)
        $ dice_pool.append(12)
        $ dice_pool.append(13)
        $ dice_pool.append(14)
        $ dice_pool.append(15)
        $ dice_pool.append(16)
    elif context == "dismissing":
        $ dice_pool.append(1)
        $ dice_pool.append(2)
        $ dice_pool.append(3)
        $ dice_pool.append(4)
        $ dice_pool.append(5)
        $ dice_pool.append(6)
        $ dice_pool.append(7)
        $ dice_pool.append(8)
        $ dice_pool.append(9)
        $ dice_pool.append(10)
        $ dice_pool.append(11)
        $ dice_pool.append(12)
        $ dice_pool.append(13)
        $ dice_pool.append(14)
        $ dice_pool.append(15)
        $ dice_pool.append(16)
    elif context == "knocking":
        $ dice_pool.append(18)
        $ dice_pool.append(19)

    $ dice_roll = renpy.random.choice(dice_pool)

    if dice_roll == 1:
        $ Jean.change_face("angry1")

        ch_Jean "Didn't you hear what I said?" 
    elif dice_roll == 2:
        $ Jean.change_face("confused1")

        ch_Jean "Really. . ."
        ch_Jean "Are you ignoring me?"
    elif dice_roll == 3:
        $ Jean.change_face("angry1")

        ch_Jean "You better be joking."
    elif dice_roll == 4:
        $ Jean.change_face("confused1")

        ch_Jean "Really? What did I already say?"
    elif dice_roll == 5:
        $ Jean.change_face("angry1")

        ch_Jean "You better stop messing around."
    elif dice_roll == 6:
        $ Jean.change_face("confused1")

        ch_Jean "Are you really ignoring me?"
    elif dice_roll == 7:
        $ Jean.change_face("angry1") 

        ch_Jean "Don't ignore me."
    elif dice_roll == 8:
        $ Jean.change_face("angry1")

        ch_Jean "Ease off, [Player.first_name]."
    elif dice_roll == 9:
        $ Jean.change_face("confused1") 

        ch_Jean "Uhm, hello. . . you just asked me?"
    elif dice_roll == 10:
        $ Jean.change_face("angry1")

        ch_Jean "I said no, [Jean.Player_petname]." 
    elif dice_roll == 11:
        $ Jean.change_face("furious")

        ch_Jean "Don't ignore me." 
        ch_Jean "I already said no."
    elif dice_roll == 12:
        $ Jean.change_face("appalled1")

        ch_Jean "I just said no!" 
    elif dice_roll == 13:
        $ Jean.change_face("worried1")

        ch_Jean "Uh. . . no. . ."
    elif dice_roll == 14:
        $ Jean.change_face("confused1")

        ch_Jean "I just said no, [Player.first_name]."
    elif dice_roll == 15:
        $ Jean.change_face("confused1")

        ch_Jean "No, I really mean it."
    elif dice_roll == 16:
        $ Jean.change_face("appalled2")

        ch_Jean "I already said no!"
    elif dice_roll == 17:
        $ Jean.change_face("confused1")  

        ch_Jean "Uhm. . . Weren't you listening?" 
        ch_Jean "I'm about to go to bed."
    elif dice_roll == 18:
        ch_Jean "Cut it out!"
    elif dice_roll == 19:
        ch_Jean "Really?" 
        ch_Jean "Go away!"

    return

label Jean_asked_twice(context):
    $ dice_pool = []

    if context == "generic":
        $ dice_pool.append(1)
        $ dice_pool.append(2)
        $ dice_pool.append(3)
        $ dice_pool.append(4)
        $ dice_pool.append(5)
        $ dice_pool.append(6)
        $ dice_pool.append(7)
        $ dice_pool.append(8)
        $ dice_pool.append(9)
        $ dice_pool.append(10)
        $ dice_pool.append(11)
        $ dice_pool.append(12)
        $ dice_pool.append(13)
        $ dice_pool.append(14)
        $ dice_pool.append(15)
    elif context == "repeating":
        $ dice_pool.append(1)
        $ dice_pool.append(2)
        $ dice_pool.append(3)
        $ dice_pool.append(4)
        $ dice_pool.append(5)
        $ dice_pool.append(6)
        $ dice_pool.append(7)
        $ dice_pool.append(8)
        $ dice_pool.append(9)
        $ dice_pool.append(10)
        $ dice_pool.append(11)
        $ dice_pool.append(12)
        $ dice_pool.append(13)
        $ dice_pool.append(14)
        $ dice_pool.append(15)
    elif context == "busy":
        $ dice_pool.append(1)
        $ dice_pool.append(2)
        $ dice_pool.append(3)
        $ dice_pool.append(4)
        $ dice_pool.append(5)
        $ dice_pool.append(6)
        $ dice_pool.append(7)
        $ dice_pool.append(8)
        $ dice_pool.append(9)
        $ dice_pool.append(10)
        $ dice_pool.append(11)
        $ dice_pool.append(12)
        $ dice_pool.append(13)
        $ dice_pool.append(14)
        $ dice_pool.append(15)
    elif context == "late":
        $ dice_pool.append(1)
        $ dice_pool.append(2)
        $ dice_pool.append(3)
        $ dice_pool.append(4)
        $ dice_pool.append(5)
        $ dice_pool.append(6)
        $ dice_pool.append(7)
        $ dice_pool.append(8)
        $ dice_pool.append(9)
        $ dice_pool.append(10)
        $ dice_pool.append(11)
        $ dice_pool.append(12)
        $ dice_pool.append(13)
        $ dice_pool.append(14)
        $ dice_pool.append(15)
    elif context == "changing":
        $ dice_pool.append(1)
        $ dice_pool.append(2)
        $ dice_pool.append(3)
        $ dice_pool.append(4)
        $ dice_pool.append(5)
        $ dice_pool.append(6)
        $ dice_pool.append(7)
        $ dice_pool.append(8)
        $ dice_pool.append(9)
        $ dice_pool.append(10)
        $ dice_pool.append(11)
        $ dice_pool.append(12)
        $ dice_pool.append(13)
        $ dice_pool.append(14)
        $ dice_pool.append(15)
        $ dice_pool.append(16)
        $ dice_pool.append(17)
    elif context == "showing":
        $ dice_pool.append(1)
        $ dice_pool.append(2)
        $ dice_pool.append(3)
        $ dice_pool.append(4)
        $ dice_pool.append(5)
        $ dice_pool.append(6)
        $ dice_pool.append(7)
        $ dice_pool.append(8)
        $ dice_pool.append(9)
        $ dice_pool.append(10)
        $ dice_pool.append(11)
        $ dice_pool.append(12)
        $ dice_pool.append(13)
        $ dice_pool.append(14)
        $ dice_pool.append(15)
        $ dice_pool.append(16)
        $ dice_pool.append(17)
    elif context == "sex":
        $ dice_pool.append(1)
        $ dice_pool.append(2)
        $ dice_pool.append(3)
        $ dice_pool.append(4)
        $ dice_pool.append(5)
        $ dice_pool.append(6)
        $ dice_pool.append(7)
        $ dice_pool.append(8)
        $ dice_pool.append(9)
        $ dice_pool.append(10)
        $ dice_pool.append(11)
        $ dice_pool.append(12)
        $ dice_pool.append(13)
        $ dice_pool.append(14)
        $ dice_pool.append(15)
        $ dice_pool.append(16)
        $ dice_pool.append(17)
    elif context == "dismissing":
        $ dice_pool.append(1)
        $ dice_pool.append(2)
        $ dice_pool.append(3)
        $ dice_pool.append(4)
        $ dice_pool.append(5)
        $ dice_pool.append(6)
        $ dice_pool.append(7)
        $ dice_pool.append(8)
        $ dice_pool.append(9)
        $ dice_pool.append(10)
        $ dice_pool.append(11)
        $ dice_pool.append(12)
        $ dice_pool.append(13)
        $ dice_pool.append(14)
        $ dice_pool.append(15)
        $ dice_pool.append(16)
        $ dice_pool.append(17)
    elif context == "knocking":
        $ dice_pool.append(18)

    $ dice_roll = renpy.random.choice(dice_pool)

    if dice_roll == 1:
        $ Jean.change_face("angry1")  

        ch_Jean "The hell?"

        $ Jean.change_face("appalled1") 

        ch_Jean "Are you ignoring me?!"
    elif dice_roll == 2:
        $ Jean.change_face("appalled1") 

        ch_Jean "Are you ignoring me?"
    elif dice_roll == 3:
        $ Jean.change_face("appalled1") 

        ch_Jean "Stop ignoring me!"
    elif dice_roll == 4:
        $ Jean.change_face("appalled2")

        ch_Jean "You better cut it out." 
    elif dice_roll == 5:
        $ Jean.change_face("appalled2")

        ch_Jean "Really?!" 
    elif dice_roll == 6:
        $ Jean.change_face("angry1")

        ch_Jean "Okay, quit it."
    elif dice_roll == 7:
        $ Jean.change_face("appalled2")

        ch_Jean "Seriously?!" 
    elif dice_roll == 8:
        $ Jean.change_face("angry1")

        ch_Jean "Okay, stop."
    elif dice_roll == 9:
        $ Jean.change_face("angry1")

        ch_Jean "Learn to listen!"
    elif dice_roll == 10:
        $ Jean.change_face("angry2")

        ch_Jean "Really not cool, [Player.first_name]."
    elif dice_roll == 11:
        $ Jean.change_face("angry1")

        ch_Jean "Why don't you listen?"
    elif dice_roll == 12:
        $ Jean.change_face("angry1")

        ch_Jean "Ugh."
    elif dice_roll == 13:
        $ Jean.change_face("perplexed")

        ch_Jean "The fuck?"
    elif dice_roll == 14:
        $ Jean.change_face("appalled2")

        ch_Jean "Take a hint." 
    elif dice_roll == 15:
        $ Jean.change_face("angry1", eyes = "right")

        ch_Jean "The hell, dude. . ."
    elif dice_roll == 16:    
        $ Jean.change_face("appalled1")

        ch_Jean "Stop. Asking."
    elif dice_roll == 17:
        $ Jean.change_face("appalled2")

        ch_Jean "The more you ask, the less I want to do it."
    elif dice_roll == 18:
        ch_Jean "You better cut it the hell out!"
        

    return

label Jean_asked_once_text(context):
    $ dice_pool = []

    if context == "generic":
        $ dice_pool.append(1)
        $ dice_pool.append(2)
    elif context == "repeating":
        $ dice_pool.append(1)
        $ dice_pool.append(2)
    elif context == "busy":
        $ dice_pool.append(1)
        $ dice_pool.append(2)
        $ dice_pool.append(3)
        $ dice_pool.append(4)
    elif context == "late":
        $ dice_pool.append(1)
        $ dice_pool.append(2)
        $ dice_pool.append(5)

    $ dice_roll = renpy.random.choice(dice_pool)

    if dice_roll == 1:
        call receive_text(Jean, "Are my messages sending?") from _call_receive_text_216
    elif dice_roll == 2:
        call receive_text(Jean, "Read up, dummy") from _call_receive_text_95
    elif dice_roll == 3:
        call receive_text(Jean, "What? No. . .") from _call_receive_text_214
    elif dice_roll == 4:
        call receive_text(Jean, "I mean it, no") from _call_receive_text_215
    elif dice_roll == 5:
        call receive_text(Jean, "I'm about to put my phone down") from _call_receive_text_107
        call receive_text(Jean, "Just text me tomorrow") from _call_receive_text_108

    return

label Jean_asked_twice_text(context):
    $ dice_pool = []

    if context == "generic":
        $ dice_pool.append(1)
        $ dice_pool.append(2)
    elif context == "repeating":
        $ dice_pool.append(1)
        $ dice_pool.append(2)
    elif context == "busy":
        $ dice_pool.append(1)
        $ dice_pool.append(2)
        $ dice_pool.append(3)
        $ dice_pool.append(4)
    elif context == "late":
        $ dice_pool.append(1)
        $ dice_pool.append(2)
        $ dice_pool.append(5)

    $ dice_roll = renpy.random.choice(dice_pool)

    if dice_roll == 1:
        call receive_text(Jean, f"This is really getting old {Player.first_name}") from _call_receive_text_218
    elif dice_roll == 2:
        call receive_text(Jean, "Okay now you're doing it on purpose") from _call_receive_text_96
        call receive_text(Jean, "Stop") from _call_receive_text_97
    elif dice_roll == 3:
        call receive_text(Jean, "What's with you?? No!") from _call_receive_text_217
    elif dice_roll == 4:
        call receive_text(Jean, "Ugh, no!") from _call_receive_text_219
    elif dice_roll == 5:
        call receive_text(Jean, "Stopppp!") from _call_receive_text_109
        call receive_text(Jean, "I'm going to bed") from _call_receive_text_110

    return

label Jean_kicking_out:
    if Player.location == Jean.home:
        $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            ch_Jean "Get out."
        elif dice_roll == 2:
            ch_Jean "Stop ignoring me and get out."
        elif dice_roll == 3:
            "[Jean.name] turns around and leaves."
    else:
        $ dice_roll = renpy.random.randint(1, 2)

        if dice_roll == 1:
            ch_Jean "I'm out of here."
        elif dice_roll == 2:
            "[Jean.name] points towards the door."

    return