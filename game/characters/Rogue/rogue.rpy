init -1:

    default Rogue = create_Rogue()
    
    define Rogue_color = "#2ca05aff"
    define ch_Rogue = Character("[Rogue.tag]")
    
    define Rogue_standing_anchor = [int(1260*character_sampling), int(1300*character_sampling)]
    define Rogue_standing_height = 0.25
    define Rogue_standing_zoom = 0.35*character_adjustment
    define Rogue_standing_neck_position = [int(1340*character_sampling), int(1370*character_sampling)]
    define Rogue_standing_left_breast_position = [int(1320*character_sampling), int(1855*character_sampling)]
    define Rogue_standing_right_breast_position = [int(1015*character_sampling), int(1840*character_sampling)]
    define Rogue_standing_left_nipple_position = [int(1320*character_sampling), int(1800*character_sampling)]
    define Rogue_standing_right_nipple_position = [int(970*character_sampling), int(1800*character_sampling)]
    define Rogue_standing_thigh_position = [int(1350*character_sampling), int(2930*character_sampling)]
    define Rogue_standing_thigh_higher_position = [int(1380*character_sampling), int(2640*character_sampling)]
    define Rogue_standing_ass_position = [int(1450*character_sampling), int(2500*character_sampling)]
    define Rogue_standing_pussy_position = [int(1225*character_sampling), int(2550*character_sampling)]

    define Rogue_masturbation_anchor = [int(2704*sex_sampling), int(1262*sex_sampling)]
    define Rogue_masturbation_height = 0.225
    define Rogue_masturbation_zoom = 0.32*sex_adjustment
    define Rogue_masturbation_neck_position = [int(2798*sex_sampling), int(1305*sex_sampling)]
    define Rogue_masturbation_left_breast_position = [int(3109*sex_sampling), int(1810*sex_sampling)]
    define Rogue_masturbation_right_breast_position = [int(2315*sex_sampling), int(1845*sex_sampling)]
    define Rogue_masturbation_left_nipple_position = [int(3120*sex_sampling), int(1716*sex_sampling)]
    define Rogue_masturbation_right_nipple_position = [int(2294*sex_sampling), int(1762*sex_sampling)]
    define Rogue_masturbation_pussy_position = [int(2476*sex_sampling), int(2470*sex_sampling)]
    define Rogue_masturbation_anus_position = [int(2465*sex_sampling), int(2908*sex_sampling)]

    define Rogue_hands_and_knees_anchor = [int(2176*sex_sampling), int(1849*sex_sampling)]
    define Rogue_hands_and_knees_height = 0.4
    define Rogue_hands_and_knees_zoom = 0.35*sex_adjustment

    define Rogue_missionary_anchor = [int(2316*sex_sampling), int(970*sex_sampling)]
    define Rogue_missionary_height = 0.08
    define Rogue_missionary_zoom = 0.35*sex_adjustment
    define Rogue_missionary_neck_position = [int(2900*sex_sampling), int(1300*sex_sampling)]
    define Rogue_missionary_left_breast_position = [int(2430*sex_sampling), int(1650*sex_sampling)]
    define Rogue_missionary_right_breast_position = [int(1765*sex_sampling), int(1525*sex_sampling)]
    define Rogue_missionary_left_nipple_position = [int(2500*sex_sampling), int(1590*sex_sampling)]
    define Rogue_missionary_right_nipple_position = [int(1723*sex_sampling), int(1460*sex_sampling)]
    define Rogue_missionary_pussy_position = [int(2015*sex_sampling), int(2778*sex_sampling)]
    define Rogue_missionary_anus_position = [int(2023*sex_sampling), int(2984*sex_sampling)]

    define Rogue_doggy_anchor = [int(1538*sex_sampling), int(944*sex_sampling)]
    define Rogue_doggy_height = 0.25
    define Rogue_doggy_zoom = 0.325*sex_adjustment
    define Rogue_doggy_pussy_position = [int(2108*sex_sampling), int(3205*sex_sampling)]
    define Rogue_doggy_anus_position = [int(2112*sex_sampling), int(2894*sex_sampling)]

    define Rogue_thresholds = {
        "talk_late": [0, 50],

        "temporary_follow": [0, 50],
        "follow": [0, 75],

        "friendship": [25, 50],
        "dating": [100, 100],
        "relationship": [250, 175],
        "love": [950, 950],

        "sleepover": [0, 0],

        "shirk_responsibilities": [0, 300],

        "polyamory": [900, 900],

        "see_bra": [0, 150],
        "give_bra": [425, 425],
        "see_underwear": [0, 175],
        "give_underwear": [525, 525],
        "see_breasts": [200, 200],
        "see_breasts_without_asking": [950, 950],
        "see_pussy": [375, 375],
        "see_pussy_without_asking": [950, 950],

        "change_Outfit": [100, 175],
        "change_in_public": [275, 275],

        "hookup": [130, 130],

        "massage": [125, 150],
        "kiss": [50, 50],
        "makeout": [130, 130],
        "spank": [825, 950],
        "choke": [825, 950],

        "touch_thighs_over_clothes": [150, 150],
        "touch_thighs_higher_over_clothes": [175, 175],
        "touch_thighs": [160, 160],
        "touch_thighs_higher": [185, 185],
        "touch_breasts_over_clothes": [175, 175],
        "touch_breasts": [210, 210],
        "pinch_nipples": [275, 275],
        "suck_nipples": [260, 260],
        "touch_pussy_over_clothes": [275, 275],
        "touch_pussy": [325, 325],
        "finger_pussy": [600, 550],
        "eat_pussy": [575, 575],
        "grab_ass_over_clothes": [150, 150],
        "grab_ass": [300, 300],
        "finger_ass": [615, 615],
        "eat_ass": [650, 650],

        "handjob": [225, 225],
        "fondle_balls": [375, 375],
        "blowjob": [350, 350],
        "suck_balls": [400, 400],
        "deepthroat": [650, 600],
        "titjob": [550, 550],
        "footjob": [760, 760],

        "striptease": [400, 400],
        "Rogue_touch_pussy": [525, 525],
        "Rogue_finger_ass": [525, 525],
        "Rogue_vibrator": [700, 700],
        "Rogue_dildo_pussy": [950, 950],
        "Rogue_dildo_ass": [950, 950],
        "jerk_off": [525, 525],
        
        "grind_pussy": [800, 775],
        "grind_ass": [750, 750],
        "sex": [950, 950],
        "anal": [875, 875],
        "vibrator": [700, 700],
        "dildo_pussy": [950, 950],
        "dildo_ass": [950, 950],
        "ass_to_mouth": [925, 925],
        "double_penetrate": [950, 950],
        
        "cumshot_belly": [400, 400],
        "cumshot_breasts": [410, 410],
        "cumshot_face": [420, 420],
        "cumshot_hair": [450, 450],
        "cumshot_back": [460, 460],
        "cumshot_ass": [470, 470],
        "cumshot_feet": [480, 480],

        "creampie": [950, 950],
        "anal_creampie": [900, 900],
        "cum_in_mouth": [600, 600],
        "cum_down_throat": [800, 800],

        "clean_cum": [0, 0],
        "swallow_cum": [675, 675],
        "wear_cum": [850, 850],

        "standing": [0, 0],
        "masturbation": [0, 0],
        "kneeling": [0, 0],
        "hands_and_knees": [0, 0],
        "missionary": [0, 0],
        "cowgirl": [0, 0],
        "doggy": [0, 0],
        "footjob": [0, 0],
        
        "lesbian": [850, 850],
        
        "exhibitionism": [1001, 1001],
        "rough_play": [825, 950],
        
        "send_underwear_pics": [225, 250],
        "send_nudes": [425, 450],
        
        "flirting_a": [0, 0],
        "flirting_b": [0, 0],
        "flirting_c": [0, 0],
        "flirting_d": [50, 50],
        "flirting_ea": [50, 50],
        "flirting_eb": [50, 50],
        "flirting_f": [0, 0],
        "flirting_g": [125, 125],
        "flirting_h": [125, 125],
        "flirting_i": [125, 125],
        "flirting_ja": [0, 150],
        "flirting_jb": [0, 175],
        "flirting_jc": [200, 200],
        "flirting_jd": [375, 375],
        "flirting_ka": [425, 425],
        "flirting_kb": [525, 525],
        "flirting_l": [0, 0],
        "flirting_ma": [210, 210],
        "flirting_mb": [300, 300],
        "flirting_mc": [325, 325],
        "flirting_na": [0, 0],
        "flirting_nb": [0, 0],
        "flirting_nc": [0, 0],
        "flirting_oa": [200, 200],
        "flirting_ob": [200, 200],
        "flirting_pa": [0, 0],
        "flirting_pb": [0, 0],
        "flirting_pc": [0, 0],
        "flirting_pd": [0, 0],
        "flirting_qa": [0, 0],
        "flirting_qb": [0, 0],
        "flirting_qc": [0, 0]}

    define Rogue_conditions = {
        "love": ["EventScheduler.Events['Rogue_I_love_you'].completed"],

        "sleepover": ["Rogue in Partners"],

        "see_bra": ["Rogue in Partners"],
        "give_bra": ["Rogue in Partners"],
        "see_underwear": ["Rogue in Partners"],
        "give_underwear": ["Rogue in Partners"],
        "see_breasts": ["Rogue in Partners"],
        "see_breasts_without_asking": ["Rogue in Partners"],
        "see_pussy": ["Rogue in Partners"],
        "see_pussy_without_asking": ["Rogue in Partners"],

        "change_Outfit": ["Rogue in Partners"],
        "change_in_public": ["Rogue in Partners"],

        "hookup": ["Rogue in Partners"],

        "spank": ["Rogue in Partners"],
        "choke": ["Rogue in Partners"],

        "touch_thighs": ["Rogue in Partners"],
        "touch_thighs_higher": ["Rogue in Partners"],
        "touch_breasts_over_clothes": ["Rogue in Partners"],
        "touch_breasts": ["Rogue in Partners"],
        "pinch_nipples": ["Rogue in Partners"],
        "suck_nipples": ["Rogue in Partners"],
        "touch_pussy_over_clothes": ["Rogue in Partners"],
        "touch_pussy": ["Rogue in Partners"],
        "finger_pussy": ["Rogue in Partners"],
        "eat_pussy": ["Rogue in Partners"],
        "grab_ass_over_clothes": ["Rogue in Partners"],
        "grab_ass": ["Rogue in Partners"],
        "finger_ass": ["Rogue in Partners"],
        "eat_ass": ["Rogue in Partners"],

        "handjob": ["Rogue in Partners"],
        "fondle_balls": ["Rogue in Partners"],
        "blowjob": ["Rogue in Partners"],
        "suck_balls": ["Rogue in Partners"],
        "deepthroat": ["Rogue in Partners"],
        "titjob": ["Rogue in Partners"],
        "footjob": ["Rogue in Partners"],

        "striptease": ["Rogue in Partners"],
        "Rogue_touch_pussy": ["Rogue in Partners"],
        "Rogue_finger_ass": ["Rogue in Partners"],
        "Rogue_vibrator": ["Rogue in Partners"],
        "Rogue_dildo_pussy": ["Rogue in Partners", "EventScheduler.Events['Rogue_first_sex'].completed"],
        "Rogue_dildo_ass": ["Rogue in Partners", "EventScheduler.Events['Rogue_first_sex'].completed"],
        "jerk_off": ["Rogue in Partners"],
        
        "grind_pussy": ["Rogue in Partners"],
        "grind_ass": ["Rogue in Partners"],
        "sex": ["Rogue in Partners", "EventScheduler.Events['Rogue_first_sex'].completed"],
        "anal": ["Rogue in Partners", "EventScheduler.Events['Rogue_first_sex'].completed"],
        "vibrator": ["Rogue in Partners"],
        "dildo_pussy": ["Rogue in Partners", "EventScheduler.Events['Rogue_first_sex'].completed"],
        "dildo_ass": ["Rogue in Partners", "EventScheduler.Events['Rogue_first_sex'].completed"],
        "ass_to_mouth": ["Rogue in Partners"],
        "double_penetrate": ["Rogue in Partners"],
        
        "cumshot_belly": ["Rogue in Partners"],
        "cumshot_breasts": ["Rogue in Partners"],
        "cumshot_face": ["Rogue in Partners"],
        "cumshot_hair": ["Rogue in Partners"],
        "cumshot_back": ["Rogue in Partners"],
        "cumshot_ass": ["Rogue in Partners"],
        "cumshot_feet": ["Rogue in Partners"],

        "creampie": ["Rogue in Partners"],
        "anal_creampie": ["Rogue in Partners"],
        "cum_in_mouth": ["Rogue in Partners"],
        "cum_down_throat": ["Rogue in Partners"],

        "clean_cum": ["Rogue in Partners"],
        "swallow_cum": ["Rogue in Partners"],
        "wear_cum": ["Rogue in Partners"],

        "kneeling": ["Rogue in Partners"],
        "hands_and_knees": ["Rogue in Partners"],
        "missionary": ["Rogue in Partners"],
        "cowgirl": ["Rogue in Partners"],
        "doggy": ["Rogue in Partners"],
        "footjob": ["Rogue in Partners"],
        
        "lesbian": ["Rogue in Partners"],
        
        "exhibitionism": ["Rogue in Partners"],
        "rough_play": ["Rogue in Partners"],
        
        "send_underwear_pics": ["Rogue in Partners"],
        "send_nudes": ["Rogue in Partners"],
        
        "flirting_ea": ["Rogue.History.check('kiss')"],
        "flirting_eb": ["Rogue.History.check('kiss')"],
        "flirting_h": ["Rogue in Partners"],
        "flirting_i": ["Rogue in Partners"],
        "flirting_ja": ["Rogue in Partners"],
        "flirting_jb": ["Rogue in Partners"],
        "flirting_jc": ["Rogue in Partners"],
        "flirting_jd": ["Rogue in Partners"],
        "flirting_ka": ["Rogue in Partners"],
        "flirting_kb": ["Rogue in Partners"],
        "flirting_l": ["Rogue.quirk"],
        "flirting_na": ["Rogue.quirk"],
        "flirting_nb": ["Rogue.quirk"],
        "flirting_nc": ["Rogue.quirk"],
        "flirting_ma": ["Rogue in Partners"],
        "flirting_mb": ["Rogue in Partners"],
        "flirting_mc": ["Rogue in Partners"],
        "flirting_oa": ["Rogue.History.check('kiss')"],
        "flirting_ob": ["Rogue.History.check('kiss')"],
        "flirting_pa": ["Rogue.quirk"],
        "flirting_pb": ["Rogue.quirk"],
        "flirting_pc": ["Rogue.quirk"],
        "flirting_pd": ["Rogue.quirk"],
        "flirting_qa": ["Rogue.quirk"],
        "flirting_qb": ["Rogue.quirk"],
        "flirting_qc": ["Rogue.quirk"],
        
        "sexy_gifts": ["Rogue in Partners"],
        
        "piercing": ["Rogue in Partners"],
        
        "sex_toy": ["Rogue in Partners"],
        
        "new_Outfit": ["Rogue in Partners"]}

    define Rogue_Outfit_shame = {
        "bra_exposed": 0,
        "breasts_exposed": 1000,
        "back_exposed": 0,
        "belly_exposed": 0,
        "thighs_exposed": 0,
        "underwear_exposed": 0,
        "ass_exposed": 1000,
        "pussy_exposed": 1000,
        "anus_exposed": 1000,
        "feet_exposed": 0,
        
        "bra_visible": 0,
        "breasts_visible": 1000,
        "back_visible": 0,
        "belly_visible": 0,
        "thighs_visible": 0,
        "underwear_visible": 0,
        "ass_visible": 1000,
        "pussy_visible": 1000,
        "anus_visible": 1000,
        "feet_visible": 0}

