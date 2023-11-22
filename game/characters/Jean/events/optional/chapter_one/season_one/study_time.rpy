init python:

    def Jean_chapter_one_season_one_study_time_setup():
        label = "Jean_chapter_one_season_one_study_time_setup"

        conditions = [
            "Jean.location != Player.location",

            "renpy.random.random() > 0.75",

            "not EventScheduler.Events['Jean_chapter_one_season_one_study_time'].completed",

            "time_index not in Jean.schedule.keys()",

            "chapter == 1 and season == 1",

            "weekday < 5 and time_index >= 2",

            "not Jean.History.check('trained_with_Player', tracker = 'daily')",

            "Jean.is_in_normal_mood()"]

        repeatable = True
        automatic = True

        return EventClass(label, conditions, repeatable = repeatable, automatic = automatic)

label Jean_chapter_one_season_one_study_time_setup:
    call send_Characters(Jean, "bg_classroom", behavior = "studying") from _call_send_Characters_332
    
    return

init python:

    def Jean_chapter_one_season_one_study_time():
        label = "Jean_chapter_one_season_one_study_time"

        conditions = [
            "Player.destination == 'bg_classroom'",
            
            "chapter == 1 and season == 1",

            "weekday < 5 and time_index >= 2",
            
            "Jean.location == 'bg_classroom'",
            "Jean.behavior == 'studying'",

            "not Jean.History.check('trained_with_Player', tracker = 'daily')",

            "Jean.is_in_normal_mood()"]

        traveling = True

        markers = {
            "bg_classroom": [
                "chapter == 1 and season == 1",

                "weekday < 5 and time_index >= 2",
                
                "Jean.location == 'bg_classroom'",
                "Jean.behavior == 'studying'",

                "not Jean.History.check('trained_with_Player', tracker = 'daily')",

                "Jean.is_in_normal_mood()"]}

        return EventClass(label, conditions, traveling = traveling, markers = markers)

label Jean_chapter_one_season_one_study_time:
    $ ongoing_Event = True

    menu:
        extend ""
        "Knock on the door":
            pass
        "Grab your wallet and try not to disturb [Jean.name]":
            $ Jean.change_face("angry1", eyes = "down")

            "[Jean.name] frowns at her notes, looking like she's pleading with them to make sense."
            "She's so engrossed by what she's doing that you're able to quietly retrieve your wallet from a nearby desk without her even noticing."
            "You head out, leaving her be."

            $ EventScheduler.Events["Jean_chapter_one_season_one_study_time"].completed = False
            $ EventScheduler.Events["Jean_chapter_one_season_one_study_time"].completed_when = 1e8

            $ EventScheduler.Events["Jean_chapter_one_season_one_study_time"].counter = 0

            $ ongoing_Event = False

            call move_location("bg_hallway") from _call_move_location_55

            return

    $ ongoing_Event = False

    return