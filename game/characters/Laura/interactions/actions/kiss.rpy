label Laura_rejects_kiss:

    return

label Laura_accepts_kiss_first_time:

    return

label Laura_accepts_kiss_second_time:

    return

label Laura_accepts_kiss:

    return

label Laura_accepts_kiss_love:

    return

label Laura_rejects_makeout:
    $ Laura.change_face("suspicious1") 

    if not Laura.History.check("makeout") and not Laura.History.check("kiss"):
        ch_Laura "I'm not just giving away my first kiss like that. . ."
    else:
        ch_Laura "Not likely."

    return

label Laura_accepts_makeout_first_time:
    $ Laura.change_face("sly", blush = 1) 

    ch_Laura "I did enjoy that first kiss. . ." 

    $ Laura.change_face("kiss2", blush = 1) 

    "She doesn't hesitate and pulls you in."

    return

label Laura_accepts_makeout_second_time:

    return

label Laura_accepts_makeout:
    $ Laura.change_face("smirk2", mouth = "lipbite", blush = 1)

    ch_Laura "Why wouldn't I want to with you. . . ?"
    
    return

label Laura_accepts_makeout_love:

    return