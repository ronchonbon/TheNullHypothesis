init python:

    def Rogue_dating_Quest():
        name = f"{Rogue.name}: Dating"

        string = "Rogue_dating_Quest"

        Quest_type = "side"

        chapter = 1

        description = "Become more than friends with your favorite Southern belle goth"

        objectives = {
            "Go on a few dates": ["Rogue.History.check('went_on_date_with_Player')", 3],

            "Gain Love": ["Rogue.love", Rogue_thresholds["relationship"][0]],

            "Gain Trust": ["Rogue.trust", Rogue_thresholds["relationship"][1]]}

        optional_objectives = {}

        rewards = {}

        criteria = [
            "EventScheduler.Events['Rogue_confession'].completed",
            "not Rogue.check_traits('platonic')"]

        return QuestClass(name, string, Quest_type, chapter, description, objectives, optional_objectives, rewards, criteria)