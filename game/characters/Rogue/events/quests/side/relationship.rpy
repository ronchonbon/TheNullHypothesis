init python:

    def Rogue_relationship_1_Quest():
        name = f"{Rogue.name}: Relationship I"

        string = "Rogue_relationship_1_Quest"

        Quest_type = "side"

        chapter = 1

        description = "Grow your relationship with your favorite Southern belle goth"

        objectives = {
            "Gain Love": ["Rogue.love", 275],

            "Gain Trust": ["Rogue.trust", 275]}

        optional_objectives = {}

        rewards = {}

        criteria = [
            "EventScheduler.Events['Rogue_boyfriend'].completed"]

        return QuestClass(name, string, Quest_type, chapter, description, objectives, optional_objectives, rewards, criteria)

    def Rogue_relationship_2_Quest():
        name = f"{Rogue.name}: Relationship II"

        string = "Rogue_relationship_2_Quest"

        Quest_type = "side"

        chapter = 1

        description = "Grow your relationship with your favorite Southern belle goth"

        objectives = {
            "Gain Love": ["Rogue.love", 525],

            "Gain Trust": ["Rogue.trust", 525]}

        optional_objectives = {}

        rewards = {}

        criteria = [
            "EventScheduler.Events['Rogue_enjoying_being_girlfriend'].completed"]

        return QuestClass(name, string, Quest_type, chapter, description, objectives, optional_objectives, rewards, criteria)

    def Rogue_relationship_3_Quest():
        name = f"{Rogue.name}: Relationship III"

        string = "Rogue_relationship_3_Quest"

        Quest_type = "side"

        chapter = 1

        description = "Grow your relationship with your favorite Southern belle goth"

        objectives = {
            "Gain Love": ["Rogue.love", 825],

            "Gain Trust": ["Rogue.trust", 825]}

        optional_objectives = {}

        rewards = {}

        criteria = [
            "EventScheduler.Events['Rogue_penultimate_penultimate_quirk'].completed"]

        return QuestClass(name, string, Quest_type, chapter, description, objectives, optional_objectives, rewards, criteria)