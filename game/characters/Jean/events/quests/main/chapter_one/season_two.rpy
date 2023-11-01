init python:

    def Jean_ch1_season_two_Quest():
        global Jean

        name = f"{Jean.full_name}: Winter"

        string = "Jean_ch1_season_two_Quest"

        Quest_type = "main"

        chapter = 1

        description = "Get to know your favorite redhaired upperclassman"

        objectives = {}

        objectives.update({"Train together to learn more about your abilities": ["Jean.History.check('trained_with_Player', tracker = 'season')", 2]})
        
        objectives.update({"Study together to stay on top of your courses": ["Jean.History.check('studied_with_Player', tracker = 'season')", 1]})

        optional_objectives = {}

        rewards = ["Increased Love and Trust Cap"]

        criteria = [
            "chapter == 1",
            "season == 2"]

        return QuestClass(name, string, Quest_type, chapter, description, objectives, optional_objectives, rewards, criteria)