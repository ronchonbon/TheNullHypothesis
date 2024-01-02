image Jean_sprite missionary:
    contains:
        "Jean_missionary_temp"

    offset (int(300*0.38), int(300*0.38))
            
layeredimage Jean_missionary_temp:
    if Jean.hovered:
        At("Jean_missionary_controls_temp", hover)
    else:
        "Jean_missionary_controls_temp"
            
layeredimage Jean_missionary_controls_temp:
    if speed > 2.5 or speed <= 1.75:
        Null()
    elif intensity >= 2.0:
        At(At("Jean_missionary", speed_200), intensity_200)
    elif intensity >= 1.75:
        At(At("Jean_missionary", speed_200), intensity_175)
    elif intensity >= 1.5:
        At(At("Jean_missionary", speed_200), intensity_150)
    elif intensity >= 1.25:
        At(At("Jean_missionary", speed_200), intensity_125)
    elif intensity >= 1.0:
        At(At("Jean_missionary", speed_200), intensity_100)
    elif intensity >= 0.75:
        At(At("Jean_missionary", speed_200), intensity_075)
    elif intensity >= 0.5:
        At(At("Jean_missionary", speed_200), intensity_050)
    elif intensity >= 0.25:
        At(At("Jean_missionary", speed_200), intensity_025)
    else:
        At(At("Jean_missionary", speed_200), intensity_000)

    if speed > 1.75 or speed <= 1.5:
        Null()
    elif intensity >= 2.0:
        At(At("Jean_missionary", speed_175), intensity_200)
    elif intensity >= 1.75:
        At(At("Jean_missionary", speed_175), intensity_175)
    elif intensity >= 1.5:
        At(At("Jean_missionary", speed_175), intensity_150)
    elif intensity >= 1.25:
        At(At("Jean_missionary", speed_175), intensity_125)
    elif intensity >= 1.0:
        At(At("Jean_missionary", speed_175), intensity_100)
    elif intensity >= 0.75:
        At(At("Jean_missionary", speed_175), intensity_075)
    elif intensity >= 0.5:
        At(At("Jean_missionary", speed_175), intensity_050)
    elif intensity >= 0.25:
        At(At("Jean_missionary", speed_175), intensity_025)
    else:
        At(At("Jean_missionary", speed_175), intensity_000)

    if speed > 1.5 or speed <= 1.25:
        Null()
    elif intensity >= 2.0:
        At(At("Jean_missionary", speed_150), intensity_200)
    elif intensity >= 1.75:
        At(At("Jean_missionary", speed_150), intensity_175)
    elif intensity >= 1.5:
        At(At("Jean_missionary", speed_150), intensity_150)
    elif intensity >= 1.25:
        At(At("Jean_missionary", speed_150), intensity_125)
    elif intensity >= 1.0:
        At(At("Jean_missionary", speed_150), intensity_100)
    elif intensity >= 0.75:
        At(At("Jean_missionary", speed_150), intensity_075)
    elif intensity >= 0.5:
        At(At("Jean_missionary", speed_150), intensity_050)
    elif intensity >= 0.25:
        At(At("Jean_missionary", speed_150), intensity_025)
    else:
        At(At("Jean_missionary", speed_150), intensity_000)
 
    if speed > 1.25 or speed <= 1.0:
        Null()
    elif intensity >= 2.0:
        At(At("Jean_missionary", speed_125), intensity_200)
    elif intensity >= 1.75:
        At(At("Jean_missionary", speed_125), intensity_175)
    elif intensity >= 1.5:
        At(At("Jean_missionary", speed_125), intensity_150)
    elif intensity >= 1.25:
        At(At("Jean_missionary", speed_125), intensity_125)
    elif intensity >= 1.0:
        At(At("Jean_missionary", speed_125), intensity_100)
    elif intensity >= 0.75:
        At(At("Jean_missionary", speed_125), intensity_075)
    elif intensity >= 0.5:
        At(At("Jean_missionary", speed_125), intensity_050)
    elif intensity >= 0.25:
        At(At("Jean_missionary", speed_125), intensity_025)
    else:
        At(At("Jean_missionary", speed_125), intensity_000)
 
    if speed > 1.0 or speed <= 0.75:
        Null()
    elif intensity >= 2.0:
        At(At("Jean_missionary", speed_100), intensity_200)
    elif intensity >= 1.75:
        At(At("Jean_missionary", speed_100), intensity_175)
    elif intensity >= 1.5:
        At(At("Jean_missionary", speed_100), intensity_150)
    elif intensity >= 1.25:
        At(At("Jean_missionary", speed_100), intensity_125)
    elif intensity >= 1.0:
        At(At("Jean_missionary", speed_100), intensity_100)
    elif intensity >= 0.75:
        At(At("Jean_missionary", speed_100), intensity_075)
    elif intensity >= 0.5:
        At(At("Jean_missionary", speed_100), intensity_050)
    elif intensity >= 0.25:
        At(At("Jean_missionary", speed_100), intensity_025)
    else:
        At(At("Jean_missionary", speed_100), intensity_000)

    if speed > 0.75 or speed <= 0.5:
        Null()
    elif intensity >= 2.0:
        At(At("Jean_missionary", speed_075), intensity_200)
    elif intensity >= 1.75:
        At(At("Jean_missionary", speed_075), intensity_175)
    elif intensity >= 1.5:
        At(At("Jean_missionary", speed_075), intensity_150)
    elif intensity >= 1.25:
        At(At("Jean_missionary", speed_075), intensity_125)
    elif intensity >= 1.0:
        At(At("Jean_missionary", speed_075), intensity_100)
    elif intensity >= 0.75:
        At(At("Jean_missionary", speed_075), intensity_075)
    elif intensity >= 0.5:
        At(At("Jean_missionary", speed_075), intensity_050)
    elif intensity >= 0.25:
        At(At("Jean_missionary", speed_075), intensity_025)
    else:
        At(At("Jean_missionary", speed_075), intensity_000)

    if speed > 0.5 or speed <= 0.25:
        Null()
    elif intensity >= 2.0:
        At(At("Jean_missionary", speed_050), intensity_200)
    elif intensity >= 1.75:
        At(At("Jean_missionary", speed_050), intensity_175)
    elif intensity >= 1.5:
        At(At("Jean_missionary", speed_050), intensity_150)
    elif intensity >= 1.25:
        At(At("Jean_missionary", speed_050), intensity_125)
    elif intensity >= 1.0:
        At(At("Jean_missionary", speed_050), intensity_100)
    elif intensity >= 0.75:
        At(At("Jean_missionary", speed_050), intensity_075)
    elif intensity >= 0.5:
        At(At("Jean_missionary", speed_050), intensity_050)
    elif intensity >= 0.25:
        At(At("Jean_missionary", speed_050), intensity_025)
    else:
        At(At("Jean_missionary", speed_050), intensity_000)

    if speed > 0.25 or speed <= 0.01:
        Null()
    elif intensity >= 2.0:
        At(At("Jean_missionary", speed_025), intensity_200)
    elif intensity >= 1.75:
        At(At("Jean_missionary", speed_025), intensity_175)
    elif intensity >= 1.5:
        At(At("Jean_missionary", speed_025), intensity_150)
    elif intensity >= 1.25:
        At(At("Jean_missionary", speed_025), intensity_125)
    elif intensity >= 1.0:
        At(At("Jean_missionary", speed_025), intensity_100)
    elif intensity >= 0.75:
        At(At("Jean_missionary", speed_025), intensity_075)
    elif intensity >= 0.5:
        At(At("Jean_missionary", speed_025), intensity_050)
    elif intensity >= 0.25:
        At(At("Jean_missionary", speed_025), intensity_025)
    else:
        At(At("Jean_missionary", speed_025), intensity_000)

    if speed != 0.01:
        Null()
    elif intensity >= 2.0:
        At(At("Jean_missionary", speed_0001), intensity_200)
    elif intensity >= 1.75:
        At(At("Jean_missionary", speed_0001), intensity_175)
    elif intensity >= 1.5:
        At(At("Jean_missionary", speed_0001), intensity_150)
    elif intensity >= 1.25:
        At(At("Jean_missionary", speed_0001), intensity_125)
    elif intensity >= 1.0:
        At(At("Jean_missionary", speed_0001), intensity_100)
    elif intensity >= 0.75:
        At(At("Jean_missionary", speed_0001), intensity_075)
    elif intensity >= 0.5:
        At(At("Jean_missionary", speed_0001), intensity_050)
    elif intensity >= 0.25:
        At(At("Jean_missionary", speed_0001), intensity_025)
    else:
        At(At("Jean_missionary", speed_0001), intensity_000)

    if speed >= 0.01 or speed < 0.0:
        Null()
    elif intensity >= 2.0:
        At(At("Jean_missionary", speed_000), intensity_200)
    elif intensity >= 1.75:
        At(At("Jean_missionary", speed_000), intensity_175)
    elif intensity >= 1.5:
        At(At("Jean_missionary", speed_000), intensity_150)
    elif intensity >= 1.25:
        At(At("Jean_missionary", speed_000), intensity_125)
    elif intensity >= 1.0:
        At(At("Jean_missionary", speed_000), intensity_100)
    elif intensity >= 0.75:
        At(At("Jean_missionary", speed_000), intensity_075)
    elif intensity >= 0.5:
        At(At("Jean_missionary", speed_000), intensity_050)
    elif intensity >= 0.25:
        At(At("Jean_missionary", speed_000), intensity_025)
    else:
        At(At("Jean_missionary", speed_000), intensity_000)
 
