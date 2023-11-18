init python:

    def Rogue_chapter_one_season_one_jogging():
        label = "Rogue_chapter_one_season_one_jogging"

        conditions = [
            "chapter == 1 and season == 1",
            "time_index < 3",
            "Player.destination == 'bg_campus'",
            "Rogue.destination == 'bg_campus'"]

        waiting = True
        traveling = True

        priority = 99

        return EventClass(label, conditions, waiting = waiting, traveling = traveling, priority = priority)

label Rogue_chapter_one_season_one_jogging:
    $ ongoing_Event = True

    $ ongoing_Event = False

    return