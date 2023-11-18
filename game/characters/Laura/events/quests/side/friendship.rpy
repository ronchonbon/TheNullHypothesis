init python:

    def Laura_friendship_Quest():
        name = f"{Laura.full_name}: Friendship"

        string = "Laura_friendship_Quest"

        Quest_type = "side"

        chapter = 1

        description = "Befriend your favorite lab-grown weapon"

        objectives = {
            "Gain Love": ["Laura.love", Laura_thresholds["dating"][0]],

            "Gain Trust": ["Laura.trust", Laura_thresholds["dating"][1]]}

        optional_objectives = {}

        rewards = ["Is friendship not a reward unto itself?"]

        criteria = [
            "chapter == 1 and season == 1"]

        return QuestClass(name, string, Quest_type, chapter, description, objectives, optional_objectives, rewards, criteria)