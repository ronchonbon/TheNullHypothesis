image Jean_sprite masturbation:
    contains:
        "Jean_masturbation_temp"

    offset (int(150*0.38), int(350*0.38))
            
layeredimage Jean_masturbation_temp:
    if Jean.hovered:
        At("Jean_masturbation_controls_temp", hover)
    else:
        "Jean_masturbation_controls_temp"
            
layeredimage Jean_masturbation_controls_temp:
    if speed > 2.5 or speed <= 1.75:
        Null()
    elif intensity >= 2.0:
        At(At("Jean_masturbation", speed_200), intensity_200)
    elif intensity >= 1.75:
        At(At("Jean_masturbation", speed_200), intensity_175)
    elif intensity >= 1.5:
        At(At("Jean_masturbation", speed_200), intensity_150)
    elif intensity >= 1.25:
        At(At("Jean_masturbation", speed_200), intensity_125)
    elif intensity >= 1.0:
        At(At("Jean_masturbation", speed_200), intensity_100)
    elif intensity >= 0.75:
        At(At("Jean_masturbation", speed_200), intensity_075)
    elif intensity >= 0.5:
        At(At("Jean_masturbation", speed_200), intensity_050)
    elif intensity >= 0.25:
        At(At("Jean_masturbation", speed_200), intensity_025)
    else:
        At(At("Jean_masturbation", speed_200), intensity_000)

    if speed > 1.75 or speed <= 1.5:
        Null()
    elif intensity >= 2.0:
        At(At("Jean_masturbation", speed_175), intensity_200)
    elif intensity >= 1.75:
        At(At("Jean_masturbation", speed_175), intensity_175)
    elif intensity >= 1.5:
        At(At("Jean_masturbation", speed_175), intensity_150)
    elif intensity >= 1.25:
        At(At("Jean_masturbation", speed_175), intensity_125)
    elif intensity >= 1.0:
        At(At("Jean_masturbation", speed_175), intensity_100)
    elif intensity >= 0.75:
        At(At("Jean_masturbation", speed_175), intensity_075)
    elif intensity >= 0.5:
        At(At("Jean_masturbation", speed_175), intensity_050)
    elif intensity >= 0.25:
        At(At("Jean_masturbation", speed_175), intensity_025)
    else:
        At(At("Jean_masturbation", speed_175), intensity_000)

    if speed > 1.5 or speed <= 1.25:
        Null()
    elif intensity >= 2.0:
        At(At("Jean_masturbation", speed_150), intensity_200)
    elif intensity >= 1.75:
        At(At("Jean_masturbation", speed_150), intensity_175)
    elif intensity >= 1.5:
        At(At("Jean_masturbation", speed_150), intensity_150)
    elif intensity >= 1.25:
        At(At("Jean_masturbation", speed_150), intensity_125)
    elif intensity >= 1.0:
        At(At("Jean_masturbation", speed_150), intensity_100)
    elif intensity >= 0.75:
        At(At("Jean_masturbation", speed_150), intensity_075)
    elif intensity >= 0.5:
        At(At("Jean_masturbation", speed_150), intensity_050)
    elif intensity >= 0.25:
        At(At("Jean_masturbation", speed_150), intensity_025)
    else:
        At(At("Jean_masturbation", speed_150), intensity_000)
 
    if speed > 1.25 or speed <= 1.0:
        Null()
    elif intensity >= 2.0:
        At(At("Jean_masturbation", speed_125), intensity_200)
    elif intensity >= 1.75:
        At(At("Jean_masturbation", speed_125), intensity_175)
    elif intensity >= 1.5:
        At(At("Jean_masturbation", speed_125), intensity_150)
    elif intensity >= 1.25:
        At(At("Jean_masturbation", speed_125), intensity_125)
    elif intensity >= 1.0:
        At(At("Jean_masturbation", speed_125), intensity_100)
    elif intensity >= 0.75:
        At(At("Jean_masturbation", speed_125), intensity_075)
    elif intensity >= 0.5:
        At(At("Jean_masturbation", speed_125), intensity_050)
    elif intensity >= 0.25:
        At(At("Jean_masturbation", speed_125), intensity_025)
    else:
        At(At("Jean_masturbation", speed_125), intensity_000)
 
    if speed > 1.0 or speed <= 0.75:
        Null()
    elif intensity >= 2.0:
        At(At("Jean_masturbation", speed_100), intensity_200)
    elif intensity >= 1.75:
        At(At("Jean_masturbation", speed_100), intensity_175)
    elif intensity >= 1.5:
        At(At("Jean_masturbation", speed_100), intensity_150)
    elif intensity >= 1.25:
        At(At("Jean_masturbation", speed_100), intensity_125)
    elif intensity >= 1.0:
        At(At("Jean_masturbation", speed_100), intensity_100)
    elif intensity >= 0.75:
        At(At("Jean_masturbation", speed_100), intensity_075)
    elif intensity >= 0.5:
        At(At("Jean_masturbation", speed_100), intensity_050)
    elif intensity >= 0.25:
        At(At("Jean_masturbation", speed_100), intensity_025)
    else:
        At(At("Jean_masturbation", speed_100), intensity_000)

    if speed > 0.75 or speed <= 0.5:
        Null()
    elif intensity >= 2.0:
        At(At("Jean_masturbation", speed_075), intensity_200)
    elif intensity >= 1.75:
        At(At("Jean_masturbation", speed_075), intensity_175)
    elif intensity >= 1.5:
        At(At("Jean_masturbation", speed_075), intensity_150)
    elif intensity >= 1.25:
        At(At("Jean_masturbation", speed_075), intensity_125)
    elif intensity >= 1.0:
        At(At("Jean_masturbation", speed_075), intensity_100)
    elif intensity >= 0.75:
        At(At("Jean_masturbation", speed_075), intensity_075)
    elif intensity >= 0.5:
        At(At("Jean_masturbation", speed_075), intensity_050)
    elif intensity >= 0.25:
        At(At("Jean_masturbation", speed_075), intensity_025)
    else:
        At(At("Jean_masturbation", speed_075), intensity_000)

    if speed > 0.5 or speed <= 0.25:
        Null()
    elif intensity >= 2.0:
        At(At("Jean_masturbation", speed_050), intensity_200)
    elif intensity >= 1.75:
        At(At("Jean_masturbation", speed_050), intensity_175)
    elif intensity >= 1.5:
        At(At("Jean_masturbation", speed_050), intensity_150)
    elif intensity >= 1.25:
        At(At("Jean_masturbation", speed_050), intensity_125)
    elif intensity >= 1.0:
        At(At("Jean_masturbation", speed_050), intensity_100)
    elif intensity >= 0.75:
        At(At("Jean_masturbation", speed_050), intensity_075)
    elif intensity >= 0.5:
        At(At("Jean_masturbation", speed_050), intensity_050)
    elif intensity >= 0.25:
        At(At("Jean_masturbation", speed_050), intensity_025)
    else:
        At(At("Jean_masturbation", speed_050), intensity_000)

    if speed > 0.25 or speed <= 0.01:
        Null()
    elif intensity >= 2.0:
        At(At("Jean_masturbation", speed_025), intensity_200)
    elif intensity >= 1.75:
        At(At("Jean_masturbation", speed_025), intensity_175)
    elif intensity >= 1.5:
        At(At("Jean_masturbation", speed_025), intensity_150)
    elif intensity >= 1.25:
        At(At("Jean_masturbation", speed_025), intensity_125)
    elif intensity >= 1.0:
        At(At("Jean_masturbation", speed_025), intensity_100)
    elif intensity >= 0.75:
        At(At("Jean_masturbation", speed_025), intensity_075)
    elif intensity >= 0.5:
        At(At("Jean_masturbation", speed_025), intensity_050)
    elif intensity >= 0.25:
        At(At("Jean_masturbation", speed_025), intensity_025)
    else:
        At(At("Jean_masturbation", speed_025), intensity_000)

    if speed != 0.01:
        Null()
    elif intensity >= 2.0:
        At(At("Jean_masturbation", speed_0001), intensity_200)
    elif intensity >= 1.75:
        At(At("Jean_masturbation", speed_0001), intensity_175)
    elif intensity >= 1.5:
        At(At("Jean_masturbation", speed_0001), intensity_150)
    elif intensity >= 1.25:
        At(At("Jean_masturbation", speed_0001), intensity_125)
    elif intensity >= 1.0:
        At(At("Jean_masturbation", speed_0001), intensity_100)
    elif intensity >= 0.75:
        At(At("Jean_masturbation", speed_0001), intensity_075)
    elif intensity >= 0.5:
        At(At("Jean_masturbation", speed_0001), intensity_050)
    elif intensity >= 0.25:
        At(At("Jean_masturbation", speed_0001), intensity_025)
    else:
        At(At("Jean_masturbation", speed_0001), intensity_000)

    if speed >= 0.01 or speed < 0.0:
        Null()
    elif intensity >= 2.0:
        At(At("Jean_masturbation", speed_000), intensity_200)
    elif intensity >= 1.75:
        At(At("Jean_masturbation", speed_000), intensity_175)
    elif intensity >= 1.5:
        At(At("Jean_masturbation", speed_000), intensity_150)
    elif intensity >= 1.25:
        At(At("Jean_masturbation", speed_000), intensity_125)
    elif intensity >= 1.0:
        At(At("Jean_masturbation", speed_000), intensity_100)
    elif intensity >= 0.75:
        At(At("Jean_masturbation", speed_000), intensity_075)
    elif intensity >= 0.5:
        At(At("Jean_masturbation", speed_000), intensity_050)
    elif intensity >= 0.25:
        At(At("Jean_masturbation", speed_000), intensity_025)
    else:
        At(At("Jean_masturbation", speed_000), intensity_000)

