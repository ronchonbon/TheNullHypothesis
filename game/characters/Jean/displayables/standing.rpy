transform Jean_standing_head_animation:
    subpixel True
    transform_anchor True
    animation
    
    pos (0.0, 0.0)
    xzoom 1.0 yzoom 1.0
    rotate 0.0

    block:
        pause 3.5
        ease 2.0 rotate 0
        pause 5.6
        ease 2.0 rotate -1
        pause 8.4
        ease 2.0 rotate 1

        repeat

transform Jean_standing_right_arm_animation:
    subpixel True
    transform_anchor True
    animation
    
    pos (0.0, 0.0)
    xzoom 1.0 yzoom 1.0
    rotate 0.0

    block:
        pause 6.3
        ease 2.0 rotate 0
        pause 3.4
        ease 2.0 rotate 1
        pause 7.2
        ease 2.0 rotate -2

        repeat

transform Jean_standing_left_arm_animation:
    subpixel True
    transform_anchor True
    animation
    
    pos (0.0, 0.0)
    xzoom 1.0 yzoom 1.0
    rotate 0.0

    block:
        pause 4.5
        ease 2.0 rotate -2
        pause 5.2
        ease 2.0 rotate 2
        pause 3.4
        ease 2.0 rotate 0

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
        "Jean_standing" at hover
    elif Jean.orgasming:
        "Jean_standing" at tremble(20)
    else:
        "Jean_standing"

