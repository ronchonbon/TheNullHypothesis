transform Laura_standing_head_animation:
    subpixel True
    transform_anchor True
    animation
    
    pos (0.0, 0.0)
    xzoom 1.0 yzoom 1.0
    rotate 0.0

    block:
        pause 4.3
        ease 2.0 rotate -1
        pause 3.4
        ease 2.0 rotate 0
        pause 6.8
        ease 2.0 rotate 1

        repeat

transform Laura_standing_right_arm_animation:
    subpixel True
    transform_anchor True
    animation
    
    pos (0.0, 0.0)
    xzoom 1.0 yzoom 1.0
    rotate 0.0

    block:
        pause 4.1
        ease 2.0 rotate 0
        pause 5.7
        ease 2.0 rotate -2
        pause 4.6
        ease 2.0 rotate -1

        repeat

transform Laura_standing_left_arm_animation:
    subpixel True
    transform_anchor True
    animation
    
    pos (0.0, 0.0)
    xzoom 1.0 yzoom 1.0
    rotate 0.0

    block:
        pause 6.2
        ease 2.0 rotate 0
        pause 4.1
        ease 2.0 rotate 2
        pause 6.4
        ease 2.0 rotate 1

        repeat

transform Laura_standing_right_claws_unsheathe_animation:
    subpixel True
    transform_anchor True

    zoom 0.0
    ease 0.1 zoom 1.0

transform Laura_standing_right_claws_sheathe_animation:
    subpixel True
    transform_anchor True

    zoom 1.0
    ease 0.2 zoom 0.0

transform Laura_standing_left_claws_unsheathe_animation:
    subpixel True
    transform_anchor True

    zoom 0.0
    ease 0.1 zoom 1.0

transform Laura_standing_left_claws_sheathe_animation:
    subpixel True
    transform_anchor True

    zoom 1.0
    ease 0.2 zoom 0.0
    
image Laura_sprite standing:
    contains:
        "Laura_standing_temp"

    xysize (int(2500*character_sampling), int(4500*character_sampling))

layeredimage Laura_standing_temp:
    if Laura.hovered:
        "Laura_standing" at hover
    elif Rogue.check_traits("orgasming"):
        "Laura_standing" at tremble(20)
    else:
        "Laura_standing"

