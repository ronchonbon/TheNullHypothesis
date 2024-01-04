init python:

    def Jean_remote_vibrator_off():
        label = "Jean_remote_vibrator_off"

        conditions = [
            "False"]

        return EventClass(label, conditions)

label Jean_remote_vibrator_off:
    if Jean.location == Player.location:
        call Character_remote_vibrator_off_narrations(Jean) from _call_Character_remote_vibrator_off_narrations

    return

init python:

    def Jean_remote_vibrator_on():
        label = "Jean_remote_vibrator_on"

        conditions = [
            "False"]

        return EventClass(label, conditions)

label Jean_remote_vibrator_on:
    if Jean.location == Player.location:
        call Character_remote_vibrator_on_narrations(Jean) from _call_Character_remote_vibrator_on_narrations

    return

init python:

    def Jean_remote_vibrator_25():
        label = "Jean_remote_vibrator_25"

        conditions = [
            "False"]

        return EventClass(label, conditions)

label Jean_remote_vibrator_25:
    if Jean.location == Player.location:
        if renpy.random.random() > 0.5:
            call Character_desire_narrations(Jean)

            if renpy.random.random() > 0.5:
                call Character_remote_vibrator_narrations(Jean, proper_subject = False) from _call_Character_remote_vibrator_narrations
        else:
            if renpy.random.random() > 0.5:
                call Character_remote_vibrator_narrations(Jean)

    return

init python:

    def Jean_remote_vibrator_50():
        label = "Jean_remote_vibrator_50"

        conditions = [
            "False"]

        return EventClass(label, conditions)

label Jean_remote_vibrator_50:
    if Jean.location == Player.location:
        if renpy.random.random() > 0.5:
            call Character_desire_narrations(Jean)

            if renpy.random.random() > 0.5:
                call Character_remote_vibrator_narrations(Jean, proper_subject = False)
        else:
            if renpy.random.random() > 0.5:
                call Character_remote_vibrator_narrations(Jean)

    return

init python:

    def Jean_remote_vibrator_75():
        label = "Jean_remote_vibrator_75"

        conditions = [
            "False"]

        return EventClass(label, conditions)

label Jean_remote_vibrator_75:
    if Jean.location == Player.location:
        if renpy.random.random() > 0.5:
            call Character_desire_narrations(Jean)

            if renpy.random.random() > 0.5:
                call Character_remote_vibrator_narrations(Jean, proper_subject = False)
        else:
            if renpy.random.random() > 0.5:
                call Character_remote_vibrator_narrations(Jean)

    return

init python:

    def Jean_remote_vibrator_orgasm():
        label = "Jean_remote_vibrator_orgasm"

        conditions = [
            "False"]

        return EventClass(label, conditions)

label Jean_remote_vibrator_orgasm:
    call Character_orgasms(Jean)
    
    if Jean.location == Player.location and renpy.random.random() > 0.5:
        call Character_remote_vibrator_narrations(Jean, proper_subject = False)

    return

init python:

    def Jean_remote_vibrator_out_of_stamina():
        label = "Jean_remote_vibrator_out_of_stamina"

        conditions = [
            "False"]

        return EventClass(label, conditions)

label Jean_remote_vibrator_out_of_stamina:
    if Jean.location == Player.location:
        if renpy.random.random() > 0.5:
            call Character_out_of_stamina_narrations(Jean) from _call_Character_out_of_stamina_narrations

            if renpy.random.random() > 0.5:
                call Character_remote_vibrator_narrations(Jean, proper_subject = False)
        else:
            if renpy.random.random() > 0.5:
                call Character_remote_vibrator_narrations(Jean)

    call change_Character_stat(Jean, "trust", -tiny_stat)

    return