layeredimage Jean_standing:
    if not Player.left_hand_Actions or Jean not in Player.left_hand_Actions[0].Targets:
        Null()
    elif Player.left_hand_Actions[0].animation_type == "grab_ass":
        "Jean_standing_male_left_arm_grab_ass_animation[Player.left_hand_Actions[0].mode]" at change_offset(Jean_standing_ass_position[0], Jean_standing_ass_position[1])

    if not Player.right_hand_Actions or Jean not in Player.right_hand_Actions[0].Targets:
        Null()
    elif Player.right_hand_Actions[0].animation_type == "grab_ass":
        "Jean_standing_male_right_arm_grab_ass_animation[Player.right_hand_Actions[0].mode]" at change_offset(Jean_standing_ass_position[0], Jean_standing_ass_position[1])

    if Jean.ground_shadow:
        "characters/Jean/images/standing/ground_shadow.webp" at Transform(blend = "multiply")

    if renpy.get_screen("Wardrobe_screen"):
        "Jean_standing_hair_back"
    else:
        "Jean_standing_hair_back" at Jean_standing_head_animation

    if Jean.left_arm in ["bra", "rub_neck", "touch_ass"]:
        "characters/Jean/images/standing/left_forearm_[Jean.left_arm].webp"

    if Jean.Clothes["bodysuit"].string not in ["blueyellow_classic_suit"]:
        Null()
    elif Jean.Clothes["bodysuit"].string in ["blueyellow_classic_suit"] and Jean.Clothes["bodysuit"].state == 1:
        Null()
    elif Jean.left_arm in ["bra", "rub_neck", "touch_ass"]:
        "characters/Jean/images/standing/bodysuit_[Jean.Clothes[bodysuit].string]_left_forearm_sleeve_[Jean.left_arm].webp"

    if not Jean.Clothes["gloves"].string:
        Null()
    elif Jean.left_arm in ["rub_neck", "touch_ass"]:
        "characters/Jean/images/standing/gloves_[Jean.Clothes[gloves].string]_left_[Jean.left_arm].webp"

    if not Jean.Clothes["sleeves"].string:
        Null()
    elif Jean.left_arm in ["bra", "rub_neck", "touch_ass"]:
        "characters/Jean/images/standing/sleeves_[Jean.Clothes[sleeves].string]_left_[Jean.left_arm].webp"

    if Jean.right_arm not in ["bra", "crossed", "extended", "fight", "fist", "hip", "neutral", "psychic1", "psychic2", "touch_pussy"]:
        Null()
    elif renpy.get_screen("Wardrobe_screen"):
        "Jean_standing_right_arm"
    elif Jean.right_arm == "neutral":
        "Jean_standing_right_arm" at Jean_standing_right_arm_animation
    else:
        "Jean_standing_right_arm"

    always:
        "Jean_standing_body"

    if Jean.Clothes["bodysuit"].string != "blueyellow_classic_suit":
        Null()
    elif Jean.right_arm in ["psychic1"]:
        "characters/Jean/images/standing/bodysuit_blueyellow_classic_suit_right_pauldron_[Jean.right_arm].webp"
    else:
        "characters/Jean/images/standing/bodysuit_blueyellow_classic_suit_right_pauldron.webp"
    
    if Jean.left_arm not in ["hip", "neutral"]:
        "characters/Jean/images/standing/left_arm_[Jean.left_arm]_shadow.webp" at Transform(blend = "multiply")

    if Jean.left_arm not in ["bra", "crossed", "extended", "fight", "fist", "grope", "hip", "neutral", "psychic1", "psychic2", "rub_neck", "touch_ass"]:
        Null()
    elif renpy.get_screen("Wardrobe_screen"):
        "Jean_standing_left_arm"
    elif Jean.left_arm == "neutral":
        "Jean_standing_left_arm" at Jean_standing_left_arm_animation
    else:
        "Jean_standing_left_arm"

    if not Jean.Clothes["bra"].string or Jean.Clothes["bodysuit"].string or Jean.Clothes["top"].string:
        Null()
    else:
        "characters/Jean/images/standing/bra_[Jean.Clothes[bra].string]_left_shoulder_[Jean.Clothes[bra].state].webp"

    if Jean.left_arm not in ["bra", "crossed", "fight", "fist", "grope", "hip", "neutral", "psychic1", "psychic2", "rub_neck", "touch_ass"]:
        Null()
    elif renpy.get_screen("Wardrobe_screen"):
        "Jean_standing_left_sleeve"
    elif Jean.left_arm == "neutral":
        "Jean_standing_left_sleeve" at Jean_standing_left_arm_animation
    else:
        "Jean_standing_left_sleeve"

    if Jean.Clothes["bodysuit"].string != "blueyellow_classic_suit":
        Null()
    elif Jean.left_arm in ["psychic1", "rub_neck"]:
        "characters/Jean/images/standing/bodysuit_blueyellow_classic_suit_left_pauldron_[Jean.left_arm].webp"
    elif Jean.left_arm not in ["extended"]:
        "characters/Jean/images/standing/bodysuit_blueyellow_classic_suit_left_pauldron.webp"
    
    if Jean.right_arm in ["hip", "touch_pussy"]:
        "characters/Jean/images/standing/right_forearm_[Jean.right_arm]_shadow.webp" at Transform(blend = "multiply")

    if Jean.right_arm in ["hip", "touch_pussy"]:
        "characters/Jean/images/standing/right_forearm_[Jean.right_arm].webp"

    if Jean.Clothes["bodysuit"].string not in ["blueyellow_classic_suit"]:
        Null()
    elif Jean.right_arm in ["hip", "touch_pussy"]:
        "characters/Jean/images/standing/bodysuit_[Jean.Clothes[bodysuit].string]_right_forearm_sleeve_[Jean.right_arm].webp"

    if not Jean.Clothes["gloves"].string:
        Null()
    elif Jean.right_arm in ["hip", "touch_pussy"]:
        "characters/Jean/images/standing/gloves_[Jean.Clothes[gloves].string]_right_[Jean.right_arm].webp"

    if not Jean.Clothes["sleeves"].string:
        Null()
    elif Jean.right_arm in ["hip", "touch_pussy"]:
        "characters/Jean/images/standing/sleeves_[Jean.Clothes[sleeves].string]_right_[Jean.right_arm].webp"

    if Jean.left_arm in ["grope"]:
        "characters/Jean/images/standing/left_forearm_[Jean.left_arm]_shadow.webp" at Transform(blend = "multiply")

    if Jean.left_arm in ["grope"]:
        "characters/Jean/images/standing/left_forearm_[Jean.left_arm].webp"

    if Jean.Clothes["bodysuit"].string not in ["blueyellow_classic_suit"]:
        Null()
    elif Jean.left_arm in ["extended", "grope"]:
        "characters/Jean/images/standing/bodysuit_[Jean.Clothes[bodysuit].string]_left_forearm_sleeve_[Jean.left_arm].webp"

    if not Jean.Clothes["gloves"].string:
        Null()
    elif Jean.left_arm in ["extended", "grope"]:
        "characters/Jean/images/standing/gloves_[Jean.Clothes[gloves].string]_left_[Jean.left_arm].webp"

    if not Jean.Clothes["top"].string:
        Null()
    elif Jean.left_arm in ["extended", "grope"]:
        "characters/Jean/images/standing/top_[Jean.Clothes[top].string]_left_forearm_sleeve_[Jean.left_arm].webp"

    if not Jean.Clothes["sleeves"].string:
        Null()
    elif Jean.left_arm in ["extended", "grope"]:
        "characters/Jean/images/standing/sleeves_[Jean.Clothes[sleeves].string]_left_[Jean.left_arm].webp"

    if Jean.Clothes["bodysuit"].string != "blueyellow_classic_suit":
        Null()
    elif Jean.left_arm in ["extended"]:
        "characters/Jean/images/standing/bodysuit_blueyellow_classic_suit_left_pauldron.webp"

    if not Player.left_hand_Actions or Jean not in Player.left_hand_Actions[0].Targets:
        Null()
    elif Player.left_hand_Actions[0].animation_type == "choke":
        "Jean_standing_male_left_arm_choke_animation[Player.left_hand_Actions[0].mode]" at change_offset(Jean_standing_neck_position[0], Jean_standing_neck_position[1])

    if not Player.right_hand_Actions or Jean not in Player.right_hand_Actions[0].Targets:
        Null()
    elif Player.right_hand_Actions[0].animation_type == "choke":
        "Jean_standing_male_right_arm_choke_animation[Player.right_hand_Actions[0].mode]" at change_offset(Jean_standing_neck_position[0], Jean_standing_neck_position[1])

    if renpy.get_screen("Wardrobe_screen"):
        "Jean_standing_head"
    else:
        "Jean_standing_head" at Jean_standing_head_animation

    if Jean.right_arm in ["extended", "fight", "psychic1"]:
        "characters/Jean/images/standing/right_forearm_[Jean.right_arm].webp"

    if Jean.Clothes["bodysuit"].string not in ["blueyellow_classic_suit"]:
        Null()
    elif Jean.right_arm in ["extended", "fight", "psychic1"]:
        "characters/Jean/images/standing/bodysuit_[Jean.Clothes[bodysuit].string]_right_forearm_sleeve_[Jean.right_arm].webp"

    if not Jean.Clothes["gloves"].string:
        Null()
    elif Jean.right_arm in ["extended", "fight", "psychic1"]:
        "characters/Jean/images/standing/gloves_[Jean.Clothes[gloves].string]_right_[Jean.right_arm].webp"

    if not Jean.Clothes["sleeves"].string:
        Null()
    elif Jean.right_arm in ["extended", "fight", "psychic1"]:
        "characters/Jean/images/standing/sleeves_[Jean.Clothes[sleeves].string]_right_[Jean.right_arm].webp"

    if Jean.left_arm in ["fight", "psychic1", "psychic2"]:
        "characters/Jean/images/standing/left_forearm_[Jean.left_arm].webp"

    if Jean.Clothes["bodysuit"].string not in ["blueyellow_classic_suit"]:
        Null()
    elif Jean.left_arm in ["fight", "psychic1", "psychic2"]:
        "characters/Jean/images/standing/bodysuit_[Jean.Clothes[bodysuit].string]_left_forearm_sleeve_[Jean.left_arm].webp"

    if not Jean.Clothes["gloves"].string:
        Null()
    elif Jean.left_arm in ["fight", "psychic1", "psychic2"]:
        "characters/Jean/images/standing/gloves_[Jean.Clothes[gloves].string]_left_[Jean.left_arm].webp"

    if not Jean.Clothes["sleeves"].string:
        Null()
    elif Jean.left_arm in ["fight", "psychic1", "psychic2"]:
        "characters/Jean/images/standing/sleeves_[Jean.Clothes[sleeves].string]_left_[Jean.left_arm].webp"

    if not Player.left_hand_Actions or Jean not in Player.left_hand_Actions[0].Targets:
        Null()
    elif Player.left_hand_Actions[0].animation_type == "touch_breasts" and Jean.right_breast_Actions and Player.left_hand_Actions[0].animation_type == Jean.right_breast_Actions[0].animation_type:
        "Jean_standing_male_left_arm_touch_right_breast_animation[Player.left_hand_Actions[0].mode]" at change_offset(Jean_standing_right_breast_position[0], Jean_standing_right_breast_position[1])
    elif Player.left_hand_Actions[0].animation_type == "touch_breasts" and Jean.left_breast_Actions and Player.left_hand_Actions[0].animation_type == Jean.left_breast_Actions[0].animation_type:
        "Jean_standing_male_left_arm_touch_left_breast_animation[Player.left_hand_Actions[0].mode]" at change_offset(Jean_standing_left_breast_position[0], Jean_standing_left_breast_position[1])
    elif Player.left_hand_Actions[0].animation_type == "pinch_nipples" and Jean.right_nipple_Actions and Player.left_hand_Actions[0].animation_type == Jean.right_nipple_Actions[0].animation_type:
        "Jean_standing_male_left_arm_touch_right_breast_animation[Player.left_hand_Actions[0].mode]" at change_offset(Jean_standing_right_nipple_position[0], Jean_standing_right_nipple_position[1])
    elif Player.left_hand_Actions[0].animation_type == "pinch_nipples" and Jean.left_nipple_Actions and Player.left_hand_Actions[0].animation_type == Jean.left_nipple_Actions[0].animation_type:
        "Jean_standing_male_left_arm_touch_left_breast_animation[Player.left_hand_Actions[0].mode]" at change_offset(Jean_standing_left_nipple_position[0], Jean_standing_left_nipple_position[1])
    elif Player.left_hand_Actions[0].animation_type == "touch_thighs":
        "Jean_standing_male_left_arm_touch_thighs_animation[Player.left_hand_Actions[0].mode]" at change_offset(Jean_standing_thigh_position[0], Jean_standing_thigh_position[1])
    elif Player.left_hand_Actions[0].animation_type == "touch_thighs_higher":
        "Jean_standing_male_left_arm_touch_thighs_higher_animation[Player.left_hand_Actions[0].mode]" at change_offset(Jean_standing_thigh_higher_position[0], Jean_standing_thigh_higher_position[1])
    elif Player.left_hand_Actions[0].animation_type == "touch_pussy":
        "Jean_standing_male_left_arm_touch_pussy_animation[Player.left_hand_Actions[0].mode]" at change_offset(Jean_standing_pussy_position[0], Jean_standing_pussy_position[1])

    if not Player.right_hand_Actions or Jean not in Player.right_hand_Actions[0].Targets:
        Null()
    elif Player.right_hand_Actions[0].animation_type == "touch_breasts" and Jean.right_breast_Actions and Player.right_hand_Actions[0].animation_type == Jean.right_breast_Actions[0].animation_type:
        "Jean_standing_male_right_arm_touch_right_breast_animation[Player.right_hand_Actions[0].mode]" at change_offset(Jean_standing_right_breast_position[0], Jean_standing_right_breast_position[1])
    elif Player.right_hand_Actions[0].animation_type == "touch_breasts" and Jean.left_breast_Actions and Player.right_hand_Actions[0].animation_type == Jean.left_breast_Actions[0].animation_type:
        "Jean_standing_male_right_arm_touch_left_breast_animation[Player.right_hand_Actions[0].mode]" at change_offset(Jean_standing_left_breast_position[0], Jean_standing_left_breast_position[1])
    elif Player.right_hand_Actions[0].animation_type == "pinch_nipples" and Jean.right_nipple_Actions and Player.right_hand_Actions[0].animation_type == Jean.right_nipple_Actions[0].animation_type:
        "Jean_standing_male_right_arm_touch_right_breast_animation[Player.right_hand_Actions[0].mode]" at change_offset(Jean_standing_right_nipple_position[0], Jean_standing_right_nipple_position[1])
    elif Player.right_hand_Actions[0].animation_type == "pinch_nipples" and Jean.left_nipple_Actions and Player.right_hand_Actions[0].animation_type == Jean.left_nipple_Actions[0].animation_type:
        "Jean_standing_male_right_arm_touch_left_breast_animation[Player.right_hand_Actions[0].mode]" at change_offset(Jean_standing_left_nipple_position[0], Jean_standing_left_nipple_position[1])
    elif Player.right_hand_Actions[0].animation_type == "touch_thighs":
        "Jean_standing_male_right_arm_touch_thighs_animation[Player.right_hand_Actions[0].mode]" at change_offset(Jean_standing_thigh_position[0], Jean_standing_thigh_position[1])
    elif Player.right_hand_Actions[0].animation_type == "touch_thighs_higher":
        "Jean_standing_male_right_arm_touch_thighs_higher_animation[Player.right_hand_Actions[0].mode]" at change_offset(Jean_standing_thigh_higher_position[0], Jean_standing_thigh_higher_position[1])
    elif Player.right_hand_Actions[0].animation_type == "touch_pussy":
        "Jean_standing_male_right_arm_touch_pussy_animation[Player.right_hand_Actions[0].mode]" at change_offset(Jean_standing_pussy_position[0], Jean_standing_pussy_position[1])

    if not Player.mouth_Actions or Jean not in Player.mouth_Actions[0].Targets:
        Null()
    elif Player.mouth_Actions[0].animation_type in ["suck_nipples"] and Jean.left_nipple_Actions and Player.mouth_Actions[0].animation_type == Jean.left_nipple_Actions[0].animation_type:
        "Jean_standing_male_head_suck_left_nipple_animation[Player.mouth_Actions[0].mode]" at change_offset(Jean_standing_left_nipple_position[0], Jean_standing_left_nipple_position[1])
    elif Player.mouth_Actions[0].animation_type in ["suck_nipples"] and Jean.right_nipple_Actions and Player.mouth_Actions[0].animation_type == Jean.right_nipple_Actions[0].animation_type:
        "Jean_standing_male_head_suck_right_nipple_animation[Player.mouth_Actions[0].mode]" at change_offset(Jean_standing_right_nipple_position[0], Jean_standing_right_nipple_position[1])

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
        "characters/Jean/images/standing/mouth_[Jean.mouth].webp"

    if Jean.eyes in ["closed", "down", "left", "right", "squint", "up", "wink"]:
        "characters/Jean/images/standing/eyes_[Jean.eyes].webp"
    else:
        "Jean_standing_blinking"

    always:
        "characters/Jean/images/standing/brows_[Jean.brows].webp"

    if Jean.blush:
        "characters/Jean/images/standing/blush[Jean.blush].webp"

    if Jean.Clothes["face_inner_accessory"].string:
        "characters/Jean/images/standing/face_inner_accessory_[Jean.Clothes[face_inner_accessory].string].webp"

    # if Jean.wet or Jean.Clothes["hair"].string == "wet":
    #     "characters/Jean/images/standing/hair_wet_shadow.webp" at Transform(blend = "multiply")
    # else:
    always:
        "characters/Jean/images/standing/hair_[Jean.Clothes[hair].string]_shadow.webp" at Transform(blend = "multiply")

    # if Jean.wet or Jean.Clothes["hair"].string == "wet":
    #     "characters/Jean/images/standing/hair_wet.webp"
    # else:
    always:
        "characters/Jean/images/standing/hair_[Jean.Clothes[hair].string].webp"

    if Jean.psychic and Jean.activating_psychic:
        "Jean_standing_psychic" at Jean_standing_activating_psychic_animation
    elif Jean.psychic:
        "Jean_standing_psychic" at Jean_standing_psychic_animation
    elif Jean.deactivating_psychic:
        "Jean_standing_psychic" at Jean_standing_deactivating_psychic_animation

    anchor (int(1315*character_sampling), int(1360*character_sampling))
    offset (int(1315*character_sampling), int(1360*character_sampling))