layeredimage Jean_masturbation:
    if Jean.vagina_Actions:
        "Jean_masturbation_thighs_animation[Jean.vagina_Actions[0].mode]"
    elif Jean.anus_Actions:
        "Jean_masturbation_thighs_animation[Jean.anus_Actions[0].mode]"
    else:
        "Jean_masturbation_thighs_animation0"
    
layeredimage Jean_masturbation_torso:
    if Jean.vagina_Actions:
        "Jean_masturbation_hair_back_animation[Jean.vagina_Actions[0].mode]"
    elif Jean.anus_Actions:
        "Jean_masturbation_hair_back_animation[Jean.anus_Actions[0].mode]"
    else:
        "Jean_masturbation_hair_back_animation0"
            
    always:
        "characters/Jean/images/masturbation/torso.webp"

    if Jean.piercings["belly"]:
        "characters/Jean/images/masturbation/belly_piercing.webp"

    if Jean.spunk["belly"]:
        "characters/Jean/images/masturbation/spunk_belly.webp"

    if Jean.vagina_Actions:
        "Jean_masturbation_left_arm_animation[Jean.vagina_Actions[0].mode]"
    elif Jean.anus_Actions:
        "Jean_masturbation_left_arm_animation[Jean.anus_Actions[0].mode]"
    else:
        "Jean_masturbation_left_arm_animation0"

    if Jean.vagina_Actions:
        "Jean_masturbation_breasts_animation[Jean.vagina_Actions[0].mode]"
    elif Jean.anus_Actions:
        "Jean_masturbation_breasts_animation[Jean.anus_Actions[0].mode]"
    else:
        "Jean_masturbation_breasts_animation0"

    if not Player.left_hand_Actions or Jean not in Player.left_hand_Actions[0].Targets:
        Null()
    elif Player.left_hand_Actions[0].animation_type == "choke":
        At("Jean_masturbation_male_left_arm_choke_animation[Player.left_hand_Actions[0].mode]", change_offset(Jean_masturbation_neck_position[0], Jean_masturbation_neck_position[1]))

    if not Player.right_hand_Actions or Jean not in Player.right_hand_Actions[0].Targets:
        Null()
    elif Player.right_hand_Actions[0].animation_type == "choke":
        At("Jean_masturbation_male_right_arm_choke_animation[Player.right_hand_Actions[0].mode]", change_offset(Jean_masturbation_neck_position[0], Jean_masturbation_neck_position[1]))

    if Jean.vagina_Actions:
        "Jean_masturbation_head_animation[Jean.vagina_Actions[0].mode]"
    elif Jean.anus_Actions:
        "Jean_masturbation_head_animation[Jean.anus_Actions[0].mode]"
    else:
        "Jean_masturbation_head_animation0"

    if Jean.right_hand_Actions and Jean.right_hand_Actions[0].animation_type == "self_touch_pussy":
        "Jean_masturbation_right_forearm_animation[Jean.right_hand_Actions[0].mode]"

    anchor (int(2576*sex_sampling), int(2541*sex_sampling))
    offset (int(2576*sex_sampling), int(2541*sex_sampling))
    
image Jean_masturbation_hair_back:
    "characters/Jean/images/masturbation/hair_back.webp"

    anchor (int(2787*sex_sampling), int(1333*sex_sampling))
    offset (int(2787*sex_sampling), int(1333*sex_sampling))
    
image Jean_masturbation_left_arm:
    "characters/Jean/images/masturbation/left_arm.webp"

    anchor (int(3344*sex_sampling), int(1534*sex_sampling))
    offset (int(3344*sex_sampling), int(1534*sex_sampling))
    
layeredimage Jean_masturbation_breasts:
    always:
        "characters/Jean/images/masturbation/breasts.webp"

    if Jean.tan_lines["top"]:
        "characters/Jean/images/masturbation/tan_lines_[Jean.tan_lines[top]].webp"

    if Jean.tan_lines["full"]:
        "characters/Jean/images/masturbation/tan_lines_[Jean.tan_lines[full]]_torso.webp"

    if Jean.piercings["nipple"] in ["barbell", "both"]:
        "characters/Jean/images/masturbation/nipple_piercings_barbell.webp"

    if Jean.piercings["nipple"] in ["ring", "both"]:
        "characters/Jean/images/masturbation/nipple_piercings_ring.webp"

    if Jean.spunk["breasts"]:
        "characters/Jean/images/masturbation/spunk_breasts.webp"

    anchor (int(2576*sex_sampling), int(2541*sex_sampling))
    offset (int(2576*sex_sampling), int(2541*sex_sampling))
    