layeredimage Jean_missionary:
    if Player.orgasming and focused_Character == Jean:
        "Jean_missionary_thighs_animation0"
    elif Player.cock_Actions and Jean in Player.cock_Actions[0].Targets:
        "Jean_missionary_thighs_animation[Player.cock_Actions[0].mode]"
    else:
        "Jean_missionary_thighs_animation0"
    
layeredimage Jean_missionary_thighs:
    if Player.orgasming and focused_Character == Jean:
        "Jean_missionary_torso_animation0"
    elif Player.cock_Actions and Jean in Player.cock_Actions[0].Targets and Jean.check_traits("orgasming"):
        At("Jean_missionary_torso_animation[Player.cock_Actions[0].mode]", tremble(20))
    elif Player.cock_Actions and Jean in Player.cock_Actions[0].Targets:
        "Jean_missionary_torso_animation[Player.cock_Actions[0].mode]"
    elif Jean.check_traits("orgasming"):
        At("Jean_missionary_torso_animation0", tremble(20))
    else:
        "Jean_missionary_torso_animation0"

    always:
        "characters/Jean/images/missionary/thighs.webp"

    if Player.orgasming == "anal_creampie" and focused_Character == Jean:
        "Jean_missionary_anus_anal_creampie_animation"
    elif not Jean.anus_Actions:
        "Jean_missionary_anus_closed"
    elif Jean.anus_Actions[0].animation_type == "eat_ass":
        "Jean_missionary_anus_open"
    elif Jean.anus_Actions[0].animation_type in ["dildo_ass", "self_dildo_ass"]:
        "Jean_missionary_anus_dildo_ass_animation[Jean.anus_Actions[0].mode]"
    elif Jean.anus_Actions[0].animation_type == "finger_ass":
        "Jean_missionary_anus_finger_ass_animation[Jean.anus_Actions[0].mode]"
    elif Player.orgasming and focused_Character == Jean:
        "Jean_missionary_anus_closed"
    else:
        "Jean_missionary_anus_[Jean.anus_Actions[0].animation_type]_animation[Jean.anus_Actions[0].mode]"

    if Player.orgasming == "creampie" and focused_Character == Jean:
        "Jean_missionary_pussy_creampie_animation"
    elif Jean.vagina_Actions and Jean.vagina_Actions[0].animation_type in ["dildo_pussy", "self_dildo_pussy"]:
        "Jean_missionary_pussy_dildo_pussy_animation[Jean.vagina_Actions[0].mode]"
    elif Jean.vagina_Actions and Jean.vagina_Actions[0].animation_type in ["finger_pussy", "self_touch_pussy"]:
        "Jean_missionary_pussy_[Jean.vagina_Actions[0].animation_type]_animation[Jean.vagina_Actions[0].mode]"
    elif Player.orgasming and focused_Character == Jean:
        "Jean_missionary_pussy_closed"
    elif Jean.vagina_Actions:
        "Jean_missionary_pussy_[Jean.vagina_Actions[0].animation_type]_animation[Jean.vagina_Actions[0].mode]"
    elif Jean.clitoris_Actions:
        "Jean_missionary_pussy_closed"
    else:
        "Jean_missionary_pussy_closed"

    if Jean.tan_lines["bottom"]:
        "characters/Jean/images/missionary/tan_lines_[Jean.tan_lines[bottom]].webp"

    if Jean.tan_lines["full"]:
        "characters/Jean/images/missionary/tan_lines_[Jean.tan_lines[full]]_thighs.webp"

    if Player.orgasming == "anal_creampie" and focused_Character == Jean:
        "Jean_missionary_anal_creampie"
    elif not Jean.creampie["anus"]:
        Null()
    elif Jean.anus_Actions and Jean.anus_Actions[0].animation_type == "eat_ass":
        "characters/Jean/images/missionary/creampie_anus_open.webp"
    elif Jean.anus_Actions:
        "characters/Jean/images/missionary/creampie_anus_agape.webp"
    else:
        "characters/Jean/images/missionary/creampie_anus_closed.webp"

    if not Jean.buttplug:
        Null()
    elif Jean.buttplug.string == "heart_anal_plug":
        "characters/Jean/images/missionary/buttplug_heart.webp"
    elif Jean.buttplug.string == "round_anal_plug":
        "characters/Jean/images/missionary/buttplug_round.webp"

    if Jean.anus_Actions and Jean.anus_Actions[0].animation_type in ["dildo_ass", "self_dildo_ass"]:
        AlphaMask("Jean_missionary_dildo_ass_animations", "Jean_missionary_mask_anus_animations")

    if not Player.check_traits("body_visible"):
        Null()
    elif Player.orgasming and focused_Character == Jean:
        "Jean_missionary_male_body_[Player.orgasming]_animation"
    elif Player.cock_Actions and Jean in Player.cock_Actions[0].Targets:
        "Jean_missionary_male_body_[Player.cock_Actions[0].animation_type]_animation[Player.cock_Actions[0].mode]"

    if Player.orgasming == "creampie" and focused_Character == Jean:
        "Jean_missionary_creampie"
    elif not Jean.creampie["pussy"]:
        Null()
    elif Jean.vagina_Actions:
        "characters/Jean/images/missionary/creampie_pussy_agape.webp"
    elif Jean.clitoris_Actions:
        "characters/Jean/images/missionary/creampie_pussy_open.webp"
    else:
        "characters/Jean/images/missionary/creampie_pussy_closed.webp"

    if Jean.piercings["labia"] in ["barbell", "both"]:
        "characters/Jean/images/missionary/labia_piercings_barbell.webp"

    if Jean.piercings["labia"] in ["ring", "both"]:
        "characters/Jean/images/missionary/labia_piercings_ring.webp"

    if "pubic" in Jean.body_hair_growing.keys():
        "characters/Jean/images/missionary/pubes_growing.webp"

    if not Jean.body_hair["pubic"]:
        Null()
    elif "triangle" in Jean.body_hair["pubic"]:
        "characters/Jean/images/missionary/pubes_triangle.webp"
    elif "strip" in Jean.body_hair["pubic"]:
        "characters/Jean/images/missionary/pubes_strip.webp"
    else:
        "characters/Jean/images/missionary/pubes_[Jean.body_hair[pubic]].webp"

    if Jean.remote_vibrator is not None:
        "characters/Jean/images/missionary/remote_vibrator.webp"

    if Player.orgasming and focused_Character == Jean:
        Null()
    elif not Jean.anus_Actions or Jean.anus_Actions[0].animation_type != "finger_ass":
        Null()
    elif Player.left_hand_Actions and Jean in Player.left_hand_Actions[0].Targets and Player.left_hand_Actions[0].animation_type == "finger_ass":
        AlphaMask("Jean_missionary_male_left_arm_finger_animations", "Jean_missionary_mask_anus_animations")
    elif Player.right_hand_Actions and Jean in Player.right_hand_Actions[0].Targets and Player.right_hand_Actions[0].animation_type == "finger_ass":
        AlphaMask("Jean_missionary_male_right_arm_finger_animations", "Jean_missionary_mask_anus_animations")

    if Player.orgasming == "anal_creampie" and focused_Character == Jean:
        AlphaMask("Jean_missionary_cock_animations", "Jean_missionary_mask_anus_animations")
    elif Player.orgasming and focused_Character == Jean:
        Null()
    elif Player.cock_Actions and Jean in Player.cock_Actions[0].Targets and Player.cock_Actions[0].animation_type == "anal":
        AlphaMask("Jean_missionary_cock_animations", "Jean_missionary_mask_anus_animations")

    if Player.orgasming and focused_Character == Jean:
        Null()
    elif not Jean.vagina_Actions or Jean.vagina_Actions[0].animation_type != "finger_pussy":
        Null()
    elif Player.left_hand_Actions and Jean in Player.left_hand_Actions[0].Targets and Player.left_hand_Actions[0].animation_type == "finger_pussy":
        AlphaMask("Jean_missionary_male_left_arm_finger_animations", "Jean_missionary_mask_pussy_animations")
    elif Player.right_hand_Actions and Jean in Player.right_hand_Actions[0].Targets and Player.right_hand_Actions[0].animation_type == "finger_pussy":
        AlphaMask("Jean_missionary_male_right_arm_finger_animations", "Jean_missionary_mask_pussy_animations")

    if Jean.vagina_Actions and Jean.vagina_Actions[0].animation_type in ["dildo_pussy", "self_dildo_pussy"]:
        AlphaMask("Jean_missionary_dildo_pussy_animations", "Jean_missionary_mask_pussy_animations")

    if Player.orgasming == "creampie" and focused_Character == Jean:
        AlphaMask("Jean_missionary_cock_animations", "Jean_missionary_mask_pussy_animations")
    elif Player.orgasming and focused_Character == Jean:
        Null()
    elif Player.cock_Actions and Jean in Player.cock_Actions[0].Targets and Player.cock_Actions[0].animation_type == "sex":
        AlphaMask("Jean_missionary_cock_animations", "Jean_missionary_mask_pussy_animations")

    if Jean.right_hand_Actions and Jean.right_hand_Actions[0].animation_type == "self_touch_pussy":
        "Jean_missionary_right_forearm_self_touch_pussy_animation[Jean.right_hand_Actions[0].mode]"

    if Player.orgasming and focused_Character == Jean:
        "Jean_missionary_left_leg_animation0"
    elif Player.cock_Actions and Jean in Player.cock_Actions[0].Targets and Jean.check_traits("orgasming"):
        At("Jean_missionary_left_leg_animation[Player.cock_Actions[0].mode]", tremble(20))
    elif Player.cock_Actions and Jean in Player.cock_Actions[0].Targets:
        "Jean_missionary_left_leg_animation[Player.cock_Actions[0].mode]"
    elif Jean.check_traits("orgasming"):
        At("Jean_missionary_left_leg_animation0", tremble(20))
    else:
        "Jean_missionary_left_leg_animation0"

    if Player.orgasming and focused_Character == Jean:
        "Jean_missionary_right_leg_animation0"
    elif Player.cock_Actions and Jean in Player.cock_Actions[0].Targets and Jean.check_traits("orgasming"):
        At("Jean_missionary_right_leg_animation[Player.cock_Actions[0].mode]", tremble(20))
    elif Player.cock_Actions and Jean in Player.cock_Actions[0].Targets:
        "Jean_missionary_right_leg_animation[Player.cock_Actions[0].mode]"
    elif Jean.check_traits("orgasming"):
        At("Jean_missionary_right_leg_animation0", tremble(20))
    else:
        "Jean_missionary_right_leg_animation0"

    if Jean.clitoris_Actions and Jean.clitoris_Actions[0].animation_type in ["vibrator", "self_vibrator"]:
        "Jean_missionary_vibrator_animation[Jean.clitoris_Actions[0].mode]"

    if Player.orgasming == "cumshot" and focused_Character == Jean:
        "Jean_missionary_cock_animations"
    elif Player.cock_Actions and Jean in Player.cock_Actions[0].Targets and Player.cock_Actions[0].animation_type in ["grind_pussy", "grind_ass"]:
        "Jean_missionary_cock_animations"
        
    if Player.orgasming == "cumshot" and focused_Character == Jean:
        "Jean_missionary_cumshot"

    if not Player.check_traits("body_visible"):
        Null()
    elif Player.orgasming and focused_Character == Jean:
        "Jean_missionary_male_knees_[Player.orgasming]_animation"
    elif Player.cock_Actions and Jean in Player.cock_Actions[0].Targets:
        "Jean_missionary_male_knees_[Player.cock_Actions[0].animation_type]_animation[Player.cock_Actions[0].mode]"

    if not Player.left_hand_Actions or Jean not in Player.left_hand_Actions[0].Targets:
        Null()
    elif Player.left_hand_Actions[0].animation_type == "touch_breasts" and Jean.right_breast_Actions and Player.left_hand_Actions[0].animation_type == Jean.right_breast_Actions[0].animation_type:
        At("Jean_missionary_male_left_arm_touch_right_breast_animation[Player.left_hand_Actions[0].mode]", change_offset(Jean_missionary_right_breast_position[0], Jean_missionary_right_breast_position[1]))
    elif Player.left_hand_Actions[0].animation_type == "touch_breasts" and Jean.left_breast_Actions and Player.left_hand_Actions[0].animation_type == Jean.left_breast_Actions[0].animation_type:
        At("Jean_missionary_male_left_arm_touch_left_breast_animation[Player.left_hand_Actions[0].mode]", change_offset(Jean_missionary_left_breast_position[0], Jean_missionary_left_breast_position[1]))
    elif Player.left_hand_Actions[0].animation_type == "pinch_nipples" and Jean.right_nipple_Actions and Player.left_hand_Actions[0].animation_type == Jean.right_nipple_Actions[0].animation_type:
        At("Jean_missionary_male_left_arm_touch_right_breast_animation[Player.left_hand_Actions[0].mode]", change_offset(Jean_missionary_right_nipple_position[0], Jean_missionary_right_nipple_position[1]))
    elif Player.left_hand_Actions[0].animation_type == "pinch_nipples" and Jean.left_nipple_Actions and Player.left_hand_Actions[0].animation_type == Jean.left_nipple_Actions[0].animation_type:
        At("Jean_missionary_male_left_arm_touch_left_breast_animation[Player.left_hand_Actions[0].mode]", change_offset(Jean_missionary_left_nipple_position[0], Jean_missionary_left_nipple_position[1]))

    if not Player.right_hand_Actions or Jean not in Player.right_hand_Actions[0].Targets:
        Null()
    elif Player.right_hand_Actions[0].animation_type == "touch_breasts" and Jean.right_breast_Actions and Player.right_hand_Actions[0].animation_type == Jean.right_breast_Actions[0].animation_type:
        At("Jean_missionary_male_right_arm_touch_right_breast_animation[Player.right_hand_Actions[0].mode]", change_offset(Jean_missionary_right_breast_position[0], Jean_missionary_right_breast_position[1]))
    elif Player.right_hand_Actions[0].animation_type == "touch_breasts" and Jean.left_breast_Actions and Player.right_hand_Actions[0].animation_type == Jean.left_breast_Actions[0].animation_type:
        At("Jean_missionary_male_right_arm_touch_left_breast_animation[Player.right_hand_Actions[0].mode]", change_offset(Jean_missionary_left_breast_position[0], Jean_missionary_left_breast_position[1]))
    elif Player.right_hand_Actions[0].animation_type == "pinch_nipples" and Jean.right_nipple_Actions and Player.right_hand_Actions[0].animation_type == Jean.right_nipple_Actions[0].animation_type:
        At("Jean_missionary_male_right_arm_touch_right_breast_animation[Player.right_hand_Actions[0].mode]", change_offset(Jean_missionary_right_nipple_position[0], Jean_missionary_right_nipple_position[1]))
    elif Player.right_hand_Actions[0].animation_type == "pinch_nipples" and Jean.left_nipple_Actions and Player.right_hand_Actions[0].animation_type == Jean.left_nipple_Actions[0].animation_type:
        At("Jean_missionary_male_right_arm_touch_left_breast_animation[Player.right_hand_Actions[0].mode]", change_offset(Jean_missionary_left_nipple_position[0], Jean_missionary_left_nipple_position[1]))

    if Player.orgasming and focused_Character == Jean:
        Null()
    elif not Player.mouth_Actions or Jean not in Player.mouth_Actions[0].Targets:
        Null()
    elif Player.mouth_Actions[0].animation_type == "suck_nipples" and Jean.right_nipple_Actions and Jean.right_nipple_Actions[0].animation_type == "suck_nipples":
        At("Jean_missionary_male_head_suck_right_nipple_animation[Player.mouth_Actions[0].mode]", change_offset(Jean_missionary_right_nipple_position[0], Jean_missionary_right_nipple_position[1]))
    elif Player.mouth_Actions[0].animation_type == "suck_nipples" and Jean.left_nipple_Actions and Jean.left_nipple_Actions[0].animation_type == "suck_nipples":
        At("Jean_missionary_male_head_suck_left_nipple_animation[Player.mouth_Actions[0].mode]", change_offset(Jean_missionary_left_nipple_position[0], Jean_missionary_left_nipple_position[1]))
    elif Player.mouth_Actions[0].animation_type == "eat_pussy":
        At("Jean_missionary_male_head_eat_pussy_animation[Player.mouth_Actions[0].mode]", change_offset(Jean_missionary_pussy_position[0], Jean_missionary_pussy_position[1]))
    elif Player.mouth_Actions[0].animation_type == "eat_ass":
        At("Jean_missionary_male_head_eat_ass_animation[Player.mouth_Actions[0].mode]", change_offset(Jean_missionary_anus_position[0], Jean_missionary_anus_position[1]))

    anchor (int(1992*sex_sampling), int(2446*sex_sampling))
    offset (int(1992*sex_sampling), int(2446*sex_sampling))
    