layeredimage Laura_standing:
    if not Player.left_hand_Actions or Laura not in Player.left_hand_Actions[0].Targets:
        Null()
    elif Player.left_hand_Actions[0].animation_type == "grab_ass":
        "Laura_standing_male_left_arm_grab_ass_animation[Player.left_hand_Actions[0].mode]" at Transform(offset = (Laura_standing_ass_position[0], Laura_standing_ass_position[1]))

    if not Player.right_hand_Actions or Laura not in Player.right_hand_Actions[0].Targets:
        Null()
    elif Player.right_hand_Actions[0].animation_type == "grab_ass":
        "Laura_standing_male_right_arm_grab_ass_animation[Player.right_hand_Actions[0].mode]" at Transform(offset = (Laura_standing_ass_position[0], Laura_standing_ass_position[1]))

    if Laura.check_traits("ground_shadow"):
        "characters/Laura/images/standing/ground_shadow.webp" at Transform(blend = "multiply")

    if renpy.get_screen("Wardrobe_screen"):
        "Laura_standing_hair_back"
    else:
        "Laura_standing_hair_back" at Laura_standing_head_animation

    if Laura.left_arm in ["bra", "touch_ass"]:
        "characters/Laura/images/standing/left_forearm_[Laura.left_arm].webp"

    if Laura.right_arm not in ["bra", "claws", "crossed", "extended", "fight", "fist", "hip", "neutral", "touch_pussy", "X"]:
        Null()
    elif renpy.get_screen("Wardrobe_screen"):
        "Laura_standing_right_arm"
    elif Laura.right_arm == "neutral":
        "Laura_standing_right_arm" at Laura_standing_right_arm_animation
    else:
        "Laura_standing_right_arm"

    always:
        "Laura_standing_body"

    if Laura.left_arm in ["grope", "hip"]:
        "characters/Laura/images/standing/left_arm_[Laura.left_arm]_shadow.webp" at Transform(blend = "multiply")

    if Laura.left_arm not in ["bra", "claws", "crossed", "fight", "fist", "grope", "hip", "neutral", "touch_ass", "X"]:
        Null()
    elif renpy.get_screen("Wardrobe_screen"):
        "Laura_standing_left_arm"
    elif Laura.left_arm == "neutral":
        "Laura_standing_left_arm" at Laura_standing_left_arm_animation
    else:
        "Laura_standing_left_arm"

    if Laura.right_arm in ["hip", "touch_pussy"]:
        "characters/Laura/images/standing/right_forearm_[Laura.right_arm]_shadow.webp" at Transform(blend = "multiply")

    if Laura.right_arm in ["hip", "touch_pussy"]:
        "characters/Laura/images/standing/right_forearm_[Laura.right_arm].webp"

    if Laura.Clothes["hair"].string in ["tucked"]:
        "characters/Laura/images/standing/hair_tucked_mid.webp"

    if Laura.Clothes["hair"].string in ["tucked"]:
        "characters/Laura/images/standing/hair_tucked_mid_shadow.webp" at Transform(blend = "multiply")

    if not Player.left_hand_Actions or Laura not in Player.left_hand_Actions[0].Targets:
        Null()
    elif Player.left_hand_Actions[0].animation_type == "choke":
        "Laura_standing_male_left_arm_choke_animation[Player.left_hand_Actions[0].mode]" at Transform(offset = (Laura_standing_neck_position[0], Laura_standing_neck_position[1]))

    if not Player.right_hand_Actions or Laura not in Player.right_hand_Actions[0].Targets:
        Null()
    elif Player.right_hand_Actions[0].animation_type == "choke":
        "Laura_standing_male_right_arm_choke_animation[Player.right_hand_Actions[0].mode]" at Transform(offset = (Laura_standing_neck_position[0], Laura_standing_neck_position[1]))

    if renpy.get_screen("Wardrobe_screen"):
        "Laura_standing_head"
    else:
        "Laura_standing_head" at Laura_standing_head_animation

    if Laura.left_arm in ["extended"]:
        "characters/Laura/images/standing/left_arm_[Laura.left_arm].webp"

    if Laura.right_arm in ["extended", "fight", "X"]:
        "characters/Laura/images/standing/right_forearm_[Laura.right_arm].webp"

    if Laura.left_arm == "X" and Laura.right_arm == "X":
        "characters/Laura/images/standing/left_forearm_X_shadow.webp" at Transform(blend = "multiply")

    if not Laura.check_traits("right_claw") or Laura.Clothes["gloves"].string:
        Null()
    elif Laura.right_arm in ["fight", "X"]:
        "characters/Laura/images/standing/claws_right_[Laura.right_arm]_shadow.webp" at Transform(blend = "multiply")

    if not Laura.check_traits("right_claw"):
        Null()
    elif Laura.right_arm in ["fight", "X"]:
        "characters/Laura/images/standing/claws_right_[Laura.right_arm].webp"

    if Laura.left_arm in ["rub_neck"]:
        "characters/Laura/images/standing/left_forearm_[Laura.left_arm]_shadow.webp" at Transform(blend = "multiply")

    if Laura.left_arm in ["fight", "rub_neck", "X"]:
        "characters/Laura/images/standing/left_forearm_[Laura.left_arm].webp"

    if not Laura.check_traits("left_claw") or Laura.Clothes["gloves"].string:
        Null()
    elif Laura.left_arm in ["fight", "X"]:
        "characters/Laura/images/standing/claws_left_[Laura.left_arm]_shadow.webp"

    if not Laura.check_traits("left_claw"):
        Null()
    elif Laura.left_arm in ["fight", "X"]:
        "characters/Laura/images/standing/claws_left_[Laura.left_arm].webp"

    if Laura.spunk["hand"] and Laura.right_arm in ["extended"]:
        "characters/Laura/images/standing/spunk_hand1.webp"

    if Laura.spunk["hand"] == 2 and Laura.right_arm in ["extended"]:
        "characters/Laura/images/standing/spunk_hand2.webp"

    if not Player.left_hand_Actions or Laura not in Player.left_hand_Actions[0].Targets:
        Null()
    elif Player.left_hand_Actions[0].animation_type == "touch_breasts" and Laura.right_breast_Actions and Player.left_hand_Actions[0].animation_type == Laura.right_breast_Actions[0].animation_type:
        "Laura_standing_male_left_arm_touch_right_breast_animation[Player.left_hand_Actions[0].mode]" at change_offset(Laura_standing_right_breast_position[0], Laura_standing_right_breast_position[1])
    elif Player.left_hand_Actions[0].animation_type == "touch_breasts" and Laura.left_breast_Actions and Player.left_hand_Actions[0].animation_type == Laura.left_breast_Actions[0].animation_type:
        "Laura_standing_male_left_arm_touch_left_breast_animation[Player.left_hand_Actions[0].mode]" at change_offset(Laura_standing_left_breast_position[0], Laura_standing_left_breast_position[1])
    elif Player.left_hand_Actions[0].animation_type == "pinch_nipples" and Laura.right_nipple_Actions and Player.left_hand_Actions[0].animation_type == Laura.right_nipple_Actions[0].animation_type:
        "Laura_standing_male_left_arm_touch_right_breast_animation[Player.left_hand_Actions[0].mode]" at change_offset(Laura_standing_right_nipple_position[0], Laura_standing_right_nipple_position[1])
    elif Player.left_hand_Actions[0].animation_type == "pinch_nipples" and Laura.left_nipple_Actions and Player.left_hand_Actions[0].animation_type == Laura.left_nipple_Actions[0].animation_type:
        "Laura_standing_male_left_arm_touch_left_breast_animation[Player.left_hand_Actions[0].mode]" at change_offset(Laura_standing_left_nipple_position[0], Laura_standing_left_nipple_position[1])
    elif Player.left_hand_Actions[0].animation_type == "touch_thighs":
        "Laura_standing_male_left_arm_touch_thighs_animation[Player.left_hand_Actions[0].mode]" at change_offset(Laura_standing_thigh_position[0], Laura_standing_thigh_position[1])
    elif Player.left_hand_Actions[0].animation_type == "touch_thighs_higher":
        "Laura_standing_male_left_arm_touch_thighs_higher_animation[Player.left_hand_Actions[0].mode]" at change_offset(Laura_standing_thigh_higher_position[0], Laura_standing_thigh_higher_position[1])
    elif Player.left_hand_Actions[0].animation_type == "touch_pussy":
        "Laura_standing_male_left_arm_touch_pussy_animation[Player.left_hand_Actions[0].mode]" at change_offset(Laura_standing_pussy_position[0], Laura_standing_pussy_position[1])

    if not Player.right_hand_Actions or Laura not in Player.right_hand_Actions[0].Targets:
        Null()
    elif Player.right_hand_Actions[0].animation_type == "touch_breasts" and Laura.right_breast_Actions and Player.right_hand_Actions[0].animation_type == Laura.right_breast_Actions[0].animation_type:
        "Laura_standing_male_right_arm_touch_right_breast_animation[Player.right_hand_Actions[0].mode]" at change_offset(Laura_standing_right_breast_position[0], Laura_standing_right_breast_position[1])
    elif Player.right_hand_Actions[0].animation_type == "touch_breasts" and Laura.left_breast_Actions and Player.right_hand_Actions[0].animation_type == Laura.left_breast_Actions[0].animation_type:
        "Laura_standing_male_right_arm_touch_left_breast_animation[Player.right_hand_Actions[0].mode]" at change_offset(Laura_standing_left_breast_position[0], Laura_standing_left_breast_position[1])
    elif Player.right_hand_Actions[0].animation_type == "pinch_nipples" and Laura.right_nipple_Actions and Player.right_hand_Actions[0].animation_type == Laura.right_nipple_Actions[0].animation_type:
        "Laura_standing_male_right_arm_touch_right_breast_animation[Player.right_hand_Actions[0].mode]" at change_offset(Laura_standing_right_nipple_position[0], Laura_standing_right_nipple_position[1])
    elif Player.right_hand_Actions[0].animation_type == "pinch_nipples" and Laura.left_nipple_Actions and Player.right_hand_Actions[0].animation_type == Laura.left_nipple_Actions[0].animation_type:
        "Laura_standing_male_right_arm_touch_left_breast_animation[Player.right_hand_Actions[0].mode]" at change_offset(Laura_standing_left_nipple_position[0], Laura_standing_left_nipple_position[1])
    elif Player.right_hand_Actions[0].animation_type == "touch_thighs":
        "Laura_standing_male_right_arm_touch_thighs_animation[Player.right_hand_Actions[0].mode]" at change_offset(Laura_standing_thigh_position[0], Laura_standing_thigh_position[1])
    elif Player.right_hand_Actions[0].animation_type == "touch_thighs_higher":
        "Laura_standing_male_right_arm_touch_thighs_higher_animation[Player.right_hand_Actions[0].mode]" at change_offset(Laura_standing_thigh_higher_position[0], Laura_standing_thigh_higher_position[1])
    elif Player.right_hand_Actions[0].animation_type == "touch_pussy":
        "Laura_standing_male_right_arm_touch_pussy_animation[Player.right_hand_Actions[0].mode]" at change_offset(Laura_standing_pussy_position[0], Laura_standing_pussy_position[1])

    if not Player.mouth_Actions or Laura not in Player.mouth_Actions[0].Targets:
        Null()
    elif Player.mouth_Actions[0].animation_type in ["suck_nipples"] and Laura.left_nipple_Actions and Player.mouth_Actions[0].animation_type == Laura.left_nipple_Actions[0].animation_type:
        "Laura_standing_male_head_suck_left_nipple_animation[Player.mouth_Actions[0].mode]" at Transform(offset = (Laura_standing_left_nipple_position[0], Laura_standing_left_nipple_position[1]))
    elif Player.mouth_Actions[0].animation_type in ["suck_nipples"] and Laura.right_nipple_Actions and Player.mouth_Actions[0].animation_type == Laura.right_nipple_Actions[0].animation_type:
        "Laura_standing_male_head_suck_right_nipple_animation[Player.mouth_Actions[0].mode]" at Transform(offset = (Laura_standing_right_nipple_position[0], Laura_standing_right_nipple_position[1]))

