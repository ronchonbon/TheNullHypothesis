init -1:
    
    default Jean = create_Jean()
    
    define Jean_color = "#d92912"
    define ch_Jean = Character("[Jean.tag]")
    
    define Jean_standing_anchor = [int(1260*character_sampling), int(1330*character_sampling)]
    define Jean_standing_height = 0.28
    define Jean_standing_zoom = 0.35*character_adjustment
    define Jean_standing_neck_position = [int(1310*character_sampling), int(1410*character_sampling)]
    define Jean_standing_left_breast_position = [int(1340*character_sampling), int(1840*character_sampling)]
    define Jean_standing_right_breast_position = [int(1020*character_sampling), int(1850*character_sampling)]
    define Jean_standing_left_nipple_position = [int(1340*character_sampling), int(1780*character_sampling)]
    define Jean_standing_right_nipple_position = [int(990*character_sampling), int(1790*character_sampling)]
    define Jean_standing_thigh_position = [int(1150*character_sampling), int(3040*character_sampling)]
    define Jean_standing_thigh_higher_position = [int(1075*character_sampling), int(2760*character_sampling)]
    define Jean_standing_ass_position = [int(1050*character_sampling), int(2600*character_sampling)]
    define Jean_standing_pussy_position = [int(1200*character_sampling), int(2680*character_sampling)]

    define Jean_masturbation_anchor = [int(2704*sex_sampling), int(1262*sex_sampling)]
    define Jean_masturbation_height = 0.225
    define Jean_masturbation_zoom = 0.32*sex_adjustment
    define Jean_masturbation_neck_position = [int(2794*sex_sampling), int(1360*sex_sampling)]
    define Jean_masturbation_left_breast_position = [int(3095*sex_sampling), int(1817*sex_sampling)]
    define Jean_masturbation_right_breast_position = [int(2304*sex_sampling), int(1864*sex_sampling)]
    define Jean_masturbation_left_nipple_position = [int(3113*sex_sampling), int(1739*sex_sampling)]
    define Jean_masturbation_right_nipple_position = [int(2284*sex_sampling), int(1788*sex_sampling)]
    define Jean_masturbation_pussy_position = [int(2480*sex_sampling), int(2474*sex_sampling)]
    define Jean_masturbation_anus_position = [int(2453*sex_sampling), int(2899*sex_sampling)]

    define Jean_hands_and_knees_anchor = [int(2176*sex_sampling), int(1849*sex_sampling)]
    define Jean_hands_and_knees_height = 0.4
    define Jean_hands_and_knees_zoom = 0.35*sex_adjustment

    define Jean_missionary_anchor = [int(2316*sex_sampling), int(970*sex_sampling)]
    define Jean_missionary_height = 0.08
    define Jean_missionary_zoom = 0.35*sex_adjustment
    define Jean_missionary_neck_position = [int(2900*sex_sampling), int(1300*sex_sampling)]
    define Jean_missionary_left_breast_position = [int(2394*sex_sampling), int(1664*sex_sampling)]
    define Jean_missionary_right_breast_position = [int(1792*sex_sampling), int(1584*sex_sampling)]
    define Jean_missionary_left_nipple_position = [int(2418*sex_sampling), int(1565*sex_sampling)]
    define Jean_missionary_right_nipple_position = [int(1763*sex_sampling), int(1513*sex_sampling)]
    define Jean_missionary_pussy_position = [int(2027*sex_sampling), int(2740*sex_sampling)]
    define Jean_missionary_anus_position = [int(2030*sex_sampling), int(3000*sex_sampling)]

    define Jean_doggy_anchor = [int(1538*sex_sampling), int(944*sex_sampling)]
    define Jean_doggy_height = 0.25
    define Jean_doggy_zoom = 0.325*sex_adjustment
    define Jean_doggy_pussy_position = [int(2113*sex_sampling), int(3181*sex_sampling)]
    define Jean_doggy_anus_position = [int(2111*sex_sampling), int(2904*sex_sampling)]

    define Jean_thresholds = {
        "talk_late": [150, 125],

        "temporary_follow": [0, 75],
        "follow": [0, 100],

        "friendship": [50, 25],
        "dating": [75, 50],
        "relationship": [125, 125],
        "love": [800, 775],

        "sleepover": [0, 0],

        "shirk_responsibilities": [0, 375],

        "polyamory": [900, 850],

        "see_bra": [0, 125],
        "give_bra": [450, 400],
        "see_underwear": [0, 175],
        "give_underwear": [550, 500],
        "see_breasts": [150, 125],
        "see_breasts_without_asking": [1001, 1001],
        "see_pussy": [375, 350],
        "see_pussy_without_asking": [1001, 1001],

        "change_Outfit": [115, 150],
        "change_in_public": [275, 250],

        "hookup": [130, 125],

        "massage": [125, 100],
        "kiss": [75, 50],
        "makeout": [130, 125],
        "spank": [925, 875],
        "choke": [925, 875],

        "touch_thighs_over_clothes": [150, 125],
        "touch_thighs_higher_over_clothes": [175, 150],
        "touch_thighs": [160, 140],
        "touch_thighs_higher": [185, 165],
        "touch_breasts_over_clothes": [175, 150],
        "touch_breasts": [215, 200],
        "pinch_nipples": [350, 325],
        "suck_nipples": [325, 300],
        "touch_pussy_over_clothes": [300, 275],
        "touch_pussy": [350, 325],
        "finger_pussy": [450, 425],
        "eat_pussy": [425, 400],
        "grab_ass_over_clothes": [150, 130],
        "grab_ass": [300, 275],
        "finger_ass": [650, 625],
        "eat_ass": [700, 675],

        "handjob": [225, 200],
        "fondle_balls": [400, 375],
        "blowjob": [575, 550],
        "suck_balls": [625, 600],
        "deepthroat": [775, 750],
        "titjob": [650, 625],
        "footjob": [800, 775],

        "striptease": [375, 350],
        "self_touch_pussy": [400, 375],
        "self_finger_ass": [400, 375],
        "self_vibrator": [650, 625],
        "self_dildo_pussy": [775, 750],
        "self_dildo_ass": [875, 850],
        "jerk_off": [475, 490],
        
        "grind_pussy": [675, 650],
        "grind_ass": [700, 675],
        "sex": [750, 725],
        "anal": [875, 850],
        "vibrator": [650, 625],
        "dildo_pussy": [775, 750],
        "dildo_ass": [875, 850],
        "ass_to_mouth": [925, 875],
        "double_penetrate": [900, 875],
        
        "cumshot_belly": [410, 400],
        "cumshot_breasts": [420, 410],
        "cumshot_face": [430, 420],
        "cumshot_hair": [460, 450],
        "cumshot_back": [470, 460],
        "cumshot_ass": [480, 470],
        "cumshot_feet": [490, 480],

        "creampie": [850, 825],
        "anal_creampie": [900, 875],
        "cum_in_mouth": [600, 575],
        "cum_down_throat": [825, 800],

        "clean_cum": [0, 0],
        "swallow_cum": [650, 625],
        "wear_cum": [825, 800],

        "standing": [0, 0],
        "masturbation": [0, 0],
        "kneeling": [0, 0],
        "hands_and_knees": [0, 0],
        "missionary": [0, 0],
        "cowgirl": [0, 0],
        "doggy": [0, 0],
        "footjob": [0, 0],
        
        "lesbian": [800, 775],
        
        "exhibitionism": [1001, 1001],
        "rough_play": [925, 875],
        
        "send_underwear_pics": [225, 200],
        "send_nudes": [425, 400],
        
        "flirting_a": [0, 0],
        "flirting_b": [0, 0],
        "flirting_c": [0, 0],
        "flirting_d": [75, 50],
        "flirting_ea": [75, 50],
        "flirting_eb": [75, 50],
        "flirting_f": [0, 0],
        "flirting_g": [125, 125],
        "flirting_h": [125, 125],
        "flirting_i": [125, 125],
        "flirting_ja": [0, 125],
        "flirting_jb": [0, 175],
        "flirting_jc": [150, 125],
        "flirting_jd": [375, 350],
        "flirting_ka": [450, 400],
        "flirting_kb": [550, 500],
        "flirting_l": [325, 300],
        "flirting_ma": [215, 200],
        "flirting_mb": [300, 275],
        "flirting_mc": [350, 325],
        "flirting_na": [0, 0],
        "flirting_nb": [0, 0],
        "flirting_nc": [0, 0],
        "flirting_oa": [150, 125],
        "flirting_ob": [150, 125],
        "flirting_pa": [0, 0],
        "flirting_pb": [0, 0],
        "flirting_pc": [0, 0],
        "flirting_pd": [0, 0],
        "flirting_qa": [0, 0],
        "flirting_qb": [0, 0],
        "flirting_qc": [0, 0]}

    define Jean_conditions = {
        "love": ["EventScheduler.Events['Jean_I_love_you'].completed"],

        "sleepover": ["Jean in Partners"],

        "see_bra": ["Jean in Partners"],
        "give_bra": ["Jean in Partners"],
        "see_underwear": ["Jean in Partners"],
        "give_underwear": ["Jean in Partners"],
        "see_breasts": ["Jean in Partners"],
        "see_breasts_without_asking": ["Jean in Partners"],
        "see_pussy": ["Jean in Partners"],
        "see_pussy_without_asking": ["Jean in Partners"],

        "change_Outfit": ["Jean in Partners"],
        "change_in_public": ["Jean in Partners"],

        "hookup": ["Jean in Partners"],

        "spank": ["Jean in Partners"],
        "choke": ["Jean in Partners"],

        "touch_thighs": ["Jean in Partners"],
        "touch_thighs_higher": ["Jean in Partners"],
        "touch_breasts_over_clothes": ["Jean in Partners"],
        "touch_breasts": ["Jean in Partners"],
        "pinch_nipples": ["Jean in Partners"],
        "suck_nipples": ["Jean in Partners"],
        "touch_pussy_over_clothes": ["Jean in Partners"],
        "touch_pussy": ["Jean in Partners"],
        "finger_pussy": ["Jean in Partners"],
        "eat_pussy": ["Jean in Partners"],
        "grab_ass_over_clothes": ["Jean in Partners"],
        "grab_ass": ["Jean in Partners"],
        "finger_ass": ["Jean in Partners"],
        "eat_ass": ["Jean in Partners"],

        "handjob": ["Jean in Partners"],
        "fondle_balls": ["Jean in Partners"],
        "blowjob": ["Jean in Partners"],
        "suck_balls": ["Jean in Partners"],
        "deepthroat": ["Jean in Partners"],
        "titjob": ["Jean in Partners"],
        "footjob": ["Jean in Partners"],

        "striptease": ["Jean in Partners"],
        "self_touch_pussy": ["Jean in Partners"],
        "self_finger_ass": ["Jean in Partners"],
        "self_vibrator": ["Jean in Partners"],
        "self_dildo_pussy": ["Jean in Partners", "EventScheduler.Events['Jean_first_sex_part_two'].completed"],
        "self_dildo_ass": ["Jean in Partners", "EventScheduler.Events['Jean_first_sex_part_two'].completed"],
        "jerk_off": ["Jean in Partners"],
        
        "grind_pussy": ["Jean in Partners"],
        "grind_ass": ["Jean in Partners"],
        "sex": ["Jean in Partners", "EventScheduler.Events['Jean_first_sex_part_one'].completed"],
        "anal": ["Jean in Partners", "EventScheduler.Events['Jean_first_sex_part_two'].completed"],
        "vibrator": ["Jean in Partners"],
        "dildo_pussy": ["Jean in Partners", "EventScheduler.Events['Jean_first_sex_part_two'].completed"],
        "dildo_ass": ["Jean in Partners", "EventScheduler.Events['Jean_first_sex_part_two'].completed"],
        "ass_to_mouth": ["Jean in Partners"],
        "double_penetrate": ["Jean in Partners"],
        
        "cumshot_belly": ["Jean in Partners"],
        "cumshot_breasts": ["Jean in Partners"],
        "cumshot_face": ["Jean in Partners"],
        "cumshot_hair": ["Jean in Partners"],
        "cumshot_back": ["Jean in Partners"],
        "cumshot_ass": ["Jean in Partners"],
        "cumshot_feet": ["Jean in Partners"],

        "creampie": ["Jean in Partners"],
        "anal_creampie": ["Jean in Partners"],
        "cum_in_mouth": ["Jean in Partners"],
        "cum_down_throat": ["Jean in Partners"],

        "clean_cum": ["Jean in Partners"],
        "swallow_cum": ["Jean in Partners"],
        "wear_cum": ["Jean in Partners"],

        "kneeling": ["Jean in Partners"],
        "hands_and_knees": ["Jean in Partners"],
        "missionary": ["Jean in Partners"],
        "cowgirl": ["Jean in Partners"],
        "doggy": ["Jean in Partners"],
        "footjob": ["Jean in Partners"],
        
        "lesbian": ["Jean in Partners"],
        
        "exhibitionism": ["Jean in Partners"],
        "rough_play": ["Jean in Partners"],
        
        "send_underwear_pics": ["Jean in Partners"],
        "send_nudes": ["Jean in Partners"],
        
        "flirting_ea": ["Jean.History.check('kiss')"],
        "flirting_eb": ["Jean.History.check('kiss')"],
        "flirting_h": ["Jean in Partners"],
        "flirting_i": ["Jean in Partners"],
        "flirting_ja": ["Jean in Partners"],
        "flirting_jb": ["Jean in Partners"],
        "flirting_jc": ["Jean in Partners"],
        "flirting_jd": ["Jean in Partners"],
        "flirting_ka": ["Jean in Partners"],
        "flirting_kb": ["Jean in Partners"],
        "flirting_l": ["Jean.quirk"],
        "flirting_na": ["Jean.quirk"],
        "flirting_nb": ["Jean.quirk"],
        "flirting_nc": ["Jean.quirk"],
        "flirting_ma": ["Jean in Partners"],
        "flirting_mb": ["Jean in Partners"],
        "flirting_mc": ["Jean in Partners"],
        "flirting_oa": ["Jean.History.check('kiss')"],
        "flirting_ob": ["Jean.History.check('kiss')"],
        "flirting_pa": ["Jean.quirk"],
        "flirting_pb": ["Jean.quirk"],
        "flirting_pc": ["Jean.quirk"],
        "flirting_pd": ["Jean.quirk"],
        "flirting_qa": ["Jean.quirk"],
        "flirting_qb": ["Jean.quirk"],
        "flirting_qc": ["Jean.quirk"],
        
        "sexy_gifts": ["Jean in Partners"],
        
        "piercing": ["Jean in Partners"],
        
        "sex_toy": ["Jean in Partners"],
        
        "new_Outfit": ["Jean in Partners"]}

    define Jean_Outfit_shame = {
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

    def create_Jean():
        Jean = CompanionClass("Jean", voice = ch_Jean)

        Jean.full_name = "Jean Grey"
        Jean.public_name = "Jean"
        Jean.call_sign = "Marvel Girl"

        Jean.Player_petname = Player.first_name
        Jean.Player_petnames.append(Player.first_name)

        Jean.default_pubes = "bush"
        Jean.pubes = Jean.default_pubes
        Jean.desired_pubes = Jean.default_pubes

        Jean.psychic = False
        Jean.activating_psychic = False
        Jean.deactivating_psychic = False

        Jean.Phoenix = False

        Jean.whiteboard = "chemistry"

        Jean.virgin = True

        Cast.append(Jean.tag)
        Sprites.append(Jean)

        all_Characters.append(Jean)
        all_Companions.append(Jean)
        Students.append(Jean)

        ch1_Companions.append(Jean)

        bedrooms.append(Jean.home)

        return Jean

label update_Jean:
    $ Jean.sprite_anchor = Jean_standing_anchor
    $ Jean.sprite_position[1] = Jean_standing_height
    $ Jean.sprite_zoom = Jean_standing_zoom

    return

label Jean_activate_psychic:
    $ Jean.psychic = True
    $ Jean.activating_psychic = True

    $ renpy.pause(0.2, hard = True)

    $ Jean.activating_psychic = False

    return

label Jean_deactivate_psychic:
    $ Jean.psychic = False
    $ Jean.deactivating_psychic = True

    $ renpy.pause(0.2, hard = True)

    $ Jean.deactivating_psychic = False

    return