label ask_Girl_to_use_Toy(Girl, Toy, buttplug_size = None, instant = False):
    if Girl.status["miffed"] or Girl.status["mad"]:
        call expression f"{Girl.tag}_{Toy.string}_change_reject" from _call_expression_335

        $ Girl.History.update(f"said_no_to_{Toy.string}")
    elif approval_check(Girl, threshold = Toy.threshold, extra_condition = "sex_toy"):
        if Toy.string in ["heart_anal_plug", "round_anal_plug"]:
            if Girl.History.check(f"used_buttplug_size_{buttplug_size}", tracker = "daily"):
                call expression f"{Girl.tag}_{Toy.string}_change_reject_worn_out" from _call_expression_336
            else:
                call expression f"{Girl.tag}_{Toy.string}_change" pass (plug_size = buttplug_size) from _call_expression_337

                if _return:
                    call expose(Girl, "anus") from _call_expose_16

                    pause 1.0

                    $ Girl.buttplug = Toy
                    $ Girl.buttplug_size = buttplug_size

                    pause 1.0

                    call fix_clothing(Girl) from _call_fix_clothing_4

                    $ Girl.History.update(f"used_buttplug_size_{buttplug_size}")

                    if buttplug_size == Girl.anal_training and Girl.History.check(f"used_buttplug_size_{buttplug_size}") >= 5:
                        $ Girl.anal_training = buttplug_size + 1
        elif Toy.string in ["remote_vibrator"]:
            call expression f"{Girl.tag}_{Toy.string}_change" from _call_expression_338

            call expose(Girl, "pussy") from _call_expose_17

            pause 1.0

            $ Girl.remote_vibrator = True

            pause 1.0

            call fix_clothing(Girl) from _call_fix_clothing

            $ Girl.History.update(Toy.string)
    else:
        if Toy.string in ["heart_anal_plug", "round_anal_plug"]:
            if Girl.History.check(f"said_no_to_{Toy.string}", tracker = "recent") >= 2:
                call change_Girl_stat(Girl, "love", -5) from _call_change_Girl_stat_1023
                call change_Girl_stat(Girl, "trust", -5) from _call_change_Girl_stat_1024

                call expression f"{Girl.tag}_rejected_buttplug_twice" from _call_expression_340
            elif Girl.History.check(f"said_no_to_{Toy.string}", tracker = "recent") == 1:
                call change_Girl_stat(Girl, "love", -2) from _call_change_Girl_stat_1025

                call expression f"{Girl.tag}_rejected_buttplug_once" from _call_expression_341
            else:
                call expression f"{Girl.tag}_{Toy.string}_change_reject" from _call_expression_342
        elif Toy.string in ["remote_vibrator"]:
            if Girl.History.check(f"said_no_to_{Toy.string}", tracker = "recent") >= 2:
                call change_Girl_stat(Girl, "love", -5) from _call_change_Girl_stat_1026
                call change_Girl_stat(Girl, "trust", -5) from _call_change_Girl_stat_1027

                call expression f"{Girl.tag}_rejected_{Toy.string}_twice" from _call_expression_343
            elif Girl.History.check(f"said_no_to_{Toy.string}", tracker = "recent") == 1:
                call change_Girl_stat(Girl, "love", -2) from _call_change_Girl_stat_1028

                call expression f"{Girl.tag}_rejected_{Toy.string}_once" from _call_expression_344
            else:
                call expression f"{Girl.tag}_{Toy.string}_change_reject" from _call_expression_345

        $ Girl.History.update(f"said_no_to_{Toy.string}")

    return