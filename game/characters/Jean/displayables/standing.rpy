transform Jean_standing_head_animation:
    subpixel True
    transform_anchor True
    
    pos (0.0, 0.0)
    xzoom 1.0 yzoom 1.0
    rotate 0.0

    block:
        pause 2.0
        ease 2.0 rotate -1
        pause 5.0
        ease 2.0 rotate 0
        pause 10.0
        ease 2.0 rotate 1

        repeat

transform Jean_standing_right_arm_animation:
    subpixel True
    transform_anchor True
    
    pos (0.0, 0.0)
    xzoom 1.0 yzoom 1.0
    rotate 0.0

    block:
        block:
            choice:
                pause 2.0
            choice:
                pause 5.0
            choice:
                pause 10.0

        block:
            choice:
                ease 2.0 rotate -2
            choice:
                ease 2.0 rotate 0
            choice:
                ease 2.0 rotate 2

        repeat

transform Jean_standing_left_arm_animation:
    subpixel True
    transform_anchor True
    
    pos (0.0, 0.0)
    xzoom 1.0 yzoom 1.0
    rotate 0.0

    block:
        block:
            choice:
                pause 2.0
            choice:
                pause 5.0
            choice:
                pause 10.0

        block:
            choice:
                ease 2.0 rotate -2
            choice:
                ease 2.0 rotate 0
            choice:
                ease 2.0 rotate 2

        repeat

transform Jean_standing_psychic_animation:
    subpixel True
    transform_anchor True
    
    pos (0.0, 0.0)
    xzoom 1.0 yzoom 1.0
    rotate 0.0

    block:
        linear 1.0 alpha 0.75
        linear 1.0 alpha 1.0
        repeat

transform Jean_standing_activating_psychic_animation:
    subpixel True
    transform_anchor True
    
    pos (0.0, 0.0)
    xzoom 1.0 yzoom 1.0
    rotate 0.0

    alpha 0.0
    ease 0.2 alpha 1.0

transform Jean_standing_deactivating_psychic_animation:
    subpixel True
    transform_anchor True
    
    pos (0.0, 0.0)
    xzoom 1.0 yzoom 1.0
    rotate 0.0

    ease 0.2 alpha 0.0
    
image Jean_sprite standing:
    contains:
        "Jean_standing_temp"
        
    xysize (int(2500*character_sampling), int(4500*character_sampling))

layeredimage Jean_standing_temp:
    if Jean.hovered:
        At("Jean_standing", hover)
    else:
        "Jean_standing"

