label Laura_record_player_shopping_accept:
    $ Laura.change_face("confused1", eyes = "down")

    ch_Laura "This plays music?"
    ch_Player "It does."
    ch_Player "I know you've been really getting into listening."

    $ Laura.change_face("confused1", eyes = "squint", blush = 1)

    pause 1.0

    $ Laura.change_face("angry1", eyes = "right", blush = 1)

    if Player.scholarship == "artistic":
        ch_Laura "It's your fault. . ." 
    else:
        ch_Laura "It's mostly [Rogue.name]'s fault. . ."
    
    ch_Laura "Not necessarily a bad thing. . ."

    $ Laura.change_face("neutral", blush = 1)

    ch_Laura "Thank you."

    $ Laura.change_face("angry1", eyes = "squint", blush = 1)

    ch_Laura "You will join me in listening sometime soon."

    return True

label Laura_record_player_shopping_reject:

    return

label Laura_record_player_gift_accept:
    $ Laura.change_face("confused1", eyes = "down")

    ch_Laura "This plays music?"
    ch_Player "It does."
    ch_Player "I know you've been really getting into listening."

    $ Laura.change_face("confused1", eyes = "squint", blush = 1)

    pause 1.0

    $ Laura.change_face("angry1", eyes = "right", blush = 1)

    if Player.scholarship == "artistic":
        ch_Laura "It's your fault. . ." 
    else:
        ch_Laura "It's mostly [Rogue.name]'s fault. . ."
    
    ch_Laura "Not necessarily a bad thing. . ."

    $ Laura.change_face("neutral", blush = 1)

    ch_Laura "Thank you."

    $ Laura.change_face("angry1", eyes = "squint", blush = 1)

    ch_Laura "You will join me in listening sometime soon."

    return True

label Laura_record_player_gift_reject:

    return