layeredimage Jean_masturbation_head:
    always:
        "characters/Jean/images/masturbation/head_[Jean.mouth].webp"

    if Jean.eyes in ["closed", "down", "left", "right", "squint", "up"]:
        "characters/Jean/images/masturbation/eyes_[Jean.eyes].webp"
    else:
        "Jean_masturbation_blinking"

    always:
        "characters/Jean/images/masturbation/brows_[Jean.brows].webp"

    if Jean.blush:
            "characters/Jean/images/masturbation/blush[Jean.blush].webp"
        
    if Jean.spunk["tongue"] and Jean.mouth in ["agape", "tongue"]:
        "characters/Jean/images/masturbation/spunk_tongue.webp"

    if Jean.spunk["mouth"] and Jean.mouth in ["agape", "tongue"]:
        "characters/Jean/images/masturbation/spunk_mouth.webp"
        
    if Jean.spunk["chin"]:
        "characters/Jean/images/masturbation/spunk_chin.webp"
        
    if Jean.spunk["face"]:
        "characters/Jean/images/masturbation/spunk_face.webp"

    if Jean.vagina_Actions:
        "Jean_masturbation_hair_animation[Jean.vagina_Actions[0].mode]"
    elif Jean.anus_Actions:
        "Jean_masturbation_hair_animation[Jean.anus_Actions[0].mode]"
    else:
        "Jean_masturbation_hair_animation0"

    if Jean.psychic:
        "characters/Jean/images/masturbation/psychic.webp"

    anchor (int(2787*sex_sampling), int(1333*sex_sampling))
    offset (int(2787*sex_sampling), int(1333*sex_sampling))
    
layeredimage Jean_masturbation_hair:
    # if Jean.wet or Jean.Clothes["hair"].string == "wet":
    #     "characters/Jean/images/masturbation/hair_shadow_wet.webp"
    # else:
    always:
        "characters/Jean/images/masturbation/hair_shadow_[Jean.Clothes[hair].string].webp"

    # if Jean.wet or Jean.Clothes["hair"].string == "wet":
    #     "characters/Jean/images/masturbation/hair_wet.webp"
    # else:
    always:
        "characters/Jean/images/masturbation/hair_[Jean.Clothes[hair].string].webp"

    if Jean.spunk["hair"]:
        "characters/Jean/images/masturbation/spunk_hair.webp"

    anchor (int(2787*sex_sampling), int(1333*sex_sampling))
    offset (int(2787*sex_sampling), int(1333*sex_sampling))

image Jean_masturbation_right_forearm:
    "characters/Jean/images/masturbation/right_forearm.webp"

    anchor (int(2091*sex_sampling), int(2343*sex_sampling))
    offset (int(2091*sex_sampling), int(2343*sex_sampling))
    
