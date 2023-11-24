init -2:
    
    define null_Clothing = ClothingClass(Owner = None, name = None, short_name = None, string = None, Clothing_type = None, shop_type = None, chapter = 0, season = 0, thresholds = {})

    define all_Clothing_types = ["makeup", "gag",
        "face_inner_accessory", "hair", "face_outer_accessory",
        "nipple_accessories", "bra", "underwear", "hose",
        "harness", "bodysuit",
        "socks", "pants", "skirt", "boots",
        "dress", "top",
        "neck", "gloves", "sleeves", "belt", "suspenders",
        "jacket", "towel", "cloak"]

    define removable_Clothing_types = ["makeup", "gag",
        "nipple_accessories", "underwear", "hose", "bra",
        "harness", "bodysuit",
        "socks", "pants", "skirt",
        "dress", "top",
        "neck", 
        "boots", "sleeves", "gloves", 
        "belt", "suspenders",
        "jacket", "towel", "cloak",
        "face_inner_accessory", "face_outer_accessory",]

    define upper_Clothing_types = ["bra", "bodysuit", "dress", "top", "jacket", "towel", "cloak"]
    define lower_Clothing_types = ["underwear", "hose", "socks", "pants", "skirt", "boots"]
    define accessory_Clothing_types = ["makeup", "gag", 
        "face_inner_accessory", "face_outer_accessory", 
        "nipple_accessories", 
        "harness",
        "neck", "gloves", "sleeves", "belt", "suspenders"]

    define bra_hiding_Clothing_types = ["dress", "top", "jacket", "towel"]
    define breasts_hiding_Clothing_types = ["bra", "bodysuit", "dress", "top", "jacket", "towel"]
    define underwear_hiding_Clothing_types = ["bodysuit", "pants", "skirt", "dress", "top", "belt", "jacket", "towel"]
    define ass_hiding_Clothing_types = ["underwear", "bodysuit", "hose", "pants", "skirt", "dress", "belt"]
    define pussy_hiding_Clothing_types = ["underwear", "bodysuit", "hose", "pants", "skirt", "dress", "belt"]
    define anus_hiding_Clothing_types = ["underwear", "bodysuit", "hose", "pants", "skirt", "dress", "belt"]

