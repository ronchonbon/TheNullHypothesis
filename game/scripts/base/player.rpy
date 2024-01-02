init -3 python:

    class PlayerClass(object):
        def __init__(self, first_name, last_name, **properties):
            self.tag = "Player"

            self.first_name = first_name
            self.last_name = last_name
            self.full_name = first_name + " " + last_name
            self.call_sign = "Null"

            self.voice = properties.get("voice", None)

            self.level = 1
            self.XP = 0
            self.XP_goal = 200
            self.stat_points = 0

            self.income = 10
            self.cash = 20
            self.total_cash = 20

            self.mutant_rank = None
            self.mutant_abilities = []
            self.ability_points = 0

            self.power = 0

            self.stamina = 1
            self.max_stamina = 1

            self.sweat = 0
            self.sweaty_threshold = 2
            
            self.chlorine = 0
            self.chlorinated_threshold = 2

            self.stat_modifier = 1.0

            self.date_planned = {}

            self.scholarship = None

            self.skin_color = properties.get("skin_color", "green")
            self.hair_color = properties.get("skin_color", "black")
            self.hair = properties.get("hair", 1)
            self.ears = properties.get("ears", "human")
            self.beard = properties.get("beard", 0)
            self.handedness = properties.get("handedness", "right")

            self.background_color = "purple"

            self.Outfits = []

            self.Outfit_index = 0
            self.Outfit = None

            self.phone_frame = 0
            self.phone_wallpaper = 1
            self.ringtone = 0

            self.desire = 0
            self.orgasming = None

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

            self.scores = {}

            self.schedule = {}
            self.behavior = None
            self.behavior_Partners = []

            self.inventory = {}
            
            self.History = HistoryClass()

            self.database = {}
            self.database_type = None

            self.home = "bg_Player"
            self.destination = "hold"
            self.location = "hold"

            self.traits = []

            self.temp = None

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

        def check_if_mutation_is_visible(self):
            if self.skin_color in ["blue", "green", "red"] or self.ears in ["elf", "fin"]:
                Player.give_trait("visible_mutation")
            else:
                Player.remove_trait("visible_mutation")

            return