layeredimage Laura_standing_hair_back:
    always:
        "characters/Laura/images/standing/hair_back_[Laura.Clothes[hair].string].webp"

    anchor (int(1300*character_sampling), int(1490*character_sampling))
    offset (int(1300*character_sampling), int(1490*character_sampling))

layeredimage Laura_standing_right_arm:
    if not Laura.check_traits("right_claw"):
        Null()
    elif Laura.right_arm in ["claws", "fist"]:
        "characters/Laura/images/standing/claws_right_[Laura.right_arm].webp"

    always:
        "characters/Laura/images/standing/right_arm_[Laura.right_arm].webp"

    anchor (int(1075*character_sampling), int(1760*character_sampling))
    offset (int(1075*character_sampling), int(1760*character_sampling))

layeredimage Laura_standing_body:
    always:
        "characters/Laura/images/standing/body.webp"

    always:
        "characters/Laura/images/standing/right_foot.webp"

    always:
        "characters/Laura/images/standing/left_foot.webp"

    if Laura.piercings["labia"] in ["barbell", "both"]:
        "characters/Laura/images/standing/labia_piercings_barbell.webp"

    if Laura.piercings["labia"] in ["ring", "both"]:
        "characters/Laura/images/standing/labia_piercings_ring.webp"

    if "pubic" in Laura.body_hair_growing.keys():
        "characters/Laura/images/standing/pubes_growing.webp"

    if Laura.body_hair["pubic"]:
        "characters/Laura/images/standing/pubes_[Laura.body_hair[pubic]].webp"

    if Laura.desire >= 75 or Laura.History.check("orgasmed", tracker = "recent"):
        "characters/Laura/images/standing/grool.webp"
    elif Laura.desire >= 50:
        "characters/Laura/images/standing/grool.webp" at Transform(alpha = 0.5)
    elif Laura.desire >= 25:
        "characters/Laura/images/standing/grool.webp" at Transform(alpha = 0.1)

    if Laura.creampie["pussy"]:
        "characters/Laura/images/standing/creampie1.webp"

    if Laura.creampie["pussy"] == 2:
        "characters/Laura/images/standing/creampie2.webp"

    if Laura.remote_vibrator is None:
        Null()
    elif Laura.remote_vibrator > 0.0:
        "characters/Laura/images/standing/remote_vibrator.webp" at vibrating
    else:
        "characters/Laura/images/standing/remote_vibrator.webp"

    if Laura.piercings["belly"]:
        "characters/Laura/images/standing/belly_piercing.webp"

    if Laura.spunk["belly"]:
        "characters/Laura/images/standing/spunk_belly1.webp"

    if Laura.spunk["belly"] == 2:
        "characters/Laura/images/standing/spunk_belly2.webp"

    always:
        "characters/Laura/images/standing/breasts_shadow.webp" at Transform(blend = "multiply")

    always:
        "characters/Laura/images/standing/breasts.webp"

    if Laura.left_arm == "grope":
        "characters/Laura/images/standing/breasts_grope_shadow.webp" at Transform(blend = "multiply")

    if Laura.left_arm == "grope":
        "characters/Laura/images/standing/breasts_grope.webp"

    if Laura.piercings["nipple"] not in ["barbell", "both"]:
        Null()
    elif Laura.left_arm == "grope":
        "characters/Laura/images/standing/nipple_piercings_barbell_grope.webp"
    else:
        "characters/Laura/images/standing/nipple_piercings_barbell.webp"

    if Laura.piercings["nipple"] not in ["ring", "both"]:
        Null()
    elif Laura.left_arm == "grope":
        "characters/Laura/images/standing/nipple_piercings_ring_grope.webp"
    else:
        "characters/Laura/images/standing/nipple_piercings_ring.webp"

    if Laura.spunk["breasts"]:
        "characters/Laura/images/standing/spunk_breasts1.webp"

    if Laura.spunk["breasts"] == 2:
        "characters/Laura/images/standing/spunk_breasts2.webp"

