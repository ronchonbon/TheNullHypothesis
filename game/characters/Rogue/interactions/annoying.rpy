label Rogue_asked_once(context):
    $ dice_pool = []

    if context == "generic":
        $ dice_pool.append(1)
    elif context == "repeating":
        $ dice_pool.append(1)
        $ dice_pool.append(2)
    elif context == "busy":
        $ dice_pool.append(1)
        $ dice_pool.append(2)
        $ dice_pool.append(3)
        $ dice_pool.append(4)
        $ dice_pool.append(5)
    elif context == "late":
        $ dice_pool.append(2)
        $ dice_pool.append(3)
        $ dice_pool.append(4)
        $ dice_pool.append(5)
        $ dice_pool.append(6)
    elif context == "changing":
        $ dice_pool.append(7)
        $ dice_pool.append(8)
        $ dice_pool.append(9)
        $ dice_pool.append(10)
        $ dice_pool.append(11)
        $ dice_pool.append(12)
        $ dice_pool.append(13)
        $ dice_pool.append(14)
    elif context == "showing":
        $ dice_pool.append(7)
        $ dice_pool.append(8)
        $ dice_pool.append(9)
        $ dice_pool.append(10)
        $ dice_pool.append(11)
        $ dice_pool.append(12)
        $ dice_pool.append(13)
        $ dice_pool.append(14)
    elif context == "sex":
        $ dice_pool.append(7)
        $ dice_pool.append(8)
        $ dice_pool.append(9)
        $ dice_pool.append(10)
        $ dice_pool.append(11)
        $ dice_pool.append(12)
        $ dice_pool.append(13)
        $ dice_pool.append(14)
    elif context == "dismissing":
        $ dice_pool.append(15)
    elif context == "knocking":
        $ dice_pool.append(16)
        $ dice_pool.append(17)

    if dice_roll == 1:
        $ Rogue.change_face("confused1")

        ch_Rogue "You alright?"
        ch_Rogue "Just asked me that. . ."
    elif dice_roll == 2:
        $ Rogue.change_face("angry1")

        ch_Rogue "Ah was clear the first time."
    elif dice_roll == 3:
        $ Rogue.change_face("worried2")

        ch_Rogue "Ah mean it, not right now. . ."
    elif dice_roll == 4:
        $ Rogue.change_face("confused1")
        
        ch_Rogue "Ah just told you ah can't. . ."
    elif dice_roll == 5:
        $ Rogue.change_face("confused1")

        ch_Rogue "Uhm. . . not right now?"

        $ Rogue.change_face("worried1")

        ch_Rogue "Are you okay?"
    elif dice_roll == 6:
        $ Rogue.change_face("confused1")

        ch_Rogue "Ah said ah'm 'bout to go to bed. . ."
    elif dice_roll == 7:
        $ Rogue.change_face("angry1")

        ch_Rogue "Askin' again ain't gonna change my mind."
    elif dice_roll == 8:
        $ Rogue.change_face("angry1")

        ch_Rogue "Ah said no."
    elif dice_roll == 9:
        $ Rogue.change_face("confused1")

        ch_Rogue "Ah said no. . ."
    elif dice_roll == 10:
        $ Rogue.change_face("angry1")

        ch_Rogue "Ah said it's not happenin'."
    elif dice_roll == 11:
        $ Rogue.change_face("angry1")

        ch_Rogue "Didn't ya hear me sayin' no the first time?"
    elif dice_roll == 12:
        $ Rogue.change_face("angry1")

        ch_Rogue "Why would you think ah already changed my mind?"
    elif dice_roll == 13:
        $ Rogue.change_face("angry1")

        ch_Rogue "Ah already said no, [Rogue.Player_petname]."
    elif dice_roll == 14:
        $ Rogue.change_face("angry1") 

        ch_Rogue "Ah already said no, stop askin'."
    elif dice_roll == 15:
        $ Rogue.change_face("angry1")

        ch_Rogue "Ah already said ah'm not goin' anywhere."
    elif dice_roll == 16:
        ch_Rogue "You better quit knockin'!"
    elif dice_roll == 17:
        ch_Rogue "What did ah just say?"
        ch_Rogue "Go away!"

    return

