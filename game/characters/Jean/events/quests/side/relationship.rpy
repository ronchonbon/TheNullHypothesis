init python:

    def Jean_relationship_1_Quest():
        name = f"{Jean.full_name}: Relationship I"

        string = "Jean_relationship_1_Quest"

        Quest_type = "side"

        chapter = 1

        description = "Grow your relationship with your favorite redhaired upperclassman"

        objectives = {
            "Gain Love": ["Jean.love", 300],

            "Gain Trust": ["Jean.trust", 275]}

        optional_objectives = {}

        rewards = {}

        criteria = [
            "EventScheduler.Events['Jean_boyfriend'].completed"]

        return QuestClass(name, string, Quest_type, chapter, description, objectives, optional_objectives, rewards, criteria)

    def Jean_relationship_2_Quest():
        name = f"{Jean.full_name}: Relationship II"

        string = "Jean_relationship_2_Quest"

        Quest_type = "side"

        chapter = 1

        description = "Grow your relationship with your favorite redhaired upperclassman"

        objectives = {
            "Gain Love": ["Jean.love", 600],

            "Gain Trust": ["Jean.trust", 550]}

        optional_objectives = {}

        rewards = {}

        criteria = [
            "EventScheduler.Events['Jean_enjoying_being_girlfriend'].completed"]

        return QuestClass(name, string, Quest_type, chapter, description, objectives, optional_objectives, rewards, criteria)

    def Jean_relationship_3_Quest():
        name = f"{Jean.full_name}: Relationship III"

        string = "Jean_relationship_3_Quest"

        Quest_type = "side"

        chapter = 1

        description = "Grow your relationship with your favorite redhaired upperclassman"

        objectives = {
            "Gain Love": ["Jean.love", Jean_thresholds["sex"][0]],

            "Gain Trust": ["Jean.trust", Jean_thresholds["sex"][1]]}

        optional_objectives = {}

        rewards = {}

        criteria = [
            "EventScheduler.Events['Jean_penultimate_quirk'].completed"]

        return QuestClass(name, string, Quest_type, chapter, description, objectives, optional_objectives, rewards, criteria)