init python:

    def Jean_dating_Quest():
        name = "Jean Grey: Dating"

        Quest_type = "side"

        chapter = 1

        description = "Become more than friends with your favorite redhaired upperclassman"

        objectives = {
            "Go on a few dates": ["Jean.History.check('went_on_date_with_Player')", 3],

            "Gain Love": ["Jean.love", Jean_thresholds["relationship"][0]],

            "Gain Trust": ["Jean.trust", Jean_thresholds["relationship"][1]]}

        rewards = ["Seems like there are a lot of potential upsides here"]

        criteria = [
            "EventScheduler.Events['Jean_asked_on_date'].completed"]

        return QuestClass(name, Quest_type, chapter, description, objectives, rewards, criteria)