layeredimage Jean_standing:
    if not Player.left_hand_Actions or Jean not in Player.left_hand_Actions[0].Targets:
        Null()
    elif Player.left_hand_Actions[0].animation_type == "grab_ass":
        At("Jean_standing_male_left_arm_grab_ass_animation[Player.left_hand_Actions[0].mode]", change_offset(Jean_standing_ass_position[0], Jean_standing_ass_position[1]))

    if not Player.right_hand_Actions or Jean not in Player.right_hand_Actions[0].Targets:
        Null()
    elif Player.right_hand_Actions[0].animation_type == "grab_ass":
        At("Jean_standing_male_right_arm_grab_ass_animation[Player.right_hand_Actions[0].mode]", change_offset(Jean_standing_ass_position[0], Jean_standing_ass_position[1]))

    if Jean.ground_shadow:
        "characters/Jean/images/standing/ground_shadow.webp"

    if renpy.get_screen("Wardrobe_screen"):
        "Jean_standing_hair_back"
    else:
        At("Jean_standing_hair_back", Jean_standing_head_animation)

    if Jean.left_arm in ["bra", "rub_neck", "touch_ass"]:
        "characters/Jean/images/standing/left_forearm_[Jean.left_arm].webp"

    if Jean.right_arm not in ["bra", "extended", "fight", "fist", "hip", "neutral", "psychic1", "psychic2", "touch_pussy"]:
        Null()
    elif renpy.get_screen("Wardrobe_screen"):
        "Jean_standing_right_arm"
    elif Jean.right_arm == "neutral":
        At("Jean_standing_right_arm", Jean_standing_right_arm_animation)
    else:
        "Jean_standing_right_arm"

    always:
        "Jean_standing_body"

    if Jean.left_arm in ["fist", "hip", "neutral"]:
        "characters/Jean/images/standing/left_arm_[Jean.left_arm]_shadow.webp"

    if Jean.left_arm not in ["bra", "extended", "fight", "fist", "grope", "hip", "neutral", "psychic1", "psychic2", "rub_neck", "touch_ass"]:
        Null()
    elif renpy.get_screen("Wardrobe_screen"):
        "Jean_standing_left_arm"
    elif Jean.left_arm == "neutral":
        At("Jean_standing_left_arm", Jean_standing_left_arm_animation)
    else:
        "Jean_standing_left_arm"

    if Jean.right_arm in ["hip", "touch_pussy"]:
        "characters/Jean/images/standing/right_forearm_[Jean.right_arm]_shadow.webp"

    if Jean.right_arm in ["hip", "touch_pussy"]:
        "characters/Jean/images/standing/right_forearm_[Jean.right_arm].webp"

    if Jean.left_arm in ["grope"]:
        "characters/Jean/images/standing/left_forearm_[Jean.left_arm]_shadow.webp"

    if Jean.left_arm in ["grope"]:
        "characters/Jean/images/standing/left_forearm_[Jean.left_arm].webp"

    always:
        "characters/Jean/images/standing/head_shadow.webp"

    if not Player.left_hand_Actions or Jean not in Player.left_hand_Actions[0].Targets:
        Null()
    elif Player.left_hand_Actions[0].animation_type == "choke":
        At("Jean_standing_male_left_arm_choke_animation[Player.left_hand_Actions[0].mode]", change_offset(Jean_standing_neck_position[0], Jean_standing_neck_position[1]))

    if not Player.right_hand_Actions or Jean not in Player.right_hand_Actions[0].Targets:
        Null()
    elif Player.right_hand_Actions[0].animation_type == "choke":
        At("Jean_standing_male_right_arm_choke_animation[Player.right_hand_Actions[0].mode]", change_offset(Jean_standing_neck_position[0], Jean_standing_neck_position[1]))

    if renpy.get_screen("Wardrobe_screen"):
        "Jean_standing_head"
    else:
        At("Jean_standing_head", Jean_standing_head_animation)

    if Jean.right_arm in ["fight", "extended", "psychic1"]:
        "characters/Jean/images/standing/right_forearm_[Jean.right_arm].webp"

    if Jean.left_arm in ["fight", "psychic1", "psychic2"]:
        "characters/Jean/images/standing/left_forearm_[Jean.left_arm].webp"

    if not Player.left_hand_Actions or Jean not in Player.left_hand_Actions[0].Targets:
        Null()
    elif Player.left_hand_Actions[0].animation_type == "touch_breasts" and Jean.right_breast_Actions and Player.left_hand_Actions[0].animation_type == Jean.right_breast_Actions[0].animation_type:
        At("Jean_standing_male_left_arm_touch_right_breast_animation[Player.left_hand_Actions[0].mode]", change_offset(Jean_standing_right_breast_position[0], Jean_standing_right_breast_position[1]))
    elif Player.left_hand_Actions[0].animation_type == "touch_breasts" and Jean.left_breast_Actions and Player.left_hand_Actions[0].animation_type == Jean.left_breast_Actions[0].animation_type:
        At("Jean_standing_male_left_arm_touch_left_breast_animation[Player.left_hand_Actions[0].mode]", change_offset(Jean_standing_left_breast_position[0], Jean_standing_left_breast_position[1]))
    elif Player.left_hand_Actions[0].animation_type == "pinch_nipples" and Jean.right_nipple_Actions and Player.left_hand_Actions[0].animation_type == Jean.right_nipple_Actions[0].animation_type:
        At("Jean_standing_male_left_arm_touch_right_breast_animation[Player.left_hand_Actions[0].mode]", change_offset(Jean_standing_right_nipple_position[0], Jean_standing_right_nipple_position[1]))
    elif Player.left_hand_Actions[0].animation_type == "pinch_nipples" and Jean.left_nipple_Actions and Player.left_hand_Actions[0].animation_type == Jean.left_nipple_Actions[0].animation_type:
        At("Jean_standing_male_left_arm_touch_left_breast_animation[Player.left_hand_Actions[0].mode]", change_offset(Jean_standing_left_nipple_position[0], Jean_standing_left_nipple_position[1]))
    elif Player.left_hand_Actions[0].animation_type == "touch_thighs":
        At("Jean_standing_male_left_arm_touch_thighs_animation[Player.left_hand_Actions[0].mode]", change_offset(Jean_standing_thigh_position[0], Jean_standing_thigh_position[1]))
    elif Player.left_hand_Actions[0].animation_type == "touch_thighs_higher":
        At("Jean_standing_male_left_arm_touch_thighs_higher_animation[Player.left_hand_Actions[0].mode]", change_offset(Jean_standing_thigh_higher_position[0], Jean_standing_thigh_higher_position[1]))
    elif Player.left_hand_Actions[0].animation_type == "touch_pussy":
        At("Jean_standing_male_left_arm_touch_pussy_animation[Player.left_hand_Actions[0].mode]", change_offset(Jean_standing_pussy_position[0], Jean_standing_pussy_position[1]))

    if not Player.right_hand_Actions or Jean not in Player.right_hand_Actions[0].Targets:
        Null()
    elif Player.right_hand_Actions[0].animation_type == "touch_breasts" and Jean.right_breast_Actions and Player.right_hand_Actions[0].animation_type == Jean.right_breast_Actions[0].animation_type:
        At("Jean_standing_male_right_arm_touch_right_breast_animation[Player.right_hand_Actions[0].mode]", change_offset(Jean_standing_right_breast_position[0], Jean_standing_right_breast_position[1]))
    elif Player.right_hand_Actions[0].animation_type == "touch_breasts" and Jean.left_breast_Actions and Player.right_hand_Actions[0].animation_type == Jean.left_breast_Actions[0].animation_type:
        At("Jean_standing_male_right_arm_touch_left_breast_animation[Player.right_hand_Actions[0].mode]", change_offset(Jean_standing_left_breast_position[0], Jean_standing_left_breast_position[1]))
    elif Player.right_hand_Actions[0].animation_type == "pinch_nipples" and Jean.right_nipple_Actions and Player.right_hand_Actions[0].animation_type == Jean.right_nipple_Actions[0].animation_type:
        At("Jean_standing_male_right_arm_touch_right_breast_animation[Player.right_hand_Actions[0].mode]", change_offset(Jean_standing_right_nipple_position[0], Jean_standing_right_nipple_position[1]))
    elif Player.right_hand_Actions[0].animation_type == "pinch_nipples" and Jean.left_nipple_Actions and Player.right_hand_Actions[0].animation_type == Jean.left_nipple_Actions[0].animation_type:
        At("Jean_standing_male_right_arm_touch_left_breast_animation[Player.right_hand_Actions[0].mode]", change_offset(Jean_standing_left_nipple_position[0], Jean_standing_left_nipple_position[1]))
    elif Player.right_hand_Actions[0].animation_type == "touch_thighs":
        At("Jean_standing_male_right_arm_touch_thighs_animation[Player.right_hand_Actions[0].mode]", change_offset(Jean_standing_thigh_position[0], Jean_standing_thigh_position[1]))
    elif Player.right_hand_Actions[0].animation_type == "touch_thighs_higher":
        At("Jean_standing_male_right_arm_touch_thighs_higher_animation[Player.right_hand_Actions[0].mode]", change_offset(Jean_standing_thigh_higher_position[0], Jean_standing_thigh_higher_position[1]))
    elif Player.right_hand_Actions[0].animation_type == "touch_pussy":
        At("Jean_standing_male_right_arm_touch_pussy_animation[Player.right_hand_Actions[0].mode]", change_offset(Jean_standing_pussy_position[0], Jean_standing_pussy_position[1]))

    if not Player.mouth_Actions or Jean not in Player.mouth_Actions[0].Targets:
        Null()
    elif Player.mouth_Actions[0].animation_type in ["suck_nipples"] and Jean.left_nipple_Actions and Player.mouth_Actions[0].animation_type == Jean.left_nipple_Actions[0].animation_type:
        At("Jean_standing_male_head_suck_left_nipple_animation[Player.mouth_Actions[0].mode]", change_offset(Jean_standing_left_nipple_position[0], Jean_standing_left_nipple_position[1]))
    elif Player.mouth_Actions[0].animation_type in ["suck_nipples"] and Jean.right_nipple_Actions and Player.mouth_Actions[0].animation_type == Jean.right_nipple_Actions[0].animation_type:
        At("Jean_standing_male_head_suck_right_nipple_animation[Player.mouth_Actions[0].mode]", change_offset(Jean_standing_right_nipple_position[0], Jean_standing_right_nipple_position[1]))

