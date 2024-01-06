label Rogue_accept_study:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        $ Rogue.change_face("smirk2")

        ch_Rogue "Sure, hon'."
    elif dice_roll == 2:
        $ Rogue.change_face("pleased1")

        ch_Rogue "Yeah, studyin' sounds good!"
    elif dice_roll == 3:
        $ Rogue.change_face("pleased1")

        ch_Rogue "Ah sure do!"

    return

label Rogue_reject_study:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        $ Rogue.change_face("sad")

        ch_Rogue "Ah can't right now, but another time?"
    elif dice_roll == 2:
        $ Rogue.change_face("worried1")

        ch_Rogue "Ah'm sorry, maybe later?"

        $ Rogue.change_face("worried1", mouth = "open", blush = 1)

        ch_Rogue "Thanks for askin' me though!"
    elif dice_roll == 3:
        $ Rogue.change_face("worried1")

        ch_Rogue "No time right now. . . Catch up later, though?"

    return

label Rogue_reject_study_asked_once:
    call Rogue_asked_once("busy") from _call_Rogue_asked_once_14

    return

label Rogue_reject_study_asked_twice:
    call Rogue_asked_twice("busy") from _call_Rogue_asked_twice_7
    call Rogue_kicking_out from _call_Rogue_kicking_out_10
    call getting_kicked_out(Rogue) from _call_getting_kicked_out_60

    return

label Rogue_accept_study_text:
    if Rogue.behavior == "studying":
        $ Rogue.schedule[time_index] = [Rogue.home, "studying"]

        call receive_text(Rogue, "Was already studying in my room") from _call_receive_text_494
        call receive_text(Rogue, "Why don't ya come on over?") from _call_receive_text_495

        $ Rogue.mandatory_text_options = ["omw, I'll bring the textbook", "nvm, we can study later"]
        $ temp = Rogue.mandatory_text_options[:]

        while Rogue.mandatory_text_options:
            pause

        if Rogue.text_history[-1][1] == temp[0]:
            hide screen phone_screen
            
            call set_the_scene(location = Rogue.location) from _call_set_the_scene_225
        elif Rogue.text_history[-1][1] == temp[1]:
            $ Player.behavior = None
    else:
        $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            call receive_text(Rogue, "Always down to study with ya") from _call_receive_text_496
            call receive_text(Rogue, "Omw!") from _call_receive_text_497
        elif dice_roll == 2:
            call receive_text(Rogue, "Ofc! I'll bring my books!")
        elif dice_roll == 3:
            call receive_text(Rogue, "Yeah! Coming!")

    return

label Rogue_reject_study_text:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        call receive_text(Rogue, "Sorry hon") from _call_receive_text_498
        call receive_text(Rogue, "Too busy atm") from _call_receive_text_499
    elif dice_roll == 2:
        call receive_text(Rogue, "Can't :((") from _call_receive_text_500
        call receive_text(Rogue, "Too much going on") from _call_receive_text_501
    elif dice_roll == 3:
        call receive_text(Rogue, f":( Sorry {Rogue.Player_petname}")
        call receive_text(Rogue "Rain check?")

    return

label Rogue_reject_study_asked_once_text:
    call Rogue_asked_once_text("busy") from _call_Rogue_asked_once_text

    return

label Rogue_reject_study_asked_twice_text:
    call Rogue_asked_twice_text("busy") from _call_Rogue_asked_twice_text

    return