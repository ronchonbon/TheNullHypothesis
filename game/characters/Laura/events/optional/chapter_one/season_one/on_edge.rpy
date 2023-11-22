init python:

    def Laura_chapter_one_season_one_on_edge_setup():
        label = "Laura_chapter_one_season_one_on_edge_setup"

        conditions = [
            "Laura.location != Player.location",

            "renpy.random.random() > 0.75",

            "not EventScheduler.Events['Laura_chapter_one_season_one_on_edge'].completed",

            "time_index not in Laura.schedule.keys()",

            "chapter == 1 and season == 1",

            "time_index < 2",

            "Laura.is_in_normal_mood()"]

        repeatable = True
        automatic = True

        return EventClass(label, conditions, repeatable = repeatable, automatic = automatic)

label Laura_chapter_one_season_one_on_edge_setup:
    call send_Characters(Laura, "bg_campus", behavior = False) from _call_send_Characters_334
    
    return

init python:

    def Laura_chapter_one_season_one_on_edge():
        label = "Laura_chapter_one_season_one_on_edge"

        conditions = [
            "Player.destination == 'bg_campus'",

            "chapter == 1 and season == 1",

            "time_index < 2",
            
            "Laura.location == 'bg_campus'",

            "Laura.is_in_normal_mood()"]

        traveling = True

        markers = {
            "bg_campus": [
                "chapter == 1 and season == 1",

                "time_index == 2",
            
                "Laura.location == 'bg_campus'",

                "Laura.is_in_normal_mood()"]}

        return EventClass(label, conditions, traveling = traveling, markers = markers)

label Laura_chapter_one_season_one_on_edge:
    $ ongoing_Event = True

    menu:
        extend ""
        "See if [Laura.name] is okay":
            pass
        "She's probably fine":
            "She's probably just doing some kind of 'advance awareness training' or something. . ."

            call remove_Characters(Laura) from _call_remove_Characters_332

            $ EventScheduler.Events["Laura_chapter_one_season_one_on_edge"].completed = False
            $ EventScheduler.Events["Laura_chapter_one_season_one_on_edge"].completed_when = 1e8

            $ EventScheduler.Events["Laura_chapter_one_season_one_on_edge"].counter = 0

            $ ongoing_Event = False

            return

    $ ongoing_Event = False

    return