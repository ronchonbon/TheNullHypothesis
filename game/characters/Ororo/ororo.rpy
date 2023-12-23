init -1:
    
    default Ororo = create_Ororo()

    define Ororo_color = "#4e6364"
    define ch_Ororo = Character("[Ororo.tag]")

    define Ororo_standing_anchor = [int(1280*character_sampling), int(1170*character_sampling)]
    define Ororo_standing_height = 0.2
    define Ororo_standing_zoom = 0.35*character_adjustment
    define Ororo_standing_bottom = 0.955

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
        "self_dildo_pussy": ["Ororo in Partners"],
        "self_dildo_ass": ["Ororo in Partners"],
        "jerk_off": ["Ororo in Partners"],
        
        "grind_pussy": ["Ororo in Partners"],
        "grind_ass": ["Ororo in Partners"],
        "sex": ["Ororo in Partners"],
        "anal": ["Ororo in Partners"],
        "vibrator": ["Ororo in Partners"],
        "dildo_pussy": ["Ororo in Partners"],
        "dildo_ass": ["Ororo in Partners"],
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

    define Ororo_base_Action_desire = 5

    define Ororo_Action_desires = {
        "spank": [0, 0, 0, 0, 0],

        "makeout": [0.0, 0.0, 0.0, 0.0, 0.0],
        "choke": [0.0, 0.0, 0.0, 0.0, 0.0],

        "touch_thighs_over_clothes": [0.0, 0.0, 0.0, 0.0, 0.0],
        "touch_thighs_higher_over_clothes": [0.0, 0.0, 0.0, 0.0, 0.0],
        "touch_thighs": [0.0, 0.0, 0.0, 0.0, 0.0],
        "touch_thighs_higher": [0.0, 0.0, 0.0, 0.0, 0.0],
        "touch_breasts_over_clothes": [0.0, 0.0, 0.0, 0.0, 0.0],
        "touch_breasts": [0.0, 0.0, 0.0, 0.0, 0.0],
        "pinch_nipples": [0.0, 0.0, 0.0, 0.0, 0.0],
        "suck_nipples": [0.0, 0.0, 0.0, 0.0, 0.0],
        "touch_pussy_over_clothes": [0.0, 0.0, 0.0, 0.0, 0.0],
        "touch_pussy": [0.0, 0.0, 0.0, 0.0, 0.0],
        "finger_pussy": [0.0, 0.0, 0.0, 0.0, 0.0],
        "eat_pussy": [0.0, 0.0, 0.0, 0.0, 0.0],
        "grab_ass_over_clothes": [0.0, 0.0, 0.0, 0.0, 0.0],
        "grab_ass": [0.0, 0.0, 0.0, 0.0, 0.0],
        "finger_ass": [0.0, 0.0, 0.0, 0.0, 0.0],
        "eat_ass": [0.0, 0.0, 0.0, 0.0, 0.0],
        
        "handjob": [0.0, 0.0, 0.0, 0.0, 0.0],
        "fondle_balls": [0.0, 0.0, 0.0, 0.0, 0.0],
        "blowjob": [0.0, 0.0, 0.0, 0.0, 0.0],
        "suck_balls": [0.0, 0.0, 0.0, 0.0, 0.0],
        "deepthroat": [0.0, 0.0, 0.0, 0.0, 0.0],
        "titjob": [0.0, 0.0, 0.0, 0.0, 0.0],
        "footjob": [0.0, 0.0, 0.0, 0.0, 0.0],

        "self_touch_pussy": [0.0, 0.0, 0.0, 0.0, 0.0],
        "self_finger_ass": [0.0, 0.0, 0.0, 0.0, 0.0],
        "self_vibrator": [0.0, 0.0, 0.0, 0.0, 0.0],
        "self_dildo_pussy": [0.0, 0.0, 0.0, 0.0, 0.0],
        "self_dildo_ass": [0.0, 0.0, 0.0, 0.0, 0.0],

        "jerk_off": [0.0, 0.0, 0.0, 0.0, 0.0],

        "grind_pussy": [0.0, 0.0, 0.0, 0.0, 0.0],
        "grind_ass": [0.0, 0.0, 0.0, 0.0, 0.0],
        "sex": [0.0, 0.0, 0.0, 0.0, 0.0],
        "anal": [0.0, 0.0, 0.0, 0.0, 0.0],
        
        "vibrator": [0.0, 0.0, 0.0, 0.0, 0.0],
        "dildo_pussy": [0.0, 0.0, 0.0, 0.0, 0.0],
        "dildo_ass": [0.0, 0.0, 0.0, 0.0, 0.0]}

    define Ororo_Action_desire_thresholds = {
        "spank": 0,

        "makeout": 0,
        "choke": 0,

        "touch_thighs_over_clothes": 0,
        "touch_thighs_higher_over_clothes": 0,
        "touch_thighs": 0,
        "touch_thighs_higher": 0,
        "touch_breasts_over_clothes": 0,
        "touch_breasts": 0,
        "pinch_nipples": 0,
        "suck_nipples": 0,
        "touch_pussy_over_clothes": 0,
        "touch_pussy": 0,
        "finger_pussy": 0,
        "eat_pussy": 0,
        "grab_ass_over_clothes": 0,
        "grab_ass": 0,
        "finger_ass": 0,
        "eat_ass": 0,
        
        "handjob": 0,
        "fondle_balls": 0,
        "blowjob": 0,
        "suck_balls": 0,
        "deepthroat": 0,
        "titjob": 0,
        "footjob": 0,

        "self_touch_pussy": 0,
        "self_finger_ass": 0,
        "self_vibrator": 0,
        "self_dildo_pussy": 0,
        "self_dildo_ass": 0,

        "jerk_off": 0,

        "grind_pussy": 0,
        "grind_ass": 0,
        "sex": 0,
        "anal": 0,
        
        "vibrator": 0,
        "dildo_pussy": 0,
        "dildo_ass": 0}