layeredimage Jean_masturbation_thighs:
    if Jean.vagina_Actions:
        "Jean_masturbation_torso_animation[Jean.vagina_Actions[0].mode]"
    elif Jean.anus_Actions:
        "Jean_masturbation_torso_animation[Jean.anus_Actions[0].mode]"
    else:
        "Jean_masturbation_torso_animation0"

    always:
        "characters/Jean/images/masturbation/thighs.webp"

    if not Jean.anus_Actions:
        "Jean_masturbation_anus_closed"
    elif Jean.anus_Actions[0].animation_type == "eat_ass":
        "Jean_masturbation_anus_open"
    elif Jean.anus_Actions[0].animation_type == "finger_ass" and Player.right_hand_Actions and Player.right_hand_Actions[0].animation_type == "finger_ass":
        "Jean_masturbation_anus_right_arm_finger_ass_animation[Jean.anus_Actions[0].mode]"
    elif Jean.anus_Actions[0].animation_type == "finger_ass" and Player.left_hand_Actions and Player.left_hand_Actions[0].animation_type == "finger_ass":
        "Jean_masturbation_anus_left_arm_finger_ass_animation[Jean.anus_Actions[0].mode]"
    elif Jean.anus_Actions[0].animation_type in ["dildo_ass", "self_dildo_ass"]:
        "Jean_masturbation_anus_dildo_ass_animation[Jean.anus_Actions[0].mode]"

    if not Jean.vagina_Actions:
        "Jean_masturbation_pussy_closed"
    elif Jean.vagina_Actions[0].animation_type == "finger_pussy" and Player.right_hand_Actions and Player.right_hand_Actions[0].animation_type == "finger_pussy":
        "Jean_masturbation_pussy_right_arm_finger_pussy_animation[Jean.vagina_Actions[0].mode]"
    elif Jean.vagina_Actions[0].animation_type == "finger_pussy" and Player.left_hand_Actions and Player.left_hand_Actions[0].animation_type == "finger_pussy":
        "Jean_masturbation_pussy_left_arm_finger_pussy_animation[Jean.vagina_Actions[0].mode]"
    elif Jean.vagina_Actions[0].animation_type in ["dildo_pussy", "self_dildo_pussy"]:
        "Jean_masturbation_pussy_dildo_pussy_animation[Jean.vagina_Actions[0].mode]"

    if Jean.tan_lines["bottom"]:
        "characters/Jean/images/masturbation/tan_lines_[Jean.tan_lines[bottom]].webp"

    if Jean.tan_lines["full"]:
        "characters/Jean/images/masturbation/tan_lines_[Jean.tan_lines[full]]_thighs.webp"

    if Jean.creampie["anus"]:
        "characters/Jean/images/masturbation/creampie_anus.webp"

    if Jean.creampie["pussy"]:
        "characters/Jean/images/masturbation/creampie_pussy.webp"

    if not Jean.buttplug:
        Null()
    elif Jean.buttplug.string == "heart_anal_plug":
        "characters/Jean/images/masturbation/buttplug_heart.webp"
    elif Jean.buttplug.string == "round_anal_plug":
        "characters/Jean/images/masturbation/buttplug_round.webp"

    if Jean.piercings["labia"] in ["barbell", "both"]:
        "characters/Jean/images/masturbation/labia_piercings_barbell.webp"

    if Jean.piercings["labia"] in ["ring", "both"]:
        "characters/Jean/images/masturbation/labia_piercings_ring.webp"

    if Jean.body_hair_growing["pubic"]:
        "characters/Jean/images/masturbation/pubes_growing.webp"

    if Jean.body_hair["pubic"]:
        "characters/Jean/images/masturbation/pubes_[Jean.body_hair[pubic]].webp"

    if Jean.remote_vibrator:
        "characters/Jean/images/masturbation/remote_vibrator.webp"

    if Jean.right_hand_Actions and Jean.right_hand_Actions[0].animation_type == "self_touch_pussy":
        "Jean_masturbation_right_hand_animation[Jean.right_hand_Actions[0].mode]"

    if Jean.vagina_Actions:
        "Jean_masturbation_left_leg_animation[Jean.vagina_Actions[0].mode]"
    elif Jean.anus_Actions:
        "Jean_masturbation_left_leg_animation[Jean.anus_Actions[0].mode]"
    else:
        "Jean_masturbation_left_leg_animation0"

    if Jean.vagina_Actions:
        "Jean_masturbation_right_leg_animation[Jean.vagina_Actions[0].mode]"
    elif Jean.anus_Actions:
        "Jean_masturbation_right_leg_animation[Jean.anus_Actions[0].mode]"
    else:
        "Jean_masturbation_right_leg_animation0"

    if not Jean.anus_Actions or Jean.anus_Actions[0].animation_type != "finger_ass":
        Null()
    elif Player.left_hand_Actions and Jean in Player.left_hand_Actions[0].Targets and Player.left_hand_Actions[0].animation_type == "finger_ass":
        AlphaMask("Jean_masturbation_male_left_arm_finger_animations", "Jean_masturbation_mask_anus_animations")
    elif Player.right_hand_Actions and Jean in Player.right_hand_Actions[0].Targets and Player.right_hand_Actions[0].animation_type == "finger_ass":
        AlphaMask("Jean_masturbation_male_right_arm_finger_animations", "Jean_masturbation_mask_anus_animations")
    
    if Jean.anus_Actions and Jean.anus_Actions[0].animation_type in ["dildo_ass", "self_dildo_ass"]:
        AlphaMask("Jean_masturbation_dildo_ass_animations", "Jean_masturbation_mask_anus_animations")

    if not Jean.vagina_Actions or Jean.vagina_Actions[0].animation_type != "finger_pussy":
        Null()
    elif Player.left_hand_Actions and Jean in Player.left_hand_Actions[0].Targets and Player.left_hand_Actions[0].animation_type == "finger_pussy":
        AlphaMask("Jean_masturbation_male_left_arm_finger_animations", "Jean_masturbation_mask_pussy_animations")
    elif Player.right_hand_Actions and Jean in Player.right_hand_Actions[0].Targets and Player.right_hand_Actions[0].animation_type == "finger_pussy":
        AlphaMask("Jean_masturbation_male_right_arm_finger_animations", "Jean_masturbation_mask_pussy_animations")
    
    if Jean.vagina_Actions and Jean.vagina_Actions[0].animation_type in ["dildo_pussy", "self_dildo_pussy"]:
        AlphaMask("Jean_masturbation_dildo_pussy_animations", "Jean_masturbation_mask_pussy_animations")

    if Jean.clitoris_Actions and Jean.clitoris_Actions[0].animation_type in ["vibrator", "self_vibrator"]:
        "Jean_masturbation_vibrator_animation[Jean.clitoris_Actions[0].mode]"

    if not Player.left_hand_Actions or Jean not in Player.left_hand_Actions[0].Targets:
        Null()
    elif Player.left_hand_Actions[0].animation_type == "touch_thighs":
        "Jean_masturbation_male_left_arm_touch_thighs_animation[Player.left_hand_Actions[0].mode]"
    elif Player.left_hand_Actions[0].animation_type == "touch_thighs_higher":
        "Jean_masturbation_male_left_arm_touch_thighs_higher_animation[Player.left_hand_Actions[0].mode]"
    elif Player.left_hand_Actions[0].animation_type == "touch_breasts" and Jean.right_breast_Actions and Player.left_hand_Actions[0].animation_type == Jean.right_breast_Actions[0].animation_type:
        At("Jean_masturbation_male_left_arm_touch_right_breast_animation[Player.left_hand_Actions[0].mode]", change_offset(Jean_masturbation_right_breast_position[0], Jean_masturbation_right_breast_position[1]))
    elif Player.left_hand_Actions[0].animation_type == "touch_breasts" and Jean.left_breast_Actions and Player.left_hand_Actions[0].animation_type == Jean.left_breast_Actions[0].animation_type:
        At("Jean_masturbation_male_left_arm_touch_left_breast_animation[Player.left_hand_Actions[0].mode]", change_offset(Jean_masturbation_left_breast_position[0], Jean_masturbation_left_breast_position[1]))
    elif Player.left_hand_Actions[0].animation_type == "pinch_nipples" and Jean.right_nipple_Actions and Player.left_hand_Actions[0].animation_type == Jean.right_nipple_Actions[0].animation_type:
        At("Jean_masturbation_male_left_arm_touch_right_breast_animation[Player.left_hand_Actions[0].mode]", change_offset(Jean_masturbation_right_nipple_position[0], Jean_masturbation_right_nipple_position[1]))
    elif Player.left_hand_Actions[0].animation_type == "pinch_nipples" and Jean.left_nipple_Actions and Player.left_hand_Actions[0].animation_type == Jean.left_nipple_Actions[0].animation_type:
        At("Jean_masturbation_male_left_arm_touch_left_breast_animation[Player.left_hand_Actions[0].mode]", change_offset(Jean_masturbation_left_nipple_position[0], Jean_masturbation_left_nipple_position[1]))

    if not Player.right_hand_Actions or Jean not in Player.right_hand_Actions[0].Targets:
        Null()
    elif Player.right_hand_Actions[0].animation_type == "touch_thighs":
        "Jean_masturbation_male_right_arm_touch_thighs_animation[Player.right_hand_Actions[0].mode]"
    elif Player.right_hand_Actions[0].animation_type == "touch_thighs_higher":
        "Jean_masturbation_male_right_arm_touch_thighs_higher_animation[Player.right_hand_Actions[0].mode]"
    elif Player.right_hand_Actions[0].animation_type == "touch_breasts" and Jean.right_breast_Actions and Player.right_hand_Actions[0].animation_type == Jean.right_breast_Actions[0].animation_type:
        At("Jean_masturbation_male_right_arm_touch_right_breast_animation[Player.right_hand_Actions[0].mode]", change_offset(Jean_masturbation_right_breast_position[0], Jean_masturbation_right_breast_position[1]))
    elif Player.right_hand_Actions[0].animation_type == "touch_breasts" and Jean.left_breast_Actions and Player.right_hand_Actions[0].animation_type == Jean.left_breast_Actions[0].animation_type:
        At("Jean_masturbation_male_right_arm_touch_left_breast_animation[Player.right_hand_Actions[0].mode]", change_offset(Jean_masturbation_left_breast_position[0], Jean_masturbation_left_breast_position[1]))
    elif Player.right_hand_Actions[0].animation_type == "pinch_nipples" and Jean.right_nipple_Actions and Player.right_hand_Actions[0].animation_type == Jean.right_nipple_Actions[0].animation_type:
        At("Jean_masturbation_male_right_arm_touch_right_breast_animation[Player.right_hand_Actions[0].mode]", change_offset(Jean_masturbation_right_nipple_position[0], Jean_masturbation_right_nipple_position[1]))
    elif Player.right_hand_Actions[0].animation_type == "pinch_nipples" and Jean.left_nipple_Actions and Player.right_hand_Actions[0].animation_type == Jean.left_nipple_Actions[0].animation_type:
        At("Jean_masturbation_male_right_arm_touch_left_breast_animation[Player.right_hand_Actions[0].mode]", change_offset(Jean_masturbation_left_nipple_position[0], Jean_masturbation_left_nipple_position[1]))
    
    if not Player.mouth_Actions or Jean not in Player.mouth_Actions[0].Targets:
        Null()
    elif Player.mouth_Actions[0].animation_type == "suck_nipples" and Jean.right_nipple_Actions and Jean.right_nipple_Actions[0].animation_type == "suck_nipples":
        At("Jean_masturbation_male_head_suck_right_nipple_animation[Player.mouth_Actions[0].mode]", change_offset(Jean_masturbation_right_nipple_position[0], Jean_masturbation_right_nipple_position[1]))
    elif Player.mouth_Actions[0].animation_type == "suck_nipples" and Jean.left_nipple_Actions and Jean.left_nipple_Actions[0].animation_type == "suck_nipples":
        At("Jean_masturbation_male_head_suck_left_nipple_animation[Player.mouth_Actions[0].mode]", change_offset(Jean_masturbation_left_nipple_position[0], Jean_masturbation_left_nipple_position[1]))
    elif Player.mouth_Actions[0].animation_type == "eat_pussy":
        At("Jean_masturbation_male_head_eat_pussy_animation[Player.mouth_Actions[0].mode]", change_offset(Jean_masturbation_pussy_position[0], Jean_masturbation_pussy_position[1]))
    elif Player.mouth_Actions[0].animation_type == "eat_ass":
        At("Jean_masturbation_male_head_eat_ass_animation[Player.mouth_Actions[0].mode]", change_offset(Jean_masturbation_anus_position[0], Jean_masturbation_anus_position[1]))

    anchor (int(2576*sex_sampling), int(2541*sex_sampling))
    offset (int(2576*sex_sampling), int(2541*sex_sampling))

