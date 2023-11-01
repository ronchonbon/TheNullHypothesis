init python:

    def Laura_love_Quest():
        name = f"{Laura.full_name}: Love"

        string = "Laura_love_Quest"

        Quest_type = "side"

        chapter = 1

        description = "Fall in love with your favorite lab-grown weapon"

        objectives = {
            "Gain Love": ["Laura.love", Laura_thresholds["love"][0]],

            "Gain Trust": ["Laura.trust", Laura_thresholds["love"][1]]}

        optional_objectives = {}

        rewards = ["She really seems to like you - better not mess it up"]

        criteria = [
            "EventScheduler.Events['Laura_penultimate_quirk'].completed"]

        return QuestClass(name, string, Quest_type, chapter, description, objectives, optional_objectives, rewards, criteria)