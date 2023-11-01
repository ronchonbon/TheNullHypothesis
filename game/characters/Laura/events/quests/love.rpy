init python:

    def Laura_love_Quest():
        name = "Laura Kinney: Love"

        Quest_type = "side"

        chapter = 1

        description = "Fall in love with your favorite lab-grown weapon"

        objectives = {
            "Gain Love": ["Laura.love", Laura_thresholds["love"][0]],

            "Gain Trust": ["Laura.trust", Laura_thresholds["love"][1]]}

        rewards = ["She really seems to like you - better not mess it up"]

        criteria = [
            "EventScheduler.Events['Laura_penultimate_quirk'].completed"]

        return QuestClass(name, Quest_type, chapter, description, objectives, rewards, criteria)