image Jean_standing_psychic:
    "characters/Jean/images/standing/psychic.webp"

    anchor (int(1220*character_sampling), int(1110*character_sampling))
    offset (int(1220*character_sampling), int(1110*character_sampling))

layeredimage Jean_standing_right_arm:
    always:
        "characters/Jean/images/standing/right_arm_[Jean.right_arm].webp"

    if Jean.Clothes["bodysuit"].string not in ["blueyellow_classic_suit"]:
        Null()
    elif Jean.right_arm == "fist":
        "characters/Jean/images/standing/bodysuit_[Jean.Clothes[bodysuit].string]_right_sleeve_neutral.webp"
    else:
        "characters/Jean/images/standing/bodysuit_[Jean.Clothes[bodysuit].string]_right_sleeve_[Jean.right_arm].webp"

    if not Jean.Clothes["gloves"].string:
        Null()
    elif Jean.right_arm in ["crossed", "fist", "neutral", "psychic2"]:
        "characters/Jean/images/standing/gloves_[Jean.Clothes[gloves].string]_right_[Jean.right_arm].webp"

    if not Jean.Clothes["top"].string:
        Null()
    elif Jean.right_arm == "fist":
        "characters/Jean/images/standing/top_[Jean.Clothes[top].string]_right_sleeve_neutral.webp"
    elif Jean.right_arm in ["bra", "crossed", "extended", "fight", "hip", "neutral", "psychic1", "touch_pussy"]:
        "characters/Jean/images/standing/top_[Jean.Clothes[top].string]_right_sleeve_[Jean.right_arm].webp"

    if not Jean.Clothes["sleeves"].string:
        Null()
    elif Jean.right_arm == "fist":
        "characters/Jean/images/standing/sleeves_[Jean.Clothes[sleeves].string]_right_neutral.webp"
    elif Jean.right_arm in ["neutral", "psychic2"]:
        "characters/Jean/images/standing/sleeves_[Jean.Clothes[sleeves].string]_right_[Jean.right_arm].webp"

    anchor (int(1070*character_sampling), int(1590*character_sampling))
    offset (int(1070*character_sampling), int(1590*character_sampling))

