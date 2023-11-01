init python:

    def Laura_dating_Quest():
        name = f"{Laura.full_name}: Dating"

        string = "Laura_dating_Quest"

        Quest_type = "side"

        chapter = 1

        description = "Become more than friends with your favorite lab-grown weapon"

        objectives = {
            "Go on a few dates": ["Laura.History.check('went_on_date_with_Player')", 3],

            "Gain Love": ["Laura.love", Laura_thresholds["relationship"][0]],

            "Gain Trust": ["Laura.trust", Laura_thresholds["relationship"][1]]}

        optional_objectives = {}

        rewards = ["It's likely there are perks to being on her good side"]

        criteria = [
            "EventScheduler.Events['Laura_first_friend_part_three'].completed"]

        return QuestClass(name, string, Quest_type, chapter, description, objectives, optional_objectives, rewards, criteria)