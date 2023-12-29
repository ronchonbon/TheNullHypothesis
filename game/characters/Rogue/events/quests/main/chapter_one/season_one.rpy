init python:

    def Rogue_ch1_season_one_Quest():
        name = f"{Rogue.name}: Fall"

        string = "Rogue_ch1_season_one_Quest"

        Quest_type = "main"

        chapter = 1

        description = "Get to know your favorite Southern belle goth"

        objectives = {}

        objectives.update({"Train together to learn more about your abilities": ["Rogue.History.check('trained_with_Player', tracker = 'season')", 1]})
        
        objectives.update({"Study together to catch up on your courses": ["Rogue.History.check('studied_with_Player', tracker = 'season')", 2]})

        optional_objectives = {}

        optional_objectives.update({"Make plans to go jogging together": ["EventScheduler.Events['Rogue_chapter_one_season_one_jogging'].completed", None]})

        optional_objectives.update({"Hang out together on the front lawn": ["EventScheduler.Events['Rogue_chapter_one_season_one_people_watching'].completed", None]})

        if day > 5:
            optional_objectives.update({"Bump into each other in the hallway": ["EventScheduler.Events['Rogue_chapter_one_season_one_standoffish_part_one'].completed", None]})

        if EventScheduler.Events["Rogue_chapter_one_season_one_standoffish_part_one"].completed:
            optional_objectives.update({"Bump into each other in the classroom": ["EventScheduler.Events['Rogue_chapter_one_season_one_standoffish_part_two'].completed", None]})

        rewards = {
            "unlock": ["love", "trust"]}
        criteria = [
            "chapter == 1 and season == 1"]

        return QuestClass(name, string, Quest_type, chapter, description, objectives, optional_objectives, rewards, criteria)