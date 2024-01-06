label Rogue_became_miffed:

    return

label Rogue_became_mad:
    if Rogue in Player.date_planned.keys():
        ch_Rogue "Ah'd rather be alone tonight."

        $ del Player.date_planned[Rogue]

    return

label Rogue_became_heartbroken:
    if Rogue in Player.date_planned.keys():
        ch_Rogue "Ah. . . think we should cancel tonight. . ."

        $ del Player.date_planned[Rogue]

    return

label Rogue_became_horny:

    return

label Rogue_became_nympho:

    return