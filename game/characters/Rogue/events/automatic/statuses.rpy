init python:

    def Rogue_became_miffed():
        label = "Rogue_became_miffed"

        conditions = [
            "False"]

        return EventClass(label, conditions)

label Rogue_became_miffed:

    return

init python:

    def Rogue_became_mad():
        label = "Rogue_became_mad"

        conditions = [
            "False"]

        return EventClass(label, conditions)

label Rogue_became_mad:
    if Rogue in Player.date_planned.keys():
        ch_Rogue "Ah'd rather be alone tonight."

        $ del Player.date_planned[Rogue]

    return

init python:

    def Rogue_became_heartbroken():
        label = "Rogue_became_heartbroken"

        conditions = [
            "False"]

        return EventClass(label, conditions)

label Rogue_became_heartbroken:
    if Rogue in Player.date_planned.keys():
        ch_Rogue "Ah. . . think we should cancel tonight. . ."

        $ del Player.date_planned[Rogue]

    return

init python:

    def Rogue_became_horny():
        label = "Rogue_became_horny"

        conditions = [
            "False"]

        return EventClass(label, conditions)

label Rogue_became_horny:

    return

init python:

    def Rogue_became_nympho():
        label = "Rogue_became_nympho"

        conditions = [
            "False"]

        return EventClass(label, conditions)

label Rogue_became_nympho:

    return