init -2 python:

    class NPCClass(object):
        def __init__(self, name, **properties):
            self.tag = name

            self.name = name
            self.names = [name]
            self.full_name = self.name
            self.public_name = self.name
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
            self.sprite_layer = 7

            self.hovered = False

            self.brows = "neutral"
            self.eyes = "neutral"
            self.mouth = "neutral"

            self.left_arm = "neutral"
            self.right_arm = "neutral"
            
            self.wet = False

            self.ground_shadow = True

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

            self.behavior = None
            self.behavior_Partners = []

            self.wants_alone_time = 0
            
            self.schedule = {}
            
            self.temp = None

        def change_face(self, face = "neutral", **kwargs):
            face = self.default_face() if not face else face

            brows = kwargs.get("brows", None)
            eyes = kwargs.get("eyes", None)
            mouth = kwargs.get("mouth", None)

            self.brows, self.eyes, self.mouth = eval(f"{self.tag}_faces('{face}')")

            if self.brows == "wrong":
                renpy.invoke_in_new_context(renpy.say, None, "Something went wrong with a face here.")

            if brows:
                self.brows = brows

            if eyes:
                self.eyes = eyes

            if mouth:
                self.mouth = mouth

            return

        def change_arms(self, pose = None, **kwargs):
            pose = self.default_arms() if not pose else pose

            left_arm = kwargs.get("left_arm", None)
            right_arm = kwargs.get("right_arm", None)

            self.left_arm, self.right_arm = eval(f"{self.tag}_arms('{pose}')")

            if self.left_arm == "wrong":
                renpy.invoke_in_new_context(renpy.say, None, "Something went wrong with an arm pose here.")

            if left_arm:
                self.left_arm = left_arm

            if right_arm:
                self.right_arm = right_arm

            if self.left_arm == "crossed" or self.right_arm == "crossed":
                self.left_arm = "crossed"
                self.right_arm = "crossed"

            return

        def travel(self):
            if self.location != "hold":
                possible_locations = eval(f"{self.tag}_locations()")

                self.destination = renpy.random.choice(possible_locations)

            return