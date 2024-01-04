init python:

    def Ororo_remote_vibrator_off():
        label = "Ororo_remote_vibrator_off"

        conditions = [
            "False"]

        return EventClass(label, conditions)

label Ororo_remote_vibrator_off:
    if Ororo.location == Player.location:
        call Character_remote_vibrator_off_narrations(Ororo)

    return

init python:

    def Ororo_remote_vibrator_on():
        label = "Ororo_remote_vibrator_on"

        conditions = [
            "False"]

        return EventClass(label, conditions)

label Ororo_remote_vibrator_on:
    if Ororo.location == Player.location:
        call Character_remote_vibrator_on_narrations(Ororo)

    return

init python:

    def Ororo_remote_vibrator_25():
        label = "Ororo_remote_vibrator_25"

        conditions = [
            "False"]

        return EventClass(label, conditions)

label Ororo_remote_vibrator_25:
    if Ororo.location == Player.location:
        if renpy.random.random() > 0.5:
            call Character_desire_narrations(Ororo)

            if renpy.random.random() > 0.5:
                call Character_remote_vibrator_narrations(Ororo, proper_subject = False)
        else:
            if renpy.random.random() > 0.5:
                call Character_remote_vibrator_narrations(Ororo)

    return

init python:

    def Ororo_remote_vibrator_50():
        label = "Ororo_remote_vibrator_50"

        conditions = [
            "False"]

        return EventClass(label, conditions)

label Ororo_remote_vibrator_50:
    if Ororo.location == Player.location:
        if renpy.random.random() > 0.5:
            call Character_desire_narrations(Ororo)

            if renpy.random.random() > 0.5:
                call Character_remote_vibrator_narrations(Ororo, proper_subject = False)
        else:
            if renpy.random.random() > 0.5:
                call Character_remote_vibrator_narrations(Ororo)

    return

init python:

    def Ororo_remote_vibrator_75():
        label = "Ororo_remote_vibrator_75"

        conditions = [
            "False"]

        return EventClass(label, conditions)

label Ororo_remote_vibrator_75:
    if Ororo.location == Player.location:
        if renpy.random.random() > 0.5:
            call Character_desire_narrations(Ororo)

            if renpy.random.random() > 0.5:
                call Character_remote_vibrator_narrations(Ororo, proper_subject = False)
        else:
            if renpy.random.random() > 0.5:
                call Character_remote_vibrator_narrations(Ororo)

    return

init python:

    def Ororo_remote_vibrator_orgasm():
        label = "Ororo_remote_vibrator_orgasm"

        conditions = [
            "False"]

        return EventClass(label, conditions)

label Ororo_remote_vibrator_orgasm:
    call Character_orgasms(Ororo)
    
    if Ororo.location == Player.location and renpy.random.random() > 0.5:
        call Character_remote_vibrator_narrations(Ororo, proper_subject = False)

    return

init python:

    def Ororo_remote_vibrator_out_of_stamina():
        label = "Ororo_remote_vibrator_out_of_stamina"

        conditions = [
            "False"]

        return EventClass(label, conditions)

label Ororo_remote_vibrator_out_of_stamina:
    if Ororo.location == Player.location:
        if renpy.random.random() > 0.5:
            call Character_out_of_stamina_narrations(Ororo)

            if renpy.random.random() > 0.5:
                call Character_remote_vibrator_narrations(Ororo, proper_subject = False)
        else:
            if renpy.random.random() > 0.5:
                call Character_remote_vibrator_narrations(Ororo)

    call change_Character_stat(Ororo, "trust", -tiny_stat)

    return