layeredimage Jean_standing_hair_back:
    # if Jean.wet or Jean.Clothes["hair"].string == "wet":
    #     "characters/Jean/images/standing/hair_back_wet.webp"
    # else:
    always:
        "characters/Jean/images/standing/hair_back.webp"

    anchor (int(1315*character_sampling), int(1360*character_sampling))
    offset (int(1315*character_sampling), int(1360*character_sampling))

layeredimage Jean_standing_head:
    always:
        "characters/Jean/images/standing/head.webp"

    always:
        "characters/Jean/images/standing/mouth_happy.webp"

    always:
        "characters/Jean/images/standing/eyes_neutral.webp"

    always:
        "characters/Jean/images/standing/brows_neutral.webp"

    # if Jean.wet or Jean.Clothes["hair"].string == "wet":
    #     "characters/Jean/images/standing/hair_wet_shadow.webp"
    # else:
    always:
        "characters/Jean/images/standing/hair_[Jean.Clothes[hair].string]_shadow.webp"

    # if Jean.wet or Jean.Clothes["hair"].string == "wet":
    #     "characters/Jean/images/standing/hair_wet.webp"
    # else:
    always:
        "characters/Jean/images/standing/hair_[Jean.Clothes[hair].string].webp"

    if Jean.psychic and Jean.activating_psychic:
        At("Jean_standing_psychic", Jean_standing_activating_psychic_animation)
    elif Jean.psychic:
        At("Jean_standing_psychic", Jean_standing_psychic_animation)
    elif Jean.deactivating_psychic:
        At("Jean_standing_psychic", Jean_standing_deactivating_psychic_animation)

    anchor (int(1315*character_sampling), int(1360*character_sampling))
    offset (int(1315*character_sampling), int(1360*character_sampling))

