init python:

    def Rogue_love_Quest():
        name = "Rogue: Love"

        Quest_type = "side"

        chapter = 1

        description = "Fall in love with your favorite Southern belle goth"

        objectives = {
            "Gain Love": ["Rogue.love", Rogue_thresholds["love"][0]],

            "Gain Trust": ["Rogue.trust", Rogue_thresholds["love"][1]]}

        rewards = ["The real question is: do you really deserve a reward?"]

        criteria = [
            "EventScheduler.Events['Rogue_penultimate_quirk'].completed"]

        return QuestClass(name, Quest_type, chapter, description, objectives, rewards, criteria)