layeredimage Jean_missionary_torso:
    if Player.orgasming and focused_Character == Jean:
        "Jean_missionary_hair_back_animation0"
    elif Player.cock_Actions and Jean in Player.cock_Actions[0].Targets:
        "Jean_missionary_hair_back_animation[Player.cock_Actions[0].mode]"
    else:
        "Jean_missionary_hair_back_animation0"

    if Player.orgasming and focused_Character == Jean:
        "Jean_missionary_left_arm_animation0"
    elif Player.cock_Actions and Jean in Player.cock_Actions[0].Targets:
        "Jean_missionary_left_arm_animation[Player.cock_Actions[0].mode]"
    else:
        "Jean_missionary_left_arm_animation0"

    if Jean.right_hand_Actions and Jean.right_hand_Actions[0].animation_type == "self_touch_pussy":
        Null()
    elif Player.orgasming and focused_Character == Jean:
        "Jean_missionary_right_arm_animation0"
    elif Player.cock_Actions and Jean in Player.cock_Actions[0].Targets:
        "Jean_missionary_right_arm_animation[Player.cock_Actions[0].mode]"
    else:
        "Jean_missionary_right_arm_animation0"

    always:
        "characters/Jean/images/missionary/torso.webp"

    if Jean.piercings["belly"]:
        "characters/Jean/images/missionary/belly_piercing.webp"

    if Jean.spunk["belly"]:
        "characters/Jean/images/missionary/spunk_belly.webp"

    if Jean.right_hand_Actions and Jean.right_hand_Actions[0].animation_type == "self_touch_pussy":
        "Jean_missionary_right_arm_self_touch_pussy_animation[Jean.right_hand_Actions[0].mode]"

    if Player.orgasming and focused_Character == Jean:
        "Jean_missionary_breasts_animation0"
    elif Player.cock_Actions and Jean in Player.cock_Actions[0].Targets:
        "Jean_missionary_breasts_animation[Player.cock_Actions[0].mode]"
    else:
        "Jean_missionary_breasts_animation0"

    if not Player.left_hand_Actions or Jean not in Player.left_hand_Actions[0].Targets:
        Null()
    elif Player.left_hand_Actions[0].animation_type == "choke":
        At("Jean_missionary_male_left_arm_choke_animation[Player.left_hand_Actions[0].mode]", change_offset(Jean_missionary_neck_position[0], Jean_missionary_neck_position[1]))

    if not Player.right_hand_Actions or Jean not in Player.right_hand_Actions[0].Targets:
        Null()
    elif Player.right_hand_Actions[0].animation_type == "choke":
        At("Jean_missionary_male_right_arm_choke_animation[Player.right_hand_Actions[0].mode]", change_offset(Jean_missionary_neck_position[0], Jean_missionary_neck_position[1]))

    if Player.orgasming and focused_Character == Jean:
        "Jean_missionary_head_animation0"
    elif Player.cock_Actions and Jean in Player.cock_Actions[0].Targets:
        "Jean_missionary_head_animation[Player.cock_Actions[0].mode]"
    else:
        "Jean_missionary_head_animation0"

    anchor (int(1992*sex_sampling), int(2446*sex_sampling))
    offset (int(1992*sex_sampling), int(2446*sex_sampling))
    