layeredimage Laura_standing_left_arm:
    if not Laura.check_traits("left_claw"):
        Null()
    elif Laura.left_arm in ["claws"]:
        "characters/Laura/images/standing/claws_left_[Laura.left_arm].webp"

    always:
        "characters/Laura/images/standing/left_arm_[Laura.left_arm].webp"

    if not Laura.check_traits("left_claw") or Laura.Clothes["gloves"].string:
        Null()
    elif Laura.left_arm in ["fist"]:
        "characters/Laura/images/standing/claws_left_[Laura.left_arm]_shadow.webp"

    if not Laura.check_traits("left_claw"):
        Null()
    elif Laura.left_arm in ["fist"]:
        "characters/Laura/images/standing/claws_left_[Laura.left_arm].webp"

    anchor (int(1575*character_sampling), int(1725*character_sampling))
    offset (int(1575*character_sampling), int(1725*character_sampling))

layeredimage Laura_standing_head:
    always:
        "characters/Laura/images/standing/head.webp"

    always:
        "characters/Laura/images/standing/mouth_[Laura.mouth].webp"

    if Laura.eyes in ["closed", "down", "left", "right", "squint", "up", "wink"]:
        "characters/Laura/images/standing/eyes_[Laura.eyes].webp"
    else:
        "Laura_standing_blinking"

    always:
        "characters/Laura/images/standing/brows_[Laura.brows].webp"

    if Laura.blush:
        "characters/Laura/images/standing/blush[Laura.blush].webp"

    if Laura.spunk["mouth"] and Laura.mouth in ["agape", "open", "snarl"]:
        "characters/Laura/images/standing/spunk_mouth1_agape.webp"

    if Laura.spunk["mouth"] == 2 and Laura.mouth in ["agape", "open", "snarl"]:
        "characters/Laura/images/standing/spunk_mouth2_agape.webp"

    if Laura.spunk["mouth"] and Laura.mouth in ["tongue"]:
        "characters/Laura/images/standing/spunk_mouth1_tongue.webp"

    if Laura.spunk["mouth"] == 2 and Laura.mouth in ["tongue"]:
        "characters/Laura/images/standing/spunk_mouth2_tongue.webp"

    if not Laura.spunk["chin"]:
        Null()
    elif Laura.mouth in ["agape", "open", "snarl", "tongue"]:
        "characters/Laura/images/standing/spunk_chin1_open.webp"
    else:
        "characters/Laura/images/standing/spunk_chin1.webp"

    if Laura.spunk["chin"] != 2:
        Null()
    elif Laura.mouth in ["agape", "open", "snarl", "tongue"]:
        "characters/Laura/images/standing/spunk_chin2_open.webp"
    else:
        "characters/Laura/images/standing/spunk_chin2.webp"

    if Laura.spunk["face"]:
        "characters/Laura/images/standing/spunk_face1.webp"

    if Laura.spunk["face"] == 2:
        "characters/Laura/images/standing/spunk_face2.webp"

    # if Laura.Clothes["face_outer_accessory"].string:
    #     Null()
    if Laura.check_traits("wet") or Laura.Clothes["hair"].string == "wet":
        "characters/Laura/images/standing/hair_wet_shadow.webp" at Transform(blend = "multiply")
    else:
        "characters/Laura/images/standing/hair_[Laura.Clothes[hair].string]_shadow.webp" at Transform(blend = "multiply")

    # if Laura.Clothes["face_outer_accessory"].string:
    #     Null()
    if Laura.check_traits("wet") or Laura.Clothes["hair"].string == "wet":
        "characters/Laura/images/standing/hair_wet.webp"
    else:
        "characters/Laura/images/standing/hair_[Laura.Clothes[hair].string].webp"

    if Laura.spunk["hair"]:
        "characters/Laura/images/standing/spunk_hair1_[Laura.Clothes[hair].string].webp"

    if Laura.spunk["hair"] == 2:
        "characters/Laura/images/standing/spunk_hair2_[Laura.Clothes[hair].string].webp"

    anchor (int(1300*character_sampling), int(1490*character_sampling))
    offset (int(1300*character_sampling), int(1490*character_sampling))