image Jean_masturbation_anus_closed:
    "characters/Jean/images/masturbation/anus_closed.webp"

    anchor (int(2472*sex_sampling), int(2914*sex_sampling))
    offset (int(2472*sex_sampling), int(2914*sex_sampling))

image Jean_masturbation_anus_open:
    "characters/Jean/images/masturbation/anus_open.webp"

    anchor (int(2472*sex_sampling), int(2914*sex_sampling))
    offset (int(2472*sex_sampling), int(2914*sex_sampling))

layeredimage Jean_masturbation_anus_agape:
    if Jean.anus_Actions[0].mode > 0:
        "characters/Jean/images/masturbation/anus_agape.webp"
    else:
        "characters/Jean/images/masturbation/anus_closed.webp"

    anchor (int(2472*sex_sampling), int(2899*sex_sampling))
    offset (int(2472*sex_sampling), int(2899*sex_sampling))

image Jean_masturbation_pussy_closed:
    "characters/Jean/images/masturbation/pussy_closed.webp"

    anchor (int(2482*sex_sampling), int(2703*sex_sampling))
    offset (int(2482*sex_sampling), int(2703*sex_sampling))

image Jean_masturbation_pussy_open:
    "characters/Jean/images/masturbation/pussy_open.webp"

    anchor (int(2482*sex_sampling), int(2703*sex_sampling))
    offset (int(2482*sex_sampling), int(2703*sex_sampling))

layeredimage Jean_masturbation_pussy_agape:
    if Jean.vagina_Actions[0].mode > 0:
        "characters/Jean/images/masturbation/pussy_agape.webp"
    else:
        "characters/Jean/images/masturbation/pussy_closed.webp"

    anchor (int(2474*sex_sampling), int(2675*sex_sampling))
    offset (int(2474*sex_sampling), int(2675*sex_sampling))

layeredimage Jean_masturbation_right_hand:
    always:
        "characters/Jean/images/masturbation/right_hand_shadow.webp"

    always:
        "characters/Jean/images/masturbation/right_hand.webp"

    anchor (int(2357*sex_sampling), int(2109*sex_sampling))
    offset (int(2357*sex_sampling), int(2109*sex_sampling))

layeredimage Jean_masturbation_left_leg:
    always:
        "characters/Jean/images/masturbation/left_leg.webp"

    if Jean.vagina_Actions:
        "Jean_masturbation_left_foot_animation[Jean.vagina_Actions[0].mode]"
    elif Jean.anus_Actions:
        "Jean_masturbation_left_foot_animation[Jean.anus_Actions[0].mode]"
    else:
        "Jean_masturbation_left_foot_animation0"

    anchor (int(4161*sex_sampling), int(1625*sex_sampling))
    offset (int(4161*sex_sampling), int(1625*sex_sampling))

layeredimage Jean_masturbation_left_foot:
    always:
        "characters/Jean/images/masturbation/left_foot.webp"

    anchor (int(4232*sex_sampling), int(3466*sex_sampling))
    offset (int(4232*sex_sampling), int(3466*sex_sampling))

layeredimage Jean_masturbation_right_leg:
    always:
        "characters/Jean/images/masturbation/right_leg.webp"

    if Jean.vagina_Actions:
        "Jean_masturbation_right_foot_animation[Jean.vagina_Actions[0].mode]"
    elif Jean.anus_Actions:
        "Jean_masturbation_right_foot_animation[Jean.anus_Actions[0].mode]"
    else:
        "Jean_masturbation_right_foot_animation0"

    anchor (int(1031*sex_sampling), int(1428*sex_sampling))
    offset (int(1031*sex_sampling), int(1428*sex_sampling))

layeredimage Jean_masturbation_right_foot:
    always:
        "characters/Jean/images/masturbation/right_foot.webp"

    anchor (int(645*sex_sampling), int(3228*sex_sampling))
    offset (int(645*sex_sampling), int(3228*sex_sampling))

image Jean_masturbation_male_left_arm_finger:
    "characters/Jean/images/masturbation/male_left_arm_[Player.skin_color]_finger.webp"

    anchor (int(2538*sex_sampling), int(2622*sex_sampling))
    offset (int(2538*sex_sampling), int(2622*sex_sampling))

image Jean_masturbation_male_right_arm_finger:
    "characters/Jean/images/masturbation/male_right_arm_[Player.skin_color]_finger.webp"

    anchor (int(2421*sex_sampling), int(2594*sex_sampling))
    offset (int(2421*sex_sampling), int(2594*sex_sampling))

layeredimage Jean_masturbation_male_left_arm:
    if Player.left_hand_Actions[0].animation_type in ["touch_thighs", "touch_thighs_higher"]:
        "characters/Jean/images/masturbation/male_hand_shadow_right.webp"

    always:
        "characters/Jean/images/masturbation/male_left_arm_[Player.skin_color].webp"

    anchor (int(1466*sex_sampling), int(2176*sex_sampling))
    offset (int(1466*sex_sampling), int(2176*sex_sampling))

layeredimage Jean_masturbation_male_right_arm:
    if Player.right_hand_Actions[0].animation_type in ["touch_thighs", "touch_thighs_higher"]:
        "characters/Jean/images/masturbation/male_hand_shadow_left.webp"

    always:
        "characters/Jean/images/masturbation/male_right_arm_[Player.skin_color].webp"

    anchor (int(3664*sex_sampling), int(2460*sex_sampling))
    offset (int(3664*sex_sampling), int(2460*sex_sampling))

image Jean_masturbation_dildo:
    "characters/Jean/images/masturbation/dildo.webp"

    anchor (int(2478*sex_sampling), int(2630*sex_sampling))
    offset (int(2478*sex_sampling), int(2630*sex_sampling))

image Jean_masturbation_vibrator:
    "characters/Jean/images/masturbation/vibrator.webp"

    anchor (int(2481*sex_sampling), int(2445*sex_sampling))
    offset (int(2481*sex_sampling), int(2445*sex_sampling))