image Jean_missionary_hair_back:
    "characters/Jean/images/missionary/hair_back.webp"

    anchor (int(2299*sex_sampling), int(1031*sex_sampling))
    offset (int(2299*sex_sampling), int(1031*sex_sampling))
    
image Jean_missionary_left_arm:
    "characters/Jean/images/missionary/left_arm.webp"

    anchor (int(2712*sex_sampling), int(1289*sex_sampling))
    offset (int(2712*sex_sampling), int(1289*sex_sampling))
    
image Jean_missionary_right_arm:
    "characters/Jean/images/missionary/right_arm.webp"

    anchor (int(1830*sex_sampling), int(1241*sex_sampling))
    offset (int(1830*sex_sampling), int(1241*sex_sampling))
    
image Jean_missionary_right_arm_self_touch_pussy:
    "characters/Jean/images/missionary/right_arm_finger.webp"

    anchor (int(1808*sex_sampling), int(1244*sex_sampling))
    offset (int(1808*sex_sampling), int(1244*sex_sampling))
    
layeredimage Jean_missionary_breasts:
    always:
        "characters/Jean/images/missionary/breasts.webp"

    if Jean.tan_lines["top"]:
        "characters/Jean/images/missionary/tan_lines_[Jean.tan_lines[top]].webp"

    if Jean.tan_lines["full"]:
        "characters/Jean/images/missionary/tan_lines_[Jean.tan_lines[full]]_torso.webp"

    if Jean.piercings["nipple"] in ["barbell", "both"]:
        "characters/Jean/images/missionary/nipple_piercings_barbell.webp"

    if Jean.piercings["nipple"] in ["ring", "both"]:
        "characters/Jean/images/missionary/nipple_piercings_ring.webp"

    if Jean.spunk["breasts"]:
        "characters/Jean/images/missionary/spunk_breasts.webp"

    anchor (int(1992*sex_sampling), int(2446*sex_sampling))
    offset (int(1992*sex_sampling), int(2446*sex_sampling))
    
layeredimage Jean_missionary_head:
    always:
        "characters/Jean/images/missionary/head_[Jean.mouth].webp"

    if Jean.eyes in ["closed", "down", "left", "right", "squint", "up"]:
        "characters/Jean/images/missionary/eyes_[Jean.eyes].webp"
    else:
        "Jean_missionary_blinking"

    always:
        "characters/Jean/images/missionary/brows_[Jean.brows].webp"

    if Jean.blush:
            "characters/Jean/images/missionary/blush[Jean.blush].webp"
        
    if Jean.spunk["tongue"] and Jean.mouth in ["agape", "tongue"]:
        "characters/Jean/images/missionary/spunk_tongue.webp"

    if Jean.spunk["mouth"] and Jean.mouth in ["agape", "tongue"]:
        "characters/Jean/images/missionary/spunk_mouth.webp"
        
    if Jean.spunk["chin"]:
        "characters/Jean/images/missionary/spunk_chin.webp"
        
    if Jean.spunk["face"]:
        "characters/Jean/images/missionary/spunk_face.webp"

    if Player.orgasming and focused_Character == Jean:
        "Jean_missionary_hair_animation0"
    elif Player.cock_Actions and Jean in Player.cock_Actions[0].Targets:
        "Jean_missionary_hair_animation[Player.cock_Actions[0].mode]"
    else:
        "Jean_missionary_hair_animation0"

    if Jean.check_traits("psychic"):
        "characters/Jean/images/missionary/psychic.webp"

    anchor (int(2299*sex_sampling), int(1031*sex_sampling))
    offset (int(2299*sex_sampling), int(1031*sex_sampling))
    
layeredimage Jean_missionary_hair:
    # if Jean.check_traits("wet") or Jean.Clothes["hair"].string == "wet":
    #     "characters/Jean/images/missionary/hair_shadow_wet.webp"
    # else:
    always:
        "characters/Jean/images/missionary/hair_shadow_[Jean.Clothes[hair].string].webp"

    # if Jean.check_traits("wet") or Jean.Clothes["hair"].string == "wet":
    #     "characters/Jean/images/missionary/hair_wet.webp"
    # else:
    always:
        "characters/Jean/images/missionary/hair_[Jean.Clothes[hair].string].webp"

    if Jean.spunk["hair"]:
        "characters/Jean/images/missionary/spunk_hair.webp"

    anchor (int(2299*sex_sampling), int(1031*sex_sampling))
    offset (int(2299*sex_sampling), int(1031*sex_sampling))
    
image Jean_missionary_anus_closed:
    "characters/Jean/images/missionary/anus_closed.webp"

    anchor (int(2017*sex_sampling), int(2985*sex_sampling))
    offset (int(2017*sex_sampling), int(2985*sex_sampling))

image Jean_missionary_anus_open:
    "characters/Jean/images/missionary/anus_open.webp"

    anchor (int(2017*sex_sampling), int(2985*sex_sampling))
    offset (int(2017*sex_sampling), int(2985*sex_sampling))

