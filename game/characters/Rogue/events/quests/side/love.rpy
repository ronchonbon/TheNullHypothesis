init python:

    def Rogue_love_Quest():
        name = f"{Rogue.name}: Love"

        string = "Rogue_love_Quest"

        Quest_type = "side"

        chapter = 1

        description = "Fall in love with your favorite Southern belle goth"

        objectives = {
            "Gain Love": ["Rogue.love", Rogue_thresholds["love"][0]],

            "Gain Trust": ["Rogue.trust", Rogue_thresholds["love"][1]]}

        optional_objectives = {}

        rewards = {}

        criteria = [
            "EventScheduler.Events['Rogue_penultimate_quirk'].completed"]

        return QuestClass(name, string, Quest_type, chapter, description, objectives, optional_objectives, rewards, criteria)