init python:

    def Laura_relationship_1_Quest():
        name = f"{Laura.full_name}: Relationship I"

        string = "Laura_relationship_1_Quest"

        Quest_type = "side"

        chapter = 1

        description = "Grow your relationship with your favorite lab-grown weapon"

        objectives = {
            "Gain Love": ["Laura.love", 275],

            "Gain Trust": ["Laura.trust", 300]}

        optional_objectives = {}

        rewards = ["Probably best to focus on not irrevocably pissing her off"]

        criteria = [
            "EventScheduler.Events['Laura_boyfriend'].completed"]

        return QuestClass(name, string, Quest_type, chapter, description, objectives, optional_objectives, rewards, criteria)

    def Laura_relationship_2_Quest():
        name = f"{Laura.full_name}: Relationship II"

        string = "Laura_relationship_2_Quest"

        Quest_type = "side"

        chapter = 1

        description = "Grow your relationship with your favorite lab-grown weapon"

        objectives = {
            "Gain Love": ["Laura.love", 550],

            "Gain Trust": ["Laura.trust", 600]}

        optional_objectives = {}

        rewards = ["Be a good boyfriend or else"]

        criteria = [
            "EventScheduler.Events['Laura_enjoying_being_girlfriend'].completed"]

        return QuestClass(name, string, Quest_type, chapter, description, objectives, optional_objectives, rewards, criteria)

    def Laura_relationship_3_Quest():
        name = f"{Laura.full_name}: Relationship III"

        string = "Laura_relationship_3_Quest"

        Quest_type = "side"

        chapter = 1

        description = "Grow your relationship with your favorite lab-grown weapon"

        objectives = {
            "Gain Love": ["Laura.love", Laura_thresholds["sex"][0]],

            "Gain Trust": ["Laura.trust", Laura_thresholds["sex"][1]]}

        optional_objectives = {}

        rewards = ["Not everything is about rewards. . . but yes, you will be rewarded"]

        criteria = [
            "EventScheduler.Events['Laura_I_love_you'].completed"]

        return QuestClass(name, string, Quest_type, chapter, description, objectives, optional_objectives, rewards, criteria)