image Jean_standing_psychic:
    "characters/Jean/images/standing/psychic.webp"

    anchor (int(1220*character_sampling), int(1110*character_sampling))
    offset (int(1220*character_sampling), int(1110*character_sampling))

layeredimage Jean_standing_right_arm:
    always:
        "characters/Jean/images/standing/right_arm_[Jean.right_arm].webp"

    anchor (int(1070*character_sampling), int(1590*character_sampling))
    offset (int(1070*character_sampling), int(1590*character_sampling))

layeredimage Jean_standing_body:
    always:
        "characters/Jean/images/standing/body.webp"

    always:
        "characters/Jean/images/standing/right_foot.webp"

    always:
        "characters/Jean/images/standing/left_foot_shadow.webp"

    always:
        "characters/Jean/images/standing/left_foot.webp"

    always:
        "characters/Jean/images/standing/breasts_shadow.webp"

    always:
        "characters/Jean/images/standing/breasts.webp"

layeredimage Jean_standing_left_arm:
    always:
        "characters/Jean/images/standing/left_arm_[Jean.left_arm].webp"

    anchor (int(1600*character_sampling), int(1550*character_sampling))
    offset (int(1600*character_sampling), int(1550*character_sampling))

image Jean_standing_blinking:
    "characters/Jean/images/standing/eyes_[Jean.eyes].webp"
    choice:
        4.5
    choice:
        4.0
    choice:
        3.5
    "characters/Jean/images/standing/eyes_blink1.webp"
    0.027
    "characters/Jean/images/standing/eyes_blink2.webp"
    0.027
    "characters/Jean/images/standing/eyes_closed.webp"
    0.054
    "characters/Jean/images/standing/eyes_blink2.webp"
    0.018
    "characters/Jean/images/standing/eyes_blink1.webp"
    0.072
    repeat

