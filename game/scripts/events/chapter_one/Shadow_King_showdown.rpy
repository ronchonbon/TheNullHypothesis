init python:

    def ch1_season_four_main_Quest():
        name = "Chapter I: Summer"

        Quest_type = "main"

        chapter = 1

        description = "Explore your new home and get to know its students"

        objectives = {
            "Attend class": ["Player.History.check('attended_class', tracker = 'season')", 5],

            "Study with [Rogue.name]": ["Rogue.History.check('studied_with_Player', tracker = 'season')", 1],
            "Study with [Laura.name]": ["Laura.History.check('studied_with_Player', tracker = 'season')", 1],
            "Study with [Jean.name]": ["Jean.History.check('studied_with_Player', tracker = 'season')", 1],

            "Train with [Rogue.name]": ["Rogue.History.check('trained_with_Player', tracker = 'season')", 1],
            "Train with [Laura.name]": ["Laura.History.check('trained_with_Player', tracker = 'season')", 1],
            "Train with [Jean.name]": ["Jean.History.check('trained_with_Player', tracker = 'season')", 1],

            "Gain 1000 Trust across all characters": ["Rogue.trust + Laura.trust + Jean.trust", 1000]}

        rewards = [
            "Increased Level, Love, and Trust Caps",
            "New Available Actions",
            "New Shop Items"]

        criteria = [
            "chapter == 1",
            "season == 4"]

        return QuestClass(name, Quest_type, chapter, description, objectives, rewards, criteria)