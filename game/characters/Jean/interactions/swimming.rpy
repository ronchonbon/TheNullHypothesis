label Jean_accept_swim:

    return

label Jean_reject_swim:

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
    $ Jean.change_face("confused1", mouth = "smirk") 
    
    ch_Jean "Think I'd look good with a tan?" 
    
    $ Jean.change_face("smirk2") 
    
    ch_Jean "Sure."

    return

label Jean_reject_sunbathe:
    $ Jean.change_face("worried1") 
    
    ch_Jean "It's not that I don't want to. . ." 
    ch_Jean ". . . but I burn so easily."

    return

label Jean_reject_sunbathe_asked_once:
    call Jean_asked_once("busy") from _call_Jean_asked_once_14
    
    return

label Jean_reject_sunbathe_asked_twice:
    call Jean_asked_twice("busy") from _call_Jean_asked_twice_14
    call Jean_kicking_out from _call_Jean_kicking_out_20
    call getting_kicked_out(Jean) from _call_getting_kicked_out_20

    return