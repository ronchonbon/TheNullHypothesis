init -1:

    default QuestPool = QuestPoolClass()

init -2 python:

    class QuestClass(object):
        def __init__(self, name, Quest_type, chapter, description, objectives, rewards, criteria, **kwargs):
            self.name = name

            self.Quest_type = Quest_type

            self.chapter = chapter

            self.description = description

            self.objectives = objectives

            self.rewards = rewards

            self.criteria = criteria

            self.resets = kwargs.get("resets", False)

            self.unlocked = False
            self.completed = False

        def check_unlocked(self):
            self.unlocked = True

            for criterion in self.criteria:
                if not eval(criterion):
                    self.unlocked = False

                    break

            return

        def check_completion(self):
            self.completed = True

            for objective, target in self.objectives.values():
                if target is None:
                    if not eval(objective):
                        self.completed = False

                        break
                else:
                    if eval(objective) < target:
                        self.completed = False

                        break

            return

    class QuestPoolClass(object):
        def __init__(self):
            self.Quests = {}

        def add_Quest(self, Quest):
            if Quest.name not in self.Quests.keys():
                self.Quests[Quest.name] = Quest
            else:
                Quest.unlocked = self.Quests[Quest.name].unlocked
                Quest.completed = self.Quests[Quest.name].completed

                self.Quests[Quest.name] = Quest

            return

        def check_progress(self):
            global journal_alert
            
            for Quest in self.Quests.values():
                if not Quest.unlocked:
                    Quest.check_unlocked()

                    if Quest.unlocked:
                        journal_alert = True

                if Quest.unlocked and not Quest.completed:
                    Quest.check_completion()

                    if Quest.completed:
                        journal_alert = True

                if Quest.unlocked and Quest.resets:
                    Quest.check_completion()

            return

        def check_Quests(self):
            for Quest in self.Quests.values():
                for criterion in Quest.criteria:
                    try:
                        eval(criterion)
                    except:
                        print(criterion)

                for objective, target in Quest.objectives.values():
                    try:
                        eval(objective)
                    except:
                        print(objective)

            return