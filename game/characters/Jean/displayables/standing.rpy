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
                ease 2.0 xzoom 0.98
            choice:
                ease 2.0 xzoom 1.0
            choice:
                ease 2.0 yzoom 1.02
            choice:
                ease 2.0 yzoom 1.0

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
        
    xysize (int(1650*character_sampling), int(3550*character_sampling))

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

    if renpy.get_screen("Wardrobe_screen"):
        "Jean_standing_hair_back"
    else:
        At("Jean_standing_hair_back", Jean_standing_head_animation)

    if Jean.Clothes["jacket"].string in ["black_trenchcoat", "puffy_jacket"]:
        "characters/Jean/images/standing/jacket_[Jean.Clothes[jacket].string]_back.webp"
        
    if Jean.Clothes["neck"].string == "maroon_scarf":
        "characters/Jean/images/standing/neck_maroon_scarf_back.webp"

    if renpy.get_screen("Wardrobe_screen"):
        "Jean_standing_right_arm"
    else:
        At("Jean_standing_right_arm", Jean_standing_right_arm_animation)

    if Jean.Clothes["jacket"].string:
        "characters/Jean/images/standing/jacket_[Jean.Clothes[jacket].string]_mid.webp"

    always:
        "Jean_standing_body"

    if renpy.get_screen("Wardrobe_screen"):
        "Jean_standing_left_arm"
    else:
        At("Jean_standing_left_arm", Jean_standing_left_arm_animation)

    if Jean.Clothes["neck"].string == "maroon_scarf":
        "characters/Jean/images/standing/neck_maroon_scarf_side.webp"

    if Jean.Clothes["bodysuit"].string == "Jean_suit":
        "characters/Jean/images/standing/bodysuit_Jean_suit_pauldrons.webp"

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
    if Jean.wet or Jean.Clothes["hair"].string in ["sleeked", "wet"]:
        "characters/Jean/images/standing/hair_back_wet.webp"
    else:
        "characters/Jean/images/standing/hair_back.webp"

    anchor (int(869*character_sampling), int(725*character_sampling))
    offset (int(869*character_sampling), int(725*character_sampling))

layeredimage Jean_standing_head:
    if Jean.Clothes["face_outer_accessory"].string == "white_hat": 
        "characters/Jean/images/standing/face_outer_accessory_white_hat_back.webp"

    always:
        "characters/Jean/images/standing/head.webp"

    always:
        "characters/Jean/images/standing/mouth_[Jean.mouth].webp"

    if Jean.eyes in ["closed", "down", "left", "right", "squint", "up"]:
        "characters/Jean/images/standing/eyes_[Jean.eyes].webp"
    else:
        "Jean_standing_blinking"

    always:
        "characters/Jean/images/standing/brows_[Jean.brows].webp"

    if Jean.blush:
        "characters/Jean/images/standing/blush[Jean.blush].webp"
        
    if Jean.Clothes["makeup"].string:
        "characters/Jean/images/standing/makeup_[Jean.Clothes[makeup].string].webp"

    if Jean.Clothes["face_inner_accessory"].string:
        "characters/Jean/images/standing/face_inner_accessory_[Jean.Clothes[face_inner_accessory].string].webp"
        
    always:
        "characters/Jean/images/standing/hair_shadow.webp"

    if Jean.wet or Jean.Clothes["hair"].string == "wet":
        "characters/Jean/images/standing/hair_wet.webp"
    else:
        "characters/Jean/images/standing/hair_[Jean.Clothes[hair].string].webp"

    if Jean.Clothes["face_outer_accessory"].string == "white_hat":
        "characters/Jean/images/standing/face_outer_accessory_white_hat.webp"
        
    if Jean.spunk["tongue"] and Jean.mouth in ["agape", "tongue"]:
        "characters/Jean/images/standing/spunk_tongue.webp"

    if Jean.spunk["mouth"] and Jean.mouth in ["agape", "tongue"]:
        "characters/Jean/images/standing/spunk_mouth.webp"
        
    if not Jean.spunk["chin"]:
        Null()
    elif Jean.mouth in ["agape", "tongue"]: 
        "characters/Jean/images/standing/spunk_chin_open.webp"
    else: 
        "characters/Jean/images/standing/spunk_chin.webp"
        
    if Jean.spunk["face"]:
        "characters/Jean/images/standing/spunk_face.webp"

    if Jean.spunk["hair"]:
        "characters/Jean/images/standing/spunk_hair.webp"

    if Jean.psychic and Jean.activating_psychic:
        At("Jean_standing_psychic", Jean_standing_activating_psychic_animation)
    elif Jean.psychic:
        At("Jean_standing_psychic", Jean_standing_psychic_animation)
    elif Jean.deactivating_psychic:
        At("Jean_standing_psychic", Jean_standing_deactivating_psychic_animation)

    anchor (int(869*character_sampling), int(725*character_sampling))
    offset (int(869*character_sampling), int(725*character_sampling))

