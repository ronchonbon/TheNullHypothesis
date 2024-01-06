label Jean_accept_study:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        $ Jean.change_face("smirk2")

        ch_Jean "Okay!"
    elif dice_roll == 2:
        $ Jean.change_face("smirk1")

        ch_Jean "You know it!"
    elif dice_roll == 3:
        $ Jean.change_face("pleased1")

        ch_Jean "I was just going to suggest that!"

    return

label Jean_reject_study:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        $ Jean.change_face("worried1")

        ch_Jean "I wish. . ."
        ch_Jean "Another time?"
    elif dice_roll == 2:
        $ Jean.change_face("worried1")
        
        ch_Jean "I can't right now. . ."

        $ Jean.change_face("worried2")

        ch_Jean "But I hope we can later!"
    elif dice_roll == 3:
        $ Jean.change_face("worried1")

        ch_Jean "Can't, maybe later, [Jean.Player_petname]?"

    return

label Jean_reject_study_asked_once:
    call Jean_asked_once("busy") from _call_Jean_asked_once_11
    
    return

label Jean_reject_study_asked_twice: 
    call Jean_asked_twice("busy") from _call_Jean_asked_twice_11
    call Jean_kicking_out from _call_Jean_kicking_out_17       
    call getting_kicked_out(Jean) from _call_getting_kicked_out_17

    return

label Jean_accept_study_text:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        call receive_text(Jean, "Ofc!") from _call_receive_text_65
    elif dice_roll == 2:
        call receive_text(Jean, "Already on my way!")
    elif dice_roll == 3:
        call receive_text(Jean, "That sounds fun!!")

    return

label Jean_reject_study_text:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        call receive_text(Jean, "Ugh I wish") from _call_receive_text_66
        call receive_text(Jean, "Maybe later?") from _call_receive_text_67
        call receive_text(Jean, "<3") from _call_receive_text_68
    elif dice_roll == 2:
        call receive_text(Jean, f"Not right now, sorry {Jean.Player_petname}. . .")
    elif dice_roll == 3:
        call receive_text(Jean, "Aw, bad timing :(")
        call receive_text(Jean, "Ask me again later?")

    return

label Jean_reject_study_asked_once_text:
    call Jean_asked_once_text("busy") from _call_Jean_asked_once_text

    return

label Jean_reject_study_asked_twice_text:
    call Jean_asked_twice_text("busy") from _call_Jean_asked_twice_text

    return