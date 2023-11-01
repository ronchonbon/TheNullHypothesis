label Laura_rejects_spank:
    $ Laura.change_face("appalled2", blush = 1)

    pause 1.0

    $ Laura.change_face("angry1", blush = 1)

    ch_Laura "Don't do that again." 

    "She forcefully taps your balls before going back to what she was doing."

    return

label Laura_accepts_spank_first_time:
    $ Laura.change_face("appalled2", blush = 1) 

    pause 1.0

    $ Laura.change_face("angry1", mouth = "lipbite", blush = 2) 

    ch_Laura "Harder. . ."

    return

label Laura_accepts_spank_second_time:

    return

label Laura_accepts_spank:
    $ Laura.change_face("surprised3", blush = 1) 

    ch_Laura "*gasp*" 

    $ Laura.change_face("sly", mouth = "lipbite", blush = 1)

    ch_Laura "Not hard enough."

    return

label Laura_accepts_spank_love:

    return