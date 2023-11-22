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

            # sprite_layer = [background_characters (eg. teachers), midground (eg. shower_steam), midground_characters (eg. teachers), foreground (eg. podium), foreground_characters (eg. Present), focused_Girl, cover (eg. shower_steam)]
            self.sprite_layer = 6

            self.hovered = False

            self.brows = "neutral"
            self.eyes = "neutral"
            self.mouth = "neutral"
            self.blush = 0

            self.left_arm_pose = "neutral"
            self.right_arm_pose = "neutral"

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

            if self.tag == "Rogue":
                if face == "neutral":
                    self.brows = "neutral"
                    self.eyes = "neutral"
                    self.mouth = "neutral"
                elif face == "angry1":
                    self.brows = "furrowed"
                    self.eyes = "neutral"
                    self.mouth = "neutral"
                elif face == "angry2":
                    self.brows = "furrowed"
                    self.eyes = "neutral"
                    self.mouth = "happy"
                elif face == "appalled1":
                    self.brows = "furrowed"
                    self.eyes = "wide"
                    self.mouth = "neutral"
                elif face == "appalled2":
                    self.brows = "furrowed"
                    self.eyes = "wide"
                    self.mouth = "open"
                elif face == "appalled3":
                    self.brows = "furrowed"
                    self.eyes = "wide"
                    self.mouth = "agape"
                elif face == "confused1":
                    self.brows = "cocked"
                    self.eyes = "neutral"
                    self.mouth = "neutral"
                elif face == "confused2":
                    self.brows = "cocked"
                    self.eyes = "wide"
                    self.mouth = "neutral"
                elif face == "confused3":
                    self.brows = "cocked"
                    self.eyes = "wide"
                    self.mouth = "agape"
                elif face == "devious":
                    self.brows = "neutral"
                    self.eyes = "squint"
                    self.mouth = "smile"
                elif face == "furious":
                    self.brows = "furrowed"
                    self.eyes = "neutral"
                    self.mouth = "frown"
                elif face == "happy":
                    self.brows = "neutral"
                    self.eyes = "neutral"
                    self.mouth = "smile"
                elif face == "kiss1":
                    self.brows = "worried"
                    self.eyes = "closed"
                    self.mouth = "kiss"
                elif face == "kiss2":
                    self.brows = "neutral"
                    self.eyes = "closed"
                    self.mouth = "kiss"
                elif face == "manic":
                    self.brows = "worried"
                    self.eyes = "wide"
                    self.mouth = "open"

                    if not blush:
                        blush = 1
                elif face == "perplexed":
                    self.brows = "cocked"
                    self.eyes = "wide"
                    self.mouth = "open"
                elif face == "pleased1":
                    self.brows = "raised"
                    self.eyes = "neutral"
                    self.mouth = "smirk"
                elif face == "pleased2":
                    self.brows = "raised"
                    self.eyes = "wide"
                    self.mouth = "smirk"
                elif face == "sad":
                    self.brows = "worried"
                    self.eyes = "neutral"
                    self.mouth = "frown"
                elif face == "sexy":
                    self.brows = "neutral"
                    self.eyes = "sexy"
                    self.mouth = "lipbite"
                elif face == "sly":
                    self.brows = "neutral"
                    self.eyes = "squint"
                    self.mouth = "smirk"
                elif face == "smirk1":
                    self.brows = "neutral"
                    self.eyes = "neutral"
                    self.mouth = "happy"
                elif face == "smirk2":
                    self.brows = "neutral"
                    self.eyes = "neutral"
                    self.mouth = "smirk"
                elif face == "surprised1":
                    self.brows = "raised"
                    self.eyes = "neutral"
                    self.mouth = "open"
                elif face == "surprised2":
                    self.brows = "raised"
                    self.eyes = "wide"
                    self.mouth = "open"
                elif face == "surprised3":
                    self.brows = "raised"
                    self.eyes = "wide"
                    self.mouth = "agape"
                elif face == "suspicious1":
                    self.brows = "furrowed"
                    self.eyes = "squint"
                    self.mouth = "neutral"
                elif face == "suspicious2":
                    self.brows = "furrowed"
                    self.eyes = "squint"
                    self.mouth = "frown"
                elif face == "worried1":
                    self.brows = "worried"
                    self.eyes = "neutral"
                    self.mouth = "neutral"
                elif face == "worried2":
                    self.brows = "worried"
                    self.eyes = "wide"
                    self.mouth = "neutral"
                elif face == "worried3":
                    self.brows = "worried"
                    self.eyes = "wide"
                    self.mouth = "open"
                elif face == "worried4":
                    self.brows = "worried"
                    self.eyes = "wide"
                    self.mouth = "agape"
                else:
                    renpy.say(None, "Something went wrong with a face here.")
            elif self.tag == "Laura":
                if face == "neutral":
                    self.brows = "neutral"
                    self.eyes = "neutral"
                    self.mouth = "neutral"
                elif face == "angry1":
                    self.brows = "furrowed"
                    self.eyes = "neutral"
                    self.mouth = "neutral"
                elif face == "angry2":
                    self.brows = "furrowed"
                    self.eyes = "neutral"
                    self.mouth = "happy"
                elif face == "appalled1":
                    self.brows = "furrowed"
                    self.eyes = "wide"
                    self.mouth = "neutral"
                elif face == "appalled2":
                    self.brows = "furrowed"
                    self.eyes = "wide"
                    self.mouth = "happy"
                elif face == "appalled3":
                    self.brows = "furrowed"
                    self.eyes = "wide"
                    self.mouth = "open"
                elif face == "confused1":
                    self.brows = "cocked"
                    self.eyes = "neutral"
                    self.mouth = "neutral"
                elif face == "confused2":
                    self.brows = "cocked"
                    self.eyes = "wide"
                    self.mouth = "neutral"
                elif face == "confused3":
                    self.brows = "cocked"
                    self.eyes = "wide"
                    self.mouth = "open"
                elif face == "devious":
                    self.brows = "neutral"
                    self.eyes = "squint"
                    self.mouth = "smile"
                elif face == "furious":
                    self.brows = "furrowed"
                    self.eyes = "neutral"
                    self.mouth = "frown"
                elif face == "happy":
                    self.brows = "neutral"
                    self.eyes = "neutral"
                    self.mouth = "smile"
                elif face == "kiss1":
                    self.brows = "worried"
                    self.eyes = "closed"
                    self.mouth = "kiss"
                elif face == "kiss2":
                    self.brows = "neutral"
                    self.eyes = "closed"
                    self.mouth = "kiss"
                elif face == "manic":
                    self.brows = "worried"
                    self.eyes = "wide"
                    self.mouth = "smile"

                    if not blush:
                        blush = 1
                elif face == "perplexed":
                    self.brows = "cocked"
                    self.eyes = "wide"
                    self.mouth = "neutral"
                elif face == "pleased1":
                    self.brows = "raised"
                    self.eyes = "neutral"
                    self.mouth = "smirk"
                elif face == "pleased2":
                    self.brows = "raised"
                    self.eyes = "wide"
                    self.mouth = "smirk"
                elif face == "sad":
                    self.brows = "worried"
                    self.eyes = "neutral"
                    self.mouth = "frown"
                elif face == "sexy":
                    self.brows = "neutral"
                    self.eyes = "sexy"
                    self.mouth = "lipbite"
                elif face == "sly":
                    self.brows = "neutral"
                    self.eyes = "squint"
                    self.mouth = "smirk"
                elif face == "smirk1":
                    self.brows = "neutral"
                    self.eyes = "neutral"
                    self.mouth = "happy"
                elif face == "smirk2":
                    self.brows = "neutral"
                    self.eyes = "neutral"
                    self.mouth = "smirk"
                elif face == "surprised1":
                    self.brows = "raised"
                    self.eyes = "neutral"
                    self.mouth = "neutral"
                elif face == "surprised2":
                    self.brows = "raised"
                    self.eyes = "wide"
                    self.mouth = "neutral"
                elif face == "surprised3":
                    self.brows = "raised"
                    self.eyes = "wide"
                    self.mouth = "open"
                elif face == "suspicious1":
                    self.brows = "furrowed"
                    self.eyes = "squint"
                    self.mouth = "neutral"
                elif face == "suspicious2":
                    self.brows = "furrowed"
                    self.eyes = "squint"
                    self.mouth = "frown"
                elif face == "worried1":
                    self.brows = "worried"
                    self.eyes = "neutral"
                    self.mouth = "neutral"
                elif face == "worried2":
                    self.brows = "worried"
                    self.eyes = "wide"
                    self.mouth = "neutral"
                elif face == "worried3":
                    self.brows = "worried"
                    self.eyes = "wide"
                    self.mouth = "happy"
                elif face == "worried4":
                    self.brows = "worried"
                    self.eyes = "wide"
                    self.mouth = "open"
                else:
                    renpy.say(None, "Something went wrong with a face here.")
            elif self.tag == "Jean":
                if face == "neutral":
                    self.brows = "neutral"
                    self.eyes = "neutral"
                    self.mouth = "neutral"
                elif face == "angry1":
                    self.brows = "furrowed"
                    self.eyes = "neutral"
                    self.mouth = "neutral"
                elif face == "angry2":
                    self.brows = "furrowed"
                    self.eyes = "neutral"
                    self.mouth = "happy"
                elif face == "appalled1":
                    self.brows = "furrowed"
                    self.eyes = "wide"
                    self.mouth = "neutral"
                elif face == "appalled2":
                    self.brows = "furrowed"
                    self.eyes = "wide"
                    self.mouth = "open"
                elif face == "appalled3":
                    self.brows = "furrowed"
                    self.eyes = "wide"
                    self.mouth = "agape"
                elif face == "confused1":
                    self.brows = "cocked"
                    self.eyes = "neutral"
                    self.mouth = "neutral"
                elif face == "confused2":
                    self.brows = "cocked"
                    self.eyes = "wide"
                    self.mouth = "neutral"
                elif face == "confused3":
                    self.brows = "cocked"
                    self.eyes = "wide"
                    self.mouth = "agape"
                elif face == "devious":
                    self.brows = "neutral"
                    self.eyes = "squint"
                    self.mouth = "smile"
                elif face == "furious":
                    self.brows = "furrowed"
                    self.eyes = "neutral"
                    self.mouth = "frown"
                elif face == "happy":
                    self.brows = "neutral"
                    self.eyes = "neutral"
                    self.mouth = "smile"
                elif face == "kiss1":
                    self.brows = "worried"
                    self.eyes = "closed"
                    self.mouth = "kiss"
                elif face == "kiss2":
                    self.brows = "neutral"
                    self.eyes = "closed"
                    self.mouth = "kiss"
                elif face == "manic":
                    self.brows = "worried"
                    self.eyes = "wide"
                    self.mouth = "smile"

                    if not blush:
                        blush = 1
                elif face == "perplexed":
                    self.brows = "cocked"
                    self.eyes = "wide"
                    self.mouth = "open"
                elif face == "pleased1":
                    self.brows = "raised"
                    self.eyes = "neutral"
                    self.mouth = "smirk"
                elif face == "pleased2":
                    self.brows = "raised"
                    self.eyes = "wide"
                    self.mouth = "smirk"
                elif face == "sad":
                    self.brows = "worried"
                    self.eyes = "neutral"
                    self.mouth = "frown"
                elif face == "sexy":
                    self.brows = "neutral"
                    self.eyes = "sexy"
                    self.mouth = "lipbite"
                elif face == "sly":
                    self.brows = "neutral"
                    self.eyes = "squint"
                    self.mouth = "smirk"
                elif face == "smirk1":
                    self.brows = "neutral"
                    self.eyes = "neutral"
                    self.mouth = "happy"
                elif face == "smirk2":
                    self.brows = "neutral"
                    self.eyes = "neutral"
                    self.mouth = "smirk"
                elif face == "surprised1":
                    self.brows = "raised"
                    self.eyes = "neutral"
                    self.mouth = "open"
                elif face == "surprised2":
                    self.brows = "raised"
                    self.eyes = "wide"
                    self.mouth = "open"
                elif face == "surprised3":
                    self.brows = "raised"
                    self.eyes = "wide"
                    self.mouth = "agape"
                elif face == "suspicious1":
                    self.brows = "furrowed"
                    self.eyes = "squint"
                    self.mouth = "neutral"
                elif face == "suspicious2":
                    self.brows = "furrowed"
                    self.eyes = "squint"
                    self.mouth = "frown"
                elif face == "worried1":
                    self.brows = "worried"
                    self.eyes = "neutral"
                    self.mouth = "neutral"
                elif face == "worried2":
                    self.brows = "worried"
                    self.eyes = "wide"
                    self.mouth = "neutral"
                elif face == "worried3":
                    self.brows = "worried"
                    self.eyes = "wide"
                    self.mouth = "open"
                elif face == "worried4":
                    self.brows = "worried"
                    self.eyes = "wide"
                    self.mouth = "agape"
            elif self.tag == "Ororo":
                if face == "neutral":
                    self.brows = "neutral"
                    self.eyes = "neutral"
                    self.mouth = "neutral"
                elif face == "angry1":
                    self.brows = "furrowed"
                    self.eyes = "neutral"
                    self.mouth = "neutral"
                elif face == "angry2":
                    self.brows = "furrowed"
                    self.eyes = "neutral"
                    self.mouth = "happy"
                elif face == "appalled1":
                    self.brows = "furrowed"
                    self.eyes = "wide"
                    self.mouth = "neutral"
                elif face == "appalled2":
                    self.brows = "furrowed"
                    self.eyes = "wide"
                    self.mouth = "open"
                elif face == "appalled3":
                    self.brows = "furrowed"
                    self.eyes = "wide"
                    self.mouth = "agape"
                elif face == "confused1":
                    self.brows = "cocked"
                    self.eyes = "neutral"
                    self.mouth = "neutral"
                elif face == "confused2":
                    self.brows = "cocked"
                    self.eyes = "wide"
                    self.mouth = "neutral"
                elif face == "confused3":
                    self.brows = "cocked"
                    self.eyes = "wide"
                    self.mouth = "agape"
                elif face == "devious":
                    self.brows = "neutral"
                    self.eyes = "squint"
                    self.mouth = "smile"
                elif face == "furious":
                    self.brows = "furrowed"
                    self.eyes = "neutral"
                    self.mouth = "frown"
                elif face == "happy":
                    self.brows = "neutral"
                    self.eyes = "neutral"
                    self.mouth = "smile"
                elif face == "kiss1":
                    self.brows = "worried"
                    self.eyes = "closed"
                    self.mouth = "kiss"
                elif face == "kiss2":
                    self.brows = "neutral"
                    self.eyes = "closed"
                    self.mouth = "kiss"
                elif face == "manic":
                    self.brows = "worried"
                    self.eyes = "wide"
                    self.mouth = "smile"

                    if not blush:
                        blush = 1
                elif face == "perplexed":
                    self.brows = "cocked"
                    self.eyes = "wide"
                    self.mouth = "open"
                elif face == "pleased1":
                    self.brows = "raised"
                    self.eyes = "neutral"
                    self.mouth = "smirk"
                elif face == "pleased2":
                    self.brows = "raised"
                    self.eyes = "wide"
                    self.mouth = "smirk"
                elif face == "sad":
                    self.brows = "worried"
                    self.eyes = "neutral"
                    self.mouth = "frown"
                elif face == "sexy":
                    self.brows = "neutral"
                    self.eyes = "sexy"
                    self.mouth = "lipbite"
                elif face == "sly":
                    self.brows = "neutral"
                    self.eyes = "squint"
                    self.mouth = "smirk"
                elif face == "smirk1":
                    self.brows = "neutral"
                    self.eyes = "neutral"
                    self.mouth = "happy"
                elif face == "smirk2":
                    self.brows = "neutral"
                    self.eyes = "neutral"
                    self.mouth = "smirk"
                elif face == "surprised1":
                    self.brows = "raised"
                    self.eyes = "neutral"
                    self.mouth = "open"
                elif face == "surprised2":
                    self.brows = "raised"
                    self.eyes = "wide"
                    self.mouth = "open"
                elif face == "surprised3":
                    self.brows = "raised"
                    self.eyes = "wide"
                    self.mouth = "agape"
                elif face == "suspicious1":
                    self.brows = "furrowed"
                    self.eyes = "squint"
                    self.mouth = "neutral"
                elif face == "suspicious2":
                    self.brows = "furrowed"
                    self.eyes = "squint"
                    self.mouth = "frown"
                elif face == "worried1":
                    self.brows = "worried"
                    self.eyes = "neutral"
                    self.mouth = "neutral"
                elif face == "worried2":
                    self.brows = "worried"
                    self.eyes = "wide"
                    self.mouth = "neutral"
                elif face == "worried3":
                    self.brows = "worried"
                    self.eyes = "wide"
                    self.mouth = "open"
                elif face == "worried4":
                    self.brows = "worried"
                    self.eyes = "wide"
                    self.mouth = "agape"
                else:
                    renpy.say(None, "Something went wrong with a face here.")

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
                face = "angry1"
            elif self.status["heartbroken"]:
                face = "sad"
            elif self.status["horny"]:
                face = "sexy"
            elif self.status["nympho"]:
                face = "manic"
            # elif approval_check(self, threshold = "love"):
            #     face = "happy"
            else:
                face = "neutral"

            return face

        def travel(self):
            global Player

            global weather
            global snow_left

            if self.location != "hold":
                if self.behavior in ["training", "swimming"]:
                    self.destination = "bg_lockers"

                    if time_index < 3 and time_index not in self.schedule.keys():
                        if renpy.random.random() > 0.5:
                            self.schedule[time_index + 1] = ["bg_lockers", "showering"]
                        else:
                            self.schedule[time_index + 1] = ["bg_lockers", "changing"]
                elif time_index == 0 and self.location == Player.location and renpy.random.random() > 0.5:
                    self.destination = Player.location
                else:
                    possible_locations = []

                    possible_locations.append(self.home)

                    if time_index < 3 and weather != "rain":
                        possible_locations.append("bg_campus")

                    if time_index < 2 and weekday < 5:
                        possible_locations.append("bg_classroom")
                        possible_locations.append("bg_classroom")

                    if time_index < 3 and self.location != "bg_lockers" and not self.History.check("trained_with_Player", tracker = "daily"):
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

                    if day > 3:
                        if (self in Partners or self.status["nympho"] or approval_check(self, threshold = "love")) and renpy.random.random() > 0.85:
                            if (Player.location not in bedrooms or Player.location == Player.home) and (Player.location != "bg_shower_Player" or self.has_keys_to_Players_room):
                                possible_locations.append(Player.location)

                            if self.has_keys_to_Players_room:
                                possible_locations.append(Player.home)

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