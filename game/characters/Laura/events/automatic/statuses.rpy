init python:

    def Laura_became_miffed():
        label = "Laura_became_miffed"

        conditions = [
            "False"]

        return EventClass(label, conditions)

label Laura_became_miffed:

    return

init python:

    def Laura_became_mad():
        label = "Laura_became_mad"

        conditions = [
            "False"]

        return EventClass(label, conditions)

label Laura_became_mad:
    if Laura in Player.date_planned.keys():
        ch_Laura "I don't want to go out tonight."

        $ del Player.date_planned[Laura]

    return

init python:

    def Laura_became_heartbroken():
        label = "Laura_became_heartbroken"

        conditions = [
            "False"]

        return EventClass(label, conditions)

label Laura_became_heartbroken:
    if Laura in Player.date_planned.keys():
        ch_Laura "I. . . I'm going to train tonight."

        $ del Player.date_planned[Laura]

    return

init python:

    def Laura_became_horny():
        label = "Laura_became_horny"

        conditions = [
            "False"]

        return EventClass(label, conditions)

label Laura_became_horny:

    return

init python:

    def Laura_became_nympho():
        label = "Laura_became_nympho"

        conditions = [
            "False"]

        return EventClass(label, conditions)

label Laura_became_nympho:

    return