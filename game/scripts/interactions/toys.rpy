label ask_Character_to_use_Toy(Character, Toy, buttplug_size = None, instant = False):
    if Character.status["miffed"] or Character.status["mad"]:
        call expression f"{Character.tag}_{Toy.string}_change_reject" from _call_expression_335

        $ Character.History.update(f"said_no_to_{Toy.string}")
    elif approval_check(Character, threshold = Toy.threshold, extra_condition = "sex_toy"):
        if Toy.string in ["heart_anal_plug", "round_anal_plug"]:
            if Character.History.check(f"used_buttplug_size_{buttplug_size}", tracker = "daily"):
                call expression f"{Character.tag}_{Toy.string}_change_reject_worn_out" from _call_expression_336
            else:
                call expression f"{Character.tag}_{Toy.string}_change" pass (plug_size = buttplug_size) from _call_expression_337

                if _return:
                    call expose(Character, "anus") from _call_expose_16

                    pause 1.0

                    $ Character.buttplug = Toy
                    $ Character.buttplug_size = buttplug_size

                    pause 1.0

                    call fix_clothing(Character) from _call_fix_clothing_4

                    $ Character.History.update(f"used_buttplug_size_{buttplug_size}")

                    if buttplug_size == Character.anal_training and Character.History.check(f"used_buttplug_size_{buttplug_size}") >= 5:
                        $ Character.anal_training = buttplug_size + 1
        elif Toy.string in ["remote_vibrator"]:
            call expression f"{Character.tag}_{Toy.string}_change" from _call_expression_338

            call expose(Character, "pussy") from _call_expose_17

            pause 1.0

            $ Character.remote_vibrator = True

            pause 1.0

            call fix_clothing(Character) from _call_fix_clothing

            $ Character.History.update(Toy.string)
    else:
        if Toy.string in ["heart_anal_plug", "round_anal_plug"]:
            if Character.History.check(f"said_no_to_{Toy.string}", tracker = "recent") >= 2:
                call change_Character_stat(Character, "love", -5) from _call_change_Character_stat_1023
                call change_Character_stat(Character, "trust", -5) from _call_change_Character_stat_1024

                call expression f"{Character.tag}_rejected_buttplug_twice" from _call_expression_340
            elif Character.History.check(f"said_no_to_{Toy.string}", tracker = "recent") == 1:
                call change_Character_stat(Character, "love", -2) from _call_change_Character_stat_1025

                call expression f"{Character.tag}_rejected_buttplug_once" from _call_expression_341
            else:
                call expression f"{Character.tag}_{Toy.string}_change_reject" from _call_expression_342
        elif Toy.string in ["remote_vibrator"]:
            if Character.History.check(f"said_no_to_{Toy.string}", tracker = "recent") >= 2:
                call change_Character_stat(Character, "love", -5) from _call_change_Character_stat_1026
                call change_Character_stat(Character, "trust", -5) from _call_change_Character_stat_1027

                call expression f"{Character.tag}_rejected_{Toy.string}_twice" from _call_expression_343
            elif Character.History.check(f"said_no_to_{Toy.string}", tracker = "recent") == 1:
                call change_Character_stat(Character, "love", -2) from _call_change_Character_stat_1028

                call expression f"{Character.tag}_rejected_{Toy.string}_once" from _call_expression_344
            else:
                call expression f"{Character.tag}_{Toy.string}_change_reject" from _call_expression_345

        $ Character.History.update(f"said_no_to_{Toy.string}")

    return