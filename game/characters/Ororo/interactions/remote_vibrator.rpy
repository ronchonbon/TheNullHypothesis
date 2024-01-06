label Ororo_remote_vibrator_off:
    if Ororo.location == Player.location:
        call Character_remote_vibrator_off_narrations(Ororo) from _call_Character_remote_vibrator_off_narrations_2

    return

label Ororo_remote_vibrator_on:
    if Ororo.location == Player.location:
        call Character_remote_vibrator_on_narrations(Ororo) from _call_Character_remote_vibrator_on_narrations_2

    return

label Ororo_remote_vibrator_25:
    if Ororo.location == Player.location:
        if renpy.random.random() > 0.5:
            call Character_desire_narrations(Ororo) from _call_Character_desire_narrations_15

            if renpy.random.random() > 0.5:
                call Character_remote_vibrator_narrations(Ororo, proper_subject = False) from _call_Character_remote_vibrator_narrations_18
        else:
            if renpy.random.random() > 0.5:
                call Character_remote_vibrator_narrations(Ororo) from _call_Character_remote_vibrator_narrations_19

    return

label Ororo_remote_vibrator_50:
    if Ororo.location == Player.location:
        if renpy.random.random() > 0.5:
            call Character_desire_narrations(Ororo) from _call_Character_desire_narrations_16

            if renpy.random.random() > 0.5:
                call Character_remote_vibrator_narrations(Ororo, proper_subject = False) from _call_Character_remote_vibrator_narrations_20
        else:
            if renpy.random.random() > 0.5:
                call Character_remote_vibrator_narrations(Ororo) from _call_Character_remote_vibrator_narrations_21

    return

label Ororo_remote_vibrator_75:
    if Ororo.location == Player.location:
        if renpy.random.random() > 0.5:
            call Character_desire_narrations(Ororo) from _call_Character_desire_narrations_17

            if renpy.random.random() > 0.5:
                call Character_remote_vibrator_narrations(Ororo, proper_subject = False) from _call_Character_remote_vibrator_narrations_22
        else:
            if renpy.random.random() > 0.5:
                call Character_remote_vibrator_narrations(Ororo) from _call_Character_remote_vibrator_narrations_23

    return

label Ororo_remote_vibrator_orgasm:
    call Character_orgasms(Ororo) from _call_Character_orgasms_6
    
    if Ororo.location == Player.location and renpy.random.random() > 0.5:
        call Character_remote_vibrator_narrations(Ororo, proper_subject = False) from _call_Character_remote_vibrator_narrations_24

    return

label Ororo_remote_vibrator_out_of_stamina:
    if Ororo.location == Player.location:
        if renpy.random.random() > 0.5:
            call Character_out_of_stamina_narrations(Ororo) from _call_Character_out_of_stamina_narrations_2

            if renpy.random.random() > 0.5:
                call Character_remote_vibrator_narrations(Ororo, proper_subject = False) from _call_Character_remote_vibrator_narrations_25
        else:
            if renpy.random.random() > 0.5:
                call Character_remote_vibrator_narrations(Ororo) from _call_Character_remote_vibrator_narrations_26

    call change_Character_stat(Ororo, "trust", -tiny_stat) from _call_change_Character_stat_591

    return