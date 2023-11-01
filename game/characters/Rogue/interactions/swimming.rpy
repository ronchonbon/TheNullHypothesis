label Rogue_accept_swim:
    $ Rogue.change_face("worried1", mouth = "smirk") 
    
    ch_Rogue "Sure, ah'm always down for a swim."

    return

label Rogue_reject_swim:
    $ Rogue.change_face("worried1") 

    ch_Rogue "Ah'm sorry, maybe another time?"

    return

label Rogue_reject_swim_asked_once:
    $ Rogue.change_face("confused1")

    ch_Rogue "Ah said no. . ."
    
    return

label Rogue_reject_swim_asked_twice:        
    $ Rogue.change_face("angry1")

    ch_Rogue "Ah really don't like when you don't listen to me. . ."

    call getting_kicked_out(Rogue) from _call_getting_kicked_out_62

    return

label Rogue_accept_sunbathe:
    $ Rogue.change_face("worried1", mouth = "smirk") 
    
    ch_Rogue "Sure, ah could use a bit of sun."

    return

label Rogue_reject_sunbathe:
    $ Rogue.change_face("worried1") 
    
    ch_Rogue "Ah'm sorry. . ."
    ch_Rogue "Not sure ah wanna risk a sunburn."

    return

label Rogue_reject_sunbathe_asked_once:
    $ Rogue.change_face("confused1")

    ch_Rogue "Ah said no. . ."
    
    return

label Rogue_reject_sunbathe_asked_twice:
    $ Rogue.change_face("angry1")

    ch_Rogue "Ah really don't like when you don't listen to me. . ."

    call getting_kicked_out(Rogue) from _call_getting_kicked_out_63

    return