init python:

    def Rogue_remote_vibrator_off():
        label = "Rogue_remote_vibrator_off"

        conditions = [
            "False"]

        return EventClass(label, conditions)

label Rogue_remote_vibrator_off:
    if Rogue.location == Player.location:
        call Character_remote_vibrator_off_narrations(Rogue)

    return

init python:

    def Rogue_remote_vibrator_on():
        label = "Rogue_remote_vibrator_on"

        conditions = [
            "False"]

        return EventClass(label, conditions)

label Rogue_remote_vibrator_on:
    if Rogue.location == Player.location:
        call Character_remote_vibrator_on_narrations(Rogue)

    return

init python:

    def Rogue_remote_vibrator_25():
        label = "Rogue_remote_vibrator_25"

        conditions = [
            "False"]

        return EventClass(label, conditions)

label Rogue_remote_vibrator_25:
    if Rogue.location == Player.location:
        if renpy.random.random() > 0.5:
            call Character_desire_narrations(Rogue)

            if renpy.random.random() > 0.5:
                call Character_remote_vibrator_narrations(Rogue, proper_subject = False)
        else:
            if renpy.random.random() > 0.5:
                call Character_remote_vibrator_narrations(Rogue)

    return

init python:

    def Rogue_remote_vibrator_50():
        label = "Rogue_remote_vibrator_50"

        conditions = [
            "False"]

        return EventClass(label, conditions)

label Rogue_remote_vibrator_50:
    if Rogue.location == Player.location:
        if renpy.random.random() > 0.5:
            call Character_desire_narrations(Rogue)

            if renpy.random.random() > 0.5:
                call Character_remote_vibrator_narrations(Rogue, proper_subject = False)
        else:
            if renpy.random.random() > 0.5:
                call Character_remote_vibrator_narrations(Rogue)

    return

init python:

    def Rogue_remote_vibrator_75():
        label = "Rogue_remote_vibrator_75"

        conditions = [
            "False"]

        return EventClass(label, conditions)

label Rogue_remote_vibrator_75:
    if Rogue.location == Player.location:
        if renpy.random.random() > 0.5:
            call Character_desire_narrations(Rogue)

            if renpy.random.random() > 0.5:
                call Character_remote_vibrator_narrations(Rogue, proper_subject = False)
        else:
            if renpy.random.random() > 0.5:
                call Character_remote_vibrator_narrations(Rogue)

    return

init python:

    def Rogue_remote_vibrator_orgasm():
        label = "Rogue_remote_vibrator_orgasm"

        conditions = [
            "False"]

        return EventClass(label, conditions)

label Rogue_remote_vibrator_orgasm:
    call Character_orgasms(Rogue)
    
    if Rogue.location == Player.location and renpy.random.random() > 0.5:
        call Character_remote_vibrator_narrations(Rogue, proper_subject = False)

    return

init python:

    def Rogue_remote_vibrator_out_of_stamina():
        label = "Rogue_remote_vibrator_out_of_stamina"

        conditions = [
            "False"]

        return EventClass(label, conditions)

label Rogue_remote_vibrator_out_of_stamina:
    if Rogue.location == Player.location:
        if renpy.random.random() > 0.5:
            call Character_out_of_stamina_narrations(Rogue)

            if renpy.random.random() > 0.5:
                call Character_remote_vibrator_narrations(Rogue, proper_subject = False)
        else:
            if renpy.random.random() > 0.5:
                call Character_remote_vibrator_narrations(Rogue)

    call change_Character_stat(Rogue, "trust", -tiny_stat)

    return