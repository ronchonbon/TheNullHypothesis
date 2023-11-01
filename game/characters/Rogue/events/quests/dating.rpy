init python:

    def Rogue_dating_Quest():
        name = "Rogue: Dating"

        Quest_type = "side"

        chapter = 1

        description = "Become more than friends with your favorite Southern belle goth"

        objectives = {
            "Go on a few dates": ["Rogue.History.check('went_on_date_with_Player')", 3],

            "Gain Love": ["Rogue.love", Rogue_thresholds["relationship"][0]],

            "Gain Trust": ["Rogue.trust", Rogue_thresholds["relationship"][1]]}

        rewards = ["You'll never know if you don't go for it"]

        criteria = [
            "EventScheduler.Events['Rogue_confession'].completed"]

        return QuestClass(name, Quest_type, chapter, description, objectives, rewards, criteria)