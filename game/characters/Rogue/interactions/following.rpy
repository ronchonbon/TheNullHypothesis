label Rogue_follow_in_love:
    "She grabs your hand."

    $ Rogue.change_face("smirk2")

    ch_Rogue "Anywhere."

    return

label Rogue_follow_in_relationship:
    "She grabs your hand."

    $ Rogue.change_face("smirk2")

    ch_Rogue "Not one bit."

    return

label Rogue_follow_love_and_trust:
    $ Rogue.change_face("smirk2")

    ch_Rogue "Where to?."

    return

label Rogue_follow_love:
    ch_Rogue "Sure."

    $ Rogue.change_face("smirk2")

    ch_Rogue "Lead the way, sugar."

    return

label Rogue_follow_trust:
    $ Rogue.change_face("confused1")

    ch_Rogue "Where we goin', hon'?"

    return

label Rogue_follow_temporary:
    ch_Rogue "Sure hon', but only for a bit."

    return

label Rogue_follow_busy:
    $ Rogue.change_face("worried1")

    if Rogue.behavior == "training":
        ch_Rogue "Ah really gotta finish this training session. . ."
    elif Rogue.behavior in ["studying", "changing", "showering", "masturbating"]:
        ch_Rogue "Ah can't. . . ah got stuff to do, ah'm sorry."
    elif Rogue.behavior == "in_class":
        ch_Rogue "Sorry. . . ah really can't be skippin' class."
    else:
        ch_Rogue "Sorry [Rogue.Player_petname], ah'm busy."

    return

label Rogue_follow_reject:
    $ Rogue.change_face("worried1")
    
    ch_Rogue "Sorry hon', ah can't."
    ch_Rogue "Schedule's pretty packed today."

    return

label Rogue_follow_reject_asked_once:
    call Rogue_asked_once("busy")

    return

label Rogue_follow_reject_asked_twice:
    $ Rogue.change_face("angry1")
    
    ch_Rogue "Ah'm not followin' you."

    if Player.location == Rogue.home:
        ch_Rogue "Get out."
    else:
        ch_Rogue "In fact, ah'm out of here."
        
    call getting_kicked_out(Rogue) from _call_getting_kicked_out_55

    return

label Rogue_follow_reject_mad:
    $ Rogue.change_face("appalled1")
    
    ch_Rogue "What?"
    ch_Rogue "No, ah'm not goin' anywhere."

    return

label Rogue_stop_follow_love:
    ch_Rogue "Ah'll be seein' you later."

    return

label Rogue_stop_follow_love_stay:
    ch_Rogue "Ah'm gonna stick 'round here for a while."

    return

label Rogue_stop_follow:
    ch_Rogue "Bye hon'."

    return

label Rogue_stop_follow_mad:
    $ Rogue.change_face("angry1")

    ch_Rogue "Yer ditchin' me?"
    ch_Rogue "Fine."

    return

label Rogue_stop_follow_heartbroken:
    $ Rogue.change_face("worried1")

    ch_Rogue "Did ah do somethin'?"

    $ Rogue.eyes = "down"

    ch_Rogue "Sorry. . . ah'll leave ya alone. . ."

    return

label Rogue_stop_follow_horny:
    $ Rogue.mouth = "lipbite"

    ch_Rogue "Ah hope you'll find me later. . ."

    $ Rogue.eyes = "down"

    pause 1.0

    $ Rogue.eyes = "neutral"

    return

label Rogue_stop_follow_nympho:
    $ Rogue.change_face("worried3", blush = 2)

    ch_Rogue "But. . . well."

    $ Rogue.mouth = "lipbite"
    $ Rogue.eyes = "down"

    pause 1.0

    $ Rogue.eyes = "sexy"

    ch_Rogue "Maybe you could come find me later. . ."

    return