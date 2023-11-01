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
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        $ Jean.change_face("confused1")

        ch_Jean "I just said no, [Player.first_name]."
    elif dice_roll == 2:
        $ Jean.change_face("worried1")

        ch_Jean "Uh. . . no. . ."
    elif dice_roll == 3:
        $ Jean.change_face("angry1")

        ch_Jean "Ease off, [Player.first_name]."

    return

label Jean_reject_train_asked_twice:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        $ Jean.change_face("angry1")

        ch_Jean "Why don't you listen?"
    elif dice_roll == 2:
        $ Jean.change_face("angry2")

        ch_Jean "Really not cool, [Player.first_name]."
    elif dice_roll == 3:
        $ Jean.change_face("angry1")

        ch_Jean "Learn to listen!"
        
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
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        call receive_text(Jean, "What? No. . .") from _call_receive_text_214
    elif dice_roll == 2:
        call receive_text(Jean, "I mean it, no") from _call_receive_text_215
    elif dice_roll == 3:
        call receive_text(Jean, "Are my messages sending?") from _call_receive_text_216

    return

label Jean_reject_train_asked_twice_text:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        call receive_text(Jean, "What's with you?? No!") from _call_receive_text_217
    elif dice_roll == 2:
        call receive_text(Jean, "This is really getting old, [Player.first_name]") from _call_receive_text_218
    elif dice_roll == 3:
        call receive_text(Jean, "Ugh, no!") from _call_receive_text_219

    return