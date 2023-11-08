label Ororo_texting(message):
    python:
        for E in Ororo.timed_text_options.keys():
            for text in Ororo.timed_text_options[E]:
                if message == text:
                    renpy.call(f"{E}_response")

    if Ororo.timed_text_options:
        call change_Girl_stat(Ororo, "love", 0) from _call_change_Girl_stat_524

        $ Ororo.timed_text_options = {}

    if message == "how are you?":
        $ selected_Event = EventScheduler.choose_Event(texting = True)

        if selected_Event:
            call start_Event(selected_Event) from _call_start_Event_4
        else:
            if time_index == 3:
                if approval_check(Ororo, threshold = "talk_late"):
                    call Ororo_text_how_are_you_late_accept from _call_Ororo_text_how_are_you_late_accept
                else:
                    if approval_check(Ororo, threshold = "friendship"):
                        call Ororo_text_how_are_you_late_reject from _call_Ororo_text_how_are_you_late_reject
                    else:
                        if Ororo.History.check("said_too_late_to_text", tracker = "recent") == 1:
                            call Ororo_text_how_are_you_late_reject_asked_once from _call_Ororo_text_how_are_you_late_reject_asked_once
                        elif Ororo.History.check("said_too_late_to_text", tracker = "recent") > 1:
                            call Ororo_text_how_are_you_late_reject_asked_twice from _call_Ororo_text_how_are_you_late_reject_asked_twice
                        else:
                            call Ororo_text_how_are_you_late_reject from _call_Ororo_text_how_are_you_late_reject_1

                    $ Ororo.History.update("said_too_late_to_text")
            else:
                $ status = Ororo.get_status()

                if status:
                    call expression f"Ororo_text_how_are_you_{status}" from _call_expression_24
                elif approval_check(Ororo, threshold = "love"):
                    call Ororo_text_how_are_you_love from _call_Ororo_text_how_are_you_love
                elif Ororo in Partners:
                    call Ororo_text_how_are_you_relationship from _call_Ororo_text_how_are_you_relationship
                else:
                    call Ororo_text_how_are_you from _call_Ororo_text_how_are_you

        $ Ororo.History.update("sent_how_are_you_text")

    if "good morning" in message:
        $ status = Ororo.get_status()

        if status:
            call expression f"Ororo_text_good_morning_{status}" from _call_expression_25
        elif approval_check(Ororo, threshold = "love"):
            call Ororo_text_good_morning_love from _call_Ororo_text_good_morning_love
        elif Ororo in Partners:
            call Ororo_text_good_morning_relationship from _call_Ororo_text_good_morning_relationship
        else:
            call Ororo_text_good_morning from _call_Ororo_text_good_morning

        $ Ororo.History.update("sent_good_morning_text")

    if "goodnight" in message:
        $ status = Ororo.get_status()

        if status:
            call expression f"Ororo_text_goodnight_{status}" from _call_expression_26
        elif approval_check(Ororo, threshold = "love"):
            call Ororo_text_goodnight_love from _call_Ororo_text_goodnight_love
        elif Ororo in Partners:
            call Ororo_text_goodnight_relationship from _call_Ororo_text_goodnight_relationship
        else:
            call Ororo_text_goodnight from _call_Ororo_text_goodnight

        $ Ororo.History.update("said_goodnight")

    if message == "wanna come over?":
        call summon(Ororo) from _call_summon_2

    return

label Ororo_text_how_are_you:

    return

label Ororo_text_how_are_you_late_accept:

    return

label Ororo_text_how_are_you_late_reject:

    return

label Ororo_text_how_are_you_late_reject_asked_once:

    return

label Ororo_text_how_are_you_late_reject_asked_twice:

    return

label Ororo_text_how_are_you_relationship:

    return

label Ororo_text_how_are_you_love:

    return

label Ororo_text_how_are_you_mad:

    return

label Ororo_text_how_are_you_hearbroken:

    return

label Ororo_text_how_are_you_horny:

    return

label Ororo_text_how_are_you_nympho:

    return

label Ororo_text_good_morning:

    return

label Ororo_text_good_morning_relationship:

    return

label Ororo_text_good_morning_love:

    return

label Ororo_text_good_morning_mad:

    return

label Ororo_text_good_morning_hearbroken:

    return

label Ororo_text_good_morning_horny:

    return

label Ororo_text_good_morning_nympho:

    return

label Ororo_text_goodnight:

    return

label Ororo_text_goodnight_relationship:

    return

label Ororo_text_goodnight_love:

    return

label Ororo_text_goodnight_mad:

    return

label Ororo_text_goodnight_hearbroken:

    return

label Ororo_text_goodnight_horny:

    return

label Ororo_text_goodnight_nympho:

    return