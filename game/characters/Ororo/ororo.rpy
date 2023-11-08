init -1:
    
    default Ororo = create_Ororo()

    define Ororo_color = "#4e6364"
    define ch_Ororo = Character("[Ororo.tag]")

    define Ororo_standing_anchor = [int(837*character_sampling), int(856*character_sampling)]
    define Ororo_standing_height = 0.2
    define Ororo_standing_zoom = 0.34*character_adjustment

    define Ororo_thresholds = {
        "talk_late": [1000, 1000],

        "temporary_follow": [1000, 1000],
        "follow": [1000, 1000],

        "friendship": [1000, 1000],
        "dating": [1000, 1000],
        "relationship": [1000, 1000],
        "love": [1000, 1000],

        "sleepover": [0, 0],

        "shirk_responsibilities": [1000, 1000],

        "polyamory": [1000, 1000],

        "see_bra": [1000, 1000],
        "give_bra": [1000, 1000],
        "see_underwear": [1000, 1000],
        "give_underwear": [1000, 1000],
        "see_breasts": [1000, 1000],
        "see_pussy": [1000, 1000],

        "change_Outfit": [1000, 1000],
        "change_in_public": [1000, 1000],

        "hookup": [1000, 1000],

        "massage": [1000, 1000],
        "kiss": [1000, 1000],
        "makeout": [1000, 1000],
        "spank": [1000, 1000],
        "choke": [1000, 1000],

        "touch_thighs_over_clothes": [1000, 1000],
        "touch_thighs_higher_over_clothes": [1000, 1000],
        "touch_thighs": [1000, 1000],
        "touch_thighs_higher": [1000, 1000],
        "touch_breasts_over_clothes": [1000, 1000],
        "touch_breasts": [1000, 1000],
        "pinch_nipples": [1000, 1000],
        "suck_nipples": [1000, 1000],
        "touch_pussy_over_clothes": [1000, 1000],
        "touch_pussy": [1000, 1000],
        "finger_pussy": [1000, 1000],
        "eat_pussy": [1000, 1000],
        "grab_ass_over_clothes": [1000, 1000],
        "grab_ass": [1000, 1000],
        "finger_ass": [1000, 1000],
        "eat_ass": [1000, 1000],

        "handjob": [1000, 1000],
        "fondle_balls": [1000, 1000],
        "blowjob": [1000, 1000],
        "suck_balls": [1000, 1000],
        "deepthroat": [1000, 1000],
        "titjob": [1000, 1000],
        "footjob": [1000, 1000],

        "striptease": [1000, 1000],
        "self_touch_pussy": [1000, 1000],
        "self_finger_ass": [1000, 1000],
        "self_vibrator": [1000, 1000],
        "self_dildo_pussy": [1000, 1000],
        "self_dildo_ass": [1000, 1000],
        "jerk_off": [1000, 1000],
        
        "grind_pussy": [1000, 1000],
        "grind_ass": [1000, 1000],
        "sex": [1000, 1000],
        "anal": [1000, 1000],
        "vibrator": [1000, 1000],
        "dildo_pussy": [1000, 1000],
        "dildo_ass": [1000, 1000],
        "ass_to_mouth": [1000, 1000],
        "double_penetrate": [1000, 1000],

        "choke": [1000, 1000],
        
        "cumshot_belly": [1000, 1000],
        "cumshot_breasts": [1000, 1000],
        "cumshot_face": [1000, 1000],
        "cumshot_hair": [1000, 1000],
        "cumshot_back": [1000, 1000],
        "cumshot_ass": [1000, 1000],
        "cumshot_feet": [1000, 1000],

        "creampie": [1000, 1000],
        "anal_creampie": [1000, 1000],
        "cum_in_mouth": [1000, 1000],
        "cum_down_throat": [1000, 1000],

        "clean_cum": [1000, 1000],
        "swallow_cum": [1000, 1000],
        "wear_cum": [1000, 1000],

        "standing": [1000, 1000],
        "masturbation": [1000, 1000],
        "kneeling": [1000, 1000],
        "hands_and_knees": [1000, 1000],
        "missionary": [1000, 1000],
        "cowgirl": [1000, 1000],
        "doggy": [1000, 1000],
        "footjob": [1000, 1000],
        
        "lesbian": [1000, 1000],
        
        "exhibitionism": [1001, 1001],
        "rough_play": [1000, 1000],
        
        "send_underwear_pics": [1000, 1000],
        "send_nudes": [1000, 1000],
        
        "flirting_a": [0, 0],
        "flirting_b": [0, 0],
        "flirting_c": [0, 0],
        "flirting_d": [0, 0],
        "flirting_ea": [0, 0],
        "flirting_eb": [0, 0],
        "flirting_f": [0, 0],
        "flirting_g": [0, 0],
        "flirting_h": [0, 0],
        "flirting_i": [0, 0],
        "flirting_ja": [0, 0],
        "flirting_jb": [0, 0],
        "flirting_jc": [0, 0],
        "flirting_jd": [0, 0],
        "flirting_ka": [0, 0],
        "flirting_kb": [0, 0],
        "flirting_l": [0, 0],
        "flirting_ma": [0, 0],
        "flirting_mb": [0, 0],
        "flirting_mc": [0, 0],
        "flirting_na": [0, 0],
        "flirting_nb": [0, 0],
        "flirting_nc": [0, 0],
        "flirting_oa": [0, 0],
        "flirting_ob": [0, 0],
        "flirting_pa": [0, 0],
        "flirting_pb": [0, 0],
        "flirting_pc": [0, 0],
        "flirting_pd": [0, 0],
        "flirting_qa": [0, 0],
        "flirting_qb": [0, 0],
        "flirting_qc": [0, 0]}

    define Ororo_conditions = {
        "sleepover": ["Ororo in Partners"],

        "see_bra": ["Ororo in Partners"],
        "give_bra": ["Ororo in Partners"],
        "see_underwear": ["Ororo in Partners"],
        "give_underwear": ["Ororo in Partners"],
        "see_breasts": ["Ororo in Partners"],
        "see_breasts_without_asking": ["Ororo in Partners"],
        "see_pussy": ["Ororo in Partners"],
        "see_pussy_without_asking": ["Ororo in Partners"],

        "change_Outfit": ["Ororo in Partners"],
        "change_in_public": ["Ororo in Partners"],

        "hookup": ["Ororo in Partners"],

        "spank": ["Ororo in Partners"],
        "choke": ["Ororo in Partners"],

        "touch_thighs": ["Ororo in Partners"],
        "touch_thighs_higher": ["Ororo in Partners"],
        "touch_breasts_over_clothes": ["Ororo in Partners"],
        "touch_breasts": ["Ororo in Partners"],
        "pinch_nipples": ["Ororo in Partners"],
        "suck_nipples": ["Ororo in Partners"],
        "touch_pussy_over_clothes": ["Ororo in Partners"],
        "touch_pussy": ["Ororo in Partners"],
        "finger_pussy": ["Ororo in Partners"],
        "eat_pussy": ["Ororo in Partners"],
        "grab_ass_over_clothes": ["Ororo in Partners"],
        "grab_ass": ["Ororo in Partners"],
        "finger_ass": ["Ororo in Partners"],
        "eat_ass": ["Ororo in Partners"],

        "handjob": ["Ororo in Partners"],
        "fondle_balls": ["Ororo in Partners"],
        "blowjob": ["Ororo in Partners"],
        "suck_balls": ["Ororo in Partners"],
        "deepthroat": ["Ororo in Partners"],
        "titjob": ["Ororo in Partners"],
        "footjob": ["Ororo in Partners"],

        "striptease": ["Ororo in Partners"],
        "self_touch_pussy": ["Ororo in Partners"],
        "self_finger_ass": ["Ororo in Partners"],
        "self_vibrator": ["Ororo in Partners"],
        "self_dildo_pussy": ["Ororo in Partners", "EventScheduler.Events['Ororo_first_sex'].completed"],
        "self_dildo_ass": ["Ororo in Partners", "EventScheduler.Events['Ororo_first_sex'].completed"],
        "jerk_off": ["Ororo in Partners"],
        
        "grind_pussy": ["Ororo in Partners"],
        "grind_ass": ["Ororo in Partners"],
        "sex": ["Ororo in Partners", "EventScheduler.Events['Ororo_first_sex'].completed"],
        "anal": ["Ororo in Partners", "EventScheduler.Events['Ororo_first_sex'].completed"],
        "vibrator": ["Ororo in Partners"],
        "dildo_pussy": ["Ororo in Partners", "EventScheduler.Events['Ororo_first_sex'].completed"],
        "dildo_ass": ["Ororo in Partners", "EventScheduler.Events['Ororo_first_sex'].completed"],
        "ass_to_mouth": ["Ororo in Partners"],
        "double_penetrate": ["Ororo in Partners"],
        
        "cumshot_belly": ["Ororo in Partners"],
        "cumshot_breasts": ["Ororo in Partners"],
        "cumshot_face": ["Ororo in Partners"],
        "cumshot_hair": ["Ororo in Partners"],
        "cumshot_back": ["Ororo in Partners"],
        "cumshot_ass": ["Ororo in Partners"],
        "cumshot_feet": ["Ororo in Partners"],

        "creampie": ["Ororo in Partners"],
        "anal_creampie": ["Ororo in Partners"],
        "cum_in_mouth": ["Ororo in Partners"],
        "cum_down_throat": ["Ororo in Partners"],

        "clean_cum": ["Ororo in Partners"],
        "swallow_cum": ["Ororo in Partners"],
        "wear_cum": ["Ororo in Partners"],

        "kneeling": ["Ororo in Partners"],
        "hands_and_knees": ["Ororo in Partners"],
        "missionary": ["Ororo in Partners"],
        "cowgirl": ["Ororo in Partners"],
        "doggy": ["Ororo in Partners"],
        "footjob": ["Ororo in Partners"],
        
        "lesbian": ["Ororo in Partners"],
        
        "exhibitionism": ["Ororo in Partners"],
        "rough_play": ["Ororo in Partners"],
        
        "send_underwear_pics": ["Ororo in Partners"],
        "send_nudes": ["Ororo in Partners"],
        
        "flirting_l": ["False"],
        "flirting_na": ["False"],
        "flirting_nb": ["False"],
        "flirting_nc": ["False"],
        "flirting_pa": ["False"],
        "flirting_pb": ["False"],
        "flirting_pc": ["False"],
        "flirting_pd": ["False"],
        "flirting_qa": ["False"],
        "flirting_qb": ["False"],
        "flirting_qc": ["False"],
        
        "sexy_gifts": ["Ororo in Partners"],
        
        "piercing": ["Ororo in Partners"],
        
        "sex_toy": ["Ororo in Partners"],
        
        "new_Outfit": ["Ororo in Partners"]}

    define Ororo_Outfit_shame = {
        "bra_exposed": 0,
        "breasts_exposed": 0,
        "back_exposed": 0,
        "belly_exposed": 0,
        "thighs_exposed": 0,
        "underwear_exposed": 0,
        "ass_exposed": 0,
        "pussy_exposed": 0,
        "anus_exposed": 0,
        "feet_exposed": 0,
        
        "bra_visible": 0,
        "breasts_visible": 0,
        "back_visible": 0,
        "belly_visible": 0,
        "thighs_visible": 0,
        "underwear_visible": 0,
        "ass_visible": 0,
        "pussy_visible": 0,
        "anus_visible": 0,
        "feet_visible": 0}

init -2 python:

    def create_Ororo():
        Ororo = GirlClass("Ororo", voice = ch_Ororo)

        Ororo.full_name = "Ororo Munroe"
        Ororo.public_name = "Storm"
        Ororo.call_sign = "Storm"

        Ororo.Player_petname = Player.first_name
        Ororo.Player_petnames.append(Player.first_name)
        Ororo.Player_petnames.append("Mr. [Player.last_name]")

        Ororo.default_pubes = "bush"
        Ororo.pubes = Ororo.default_pubes
        Ororo.desired_pubes = Ororo.default_pubes

        Ororo.white = False
        Ororo.electricity = False

        Ororo.virgin = False

        Cast.append(Ororo.tag)
        Sprites.append(Ororo)
        
        all_Characters.append(Ororo)
        all_Girls.append(Ororo)
        Professors.append(Ororo)

        return Ororo

label update_Ororo:
    $ Ororo.sprite_anchor = Ororo_standing_anchor
    $ Ororo.sprite_position[1] = Ororo_standing_height
    $ Ororo.sprite_zoom = Ororo_standing_zoom

    return