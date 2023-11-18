init python:

    def Laura_ch1_season_one_Quest():
        global Laura

        global QuestPool

        global EventScheduler

        name = f"{Laura.full_name}: Fall"

        string = "Laura_ch1_season_one_Quest"

        Quest_type = "main"

        chapter = 1

        description = "Get to know your favorite lab-grown weapon"

        objectives = {}

        objectives.update({"Train together to develop your combat abilities": ["Laura.History.check('trained_with_Player', tracker = 'season')", 4]})
        
        objectives.update({"Study together to help her with her coursework": ["Laura.History.check('studied_with_Player', tracker = 'season')", 1]})

        if Laura.History.check("trained_with_Player", tracker = "season") == 4:
            objectives.update({"Become friends": ["QuestPool.Quests['Laura_friendship_Quest'].completed", None]})

            if QuestPool.Quests['Laura_friendship_Quest'].completed:
                objectives.update({"Become her first friend": ["EventScheduler.Events['Laura_first_friend_part_one'].completed", None]})

            if EventScheduler.Events["Laura_first_friend_part_one"].completed:
                objectives.update({"Talk to her about the nature of friendship": ["EventScheduler.Events['Laura_first_friend_part_two'].completed", None]})

        optional_objectives = {}

        rewards = ["Increased Love and Trust Cap"]

        criteria = [
            "chapter == 1 and season == 1"]

        return QuestClass(name, string, Quest_type, chapter, description, objectives, optional_objectives, rewards, criteria)