image Laura_standing_blinking:
    "characters/Laura/images/standing/eyes_[Laura.eyes].webp"
    choice:
        4.5
    choice:
        4.0
    choice:
        3.5
    "characters/Laura/images/standing/eyes_blink1.webp"
    0.027
    "characters/Laura/images/standing/eyes_blink2.webp"
    0.027
    "characters/Laura/images/standing/eyes_closed.webp"
    0.054
    "characters/Laura/images/standing/eyes_blink2.webp"
    0.018
    "characters/Laura/images/standing/eyes_blink1.webp"
    0.072
    repeat

layeredimage Laura_standing_male_left_arm:
    if Player.left_hand_Actions[0].animation_type in ["touch_thighs", "touch_thighs_higher", "touch_breasts", "touch_pussy", "grab_ass"]:
        "Player_left_arm_fondle"
    elif Player.left_hand_Actions[0].animation_type in ["choke", "pinch_nipples"]:
        "Player_left_arm_pinch"

layeredimage Laura_standing_male_right_arm:
    if Player.right_hand_Actions[0].animation_type in ["touch_thighs", "touch_thighs_higher", "touch_breasts", "touch_pussy", "grab_ass"]:
        "Player_right_arm_fondle"
    elif Player.right_hand_Actions[0].animation_type in ["choke", "pinch_nipples"]:
        "Player_right_arm_pinch"

