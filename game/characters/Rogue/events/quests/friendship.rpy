init python:

    def Rogue_friendship_Quest():
        name = "Rogue: Friendship"

        Quest_type = "side"

        chapter = 1

        description = "Befriend your favorite Southern belle goth"

        objectives = {
            "Gain Love": ["Rogue.love", Rogue_thresholds["dating"][0]],

            "Gain Trust": ["Rogue.trust", Rogue_thresholds["dating"][1]]}

        rewards = ["The friends we make along the way"]

        criteria = [
            "chapter == 1",
            "season == 1"]

        return QuestClass(name, Quest_type, chapter, description, objectives, rewards, criteria)