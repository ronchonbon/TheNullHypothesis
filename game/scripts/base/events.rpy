init -2:

    default sandbox = False
    default ongoing_Event = False
    
    default EventScheduler = EventSchedulerClass()

init -3 python:

    class EventClass(object):
        def __init__(self, label, conditions, **kwargs):
            self.label = label

            self.conditions = conditions

            self.waiting = kwargs.get("waiting", False)
            self.traveling = kwargs.get("traveling", False)
            self.chatting = kwargs.get("chatting", False)
            self.texting = kwargs.get("texting", False)
            self.flirting = kwargs.get("flirting", False)
            self.hooking_up = kwargs.get("hooking_up", False)
            self.getting_ready_for_bed = kwargs.get("getting_ready_for_bed", False)
            self.sleeping = kwargs.get("sleeping", False)
            self.waking = kwargs.get("waking", False)

            self.priority = kwargs.get("priority", 0)

            self.repeatable = kwargs.get("repeatable", False)

            self.automatic = kwargs.get("automatic", False)

            self.markers = kwargs.get("markers", {})

            self.active = False

            self.completed = False
            self.completed_when = 1e8

            self.counter = 0

        def check_conditions(self):
            met = True

            for condition in self.conditions:
                if not eval(condition):
                    met = False

                    break

            if met:
                self.active = True
            else:
                self.active = False

            return

        def check_markers(self):
            global marked_locations

            for marker_location in self.markers.keys():
                met = True

                for condition in self.markers[marker_location]:
                    if not eval(condition):
                        met = False

                        break

                if met and self.label not in marked_locations[marker_location]:
                    marked_locations[marker_location].append(self.label)
                elif not met and self.label in marked_locations[marker_location]:
                    marked_locations[marker_location].remove(self.label)

            return

        def start(self):
            global day

            self.completed = True
            self.completed_when = day

            self.counter += 1

            renpy.call(self.label)

            return

    class EventSchedulerClass(object):
        def __init__(self):
            self.Events = {}

        def add_Event(self, Event):
            if Event.label not in self.Events.keys():
                self.Events[Event.label] = Event
            else:
                if hasattr(self.Events[Event.label], "completed_when"):
                    Event.completed_when = self.Events[Event.label].completed_when
                else:
                    if self.Events[Event.label].counter:
                        Event.completed_when = self.Events[Event.label].completed

                if self.Events[Event.label].counter:
                    Event.completed = True

                    Event.counter = self.Events[Event.label].counter

                self.Events[Event.label] = Event
                
            return

        def update_conditions(self):
            global QuestPool

            for Event in self.Events.values():
                if not Event.completed or Event.repeatable:
                    Event.check_conditions()
                    Event.check_markers()
                else:
                    Event.active = False

            QuestPool.check_progress()
            register_Quests()
            QuestPool.check_progress()

            return

        def get_automatic_Events(self):
            self.update_conditions()

            automatic_Events = []

            for Event in self.Events.values():
                if Event.active and Event.automatic:
                    automatic_Events.append(Event)

            return automatic_Events

        def choose_Event(self, **kwargs):
            self.update_conditions()

            waiting = kwargs.get("waiting", False)
            traveling = kwargs.get("traveling", False)
            chatting = kwargs.get("chatting", False)
            texting = kwargs.get("texting", False)
            flirting = kwargs.get("flirting", False)
            hooking_up = kwargs.get("hooking_up", False)
            getting_ready_for_bed = kwargs.get("getting_ready_for_bed", False)
            sleeping = kwargs.get("sleeping", False)
            waking = kwargs.get("waking", False)

            active_Events = []

            for Event in self.Events.values():
                if Event.active and not Event.automatic:
                    if waiting:
                        if Event.waiting:
                            active_Events.append(Event)
                    elif traveling:
                        if Event.traveling:
                            active_Events.append(Event)
                    elif chatting:
                        if Event.chatting:
                            active_Events.append(Event)
                    elif texting:
                        if Event.texting:
                            active_Events.append(Event)
                    elif hooking_up:
                        if Event.hooking_up:
                            active_Events.append(Event)
                    elif getting_ready_for_bed:
                        if Event.getting_ready_for_bed:
                            active_Events.append(Event)
                    elif sleeping:
                        if Event.sleeping:
                            active_Events.append(Event)
                    elif waking:
                        if Event.waking:
                            active_Events.append(Event)
                    elif not Event.waiting and not Event.traveling and not Event.chatting and not Event.texting and not Event.flirting and not Event.hooking_up and not Event.getting_ready_for_bed and not Event.sleeping and not Event.waking:
                        active_Events.append(Event)

            priority_Events = {}

            for Event in active_Events:
                if Event.priority:
                    if Event.priority not in priority_Events.keys():
                        priority_Events[Event.priority] = [Event]
                    else:
                        priority_Events[Event.priority].append(Event)

            if priority_Events:
                chosen_priority = max(priority_Events.keys())

                return renpy.random.choice(priority_Events[chosen_priority])
            elif active_Events:
                return renpy.random.choice(active_Events)
            else:
                return False

        def check_Events(self):
            for Event in self.Events.values():
                for condition in Event.conditions:
                    try:
                        eval(condition)
                    except:
                        print(condition)

            return

label start_Event(E):
    $ E.start()

    return