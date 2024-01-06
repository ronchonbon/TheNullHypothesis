label Laura_remote_vibrator_off:
    if Laura.location == Player.location:
        call Character_remote_vibrator_off_narrations(Laura) from _call_Character_remote_vibrator_off_narrations_1

    return

label Laura_remote_vibrator_on:
    if Laura.location == Player.location:
        call Character_remote_vibrator_on_narrations(Laura) from _call_Character_remote_vibrator_on_narrations_1

    return

label Laura_remote_vibrator_25:
    if Laura.location == Player.location:
        if renpy.random.random() > 0.5:
            call Character_desire_narrations(Laura) from _call_Character_desire_narrations_9

            if renpy.random.random() > 0.5:
                call Character_remote_vibrator_narrations(Laura, proper_subject = False) from _call_Character_remote_vibrator_narrations_9
        else:
            if renpy.random.random() > 0.5:
                call Character_remote_vibrator_narrations(Laura) from _call_Character_remote_vibrator_narrations_10

    return

label Laura_remote_vibrator_50:
    if Laura.location == Player.location:
        if renpy.random.random() > 0.5:
            call Character_desire_narrations(Laura) from _call_Character_desire_narrations_10

            if renpy.random.random() > 0.5:
                call Character_remote_vibrator_narrations(Laura, proper_subject = False) from _call_Character_remote_vibrator_narrations_11
        else:
            if renpy.random.random() > 0.5:
                call Character_remote_vibrator_narrations(Laura) from _call_Character_remote_vibrator_narrations_12

    return

label Laura_remote_vibrator_75:
    if Laura.location == Player.location:
        if renpy.random.random() > 0.5:
            call Character_desire_narrations(Laura) from _call_Character_desire_narrations_11

            if renpy.random.random() > 0.5:
                call Character_remote_vibrator_narrations(Laura, proper_subject = False) from _call_Character_remote_vibrator_narrations_13
        else:
            if renpy.random.random() > 0.5:
                call Character_remote_vibrator_narrations(Laura) from _call_Character_remote_vibrator_narrations_14

    return

label Laura_remote_vibrator_orgasm:
    call Character_orgasms(Laura) from _call_Character_orgasms_4
    
    if Laura.location == Player.location and renpy.random.random() > 0.5:
        call Character_remote_vibrator_narrations(Laura, proper_subject = False) from _call_Character_remote_vibrator_narrations_15

    return

label Laura_remote_vibrator_out_of_stamina:
    if Laura.location == Player.location:
        if renpy.random.random() > 0.5:
            call Character_out_of_stamina_narrations(Laura) from _call_Character_out_of_stamina_narrations_1

            if renpy.random.random() > 0.5:
                call Character_remote_vibrator_narrations(Laura, proper_subject = False) from _call_Character_remote_vibrator_narrations_16
        else:
            if renpy.random.random() > 0.5:
                call Character_remote_vibrator_narrations(Laura) from _call_Character_remote_vibrator_narrations_17

    call change_Character_stat(Laura, "trust", -tiny_stat) from _call_change_Character_stat_590

    return