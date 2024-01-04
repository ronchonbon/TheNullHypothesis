label Laura_accept_train:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        ch_Laura "Sure."
    elif dice_roll == 2:
        ch_Laura "Yep."
    elif dice_roll == 3:
        ch_Laura "Obviously."

    return

label Laura_reject_train:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        ch_Laura "Later."
    elif dice_roll == 2:
        ch_Laura "No, but you should train anyways."
    elif dice_roll == 3:
        ch_Laura "Can't."

    return

label Laura_reject_train_asked_once:
    call Laura_asked_once("busy")
    
    return

label Laura_reject_train_asked_twice:
    call Laura_asked_twice("busy")
    call Laura_kicking_out
    call getting_kicked_out(Laura) from _call_getting_kicked_out_43

    return

label Laura_accept_train_text:
    if Laura.behavior == "studying" and Laura.History.check("studied_with_Player") and day - Laura.History.check_when("studied_with_Player") > 4:
        $ Laura.schedule[time_index] = [Laura.home, "studying"]

        call receive_text(Laura, "Can't") from _call_receive_text_436
        call receive_text(Laura, "I need to study or I'll fail another goddamn test") from _call_receive_text_437
        call receive_text(Laura, "Come and teach me") from _call_receive_text_438

        $ Laura.mandatory_text_options = ["fine, omw with the textbook", "sorry, I really need to train"]
        $ temp = Laura.mandatory_text_options[:]

        while Laura.mandatory_text_options:
            pause

        if Laura.text_history[-1][1] == temp[0]:
            hide screen phone_screen
            
            call set_the_scene(location = Laura.location) from _call_set_the_scene_151

            $ Player.behavior = "studying"
            $ Player.behavior_Partners = [Laura]
        else:
            $ Player.behavior = None
    else:
        $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            call receive_text(Laura, "Okay") from _call_receive_text_439
        elif dice_roll == 2:
            call receive_text(Laura, "Of course") from _call_receive_text_440
        elif dice_roll == 3:
            call receive_text(Laura, "Already on my way") from _call_receive_text_441

    return

label Laura_reject_train_text:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        call receive_text(Laura, "Cant") from _call_receive_text_442
        call receive_text(Laura, "Busy") from _call_receive_text_443
    elif dice_roll == 2:
        call receive_text(Laura, "Later") from _call_receive_text_444
    elif dice_roll == 3:
        call receive_text(Laura, "Some other time") from _call_receive_text_445

    return

label Laura_reject_train_asked_once_text:
    call Laura_asked_once_text("busy")
    
    return

label Laura_reject_train_asked_twice_text:
    call Laura_asked_twice_text("busy")

    return