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
            call Character_desire_narrations(Jean) from _call_Character_desire_narrations_3

            if renpy.random.random() > 0.5:
                call Character_remote_vibrator_narrations(Jean, proper_subject = False) from _call_Character_remote_vibrator_narrations
        else:
            if renpy.random.random() > 0.5:
                call Character_remote_vibrator_narrations(Jean) from _call_Character_remote_vibrator_narrations_1

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
            call Character_desire_narrations(Jean) from _call_Character_desire_narrations_4

            if renpy.random.random() > 0.5:
                call Character_remote_vibrator_narrations(Jean, proper_subject = False) from _call_Character_remote_vibrator_narrations_2
        else:
            if renpy.random.random() > 0.5:
                call Character_remote_vibrator_narrations(Jean) from _call_Character_remote_vibrator_narrations_3

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
            call Character_desire_narrations(Jean) from _call_Character_desire_narrations_5

            if renpy.random.random() > 0.5:
                call Character_remote_vibrator_narrations(Jean, proper_subject = False) from _call_Character_remote_vibrator_narrations_4
        else:
            if renpy.random.random() > 0.5:
                call Character_remote_vibrator_narrations(Jean) from _call_Character_remote_vibrator_narrations_5

    return

init python:

    def Jean_remote_vibrator_orgasm():
        label = "Jean_remote_vibrator_orgasm"

        conditions = [
            "False"]

        return EventClass(label, conditions)

label Jean_remote_vibrator_orgasm:
    call Character_orgasms(Jean) from _call_Character_orgasms_2
    
    if Jean.location == Player.location and renpy.random.random() > 0.5:
        call Character_remote_vibrator_narrations(Jean, proper_subject = False) from _call_Character_remote_vibrator_narrations_6

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
                call Character_remote_vibrator_narrations(Jean, proper_subject = False) from _call_Character_remote_vibrator_narrations_7
        else:
            if renpy.random.random() > 0.5:
                call Character_remote_vibrator_narrations(Jean) from _call_Character_remote_vibrator_narrations_8

    return