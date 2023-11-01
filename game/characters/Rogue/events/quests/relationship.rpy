init python:

    def Rogue_relationship_1_Quest():
        name = "Rogue: Relationship I"

        Quest_type = "side"

        chapter = 1

        description = "Grow your relationship with your favorite Southern belle goth"

        objectives = {
            "Gain Love": ["Rogue.love", 275],

            "Gain Trust": ["Rogue.trust", 275]}

        rewards = ["Seems kind of selfish to ask, doesn't it?"]

        criteria = [
            "EventScheduler.Events['Rogue_boyfriend'].completed"]

        return QuestClass(name, Quest_type, chapter, description, objectives, rewards, criteria)

    def Rogue_relationship_2_Quest():
        name = "Rogue: Relationship II"

        Quest_type = "side"

        chapter = 1

        description = "Grow your relationship with your favorite Southern belle goth"

        objectives = {
            "Gain Love": ["Rogue.love", 525],

            "Gain Trust": ["Rogue.trust", 525]}

        rewards = ["She really, really likes you, if you can't tell"]

        criteria = [
            "EventScheduler.Events['Rogue_enjoying_being_girlfriend'].completed"]

        return QuestClass(name, Quest_type, chapter, description, objectives, rewards, criteria)

    def Rogue_relationship_3_Quest():
        name = "Rogue: Relationship III"

        Quest_type = "side"

        chapter = 1

        description = "Grow your relationship with your favorite Southern belle goth"

        objectives = {
            "Gain Love": ["Rogue.love", 825],

            "Gain Trust": ["Rogue.trust", 825]}

        rewards = ["You two are looking awfully close - that's a reward, right?"]

        criteria = [
            "EventScheduler.Events['Rogue_penultimate_penultimate_quirk'].completed"]

        return QuestClass(name, Quest_type, chapter, description, objectives, rewards, criteria)