layeredimage Jean_standing_male_left_arm:
    if Player.left_hand_Actions[0].animation_type in ["touch_thighs", "touch_thighs_higher", "touch_breasts", "touch_pussy", "grab_ass"]:
        "Player_left_arm_fondle"
    elif Player.left_hand_Actions[0].animation_type in ["choke", "pinch_nipples"]:
        "Player_left_arm_pinch"

layeredimage Jean_standing_male_right_arm:
    if Player.right_hand_Actions[0].animation_type in ["touch_thighs", "touch_thighs_higher", "touch_breasts", "touch_pussy", "grab_ass"]:
        "Player_right_arm_fondle"
    elif Player.right_hand_Actions[0].animation_type in ["choke", "pinch_nipples"]:
        "Player_right_arm_pinch"

layeredimage Jean_standing_male_head:
    if Player.body_visible:
        "Player_head"

    if Player.mouth_Actions and Jean in Player.mouth_Actions[0].Targets and Player.mouth_Actions[0].animation_type in ["suck_nipples", "eat_pussy", "eat_ass"]:
        "Jean_standing_male_tongue_animation[Player.mouth_Actions[0].mode]"

image Jean_standing_male_tongue:
    "Player_tongue"
    
image Jean_standing_male_left_arm_choke_animation0:
    "Jean_standing_male_left_arm"

    standing_male_left_arm_choke_animation0

image Jean_standing_male_left_arm_choke_animation1:
    "Jean_standing_male_left_arm"

    standing_male_left_arm_choke_animation1

image Jean_standing_male_left_arm_touch_thighs_animation0:
    "Jean_standing_male_left_arm"

    standing_male_left_arm_touch_thighs_animation0

image Jean_standing_male_left_arm_touch_thighs_animation1:
    "Jean_standing_male_left_arm"

    standing_male_left_arm_touch_thighs_animation1

image Jean_standing_male_left_arm_touch_thighs_higher_animation0:
    "Jean_standing_male_left_arm"

    standing_male_left_arm_touch_thighs_higher_animation0

image Jean_standing_male_left_arm_touch_thighs_higher_animation1:
    "Jean_standing_male_left_arm"

    standing_male_left_arm_touch_thighs_higher_animation1

image Jean_standing_male_left_arm_touch_left_breast_animation0:
    "Jean_standing_male_left_arm"

    standing_male_left_arm_touch_left_breast_animation0

image Jean_standing_male_left_arm_touch_left_breast_animation1:
    "Jean_standing_male_left_arm"

    standing_male_left_arm_touch_left_breast_animation1

image Jean_standing_male_left_arm_touch_right_breast_animation0:
    "Jean_standing_male_left_arm"

    standing_male_left_arm_touch_right_breast_animation0

image Jean_standing_male_left_arm_touch_right_breast_animation1:
    "Jean_standing_male_left_arm"

    standing_male_left_arm_touch_right_breast_animation1

