init python:

    def Laura_ch1_season_four_Quest():
        global Laura

        name = f"{Laura.full_name}: Summer"

        string = "Laura_ch1_season_four_Quest"

        Quest_type = "main"

        chapter = 1

        description = "Get to know your favorite lab-grown weapon"

        objectives = {}

        objectives.update({"Train together to learn more about your abilities": ["Laura.History.check('trained_with_Player', tracker = 'season')", 1]})
        
        objectives.update({"Study together to help her with her coursework": ["Laura.History.check('studied_with_Player', tracker = 'season')", 1]})

        optional_objectives = {}

        rewards = ["Increased Love and Trust Cap"]

        criteria = [
            "chapter == 1 and season == 4"]

        return QuestClass(name, string, Quest_type, chapter, description, objectives, optional_objectives, rewards, criteria)