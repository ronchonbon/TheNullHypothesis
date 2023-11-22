init python:

    def Laura_chapter_one_season_one_late_night_training_setup():
        label = "Laura_chapter_one_season_one_late_night_training_setup"

        conditions = [
            "Laura.location != Player.location",

            "renpy.random.random() > 0.75",

            "not EventScheduler.Events['Laura_chapter_one_season_one_late_night_training'].completed",

            "time_index not in Laura.schedule.keys()",

            "chapter == 1 and season == 1",

            "time_index >= 3",

            "Laura.is_in_normal_mood()"]

        repeatable = True
        automatic = True

        return EventClass(label, conditions, repeatable = repeatable, automatic = automatic)

label Laura_chapter_one_season_one_late_night_training_setup:
    call send_Characters(Laura, "bg_danger", behavior = "training") from _call_send_Characters_333
    
    return

init python:

    def Laura_chapter_one_season_one_late_night_training():
        label = "Laura_chapter_one_season_one_late_night_training"

        conditions = [
            "Player.destination == 'bg_danger'",

            "chapter == 1 and season == 1",

            "time_index >= 3",
            
            "Laura.location == 'bg_danger'",
            "Laura.behavior == 'training'",

            "Laura.is_in_normal_mood()"]

        traveling = True

        markers = {
            "bg_danger": [
                "chapter == 1 and season == 1",

                "time_index >= 3",
                
                "Laura.location == 'bg_danger'",
                "Laura.behavior == 'training'",

                "Laura.is_in_normal_mood()"]}

        return EventClass(label, conditions, traveling = traveling, markers = markers)

label Laura_chapter_one_season_one_late_night_training:
    $ ongoing_Event = True

    menu:
        extend ""
        "Watch for a bit":
            pass
        "Don't disturb her training":
            "Looks like the Danger Room is off the table while [Laura.name]'s using it."
            "The regular training rooms should still be free, maybe a few minutes on the treadmill will help. . ."

            $ EventScheduler.Events["Laura_chapter_one_season_one_late_night_training"].completed = False
            $ EventScheduler.Events["Laura_chapter_one_season_one_late_night_training"].completed_when = 1e8

            $ EventScheduler.Events["Laura_chapter_one_season_one_late_night_training"].counter = 0

            $ ongoing_Event = False

            call move_location(Player.home) from _call_move_location_58

            return

    $ ongoing_Event = False

    return