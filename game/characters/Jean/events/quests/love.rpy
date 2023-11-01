init python:

    def Jean_love_Quest():
        name = "Jean Grey: Love"

        Quest_type = "side"

        chapter = 1

        description = "Fall in love with your favorite redhaired upperclassman"

        objectives = {
            "Gain Love": ["Jean.love", Jean_thresholds["love"][0]],

            "Gain Trust": ["Jean.trust", Jean_thresholds["love"][1]]}

        rewards = ["Do you know the difference between love and obsession?"]

        criteria = [
            "EventScheduler.Events['Jean_first_sex_part_two'].completed"]

        return QuestClass(name, Quest_type, chapter, description, objectives, rewards, criteria)