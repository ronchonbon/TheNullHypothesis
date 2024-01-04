init python:

    def Jean_masturbating_25():
        label = "Jean_masturbating_25"

        conditions = [
            "False"]

        return EventClass(label, conditions)

label Jean_masturbating_25:
    if Jean.location == Player.location and renpy.random.random() > 0.5:
        call Character_desire_narrations(Jean) from _call_Character_desire_narrations

    return

init python:

    def Jean_masturbating_50():
        label = "Jean_masturbating_50"

        conditions = [
            "False"]

        return EventClass(label, conditions)

label Jean_masturbating_50:
    if Jean.location == Player.location and renpy.random.random() > 0.5:
        call Character_desire_narrations(Jean)

    return

init python:

    def Jean_masturbating_75():
        label = "Jean_masturbating_75"

        conditions = [
            "False"]

        return EventClass(label, conditions)

label Jean_masturbating_75:
    if Jean.location == Player.location and renpy.random.random() > 0.5:
        call Character_desire_narrations(Jean)

    return

init python:

    def Jean_masturbating_orgasm():
        label = "Jean_masturbating_orgasm"

        conditions = [
            "False"]

        return EventClass(label, conditions)

label Jean_masturbating_orgasm:
    call Character_orgasms(Jean)

    return