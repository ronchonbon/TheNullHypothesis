init python:

    def attend_class_weekly():
        name = "Attend Class Weekly"

        string = "attend_class_weekly"

        Quest_type = "side"

        chapter = 1

        description = "Attend class every week so you don't fall behind on your studies"

        objectives = {
            "Attend class this week": ["Player.History.check('attended_class', tracker = 'weekly')", 3]}

        optional_objectives = {}

        rewards = ["+10% on Love, Trust, and XP Gains for the Following Week"]

        criteria = [
            "chapter == 1 and season == 1"]

        resets = True

        return QuestClass(name, string, Quest_type, chapter, description, objectives, optional_objectives, rewards, criteria, resets = resets)