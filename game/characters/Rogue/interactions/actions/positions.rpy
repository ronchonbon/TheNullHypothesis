label Rogue_rejects_masturbation:
    $ Rogue.change_face("worried1", blush = 1)

    ch_Rogue "Could we. . . could we stay like this?"

    return

label Rogue_accepts_masturbation_first_time:
    $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

    ch_Rogue "Ah suppose we could lean back."

    return

label Rogue_accepts_masturbation_second_time:

    return

label Rogue_accepts_masturbation:
    $ Rogue.change_face("sexy", mouth = "lipbite", blush = 1)

    return

label Rogue_accepts_masturbation_love:

    return

label Rogue_rejects_hands_and_knees:
    $ Rogue.change_face("worried1", blush = 1)

    ch_Rogue ". . . Ah'm not there yet, sorry [Rogue.Player_petname]. . ."

    return

label Rogue_accepts_hands_and_knees_first_time:
    $ Rogue.change_face("sexy", mouth = "lipbite", blush = 1)

    ch_Rogue "Ah guess it won't hurt."

    return

label Rogue_accepts_hands_and_knees_second_time:

    return

label Rogue_accepts_hands_and_knees:
    $ Rogue.change_face("sexy", mouth = "smirk", blush = 1)

    ch_Rogue "Like the view?"

    return

label Rogue_accepts_hands_and_knees_love:

    return
    
label Rogue_rejects_missionary:
    $ Rogue.change_face("worried1", blush = 2)

    ch_Rogue "Slow down, [Rogue.Player_petname]. . ."

    return

label Rogue_accepts_missionary_first_time:
    $ Rogue.change_face("worried1", blush = 2)

    ch_Rogue "Like this?"

    return

label Rogue_accepts_missionary_second_time:

    return

label Rogue_accepts_missionary:
    $ Rogue.change_face("sexy", mouth = "lipbite", blush = 2)

    ch_Rogue "Ah love you on top. . ."

    return

label Rogue_accepts_missionary_love:

    return

label Rogue_rejects_cowgirl:

    return

label Rogue_accepts_cowgirl_first_time:

    return

label Rogue_accepts_cowgirl_second_time:

    return

label Rogue_accepts_cowgirl:

    return

label Rogue_accepts_cowgirl_love:

    return

label Rogue_rejects_doggy:
    $ Rogue.change_face("worried1", blush = 2)

    ch_Rogue "No way, not yet. . ."

    return

label Rogue_accepts_doggy_first_time:
    $ Rogue.change_face("worried1", blush = 2)

    ch_Rogue "Just. . . like this?"

    return

label Rogue_accepts_doggy_second_time:

    return

label Rogue_accepts_doggy:
    $ Rogue.change_face("sexy", blush = 2)

    ch_Rogue "Mmm, take me [Rogue.Player_petname]. . ."

    return

label Rogue_accepts_doggy_love:

    return