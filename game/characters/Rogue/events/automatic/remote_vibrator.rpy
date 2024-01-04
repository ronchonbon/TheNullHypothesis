init python:

    def Rogue_remote_vibrator_off():
        label = "Rogue_remote_vibrator_off"

        conditions = [
            "False"]

        return EventClass(label, conditions)

label Rogue_remote_vibrator_off:
    if Rogue.location == Player.location:
        call Character_remote_vibrator_off_narrations(Rogue) from _call_Character_remote_vibrator_off_narrations_2

    return

init python:

    def Rogue_remote_vibrator_on():
        label = "Rogue_remote_vibrator_on"

        conditions = [
            "False"]

        return EventClass(label, conditions)

label Rogue_remote_vibrator_on:
    if Rogue.location == Player.location:
        call Character_remote_vibrator_on_narrations(Rogue) from _call_Character_remote_vibrator_on_narrations_2

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
            call Character_desire_narrations(Rogue) from _call_Character_desire_narrations_15

            if renpy.random.random() > 0.5:
                call Character_remote_vibrator_narrations(Rogue, proper_subject = False) from _call_Character_remote_vibrator_narrations_18
        else:
            if renpy.random.random() > 0.5:
                call Character_remote_vibrator_narrations(Rogue) from _call_Character_remote_vibrator_narrations_19

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
            call Character_desire_narrations(Rogue) from _call_Character_desire_narrations_16

            if renpy.random.random() > 0.5:
                call Character_remote_vibrator_narrations(Rogue, proper_subject = False) from _call_Character_remote_vibrator_narrations_20
        else:
            if renpy.random.random() > 0.5:
                call Character_remote_vibrator_narrations(Rogue) from _call_Character_remote_vibrator_narrations_21

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
            call Character_desire_narrations(Rogue) from _call_Character_desire_narrations_17

            if renpy.random.random() > 0.5:
                call Character_remote_vibrator_narrations(Rogue, proper_subject = False) from _call_Character_remote_vibrator_narrations_22
        else:
            if renpy.random.random() > 0.5:
                call Character_remote_vibrator_narrations(Rogue) from _call_Character_remote_vibrator_narrations_23

    return

init python:

    def Rogue_remote_vibrator_orgasm():
        label = "Rogue_remote_vibrator_orgasm"

        conditions = [
            "False"]

        return EventClass(label, conditions)

label Rogue_remote_vibrator_orgasm:
    call Character_orgasms(Rogue) from _call_Character_orgasms_6
    
    if Rogue.location == Player.location and renpy.random.random() > 0.5:
        call Character_remote_vibrator_narrations(Rogue, proper_subject = False) from _call_Character_remote_vibrator_narrations_24

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
            call Character_out_of_stamina_narrations(Rogue) from _call_Character_out_of_stamina_narrations_2

            if renpy.random.random() > 0.5:
                call Character_remote_vibrator_narrations(Rogue, proper_subject = False) from _call_Character_remote_vibrator_narrations_25
        else:
            if renpy.random.random() > 0.5:
                call Character_remote_vibrator_narrations(Rogue) from _call_Character_remote_vibrator_narrations_26

    return