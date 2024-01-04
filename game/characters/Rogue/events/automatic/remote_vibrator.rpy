init python:

    def Rogue_remote_vibrator_off():
        label = "Rogue_remote_vibrator_off"

        conditions = [
            "False"]

        return EventClass(label, conditions)

label Rogue_remote_vibrator_off:
    if Rogue.location == Player.location:
        call Character_remote_vibrator_off_narrations(Rogue) from _call_Character_remote_vibrator_off_narrations_3

    return

init python:

    def Rogue_remote_vibrator_on():
        label = "Rogue_remote_vibrator_on"

        conditions = [
            "False"]

        return EventClass(label, conditions)

label Rogue_remote_vibrator_on:
    if Rogue.location == Player.location:
        call Character_remote_vibrator_on_narrations(Rogue) from _call_Character_remote_vibrator_on_narrations_3

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
            call Character_desire_narrations(Rogue) from _call_Character_desire_narrations_21

            if renpy.random.random() > 0.5:
                call Character_remote_vibrator_narrations(Rogue, proper_subject = False) from _call_Character_remote_vibrator_narrations_27
        else:
            if renpy.random.random() > 0.5:
                call Character_remote_vibrator_narrations(Rogue) from _call_Character_remote_vibrator_narrations_28

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
            call Character_desire_narrations(Rogue) from _call_Character_desire_narrations_22

            if renpy.random.random() > 0.5:
                call Character_remote_vibrator_narrations(Rogue, proper_subject = False) from _call_Character_remote_vibrator_narrations_29
        else:
            if renpy.random.random() > 0.5:
                call Character_remote_vibrator_narrations(Rogue) from _call_Character_remote_vibrator_narrations_30

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
            call Character_desire_narrations(Rogue) from _call_Character_desire_narrations_23

            if renpy.random.random() > 0.5:
                call Character_remote_vibrator_narrations(Rogue, proper_subject = False) from _call_Character_remote_vibrator_narrations_31
        else:
            if renpy.random.random() > 0.5:
                call Character_remote_vibrator_narrations(Rogue) from _call_Character_remote_vibrator_narrations_32

    return

init python:

    def Rogue_remote_vibrator_orgasm():
        label = "Rogue_remote_vibrator_orgasm"

        conditions = [
            "False"]

        return EventClass(label, conditions)

label Rogue_remote_vibrator_orgasm:
    call Character_orgasms(Rogue) from _call_Character_orgasms_8
    
    if Rogue.location == Player.location and renpy.random.random() > 0.5:
        call Character_remote_vibrator_narrations(Rogue, proper_subject = False) from _call_Character_remote_vibrator_narrations_33

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
            call Character_out_of_stamina_narrations(Rogue) from _call_Character_out_of_stamina_narrations_3

            if renpy.random.random() > 0.5:
                call Character_remote_vibrator_narrations(Rogue, proper_subject = False) from _call_Character_remote_vibrator_narrations_34
        else:
            if renpy.random.random() > 0.5:
                call Character_remote_vibrator_narrations(Rogue) from _call_Character_remote_vibrator_narrations_35

    call change_Character_stat(Rogue, "trust", -tiny_stat) from _call_change_Character_stat_592

    return