image Jean_missionary_anus_agape:
    "characters/Jean/images/missionary/anus_agape.webp"

    anchor (int(2016*sex_sampling), int(2977*sex_sampling))
    offset (int(2016*sex_sampling), int(2977*sex_sampling))
    
image Jean_missionary_pussy_closed:
    "characters/Jean/images/missionary/pussy_closed.webp"

    anchor (int(2007*sex_sampling), int(2884*sex_sampling))
    offset (int(2007*sex_sampling), int(2884*sex_sampling))

image Jean_missionary_pussy_open:
    "characters/Jean/images/missionary/pussy_open.webp"

    anchor (int(2007*sex_sampling), int(2884*sex_sampling))
    offset (int(2007*sex_sampling), int(2884*sex_sampling))

image Jean_missionary_pussy_agape:
    "characters/Jean/images/missionary/pussy_agape.webp"

    anchor (int(2003*sex_sampling), int(2877*sex_sampling))
    offset (int(2003*sex_sampling), int(2877*sex_sampling))
    
layeredimage Jean_missionary_right_forearm_self_touch_pussy:
    always:
        "characters/Jean/images/missionary/right_forearm_finger_shadow.webp"

    always:
        "characters/Jean/images/missionary/right_forearm_finger.webp"

    anchor (int(1512*sex_sampling), int(1832*sex_sampling))
    offset (int(1512*sex_sampling), int(1832*sex_sampling))
    
layeredimage Jean_missionary_left_leg:
    always:
        "characters/Jean/images/missionary/left_leg.webp"

    if Player.orgasming and focused_Character == Jean:
        "Jean_missionary_left_foot_animation0"
    elif Player.cock_Actions and Jean in Player.cock_Actions[0].Targets:
        "Jean_missionary_left_foot_animation[Player.cock_Actions[0].mode]"
    else:
        "Jean_missionary_left_foot_animation0"

    anchor (int(3618*sex_sampling), int(2693*sex_sampling))
    offset (int(3618*sex_sampling), int(2693*sex_sampling))
    
layeredimage Jean_missionary_left_foot:
    always:
        "characters/Jean/images/missionary/left_foot.webp"

    anchor (int(3240*sex_sampling), int(4002*sex_sampling))
    offset (int(3240*sex_sampling), int(4002*sex_sampling))
    
layeredimage Jean_missionary_right_leg:
    always:
        "characters/Jean/images/missionary/right_leg.webp"

    if Player.orgasming and focused_Character == Jean:
        "Jean_missionary_right_foot_animation0"
    elif Player.cock_Actions and Jean in Player.cock_Actions[0].Targets:
        "Jean_missionary_right_foot_animation[Player.cock_Actions[0].mode]"
    else:
        "Jean_missionary_right_foot_animation0"

    anchor (int(574*sex_sampling), int(2327*sex_sampling))
    offset (int(574*sex_sampling), int(2327*sex_sampling))
    
layeredimage Jean_missionary_right_foot:
    always:
        "characters/Jean/images/missionary/right_foot.webp"

    anchor (int(967*sex_sampling), int(3809*sex_sampling))
    offset (int(967*sex_sampling), int(3809*sex_sampling))
    
image Jean_missionary_male_body:
    "characters/Jean/images/missionary/male_body_[Player.skin_color].webp"

    anchor (int(2012*sex_sampling), int(3071*sex_sampling))
    offset (int(2012*sex_sampling), int(3071*sex_sampling))
    
image Jean_missionary_cock:
    "characters/Jean/images/missionary/cock_[Player.skin_color].webp"

    anchor (int(2012*sex_sampling), int(3071*sex_sampling))
    offset (int(2012*sex_sampling), int(3071*sex_sampling))

image Jean_missionary_spunk_tip:
    "characters/Jean/images/missionary/spunk_tip.webp"

    anchor (int(2012*sex_sampling), int(3071*sex_sampling))
    offset (int(2012*sex_sampling), int(3071*sex_sampling))
    
image Jean_missionary_male_knees:
    "characters/Jean/images/missionary/male_knees_[Player.skin_color].webp"

    anchor (int(2012*sex_sampling), int(3071*sex_sampling))
    offset (int(2012*sex_sampling), int(3071*sex_sampling))

image Jean_missionary_male_left_arm_finger:
    "characters/Jean/images/missionary/male_left_arm_[Player.skin_color]_finger.webp"

    anchor (int(2025*sex_sampling), int(2795*sex_sampling))
    offset (int(2025*sex_sampling), int(2795*sex_sampling))

image Jean_missionary_male_right_arm_finger:
    "characters/Jean/images/missionary/male_right_arm_[Player.skin_color]_finger.webp"

    anchor (int(2025*sex_sampling), int(2795*sex_sampling))
    offset (int(2025*sex_sampling), int(2795*sex_sampling))

image Jean_missionary_dildo:
    "characters/Jean/images/missionary/dildo.webp"

    anchor (int(2017*sex_sampling), int(2850*sex_sampling))
    offset (int(2017*sex_sampling), int(2850*sex_sampling))

image Jean_missionary_vibrator:
    "characters/Jean/images/missionary/vibrator.webp"

    anchor (int(2020*sex_sampling), int(2778*sex_sampling))
    offset (int(2020*sex_sampling), int(2778*sex_sampling))

image Jean_missionary_mask_anus:
    "characters/Jean/images/missionary/mask_anus.webp"

    anchor (int(2016*sex_sampling), int(2977*sex_sampling))
    offset (int(2016*sex_sampling), int(2977*sex_sampling))

image Jean_missionary_mask_pussy:
    "characters/Jean/images/missionary/mask_pussy.webp"

    anchor (int(2003*sex_sampling), int(2877*sex_sampling))
    offset (int(2003*sex_sampling), int(2877*sex_sampling))

layeredimage Jean_missionary_male_left_arm_fondle:
    if Player.left_hand_Actions[0].animation_type in ["touch_thighs", "touch_thighs_higher", "touch_breasts", "touch_pussy", "grab_ass"]:
        "Player_left_arm_fondle"
    elif Player.left_hand_Actions[0].animation_type in ["choke", "pinch_nipples"]:
        "Player_left_arm_pinch"

layeredimage Jean_missionary_male_right_arm_fondle:
    if Player.right_hand_Actions[0].animation_type in ["touch_thighs", "touch_thighs_higher", "touch_breasts", "touch_pussy", "grab_ass"]:
        "Player_right_arm_fondle"
    elif Player.right_hand_Actions[0].animation_type in ["choke", "pinch_nipples"]:
        "Player_right_arm_pinch"

layeredimage Jean_missionary_male_head:
    if Player.check_traits("body_visible"):
        "Player_head"

    if Player.mouth_Actions and Jean in Player.mouth_Actions[0].Targets and Player.mouth_Actions[0].animation_type in ["suck_nipples", "eat_pussy", "eat_ass"]:
        "Jean_missionary_male_tongue_animation[Player.mouth_Actions[0].mode]"

image Jean_missionary_male_tongue:
    "Player_tongue"

image Jean_missionary_hair_back_animation0:
    "Jean_missionary_hair_back"

    missionary_hair_back_animation0

image Jean_missionary_hair_back_animation1:
    "Jean_missionary_hair_back"

    missionary_hair_back_animation1

image Jean_missionary_hair_back_animation2:
    "Jean_missionary_hair_back"

    missionary_hair_back_animation2

image Jean_missionary_left_arm_animation0:
    "Jean_missionary_left_arm"

    missionary_left_arm_animation0

image Jean_missionary_left_arm_animation1:
    "Jean_missionary_left_arm"

    missionary_left_arm_animation1

image Jean_missionary_left_arm_animation2:
    "Jean_missionary_left_arm"

    missionary_left_arm_animation2

image Jean_missionary_right_arm_animation0:
    "Jean_missionary_right_arm"

    missionary_right_arm_animation0

image Jean_missionary_right_arm_animation1:
    "Jean_missionary_right_arm"

    missionary_right_arm_animation1

image Jean_missionary_right_arm_animation2:
    "Jean_missionary_right_arm"

    missionary_right_arm_animation2

image Jean_missionary_torso_animation0:
    "Jean_missionary_torso"

    missionary_torso_animation0

image Jean_missionary_torso_animation1:
    "Jean_missionary_torso"

    missionary_torso_animation1

image Jean_missionary_torso_animation2:
    "Jean_missionary_torso"

    missionary_torso_animation2

image Jean_missionary_right_arm_self_touch_pussy_animation0:
    "Jean_missionary_right_arm_self_touch_pussy"

    missionary_right_arm_self_touch_pussy_animation0

image Jean_missionary_right_arm_self_touch_pussy_animation1:
    "Jean_missionary_right_arm_self_touch_pussy"

    missionary_right_arm_self_touch_pussy_animation1

