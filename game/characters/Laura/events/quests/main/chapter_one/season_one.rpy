init python:

    def Laura_ch1_season_one_Quest():
        name = f"{Laura.full_name}: Fall"

        string = "Laura_ch1_season_one_Quest"

        Quest_type = "main"

        chapter = 1

        description = "Get to know your favorite lab-grown weapon"

        objectives = {}

        objectives.update({"Train together to develop your combat abilities": ["Laura.History.check('trained_with_Player', tracker = 'season')", 4]})
        
        objectives.update({"Study together to help her with her coursework": ["Laura.History.check('studied_with_Player', tracker = 'season')", 1]})

        if Laura.History.check("trained_with_Player", tracker = "season") >= 4:
            if QuestPool.Quests['Laura_friendship_Quest'].completed:
                objectives.update({"Become her first friend": ["EventScheduler.Events['Laura_first_friend_part_one'].completed", None]})
            else:
                objectives.update({"Become friends": ["QuestPool.Quests['Laura_friendship_Quest'].completed", None]})

            if EventScheduler.Events["Laura_first_friend_part_one"].completed:
                objectives.update({"Talk to her about the nature of friendship": ["EventScheduler.Events['Laura_first_friend_part_two'].completed", None]})

        optional_objectives = {}

        optional_objectives.update({"Ask her why she looks on edge": ["EventScheduler.Events['Laura_chapter_one_season_one_on_edge'].completed", None]})

        optional_objectives.update({"Run into her training late at night": ["EventScheduler.Events['Laura_chapter_one_season_one_late_night_training'].completed", None]})

        optional_objectives.update({"Sit next to her in class": ["EventScheduler.Events['Laura_chapter_one_season_one_outcast'].completed", None]})

        rewards = {}
        criteria = [
            "chapter == 1 and season == 1"]

        return QuestClass(name, string, Quest_type, chapter, description, objectives, optional_objectives, rewards, criteria)