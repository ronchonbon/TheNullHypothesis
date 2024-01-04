label Laura_asked_once(context):
    $ dice_pool = []

    if context == "generic":
        $ dice_pool.append(1)
        $ dice_pool.append(2)
        $ dice_pool.append(3)
        $ dice_pool.append(4)
        $ dice_pool.append(5)
    elif context == "repeating":
        $ dice_pool.append(1)
        $ dice_pool.append(2)
        $ dice_pool.append(3)
        $ dice_pool.append(4)
        $ dice_pool.append(5)
    elif context == "busy":
        $ dice_pool.append(1)
        $ dice_pool.append(2)
        $ dice_pool.append(3)
        $ dice_pool.append(4)
        $ dice_pool.append(5)
        $ dice_pool.append(6)
        $ dice_pool.append(7)
        $ dice_pool.append(8)
    elif context == "late":
        $ dice_pool.append(1)
        $ dice_pool.append(2)
        $ dice_pool.append(3)
        $ dice_pool.append(4)
        $ dice_pool.append(5)
        $ dice_pool.append(6)
        $ dice_pool.append(7)
        $ dice_pool.append(8)
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
    elif context == "dismissing":
        $ dice_pool.append(1)
        $ dice_pool.append(2)
        $ dice_pool.append(3)
        $ dice_pool.append(4)
        $ dice_pool.append(5)
        $ dice_pool.append(15)
    elif context == "knocking":
        $ dice_pool.append(16)
        $ dice_pool.append(17)

    if dice_roll == 1:
        $ Laura.change_face("confused1")

        ch_Laura "What did I just say?"
    elif dice_roll == 2:
        $ Laura.change_face("confused1")

        ch_Laura "You listening to me?"
    elif dice_roll == 3:
        $ Laura.change_face("suspicious1")

        ch_Laura "Really?" 
        ch_Laura "Are you not listening?"
    elif dice_roll == 4:
        $ Laura.change_face("suspicious1")

        ch_Laura ". . ." 
    elif dice_roll == 5:
        $ Laura.change_face("angry1")

        ch_Laura "What are you doing?"
    elif dice_roll == 6:
        $ Laura.change_face("angry1")

        ch_Laura "I said no."
    elif dice_roll == 7:
        $ Laura.change_face("confused1")

        ch_Laura ". . . No. . ."
    elif dice_roll == 8:
        $ Laura.change_face("confused1")

        ch_Laura "What? No."
    elif dice_roll == 9:
        $ Laura.change_face("suspicious1")

        ch_Laura "Really thought asking again would work?" 
    elif dice_roll == 10:
        $ Laura.change_face("angry1")

        ch_Laura "I said no, don't make me say it again."
    elif dice_roll == 11:
        $ Laura.change_face("angry1") 

        ch_Laura "Don't make me repeat myself."
    elif dice_roll == 12:
        $ Laura.change_face("confused1", eyes = "squint")

        ch_Laura "Does 'no' mean something else to you?"
    elif dice_roll == 13:
        $ Laura.change_face("suspicious1")

        ch_Laura "What's your problem?"
    elif dice_roll == 14:
        $ Laura.change_face("angry1")

        ch_Laura "Keep asking, and I will hurt you."
    elif dice_roll == 15:
        $ Laura.change_face("angry1")

        ch_Laura "I'm not going anywhere."

        $ Laura.change_face("appalled2")

        ch_Laura "I'll make you leave if you keep asking."
    elif dice_roll == 16:
        ch_Laura "I said go away!"
    elif dice_roll == 17:
        ch_Laura "Don't push it."

    return