image Jean_standing_psychic:
    "characters/Jean/images/standing/psychic.webp"

    anchor (int(753*character_sampling), int(484*character_sampling))
    offset (int(753*character_sampling), int(484*character_sampling))

layeredimage Jean_standing_right_arm:
    always:
        "characters/Jean/images/standing/right_arm[Jean.right_arm_pose].webp"

    if Jean.Clothes["bodysuit"].string == "Jean_suit":
        "characters/Jean/images/standing/bodysuit_Jean_suit_right_sleeve[Jean.right_arm_pose].webp"

    if Jean.Clothes["gloves"].string:
        "characters/Jean/images/standing/gloves_[Jean.Clothes[gloves].string]_right[Jean.right_arm_pose].webp"

    if not Jean.Clothes["top"].string or Jean.Clothes["top"].string == "white_cami":
        Null()
    elif Jean.Clothes["jacket"].string and Jean.Clothes["top"].string != "white_sweater":
        Null()
    else:
        "characters/Jean/images/standing/top_[Jean.Clothes[top].string]_right_sleeve[Jean.right_arm_pose].webp"

    if Jean.Clothes["sleeves"].string:
        "characters/Jean/images/standing/sleeves_[Jean.Clothes[sleeves].string]_right[Jean.right_arm_pose].webp"

    if Jean.Clothes["jacket"].string:
        "characters/Jean/images/standing/jacket_[Jean.Clothes[jacket].string]_right_sleeve[Jean.right_arm_pose].webp"

    if Jean.spunk["hand"]:
        "characters/Jean/images/standing/spunk_right_hand[Jean.right_arm_pose].webp"

    anchor (int(588*character_sampling), int(980*character_sampling))
    offset (int(588*character_sampling), int(980*character_sampling))

