label check_for_Events(only_automatic = False, priority = False, waiting = False, traveling = False, chatting = False, texting = False, flirting = False, hooking_up = False, getting_ready_for_bed = False, sleeping = False, waking = False):
    $ automatic_Events = EventScheduler.get_automatic_Events()

    while automatic_Events:
        if not priority or automatic_Events[0].priority:
            call start_Event(automatic_Events[0]) from _call_start_Event_16

        $ automatic_Events.remove(automatic_Events[0])

    if not only_automatic:
        $ selected_Event = EventScheduler.choose_Event(waiting = waiting, traveling = traveling, chatting = chatting, texting = texting, flirting = flirting, hooking_up = hooking_up, getting_ready_for_bed = getting_ready_for_bed, sleeping = sleeping, waking = waking)

        if selected_Event:
            if not priority or selected_Event.priority:
                call start_Event(selected_Event) from _call_start_Event_17

    return