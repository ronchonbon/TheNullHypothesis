init python:

    def Jean_became_miffed():
        label = "Jean_became_miffed"

        conditions = [
            "False"]

        return EventClass(label, conditions)

label Jean_became_miffed:

    return

init python:

    def Jean_became_mad():
        label = "Jean_became_mad"

        conditions = [
            "False"]

        return EventClass(label, conditions)

label Jean_became_mad:
    if Jean in Player.date_planned.keys():
        ch_Jean "I really don't feel like going on a date anymore."

        $ del Player.date_planned[Jean]

    return

init python:

    def Jean_became_heartbroken():
        label = "Jean_became_heartbroken"

        conditions = [
            "False"]

        return EventClass(label, conditions)

label Jean_became_heartbroken:
    if Jean in Player.date_planned.keys():
        ch_Jean "I. . . think we should cancel for tonight. . ."

        $ del Player.date_planned[Jean]

    return

init python:

    def Jean_became_horny():
        label = "Jean_became_horny"

        conditions = [
            "False"]

        return EventClass(label, conditions)

label Jean_became_horny:

    return

init python:

    def Jean_became_nympho():
        label = "Jean_became_nympho"

        conditions = [
            "False"]

        return EventClass(label, conditions)

label Jean_became_nympho:

    return