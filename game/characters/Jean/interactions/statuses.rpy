label Jean_became_miffed:

    return

label Jean_became_mad:
    if Jean in Player.date_planned.keys():
        ch_Jean "I really don't feel like going on a date anymore."

        $ del Player.date_planned[Jean]

    return

label Jean_became_heartbroken:
    if Jean in Player.date_planned.keys():
        ch_Jean "I. . . think we should cancel for tonight. . ."

        $ del Player.date_planned[Jean]

    return

label Jean_became_horny:

    return

label Jean_became_nympho:

    return