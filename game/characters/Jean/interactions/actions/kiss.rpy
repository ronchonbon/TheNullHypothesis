label Jean_rejects_kiss:

    return

label Jean_accepts_kiss_first_time:

    return

label Jean_accepts_kiss_second_time:

    return

label Jean_accepts_kiss:

    return

label Jean_accepts_kiss_love:

    return

label Jean_rejects_makeout:
    $ Jean.change_face("confused1", blush = 1) 

    ch_Jean "Uhm, no. . ."

    return

label Jean_accepts_makeout_first_time:
    $ Jean.change_face("smirk2", mouth = "lipbite", blush = 1)

    ch_Jean "Yeah. . . I do."

    return

label Jean_accepts_makeout_second_time:

    return

label Jean_accepts_makeout:
    $ Jean.change_face("smirk2", mouth = "lipbite", blush = 1)

    ch_Jean "What a silly question. . ."
    
    return

label Jean_accepts_makeout_love:

    return