image Jean_standing_male_left_arm_touch_pussy_animation0:
    "Jean_standing_male_left_arm"

    standing_male_left_arm_touch_pussy_animation0

image Jean_standing_male_left_arm_touch_pussy_animation1:
    "Jean_standing_male_left_arm"

    standing_male_left_arm_touch_pussy_animation1

image Jean_standing_male_left_arm_grab_ass_animation0:
    "Jean_standing_male_left_arm"

    standing_male_left_arm_grab_ass_animation0

image Jean_standing_male_left_arm_grab_ass_animation1:
    "Jean_standing_male_left_arm"

    standing_male_left_arm_grab_ass_animation1
    
image Jean_standing_male_right_arm_choke_animation0:
    "Jean_standing_male_right_arm"

    standing_male_right_arm_choke_animation0

image Jean_standing_male_right_arm_choke_animation1:
    "Jean_standing_male_right_arm"

    standing_male_right_arm_choke_animation1

image Jean_standing_male_right_arm_touch_thighs_animation0:
    "Jean_standing_male_right_arm"

    standing_male_right_arm_touch_thighs_animation0

image Jean_standing_male_right_arm_touch_thighs_animation1:
    "Jean_standing_male_right_arm"

    standing_male_right_arm_touch_thighs_animation1

image Jean_standing_male_right_arm_touch_thighs_higher_animation0:
    "Jean_standing_male_right_arm"

    standing_male_right_arm_touch_thighs_higher_animation0

image Jean_standing_male_right_arm_touch_thighs_higher_animation1:
    "Jean_standing_male_right_arm"

    standing_male_right_arm_touch_thighs_higher_animation1

image Jean_standing_male_right_arm_touch_left_breast_animation0:
    "Jean_standing_male_right_arm"

    standing_male_right_arm_touch_left_breast_animation0

image Jean_standing_male_right_arm_touch_left_breast_animation1:
    "Jean_standing_male_right_arm"

    standing_male_right_arm_touch_left_breast_animation1

image Jean_standing_male_right_arm_touch_right_breast_animation0:
    "Jean_standing_male_right_arm"

    standing_male_right_arm_touch_right_breast_animation0

image Jean_standing_male_right_arm_touch_right_breast_animation1:
    "Jean_standing_male_right_arm"

    standing_male_right_arm_touch_right_breast_animation1

image Jean_standing_male_right_arm_touch_pussy_animation0:
    "Jean_standing_male_right_arm"

    standing_male_right_arm_touch_pussy_animation0

image Jean_standing_male_right_arm_touch_pussy_animation1:
    "Jean_standing_male_right_arm"

    standing_male_right_arm_touch_pussy_animation1

image Jean_standing_male_right_arm_grab_ass_animation0:
    "Jean_standing_male_right_arm"

    standing_male_right_arm_grab_ass_animation0

image Jean_standing_male_right_arm_grab_ass_animation1:
    "Jean_standing_male_right_arm"

    standing_male_right_arm_grab_ass_animation1

image Jean_standing_male_head_suck_left_nipple_animation0:
    "Jean_standing_male_head"

    standing_male_head_suck_left_nipple_animation0

image Jean_standing_male_head_suck_left_nipple_animation1:
    "Jean_standing_male_head"

    standing_male_head_suck_left_nipple_animation1

image Jean_standing_male_head_suck_right_nipple_animation0:
    "Jean_standing_male_head"

    standing_male_head_suck_right_nipple_animation0

image Jean_standing_male_head_suck_right_nipple_animation1:
    "Jean_standing_male_head"

    standing_male_head_suck_right_nipple_animation1

image Jean_standing_male_tongue_animation0:
    "Jean_standing_male_tongue"

    standing_male_tongue_animation0

image Jean_standing_male_tongue_animation1:
    "Jean_standing_male_tongue"

    standing_male_tongue_animation1