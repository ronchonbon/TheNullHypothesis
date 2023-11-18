init python:

    def Jean_ch1_season_three_Quest():
        global Jean

        name = f"{Jean.full_name}: Spring"

        string = "Jean_ch1_season_three_Quest"

        Quest_type = "main"

        chapter = 1

        description = "Get to know your favorite redhaired upperclassman"

        objectives = {}

        objectives.update({"Train together to learn more about your abilities": ["Jean.History.check('trained_with_Player', tracker = 'season')", 2]})
        
        optional_objectives = {}

        rewards = ["Increased Love and Trust Cap"]

        criteria = [
            "chapter == 1 and season == 3"]

        return QuestClass(name, string, Quest_type, chapter, description, objectives, optional_objectives, rewards, criteria)