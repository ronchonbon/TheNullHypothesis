init python:

    def Jean_ch1_season_one_Quest():
        name = f"{Jean.full_name}: Fall"

        string = "Jean_ch1_season_one_Quest"

        Quest_type = "main"

        chapter = 1

        description = "Get to know your favorite redhaired upperclassman"

        objectives = {}

        objectives.update({"Bump into each other while exploring the mansion": ["EventScheduler.Events['Jean_leaving_for_mission'].completed", None]})

        if EventScheduler.Events["Jean_leaving_for_mission"].completed:
            objectives.update({"Wait for her to return from her mission": ["EventScheduler.Events['Jean_back_from_mission'].completed", None]})

        if EventScheduler.Events["Jean_back_from_mission"].completed:
            objectives.update({"Train together to learn more about your abilities": ["Jean.History.check('trained_with_Player', tracker = 'season')", 4]})
            
            objectives.update({"Study together to catch up on your courses": ["Jean.History.check('studied_with_Player', tracker = 'season')", 1]})

        optional_objectives = {}

        if EventScheduler.Events["Jean_back_from_mission"].completed:
            optional_objectives.update({"Check in on her late night study session": ["EventScheduler.Events['Jean_chapter_one_season_one_study_time'].completed", None]})

            optional_objectives.update({"Help her unwind after her exam": ["EventScheduler.Events['Jean_chapter_one_season_one_exam_freakout'].completed", None]})

            optional_objectives.update({"Talk to her about her friends": ["EventScheduler.Events['Jean_chapter_one_season_one_friendless'].completed", None]})

        rewards = {
            "unlock": ["love", "trust"]}
        criteria = [
            "chapter == 1 and season == 1"]

        return QuestClass(name, string, Quest_type, chapter, description, objectives, optional_objectives, rewards, criteria)