init -2 python:

    def create_Ororo():
        Ororo = CompanionClass("Ororo", voice = ch_Ororo)

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
        all_Companions.append(Ororo)
        Professors.append(Ororo)

        return Ororo

    def Ororo_faces(face):
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
            mouth = "smile"
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
            return "wrong", "wrong", "wrong", 0

        return brows, eyes, mouth, blush

    def Ororo_arms(pose):
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
        elif pose == "shrug":
            left_arm = "extended"
            right_arm = "extended"
        elif pose == "sheepish":
            left_arm = "rub_neck"
            right_arm = "extended"
        elif pose == "storm1":
            left_arm = "storm1"
            right_arm = "storm1"
        elif pose == "storm2":
            left_arm = "storm2"
            right_arm = "storm2"
        elif pose == "touch_self":
            left_arm = "grope"
            right_arm = "touch_pussy"
        else:
            return "wrong", "wrong"

        return left_arm, right_arm

    def Ororo_locations():
        possible_locations = []

        possible_locations.append(Ororo.home)

        if time_index < 3 and weather != "rain":
            possible_locations.append("bg_campus")

        if time_index < 2 and weekday < 5:
            possible_locations.append("bg_classroom")
            possible_locations.append("bg_classroom")

        if time_index < 3 and Ororo.location != "bg_lockers" and not Ororo.History.check("trained_with_Player", tracker = "daily"):
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
            if (Ororo in Partners or Ororo.status["nympho"] or approval_check(Ororo, threshold = "love")) and renpy.random.random() > 0.85:
                if (Player.location not in bedrooms or Player.location == Player.home) and (Player.location != "bg_shower_Player" or Ororo.has_keys_to_Players_room):
                    possible_locations.append(Player.location)

                if Ororo.has_keys_to_Players_room:
                    possible_locations.append(Player.home)

        return possible_locations

label update_Ororo:
    $ Ororo.sprite_anchor = Ororo_standing_anchor
    $ Ororo.sprite_position[1] = Ororo_standing_height
    $ Ororo.sprite_zoom = Ororo_standing_zoom

    return