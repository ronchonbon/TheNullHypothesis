init -1:
    
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
        "finger_ass": [-0.05, 0.2, 0.4, 0.6, 0.8],
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
        "self_dildo_ass": [-0.1, 0.0, 0.3, 0.5, 0.7],

        "jerk_off": [0.1, 0.2, 0.2, 0.1, 0.0],

        "grind_pussy": [0.3, 0.6, 0.6, 0.6, 0.6],
        "grind_ass": [0.3, 0.6, 0.6, 0.6, 0.6],
        "sex": [0.1, 0.4, 0.8, 0.8, 0.8],
        "anal": [-0.2, 0.0, 0.4, 0.6, 0.8],
        
        "vibrator": [0.5, 1.0, 1.0, 1.0, 1.0],
        "dildo_pussy": [0.1, 0.4, 0.8, 0.8, 0.8],
        "dildo_ass": [-0.1, 0.0, 0.4, 0.6, 0.8]}

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