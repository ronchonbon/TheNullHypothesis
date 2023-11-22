init python:

    def Laura_chapter_one_season_one_outcast_setup():
        label = "Laura_chapter_one_season_one_outcast_setup"

        conditions = [
            "Laura.location != Player.location",

            "renpy.random.random() > 0.75",

            "not EventScheduler.Events['Laura_chapter_one_season_one_outcast'].completed",

            "time_index not in Laura.schedule.keys()",

            "chapter == 1 and season == 1",

            "weekday < 5 and time_index < 2",
            "clock == Player.max_stamina",

            "Laura.is_in_normal_mood()"]

        repeatable = True
        automatic = True

        return EventClass(label, conditions, repeatable = repeatable, automatic = automatic)

label Laura_chapter_one_season_one_outcast_setup:
    call send_Characters(Laura, "bg_classroom", behavior = "in_class") from _call_send_Characters_335
    
    return

init python:

    def Laura_chapter_one_season_one_outcast():
        label = "Laura_chapter_one_season_one_outcast"

        conditions = [
            "Player.destination == 'bg_classroom'",
            
            "chapter == 1 and season == 1",

            "weekday < 5 and time_index < 2",
            "clock == Player.max_stamina",
            
            "Laura.location == 'bg_classroom'",
            "Laura.behavior == 'in_class'",

            "Laura.is_in_normal_mood()"]

        traveling = True

        markers = {
            "bg_classroom": [
                "chapter == 1 and season == 1",

                "weekday < 5 and time_index < 2",
                "clock == Player.max_stamina",
                
                "Laura.location == 'bg_classroom'",
                "Laura.behavior == 'in_class'",

                "Laura.is_in_normal_mood()"]}

        return EventClass(label, conditions, traveling = traveling, markers = markers)

label Laura_chapter_one_season_one_outcast:
    $ ongoing_Event = True

    menu:
        extend ""
        "Sit next to [Laura.name]":
            pass
        "Take a random seat":
            "You grab a seat in the chair closest to you."

            call send_Characters(Laura, "nearby", behavior = "in_class") from _call_send_Characters_336

            $ EventScheduler.Events["Laura_chapter_one_season_one_outcast"].completed = False
            $ EventScheduler.Events["Laura_chapter_one_season_one_outcast"].completed_when = 1e8

            $ EventScheduler.Events["Laura_chapter_one_season_one_outcast"].counter = 0

            $ ongoing_Event = False

            call move_location(Player.home) from _call_move_location_59

            return

    $ ongoing_Event = False

    return