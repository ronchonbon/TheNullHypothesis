label Charles_texting(message):
    if message == "how's it going?":
        $ selected_Event = EventScheduler.choose_Event(texting = True)

        if selected_Event:
            call start_Event(selected_Event) from _call_start_Event
        else:
            if time_index == 3:
                if Charles.History.check("said_too_late_to_text", tracker = "recent") == 1:
                    call Charles_text_how_are_you_late_reject_asked_once from _call_Charles_text_how_are_you_late_reject_asked_once
                elif Charles.History.check("said_too_late_to_text", tracker = "recent") > 1:
                    call Charles_text_how_are_you_late_reject_asked_twice from _call_Charles_text_how_are_you_late_reject_asked_twice
                else:
                    call Charles_text_how_are_you_late_reject from _call_Charles_text_how_are_you_late_reject

                $ Charles.History.update("said_too_late_to_text")
            else:
                call Charles_text_how_are_you from _call_Charles_text_how_are_you

        $ Charles.History.update("sent_how_are_you_text")

    return

label Charles_text_how_are_you:

    return

label Charles_text_how_are_you_late_reject:

    return

label Charles_text_how_are_you_late_reject_asked_once:

    return

label Charles_text_how_are_you_late_reject_asked_twice:

    return