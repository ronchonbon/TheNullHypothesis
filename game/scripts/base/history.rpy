init -3 python:

    import copy

    class HistoryItemClass(object):
        def __init__(self):
            self.completed = []

    class HistoryClass(object):
        def __init__(self):
            self.event = {}

            self.recent = {}

            self.last = {}

            self.daily = {}

            self.weekly = {}

            self.season = {}

            self.persistent = {}

            self.permanent = {}

        def initialize(self, Item):
            for tracker in [self.event, self.recent, self.daily, self.weekly, self.season, self.persistent, self.permanent]:
                if Item not in tracker.keys():
                    tracker.update({Item: HistoryItemClass()})

        def update(self, Item):
            global EventScheduler

            for tracker in [self.event, self.recent, self.daily, self.weekly, self.season, self.persistent, self.permanent]:
                if Item not in tracker.keys():
                    HistoryItem = HistoryItemClass()
                    HistoryItem.completed.append(day)

                    tracker.update({Item: HistoryItem})
                else:
                    tracker[Item].completed.append(day)

            EventScheduler.update_conditions()

            return

        def check(self, Item, tracker = "permanent", after = 0):
            tracker = getattr(self, tracker)

            if Item in tracker.keys():
                edited_tracker = tracker[Item].completed

                for instance in tracker[Item].completed:
                    if instance in edited_tracker and instance < after:
                        edited_tracker.remove(instance)

                return len(edited_tracker)

            return 0

        def check_when(self, Item, tracker = "permanent"):
            tracker = getattr(self, tracker)

            if Item in tracker.keys():
                if len(tracker[Item].completed) > 0:
                    return tracker[Item].completed[-1]

            return 0

        def remove(self, Item):
            for tracker in [self.event, self.recent, self.daily, self.weekly, self.season, self.persistent]:
                if Item in tracker.keys():
                    del tracker[Item]

            return

        def increment(self):
            self.last = copy.copy(self.recent)

            self.recent = {}

            if time_index == 0:
                self.daily = {}

                for Item in self.weekly.keys():
                    temp = self.weekly[Item].completed

                    for instance in temp:
                        if instance in self.weekly[Item].completed and day - instance > 6:
                            self.weekly[Item].completed.remove(instance)

                temp = self.weekly.keys()

                for Item in temp:
                    if not self.weekly[Item].completed:
                        del self.weekly[Item]

                if season_day == 0:
                    self.season = {}

            return

        def manually_reset(self, tracker):
            setattr(self, tracker, {})

            return