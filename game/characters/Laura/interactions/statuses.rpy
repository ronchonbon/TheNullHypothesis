label Laura_became_miffed:

    return

label Laura_became_mad:
    if Laura in Player.date_planned.keys():
        ch_Laura "I don't want to go out tonight."

        $ del Player.date_planned[Laura]

    return

label Laura_became_heartbroken:
    if Laura in Player.date_planned.keys():
        ch_Laura "I. . . I'm going to train tonight."

        $ del Player.date_planned[Laura]

    return

label Laura_became_horny:

    return

label Laura_became_nympho:

    return