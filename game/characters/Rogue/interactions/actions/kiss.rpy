label Rogue_rejects_kiss:

    return

label Rogue_accepts_kiss_first_time:

    return

label Rogue_accepts_kiss_second_time:

    return

label Rogue_accepts_kiss:

    return

label Rogue_accepts_kiss_love:

    return

label Rogue_rejects_makeout:
    $ Rogue.change_face("surprised2", blush = 1)

    pause 1.0

    $ Rogue.change_face("worried1", blush = 1)

    if not Rogue.History.check("makeout"):
        ch_Rogue "Maybe after we've kissed in the first place. . ."
    else:
        ch_Rogue "No thanks, [Rogue.Player_petname]."

    return

label Rogue_accepts_makeout_first_time:
    $ Rogue.change_face("smirk2", mouth = "lipbite", blush = 1)

    ch_Rogue "Ah won't say no to that. . ."

    return

label Rogue_accepts_makeout_second_time:

    return

label Rogue_accepts_makeout:
    $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

    ch_Rogue "You know ah'd never say no to that. . ."

    return

label Rogue_accepts_makeout_love:

    return