layeredimage Laura_standing_male_head:
    if Player.check_traits("body_visible"):
        "Player_head"

    if Player.mouth_Actions and Laura in Player.mouth_Actions[0].Targets and Player.mouth_Actions[0].animation_type in ["suck_nipples", "eat_pussy", "eat_ass"]:
        "Laura_standing_male_tongue_animation[Player.mouth_Actions[0].mode]"

image Laura_standing_male_tongue:
    "Player_tongue"
    
image Laura_standing_male_left_arm_choke_animation0:
    "Laura_standing_male_left_arm"

    standing_male_left_arm_choke_animation0

image Laura_standing_male_left_arm_choke_animation1:
    "Laura_standing_male_left_arm"

    standing_male_left_arm_choke_animation1

image Laura_standing_male_left_arm_touch_thighs_animation0:
    "Laura_standing_male_left_arm"

    standing_male_left_arm_touch_thighs_animation0

image Laura_standing_male_left_arm_touch_thighs_animation1:
    "Laura_standing_male_left_arm"

    standing_male_left_arm_touch_thighs_animation1

image Laura_standing_male_left_arm_touch_thighs_higher_animation0:
    "Laura_standing_male_left_arm"

    standing_male_left_arm_touch_thighs_higher_animation0

image Laura_standing_male_left_arm_touch_thighs_higher_animation1:
    "Laura_standing_male_left_arm"

    standing_male_left_arm_touch_thighs_higher_animation1

image Laura_standing_male_left_arm_touch_left_breast_animation0:
    "Laura_standing_male_left_arm"

    standing_male_left_arm_touch_left_breast_animation0

