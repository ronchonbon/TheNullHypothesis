label Rogue_rejects_spank:
    $ Rogue.change_face("surprised2", blush = 1) 

    pause 1.0

    $ Rogue.change_face("confused1", mouth = "lipbite", blush = 1) 

    if not Rogue.History.check("spank"):
        ch_Rogue "The hell was that for?"
     
    ch_Rogue "Quit it." 

    return

label Rogue_accepts_spank_first_time:
    $ Rogue.change_face("worried2", mouth = "lipbite", blush = 1)

    ch_Rogue "*gasp*"

    $ Rogue.change_face("sexy", blush = 2)

    return

label Rogue_accepts_spank_second_time:

    return

label Rogue_accepts_spank:
    $ Rogue.change_face("worried2", mouth = "lipbite", blush = 1)

    ch_Rogue "*gasp*"

    $ Rogue.change_face("worried1", mouth = "lipbite", blush = 2)

    if Rogue.quirk:
        ch_Rogue "Harder please."

    return

label Rogue_accepts_spank_love:

    return