image Jean_missionary_right_arm_self_touch_pussy_animation2:
    "Jean_missionary_right_arm_self_touch_pussy"

    missionary_right_arm_self_touch_pussy_animation2

image Jean_missionary_breasts_animation0:
    "Jean_missionary_breasts"

    missionary_breasts_animation0

image Jean_missionary_breasts_animation1:
    "Jean_missionary_breasts"

    missionary_breasts_animation1

image Jean_missionary_breasts_animation2:
    "Jean_missionary_breasts"

    missionary_breasts_animation2

image Jean_missionary_head_animation0:
    "Jean_missionary_head"

    missionary_head_animation0

image Jean_missionary_head_animation1:
    "Jean_missionary_head"

    missionary_head_animation1

image Jean_missionary_head_animation2:
    "Jean_missionary_head"

    missionary_head_animation2

image Jean_missionary_hair_animation0:
    "Jean_missionary_hair"

    missionary_hair_animation0

image Jean_missionary_hair_animation1:
    "Jean_missionary_hair"

    missionary_hair_animation1

image Jean_missionary_hair_animation2:
    "Jean_missionary_hair"

    missionary_hair_animation2

image Jean_missionary_thighs_animation0:
    "Jean_missionary_thighs"

    missionary_thighs_animation0

image Jean_missionary_thighs_animation1:
    "Jean_missionary_thighs"

    missionary_thighs_animation1

image Jean_missionary_thighs_animation2:
    "Jean_missionary_thighs"

    missionary_thighs_animation2

image Jean_missionary_pussy_finger_pussy_animation0:
    "Jean_missionary_pussy_closed"

    missionary_pussy_finger_pussy_animation0

image Jean_missionary_pussy_finger_pussy_animation1:
    "Jean_missionary_pussy_agape"

    missionary_pussy_finger_pussy_animation1

image Jean_missionary_anus_finger_ass_animation0:
    "Jean_missionary_anus_closed"

    missionary_anus_finger_ass_animation0

image Jean_missionary_anus_finger_ass_animation1:
    "Jean_missionary_anus_agape"

    missionary_anus_finger_ass_animation1

image Jean_missionary_pussy_sex_animation0:
    "Jean_missionary_pussy_closed"

    missionary_pussy_sex_animation0

image Jean_missionary_pussy_sex_animation1:
    "Jean_missionary_pussy_agape"

    missionary_pussy_sex_animation1

image Jean_missionary_pussy_sex_animation2:
    "Jean_missionary_pussy_agape"

    missionary_pussy_sex_animation2

image Jean_missionary_anus_anal_animation0:
    "Jean_missionary_anus_closed"

    missionary_anus_anal_animation0

image Jean_missionary_anus_anal_animation1:
    "Jean_missionary_anus_agape"

    missionary_anus_anal_animation1

image Jean_missionary_anus_anal_animation2:
    "Jean_missionary_anus_agape"

    missionary_anus_anal_animation2

image Jean_missionary_pussy_grind_pussy_animation0:
    "Jean_missionary_pussy_closed"

    missionary_pussy_grind_pussy_animation0

image Jean_missionary_pussy_grind_pussy_animation2:
    "Jean_missionary_pussy_open"

    missionary_pussy_grind_pussy_animation2

image Jean_missionary_anus_grind_ass_animation0:
    "Jean_missionary_anus_closed"

    missionary_anus_grind_ass_animation0

image Jean_missionary_anus_grind_ass_animation2:
    "Jean_missionary_anus_open"

    missionary_anus_grind_ass_animation2

image Jean_missionary_pussy_dildo_pussy_animation0:
    "Jean_missionary_pussy_closed"

    missionary_pussy_dildo_pussy_animation0

image Jean_missionary_pussy_dildo_pussy_animation1:
    "Jean_missionary_pussy_agape"

    missionary_pussy_dildo_pussy_animation1

image Jean_missionary_anus_dildo_ass_animation0:
    "Jean_missionary_anus_closed"

    missionary_anus_dildo_ass_animation0

image Jean_missionary_anus_dildo_ass_animation1:
    "Jean_missionary_anus_agape"

    missionary_anus_dildo_ass_animation1

image Jean_missionary_right_forearm_self_touch_pussy_animation0:
    "Jean_missionary_right_forearm_self_touch_pussy"

    missionary_right_forearm_self_touch_pussy_animation0

image Jean_missionary_right_forearm_self_touch_pussy_animation1:
    "Jean_missionary_right_forearm_self_touch_pussy"

    missionary_right_forearm_self_touch_pussy_animation1

image Jean_missionary_left_leg_animation0:
    "Jean_missionary_left_leg"

    missionary_left_leg_animation0

image Jean_missionary_left_leg_animation1:
    "Jean_missionary_left_leg"

    missionary_left_leg_animation1

image Jean_missionary_left_leg_animation2:
    "Jean_missionary_left_leg"

    missionary_left_leg_animation2

image Jean_missionary_left_foot_animation0:
    "Jean_missionary_left_foot"

    missionary_left_foot_animation0

image Jean_missionary_left_foot_animation1:
    "Jean_missionary_left_foot"

    missionary_left_foot_animation1

image Jean_missionary_left_foot_animation2:
    "Jean_missionary_left_foot"

    missionary_left_foot_animation2

image Jean_missionary_right_leg_animation0:
    "Jean_missionary_right_leg"

    missionary_right_leg_animation0

image Jean_missionary_right_leg_animation1:
    "Jean_missionary_right_leg"

    missionary_right_leg_animation1

image Jean_missionary_right_leg_animation2:
    "Jean_missionary_right_leg"

    missionary_right_leg_animation2

image Jean_missionary_right_foot_animation0:
    "Jean_missionary_right_foot"

    missionary_right_foot_animation0

image Jean_missionary_right_foot_animation1:
    "Jean_missionary_right_foot"

    missionary_right_foot_animation1

image Jean_missionary_right_foot_animation2:
    "Jean_missionary_right_foot"

    missionary_right_foot_animation2

image Jean_missionary_male_body_sex_animation0:
    "Jean_missionary_male_body"

    missionary_cock_sex_animation0

image Jean_missionary_male_body_sex_animation1:
    "Jean_missionary_male_body"

    missionary_cock_sex_animation1

image Jean_missionary_male_body_sex_animation2:
    "Jean_missionary_male_body"

    missionary_cock_sex_animation2

image Jean_missionary_male_body_anal_animation0:
    "Jean_missionary_male_body"

    missionary_cock_anal_animation0

image Jean_missionary_male_body_anal_animation1:
    "Jean_missionary_male_body"

    missionary_cock_anal_animation1

image Jean_missionary_male_body_anal_animation2:
    "Jean_missionary_male_body"

    missionary_cock_anal_animation2

image Jean_missionary_male_body_grind_pussy_animation0:
    "Jean_missionary_male_body"

    missionary_cock_grind_pussy_animation0

image Jean_missionary_male_body_grind_pussy_animation2:
    "Jean_missionary_male_body"

    missionary_cock_grind_pussy_animation2

image Jean_missionary_male_body_grind_ass_animation0:
    "Jean_missionary_male_body"

    missionary_cock_grind_ass_animation0

image Jean_missionary_male_body_grind_ass_animation2:
    "Jean_missionary_male_body"

    missionary_cock_grind_ass_animation2

image Jean_missionary_cock_sex_animation0:
    "Jean_missionary_cock"

    missionary_cock_sex_animation0

image Jean_missionary_cock_sex_animation1:
    "Jean_missionary_cock"

    missionary_cock_sex_animation1

image Jean_missionary_cock_sex_animation2:
    "Jean_missionary_cock"

    missionary_cock_sex_animation2

image Jean_missionary_cock_anal_animation0:
    "Jean_missionary_cock"

    missionary_cock_anal_animation0

image Jean_missionary_cock_anal_animation1:
    "Jean_missionary_cock"

    missionary_cock_anal_animation1

image Jean_missionary_cock_anal_animation2:
    "Jean_missionary_cock"

    missionary_cock_anal_animation2

image Jean_missionary_cock_grind_pussy_animation0:
    "Jean_missionary_cock"

    missionary_cock_grind_pussy_animation0

image Jean_missionary_cock_grind_pussy_animation2:
    "Jean_missionary_cock"

    missionary_cock_grind_pussy_animation2

image Jean_missionary_cock_grind_ass_animation0:
    "Jean_missionary_cock"

    missionary_cock_grind_ass_animation0

image Jean_missionary_cock_grind_ass_animation2:
    "Jean_missionary_cock"

    missionary_cock_grind_ass_animation2

image Jean_missionary_spunk_tip_sex_animation0:
    "Jean_missionary_spunk_tip"

    missionary_cock_sex_animation0

