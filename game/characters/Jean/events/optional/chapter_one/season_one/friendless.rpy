define ch_bully = Character("???")

init python:

    def Jean_chapter_one_season_one_friendless_setup():
        label = "Jean_chapter_one_season_one_friendless_setup"

        conditions = [
            "Jean.location != Player.location",

            "renpy.random.random() > 0.75",

            "not EventScheduler.Events['Jean_chapter_one_season_one_friendless'].completed",

            "time_index not in Jean.schedule.keys()",

            "chapter == 1 and season == 1",
            
            "time_index < 3",

            "Jean.is_in_normal_mood()"]

        repeatable = True
        automatic = True

        return EventClass(label, conditions, repeatable = repeatable, automatic = automatic)

label Jean_chapter_one_season_one_friendless_setup:
    call send_Characters(Jean, "bg_danger", behavior = "training") from _call_send_Characters_331
    
    return

init python:

    def Jean_chapter_one_season_one_friendless():
        label = "Jean_chapter_one_season_one_friendless"

        conditions = [
            "Player.destination == 'bg_danger'",

            "chapter == 1 and season == 1",

            "time_index < 3",
            
            "Jean.location == 'bg_danger'",
            "Jean.behavior == 'training'",

            "Jean.is_in_normal_mood()"]

        traveling = True

        markers = {
            "bg_danger": [
                "chapter == 1 and season == 1",

                "time_index < 3",
                
                "Jean.location == 'bg_danger'",
                "Jean.behavior == 'training'",
                
                "Jean.is_in_normal_mood()"]}

        return EventClass(label, conditions, traveling = traveling, markers = markers)

label Jean_chapter_one_season_one_friendless:
    $ ongoing_Event = True

    menu:
        extend ""
        "Go up to [Jean.name]":
            pass
        "Don't involve yourself":
            "You keep your distance and don't get involved."

            call remove_Characters(Jean) from _call_remove_Characters_327

            $ EventScheduler.Events["Jean_chapter_one_season_one_friendless"].completed = False
            $ EventScheduler.Events["Jean_chapter_one_season_one_friendless"].completed_when = 1e8

            $ EventScheduler.Events["Jean_chapter_one_season_one_friendless"].counter = 0

            $ ongoing_Event = False

            return

    $ ongoing_Event = False

    return