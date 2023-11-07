init python:

    def Jean_friendship_Quest():
        name = "Jean Grey: Friendship"

        Quest_type = "side"

        chapter = 1

        description = "Befriend your favorite redhaired upperclassman"

        objectives = {
            "Gain Love": ["Jean.love", Jean_thresholds["dating"][0]],

            "Gain Trust": ["Jean.trust", Jean_thresholds["dating"][1]]}

        rewards = ["What can any of us amount to without friendship?"]

        criteria = [
            "chapter == 1",
            "season == 1"]

        return QuestClass(name, Quest_type, chapter, description, objectives, rewards, criteria)