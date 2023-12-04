init -1:

    default Laura = create_Laura()
    
    define Laura_color = "#bca10a"
    define ch_Laura = Character("[Laura.tag]")

    define Laura_standing_anchor = [int(1220*character_sampling), int(1510*character_sampling)]
    define Laura_standing_height = 0.305
    define Laura_standing_zoom = 0.35*character_adjustment
    define Laura_standing_bottom = 0.959
    define Laura_standing_neck_position = [int(1305*character_sampling), int(1575*character_sampling)]
    define Laura_standing_left_breast_position = [int(1330*character_sampling), int(1980*character_sampling)]
    define Laura_standing_right_breast_position = [int(1040*character_sampling), int(1985*character_sampling)]
    define Laura_standing_left_nipple_position = [int(1335*character_sampling), int(1930*character_sampling)]
    define Laura_standing_right_nipple_position = [int(1000*character_sampling), int(1930*character_sampling)]
    define Laura_standing_thigh_position = [int(1090*character_sampling), int(3090*character_sampling)]
    define Laura_standing_thigh_higher_position = [int(1125*character_sampling), int(2880*character_sampling)]
    define Laura_standing_ass_position = [int(1450*character_sampling), int(2640*character_sampling)]
    define Laura_standing_pussy_position = [int(1215*character_sampling), int(2770*character_sampling)]

    define Laura_masturbation_anchor = [int(2704*sex_sampling), int(1262*sex_sampling)]
    define Laura_masturbation_height = 0.225
    define Laura_masturbation_zoom = 0.32*sex_adjustment
    define Laura_masturbation_neck_position = [int(2805*sex_sampling), int(1327*sex_sampling)]
    define Laura_masturbation_left_breast_position = [int(3050*sex_sampling), int(1788*sex_sampling)]
    define Laura_masturbation_right_breast_position = [int(2380*sex_sampling), int(1825*sex_sampling)]
    define Laura_masturbation_left_nipple_position = [int(3078*sex_sampling), int(1700*sex_sampling)]
    define Laura_masturbation_right_nipple_position = [int(2338*sex_sampling), int(1734*sex_sampling)]
    define Laura_masturbation_pussy_position = [int(2490*sex_sampling), int(2482*sex_sampling)]
    define Laura_masturbation_anus_position = [int(2478*sex_sampling), int(2899*sex_sampling)]

    define Laura_hands_and_knees_anchor = [int(2176*sex_sampling), int(1849*sex_sampling)]
    define Laura_hands_and_knees_height = 0.4
    define Laura_hands_and_knees_zoom = 0.35*sex_adjustment

    define Laura_missionary_anchor = [int(2316*sex_sampling), int(970*sex_sampling)]
    define Laura_missionary_height = 0.08
    define Laura_missionary_zoom = 0.35*sex_adjustment
    define Laura_missionary_neck_position = [int(2900*sex_sampling), int(1300*sex_sampling)]
    define Laura_missionary_left_breast_position = [int(2400*sex_sampling), int(1571*sex_sampling)]
    define Laura_missionary_right_breast_position = [int(1855*sex_sampling), int(1482*sex_sampling)]
    define Laura_missionary_left_nipple_position = [int(2462*sex_sampling), int(1482*sex_sampling)]
    define Laura_missionary_right_nipple_position = [int(1832*sex_sampling), int(1389*sex_sampling)]
    define Laura_missionary_pussy_position = [int(2019*sex_sampling), int(2795*sex_sampling)]
    define Laura_missionary_anus_position = [int(2033*sex_sampling), int(3013*sex_sampling)]

    define Laura_doggy_anchor = [int(1538*sex_sampling), int(944*sex_sampling)]
    define Laura_doggy_height = 0.25
    define Laura_doggy_zoom = 0.325*sex_adjustment
    define Laura_doggy_pussy_position = [int(2112*sex_sampling), int(3219*sex_sampling)]
    define Laura_doggy_anus_position = [int(2106*sex_sampling), int(2888*sex_sampling)]

    define Laura_thresholds = {
        "talk_late": [0, 100],

        "temporary_follow": [0, 100],
        "follow": [0, 115],

        "friendship": [50, 75],
        "dating": [75, 100],
        "relationship": [100, 150],
        "love": [775, 850],

        "sleepover": [0, 0],

        "shirk_responsibilities": [0, 100],

        "polyamory": [875, 950],

        "see_bra": [0, 75],
        "give_bra": [325, 350],
        "see_underwear": [0, 75],
        "give_underwear": [350, 475],
        "see_breasts": [125, 150],
        "see_breasts_without_asking": [1001, 1001],
        "see_pussy": [125, 175],
        "see_pussy_without_asking": [1001, 1001],

        "change_Outfit": [100, 200],
        "change_in_public": [275, 300],

        "hookup": [150, 200],

        "massage": [125, 225],
        "kiss": [75, 100],
        "makeout": [150, 200],
        "spank": [750, 775],
        "choke": [750, 775],

        "touch_thighs_over_clothes": [125, 150],
        "touch_thighs_higher_over_clothes": [125, 175],
        "touch_thighs": [125, 175],
        "touch_thighs_higher": [150, 200],
        "touch_breasts_over_clothes": [125, 175],
        "touch_breasts": [175, 225],
        "pinch_nipples": [275, 325],
        "suck_nipples": [275, 300],
        "touch_pussy_over_clothes": [150, 175],
        "touch_pussy": [500, 575],
        "finger_pussy": [550, 600],
        "eat_pussy": [575, 625],
        "grab_ass_over_clothes": [125, 150],
        "grab_ass": [150, 175],
        "finger_ass": [575, 625],
        "eat_ass": [625, 675],

        "handjob": [150, 225],
        "fondle_balls": [350, 400],
        "blowjob": [575, 625],
        "suck_balls": [600, 675],
        "deepthroat": [625, 725],
        "titjob": [750, 800],
        "footjob": [700, 775],

        "striptease": [175, 225],
        "self_touch_pussy": [250, 325],
        "self_finger_ass": [250, 325],
        "self_vibrator": [550, 625],
        "self_dildo_pussy": [750, 850],
        "self_dildo_ass": [875, 925],
        "jerk_off": [500, 575],
        
        "grind_pussy": [750, 825],
        "grind_ass": [825, 900],
        "sex": [850, 900],
        "anal": [875, 925],
        "vibrator": [550, 625],
        "dildo_pussy": [750, 850],
        "dildo_ass": [875, 925],
        "ass_to_mouth": [925, 950],
        "double_penetrate": [950, 950],
        
        "cumshot_belly": [400, 420],
        "cumshot_breasts": [420, 430],
        "cumshot_face": [400, 420],
        "cumshot_hair": [460, 470],
        "cumshot_back": [470, 525],
        "cumshot_ass": [490, 525],
        "cumshot_feet": [480, 490],

        "creampie": [925, 950],
        "anal_creampie": [925, 975],
        "cum_in_mouth": [600, 625],
        "cum_down_throat": [825, 850],

        "clean_cum": [0, 0],
        "swallow_cum": [650, 675],
        "wear_cum": [800, 825],

        "standing": [0, 0],
        "masturbation": [0, 0],
        "kneeling": [0, 0],
        "hands_and_knees": [0, 0],
        "missionary": [0, 0],
        "cowgirl": [0, 0],
        "doggy": [0, 0],
        "footjob": [0, 0],
        
        "lesbian": [900, 925],
        
        "exhibitionism": [1001, 1001],
        "rough_play": [750, 775],
        
        "send_underwear_pics": [150, 175],
        "send_nudes": [475, 400],
        
        "flirting_a": [0, 0],
        "flirting_b": [0, 0],
        "flirting_c": [0, 0],
        "flirting_d": [75, 100],
        "flirting_ea": [75, 100],
        "flirting_eb": [75, 100],
        "flirting_f": [0, 0],
        "flirting_g": [100, 150],
        "flirting_h": [100, 150],
        "flirting_i": [100, 150],
        "flirting_ja": [0, 150],
        "flirting_jb": [0, 150],
        "flirting_jc": [125, 150],
        "flirting_jd": [125, 175],
        "flirting_ka": [325, 350],
        "flirting_kb": [350, 475],
        "flirting_l": [175, 200],
        "flirting_ma": [175, 225],
        "flirting_mb": [150, 175],
        "flirting_mc": [500, 575],
        "flirting_na": [0, 0],
        "flirting_nb": [0, 0],
        "flirting_nc": [0, 0],
        "flirting_oa": [125, 150],
        "flirting_ob": [125, 150],
        "flirting_pa": [0, 0],
        "flirting_pb": [0, 0],
        "flirting_pc": [0, 0],
        "flirting_pd": [0, 0],
        "flirting_qa": [0, 0],
        "flirting_qb": [0, 0],
        "flirting_qc": [0, 0]}

    define Laura_conditions = {
        "love": ["EventScheduler.Events['Laura_I_love_you'].completed"],

        "sleepover": ["Laura in Partners"],

        "see_bra": ["Laura in Partners"],
        "give_bra": ["Laura in Partners"],
        "see_underwear": ["Laura in Partners"],
        "give_underwear": ["Laura in Partners"],
        "see_breasts": ["Laura in Partners"],
        "see_breasts_without_asking": ["Laura in Partners"],
        "see_pussy": ["Laura in Partners"],
        "see_pussy_without_asking": ["Laura in Partners"],

        "change_Outfit": ["Laura in Partners"],
        "change_in_public": ["Laura in Partners"],

        "hookup": ["Laura in Partners"],

        "spank": ["Laura in Partners"],
        "choke": ["Laura in Partners"],

        "touch_thighs": ["Laura in Partners"],
        "touch_thighs_higher": ["Laura in Partners"],
        "touch_breasts_over_clothes": ["Laura in Partners"],
        "touch_breasts": ["Laura in Partners"],
        "pinch_nipples": ["Laura in Partners"],
        "suck_nipples": ["Laura in Partners"],
        "touch_pussy_over_clothes": ["Laura in Partners"],
        "touch_pussy": ["Laura in Partners"],
        "finger_pussy": ["Laura in Partners"],
        "eat_pussy": ["Laura in Partners"],
        "grab_ass_over_clothes": ["Laura in Partners"],
        "grab_ass": ["Laura in Partners"],
        "finger_ass": ["Laura in Partners"],
        "eat_ass": ["Laura in Partners"],

        "handjob": ["Laura in Partners"],
        "fondle_balls": ["Laura in Partners"],
        "blowjob": ["Laura in Partners"],
        "suck_balls": ["Laura in Partners"],
        "deepthroat": ["Laura in Partners"],
        "titjob": ["Laura in Partners"],
        "footjob": ["Laura in Partners"],

        "striptease": ["Laura in Partners"],
        "self_touch_pussy": ["Laura in Partners"],
        "self_finger_ass": ["Laura in Partners"],
        "self_vibrator": ["Laura in Partners"],
        "self_dildo_pussy": ["Laura in Partners", "EventScheduler.Events['Laura_first_sex_part_two'].completed"],
        "self_dildo_ass": ["Laura in Partners", "EventScheduler.Events['Laura_first_sex_part_two'].completed"],
        "jerk_off": ["Laura in Partners"],
        
        "grind_pussy": ["Laura in Partners"],
        "grind_ass": ["Laura in Partners"],
        "sex": ["Laura in Partners", "EventScheduler.Events['Laura_first_sex_part_one'].completed"],
        "anal": ["Laura in Partners", "EventScheduler.Events['Laura_first_sex_part_two'].completed"],
        "vibrator": ["Laura in Partners"],
        "dildo_pussy": ["Laura in Partners", "EventScheduler.Events['Laura_first_sex_part_two'].completed"],
        "dildo_ass": ["Laura in Partners", "EventScheduler.Events['Laura_first_sex_part_two'].completed"],
        "ass_to_mouth": ["Laura in Partners"],
        "double_penetrate": ["Laura in Partners"],
        
        "cumshot_belly": ["Laura in Partners"],
        "cumshot_breasts": ["Laura in Partners"],
        "cumshot_face": ["Laura in Partners"],
        "cumshot_hair": ["Laura in Partners"],
        "cumshot_back": ["Laura in Partners"],
        "cumshot_ass": ["Laura in Partners"],
        "cumshot_feet": ["Laura in Partners"],

        "creampie": ["Laura in Partners"],
        "anal_creampie": ["Laura in Partners"],
        "cum_in_mouth": ["Laura in Partners"],
        "cum_down_throat": ["Laura in Partners"],

        "clean_cum": ["Laura in Partners"],
        "swallow_cum": ["Laura in Partners"],
        "wear_cum": ["Laura in Partners"],

        "kneeling": ["Laura in Partners"],
        "hands_and_knees": ["Laura in Partners"],
        "missionary": ["Laura in Partners"],
        "cowgirl": ["Laura in Partners"],
        "doggy": ["Laura in Partners"],
        "footjob": ["Laura in Partners"],
        
        "lesbian": ["Laura in Partners"],
        
        "exhibitionism": ["Laura in Partners"],
        "rough_play": ["Laura in Partners"],
        
        "send_underwear_pics": ["Laura in Partners"],
        "send_nudes": ["Laura in Partners"],
        
        "flirting_ea": ["Laura.History.check('kiss')"],
        "flirting_eb": ["Laura.History.check('kiss')"],
        "flirting_h": ["Laura in Partners"],
        "flirting_i": ["Laura in Partners"],
        "flirting_ja": ["Laura in Partners"],
        "flirting_jb": ["Laura in Partners"],
        "flirting_jc": ["Laura in Partners"],
        "flirting_jd": ["Laura in Partners"],
        "flirting_ka": ["Laura in Partners"],
        "flirting_kb": ["Laura in Partners"],
        "flirting_l": ["Laura.quirk"],
        "flirting_na": ["Laura.quirk"],
        "flirting_nb": ["Laura.quirk"],
        "flirting_nc": ["Laura.quirk"],
        "flirting_ma": ["Laura in Partners"],
        "flirting_mb": ["Laura in Partners"],
        "flirting_mc": ["Laura in Partners"],
        "flirting_oa": ["Laura.History.check('kiss')"],
        "flirting_ob": ["Laura.History.check('kiss')"],
        "flirting_pa": ["Laura.quirk"],
        "flirting_pb": ["Laura.quirk"],
        "flirting_pc": ["Laura.quirk"],
        "flirting_pd": ["Laura.quirk"],
        "flirting_qa": ["Laura.quirk"],
        "flirting_qb": ["Laura.quirk"],
        "flirting_qc": ["Laura.quirk"],
        
        "sexy_gifts": ["Laura in Partners"],
        
        "piercing": ["Laura in Partners"],
        
        "sex_toy": ["Laura in Partners"],
        
        "new_Outfit": ["Laura in Partners"]}

    define Laura_Outfit_shame = {
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

    define Laura_base_Action_desire = 10

    define Laura_Action_desires = {
        "spank": [0.1, 0.5, 1.0, 1.0, 0.5],

        "makeout": [0.2, 0.2, 0.2, 0.1, 0.05],
        "choke": [0.05, 0.1, 0.1, 0.1, 0.05],

        "touch_thighs_over_clothes": [0.8, 0.6, 0.2, 0.1, 0.0],
        "touch_thighs_higher_over_clothes": [0.8, 0.7, 0.3, 0.1, 0.0],
        "touch_thighs": [1.0, 0.8, 0.4, 0.2, 0.0],
        "touch_thighs_higher": [1.0, 0.9, 0.5, 0.2, 0.0],
        "touch_breasts_over_clothes": [0.8, 0.6, 0.3, 0.1, 0.0],
        "touch_breasts": [1.0, 0.8, 0.6, 0.2, 0.05],
        "pinch_nipples": [0.6, 1.0, 0.6, 0.3, 0.1],
        "suck_nipples": [0.8, 1.0, 0.8, 0.8, 0.2],
        "touch_pussy_over_clothes": [1.0, 0.6, 0.3, 0.3, 0.1],
        "touch_pussy": [1.0, 0.9, 0.8, 0.8, 0.8],
        "finger_pussy": [0.1, 0.4, 1.0, 0.8, 0.6],
        "eat_pussy": [0.2, 0.5, 1.0, 1.0, 1.0],
        "grab_ass_over_clothes": [0.8, 0.7, 0.3, 0.1, 0.0],
        "grab_ass": [1.0, 0.9, 0.5, 0.2, 0.0],
        "finger_ass": [0.05, 0.2, 0.4, 0.6, 0.8],
        "eat_ass": [0.05, 0.1, 0.2, 0.5, 1.0],
        
        "handjob": [0.2, 0.4, 0.4, 0.2, 0.0],
        "fondle_balls": [0.1, 0.2, 0.2, 0.1, 0.0],
        "blowjob": [0.3, 0.6, 0.6, 0.3, 0.0],
        "suck_balls": [0.2, 0.4, 0.4, 0.2, 0.0],
        "deepthroat": [0.4, 0.8, 0.8, 0.4, 0.0],
        "titjob": [0.3, 0.6, 0.6, 0.3, 0.0],
        "footjob": [0.2, 0.4, 0.4, 0.2, 0.0],

        "self_touch_pussy": [0.8, 0.7, 0.6, 0.6, 0.6],
        "self_finger_ass": [0.0, 0.1, 0.3, 0.5, 0.7],
        "self_vibrator": [0.5, 1.0, 1.0, 1.0, 1.0],
        "self_dildo_pussy": [0.1, 0.3, 0.7, 0.7, 0.7],
        "self_dildo_ass": [0.0, 0.0, 0.3, 0.5, 0.7],

        "jerk_off": [0.1, 0.2, 0.2, 0.1, 0.0],

        "grind_pussy": [0.3, 0.6, 0.6, 0.6, 0.6],
        "grind_ass": [0.3, 0.6, 0.6, 0.6, 0.6],
        "sex": [0.2, 0.4, 0.8, 0.8, 0.8],
        "anal": [0.0, 0.0, 0.4, 0.6, 0.8],
        
        "vibrator": [0.5, 1.0, 1.0, 1.0, 1.0],
        "dildo_pussy": [0.2, 0.4, 0.8, 0.8, 0.8],
        "dildo_ass": [0.0, 0.0, 0.4, 0.6, 0.8]}

    define Laura_Action_desire_thresholds = {
        "spank": 10,

        "makeout": 0,
        "choke": 10,

        "touch_thighs_over_clothes": 0,
        "touch_thighs_higher_over_clothes": 0,
        "touch_thighs": 0,
        "touch_thighs_higher": 0,
        "touch_breasts_over_clothes": 0,
        "touch_breasts": 0,
        "pinch_nipples": 10,
        "suck_nipples": 0,
        "touch_pussy_over_clothes": 0,
        "touch_pussy": 0,
        "finger_pussy": 20,
        "eat_pussy": 20,
        "grab_ass_over_clothes": 0,
        "grab_ass": 0,
        "finger_ass": 30,
        "eat_ass": 30,
        
        "handjob": 0,
        "fondle_balls": 0,
        "blowjob": 0,
        "suck_balls": 0,
        "deepthroat": 10,
        "titjob": 0,
        "footjob": 0,

        "self_touch_pussy": 0,
        "self_finger_ass": 30,
        "self_vibrator": 20,
        "self_dildo_pussy": 40,
        "self_dildo_ass": 50,

        "jerk_off": 0,

        "grind_pussy": 0,
        "grind_ass": 10,
        "sex": 40,
        "anal": 50,
        
        "vibrator": 20,
        "dildo_pussy": 40,
        "dildo_ass": 50}

init -2 python:

    def create_Laura():
        Laura = CompanionClass("Laura", voice = ch_Laura)

        Laura.full_name = "Laura Kinney"
        Laura.public_name = "X-23"
        Laura.call_sign = "X-23"

        Laura.Player_petname = Player.first_name
        Laura.Player_petnames.append(Player.first_name)
        Laura.Player_petnames.append("guy")

        Laura.default_pubes = "hairy"
        Laura.pubes = Laura.default_pubes
        Laura.desired_pubes = Laura.default_pubes

        Laura.left_claw = False
        Laura.right_claw = False
        Laura.unsheathing_claws = False
        Laura.sheathing_claws = False

        Laura.virgin = True

        Cast.append(Laura.tag)
        Sprites.append(Laura)

        all_Characters.append(Laura)
        all_Companions.append(Laura)
        Students.append(Laura)

        ch1_Companions.append(Laura)

        bedrooms.append(Laura.home)

        return Laura

    def Laura_faces(face):
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
            mouth = "happy"
        elif face == "appalled3":
            brows = "furrowed"
            eyes = "wide"
            mouth = "open"
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
            mouth = "open"
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
            mouth = "smile"
            blush = 1
        elif face == "perplexed":
            brows = "cocked"
            eyes = "wide"
            mouth = "neutral"
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
        elif face == "snarl":
            brows = "furrowed"
            eyes = "squint"
            mouth = "snarl"
        elif face == "surprised1":
            brows = "raised"
            eyes = "neutral"
            mouth = "neutral"
        elif face == "surprised2":
            brows = "raised"
            eyes = "wide"
            mouth = "neutral"
        elif face == "surprised3":
            brows = "raised"
            eyes = "wide"
            mouth = "open"
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
            mouth = "happy"
        elif face == "worried4":
            brows = "worried"
            eyes = "wide"
            mouth = "open"
        else:
            return "wrong", "wrong", "wrong", 0

            return "neutral", "neutral", "neutral", 0

        return brows, eyes, mouth, blush

    def Laura_arms(pose):
        if pose == "neutral":
            left_arm = "neutral"
            right_arm = "neutral"
        elif pose == "angry":
            left_arm = "fist"
            right_arm = "fist"
        elif pose == "bra":
            left_arm = "bra"
            right_arm = "bra"
        elif pose == "claws":
            left_arm = "claws"
            right_arm = "claws"
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
        elif pose == "shrug":
            left_arm = "extended"
            right_arm = "extended"
        elif pose == "sheepish":
            left_arm = "rub_neck"
            right_arm = "extended"
        elif pose == "touch_self":
            left_arm = "grope"
            right_arm = "touch_pussy"
        elif pose == "X":
            left_arm = "X"
            right_arm = "X"
        else:
            return "wrong", "wrong"

        return left_arm, right_arm

    def Laura_locations():
        possible_locations = []

        possible_locations.append(Laura.home)

        if time_index < 3 and weather != "rain":
            possible_locations.append("bg_campus")

        if time_index < 2 and weekday < 5:
            possible_locations.append("bg_classroom")
            possible_locations.append("bg_classroom")

        if time_index < 3 and Laura.location != "bg_lockers" and not Laura.History.check("trained_with_Player", tracker = "daily"):
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
            if (Laura in Partners or Laura.status["nympho"] or approval_check(Laura, threshold = "love")) and renpy.random.random() > 0.85:
                if (Player.location not in bedrooms or Player.location == Player.home) and (Player.location != "bg_shower_Player" or Laura.has_keys_to_Players_room):
                    possible_locations.append(Player.location)

                if Laura.has_keys_to_Players_room:
                    possible_locations.append(Player.home)

        return possible_locations

label update_Laura:
    $ Laura.sprite_anchor = Laura_standing_anchor
    $ Laura.sprite_position[1] = Laura_standing_height
    $ Laura.sprite_zoom = Laura_standing_zoom

    return

label Laura_unsheathes_claws(hand = "both"):
    pause 0.2

    if hand == "both":
        $ Laura.left_claw = True
        $ Laura.right_claw = True
    elif hand == "left":
        $ Laura.left_claw = True
    elif hand == "right":
        $ Laura.right_claw = True

    $ Laura.unsheathing_claws = True

    show expression "images/effects/snikt.webp" as snikt onlayer effects:
        anchor (0.5, 0.5) pos (0.675, 0.25)

        zoom 0.0
        alpha 0.0
        ease 0.1 zoom 0.5 alpha 1.0
        ease 2.0 alpha 0.0

    $ renpy.pause(0.1, hard = True)

    $ Laura.unsheathing_claws = False

    return

label Laura_sheathes_claws(hand = "both"):
    if hand == "both":
        $ Laura.left_claw = False
        $ Laura.right_claw = False
    elif hand == "left":
        $ Laura.left_claw = False
    elif hand == "right":
        $ Laura.right_claw = False

    $ Laura.sheathing_claws = True

    show expression "images/effects/snakt.webp" as snakt onlayer effects:
        anchor (0.5, 0.5) pos (0.675, 0.25)

        zoom 0.5
        alpha 0.0
        ease 0.01 alpha 1.0
        ease 0.5 zoom 0.0 alpha 0.0

    $ renpy.pause(0.51, hard = True)

    $ Laura.sheathing_claws = False

    pause 0.5
    
    return