layeredimage Jean_masturbation_mask_anus:
    if Jean.anus_Actions[0].animation_type == "finger_ass" and Player.right_hand_Actions and Player.right_hand_Actions[0].animation_type == "finger_ass":
        "characters/Jean/images/masturbation/mask_anus_right_finger.webp"
    elif Jean.anus_Actions[0].animation_type == "finger_ass" and Player.left_hand_Actions and Player.left_hand_Actions[0].animation_type == "finger_ass":
        "characters/Jean/images/masturbation/mask_anus_left_finger.webp"
    elif Jean.anus_Actions[0].animation_type in ["dildo_ass", "self_dildo_ass"]:
        "characters/Jean/images/masturbation/mask_anus_dildo.webp"

    anchor (int(2472*sex_sampling), int(2899*sex_sampling))
    offset (int(2472*sex_sampling), int(2899*sex_sampling))

layeredimage Jean_masturbation_mask_pussy:
    if Jean.vagina_Actions[0].animation_type == "finger_pussy" and Player.right_hand_Actions and Player.right_hand_Actions[0].animation_type == "finger_pussy":
        "characters/Jean/images/masturbation/mask_pussy_right_finger.webp"
    elif Jean.vagina_Actions[0].animation_type == "finger_pussy" and Player.left_hand_Actions and Player.left_hand_Actions[0].animation_type == "finger_pussy":
        "characters/Jean/images/masturbation/mask_pussy_left_finger.webp"
    elif Jean.vagina_Actions[0].animation_type in ["dildo_pussy", "self_dildo_pussy"]:
        "characters/Jean/images/masturbation/mask_pussy_dildo.webp"

    anchor (int(2474*sex_sampling), int(2675*sex_sampling))
    offset (int(2474*sex_sampling), int(2675*sex_sampling))

layeredimage Jean_masturbation_male_left_arm_fondle:
    if Player.left_hand_Actions[0].animation_type in ["touch_breasts", "touch_pussy", "grab_ass"]:
        "Player_left_arm_fondle"
    elif Player.left_hand_Actions[0].animation_type in ["choke", "pinch_nipples"]:
        "Player_left_arm_pinch"

layeredimage Jean_masturbation_male_right_arm_fondle:
    if Player.right_hand_Actions[0].animation_type in ["touch_breasts", "touch_pussy", "grab_ass"]:
        "Player_right_arm_fondle"
    elif Player.right_hand_Actions[0].animation_type in ["choke", "pinch_nipples"]:
        "Player_right_arm_pinch"

layeredimage Jean_masturbation_male_head:
    if Player.body_visible:
        "Player_head"

    if Player.mouth_Actions and Jean in Player.mouth_Actions[0].Targets and Player.mouth_Actions[0].animation_type in ["suck_nipples", "eat_pussy", "eat_ass"]:
        "Jean_masturbation_male_tongue_animation[Player.mouth_Actions[0].mode]"

image Jean_masturbation_male_tongue:
    "Player_tongue"
    
image Jean_masturbation_hair_back_animation0:
    "Jean_masturbation_hair_back"

    masturbation_hair_back_animation0
    
image Jean_masturbation_hair_back_animation1:
    "Jean_masturbation_hair_back"

    masturbation_hair_back_animation1
    
image Jean_masturbation_torso_animation0:
    "Jean_masturbation_torso"

    masturbation_torso_animation0
    
image Jean_masturbation_torso_animation1:
    "Jean_masturbation_torso"

    masturbation_torso_animation1
    
image Jean_masturbation_left_arm_animation0:
    "Jean_masturbation_left_arm"

    masturbation_left_arm_animation0
    
image Jean_masturbation_left_arm_animation1:
    "Jean_masturbation_left_arm"

    masturbation_left_arm_animation1
    
image Jean_masturbation_breasts_animation0:
    "Jean_masturbation_breasts"

    masturbation_breasts_animation0
    
image Jean_masturbation_breasts_animation1:
    "Jean_masturbation_breasts"

    masturbation_breasts_animation1
    
image Jean_masturbation_head_animation0:
    "Jean_masturbation_head"

    masturbation_head_animation0
    
image Jean_masturbation_head_animation1:
    "Jean_masturbation_head"

    masturbation_head_animation1
    
image Jean_masturbation_hair_animation0:
    "Jean_masturbation_hair"

    masturbation_hair_animation0
    
image Jean_masturbation_hair_animation1:
    "Jean_masturbation_hair"

    masturbation_hair_animation1
    
image Jean_masturbation_right_forearm_animation0:
    "Jean_masturbation_right_forearm"

    masturbation_right_forearm_animation0
    
image Jean_masturbation_right_forearm_animation1:
    "Jean_masturbation_right_forearm"

    masturbation_right_forearm_animation1
    
image Jean_masturbation_thighs_animation0:
    "Jean_masturbation_thighs"

    masturbation_thighs_animation0
    
image Jean_masturbation_thighs_animation1:
    "Jean_masturbation_thighs"

    masturbation_thighs_animation1
    
image Jean_masturbation_pussy_left_arm_finger_pussy_animation0:
    "Jean_masturbation_pussy_closed"

    masturbation_pussy_left_arm_finger_pussy_animation0
    
image Jean_masturbation_pussy_left_arm_finger_pussy_animation1:
    "Jean_masturbation_pussy_agape"

    masturbation_pussy_left_arm_finger_pussy_animation1
    
image Jean_masturbation_anus_left_arm_finger_ass_animation0:
    "Jean_masturbation_anus_closed"

    masturbation_anus_left_arm_finger_ass_animation0
    
image Jean_masturbation_anus_left_arm_finger_ass_animation1:
    "Jean_masturbation_anus_agape"

    masturbation_anus_left_arm_finger_ass_animation1
    
image Jean_masturbation_pussy_right_arm_finger_pussy_animation0:
    "Jean_masturbation_pussy_closed"

    masturbation_pussy_right_arm_finger_pussy_animation0
    
image Jean_masturbation_pussy_right_arm_finger_pussy_animation1:
    "Jean_masturbation_pussy_agape"

    masturbation_pussy_right_arm_finger_pussy_animation1
    
image Jean_masturbation_anus_right_arm_finger_ass_animation0:
    "Jean_masturbation_anus_closed"

    masturbation_anus_right_arm_finger_ass_animation0
    
image Jean_masturbation_anus_right_arm_finger_ass_animation1:
    "Jean_masturbation_anus_agape"

    masturbation_anus_right_arm_finger_ass_animation1
    
image Jean_masturbation_pussy_dildo_pussy_animation0:
    "Jean_masturbation_pussy_closed"

    masturbation_pussy_dildo_pussy_animation0
    
image Jean_masturbation_pussy_dildo_pussy_animation1:
    "Jean_masturbation_pussy_agape"

    masturbation_pussy_dildo_pussy_animation1
    
image Jean_masturbation_anus_dildo_ass_animation0:
    "Jean_masturbation_anus_closed"

    masturbation_anus_dildo_ass_animation0
    
image Jean_masturbation_anus_dildo_ass_animation1:
    "Jean_masturbation_anus_agape"

    masturbation_anus_dildo_ass_animation1
    
