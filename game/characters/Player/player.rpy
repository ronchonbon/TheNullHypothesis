init -2:
    
    define Player_color = "#000000"
    define ch_Player = Character("Player")

    define Player_base_Action_desire = 10

    define Player_Action_desires = {
        "spank": [0.1, 0.1, 0.1, 0.05, 0.0],
        
        "makeout": [0.2, 0.2, 0.2, 0.1, 0.05],
        "choke": [0.1, 0.1, 0.1, 0.05, 0.0],

        "touch_thighs_over_clothes": [0.05, 0.05, 0.05, 0.0, 0.0],
        "touch_thighs_higher_over_clothes": [0.1, 0.1, 0.1, 0.05, 0.0],
        "touch_thighs": [0.1, 0.1, 0.1, 0.05, 0.0],
        "touch_thighs_higher": [0.2, 0.2, 0.2, 0.1, 0.0],
        "touch_breasts_over_clothes": [0.1, 0.1, 0.1, 0.0, 0.0],
        "touch_breasts": [0.2, 0.2, 0.2, 0.05, 0.0],
        "pinch_nipples": [0.3, 0.3, 0.3, 0.1, 0.0],
        "suck_nipples": [0.4, 0.4, 0.4, 0.2, 0.0],
        "touch_pussy_over_clothes": [0.2, 0.2, 0.2, 0.0, 0.0],
        "touch_pussy": [0.3, 0.3, 0.3, 0.05, 0.0],
        "finger_pussy": [0.4, 0.4, 0.4, 0.1, 0.0],
        "eat_pussy": [0.2, 0.5, 0.5, 0.5, 0.0],
        "grab_ass_over_clothes": [0.2, 0.2, 0.2, 0.1, 0.0],
        "grab_ass": [0.3, 0.3, 0.3, 0.2, 0.0],
        "finger_ass": [0.6, 0.6, 0.6, 0.2, 0.0],
        "eat_ass": [0.2, 0.6, 0.6, 0.6, 0.0],
        
        "handjob": [0.3, 0.6, 0.6, 0.6, 0.6],
        "fondle_balls": [0.1, 0.3, 0.3, 0.3, 0.0],
        "blowjob": [0.4, 0.8, 0.8, 0.8, 0.8],
        "suck_balls": [0.3, 0.6, 0.6, 0.6, 0.1],
        "deepthroat": [0.5, 1.0, 1.0, 1.0, 1.0],
        "titjob": [0.4, 0.8, 0.8, 0.8, 0.8],
        "footjob": [0.3, 0.6, 0.6, 0.6, 0.6],

        "self_touch_pussy": [0.1, 0.2, 0.2, 0.1, 0.0],
        "self_finger_ass": [0.2, 0.5, 0.5, 0.2, 0.0],
        "self_vibrator": [0.2, 0.4, 0.4, 0.2, 0.0],
        "self_dildo_pussy": [0.2, 0.5, 0.5, 0.2, 0.0],
        "self_dildo_ass": [0.3, 0.6, 0.6, 0.3, 0.0],

        "jerk_off": [0.3, 0.6, 0.6, 0.6, 0.6],

        "grind_pussy": [0.3, 0.6, 0.6, 0.6, 0.6],
        "grind_ass": [0.3, 0.6, 0.6, 0.6, 0.6],
        "sex": [0.4, 0.8, 0.8, 0.8, 0.8],
        "anal": [0.5, 1.0, 1.0, 1.0, 1.0],
        
        "vibrator": [0.3, 0.6, 0.6, 0.3, 0.0],
        "dildo_pussy": [0.3, 0.7, 0.7, 0.3, 0.0],
        "dildo_ass": [0.4, 0.8, 0.8, 0.4, 0.0]}

init -2 python:

    def create_Player(first_name, last_name):
        Player = PlayerClass(
            first_name, last_name,
            voice = ch_Player)

        Player.call_sign = "Null"
            
        return Player