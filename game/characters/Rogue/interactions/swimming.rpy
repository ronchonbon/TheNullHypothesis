label Rogue_accept_swim:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        $ Rogue.change_face("worried1", mouth = "smirk") 
        
        ch_Rogue "Sure, ah'm always down for a swim."
    elif dice_roll == 2:
        $ Rogue.change_face("smirk2") 
        
        ch_Rogue "Ah'd love to go swimmin' with ya!"

        $ Rogue.change_face("smirk1", blush = 1)

        ch_Rogue "Ah'm glad you asked. . ."
    elif dice_roll == 3:
        $ Rogue.change_face("pleased1")

        ch_Rogue "A swim sounds lovely right about now!"

    return

label Rogue_reject_swim:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        $ Rogue.change_face("worried1") 

        ch_Rogue "Ah'm sorry, maybe another time?"
    elif dice_roll == 2:
        $ Rogue.change_face("worried1")

        ch_Rogue "Sorry, [Rogue.Player_petname], it's not a great time."

        $ Rogue.eyes = "left"

        pause 1.0

        $ Rogue.eyes = "right"
    elif dice_roll == 3:
        $ Rogue.change_face("worried1") 

        ch_Rogue "Ah don't know. . . ask again later?"

    return

label Rogue_reject_swim_asked_once:
    call Rogue_asked_once("busy") from _call_Rogue_asked_once_16
    
    return

label Rogue_reject_swim_asked_twice:        
    call Rogue_asked_twice("busy") from _call_Rogue_asked_twice_9
    call Rogue_kicking_out from _call_Rogue_kicking_out_12
    call getting_kicked_out(Rogue) from _call_getting_kicked_out_62

    return

label Rogue_accept_sunbathe:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        $ Rogue.change_face("worried1", mouth = "smirk") 
        
        ch_Rogue "Sure, ah could use a bit of sun."
    elif dice_roll == 2:
        $ Rogue.change_face("smirk2")

        ch_Rogue "A little sun sounds real nice right about now."
    elif dice_roll == 3:
        $ Rogue.change_face("smirk2")

        ch_Rogue "Ah'd love to! Will be nice to hang out too."

    return

label Rogue_reject_sunbathe:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        $ Rogue.change_face("worried1") 
        
        ch_Rogue "Ah'm sorry. . ."
        ch_Rogue "Not sure ah wanna risk a sunburn."
    elif dice_roll == 2:
        $ Rogue.change_face("worried1", mouth = "happy")

        ch_Rogue "Maybe another time? Ah'm kinda busy. . ." 
    elif dice_roll == 3:
        $ Rogue.change_face("worried1")

        ch_Rogue "Sorry, [Rogue.Player_petname], kinda got a busy day."

    return

label Rogue_reject_sunbathe_asked_once:
    call Rogue_asked_once("busy") from _call_Rogue_asked_once_17
    
    return

label Rogue_reject_sunbathe_asked_twice:
    call Rogue_asked_twice("busy") from _call_Rogue_asked_twice_10
    call Rogue_kicking_out from _call_Rogue_kicking_out_13
    call getting_kicked_out(Rogue) from _call_getting_kicked_out_63

    return