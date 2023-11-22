init python:

    def Jean_chapter_one_season_one_exam_freakout_setup():
        label = "Jean_chapter_one_season_one_exam_freakout_setup"

        conditions = [
            "Jean.location != Player.location",

            "renpy.random.random() > 0.75",

            "not EventScheduler.Events['Jean_chapter_one_season_one_exam_freakout'].completed",

            "time_index not in Jean.schedule.keys()",

            "chapter == 1 and season == 1",

            "weekday < 5 and time_index < 2",
            "clock == Player.max_stamina",

            "Jean.is_in_normal_mood()"]

        repeatable = True
        automatic = True

        return EventClass(label, conditions, repeatable = repeatable, automatic = automatic)

label Jean_chapter_one_season_one_exam_freakout_setup:
    call send_Characters(Jean, "bg_classroom", behavior = "in_class") from _call_send_Characters_329
    
    return

init python:

    def Jean_chapter_one_season_one_exam_freakout():
        label = "Jean_chapter_one_season_one_exam_freakout"

        conditions = [
            "Player.destination == 'bg_classroom'",
            
            "chapter == 1 and season == 1",

            "weekday < 5 and time_index < 2",
            "clock == Player.max_stamina",
            
            "Jean.location == 'bg_classroom'",
            "Jean.behavior == 'in_class'",

            "Jean.is_in_normal_mood()"]

        traveling = True

        markers = {
            "bg_classroom": [
                "chapter == 1 and season == 1",

                "weekday < 5 and time_index < 2",
                "clock == Player.max_stamina",
                
                "Jean.location == 'bg_classroom'",
                "Jean.behavior == 'in_class'",

                "Jean.is_in_normal_mood()"]}

        return EventClass(label, conditions, traveling = traveling, markers = markers)

label Jean_chapter_one_season_one_exam_freakout:
    $ ongoing_Event = True

    menu:
        extend ""
        "Check on [Jean.name]":
            pass
        "Leave her to her thoughts":
            "You keep your distance."

            call send_Characters(Jean, "nearby", behavior = "in_class") from _call_send_Characters_330

            $ EventScheduler.Events["Jean_chapter_one_season_one_exam_freakout"].completed = False
            $ EventScheduler.Events["Jean_chapter_one_season_one_exam_freakout"].completed_when = 1e8

            $ EventScheduler.Events["Jean_chapter_one_season_one_exam_freakout"].counter = 0

            $ ongoing_Event = False

            return

    $ ongoing_Event = False

    return