init -3 python:

    class ClothingClass(object):
        def __init__(self, Owner, name, short_name, string, Clothing_type, shop_type, chapter, season, thresholds, **properties):
            self.Owner = Owner

            self.name = name
            self.short_name = short_name
            self.string = string

            self.Clothing_type = Clothing_type
            
            self.shop_type = shop_type
            self.chapter = chapter
            self.season = season

            self.thresholds = thresholds

            self.price = properties.get("price", 0)

            self.shame = properties.get("shame", [0, 0])

            self.available_states = properties.get("available_states", {"standing": []})
            self.undressed_states = properties.get("undressed_states", {"standing": []})

            self.covers = properties.get("covers", {"standing": {}})
            self.hides = properties.get("hides", {"standing": {}})

            self.blocked_by = properties.get("blocked_by", {})
            self.covered_by = properties.get("covered_by", {})

            self.supports_breasts = properties.get("supports_breasts", False)

            self.incompatibilities = properties.get("incompatibilities", [])

            self.poses = list(self.available_states.keys())

            self.state = 0
            self.state_index = 0
            self.selected_state = 0

            self.covered = False
            self.blocked = False

            self.soiled = False

            self.gift = False

    class OutfitClass(object):
        def __init__(self, name, **properties):
            self.name = name

            self.wear_in_public = properties.get("wear_in_public", False)
            self.wear_in_private = properties.get("wear_in_private", False)

            self.daywear = properties.get("daywear", False)
            self.activewear = properties.get("activewear", False)
            self.superwear = properties.get("superwear", False)
            self.swimwear = properties.get("swimwear", False)
            self.datewear = properties.get("datewear", False)
            self.sexwear = properties.get("sexwear", False)
            self.sleepwear = properties.get("sleepwear", False)

            self.winterwear = properties.get("winterwear", False)

            self.shame = 0

            self.Outfit_type = "default"
            self.color = "yellow"

            self.disabled = False

            self.Clothes = {}

            for Clothing_type in all_Clothing_types:
                self.Clothes[Clothing_type] = null_Clothing

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

    class WardrobeClass(object):
        def __init__(self):
            self.Clothes = {}

            self.Outfits = {}

            self.outdoor_Outfit = OutfitClass("null")
            self.indoor_Outfit = OutfitClass("null")

            self.private_Outfit = OutfitClass("null")

            self.gym_Outfit = OutfitClass("null")
            self.superhero_Outfit = OutfitClass("null")
            self.swimming_Outfit = OutfitClass("null")
            self.date_Outfit = OutfitClass("null")
            self.sex_Outfit = OutfitClass("null")
            self.sleeping_Outfit = OutfitClass("null")

        def add_Clothing(self, Clothing):
            if Clothing.name not in self.Clothes.keys():
                self.Clothes[Clothing.name] = Clothing

            return

        def add_Outfit(self, Outfit):
            if Outfit not in self.Outfits.values():
                self.Outfits[Outfit.name] = Outfit

            return

        def remove_Outfit(self, name):
            del self.Outfits[name]

            return

        def choose_Outfits(self):
            global temperature
            global weather

            public_Outfits = []
            private_Outfits = []
            
            day_Outfits = []
            gym_Outfits = []
            superhero_Outfits = []
            swimming_Outfits = []
            date_Outfits = []
            sex_Outfits = []
            sleeping_Outfits = []

            for O in self.Outfits.values():
                if not O.disabled:
                    if O.wear_in_public:
                        if temperature[1] >= 10:
                            if not O.winterwear and "Winter" not in O.name:
                                public_Outfits.append(O)
                        else:
                            if O.winterwear:
                                public_Outfits.append(O)

                    if O.wear_in_private:
                        private_Outfits.append(O)

                    if O.daywear:
                        if temperature[0] >= 10:
                            if not O.winterwear and "Winter" not in O.name:
                                day_Outfits.append(O)
                        else:
                            day_Outfits.append(O)

                    if O.activewear:
                        if temperature[0] >= 10:
                            if not O.winterwear and "Winter" not in O.name:
                                gym_Outfits.append(O)
                        else:
                            gym_Outfits.append(O)

                    if O.superwear:
                        if temperature[0] >= 10:
                            if not O.winterwear and "Winter" not in O.name:
                                superhero_Outfits.append(O)
                        else:
                            superhero_Outfits.append(O)

                    if O.swimwear:
                        if temperature[0] >= 10:
                            if not O.winterwear and "Winter" not in O.name:
                                swimming_Outfits.append(O)
                        else:
                            swimming_Outfits.append(O)

                    if O.datewear:
                        if temperature[0] >= 10:
                            if not O.winterwear and "Winter" not in O.name:
                                date_Outfits.append(O)
                        else:
                            date_Outfits.append(O)
                    
                    if O.sexwear:
                        sex_Outfits.append(O)

                    if O.sleepwear:
                        if temperature[0] >= 10:
                            if not O.winterwear and "Winter" not in O.name:
                                sleeping_Outfits.append(O)
                        else:
                            sleeping_Outfits.append(O)

            if not public_Outfits:
                public_Outfits.append(self.Outfits["Casual 1"])

            self.outdoor_Outfit = renpy.random.choice(public_Outfits) if public_Outfits else OutfitClass("null")

            if self.outdoor_Outfit.winterwear:
                Outfit_name = self.outdoor_Outfit.name.replace(" (Outdoor)", " (Indoor)")

                if Outfit_name in self.Outfits.keys():
                    self.indoor_Outfit = self.Outfits[Outfit_name]
                else:
                    self.indoor_Outfit = self.outdoor_Outfit
            else:
                self.indoor_Outfit = self.outdoor_Outfit

            if self.indoor_Outfit in date_Outfits:
                date_Outfits.remove(self.indoor_Outfit)

            self.private_Outfit = renpy.random.choice(private_Outfits) if private_Outfits else self.indoor_Outfit
            
            self.gym_Outfit = renpy.random.choice(gym_Outfits) if gym_Outfits else self.indoor_Outfit
            self.superhero_Outfit = renpy.random.choice(superhero_Outfits) if superhero_Outfits else self.indoor_Outfit
            self.swimming_Outfit = renpy.random.choice(swimming_Outfits) if swimming_Outfits else self.indoor_Outfit
            self.date_Outfit = renpy.random.choice(date_Outfits) if date_Outfits else self.indoor_Outfit
            self.sex_Outfit = renpy.random.choice(sex_Outfits) if sex_Outfits else self.private_Outfit
            self.sleeping_Outfit = renpy.random.choice(sleeping_Outfits) if sleeping_Outfits else self.private_Outfit

            return

        def replace_disabled_Outfits(self):
            public_Outfits = []
            private_Outfits = []
            
            day_Outfits = []
            gym_Outfits = []
            superhero_Outfits = []
            swimming_Outfits = []
            date_Outfits = []
            sex_Outfits = []
            sleeping_Outfits = []

            for O in self.Outfits.values():
                if not O.disabled:
                    if O.wear_in_public:
                        if temperature[1] >= 10:
                            if not O.winterwear and "Winter" not in O.name:
                                public_Outfits.append(O)
                        else:
                            if O.winterwear:
                                public_Outfits.append(O)

                    if O.wear_in_private:
                        private_Outfits.append(O)

                    if O.daywear:
                        if temperature[0] >= 10:
                            if not O.winterwear and "Winter" not in O.name:
                                day_Outfits.append(O)
                        else:
                            day_Outfits.append(O)

                    if O.activewear:
                        if temperature[0] >= 10:
                            if not O.winterwear and "Winter" not in O.name:
                                gym_Outfits.append(O)
                        else:
                            gym_Outfits.append(O)

                    if O.superwear:
                        if temperature[0] >= 10:
                            if not O.winterwear and "Winter" not in O.name:
                                superhero_Outfits.append(O)
                        else:
                            superhero_Outfits.append(O)

                    if O.swimwear:
                        if temperature[0] >= 10:
                            if not O.winterwear and "Winter" not in O.name:
                                swimming_Outfits.append(O)
                        else:
                            swimming_Outfits.append(O)

                    if O.datewear:
                        if temperature[0] >= 10:
                            if not O.winterwear and "Winter" not in O.name:
                                date_Outfits.append(O)
                        else:
                            date_Outfits.append(O)
                    
                    if O.sexwear:
                        sex_Outfits.append(O)

                    if O.sleepwear:
                        if temperature[0] >= 10:
                            if not O.winterwear and "Winter" not in O.name:
                                sleeping_Outfits.append(O)
                        else:
                            sleeping_Outfits.append(O)

            if not public_Outfits:
                public_Outfits.append(self.Outfits["Casual 1"])

            if self.outdoor_Outfit.disabled or self.indoor_Outfit.disabled:
                self.outdoor_Outfit = renpy.random.choice(public_Outfits) if public_Outfits else OutfitClass("null")

                if self.outdoor_Outfit.winterwear:
                    Outfit_name = self.outdoor_Outfit.name.replace(" (Outdoor)", " (Indoor)")

                    if Outfit_name in self.Outfits.keys():
                        self.indoor_Outfit = self.Outfits[Outfit_name]
                    else:
                        self.indoor_Outfit = self.outdoor_Outfit
                else:
                    self.indoor_Outfit = self.outdoor_Outfit

            if self.indoor_Outfit in date_Outfits:
                date_Outfits.remove(self.indoor_Outfit)

            if self.private_Outfit.disabled:
                self.private_Outfit = renpy.random.choice(private_Outfits) if private_Outfits else self.indoor_Outfit
            
            if self.gym_Outfit.disabled:
                self.gym_Outfit = renpy.random.choice(gym_Outfits) if gym_Outfits else self.indoor_Outfit

            if self.swimming_Outfit.disabled:
                self.swimming_Outfit = renpy.random.choice(swimming_Outfits) if swimming_Outfits else self.indoor_Outfit
            
            if self.superhero_Outfit.disabled:
                self.superhero_Outfit = renpy.random.choice(superhero_Outfits) if superhero_Outfits else self.indoor_Outfit

            if self.date_Outfit.disabled:
                self.date_Outfit = renpy.random.choice(date_Outfits) if date_Outfits else self.indoor_Outfit

            if self.sex_Outfit.disabled:
                self.sex_Outfit = renpy.random.choice(sex_Outfits) if sex_Outfits else self.private_Outfit

            if self.sleeping_Outfit.disabled:
                self.sleeping_Outfit = renpy.random.choice(sleeping_Outfits) if sleeping_Outfits else self.private_Outfit

            return