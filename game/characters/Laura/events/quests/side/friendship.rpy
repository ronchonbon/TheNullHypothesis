init python:

    def Laura_friendship_Quest():
        name = f"{Laura.full_name}: Friendship"

        string = "Laura_friendship_Quest"

        Quest_type = "side"

        chapter = 1

        description = "Befriend your favorite lab-grown weapon"

        objectives = {
            "Gain Love": ["Laura.love", Laura_thresholds["dating"][0]],

            "Gain Trust": ["Laura.trust", Laura_thresholds["dating"][1]],
            
            "Sit next to her in class": ["EventScheduler.Events['Laura_chapter_one_season_one_outcast'].completed", None],

            "Run into her training late at night": ["EventScheduler.Events['Laura_chapter_one_season_one_late_night_training'].completed", None]}

        optional_objectives = {}

        rewards = {}

        criteria = [
            "chapter == 1 and season == 1"]

        return QuestClass(name, string, Quest_type, chapter, description, objectives, optional_objectives, rewards, criteria)