image Jean_masturbation_right_hand_animation0:
    "Jean_masturbation_right_hand"

    masturbation_right_hand_animation0
    
image Jean_masturbation_right_hand_animation1:
    "Jean_masturbation_right_hand"

    masturbation_right_hand_animation1
    
image Jean_masturbation_left_leg_animation0:
    "Jean_masturbation_left_leg"

    masturbation_left_leg_animation0
    
image Jean_masturbation_left_leg_animation1:
    "Jean_masturbation_left_leg"

    masturbation_left_leg_animation1

image Jean_masturbation_left_foot_animation0:
    "Jean_masturbation_left_foot"

    masturbation_left_foot_animation0
    
image Jean_masturbation_left_foot_animation1:
    "Jean_masturbation_left_foot"

    masturbation_left_foot_animation1
    
image Jean_masturbation_right_leg_animation0:
    "Jean_masturbation_right_leg"

    masturbation_right_leg_animation0
    
image Jean_masturbation_right_leg_animation1:
    "Jean_masturbation_right_leg"

    masturbation_right_leg_animation1
    
image Jean_masturbation_right_foot_animation0:
    "Jean_masturbation_right_foot"

    masturbation_right_foot_animation0
    
image Jean_masturbation_right_foot_animation1:
    "Jean_masturbation_right_foot"

    masturbation_right_foot_animation1
    
image Jean_masturbation_male_left_arm_choke_animation0:
    "Jean_masturbation_male_left_arm_fondle"

    masturbation_male_left_arm_choke_animation0
    
image Jean_masturbation_male_left_arm_choke_animation1:
    "Jean_masturbation_male_left_arm_fondle"

    masturbation_male_left_arm_choke_animation1
    
image Jean_masturbation_male_left_arm_touch_thighs_animation0:
    "Jean_masturbation_male_left_arm"

    masturbation_male_left_arm_touch_thighs_animation0
    
image Jean_masturbation_male_left_arm_touch_thighs_animation1:
    "Jean_masturbation_male_left_arm"

    masturbation_male_left_arm_touch_thighs_animation1
    
image Jean_masturbation_male_left_arm_touch_thighs_higher_animation0:
    "Jean_masturbation_male_left_arm"

    masturbation_male_left_arm_touch_thighs_higher_animation0
    
image Jean_masturbation_male_left_arm_touch_thighs_higher_animation1:
    "Jean_masturbation_male_left_arm"

    masturbation_male_left_arm_touch_thighs_higher_animation1
    
image Jean_masturbation_male_left_arm_touch_right_breast_animation0:
    "Jean_masturbation_male_left_arm_fondle"

    masturbation_male_left_arm_touch_right_breast_animation0
    
image Jean_masturbation_male_left_arm_touch_right_breast_animation1:
    "Jean_masturbation_male_left_arm_fondle"

    masturbation_male_left_arm_touch_right_breast_animation1
    
image Jean_masturbation_male_left_arm_touch_left_breast_animation0:
    "Jean_masturbation_male_left_arm_fondle"

    masturbation_male_left_arm_touch_left_breast_animation0
    
image Jean_masturbation_male_left_arm_touch_left_breast_animation1:
    "Jean_masturbation_male_left_arm_fondle"

    masturbation_male_left_arm_touch_left_breast_animation1

image Jean_masturbation_male_left_arm_finger_pussy_animation0:
    "Jean_masturbation_male_left_arm_finger"

    masturbation_male_left_arm_finger_pussy_animation0

image Jean_masturbation_male_left_arm_finger_pussy_animation1:
    "Jean_masturbation_male_left_arm_finger"

    masturbation_male_left_arm_finger_pussy_animation1
    
image Jean_masturbation_male_left_arm_finger_ass_animation0:
    "Jean_masturbation_male_left_arm_finger"

    masturbation_male_left_arm_finger_ass_animation0
    
image Jean_masturbation_male_left_arm_finger_ass_animation1:
    "Jean_masturbation_male_left_arm_finger"

    masturbation_male_left_arm_finger_ass_animation1
    
image Jean_masturbation_male_right_arm_choke_animation0:
    "Jean_masturbation_male_right_arm_fondle"

    masturbation_male_right_arm_choke_animation0
    
image Jean_masturbation_male_right_arm_choke_animation1:
    "Jean_masturbation_male_right_arm_fondle"

    masturbation_male_right_arm_choke_animation1
    
image Jean_masturbation_male_right_arm_touch_thighs_animation0:
    "Jean_masturbation_male_right_arm"

    masturbation_male_right_arm_touch_thighs_animation0
    
image Jean_masturbation_male_right_arm_touch_thighs_animation1:
    "Jean_masturbation_male_right_arm"

    masturbation_male_right_arm_touch_thighs_animation1
    
image Jean_masturbation_male_right_arm_touch_thighs_higher_animation0:
    "Jean_masturbation_male_right_arm"

    masturbation_male_right_arm_touch_thighs_higher_animation0
    
image Jean_masturbation_male_right_arm_touch_thighs_higher_animation1:
    "Jean_masturbation_male_right_arm"

    masturbation_male_right_arm_touch_thighs_higher_animation1
    
image Jean_masturbation_male_right_arm_touch_right_breast_animation0:
    "Jean_masturbation_male_right_arm_fondle"

    masturbation_male_right_arm_touch_right_breast_animation0
    
image Jean_masturbation_male_right_arm_touch_right_breast_animation1:
    "Jean_masturbation_male_right_arm_fondle"

    masturbation_male_right_arm_touch_right_breast_animation1
    
image Jean_masturbation_male_right_arm_touch_left_breast_animation0:
    "Jean_masturbation_male_right_arm_fondle"

    masturbation_male_right_arm_touch_left_breast_animation0
    
image Jean_masturbation_male_right_arm_touch_left_breast_animation1:
    "Jean_masturbation_male_right_arm_fondle"

    masturbation_male_right_arm_touch_left_breast_animation1

image Jean_masturbation_male_right_arm_finger_pussy_animation0:
    "Jean_masturbation_male_right_arm_finger"

    masturbation_male_right_arm_finger_pussy_animation0

image Jean_masturbation_male_right_arm_finger_pussy_animation1:
    "Jean_masturbation_male_right_arm_finger"

    masturbation_male_right_arm_finger_pussy_animation1
    
image Jean_masturbation_male_right_arm_finger_ass_animation0:
    "Jean_masturbation_male_right_arm_finger"

    masturbation_male_right_arm_finger_ass_animation0
    
image Jean_masturbation_male_right_arm_finger_ass_animation1:
    "Jean_masturbation_male_right_arm_finger"

    masturbation_male_right_arm_finger_ass_animation1
    
image Jean_masturbation_dildo_pussy_animation0:
    "Jean_masturbation_dildo"

    masturbation_dildo_pussy_animation0

image Jean_masturbation_dildo_pussy_animation1:
    "Jean_masturbation_dildo"

    masturbation_dildo_pussy_animation1
    
image Jean_masturbation_dildo_ass_animation0:
    "Jean_masturbation_dildo"

    masturbation_dildo_ass_animation0
    
image Jean_masturbation_dildo_ass_animation1:
    "Jean_masturbation_dildo"

    masturbation_dildo_ass_animation1
    
