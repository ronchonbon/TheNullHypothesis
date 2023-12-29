init python:

    def Jean_friendship_Quest():
        name = f"{Jean.full_name}: Friendship"

        string = "Jean_friendship_Quest"

        Quest_type = "side"

        chapter = 1

        description = "Befriend your favorite redhaired upperclassman"

        objectives = {
            "Gain Love": ["Jean.love", Jean_thresholds["dating"][0]],

            "Gain Trust": ["Jean.trust", Jean_thresholds["dating"][1]]}

        optional_objectives = {}

        rewards = {}

        criteria = [
            "chapter == 1 and season == 1"]

        return QuestClass(name, string, Quest_type, chapter, description, objectives, optional_objectives, rewards, criteria)