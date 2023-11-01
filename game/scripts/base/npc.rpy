init -2 python:

    class NPCClass(object):
        def __init__(self, name, **properties):
            self.tag = name

            self.name = name
            self.names = [name]
            self.full_name = self.name
            self.call_sign = self.name

            self.database = {}

            self.voice = properties.get("voice", None)

            self.electronic = False
            self.telepathic = False

            self.sprite_anchor = [0.5, 0.5]
            self.sprite_position = [stage_center, 0.0]
            self.sprite_zoom = 1.0
            self.sprite_rotation = 0.0

            # sprite_layer = [background_characters (eg. teachers), midground (eg. shower_steam), midground_characters (eg. teachers), foreground (eg. podium), foreground_characters (eg. Present), focused_Girl, cover (eg. shower_steam)]
            self.sprite_layer = 6

            self.hovered = False

            self.brows = "neutral"
            self.eyes = "neutral"
            self.mouth = "neutral"

            self.wet = False

            self.home = f"bg_{self.tag}"
            self.destination = "hold"
            self.location = "hold"

            self.is_shop = False
            self.gives_quests = False
            self.gives_work = False
            self.has_jobs = False

            self.chat_options = []
            self.Event_chat_options = []
            self.text_options = []
            self.timed_text_options = {}
            self.mandatory_text_options = []
            self.text_history = []

            self.History = HistoryClass()

            self.outfit = None
            
            self.inventory = {}

            self.waking_up = False
            self.studying = False
            self.in_class = False
            self.training = False
            self.teaching = False
            self.swimming = False
            self.sunbathing = False
            self.showering = False
            self.getting_ready_for_bed = False
            self.sleeping = False

            self.wants_alone_time = 0
            
            self.schedule = {}
            
            self.temp = None

        def change_face(self, face = "neutral", **kwargs):
            brows = kwargs.get("brows", None)
            eyes = kwargs.get("eyes", None)
            mouth = kwargs.get("mouth", None)

            if face == "neutral":
                self.mouth = "neutral"
                self.brows = "neutral"
                self.eyes = "neutral"
            elif face == "angry":
                self.brows = "furrowed"
                self.eyes = "neutral"
                self.mouth = "frown"
            elif face == "confused":
                self.brows = "furrowed"
                self.eyes = "squint"
                self.mouth = "neutral"
            elif face == "happy":
                self.brows = "neutral"
                self.eyes = "neutral"
                self.mouth = "smile"
            elif face == "sad":
                self.brows = "neutral"
                self.eyes = "neutral"
                self.mouth = "frown"
            elif face == "stunned":
                self.brows = "neutral"
                self.eyes = "up"
                self.mouth = "neutral"
            elif face == "surprised":
                self.brows = "raised"
                self.eyes = "wide"
                self.mouth = "neutral"
            else:
                renpy.say(None, "Something went wrong with a face here.")

            if brows:
                self.brows = brows

            if eyes:
                self.eyes = eyes

            if mouth:
                self.mouth = mouth

            return

        def travel(self):
            global weather
            global snow_left

            if self.location != "hold":
                possible_locations = []

                possible_locations.append(self.home)

                if time_index < 2 and weekday < 5:
                    possible_locations.append("bg_classroom")
                    possible_locations.append("bg_classroom")
                
                if self.tag == "Charles":
                    if time_index < 3:
                        possible_locations.append("bg_study")

                        if time_index == 2:
                            self.destination = "bg_study"

                            return
                elif self.tag == "Kurt":
                    if time_index < 3 and weather != "rain":
                        possible_locations.append("bg_campus")

                    if time_index < 3:
                        possible_locations.append("bg_danger")

                    if time_index < 3:
                        if time_index == 2:
                            if temperature[time_index] > 22 and not weather and snow_left == 0:
                                possible_locations.append("bg_pool")

                            possible_locations.append("bg_mall")
                        elif weekday > 4:
                            if temperature[time_index] > 22 and not weather and snow_left == 0:
                                possible_locations.append("bg_pool")

                            possible_locations.append("bg_mall")

                self.destination = renpy.random.choice(possible_locations)

            return