image Jean_masturbation_vibrator_animation0:
    "Jean_masturbation_vibrator"

    masturbation_vibrator_animation0
    
image Jean_masturbation_vibrator_animation1:
    "Jean_masturbation_vibrator"

    masturbation_vibrator_animation1
    
image Jean_masturbation_mask_left_arm_finger_pussy_animation0:
    "Jean_masturbation_mask_pussy"

    masturbation_mask_left_arm_finger_pussy_animation0
    
image Jean_masturbation_mask_left_arm_finger_pussy_animation1:
    "Jean_masturbation_mask_pussy"

    masturbation_mask_left_arm_finger_pussy_animation1
    
image Jean_masturbation_mask_left_arm_finger_ass_animation0:
    "Jean_masturbation_mask_anus"

    masturbation_mask_left_arm_finger_ass_animation0
    
image Jean_masturbation_mask_left_arm_finger_ass_animation1:
    "Jean_masturbation_mask_anus"

    masturbation_mask_left_arm_finger_ass_animation1
    
image Jean_masturbation_mask_right_arm_finger_pussy_animation0:
    "Jean_masturbation_mask_pussy"

    masturbation_mask_right_arm_finger_pussy_animation0
    
image Jean_masturbation_mask_right_arm_finger_pussy_animation1:
    "Jean_masturbation_mask_pussy"

    masturbation_mask_right_arm_finger_pussy_animation1
    
image Jean_masturbation_mask_right_arm_finger_ass_animation0:
    "Jean_masturbation_mask_anus"

    masturbation_mask_right_arm_finger_ass_animation0
    
image Jean_masturbation_mask_right_arm_finger_ass_animation1:
    "Jean_masturbation_mask_anus"

    masturbation_mask_right_arm_finger_ass_animation1
    
image Jean_masturbation_mask_dildo_pussy_animation0:
    "Jean_masturbation_mask_pussy"

    masturbation_mask_dildo_pussy_animation0
    
image Jean_masturbation_mask_dildo_pussy_animation1:
    "Jean_masturbation_mask_pussy"

    masturbation_mask_dildo_pussy_animation1
    
image Jean_masturbation_mask_dildo_ass_animation0:
    "Jean_masturbation_mask_anus"

    masturbation_mask_dildo_ass_animation0
    
image Jean_masturbation_mask_dildo_ass_animation1:
    "Jean_masturbation_mask_anus"

    masturbation_mask_dildo_ass_animation1
    
image Jean_masturbation_male_head_suck_left_nipple_animation0:
    "Jean_masturbation_male_head"

    masturbation_male_head_suck_left_nipple_animation0
    
image Jean_masturbation_male_head_suck_left_nipple_animation1:
    "Jean_masturbation_male_head"

    masturbation_male_head_suck_left_nipple_animation1
    
image Jean_masturbation_male_head_suck_right_nipple_animation0:
    "Jean_masturbation_male_head"

    masturbation_male_head_suck_right_nipple_animation0
    
image Jean_masturbation_male_head_suck_right_nipple_animation1:
    "Jean_masturbation_male_head"

    masturbation_male_head_suck_right_nipple_animation1
    
image Jean_masturbation_male_head_eat_pussy_animation0:
    "Jean_masturbation_male_head"

    masturbation_male_head_eat_pussy_animation0
    
image Jean_masturbation_male_head_eat_pussy_animation1:
    "Jean_masturbation_male_head"

    masturbation_male_head_eat_pussy_animation1
    
image Jean_masturbation_male_head_eat_ass_animation0:
    "Jean_masturbation_male_head"

    masturbation_male_head_eat_ass_animation0
    
image Jean_masturbation_male_head_eat_ass_animation1:
    "Jean_masturbation_male_head"

    masturbation_male_head_eat_ass_animation1
    
image Jean_masturbation_male_tongue_animation0:
    "Jean_masturbation_male_tongue"

    masturbation_male_tongue_animation0
    
image Jean_masturbation_male_tongue_animation1:
    "Jean_masturbation_male_tongue"

    masturbation_male_tongue_animation1

layeredimage Jean_masturbation_male_left_arm_finger_animations:
    always:
        "Jean_masturbation_male_left_arm_[Player.left_hand_Actions[0].animation_type]_animation[Player.left_hand_Actions[0].mode]"

layeredimage Jean_masturbation_male_right_arm_finger_animations:
    always:
        "Jean_masturbation_male_right_arm_[Player.right_hand_Actions[0].animation_type]_animation[Player.right_hand_Actions[0].mode]"

layeredimage Jean_masturbation_dildo_pussy_animations:
    always:
        "Jean_masturbation_dildo_pussy_animation[Jean.vagina_Actions[0].mode]"

layeredimage Jean_masturbation_dildo_ass_animations:
    always:
        "Jean_masturbation_dildo_ass_animation[Jean.anus_Actions[0].mode]"

layeredimage Jean_masturbation_mask_anus_animations:
    if Jean.anus_Actions[0].animation_type == "finger_ass" and Player.left_hand_Actions and Player.left_hand_Actions[0].animation_type == "finger_ass":
        "Jean_masturbation_mask_left_arm_finger_ass_animation[Jean.anus_Actions[0].mode]"
    elif Jean.anus_Actions[0].animation_type == "finger_ass" and Player.right_hand_Actions and Player.right_hand_Actions[0].animation_type == "finger_ass":
        "Jean_masturbation_mask_right_arm_finger_ass_animation[Jean.anus_Actions[0].mode]"
    elif Jean.anus_Actions[0].animation_type in ["dildo_ass", "self_dildo_ass"]:
        "Jean_masturbation_mask_dildo_ass_animation[Jean.anus_Actions[0].mode]"

layeredimage Jean_masturbation_mask_pussy_animations:
    if Jean.vagina_Actions[0].animation_type == "finger_pussy" and Player.left_hand_Actions and Player.left_hand_Actions[0].animation_type == "finger_pussy":
        "Jean_masturbation_mask_left_arm_finger_pussy_animation[Jean.vagina_Actions[0].mode]"
    elif Jean.vagina_Actions[0].animation_type == "finger_pussy" and Player.right_hand_Actions and Player.right_hand_Actions[0].animation_type == "finger_pussy":
        "Jean_masturbation_mask_right_arm_finger_pussy_animation[Jean.vagina_Actions[0].mode]"
    elif Jean.vagina_Actions[0].animation_type in ["dildo_pussy", "self_dildo_pussy"]:
        "Jean_masturbation_mask_dildo_pussy_animation[Jean.vagina_Actions[0].mode]"
    
image Jean_masturbation_blinking:
    "characters/Jean/images/masturbation/eyes_[Jean.eyes].webp"
    choice:
        4.5
    choice:
        4.0
    choice:
        3.5
    "characters/Jean/images/masturbation/eyes_blink1.webp"
    0.023
    "characters/Jean/images/masturbation/eyes_blink2.webp"
    0.023
    "characters/Jean/images/masturbation/eyes_closed.webp"
    0.054
    "characters/Jean/images/masturbation/eyes_blink2.webp"
    0.018
    "characters/Jean/images/masturbation/eyes_blink1.webp"
    0.072
    repeat