label Laura_asked_twice(context):
    $ dice_pool = []

    if context == "generic":
        $ dice_pool.append(1)
        $ dice_pool.append(2)
        $ dice_pool.append(3)
        $ dice_pool.append(4)
        $ dice_pool.append(5)
        $ dice_pool.append(6)
    elif context == "repeating":
        $ dice_pool.append(1)
        $ dice_pool.append(2)
        $ dice_pool.append(3)
        $ dice_pool.append(4)
        $ dice_pool.append(5)
        $ dice_pool.append(6)
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
    elif context == "knocking":
        $ dice_pool.append(14)

    if dice_roll == 1:
        $ Laura.change_face("angry1")

        ch_Laura "You're pissing me off."
    elif dice_roll == 2:
        $ Laura.change_face("appalled1")

        ch_Laura "Trying to anger me?"
    elif dice_roll == 3:
        $ Laura.change_face("angry1")

        ch_Laura "{i}Grrrrrrr{/i}"
    elif dice_roll == 4:
        $ Laura.change_face("angry1", eyes = "left")

        ch_Laura "Whatever."
    elif dice_roll == 5:
        $ Laura.change_face("angry1")

        ch_Laura "What the hell."
    elif dice_roll == 6:
        $ Laura.change_face("angry1")

        ch_Laura "Not funny."
    elif dice_roll == 7:
        $ Laura.change_face("appalled1")

        ch_Laura "You will stop asking. Or else."
    elif dice_roll == 8:
        $ Laura.change_face("appalled1")

        ch_Laura "Don't ask again."
    elif dice_roll == 9:
        $ Laura.change_face("appalled2")

        ch_Laura "I just said no."
    elif dice_roll == 10:
        $ Laura.change_face("appalled1")

        ch_Laura "No."
        
        show expression "images/effects/green_smack.webp" as smack onlayer effects:
            anchor (0.5, 0.5) pos (0.5, 0.4)

            zoom 0.0
            alpha 0.0
            ease 0.1 zoom 1.0 alpha 1.0
            ease 1.0 alpha 0.0

        with small_screenshake

        "She punches you on the shoulder, hard." 
    elif dice_roll == 11:
        $ Laura.change_face("appalled1")

        ch_Laura "Stop before you get yourself hurt."
    elif dice_roll == 12:
        $ Laura.change_face("appalled1")

        ch_Laura "Better stop asking."
    elif dice_roll == 13:
        $ Laura.change_face("appalled2")

        ch_Laura "Don't make me lay you out."
    elif dice_roll == 14:
        ch_Laura "Stop before I put a hole through the door."

    return

label Laura_asked_once_text(context):
    $ dice_pool = []

    if context == "generic":
        $ dice_pool.append(1)
        $ dice_pool.append(2)
        $ dice_pool.append(3)
        $ dice_pool.append(4)
    elif context == "repeating":
        $ dice_pool.append(1)
        $ dice_pool.append(2)
        $ dice_pool.append(3)
        $ dice_pool.append(4)
    elif context == "busy":
        $ dice_pool.append(1)
        $ dice_pool.append(2)
        $ dice_pool.append(3)
        $ dice_pool.append(4)
        $ dice_pool.append(5)
    elif context == "late":
        $ dice_pool.append(1)
        $ dice_pool.append(2)
        $ dice_pool.append(3)
        $ dice_pool.append(4)
        $ dice_pool.append(5)

    if dice_roll == 1:
        call receive_text(Laura, ". . .") from _call_receive_text_446
    elif dice_roll == 2:
        call receive_text(Laura, "What?") from _call_receive_text_447
    elif dice_roll == 3:
        call receive_text(Laura, "Did my last text not go through") from _call_receive_text_330
    elif dice_roll == 4:
        call receive_text(Laura, "Can't you read?") from _call_receive_text_316
    elif dice_roll == 5:
        call receive_text(Laura, "I said I cant.") from _call_receive_text_448

    return

label Laura_asked_twice_text(context):
    $ dice_pool = []

    if context == "generic":
        $ dice_pool.append(1)
        $ dice_pool.append(2)
        $ dice_pool.append(3)
        $ dice_pool.append(4)
    elif context == "repeating":
        $ dice_pool.append(1)
        $ dice_pool.append(2)
        $ dice_pool.append(3)
        $ dice_pool.append(4)
    elif context == "busy":
        $ dice_pool.append(1)
        $ dice_pool.append(2)
        $ dice_pool.append(3)
        $ dice_pool.append(4)
    elif context == "late":
        $ dice_pool.append(1)
        $ dice_pool.append(2)
        $ dice_pool.append(3)
        $ dice_pool.append(4)
        $ dice_pool.append(5)

    if dice_roll == 1:
        call receive_text(Laura, "This isn't cute.") from _call_receive_text_449
    elif dice_roll == 2:
        call receive_text(Laura, "This is very annoying") from _call_receive_text_450
    elif dice_roll == 3:
        call receive_text(Laura, "Stop") from _call_receive_text_451
    elif dice_roll == 4:
        call receive_text(Laura, "Stop.") from _call_receive_text_317
    elif dice_roll == 5:
        call receive_text(Laura, "Shut up") from _call_receive_text_331
        call receive_text(Laura, "I'm going to bed") from _call_receive_text_332

    return

label Laura_kicking_out:
    if Player.location == Laura.home:
        $ dice_roll = renpy.random.randint(1, 4)

        if dice_roll == 1:
            ch_Laura "Go away." 
            "She pushes you out of the room, locking the door behind you."
        elif dice_roll == 2:
            ch_Laura "Get out, now."
        elif dice_roll == 3:
            "[Laura.name] shoves you out the door."
        elif dice_roll == 4:
            "She forcefully shoves you out of the room, slamming the door shut behind you."
    else:
        $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            "She storms out of the room."
        elif dice_roll == 2:
            "[Laura.name] turns around and leaves."
        elif dice_roll == 3:
            "She storms out of the room, slamming the door behind her."

    return