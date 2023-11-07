label Laura_accept_swim:
    $ Laura.change_face("confused1") 

    ch_Laura "Just. . . for fun?"

    $ Laura.change_face("neutral")

    ch_Laura ". . ."
    ch_Laura 'Fine.'

    return

label Laura_reject_swim:
    $ Laura.change_face("confused1") 

    ch_Laura "I don't understand why I would want to 'hang out' in water."

    return

label Laura_reject_swim_asked_once:
    $ Laura.change_face("confused1")

    ch_Laura "What? No."
    
    return

label Laura_reject_swim_asked_twice:        
    $ Laura.change_face("angry1")

    ch_Laura "What the hell."

    call getting_kicked_out(Laura) from _call_getting_kicked_out_41

    return

label Laura_accept_sunbathe:
    $ Laura.change_face("confused1") 
    
    ch_Laura "Just lying down in the sun?" 
    
    $ Laura.change_face("neutral") 
    
    ch_Laura "Fine."

    return

label Laura_reject_sunbathe:
    $ Laura.change_face("confused1") 
    
    ch_Laura "Why would I want to idle around?" 
    
    $ Laura.change_face("neutral") 
    
    ch_Laura "No."

    return

label Laura_reject_sunbathe_asked_once:
    $ Laura.change_face("confused1")

    ch_Laura "What? No."
    
    return

label Laura_reject_sunbathe_asked_twice:
    $ Laura.change_face("angry1")

    ch_Laura "What the hell."

    call getting_kicked_out(Laura) from _call_getting_kicked_out_42

    return