layeredimage Jean_standing_body:
    always:
        "characters/Jean/images/standing/body.webp"

    always:
        "characters/Jean/images/standing/right_foot.webp"

    always:
        "characters/Jean/images/standing/left_foot.webp"

    if Jean.Clothes["underwear"].string:
        "characters/Jean/images/standing/underwear_[Jean.Clothes[underwear].string]_[Jean.Clothes[underwear].state].webp"

    if not Jean.Clothes["bodysuit"].string:
        Null()
    elif Jean.Clothes["bodysuit"].string in ["blueyellow_classic_suit"]:
        "characters/Jean/images/standing/bodysuit_[Jean.Clothes[bodysuit].string]_lower.webp"
    elif Jean.Clothes["bodysuit"].string in ["red_swimsuit"] and Jean.Clothes["bodysuit"].state in [0, 1]:
        "characters/Jean/images/standing/bodysuit_[Jean.Clothes[bodysuit].string]_0_lower.webp"
    elif Jean.Clothes["bodysuit"].string in ["red_swimsuit"] and Jean.Clothes["bodysuit"].state in [2, 3]:
        "characters/Jean/images/standing/bodysuit_[Jean.Clothes[bodysuit].string]_2_lower.webp"
    else:
        "characters/Jean/images/standing/bodysuit_[Jean.Clothes[bodysuit].string]_[Jean.Clothes[bodysuit].state]_lower.webp"

    if Jean.Clothes["footwear"].string:
        "characters/Jean/images/standing/footwear_[Jean.Clothes[footwear].string].webp"

    if Jean.Clothes["pants"].string:
        "characters/Jean/images/standing/pants_[Jean.Clothes[pants].string]_[Jean.Clothes[pants].state].webp"

    always:
        "characters/Jean/images/standing/breasts_shadow.webp" at Transform(blend = "multiply")

    if Jean.left_arm == "crossed" and Jean.right_arm == "crossed":
        "characters/Jean/images/standing/breasts_crossed.webp"
    else:
        "characters/Jean/images/standing/breasts.webp"

    if Jean.left_arm == "grope":
        "characters/Jean/images/standing/left_forearm_grope_shadow.webp" at Transform(blend = "multiply")

    if not Jean.Clothes["bra"].string:
        Null()
    elif Jean.Clothes["bodysuit"].string in ["blueyellow_classic_suit"]:
        Null()
    else:
        "characters/Jean/images/standing/bra_[Jean.Clothes[bra].string]_[Jean.Clothes[bra].state].webp"

    if not Jean.Clothes["bodysuit"].string:
        Null()
    elif Jean.Clothes["bodysuit"].string in ["red_swimsuit"] and Jean.Clothes["bodysuit"].state in [0, 2]:
        "characters/Jean/images/standing/bodysuit_[Jean.Clothes[bodysuit].string]_0.webp"
    elif Jean.Clothes["bodysuit"].string in ["red_swimsuit"] and Jean.Clothes["bodysuit"].state in [1, 3]:
        "characters/Jean/images/standing/bodysuit_[Jean.Clothes[bodysuit].string]_1.webp"
    else:
        "characters/Jean/images/standing/bodysuit_[Jean.Clothes[bodysuit].string]_[Jean.Clothes[bodysuit].state].webp"

    if Jean.Clothes["top"].string:
        "characters/Jean/images/standing/top_[Jean.Clothes[top].string]_[Jean.Clothes[top].state].webp"