image Jean_missionary_spunk_tip_sex_animation1:
    "Jean_missionary_spunk_tip"

    missionary_cock_sex_animation1

image Jean_missionary_spunk_tip_sex_animation2:
    "Jean_missionary_spunk_tip"

    missionary_cock_sex_animation2

image Jean_missionary_spunk_tip_anal_animation0:
    "Jean_missionary_spunk_tip"

    missionary_cock_anal_animation0

image Jean_missionary_spunk_tip_anal_animation1:
    "Jean_missionary_spunk_tip"

    missionary_cock_anal_animation1

image Jean_missionary_spunk_tip_anal_animation2:
    "Jean_missionary_spunk_tip"

    missionary_cock_anal_animation2

image Jean_missionary_spunk_tip_grind_pussy_animation0:
    "Jean_missionary_spunk_tip"

    missionary_cock_grind_pussy_animation0

image Jean_missionary_spunk_tip_grind_pussy_animation2:
    "Jean_missionary_spunk_tip"

    missionary_cock_grind_pussy_animation2

image Jean_missionary_spunk_tip_grind_ass_animation0:
    "Jean_missionary_spunk_tip"

    missionary_cock_grind_ass_animation0

image Jean_missionary_spunk_tip_grind_ass_animation2:
    "Jean_missionary_spunk_tip"

    missionary_cock_grind_ass_animation2

image Jean_missionary_male_knees_sex_animation0:
    "Jean_missionary_male_knees"

    missionary_cock_sex_animation0

image Jean_missionary_male_knees_sex_animation1:
    "Jean_missionary_male_knees"

    missionary_cock_sex_animation1

image Jean_missionary_male_knees_sex_animation2:
    "Jean_missionary_male_knees"

    missionary_cock_sex_animation2

image Jean_missionary_male_knees_anal_animation0:
    "Jean_missionary_male_knees"

    missionary_cock_anal_animation0

image Jean_missionary_male_knees_anal_animation1:
    "Jean_missionary_male_knees"

    missionary_cock_anal_animation1

image Jean_missionary_male_knees_anal_animation2:
    "Jean_missionary_male_knees"

    missionary_cock_anal_animation2

image Jean_missionary_male_knees_grind_pussy_animation0:
    "Jean_missionary_male_knees"

    missionary_cock_grind_pussy_animation0

image Jean_missionary_male_knees_grind_pussy_animation2:
    "Jean_missionary_male_knees"

    missionary_cock_grind_pussy_animation2

image Jean_missionary_male_knees_grind_ass_animation0:
    "Jean_missionary_male_knees"

    missionary_cock_grind_ass_animation0

image Jean_missionary_male_knees_grind_ass_animation2:
    "Jean_missionary_male_knees"

    missionary_cock_grind_ass_animation2

image Jean_missionary_male_left_arm_choke_animation0:
    "Jean_missionary_male_left_arm_fondle"

    missionary_male_left_arm_choke_animation0

image Jean_missionary_male_left_arm_choke_animation1:
    "Jean_missionary_male_left_arm_fondle"

    missionary_male_left_arm_choke_animation1

image Jean_missionary_male_left_arm_touch_left_breast_animation0:
    "Jean_missionary_male_left_arm_fondle"

    missionary_male_left_arm_touch_left_breast_animation0

image Jean_missionary_male_left_arm_touch_left_breast_animation1:
    "Jean_missionary_male_left_arm_fondle"
    
    missionary_male_left_arm_touch_left_breast_animation1

image Jean_missionary_male_left_arm_touch_right_breast_animation0:
    "Jean_missionary_male_left_arm_fondle"

    missionary_male_left_arm_touch_right_breast_animation0

image Jean_missionary_male_left_arm_touch_right_breast_animation1:
    "Jean_missionary_male_left_arm_fondle"

    missionary_male_left_arm_touch_right_breast_animation1

image Jean_missionary_male_left_arm_finger_pussy_animation0:
    "Jean_missionary_male_left_arm_finger"

    missionary_male_left_arm_finger_pussy_animation0

image Jean_missionary_male_left_arm_finger_pussy_animation1:
    "Jean_missionary_male_left_arm_finger"

    missionary_male_left_arm_finger_pussy_animation1

image Jean_missionary_male_left_arm_finger_ass_animation0:
    "Jean_missionary_male_left_arm_finger"

    missionary_male_left_arm_finger_ass_animation0

image Jean_missionary_male_left_arm_finger_ass_animation1:
    "Jean_missionary_male_left_arm_finger"

    missionary_male_left_arm_finger_ass_animation1

image Jean_missionary_male_right_arm_choke_animation0:
    "Jean_missionary_male_right_arm_fondle"

    missionary_male_right_arm_choke_animation0

image Jean_missionary_male_right_arm_choke_animation1:
    "Jean_missionary_male_right_arm_fondle"

    missionary_male_right_arm_choke_animation1

image Jean_missionary_male_right_arm_touch_left_breast_animation0:
    "Jean_missionary_male_right_arm_fondle"

    missionary_male_right_arm_touch_left_breast_animation0

image Jean_missionary_male_right_arm_touch_left_breast_animation1:
    "Jean_missionary_male_right_arm_fondle"

    missionary_male_right_arm_touch_left_breast_animation1

image Jean_missionary_male_right_arm_touch_right_breast_animation0:
    "Jean_missionary_male_right_arm_fondle"

    missionary_male_right_arm_touch_right_breast_animation0

image Jean_missionary_male_right_arm_touch_right_breast_animation1:
    "Jean_missionary_male_right_arm_fondle"

    missionary_male_right_arm_touch_right_breast_animation1

image Jean_missionary_male_right_arm_finger_pussy_animation0:
    "Jean_missionary_male_right_arm_finger"

    missionary_male_right_arm_finger_pussy_animation0

image Jean_missionary_male_right_arm_finger_pussy_animation1:
    "Jean_missionary_male_right_arm_finger"

    missionary_male_right_arm_finger_pussy_animation1

image Jean_missionary_male_right_arm_finger_ass_animation0:
    "Jean_missionary_male_right_arm_finger"

    missionary_male_right_arm_finger_ass_animation0

image Jean_missionary_male_right_arm_finger_ass_animation1:
    "Jean_missionary_male_right_arm_finger"

    missionary_male_right_arm_finger_ass_animation1

image Jean_missionary_dildo_pussy_animation0:
    "Jean_missionary_dildo"

    missionary_dildo_pussy_animation0

image Jean_missionary_dildo_pussy_animation1:
    "Jean_missionary_dildo"

    missionary_dildo_pussy_animation1
    
image Jean_missionary_dildo_ass_animation0:
    "Jean_missionary_dildo"

    missionary_dildo_ass_animation0
    
image Jean_missionary_dildo_ass_animation1:
    "Jean_missionary_dildo"

    missionary_dildo_ass_animation1

image Jean_missionary_vibrator_animation0:
    "Jean_missionary_vibrator"

    missionary_vibrator_animation0

image Jean_missionary_vibrator_animation1:
    "Jean_missionary_vibrator"

    missionary_vibrator_animation1

image Jean_missionary_mask_finger_pussy_animation0:
    "Jean_missionary_mask_pussy"

    missionary_mask_finger_pussy_animation0

image Jean_missionary_mask_finger_pussy_animation1:
    "Jean_missionary_mask_pussy"

    missionary_mask_finger_pussy_animation1

image Jean_missionary_mask_finger_ass_animation0:
    "Jean_missionary_mask_anus"

    missionary_mask_finger_ass_animation0

image Jean_missionary_mask_finger_ass_animation1:
    "Jean_missionary_mask_anus"

    missionary_mask_finger_ass_animation1

image Jean_missionary_mask_sex_animation0:
    "Jean_missionary_mask_pussy"

    missionary_mask_sex_animation0

image Jean_missionary_mask_sex_animation1:
    "Jean_missionary_mask_pussy"

    missionary_mask_sex_animation1

image Jean_missionary_mask_sex_animation2:
    "Jean_missionary_mask_pussy"

    missionary_mask_sex_animation2

image Jean_missionary_mask_anal_animation0:
    "Jean_missionary_mask_anus"

    missionary_mask_anal_animation0

image Jean_missionary_mask_anal_animation1:
    "Jean_missionary_mask_anus"

    missionary_mask_anal_animation1

image Jean_missionary_mask_anal_animation2:
    "Jean_missionary_mask_anus"

    missionary_mask_anal_animation2

image Jean_missionary_mask_dildo_pussy_animation0:
    "Jean_missionary_mask_pussy"

    missionary_mask_dildo_pussy_animation0

image Jean_missionary_mask_dildo_pussy_animation1:
    "Jean_missionary_mask_pussy"

    missionary_mask_dildo_pussy_animation1

