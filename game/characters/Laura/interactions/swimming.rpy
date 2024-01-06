label Laura_accept_swim:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        $ Laura.change_face("confused1") 

        ch_Laura "Just. . . for fun?"

        $ Laura.change_face("neutral")

        ch_Laura ". . ."
        ch_Laura "Fine."
    elif dice_roll == 2:
        $ Laura.change_face("smirk1") 

        ch_Laura "I suppose we could swim a little."
    elif dice_roll == 3:
        $ Laura.change_face("neutral")

        ch_Laura "Sure, why not."

    return

label Laura_reject_swim:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        $ Laura.change_face("confused1") 

        ch_Laura "I don't understand why I would want to 'hang out' in water."
    elif dice_roll == 2:
        $ Laura.change_face("neutral")

        ch_Laura "Not interested."
    elif dice_roll == 3:
        $ Laura.change_face("neutral")

        ch_Laura "No."

    return

label Laura_reject_swim_asked_once:
    call Laura_asked_once("busy") from _call_Laura_asked_once_13
    
    return

label Laura_reject_swim_asked_twice:  
    call Laura_asked_twice("busy") from _call_Laura_asked_twice_13
    call Laura_kicking_out from _call_Laura_kicking_out_16
    call getting_kicked_out(Laura) from _call_getting_kicked_out_41

    return

label Laura_accept_sunbathe:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        $ Laura.change_face("confused1") 
        
        ch_Laura "Just lying down in the sun?" 
        
        $ Laura.change_face("neutral") 
        
        ch_Laura "Fine."
    elif dice_roll == 2:
        $ Laura.change_face("confused1")

        ch_Laura "You want to just lay out here? Together?"

        $ Laura.eyes = "left"

        pause 1.0

        $ Laura.change_face("neutral")

        ch_Laura "Fine."
    elif dice_roll == 3:
        $ Laura.change_face("smirk1")

        ch_Laura "I suppose sunbathing could be 'relaxing.'"

    return

label Laura_reject_sunbathe:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        $ Laura.change_face("confused1") 
        
        ch_Laura "Why would I want to idle around right now?" 
        
        $ Laura.change_face("neutral") 
        
        ch_Laura "No."
    elif dice_roll == 2:
        $ Laura.change_face("neutral")

        ch_Laura "Too much to do to just lay around right now."
    elif dice_roll == 3:
        $ Laura.change_face("neutral")

        ch_Laura "No. . . thanks."

    return

label Laura_reject_sunbathe_asked_once:
    call Laura_asked_once("busy") from _call_Laura_asked_once_14
    
    return

label Laura_reject_sunbathe_asked_twice:
    call Laura_asked_twice("busy") from _call_Laura_asked_twice_14
    call Laura_kicking_out from _call_Laura_kicking_out_17
    call getting_kicked_out(Laura) from _call_getting_kicked_out_42

    return