image Laura_standing_male_left_arm_touch_left_breast_animation1:
    "Laura_standing_male_left_arm"

    standing_male_left_arm_touch_left_breast_animation1

image Laura_standing_male_left_arm_touch_right_breast_animation0:
    "Laura_standing_male_left_arm"

    standing_male_left_arm_touch_right_breast_animation0

image Laura_standing_male_left_arm_touch_right_breast_animation1:
    "Laura_standing_male_left_arm"

    standing_male_left_arm_touch_right_breast_animation1

image Laura_standing_male_left_arm_touch_pussy_animation0:
    "Laura_standing_male_left_arm"

    standing_male_left_arm_touch_pussy_animation0

image Laura_standing_male_left_arm_touch_pussy_animation1:
    "Laura_standing_male_left_arm"

    standing_male_left_arm_touch_pussy_animation1

image Laura_standing_male_left_arm_grab_ass_animation0:
    "Laura_standing_male_left_arm"

    standing_male_left_arm_grab_ass_animation0

image Laura_standing_male_left_arm_grab_ass_animation1:
    "Laura_standing_male_left_arm"

    standing_male_left_arm_grab_ass_animation1
    
image Laura_standing_male_right_arm_choke_animation0:
    "Laura_standing_male_right_arm"

    standing_male_right_arm_choke_animation0

image Laura_standing_male_right_arm_choke_animation1:
    "Laura_standing_male_right_arm"

    standing_male_right_arm_choke_animation1

image Laura_standing_male_right_arm_touch_thighs_animation0:
    "Laura_standing_male_right_arm"

    standing_male_right_arm_touch_thighs_animation0

image Laura_standing_male_right_arm_touch_thighs_animation1:
    "Laura_standing_male_right_arm"

    standing_male_right_arm_touch_thighs_animation1

image Laura_standing_male_right_arm_touch_thighs_higher_animation0:
    "Laura_standing_male_right_arm"

    standing_male_right_arm_touch_thighs_higher_animation0

image Laura_standing_male_right_arm_touch_thighs_higher_animation1:
    "Laura_standing_male_right_arm"

    standing_male_right_arm_touch_thighs_higher_animation1

image Laura_standing_male_right_arm_touch_left_breast_animation0:
    "Laura_standing_male_right_arm"

    standing_male_right_arm_touch_left_breast_animation0

image Laura_standing_male_right_arm_touch_left_breast_animation1:
    "Laura_standing_male_right_arm"

    standing_male_right_arm_touch_left_breast_animation1

image Laura_standing_male_right_arm_touch_right_breast_animation0:
    "Laura_standing_male_right_arm"

    standing_male_right_arm_touch_right_breast_animation0

image Laura_standing_male_right_arm_touch_right_breast_animation1:
    "Laura_standing_male_right_arm"

    standing_male_right_arm_touch_right_breast_animation1

image Laura_standing_male_right_arm_touch_pussy_animation0:
    "Laura_standing_male_right_arm"

    standing_male_right_arm_touch_pussy_animation0

image Laura_standing_male_right_arm_touch_pussy_animation1:
    "Laura_standing_male_right_arm"

    standing_male_right_arm_touch_pussy_animation1

image Laura_standing_male_right_arm_grab_ass_animation0:
    "Laura_standing_male_right_arm"

    standing_male_right_arm_grab_ass_animation0

image Laura_standing_male_right_arm_grab_ass_animation1:
    "Laura_standing_male_right_arm"

    standing_male_right_arm_grab_ass_animation1

image Laura_standing_male_head_suck_left_nipple_animation0:
    "Laura_standing_male_head"

    standing_male_head_suck_left_nipple_animation0

image Laura_standing_male_head_suck_left_nipple_animation1:
    "Laura_standing_male_head"

    standing_male_head_suck_left_nipple_animation1

image Laura_standing_male_head_suck_right_nipple_animation0:
    "Laura_standing_male_head"

    standing_male_head_suck_right_nipple_animation0

image Laura_standing_male_head_suck_right_nipple_animation1:
    "Laura_standing_male_head"

    standing_male_head_suck_right_nipple_animation1

image Laura_standing_male_tongue_animation0:
    "Laura_standing_male_tongue"

    standing_male_tongue_animation0

image Laura_standing_male_tongue_animation1:
    "Laura_standing_male_tongue"

    standing_male_tongue_animation1