image Jean_missionary_mask_dildo_ass_animation0:
    "Jean_missionary_mask_anus"

    missionary_mask_dildo_ass_animation0

image Jean_missionary_mask_dildo_ass_animation1:
    "Jean_missionary_mask_anus"

    missionary_mask_dildo_ass_animation1
    
image Jean_missionary_male_head_suck_left_nipple_animation0:
    "Jean_missionary_male_head"

    missionary_male_head_suck_left_nipple_animation0
    
image Jean_missionary_male_head_suck_left_nipple_animation1:
    "Jean_missionary_male_head"

    missionary_male_head_suck_left_nipple_animation1
    
image Jean_missionary_male_head_suck_right_nipple_animation0:
    "Jean_missionary_male_head"

    missionary_male_head_suck_right_nipple_animation0
    
image Jean_missionary_male_head_suck_right_nipple_animation1:
    "Jean_missionary_male_head"

    missionary_male_head_suck_right_nipple_animation1
    
image Jean_missionary_male_head_eat_pussy_animation0:
    "Jean_missionary_male_head"

    missionary_male_head_eat_pussy_animation0
    
image Jean_missionary_male_head_eat_pussy_animation1:
    "Jean_missionary_male_head"

    missionary_male_head_eat_pussy_animation1
    
image Jean_missionary_male_head_eat_ass_animation0:
    "Jean_missionary_male_head"

    missionary_male_head_eat_ass_animation0
    
image Jean_missionary_male_head_eat_ass_animation1:
    "Jean_missionary_male_head"

    missionary_male_head_eat_ass_animation1
    
image Jean_missionary_male_tongue_animation0:
    "Jean_missionary_male_tongue"

    missionary_male_tongue_animation0
    
image Jean_missionary_male_tongue_animation1:
    "Jean_missionary_male_tongue"

    missionary_male_tongue_animation1

image Jean_missionary_male_body_cumshot_animation:
    "Jean_missionary_male_body"

    missionary_cock_cumshot_animation

image Jean_missionary_male_body_creampie_animation:
    "Jean_missionary_male_body"

    missionary_cock_creampie_animation

image Jean_missionary_male_body_anal_creampie_animation:
    "Jean_missionary_male_body"

    missionary_cock_anal_creampie_animation

image Jean_missionary_cock_cumshot_animation:
    "Jean_missionary_cock"

    missionary_cock_cumshot_animation

image Jean_missionary_cock_creampie_animation:
    "Jean_missionary_cock"

    missionary_cock_creampie_animation

image Jean_missionary_cock_anal_creampie_animation:
    "Jean_missionary_cock"

    missionary_cock_anal_creampie_animation

image Jean_missionary_spunk_tip_cumshot_animation:
    "Jean_missionary_spunk_tip"

    missionary_cock_cumshot_animation

image Jean_missionary_spunk_tip_creampie_animation:
    "Jean_missionary_spunk_tip"

    missionary_cock_creampie_animation

image Jean_missionary_spunk_tip_anal_creampie_animation:
    "Jean_missionary_spunk_tip"

    missionary_cock_anal_creampie_animation

image Jean_missionary_male_knees_cumshot_animation:
    "Jean_missionary_male_knees"

    missionary_cock_cumshot_animation

image Jean_missionary_male_knees_creampie_animation:
    "Jean_missionary_male_knees"

    missionary_cock_creampie_animation

image Jean_missionary_male_knees_anal_creampie_animation:
    "Jean_missionary_male_knees"

    missionary_cock_anal_creampie_animation

image Jean_missionary_pussy_creampie_animation:
    "Jean_missionary_pussy_agape"

    missionary_pussy_creampie_animation

image Jean_missionary_anus_anal_creampie_animation:
    "Jean_missionary_anus_agape"

    missionary_anus_anal_creampie_animation

image Jean_missionary_mask_creampie_animation:
    "Jean_missionary_mask_pussy"

    missionary_mask_creampie_animation

image Jean_missionary_mask_anal_creampie_animation:
    "Jean_missionary_mask_anus"

    missionary_mask_anal_creampie_animation

layeredimage Jean_missionary_cock_animations:
    if Player.orgasming and focused_Character == Jean:
        "Jean_missionary_cock_[Player.orgasming]_animation"
    else:
        "Jean_missionary_cock_[Player.cock_Actions[0].animation_type]_animation[Player.cock_Actions[0].mode]"

    if not Player.check_traits("spunk") and not Player.orgasming:
        Null()
    elif Player.orgasming and focused_Character == Jean:
        "Jean_missionary_spunk_tip_[Player.orgasming]_animation"
    else:
        "Jean_missionary_spunk_tip_[Player.cock_Actions[0].animation_type]_animation[Player.cock_Actions[0].mode]"

layeredimage Jean_missionary_male_left_arm_finger_animations:
    always:
        "Jean_missionary_male_left_arm_[Player.left_hand_Actions[0].animation_type]_animation[Player.left_hand_Actions[0].mode]"

layeredimage Jean_missionary_male_right_arm_finger_animations:
    always:
        "Jean_missionary_male_right_arm_[Player.right_hand_Actions[0].animation_type]_animation[Player.right_hand_Actions[0].mode]"

layeredimage Jean_missionary_dildo_pussy_animations:
    always:
        "Jean_missionary_dildo_pussy_animation[Jean.vagina_Actions[0].mode]"

layeredimage Jean_missionary_dildo_ass_animations:
    always:
        "Jean_missionary_dildo_ass_animation[Jean.anus_Actions[0].mode]"

layeredimage Jean_missionary_mask_anus_animations:
    if Player.orgasming == "anal_creampie" and focused_Character == Jean:
        "Jean_missionary_mask_anal_creampie_animation"
    elif Jean.anus_Actions[0].animation_type in ["dildo_ass", "self_dildo_ass"]:
        "Jean_missionary_mask_dildo_ass_animation[Jean.anus_Actions[0].mode]"
    else:
        "Jean_missionary_mask_[Jean.anus_Actions[0].animation_type]_animation[Jean.anus_Actions[0].mode]"

layeredimage Jean_missionary_mask_pussy_animations:
    if Player.orgasming == "creampie" and focused_Character == Jean:
        "Jean_missionary_mask_creampie_animation"
    elif Jean.vagina_Actions[0].animation_type in ["dildo_pussy", "self_dildo_pussy"]:
        "Jean_missionary_mask_dildo_pussy_animation[Jean.vagina_Actions[0].mode]"
    else:
        "Jean_missionary_mask_[Jean.vagina_Actions[0].animation_type]_animation[Jean.vagina_Actions[0].mode]"
    
image Jean_missionary_blinking:
    "characters/Jean/images/missionary/eyes_[Jean.eyes].webp"
    choice:
        4.5
    choice:
        4.0
    choice:
        3.5
    "characters/Jean/images/missionary/eyes_blink1.webp"
    0.023
    "characters/Jean/images/missionary/eyes_blink2.webp"
    0.023
    "characters/Jean/images/missionary/eyes_closed.webp"
    0.054
    "characters/Jean/images/missionary/eyes_blink2.webp"
    0.018
    "characters/Jean/images/missionary/eyes_blink1.webp"
    0.072
    repeat

image Jean_missionary_cumshot:
    "characters/Jean/images/missionary/spunk_jet.webp"

    anchor (int(2040*sex_sampling), int(2390*sex_sampling))
    offset (int(2040*sex_sampling), int(2390*sex_sampling))

    subpixel True
    transform_anchor True

    block:
        yzoom 0.0 alpha 1.0
        easein_cubic 0.2 yzoom 1.0 alpha 0.5
        linear 0.1 alpha 0.0
        pause 1.0

        repeat

image Jean_missionary_creampie:
    "characters/Jean/images/missionary/creampie_pussy_agape.webp"

    anchor (int(2003*sex_sampling), int(2877*sex_sampling))
    offset (int(2003*sex_sampling), int(2877*sex_sampling))

    subpixel True
    transform_anchor True

    block:
        xzoom 0.0 alpha 1.0
        easein_cubic 0.2 xzoom 1.5 alpha 0.5
        linear 0.1 alpha 0.0
        pause 1.0

        repeat

image Jean_missionary_anal_creampie:
    "characters/Jean/images/missionary/creampie_anus_agape.webp"

    anchor (int(2016*sex_sampling), int(2977*sex_sampling))
    offset (int(2016*sex_sampling), int(2977*sex_sampling))

    subpixel True
    transform_anchor True

    block:
        xzoom 0.0 alpha 1.0
        easein_cubic 0.2 xzoom 1.5 alpha 0.5
        linear 0.1 alpha 0.0
        pause 1.0

        repeat