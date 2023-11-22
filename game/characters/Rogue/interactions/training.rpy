label Rogue_accept_train:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        $ Rogue.change_face("smirk2")

        ch_Rogue "Ah'd love to."
    elif dice_roll == 2:
        $ Rogue.change_face("happy")

        ch_Rogue "For sure!"
    elif dice_roll == 3:
        $ Rogue.change_face("worried1")

        ch_Rogue "Yes, please."
        ch_Rogue "Ah could really use it."

    return

label Rogue_reject_train:
    if Rogue.behavior == "training":
        $ dice_roll = renpy.random.randint(1, 3)
    else:
        $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Rogue.change_face("worried1")

        ch_Rogue "Sorry, [Rogue.Player_petname], not right now. . ."
    elif dice_roll == 2:
        $ Rogue.change_face("sad")

        ch_Rogue "Ah can't right this minute - maybe later?"
    elif dice_roll == 3:
        $ Rogue.change_face("worried1")

        ch_Rogue "Ah'd rather work on this exercise on my own, [Rogue.Player_petname]."

    return

label Rogue_reject_train_asked_once:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        $ Rogue.change_face("worried2")

        ch_Rogue "Ah mean it, not right now. . ."
    elif dice_roll == 2:
        $ Rogue.change_face("angry1")

        ch_Rogue "Ah said no. . ."
    elif dice_roll == 3:
        $ Rogue.change_face("confused1")

        ch_Rogue "Uhm. . . not right now?"

        $ Rogue.change_face("worried1")

        ch_Rogue "Are you okay?"

    return

label Rogue_reject_train_asked_twice:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        $ Rogue.change_face("angry1")

        ch_Rogue "Stop it!"
    elif dice_roll == 2:
        $ Rogue.change_face("angry1")

        ch_Rogue "[Player.first_name], no!"
    elif dice_roll == 3:
        $ Rogue.change_face("angry2")

        ch_Rogue "Not sure what's going on, but ah'm over it."
        
    call getting_kicked_out(Rogue) from _call_getting_kicked_out_64

    return

label Rogue_accept_train_text:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        call receive_text(Rogue, "Ok! Coming") from _call_receive_text_639
    elif dice_roll == 2:
        call receive_text(Rogue, "Yeah! Meet you there") from _call_receive_text_640
    elif dice_roll == 3:
        call receive_text(Rogue, "Ah was hopin youd ask!") from _call_receive_text_641

    return

label Rogue_reject_train_text:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        call receive_text(Rogue, "Little busy, let's try again another time?") from _call_receive_text_642
    elif dice_roll == 2:
        call receive_text(Rogue, f"Maybe later, {Rogue.Player_petname}") from _call_receive_text_643
    elif dice_roll == 3:
        call receive_text(Rogue, "Lets try sometime later") from _call_receive_text_644

    return

label Rogue_reject_train_asked_once_text:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        call receive_text(Rogue, "Nope") from _call_receive_text_645
    elif dice_roll == 2:
        call receive_text(Rogue, "I just said no") from _call_receive_text_646
    elif dice_roll == 3:
        call receive_text(Rogue, "Askin again doesnt help") from _call_receive_text_647
    
    return

label Rogue_reject_train_asked_twice_text:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        call receive_text(Rogue, "NO!") from _call_receive_text_648
    elif dice_roll == 2:
        call receive_text(Rogue, "Why do you do this?") from _call_receive_text_649
    elif dice_roll == 3:
        call receive_text(Rogue, "Stop") from _call_receive_text_650

    return