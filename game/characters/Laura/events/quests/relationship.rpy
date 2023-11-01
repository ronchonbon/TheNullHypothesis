init python:

    def Laura_relationship_1_Quest():
        name = "Laura Kinney: Relationship I"

        Quest_type = "side"

        chapter = 1

        description = "Grow your relationship with your favorite lab-grown weapon"

        objectives = {
            "Gain Love": ["Laura.love", 275],

            "Gain Trust": ["Laura.trust", 300]}

        rewards = ["Probably best to focus on not irrevocably pissing her off"]

        criteria = [
            "EventScheduler.Events['Laura_boyfriend'].completed"]

        return QuestClass(name, Quest_type, chapter, description, objectives, rewards, criteria)

    def Laura_relationship_2_Quest():
        name = "Laura Kinney: Relationship II"

        Quest_type = "side"

        chapter = 1

        description = "Grow your relationship with your favorite lab-grown weapon"

        objectives = {
            "Gain Love": ["Laura.love", 550],

            "Gain Trust": ["Laura.trust", 600]}

        rewards = ["Be a good boyfriend or else"]

        criteria = [
            "EventScheduler.Events['Laura_enjoying_being_girlfriend'].completed"]

        return QuestClass(name, Quest_type, chapter, description, objectives, rewards, criteria)

    def Laura_relationship_3_Quest():
        name = "Laura Kinney: Relationship III"

        Quest_type = "side"

        chapter = 1

        description = "Grow your relationship with your favorite lab-grown weapon"

        objectives = {
            "Gain Love": ["Laura.love", Laura_thresholds["sex"][0]],

            "Gain Trust": ["Laura.trust", Laura_thresholds["sex"][1]]}

        rewards = ["Not everything is about rewards. . . but yes, you will be rewarded"]

        criteria = [
            "EventScheduler.Events['Laura_I_love_you'].completed"]

        return QuestClass(name, Quest_type, chapter, description, objectives, rewards, criteria)