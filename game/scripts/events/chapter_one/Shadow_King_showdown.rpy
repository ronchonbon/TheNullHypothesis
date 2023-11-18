init python:

    def ch1_season_four_main_Quest():
        name = "Chapter I: Summer"

        string = "ch1_season_four_main_Quest"

        Quest_type = "main"

        chapter = 1

        description = "Explore your new home and get to know its students"

        objectives = {
            "Increase your level": ["Player.level", 5],

            "Complete [Rogue.name]'s Summer Quest": ["QuestPool.Quests['Rogue_ch1_season_four_Quest'].completed", None],
            "Complete [Laura.name]'s Summer Quest": ["QuestPool.Quests['Laura_ch1_season_four_Quest'].completed", None],
            "Complete [Jean.name]'s Summer Quest": ["QuestPool.Quests['Jean_ch1_season_four_Quest'].completed", None],

            "Gain Trust across all characters": ["Rogue.trust + Laura.trust + Jean.trust", 1500]}

        optional_objectives = {}

        rewards = [
            "New Available Actions",
            "New Shop Items"]

        criteria = [
            "chapter == 1 and season == 4"]

        return QuestClass(name, string, Quest_type, chapter, description, objectives, optional_objectives, rewards, criteria)