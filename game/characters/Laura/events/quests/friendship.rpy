init python:

    def Laura_friendship_Quest():
        name = "Laura Kinney: Friendship"

        Quest_type = "side"

        chapter = 1

        description = "Befriend your favorite lab-grown weapon"

        objectives = {
            "Train together": ["Laura.History.check('trained_with_Player')", 4],

            "Gain Love": ["Laura.love", Laura_thresholds["dating"][0]],

            "Gain Trust": ["Laura.trust", Laura_thresholds["dating"][1]]}

        rewards = ["Is friendship not a reward unto itself?"]

        criteria = [
            "chapter == 1",
            "season == 1"]

        return QuestClass(name, Quest_type, chapter, description, objectives, rewards, criteria)