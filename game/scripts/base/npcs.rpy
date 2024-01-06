init -2 python:

    class NPCClass(object):
        def __init__(self, name, **properties):
            self.tag = name

            self.name = name
            self.names = [name]
            self.full_name = self.name
            self.public_name = self.name
            self.call_sign = self.name

            self.voice = properties.get("voice", None)
            
            self.level = 1
            self.XP = 0
            self.XP_goal = 250
            self.stat_points = 0

            self.ability_points = 0

            self.sprite_anchor = [0.5, 0.5]
            self.sprite_position = [stage_center, 0.0]
            self.sprite_zoom = 1.0
            self.sprite_rotation = 0.0

            # sprite_layer = [background_characters (eg. teachers), midground (eg. shower_steam), midground_characters (eg. teachers), foreground (eg. podium), foreground_characters (eg. Present), focused_Character, cover (eg. shower_steam)]
            self.sprite_layer = 7

            self.hovered = False

            self.brows = "neutral"
            self.eyes = "neutral"
            self.mouth = "neutral"

            self.left_arm = "neutral"
            self.right_arm = "neutral"

            self.outfit = None
            self.hair = None
            self.beard = None

            self.chat_options = []
            self.Event_chat_options = []
            self.text_options = []
            self.timed_text_options = {}
            self.mandatory_text_options = []
            self.text_history = []

            self.schedule = {}
            self.behavior = None
            self.behavior_Partners = []

            self.wants_alone_time = 0

            self.inventory = {}

            self.History = HistoryClass()

            self.database = {}
            self.database_type = None

            self.home = f"bg_{self.tag}"
            self.destination = "hold"
            self.location = "hold"
            
            self.traits = []
            
            self.temp = None

        def change_face(self, face = "neutral", **kwargs):
            if not face:
                face, brows, eyes, mouth, blush = self.default_face()

            brows = kwargs.get("brows", None)
            eyes = kwargs.get("eyes", None)
            mouth = kwargs.get("mouth", None)
            blush = kwargs.get("blush", 0)

            self.brows, self.eyes, self.mouth, self.blush = eval(f"{self.tag}_faces('{face}')")

            if blush:
                self.blush = blush
                
            if self.brows == "wrong":
                renpy.invoke_in_new_context(renpy.say, None, "Something went wrong with a face here.")

            if brows:
                self.brows = brows

            if eyes:
                self.eyes = eyes

            if mouth:
                self.mouth = mouth

            return

        def default_face(self):
            face = "neutral"
            brows = None
            eyes = None
            mouth = None
            blush = 0

            dice_roll = renpy.random.randint(1, 2)

            if dice_roll == 1:
                face = "neutral"
            elif dice_roll == 2:
                face = "smirk1"

            return face, brows, eyes, mouth, blush

        def change_arms(self, pose = None, **kwargs):
            if not pose:
                pose, left_arm, right_arm = self.default_arms()

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

        def default_arms(self):
            pose = "neutral"
            left_arm = None
            right_arm = None

            dice_roll = renpy.random.randint(1, 2)

            if dice_roll == 1:
                pose = "neutral"
            elif dice_roll == 2:
                pose = "crossed"

            return pose, left_arm, right_arm

        def give_trait(self, trait):
            if trait not in self.traits:
                self.traits.append(trait)

            return

        def remove_trait(self, trait):
            if trait in self.traits:
                self.traits.remove(trait)

            return

        def check_traits(self, trait):
            if trait in self.traits:
                return True
        
            return False

        def travel(self):
            if self.location != "hold":
                possible_locations = eval(f"{self.tag}_locations()")

                self.destination = renpy.random.choice(possible_locations)

            return