init -2 python:

    def create_Rogue():
        Rogue = CompanionClass("Rogue", voice = ch_Rogue)

        Rogue.full_name = "???"
        Rogue.public_name = "Rogue"
        Rogue.call_sign = "Rogue"

        Rogue.Player_petname = "hon'"
        Rogue.Player_petnames.append(Player.first_name)
        Rogue.Player_petnames.append(Rogue.Player_petname)

        Rogue.default_pubes = "bush"
        Rogue.pubes = Rogue.default_pubes
        Rogue.desired_pubes = Rogue.default_pubes

        Rogue.virgin = True

        Cast.append(Rogue.tag)
        Sprites.append(Rogue)

        all_Characters.append(Rogue)
        all_Companions.append(Rogue)
        Students.append(Rogue)

        ch1_Companions.append(Rogue)

        bedrooms.append(Rogue.home)

        return Rogue

    def Rogue_faces(face):
        blush = 0

        if face == "neutral":
            brows = "neutral"
            eyes = "neutral"
            mouth = "neutral"
        elif face == "angry1":
            brows = "furrowed"
            eyes = "neutral"
            mouth = "neutral"
        elif face == "angry2":
            brows = "furrowed"
            eyes = "neutral"
            mouth = "happy"
        elif face == "appalled1":
            brows = "furrowed"
            eyes = "wide"
            mouth = "neutral"
        elif face == "appalled2":
            brows = "furrowed"
            eyes = "wide"
            mouth = "open"
        elif face == "appalled3":
            brows = "furrowed"
            eyes = "wide"
            mouth = "agape"
        elif face == "confused1":
            brows = "cocked"
            eyes = "neutral"
            mouth = "neutral"
        elif face == "confused2":
            brows = "cocked"
            eyes = "wide"
            mouth = "neutral"
        elif face == "confused3":
            brows = "cocked"
            eyes = "wide"
            mouth = "agape"
        elif face == "devious":
            brows = "neutral"
            eyes = "squint"
            mouth = "smile"
        elif face == "furious":
            brows = "furrowed"
            eyes = "neutral"
            mouth = "frown"
        elif face == "grimace":
            brows = "furrowed"
            eyes = "closed"
            mouth = "lipbite"
        elif face == "happy":
            brows = "neutral"
            eyes = "neutral"
            mouth = "smile"
        elif face == "kiss1":
            brows = "worried"
            eyes = "closed"
            mouth = "kiss"
        elif face == "kiss2":
            brows = "neutral"
            eyes = "closed"
            mouth = "kiss"
        elif face == "manic":
            brows = "worried"
            eyes = "wide"
            mouth = "open"
            blush = 1
        elif face == "perplexed":
            brows = "cocked"
            eyes = "wide"
            mouth = "open"
        elif face == "pleased1":
            brows = "raised"
            eyes = "neutral"
            mouth = "smirk"
        elif face == "pleased2":
            brows = "raised"
            eyes = "wide"
            mouth = "smirk"
        elif face == "sad":
            brows = "worried"
            eyes = "neutral"
            mouth = "frown"
        elif face == "sexy":
            brows = "neutral"
            eyes = "sexy"
            mouth = "lipbite"
        elif face == "sly":
            brows = "neutral"
            eyes = "squint"
            mouth = "smirk"
        elif face == "smirk1":
            brows = "neutral"
            eyes = "neutral"
            mouth = "happy"
        elif face == "smirk2":
            brows = "neutral"
            eyes = "neutral"
            mouth = "smirk"
        elif face == "surprised1":
            brows = "raised"
            eyes = "neutral"
            mouth = "open"
        elif face == "surprised2":
            brows = "raised"
            eyes = "wide"
            mouth = "open"
        elif face == "surprised3":
            brows = "raised"
            eyes = "wide"
            mouth = "agape"
        elif face == "suspicious1":
            brows = "furrowed"
            eyes = "squint"
            mouth = "neutral"
        elif face == "suspicious2":
            brows = "furrowed"
            eyes = "squint"
            mouth = "frown"
        elif face == "wink":
            brows = "wink"
            eyes = "wink"
            mouth = "kiss"
        elif face == "worried1":
            brows = "worried"
            eyes = "neutral"
            mouth = "neutral"
        elif face == "worried2":
            brows = "worried"
            eyes = "wide"
            mouth = "neutral"
        elif face == "worried3":
            brows = "worried"
            eyes = "wide"
            mouth = "open"
        elif face == "worried4":
            brows = "worried"
            eyes = "wide"
            mouth = "agape"
        else:
            renpy.say(None, "Something went wrong with a face here.")

            return "neutral", "neutral", "neutral", 0

        return brows, eyes, mouth, blush

    def Rogue_arms(pose):
        if pose == "neutral":
            left_arm = "neutral"
            right_arm = "neutral"
        elif pose == "angry":
            left_arm = "fist"
            right_arm = "fist"
        elif pose == "bra":
            left_arm = "bra"
            right_arm = "bra"
        elif pose == "come_here":
            left_arm = "fight"
            right_arm = "extended"
        elif pose == "crossed":
            left_arm = "crossed"
            right_arm = "crossed"
        elif pose == "fight":
            left_arm = "fight"
            right_arm = "fight"
        elif pose == "hips":
            left_arm = "hip"
            right_arm = "hip"
        elif pose == "plug":
            left_arm = "touch_ass"
            right_arm = "fist"
        elif pose == "sass":
            left_arm = "hip"
            right_arm = "neutral"
        elif pose == "sheepish":
            left_arm = "rub_neck"
            right_arm = "extended"
        elif pose == "shrug":
            left_arm = "extended"
            right_arm = "extended"
        elif pose == "touch_Rogue":
            left_arm = "grope"
            right_arm = "touch_pussy"
        else:
            renpy.say(None, "Something went wrong with an arm pose here.")

            return "neutral", "neutral"

        return left_arm, right_arm

    def Rogue_locations():
        global Player
        
        global weekday
        global time_index

        global weather
        global snow_left
        
        possible_locations = []

        possible_locations.append(Rogue.home)

        if time_index < 3 and weather != "rain":
            possible_locations.append("bg_campus")

        if time_index < 2 and weekday < 5:
            possible_locations.append("bg_classroom")
            possible_locations.append("bg_classroom")

        if time_index < 3 and Rogue.location != "bg_lockers" and not Rogue.History.check("trained_with_Player", tracker = "daily"):
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
            if (Rogue in Partners or Rogue.status["nympho"] or approval_check(Rogue, threshold = "love")) and renpy.random.random() > 0.85:
                if (Player.location not in bedrooms or Player.location == Player.home) and (Player.location != "bg_shower_Player" or Rogue.has_keys_to_Players_room):
                    possible_locations.append(Player.location)

                if Rogue.has_keys_to_Players_room:
                    possible_locations.append(Player.home)

        return possible_locations

label update_Rogue:
    $ Rogue.sprite_anchor = Rogue_standing_anchor
    $ Rogue.sprite_position[1] = Rogue_standing_height
    $ Rogue.sprite_zoom = Rogue_standing_zoom

    return