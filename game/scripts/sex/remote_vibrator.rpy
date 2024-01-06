label remote_vibrator_on(Character):
    if Character.location == Player.location:
        call remote_vibrator_on_narrations(Character) from _call_remote_vibrator_on_narrations

    call expression f"{Character.tag}_remote_vibrator_on" from _call_expression_133

    return

label remote_vibrator_off(Character):
    if Character.location == Player.location:
        call remote_vibrator_off_narrations(Character) from _call_remote_vibrator_off_narrations

    call expression f"{Character.tag}_remote_vibrator_off" from _call_expression_134

    return