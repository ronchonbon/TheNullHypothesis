init -3 python:

    class PlayerClass(object):
        def __init__(self, first_name, last_name, **properties):
            self.tag = "Player"

            self.first_name = first_name
            self.last_name = last_name
            self.full_name = first_name + " " + last_name
            self.call_sign = "Null"

            self.database = {}

            self.voice = properties.get("voice", None)

            self.powers = "Nullification"
            self.power = 0

            self.level = 1
            self.XP = 0
            self.XP_goal = 200
            self.stat_points = 0

            self.stat_modifier = 1.0

            self.scholarship = None
            self.has_family = True

            self.desire = 0

            self.stamina = 1
            self.max_stamina = 1

            self.electronic = False
            self.telepathic = False

            self.skin_color = properties.get("skin_color", "green")
            self.hair_color = properties.get("skin_color", "black")
            self.hair = properties.get("hair", 1)
            self.ears = properties.get("ears", "human")
            self.beard = properties.get("beard", 0)
            self.handedness = properties.get("handedness", "right")

            self.visible_mutation = False

            self.body_visible = True

            self.beards_unlocked = False

            self.background_color = "purple"

            self.phone_frame = 0
            self.phone_wallpaper = 1
            self.ringtone = 0

            self.attendance_bonus = False
            
            self.sweat = 0
            self.sweaty_threshold = 2
            
            self.chlorine = 0
            self.chlorinated_threshold = 2

            self.naked = False
            self.cock_out = False
            self.spunk = False
            self.saliva = False
            self.grool = False
            self.dirty_cock = False

            self.home = "bg_Player"
            self.destination = "hold"
            self.location = "hold"

            self.income = 10
            self.cash = 20
            self.total_cash = 20

            self.History = HistoryClass()

            self.Outfits = []

            self.Outfit_index = 0
            self.Outfit = None

            self.inventory = {}

            self.phone_cracked = False

            self.position = None
            self.Lovers = {}

            self.mouth_Actions = []
            self.right_hand_Actions = []
            self.left_hand_Actions = []
            self.cock_Actions = []
            self.balls_Actions = []
            self.all_Actions = []

            self.all_Organs = [
                "mouth",
                "right_hand",
                "left_hand",
                "cock",
                "balls"]

            self.orgasming = None

            self.behavior = None
            self.behavior_Partners = []
            
            self.schedule = {}
            self.date_planned = {}

            self.messy_bed = False
            self.clothes_on_floor = False

            self.scores = {}

            self.mutant_rank = None
            self.mutant_abilities = []
            self.ability_points = 0

            self.database_type = None

            self.temp = None

        def check_if_mutation_is_visible(self):
            Player.visible_mutation = False

            if self.skin_color in ["blue", "green", "red"]:
                Player.visible_mutation = True

            if self.ears in ["elf", "fin"]:
                Player.visible_mutation = True

            return