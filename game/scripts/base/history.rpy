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

        def initialize(self, item):
            for tracker in [self.event, self.recent, self.daily, self.weekly, self.season, self.persistent, self.permanent]:
                if item not in tracker.keys():
                    tracker.update({item: HistoryItemClass()})

        def update(self, item):
            global day

            global EventScheduler

            for tracker in [self.event, self.recent, self.daily, self.weekly, self.season, self.persistent, self.permanent]:
                if item not in tracker.keys():
                    HistoryItem = HistoryItemClass()
                    HistoryItem.completed.append(day)

                    tracker.update({item: HistoryItem})
                else:
                    tracker[item].completed.append(day)

            EventScheduler.update_conditions()

            return

        def check(self, item, tracker = "permanent"):
            tracker = getattr(self, tracker)

            if item in tracker.keys():
                if len(tracker[item].completed) > 0:
                    return len(tracker[item].completed)

            return 0

        def check_when(self, item, tracker = "permanent"):
            tracker = getattr(self, tracker)

            if item in tracker.keys():
                if len(tracker[item].completed) > 0:
                    return tracker[item].completed[-1]

            return 0

        def remove(self, item):
            for tracker in [self.event, self.recent, self.daily, self.weekly, self.season, self.persistent]:
                if item in tracker.keys():
                    del tracker[item]

            return

        def increment(self):
            self.last = copy.copy(self.recent)

            self.recent = {}

            if time_index == 0:
                self.daily = {}

                if weekday == 0:
                    self.weekly = {}

                if season_day == 0:
                    self.weekly = {}
                    
                    self.season = {}

            return

        def manually_reset(self, tracker):
            setattr(self, tracker, {})

            return