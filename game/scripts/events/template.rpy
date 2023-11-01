init python:

    def Event():
        label = "Event_label"

        conditions = [
            "Rogue in active_Girls",
            "Rogue.love >= 45"]

        chatting = True

        priority = True

        repeatable = False

        return EventClass(label, conditions, chatting = chatting, priority = priority, repeatable = repeatable)

label Event_label:
    "Congrats, you triggered an event."

    return