label Rogue_asked_twice(context):
    $ dice_pool = []

    if context == "generic":
        $ dice_pool.append(1)
        $ dice_pool.append(2)
        $ dice_pool.append(3)
        $ dice_pool.append(4)
        $ dice_pool.append(5)
        $ dice_pool.append(6)
        $ dice_pool.append(7)
    elif context == "repeating":
        $ dice_pool.append(1)
        $ dice_pool.append(2)
        $ dice_pool.append(3)
        $ dice_pool.append(4)
        $ dice_pool.append(5)
        $ dice_pool.append(6)
        $ dice_pool.append(7)
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
    elif context == "showing":
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
        $ dice_pool.append(9)
        $ dice_pool.append(10)
    elif context == "knocking":
        $ dice_pool.append(14)

    if dice_roll == 1:
        $ Rogue.change_face("angry1")

        ch_Rogue "Stop it!"
    elif dice_roll == 2:
        $ Rogue.change_face("appalled2")

        ch_Rogue "Are ya ignorin' me or somethin'?"
    elif dice_roll == 3:
        $ Rogue.change_face("angry2")

        ch_Rogue "Not sure what's going on, but ah'm over it."
    elif dice_roll == 4:
        $ Rogue.change_face("appalled2")

        ch_Rogue "Now yer just pissin' me off."
    elif dice_roll == 5:
        $ Rogue.change_face("appalled2")
        
        ch_Rogue "Really?"
    elif dice_roll == 6:
        $ Rogue.change_face("angry1")

        ch_Rogue "Ah really don't like when you don't listen to me. . ."
    elif dice_roll == 7:
        $ Rogue.change_face("furious") 

        ch_Rogue "That's it, you're done."
    elif dice_roll == 8:
        $ Rogue.change_face("angry1")

        ch_Rogue "Ah told ya ah'm busy."
    elif dice_roll == 9:
        $ Rogue.change_face("angry1")

        ch_Rogue "[Player.first_name], no!"
    elif dice_roll == 10:
        $ Rogue.change_face("appalled2")

        ch_Rogue "Really?"
        ch_Rogue "Why the hell are you still askin'?"
    elif dice_roll == 11:
        $ Rogue.change_face("appalled2")

        ch_Rogue "Ah'm done listenin' to you right now."
    elif dice_roll == 12:
        $ Rogue.change_face("appalled2")

        ch_Rogue "You tryin' to get kicked in the jewels?"
    elif dice_roll == 13:
        $ Rogue.change_face("appalled1")

        ch_Rogue "Ah think you should stop askin'."

        $ Rogue.change_face("furious")

        ch_Rogue "Or else."
    elif dice_roll == 14:
        ch_Rogue "If ya don't cut it out, I'm fixin' to come out 'n make ya!"

    return

label Rogue_asked_once_text(context):
    $ dice_pool = []

    if context == "generic":
        $ dice_pool.append(1)
        $ dice_pool.append(2)
        $ dice_pool.append(3)
    elif context == "repeating":
        $ dice_pool.append(1)
        $ dice_pool.append(2)
        $ dice_pool.append(3)
    elif context == "busy":
        $ dice_pool.append(1)
        $ dice_pool.append(2)
        $ dice_pool.append(3)
        $ dice_pool.append(4)
        $ dice_pool.append(5)
        $ dice_pool.append(6)
    elif context == "late":
        $ dice_pool.append(1)
        $ dice_pool.append(2)
        $ dice_pool.append(3)
        $ dice_pool.append(7)

    if dice_roll == 1:
        call receive_text(Rogue, "Huh?")
    elif dice_roll == 2:
        call receive_text(Rogue, f"You're repeatin yourself, {Rogue.Player_petname}")
    elif dice_roll == 3:
        call receive_text(Rogue, "Did ya not see my last text?") from _call_receive_text_527
    elif dice_roll == 4:
        call receive_text(Rogue, "Nope") from _call_receive_text_645
    elif dice_roll == 5:
        call receive_text(Rogue, "I just said no") from _call_receive_text_646
    elif dice_roll == 6:
        call receive_text(Rogue, "Askin again doesnt help") from _call_receive_text_647
    elif dice_roll == 7:
        call receive_text(Rogue, "Just said im goin to bed") from _call_receive_text_541
        call receive_text(Rogue, "Try again in the mornin") from _call_receive_text_542

    return

label Rogue_asked_twice_text(context):
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

    if dice_roll == 1:
        call receive_text(Rogue, "Why do you do this?") from _call_receive_text_649
    elif dice_roll == 2:
        call receive_text(Rogue, "Stop") from _call_receive_text_650
    elif dice_roll == 3:
        call receive_text(Rogue, "NO!") from _call_receive_text_648
    elif dice_roll == 4:
        call receive_text(Rogue, "The hell?") from _call_receive_text_528
        call receive_text(Rogue, "Just said no") from _call_receive_text_529
    elif dice_roll == 5:
        call receive_text(Rogue, "Stop textin me!") from _call_receive_text_543
        call receive_text(Rogue, "Tryin to sleep >:((") from _call_receive_text_544

    return

label Rogue_kicking_out:
    if Player.location == Rogue.home:
        $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            ch_Rogue "Get out."
        elif dice_roll == 2:
            ch_Rogue "Ah think you should leave."
        elif dice_roll == 3:
            "She pushes you out of the room, locking the door behind you."
    else:
        $ dice_roll = renpy.random.randint(1, 2)

        if dice_roll == 1:
            ch_Rogue "Ah'm out of here."
        elif dice_roll == 2:
            "She storms out of the room."

    return