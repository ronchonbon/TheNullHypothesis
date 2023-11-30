init python:

    def Rogue_ch1_season_four_Quest():
        name = f"{Rogue.name}: Summer"

        string = "Rogue_ch1_season_four_Quest"

        Quest_type = "main"

        chapter = 1

        description = "Get to know your favorite Southern belle goth"

        objectives = {}

        objectives.update({"Train together to learn more about your abilities": ["Rogue.History.check('trained_with_Player', tracker = 'season')", 1]})
        
        objectives.update({"Study together to stay on top of your courses": ["Rogue.History.check('studied_with_Player', tracker = 'season')", 1]})

        optional_objectives = {}

        rewards = ["Increased Love and Trust Cap"]

        criteria = [
            "chapter == 1 and season == 4"]

        return QuestClass(name, string, Quest_type, chapter, description, objectives, optional_objectives, rewards, criteria)