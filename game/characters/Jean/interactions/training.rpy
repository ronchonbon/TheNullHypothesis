label Jean_accept_train:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        $ Jean.change_face("happy")

        ch_Jean "Sounds great!"
    elif dice_roll == 2:
        $ Jean.change_face("pleased1")

        ch_Jean "You bet."
    elif dice_roll == 3:
        $ Jean.change_face("smirk1")

        ch_Jean "Yeah!"

    return

label Jean_reject_train:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        $ Jean.change_face("worried1")

        ch_Jean "Sorry, a little busy at the moment!"
    elif dice_roll == 2:
        $ Jean.change_face("sad")

        ch_Jean "Maybe later!"
    elif dice_roll == 3:
        $ Jean.change_face("worried1")

        ch_Jean "Not a great time, sorry. . ."

    return

label Jean_reject_train_asked_once:
    call Jean_asked_once("busy") from _call_Jean_asked_once_15

    return

label Jean_reject_train_asked_twice:
    call Jean_asked_twice("busy") from _call_Jean_asked_twice_15
    call Jean_kicking_out from _call_Jean_kicking_out_21
    call getting_kicked_out(Jean) from _call_getting_kicked_out_21

    return

label Jean_accept_train_text:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        call receive_text(Jean, "Yeah! On my way!") from _call_receive_text_208
    elif dice_roll == 2:
        call receive_text(Jean, "You know ittt") from _call_receive_text_209
    elif dice_roll == 3:
        call receive_text(Jean, "Ofc!") from _call_receive_text_210

    return

label Jean_reject_train_text:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        call receive_text(Jean, "A little busy, rain check? <3") from _call_receive_text_211
    elif dice_roll == 2:
        call receive_text(Jean, "Bad timing, sorry [Jean.Player_petname]") from _call_receive_text_212
    elif dice_roll == 3:
        call receive_text(Jean, "Cant this time, have fun without me!") from _call_receive_text_213

    return

label Jean_reject_train_asked_once_text:
    call Jean_asked_once_text("busy") from _call_Jean_asked_once_text_3

    return

label Jean_reject_train_asked_twice_text:
    call Jean_asked_twice_text("busy") from _call_Jean_asked_twice_text_3

    return