layeredimage Jean_standing_left_arm:
    always:
        "characters/Jean/images/standing/left_arm_[Jean.left_arm].webp"

    anchor (int(1600*character_sampling), int(1550*character_sampling))
    offset (int(1600*character_sampling), int(1550*character_sampling))

layeredimage Jean_standing_left_sleeve:
    if Jean.Clothes["bodysuit"].string not in ["blueyellow_classic_suit"]:
        Null()
    elif Jean.left_arm == "fist":
        "characters/Jean/images/standing/bodysuit_[Jean.Clothes[bodysuit].string]_left_sleeve_neutral.webp"
    else:
        "characters/Jean/images/standing/bodysuit_[Jean.Clothes[bodysuit].string]_left_sleeve_[Jean.left_arm].webp"

    if not Jean.Clothes["gloves"].string:
        Null()
    elif Jean.left_arm in ["crossed", "fist", "hip", "neutral"]:
        "characters/Jean/images/standing/gloves_[Jean.Clothes[gloves].string]_left_[Jean.left_arm].webp"

    if not Jean.Clothes["top"].string:
        Null()
    elif Jean.left_arm == "fist":
        "characters/Jean/images/standing/top_[Jean.Clothes[top].string]_left_sleeve_neutral.webp"
    else:
        "characters/Jean/images/standing/top_[Jean.Clothes[top].string]_left_sleeve_[Jean.left_arm].webp"

    if not Jean.Clothes["sleeves"].string:
        Null()
    elif Jean.left_arm == "fist":
        "characters/Jean/images/standing/sleeves_[Jean.Clothes[sleeves].string]_left_neutral.webp"
    elif Jean.left_arm in ["crossed", "hip", "neutral"]:
        "characters/Jean/images/standing/sleeves_[Jean.Clothes[sleeves].string]_left_[Jean.left_arm].webp"

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