layeredimage Jean_standing_body:
    always:
        "characters/Jean/images/standing/body.webp"

    if Jean.Clothes["jacket"].string == "black_trenchcoat":
        "characters/Jean/images/standing/jacket_black_trenchcoat_mid.webp"

    always:
        "characters/Jean/images/standing/breasts.webp"

    if Jean.tan_lines["full"]:
        "characters/Jean/images/standing/tan_lines_[Jean.tan_lines[full]].webp"

    if Jean.tan_lines["bottom"]:
        "characters/Jean/images/standing/tan_lines_[Jean.tan_lines[bottom]].webp"

    if Jean.tan_lines["top"]:
        "characters/Jean/images/standing/tan_lines_[Jean.tan_lines[top]].webp"

    if Jean.piercings["labia"] in ["barbell", "both"]:
        "characters/Jean/images/standing/labia_piercings_barbell.webp"

    if Jean.piercings["labia"] in ["ring", "both"]:
        "characters/Jean/images/standing/labia_piercings_ring.webp"

    if Jean.piercings["belly"]:
        "characters/Jean/images/standing/belly_piercing.webp"

    if Jean.piercings["nipple"] in ["barbell", "both"]:
        "characters/Jean/images/standing/nipple_piercings_barbell.webp"

    if Jean.piercings["nipple"] in ["ring", "both"]:
        "characters/Jean/images/standing/nipple_piercings_ring.webp"

    if Jean.Clothes["nipple_accessories"].string:
        "characters/Jean/images/standing/nipple_accessories_[Jean.Clothes[nipple_accessories].string].webp"

    if Jean.pubes_growing:
        "characters/Jean/images/standing/pubes_growing.webp"

    if Jean.pubes:
        "characters/Jean/images/standing/pubes_[Jean.pubes].webp"

    if Jean.remote_vibrator:
        "characters/Jean/images/standing/remote_vibrator.webp"

    if Jean.creampie["pussy"]:
        "characters/Jean/images/standing/creampie.webp"

    if Jean.Clothes["socks"].string:
        "characters/Jean/images/standing/socks_[Jean.Clothes[socks].string].webp"

    if Jean.Clothes["underwear"].string:
        "characters/Jean/images/standing/underwear_[Jean.Clothes[underwear].string]_[Jean.Clothes[underwear].state].webp"

    if Jean.Clothes["hose"].string:
        "characters/Jean/images/standing/hose_[Jean.Clothes[hose].string].webp"

    if Jean.Clothes["bra"].string and (Jean.Clothes["bodysuit"].string != "Jean_suit" or Jean.Clothes["bodysuit"].state == 1):
        "characters/Jean/images/standing/bra_[Jean.Clothes[bra].string]_[Jean.Clothes[bra].state].webp"

    if Jean.Clothes["bodysuit"].string:
        "characters/Jean/images/standing/bodysuit_[Jean.Clothes[bodysuit].string]_[Jean.Clothes[bodysuit].state].webp"

    if Jean.piercings["labia"] not in ["barbell", "both"]:
        Null()
    elif Jean.Clothes["bodysuit"].string:
        "characters/Jean/images/standing/labia_piercings_barbell_covered_[Jean.Clothes[bodysuit].string].webp"
    elif Jean.Clothes["underwear"].string and Jean.Clothes["underwear"].state == 0:
        "characters/Jean/images/standing/labia_piercings_barbell_covered_[Jean.Clothes[underwear].string].webp"

    if Jean.piercings["labia"] not in ["ring", "both"]:
        Null()
    elif Jean.Clothes["bodysuit"].string:
        "characters/Jean/images/standing/labia_piercings_ring_covered_[Jean.Clothes[bodysuit].string].webp"
    elif Jean.Clothes["underwear"].string and Jean.Clothes["underwear"].state == 0:
        "characters/Jean/images/standing/labia_piercings_ring_covered_[Jean.Clothes[underwear].string].webp"

    if Jean.piercings["belly"] and Jean.Clothes["bodysuit"].string:
        "characters/Jean/images/standing/belly_piercing_covered_[Jean.Clothes[bodysuit].string].webp"

    if not Jean.grool:
        Null()
    elif Jean.Clothes["bodysuit"].string:
        "characters/Jean/images/standing/grool_[Jean.Clothes[bodysuit].string].webp"
    elif Jean.Clothes["underwear"].string:
        "characters/Jean/images/standing/grool_[Jean.Clothes[underwear].string]_[Jean.Clothes[underwear].state].webp"

    if Jean.Clothes["pants"].string:
        "characters/Jean/images/standing/pants_[Jean.Clothes[pants].string]_[Jean.Clothes[pants].state].webp"

    if Jean.Clothes["boots"].string:
        "characters/Jean/images/standing/boots_[Jean.Clothes[boots].string].webp"

    if Jean.Clothes["skirt"].string:
        "characters/Jean/images/standing/skirt_[Jean.Clothes[skirt].string]_[Jean.Clothes[skirt].state].webp"

    if Jean.Clothes["dress"].string:
        "characters/Jean/images/standing/dress_[Jean.Clothes[dress].string]_[Jean.Clothes[dress].state].webp"

    if Jean.Clothes["top"].string:
        "characters/Jean/images/standing/top_[Jean.Clothes[top].string]_[Jean.Clothes[top].state].webp"
        
    if Jean.piercings["nipple"] not in ["barbell", "both"]:
        Null()
    elif Jean.Clothes["top"].string in ["black_shirt", "pink_shirt"] and Jean.Clothes["top"].state == 0:
        "characters/Jean/images/standing/nipple_piercings_barbell_covered_[Jean.Clothes[top].string].webp"
    elif Jean.Clothes["top"].string in ["college_shirt", "white_sweater"] and Jean.Clothes["top"].state == 0:
        Null()
    elif Jean.Clothes["dress"].string and Jean.Clothes["dress"].state == 0:
        "characters/Jean/images/standing/nipple_piercings_barbell_covered_[Jean.Clothes[dress].string].webp"
    elif Jean.Clothes["bodysuit"].string and Jean.Clothes["bodysuit"].state == 0:
        "characters/Jean/images/standing/nipple_piercings_barbell_covered_[Jean.Clothes[bodysuit].string].webp"
    elif Jean.Clothes["bra"].string and Jean.Clothes["bra"].state == 0:
        "characters/Jean/images/standing/nipple_piercings_barbell_covered_[Jean.Clothes[bra].string].webp"
    elif Jean.Clothes["nipple_accessories"].string:
        "characters/Jean/images/standing/nipple_piercings_barbell_covered_[Jean.Clothes[nipple_accessories].string].webp"
        
    if Jean.piercings["nipple"] not in ["ring", "both"]:
        Null()
    elif Jean.Clothes["top"].string in ["black_shirt", "pink_shirt"] and Jean.Clothes["top"].state == 0:
        "characters/Jean/images/standing/nipple_piercings_ring_covered_[Jean.Clothes[top].string].webp"
    elif Jean.Clothes["top"].string in ["college_shirt", "white_sweater"] and Jean.Clothes["top"].state == 0:
        Null()
    elif Jean.Clothes["dress"].string and Jean.Clothes["dress"].state == 0:
        "characters/Jean/images/standing/nipple_piercings_ring_covered_[Jean.Clothes[dress].string].webp"
    elif Jean.Clothes["bodysuit"].string and Jean.Clothes["bodysuit"].state == 0:
        "characters/Jean/images/standing/nipple_piercings_ring_covered_[Jean.Clothes[bodysuit].string].webp"
    elif Jean.Clothes["bra"].string and Jean.Clothes["bra"].state == 0:
        "characters/Jean/images/standing/nipple_piercings_ring_covered_[Jean.Clothes[bra].string].webp"
    elif Jean.Clothes["nipple_accessories"].string:
        "characters/Jean/images/standing/nipple_piercings_ring_covered_[Jean.Clothes[nipple_accessories].string].webp"

    if Jean.Clothes["neck"].string:
        "characters/Jean/images/standing/neck_[Jean.Clothes[neck].string].webp"

    if Jean.Clothes["belt"].string:
        "characters/Jean/images/standing/belt_[Jean.Clothes[belt].string].webp"

    if Jean.Clothes["jacket"].string:
        "characters/Jean/images/standing/jacket_[Jean.Clothes[jacket].string]_[Jean.Clothes[jacket].state].webp"

    if Jean.Clothes["towel"].string:
        "characters/Jean/images/standing/towel_[Jean.Clothes[towel].string]_[Jean.Clothes[towel].state].webp"

    if Jean.spunk["belly"]:
        "characters/Jean/images/standing/spunk_belly.webp"

    if Jean.spunk["breasts"]:
        "characters/Jean/images/standing/spunk_breasts.webp"

    anchor (int(713*character_sampling), int(1719*character_sampling))
    offset (int(713*character_sampling), int(1719*character_sampling))

