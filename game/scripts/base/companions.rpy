init -2 python:

    import copy

    class CompanionClass(object):
        def __init__(self, name, **properties):
            self.tag = name

            self.name = name
            self.names = [name]
            self.full_name = self.name
            self.public_name = self.name
            self.call_sign = self.name

            self.petname = self.name
            self.petnames = [self.name]
            self.Player_petname = None
            self.Player_petnames = []

            self.voice = properties.get("voice", None)
            
            self.level = 1
            self.XP = 0
            self.XP_goal = 200
            self.ability_points = 0

            self.stamina = 2
            self.max_stamina = 2

            self.love = properties.get("love", 0)
            self.trust = properties.get("trust", 0)

            self.stat_modifier = 1.0

            self.status = {
                "miffed": 0, "mad": 0, "heartbroken": 0, "horny": 0, "nympho": 0}

            self.sprite_anchor = [0.5, 0.5]
            self.sprite_position = [stage_center, 0.0]
            self.sprite_zoom = 1.0
            self.sprite_rotation = 0.0

            # sprite_layer = [background_characters (eg. teachers), top_bar, midground (eg. shower_steam), midground_characters (eg. teachers), foreground (eg. podium), foreground_characters (eg. Present), focused_Character, cover (eg. shower_steam)]
            self.sprite_layer = 7

            self.hovered = False

            self.brows = "neutral"
            self.eyes = "neutral"
            self.mouth = "neutral"
            self.blush = 0

            self.left_arm = "neutral"
            self.right_arm = "neutral"

            self.body_hair = {}
            self.default_body_hair = {}
            self.desired_body_hair = {}
            self.body_hair_to_shave = {}
            self.body_hair_to_grow = {}
            self.body_hair_growing = {}
            
            self.tan_lines = {
                "full": False, "top": False, "bottom": False}
            
            self.piercings = {
                "face": False, "nipple": False, "belly": False, "labia": False}
            
            self.spunk = {
                "hair": 0, "face": 0, "chin": 0, "mouth": 0, "tongue": 0,
                "breasts": 0, "back": 0, "belly": 0, "ass": 0, "hand": 0, "feet": 0}
            self.persistent_spunk = {
                "hair": 0, "face": 0, "chin": 0, "mouth": 0, "tongue": 0,
                "breasts": 0, "back": 0, "belly": 0, "ass": 0, "hand": 0, "feet": 0}
            self.creampie = {
                "pussy": 0, "anus": 0}

            self.buttplug = None
            self.buttplug_size = None

            self.remote_vibrator = None

            self.Wardrobe = WardrobeClass()
            self.Outfit = self.Wardrobe.indoor_Outfit
            self.previous_Outfit = self.Outfit.name
            self.Clothes = {}

            for C in self.Outfit.Clothes.keys():
                self.Clothes[C] = copy.copy(self.Outfit.Clothes[C])

            self.desire = 0

            self.position = "standing"
            self.Lovers = {}
            
            self.mouth_Actions = []
            self.neck_Actions = []
            self.right_hand_Actions = []
            self.left_hand_Actions = []
            self.right_thigh_Actions = []
            self.left_thigh_Actions = []
            self.right_foot_Actions = []
            self.left_foot_Actions = []
            self.right_breast_Actions = []
            self.right_nipple_Actions = []
            self.left_breast_Actions = []
            self.left_nipple_Actions = []
            self.ass_Actions = []
            self.vagina_Actions = []
            self.clitoris_Actions = []
            self.anus_Actions = []
            self.all_Actions = []

            self.all_Organs = [
                "mouth",
                "neck",
                "right_hand",
                "left_hand",
                "right_thigh",
                "left_thigh",
                "right_foot",
                "left_foot",
                "left_breast",
                "right_breast",
                "left_nipple",
                "right_nipple",
                "ass",
                "vagina",
                "clitoris",
                "anus"]

            self.unlocked_Actions = []
            self.possible_Actions = []
            self.available_Actions = []

            self.possible_poses = []
            self.available_poses = []

            self.throat_training = 0
            self.anal_training = 0
            
            self.likes = {}
            self.knows_about = []

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
            self.original_location = "hold"

            self.traits = []

            self.temp = None

        def change_face(self, face = None, **kwargs):
            face = self.default_face() if not face else face

            brows = kwargs.get("brows", None)
            eyes = kwargs.get("eyes", None)
            mouth = kwargs.get("mouth", None)
            blush = kwargs.get("blush", 0)

            self.brows, self.eyes, self.mouth, self.blush = eval(f"{self.tag}_faces('{face}')")

            if self.brows == "wrong":
                renpy.invoke_in_new_context(renpy.say, None, "Something went wrong with a face here.")

            if blush:
                self.blush = blush

            if brows:
                self.brows = brows

            if eyes:
                self.eyes = eyes

            if mouth:
                self.mouth = mouth

            return

        def default_face(self):
            if self.status["miffed"] or self.status["mad"]:
                face = "furious"
            elif self.status["heartbroken"]:
                face = "sad"
            elif self.status["horny"]:
                face = "sexy"
            elif self.status["nympho"]:
                face = "sexy"
            elif approval_check(self, threshold = "love"):
                face = "smirk2"
            else:
                face = "neutral"

            return face

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

            if self.status["miffed"] or self.status["mad"]:
                if renpy.random.random() > 0.75:
                    pose = "angry"
                elif renpy.random.random() > 0.5:
                    pose = "crossed"
                elif renpy.random.random() > 0.25:
                    pose = "hips"
                else:
                    pose = "neutral"
            elif self.status["heartbroken"]:
                if renpy.random.random() > 0.75:
                    if self.tag in ["Rogue"]:
                        left_arm = "rub_neck"
                        right_arm = "neutral"
                    elif self.tag in ["Laura"]:
                        pose = "angry"
                    elif self.tag in ["Jean"]:
                        pose = "sass"
                elif renpy.random.random() > 0.5:
                    pose = "crossed"
                elif renpy.random.random() > 0.25:
                    pose = "hips"
                else:
                    pose = "neutral"
            elif self.status["horny"]:
                if renpy.random.random() > 0.75:
                    if self.tag in ["Rogue"]:
                        left_arm = "rub_neck"
                        right_arm = "neutral"
                    elif self.tag in ["Laura"]:
                        pose = "angry"
                    elif self.tag in ["Jean"]:
                        pose = "sass"
                elif renpy.random.random() > 0.5:
                    pose = "crossed"
                elif renpy.random.random() > 0.25:
                    pose = "hips"
                else:
                    pose = "neutral"
            elif self.status["nympho"]:
                if renpy.random.random() > 0.75:
                    if self.tag in ["Rogue"]:
                        left_arm = "rub_neck"
                        right_arm = "neutral"
                    elif self.tag in ["Laura"]:
                        pose = "angry"
                    elif self.tag in ["Jean"]:
                        pose = "sass"
                elif renpy.random.random() > 0.5:
                    pose = "crossed"
                elif renpy.random.random() > 0.25:
                    pose = "hips"
                else:
                    pose = "neutral"
            else:
                if renpy.random.random() > 0.75:
                    if self.tag in ["Rogue"]:
                        left_arm = "rub_neck"
                        right_arm = "neutral"
                    elif self.tag in ["Laura"]:
                        pose = "angry"
                    elif self.tag in ["Jean"]:
                        pose = "sass"
                elif renpy.random.random() > 0.5:
                    pose = "crossed"
                elif renpy.random.random() > 0.25:
                    pose = "hips"
                else:
                    pose = "neutral"

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
                if self.behavior in ["training", "swimming"]:
                    self.destination = "bg_lockers"

                    if time_index < 3 and time_index not in self.schedule.keys():
                        if renpy.random.random() > 0.66:
                            self.schedule[time_index + 1] = ["bg_lockers", "showering"]
                        elif renpy.random.random() > 0.33:
                            self.schedule[time_index + 1] = ["bg_lockers", "changing"]
                elif time_index == 0 and self.location == Player.location and renpy.random.random() > 0.5:
                    self.destination = Player.location
                else:
                    possible_locations = eval(f"{self.tag}_locations()")

                    self.destination = renpy.random.choice(possible_locations)

            return

        def give(self, Clothing, reset_Wardrobe = True):
            self.Wardrobe.add_Clothing(Clothing)

            return

        def add_Outfit(self, Outfit):
            self.Wardrobe.add_Outfit(Outfit)

            return

        def remove_Outfit(self, name):
            self.Wardrobe.remove_Outfit(name)

            return

        def choose_Outfits(self):
            self.Wardrobe.choose_Outfits()

            return

        def check_statuses(self):
            if self.desire >= 75 and not self.History.check("horny", tracker = "recent"):
                self.give_status("horny")

            return

        def give_status(self, status):
            global update_messages
            
            if status == "miffed":
                if self.status["miffed"]:
                    self.status["miffed"] = 0
                    self.status["mad"] += 3
                else:
                    self.status[status] += 1
            elif status == "mad":
                self.status[status] += 3
            elif status == "heartbroken":
                self.status[status] += 3
            elif status == "horny":
                if self.status["horny"] >= 3:
                    self.status["horny"] = 0
                    self.status["nympho"] += 3
                else:
                    self.status[status] += 1
            elif status == "nympho":
                self.status[status] += 3

            update_messages.append("{color=%s}%s{/color} is {color=%s}%s{/color}" % (eval(f"{self.tag}_color"), self.name, "#feba00", status))
            
            if self.status[status] == 1:
                EventScheduler.Events[f"{self.tag}_became_{status}"].start()

            self.History.update(status)

            return

        def get_status(self):
            status = None

            if self.status["miffed"] or self.status["mad"]:
                status = "mad"
            elif self.status["heartbroken"]:
                status = "heartbroken"
            elif self.status["nympho"]:
                status = "nympho"
            elif self.status["horny"]:
                status = "horny"

            return status

        def is_in_normal_mood(self):
            if self.status["miffed"]:
                return False
            elif self.status["mad"]:
                return False
            elif self.status["heartbroken"]:
                return False
            elif self.wants_alone_time:
                return False

            return True