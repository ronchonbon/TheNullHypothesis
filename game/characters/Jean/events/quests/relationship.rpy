init python:

    def Jean_relationship_1_Quest():
        name = "Jean Grey: Relationship I"

        Quest_type = "side"

        chapter = 1

        description = "Grow your relationship with your favorite redhaired upperclassman"

        objectives = {
            "Gain Love": ["Jean.love", 300],

            "Gain Trust": ["Jean.trust", 275]}

        rewards = ["Think too much about rewards and you won't enjoy the little things"]

        criteria = [
            "EventScheduler.Events['Jean_boyfriend'].completed"]

        return QuestClass(name, Quest_type, chapter, description, objectives, rewards, criteria)

    def Jean_relationship_2_Quest():
        name = "Jean Grey: Relationship II"

        Quest_type = "side"

        chapter = 1

        description = "Grow your relationship with your favorite redhaired upperclassman"

        objectives = {
            "Gain Love": ["Jean.love", 600],

            "Gain Trust": ["Jean.trust", 550]}

        rewards = ["Strong relationships are built on clear and effective communication"]

        criteria = [
            "EventScheduler.Events['Jean_enjoying_being_girlfriend'].completed"]

        return QuestClass(name, Quest_type, chapter, description, objectives, rewards, criteria)

    def Jean_relationship_3_Quest():
        name = "Jean Grey: Relationship III"

        Quest_type = "side"

        chapter = 1

        description = "Grow your relationship with your favorite redhaired upperclassman"

        objectives = {
            "Gain Love": ["Jean.love", Jean_thresholds["sex"][0]],

            "Gain Trust": ["Jean.trust", Jean_thresholds["sex"][1]]}

        rewards = ["It's always about rewards with you - what about romance?"]

        criteria = [
            "EventScheduler.Events['Jean_penultimate_quirk'].completed"]

        return QuestClass(name, Quest_type, chapter, description, objectives, rewards, criteria)