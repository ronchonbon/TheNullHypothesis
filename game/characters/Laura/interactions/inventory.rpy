label Laura_rejected_gift_once:
    $ Laura.change_face("confused1")

    ch_Laura "I already said no to this. . ."

    return

label Laura_rejected_gift_twice:
    $ Laura.change_face("appalled2")

    ch_Laura "Stop trying to give me this shit."
        
    call Laura_kicking_out from _call_Laura_kicking_out_13
    call getting_kicked_out(Laura) from _call_getting_kicked_out_35

    return

label Laura_rejected_piercing_once:
    $ Laura.change_face("angry1")

    ch_Laura "Didn't I already say no."

    return

label Laura_rejected_piercing_twice:
    $ Laura.change_face("appalled2")

    ch_Laura "Go away before I pierce {i}you{/i}. . ."
        
    call getting_kicked_out(Laura) from _call_getting_kicked_out_36

    return

label Laura_rejected_remote_vibrator_once:
    $ Laura.change_face("angry1")

    ch_Laura "Didn't I already say no."

    return

label Laura_rejected_remote_vibrator_twice:
    $ Laura.change_face("appalled2")

    ch_Laura "Go away before I put it in {i}you{/i}. . ."
        
    call getting_kicked_out(Laura) from _call_getting_kicked_out_37

    return

label Laura_rejected_buttplug_once:
    $ Laura.change_face("angry1")

    ch_Laura "Didn't I already say no."

    return

label Laura_rejected_buttplug_twice:
    $ Laura.change_face("appalled2")

    ch_Laura "Go away before I plug {i}you{/i}. . ."
        
    call getting_kicked_out(Laura) from _call_getting_kicked_out_38

    return