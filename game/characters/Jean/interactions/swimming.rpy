label Jean_accept_swim:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        $ Jean.change_face("smirk2")

        ch_Jean "Sure, that sounds like fun."
    elif dice_roll == 2:
        $ Jean.change_face("pleased1")

        ch_Jean "Yeah, a little swim sounds like just what I need right now."
    elif dice_roll == 3:
        $ Jean.change_face("happy")

        ch_Jean "I'd love to swim with you!"

        $ Jean.change_face("smirk2")

        ch_Jean "Thanks for asking me."

    return

label Jean_reject_swim:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        $ Jean.change_face("worried1")
        
        ch_Jean "Maybe another time? Little too stressed right now."
    elif dice_roll == 2:
        $ Jean.change_face("sad")
        
        ch_Jean "I don't know, rain check?"
    elif dice_roll == 3:
        $ Jean.change_face("worried1")

        ch_Jean "Too busy, another time, [Jean.Player_petname]?"

    return

label Jean_reject_swim_asked_once:
    call Jean_asked_once("busy") from _call_Jean_asked_once_13
    
    return

label Jean_reject_swim_asked_twice:  
    call Jean_asked_twice("busy") from _call_Jean_asked_twice_13
    call Jean_kicking_out from _call_Jean_kicking_out_19      
    call getting_kicked_out(Jean) from _call_getting_kicked_out_19

    return

label Jean_accept_sunbathe:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        $ Jean.change_face("confused1", mouth = "smirk") 
        
        ch_Jean "Think I'd look good with a tan?" 
        
        $ Jean.change_face("smirk2") 
        
        ch_Jean "Sure."
    elif dice_roll == 2:
        $ Jean.change_face("smirk2")

        ch_Jean "Okay, but don't let me catch you staring. . ."
    elif dice_roll == 3:
        $ Jean.change_face("smirk1")

        ch_Jean "That actually sounds really nice right now. . ."

    return

label Jean_reject_sunbathe:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        $ Jean.change_face("worried1") 
        
        ch_Jean "It's not that I don't want to. . ." 
        ch_Jean ". . . but I burn so easily."
    elif dice_roll == 2:
        $ Jean.change_face("worried1")

        ch_Jean "Sorry, there's no way I can relax enough to enjoy laying around right now."
    elif dice_roll == 3:
        $ Jean.change_face("worried1")

        ch_Jean "Mmm, maybe another time."

        $ Jean.change_face("worried1", mouth = "frown")

        ch_Jean "When things are less hectic."

    return

label Jean_reject_sunbathe_asked_once:
    call Jean_asked_once("busy") from _call_Jean_asked_once_14
    
    return

label Jean_reject_sunbathe_asked_twice:
    call Jean_asked_twice("busy") from _call_Jean_asked_twice_14
    call Jean_kicking_out from _call_Jean_kicking_out_20
    call getting_kicked_out(Jean) from _call_getting_kicked_out_20

    return