layeredimage Jean_standing_left_arm:
    always:
        "characters/Jean/images/standing/left_arm.webp"

    if Jean.Clothes["bodysuit"].string == "Jean_suit":
        "characters/Jean/images/standing/bodysuit_Jean_suit_left_sleeve.webp"
        
    if Jean.Clothes["gloves"].string:
        "characters/Jean/images/standing/gloves_[Jean.Clothes[gloves].string]_left.webp"
        
    if not Jean.Clothes["top"].string or Jean.Clothes["top"].string == "white_cami":
        Null()
    elif Jean.Clothes["jacket"].string and Jean.Clothes["top"].string != "white_sweater":
        Null()
    else:
        "characters/Jean/images/standing/top_[Jean.Clothes[top].string]_left_sleeve.webp"

    if Jean.Clothes["sleeves"].string:
        "characters/Jean/images/standing/sleeves_[Jean.Clothes[sleeves].string]_left.webp"

    if not Jean.Clothes["jacket"].string:
        Null()
    elif Jean.Clothes["jacket"].string == "denim_jacket":
        "characters/Jean/images/standing/jacket_denim_jacket_left_sleeve_[Jean.Clothes[jacket].state].webp"
    else:
        "characters/Jean/images/standing/jacket_[Jean.Clothes[jacket].string]_left_sleeve.webp"

    anchor (int(1139*character_sampling), int(904*character_sampling))
    offset (int(1139*character_sampling), int(904*character_sampling))

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