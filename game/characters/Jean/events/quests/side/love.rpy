init python:

    def Jean_love_Quest():
        name = f"{Jean.full_name}: Love"

        string = "Jean_love_Quest"

        Quest_type = "side"

        chapter = 1

        description = "Fall in love with your favorite redhaired upperclassman"

        objectives = {
            "Gain Love": ["Jean.love", Jean_thresholds["love"][0]],

            "Gain Trust": ["Jean.trust", Jean_thresholds["love"][1]]}

        optional_objectives = {}

        rewards = {}

        criteria = [
            "EventScheduler.Events['Jean_first_sex_part_two'].completed"]

        return QuestClass(name, string, Quest_type, chapter, description, objectives, optional_objectives, rewards, criteria)