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

            self.database = {}

            self.petname = self.name
            self.petnames = [self.name]
            self.Player_petname = None
            self.Player_petnames = []

            self.voice = properties.get("voice", None)
            
            self.level = 1
            self.XP = 0
            self.XP_goal = 200

            self.platonic = False

            self.love = properties.get("love", 0)
            self.trust = properties.get("trust", 0)

            self.desire = properties.get("desire", 0)

            self.stat_modifier = 1.0

            self.stamina = 2
            self.max_stamina = 2

            self.status = {
                "miffed": 0, "mad": 0, "heartbroken": 0, "horny": 0, "nympho": 0}

            self.electronic = False
            self.telepathic = False

            self.sprite_anchor = [0.5, 0.5]
            self.sprite_position = [stage_center, 0.0]
            self.sprite_zoom = 1.0
            self.sprite_rotation = 0.0

            # sprite_layer = [background_characters (eg. teachers), top_bar, midground (eg. shower_steam), midground_characters (eg. teachers), foreground (eg. podium), foreground_characters (eg. Present), focused_Girl, cover (eg. shower_steam)]
            self.sprite_layer = 7

            self.hovered = False

            self.brows = "neutral"
            self.eyes = "neutral"
            self.mouth = "neutral"
            self.blush = 0

            self.left_arm = "neutral"
            self.right_arm = "neutral"

            self.pubes = None
            self.default_pubes = None
            self.desired_pubes = None
            self.pubes_to_shave = False
            self.pubes_to_grow = False
            self.pubes_growing = False
            self.customizable_pubes = False

            self.wet = False
            
            self.tan_lines = {
                "full": False, "top": False, "bottom": False}
            
            self.piercings = {
                "face": False, "nipple": False, "belly": False, "labia": False}
            
            self.grool = 0
            
            self.spunk = {
                "hair": False, "face": False, "chin": False, "mouth": False, "tongue": False,
                "breasts": False, "back": False, "belly": False, "ass": False, "hand": False, "feet": False}
            self.persistent_spunk = {
                "hair": False, "face": False, "chin": False, "mouth": False, "tongue": False,
                "breasts": False, "back": False, "belly": False, "ass": False, "hand": False, "feet": False}
            self.creampie = {
                "pussy": False, "anus": False}

            self.buttplug = None
            self.buttplug_size = None

            self.remote_vibrator = False

            self.ground_shadow = True

            self.home = f"bg_{self.tag}"
            self.destination = "hold"
            self.location = "hold"
            self.original_location = "hold"

            self.chat_options = []
            self.Event_chat_options = []
            self.text_options = []
            self.timed_text_options = {}
            self.mandatory_text_options = []
            self.text_history = []

            self.History = HistoryClass()

            self.Wardrobe = WardrobeClass()
            self.Outfit = self.Wardrobe.indoor_Outfit
            self.previous_Outfit = self.Outfit.name
            self.Clothes = {}

            for C in self.Outfit.Clothes.keys():
                self.Clothes[C] = copy.copy(self.Outfit.Clothes[C])

            self.inventory = {}
            self.has_keys_to_Players_room = False

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

            self.virgin = False
            self.exhibitionist = False
            self.throat_training = 0
            self.anal_training = 0
            self.orgasm_control = False
            self.birth_control = False

            self.likes = {}
            self.knows_about = []

            self.behavior = None
            self.behavior_Partners = []
            
            self.orgasming = False
            
            self.wants_alone_time = 0
            
            self.schedule = {}

            self.messy_bed = False
            self.clothes_on_floor = False

            self.quirk = None

            self.naked = False
            
            self.breasts_supported = False

            self.bra_covered = False
            self.breasts_covered = False
            self.back_covered = False
            self.belly_covered = False
            self.thighs_covered = False
            self.underwear_covered = False
            self.ass_covered = False
            self.pussy_covered = False
            self.anus_covered = False
            self.feet_covered = False

            self.bra_hidden = False
            self.breasts_hidden = False
            self.back_hidden = False
            self.belly_hidden = False
            self.thighs_hidden = False
            self.underwear_hidden = False
            self.ass_hidden = False
            self.pussy_hidden = False
            self.anus_hidden = False
            self.feet_hidden = False

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
                face = "neutral"
            elif self.status["heartbroken"]:
                face = "neutral"
            elif self.status["horny"]:
                face = "neutral"
            elif self.status["nympho"]:
                face = "neutral"
            # elif approval_check(self, threshold = "love"):
            #     face = "neutral"
            else:
                face = "neutral"

            return face

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

        def default_arms(self):
            if self.status["miffed"] or self.status["mad"]:
                pose = "neutral"
            elif self.status["heartbroken"]:
                pose = "neutral"
            elif self.status["horny"]:
                pose = "neutral"
            elif self.status["nympho"]:
                pose = "neutral"
            # elif approval_check(self, threshold = "love"):
            #     pose = "neutral"
            else:
                pose = "neutral"

            return pose

        def travel(self):
            global Player

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
            
            global EventScheduler
            
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