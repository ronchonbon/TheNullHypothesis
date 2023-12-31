image Rogue_sprite masturbation:
    contains:
        "Rogue_masturbation_temp"

    offset (int(150*0.38), int(350*0.38))
            
layeredimage Rogue_masturbation_temp:
    if Rogue.hovered:
        At("Rogue_masturbation_controls_temp", hover)
    else:
        "Rogue_masturbation_controls_temp"
            
layeredimage Rogue_masturbation_controls_temp:
    if speed > 2.5 or speed <= 1.75:
        Null()
    elif intensity >= 2.0:
        At(At("Rogue_masturbation", speed_200), intensity_200)
    elif intensity >= 1.75:
        At(At("Rogue_masturbation", speed_200), intensity_175)
    elif intensity >= 1.5:
        At(At("Rogue_masturbation", speed_200), intensity_150)
    elif intensity >= 1.25:
        At(At("Rogue_masturbation", speed_200), intensity_125)
    elif intensity >= 1.0:
        At(At("Rogue_masturbation", speed_200), intensity_100)
    elif intensity >= 0.75:
        At(At("Rogue_masturbation", speed_200), intensity_075)
    elif intensity >= 0.5:
        At(At("Rogue_masturbation", speed_200), intensity_050)
    elif intensity >= 0.25:
        At(At("Rogue_masturbation", speed_200), intensity_025)
    else:
        At(At("Rogue_masturbation", speed_200), intensity_000)

    if speed > 1.75 or speed <= 1.5:
        Null()
    elif intensity >= 2.0:
        At(At("Rogue_masturbation", speed_175), intensity_200)
    elif intensity >= 1.75:
        At(At("Rogue_masturbation", speed_175), intensity_175)
    elif intensity >= 1.5:
        At(At("Rogue_masturbation", speed_175), intensity_150)
    elif intensity >= 1.25:
        At(At("Rogue_masturbation", speed_175), intensity_125)
    elif intensity >= 1.0:
        At(At("Rogue_masturbation", speed_175), intensity_100)
    elif intensity >= 0.75:
        At(At("Rogue_masturbation", speed_175), intensity_075)
    elif intensity >= 0.5:
        At(At("Rogue_masturbation", speed_175), intensity_050)
    elif intensity >= 0.25:
        At(At("Rogue_masturbation", speed_175), intensity_025)
    else:
        At(At("Rogue_masturbation", speed_175), intensity_000)

    if speed > 1.5 or speed <= 1.25:
        Null()
    elif intensity >= 2.0:
        At(At("Rogue_masturbation", speed_150), intensity_200)
    elif intensity >= 1.75:
        At(At("Rogue_masturbation", speed_150), intensity_175)
    elif intensity >= 1.5:
        At(At("Rogue_masturbation", speed_150), intensity_150)
    elif intensity >= 1.25:
        At(At("Rogue_masturbation", speed_150), intensity_125)
    elif intensity >= 1.0:
        At(At("Rogue_masturbation", speed_150), intensity_100)
    elif intensity >= 0.75:
        At(At("Rogue_masturbation", speed_150), intensity_075)
    elif intensity >= 0.5:
        At(At("Rogue_masturbation", speed_150), intensity_050)
    elif intensity >= 0.25:
        At(At("Rogue_masturbation", speed_150), intensity_025)
    else:
        At(At("Rogue_masturbation", speed_150), intensity_000)
 
    if speed > 1.25 or speed <= 1.0:
        Null()
    elif intensity >= 2.0:
        At(At("Rogue_masturbation", speed_125), intensity_200)
    elif intensity >= 1.75:
        At(At("Rogue_masturbation", speed_125), intensity_175)
    elif intensity >= 1.5:
        At(At("Rogue_masturbation", speed_125), intensity_150)
    elif intensity >= 1.25:
        At(At("Rogue_masturbation", speed_125), intensity_125)
    elif intensity >= 1.0:
        At(At("Rogue_masturbation", speed_125), intensity_100)
    elif intensity >= 0.75:
        At(At("Rogue_masturbation", speed_125), intensity_075)
    elif intensity >= 0.5:
        At(At("Rogue_masturbation", speed_125), intensity_050)
    elif intensity >= 0.25:
        At(At("Rogue_masturbation", speed_125), intensity_025)
    else:
        At(At("Rogue_masturbation", speed_125), intensity_000)
 
    if speed > 1.0 or speed <= 0.75:
        Null()
    elif intensity >= 2.0:
        At(At("Rogue_masturbation", speed_100), intensity_200)
    elif intensity >= 1.75:
        At(At("Rogue_masturbation", speed_100), intensity_175)
    elif intensity >= 1.5:
        At(At("Rogue_masturbation", speed_100), intensity_150)
    elif intensity >= 1.25:
        At(At("Rogue_masturbation", speed_100), intensity_125)
    elif intensity >= 1.0:
        At(At("Rogue_masturbation", speed_100), intensity_100)
    elif intensity >= 0.75:
        At(At("Rogue_masturbation", speed_100), intensity_075)
    elif intensity >= 0.5:
        At(At("Rogue_masturbation", speed_100), intensity_050)
    elif intensity >= 0.25:
        At(At("Rogue_masturbation", speed_100), intensity_025)
    else:
        At(At("Rogue_masturbation", speed_100), intensity_000)

    if speed > 0.75 or speed <= 0.5:
        Null()
    elif intensity >= 2.0:
        At(At("Rogue_masturbation", speed_075), intensity_200)
    elif intensity >= 1.75:
        At(At("Rogue_masturbation", speed_075), intensity_175)
    elif intensity >= 1.5:
        At(At("Rogue_masturbation", speed_075), intensity_150)
    elif intensity >= 1.25:
        At(At("Rogue_masturbation", speed_075), intensity_125)
    elif intensity >= 1.0:
        At(At("Rogue_masturbation", speed_075), intensity_100)
    elif intensity >= 0.75:
        At(At("Rogue_masturbation", speed_075), intensity_075)
    elif intensity >= 0.5:
        At(At("Rogue_masturbation", speed_075), intensity_050)
    elif intensity >= 0.25:
        At(At("Rogue_masturbation", speed_075), intensity_025)
    else:
        At(At("Rogue_masturbation", speed_075), intensity_000)

    if speed > 0.5 or speed <= 0.25:
        Null()
    elif intensity >= 2.0:
        At(At("Rogue_masturbation", speed_050), intensity_200)
    elif intensity >= 1.75:
        At(At("Rogue_masturbation", speed_050), intensity_175)
    elif intensity >= 1.5:
        At(At("Rogue_masturbation", speed_050), intensity_150)
    elif intensity >= 1.25:
        At(At("Rogue_masturbation", speed_050), intensity_125)
    elif intensity >= 1.0:
        At(At("Rogue_masturbation", speed_050), intensity_100)
    elif intensity >= 0.75:
        At(At("Rogue_masturbation", speed_050), intensity_075)
    elif intensity >= 0.5:
        At(At("Rogue_masturbation", speed_050), intensity_050)
    elif intensity >= 0.25:
        At(At("Rogue_masturbation", speed_050), intensity_025)
    else:
        At(At("Rogue_masturbation", speed_050), intensity_000)

    if speed > 0.25 or speed <= 0.01:
        Null()
    elif intensity >= 2.0:
        At(At("Rogue_masturbation", speed_025), intensity_200)
    elif intensity >= 1.75:
        At(At("Rogue_masturbation", speed_025), intensity_175)
    elif intensity >= 1.5:
        At(At("Rogue_masturbation", speed_025), intensity_150)
    elif intensity >= 1.25:
        At(At("Rogue_masturbation", speed_025), intensity_125)
    elif intensity >= 1.0:
        At(At("Rogue_masturbation", speed_025), intensity_100)
    elif intensity >= 0.75:
        At(At("Rogue_masturbation", speed_025), intensity_075)
    elif intensity >= 0.5:
        At(At("Rogue_masturbation", speed_025), intensity_050)
    elif intensity >= 0.25:
        At(At("Rogue_masturbation", speed_025), intensity_025)
    else:
        At(At("Rogue_masturbation", speed_025), intensity_000)

    if speed != 0.01:
        Null()
    elif intensity >= 2.0:
        At(At("Rogue_masturbation", speed_0001), intensity_200)
    elif intensity >= 1.75:
        At(At("Rogue_masturbation", speed_0001), intensity_175)
    elif intensity >= 1.5:
        At(At("Rogue_masturbation", speed_0001), intensity_150)
    elif intensity >= 1.25:
        At(At("Rogue_masturbation", speed_0001), intensity_125)
    elif intensity >= 1.0:
        At(At("Rogue_masturbation", speed_0001), intensity_100)
    elif intensity >= 0.75:
        At(At("Rogue_masturbation", speed_0001), intensity_075)
    elif intensity >= 0.5:
        At(At("Rogue_masturbation", speed_0001), intensity_050)
    elif intensity >= 0.25:
        At(At("Rogue_masturbation", speed_0001), intensity_025)
    else:
        At(At("Rogue_masturbation", speed_0001), intensity_000)

    if speed >= 0.01 or speed < 0.0:
        Null()
    elif intensity >= 2.0:
        At(At("Rogue_masturbation", speed_000), intensity_200)
    elif intensity >= 1.75:
        At(At("Rogue_masturbation", speed_000), intensity_175)
    elif intensity >= 1.5:
        At(At("Rogue_masturbation", speed_000), intensity_150)
    elif intensity >= 1.25:
        At(At("Rogue_masturbation", speed_000), intensity_125)
    elif intensity >= 1.0:
        At(At("Rogue_masturbation", speed_000), intensity_100)
    elif intensity >= 0.75:
        At(At("Rogue_masturbation", speed_000), intensity_075)
    elif intensity >= 0.5:
        At(At("Rogue_masturbation", speed_000), intensity_050)
    elif intensity >= 0.25:
        At(At("Rogue_masturbation", speed_000), intensity_025)
    else:
        At(At("Rogue_masturbation", speed_000), intensity_000)

layeredimage Rogue_masturbation:
    if Rogue.vagina_Actions:
        "Rogue_masturbation_thighs_animation[Rogue.vagina_Actions[0].mode]"
    elif Rogue.anus_Actions:
        "Rogue_masturbation_thighs_animation[Rogue.anus_Actions[0].mode]"
    else:
        "Rogue_masturbation_thighs_animation0"
    
layeredimage Rogue_masturbation_torso:
    if Rogue.vagina_Actions:
        "Rogue_masturbation_hair_back_animation[Rogue.vagina_Actions[0].mode]"
    elif Rogue.anus_Actions:
        "Rogue_masturbation_hair_back_animation[Rogue.anus_Actions[0].mode]"
    else:
        "Rogue_masturbation_hair_back_animation0"
            
    always:
        "characters/Rogue/images/masturbation/torso.webp"

    if Rogue.piercings["belly"]:
        "characters/Rogue/images/masturbation/belly_piercing.webp"

    if Rogue.spunk["belly"]:
        "characters/Rogue/images/masturbation/spunk_belly.webp"

    if Rogue.vagina_Actions:
        "Rogue_masturbation_left_arm_animation[Rogue.vagina_Actions[0].mode]"
    elif Rogue.anus_Actions:
        "Rogue_masturbation_left_arm_animation[Rogue.anus_Actions[0].mode]"
    else:
        "Rogue_masturbation_left_arm_animation0"

    if Rogue.vagina_Actions:
        "Rogue_masturbation_breasts_animation[Rogue.vagina_Actions[0].mode]"
    elif Rogue.anus_Actions:
        "Rogue_masturbation_breasts_animation[Rogue.anus_Actions[0].mode]"
    else:
        "Rogue_masturbation_breasts_animation0"

    if not Player.left_hand_Actions or Rogue not in Player.left_hand_Actions[0].Targets:
        Null()
    elif Player.left_hand_Actions[0].animation_type == "choke":
        At("Rogue_masturbation_male_left_arm_choke_animation[Player.left_hand_Actions[0].mode]", change_offset(Rogue_masturbation_neck_position[0], Rogue_masturbation_neck_position[1]))

    if not Player.right_hand_Actions or Rogue not in Player.right_hand_Actions[0].Targets:
        Null()
    elif Player.right_hand_Actions[0].animation_type == "choke":
        At("Rogue_masturbation_male_right_arm_choke_animation[Player.right_hand_Actions[0].mode]", change_offset(Rogue_masturbation_neck_position[0], Rogue_masturbation_neck_position[1]))

    if Rogue.vagina_Actions:
        "Rogue_masturbation_head_animation[Rogue.vagina_Actions[0].mode]"
    elif Rogue.anus_Actions:
        "Rogue_masturbation_head_animation[Rogue.anus_Actions[0].mode]"
    else:
        "Rogue_masturbation_head_animation0"

    if Rogue.right_hand_Actions and Rogue.right_hand_Actions[0].animation_type == "self_touch_pussy":
        "Rogue_masturbation_right_forearm_animation[Rogue.right_hand_Actions[0].mode]"

    anchor (int(2576*sex_sampling), int(2541*sex_sampling))
    offset (int(2576*sex_sampling), int(2541*sex_sampling))
    
image Rogue_masturbation_hair_back:
    "characters/Rogue/images/masturbation/hair_back.webp"

    anchor (int(2787*sex_sampling), int(1333*sex_sampling))
    offset (int(2787*sex_sampling), int(1333*sex_sampling))
    
layeredimage Rogue_masturbation_left_arm:
    always:
        "characters/Rogue/images/masturbation/left_arm.webp"

    anchor (int(3344*sex_sampling), int(1534*sex_sampling))
    offset (int(3344*sex_sampling), int(1534*sex_sampling))
    
layeredimage Rogue_masturbation_breasts:
    always:
        "characters/Rogue/images/masturbation/breasts.webp"

    if Rogue.tan_lines["top"]:
        "characters/Rogue/images/masturbation/tan_lines_[Rogue.tan_lines[top]].webp"

    if Rogue.tan_lines["full"]:
        "characters/Rogue/images/masturbation/tan_lines_[Rogue.tan_lines[full]]_torso.webp"

    if Rogue.piercings["nipple"] in ["barbell", "both"]:
        "characters/Rogue/images/masturbation/nipple_piercings_barbell.webp"

    if Rogue.piercings["nipple"] in ["ring", "both"]:
        "characters/Rogue/images/masturbation/nipple_piercings_ring.webp"

    if Rogue.spunk["breasts"]:
        "characters/Rogue/images/masturbation/spunk_breasts.webp"

    anchor (int(2576*sex_sampling), int(2541*sex_sampling))
    offset (int(2576*sex_sampling), int(2541*sex_sampling))
    
layeredimage Rogue_masturbation_head:
    always:
        "characters/Rogue/images/masturbation/head_[Rogue.mouth].webp"

    if Rogue.eyes in ["closed", "down", "left", "right", "squint", "up"]:
        "characters/Rogue/images/masturbation/eyes_[Rogue.eyes].webp"
    else:
        "Rogue_masturbation_blinking"

    always:
        "characters/Rogue/images/masturbation/brows_[Rogue.brows].webp"

    if Rogue.blush:
            "characters/Rogue/images/masturbation/blush[Rogue.blush].webp"
        
    if Rogue.spunk["tongue"] and Rogue.mouth in ["agape", "tongue"]:
        "characters/Rogue/images/masturbation/spunk_tongue.webp"

    if Rogue.spunk["mouth"] and Rogue.mouth in ["agape", "tongue"]:
        "characters/Rogue/images/masturbation/spunk_mouth.webp"
        
    if Rogue.spunk["chin"]:
        "characters/Rogue/images/masturbation/spunk_chin.webp"
        
    if Rogue.spunk["face"]:
        "characters/Rogue/images/masturbation/spunk_face.webp"

    if Rogue.vagina_Actions:
        "Rogue_masturbation_hair_animation[Rogue.vagina_Actions[0].mode]"
    elif Rogue.anus_Actions:
        "Rogue_masturbation_hair_animation[Rogue.anus_Actions[0].mode]"
    else:
        "Rogue_masturbation_hair_animation0"

    anchor (int(2787*sex_sampling), int(1333*sex_sampling))
    offset (int(2787*sex_sampling), int(1333*sex_sampling))
    
layeredimage Rogue_masturbation_hair:
    if Rogue.wet or Rogue.Clothes["hair"].string == "wet":
        "characters/Rogue/images/masturbation/hair_wet.webp"
    elif Rogue.Clothes["hair"].string in ["messy", "ponytail"]:
        "characters/Rogue/images/masturbation/hair_asymmetric.webp"
    else:
        "characters/Rogue/images/masturbation/hair_[Rogue.Clothes[hair].string].webp"

    if Rogue.spunk["hair"]:
        "characters/Rogue/images/masturbation/spunk_hair.webp"

    anchor (int(2787*sex_sampling), int(1333*sex_sampling))
    offset (int(2787*sex_sampling), int(1333*sex_sampling))

image Rogue_masturbation_right_forearm:
    "characters/Rogue/images/masturbation/right_forearm.webp"

    anchor (int(2091*sex_sampling), int(2343*sex_sampling))
    offset (int(2091*sex_sampling), int(2343*sex_sampling))
    
layeredimage Rogue_masturbation_thighs:
    if Rogue.vagina_Actions and Rogue.orgasming:
        At("Rogue_masturbation_torso_animation[Rogue.vagina_Actions[0].mode]", tremble(20))
    if Rogue.vagina_Actions:
        "Rogue_masturbation_torso_animation[Rogue.vagina_Actions[0].mode]"
    elif Rogue.anus_Actions and Rogue.orgasming:
        At("Rogue_masturbation_torso_animation[Rogue.anus_Actions[0].mode]", tremble(20))
    elif Rogue.anus_Actions:
        "Rogue_masturbation_torso_animation[Rogue.anus_Actions[0].mode]"
    elif Rogue.orgasming:
        At("Rogue_masturbation_torso_animation0", tremble(20))
    else:
        "Rogue_masturbation_torso_animation0"

    always:
        "characters/Rogue/images/masturbation/thighs.webp"

    if not Rogue.anus_Actions:
        "Rogue_masturbation_anus_closed"
    elif Rogue.anus_Actions[0].animation_type == "eat_ass":
        "Rogue_masturbation_anus_open"
    elif Rogue.anus_Actions[0].animation_type == "finger_ass" and Player.left_hand_Actions and Player.left_hand_Actions[0].animation_type == "finger_ass":
        "Rogue_masturbation_anus_left_arm_finger_ass_animation[Rogue.anus_Actions[0].mode]"
    elif Rogue.anus_Actions[0].animation_type == "finger_ass" and Player.right_hand_Actions and Player.right_hand_Actions[0].animation_type == "finger_ass":
        "Rogue_masturbation_anus_right_arm_finger_ass_animation[Rogue.anus_Actions[0].mode]"
    elif Rogue.anus_Actions[0].animation_type in ["dildo_ass", "self_dildo_ass"]:
        "Rogue_masturbation_anus_dildo_ass_animation[Rogue.anus_Actions[0].mode]"

    if not Rogue.vagina_Actions:
        "Rogue_masturbation_pussy_closed"
    elif Rogue.vagina_Actions[0].animation_type == "finger_pussy" and Player.left_hand_Actions and Player.left_hand_Actions[0].animation_type == "finger_pussy":
        "Rogue_masturbation_pussy_left_arm_finger_pussy_animation[Rogue.vagina_Actions[0].mode]"
    elif Rogue.vagina_Actions[0].animation_type == "finger_pussy" and Player.right_hand_Actions and Player.right_hand_Actions[0].animation_type == "finger_pussy":
        "Rogue_masturbation_pussy_right_arm_finger_pussy_animation[Rogue.vagina_Actions[0].mode]"
    elif Rogue.vagina_Actions[0].animation_type in ["dildo_pussy", "self_dildo_pussy"]:
        "Rogue_masturbation_pussy_dildo_pussy_animation[Rogue.vagina_Actions[0].mode]"

    if Rogue.tan_lines["bottom"]:
        "characters/Rogue/images/masturbation/tan_lines_[Rogue.tan_lines[bottom]].webp"

    if Rogue.tan_lines["full"]:
        "characters/Rogue/images/masturbation/tan_lines_[Rogue.tan_lines[full]]_thighs.webp"

    if Rogue.creampie["anus"]:
        "characters/Rogue/images/masturbation/creampie_anus.webp"

    if Rogue.creampie["pussy"]:
        "characters/Rogue/images/masturbation/creampie_pussy.webp"

    if not Rogue.buttplug:
        Null()
    elif Rogue.buttplug.string == "heart_anal_plug":
        "characters/Rogue/images/masturbation/buttplug_heart.webp"
    elif Rogue.buttplug.string == "round_anal_plug":
        "characters/Rogue/images/masturbation/buttplug_round.webp"

    if Rogue.piercings["labia"] in ["barbell", "both"]:
        "characters/Rogue/images/masturbation/labia_piercings_barbell.webp"

    if Rogue.piercings["labia"] in ["ring", "both"]:
        "characters/Rogue/images/masturbation/labia_piercings_ring.webp"

    if "pubic" in Rogue.body_hair_growing.keys():
        "characters/Rogue/images/masturbation/pubes_growing.webp"

    if not Rogue.body_hair["pubic"]:
        Null()
    elif "triangle" in Rogue.body_hair["pubic"]:
        "characters/Rogue/images/masturbation/pubes_triangle.webp"
    elif "strip" in Rogue.body_hair["pubic"]:
        "characters/Rogue/images/masturbation/pubes_strip.webp"
    else:
        "characters/Rogue/images/masturbation/pubes_[Rogue.body_hair[pubic]].webp"

    if Rogue.remote_vibrator is not None:
        "characters/Rogue/images/masturbation/remote_vibrator.webp"

    if Rogue.right_hand_Actions and Rogue.right_hand_Actions[0].animation_type == "self_touch_pussy":
        "Rogue_masturbation_right_hand_animation[Rogue.right_hand_Actions[0].mode]"

    if Rogue.vagina_Actions and Rogue.orgasming:
        At("Rogue_masturbation_left_leg_animation[Rogue.vagina_Actions[0].mode]", tremble(20))
    elif Rogue.vagina_Actions:
        "Rogue_masturbation_left_leg_animation[Rogue.vagina_Actions[0].mode]"
    elif Rogue.anus_Actions and Rogue.orgasming:
        At("Rogue_masturbation_left_leg_animation[Rogue.anus_Actions[0].mode]", tremble(20))
    elif Rogue.anus_Actions:
        "Rogue_masturbation_left_leg_animation[Rogue.anus_Actions[0].mode]"
    elif Rogue.orgasming:
        At("Rogue_masturbation_left_leg_animation0", tremble(20))
    else:
        "Rogue_masturbation_left_leg_animation0"

    if Rogue.vagina_Actions and Rogue.orgasming:
        At("Rogue_masturbation_right_leg_animation[Rogue.vagina_Actions[0].mode]", tremble(20))
    elif Rogue.vagina_Actions:
        "Rogue_masturbation_right_leg_animation[Rogue.vagina_Actions[0].mode]"
    elif Rogue.anus_Actions and Rogue.orgasming:
        At("Rogue_masturbation_right_leg_animation[Rogue.anus_Actions[0].mode]", tremble(20))
    elif Rogue.anus_Actions:
        "Rogue_masturbation_right_leg_animation[Rogue.anus_Actions[0].mode]"
    elif Rogue.orgasming:
        At("Rogue_masturbation_right_leg_animation0", tremble(20))
    else:
        "Rogue_masturbation_right_leg_animation0"

    if not Rogue.anus_Actions or Rogue.anus_Actions[0].animation_type != "finger_ass":
        Null()
    elif Player.left_hand_Actions and Rogue in Player.left_hand_Actions[0].Targets and Player.left_hand_Actions[0].animation_type == "finger_ass":
        AlphaMask("Rogue_masturbation_male_left_arm_finger_animations", "Rogue_masturbation_mask_anus_animations")
    elif Player.right_hand_Actions and Rogue in Player.right_hand_Actions[0].Targets and Player.right_hand_Actions[0].animation_type == "finger_ass":
        AlphaMask("Rogue_masturbation_male_right_arm_finger_animations", "Rogue_masturbation_mask_anus_animations")

    if Rogue.anus_Actions and Rogue.anus_Actions[0].animation_type in ["dildo_ass", "self_dildo_ass"]:
        AlphaMask("Rogue_masturbation_dildo_ass_animations", "Rogue_masturbation_mask_anus_animations")

    if not Rogue.vagina_Actions or Rogue.vagina_Actions[0].animation_type != "finger_pussy":
        Null()
    elif Player.left_hand_Actions and Rogue in Player.left_hand_Actions[0].Targets and Player.left_hand_Actions[0].animation_type == "finger_pussy":
        AlphaMask("Rogue_masturbation_male_left_arm_finger_animations", "Rogue_masturbation_mask_pussy_animations")
    elif Player.right_hand_Actions and Rogue in Player.right_hand_Actions[0].Targets and Player.right_hand_Actions[0].animation_type == "finger_pussy":
        AlphaMask("Rogue_masturbation_male_right_arm_finger_animations", "Rogue_masturbation_mask_pussy_animations")

    if Rogue.vagina_Actions and Rogue.vagina_Actions[0].animation_type in ["dildo_pussy", "self_dildo_pussy"]:
        AlphaMask("Rogue_masturbation_dildo_pussy_animations", "Rogue_masturbation_mask_pussy_animations")

    if Rogue.clitoris_Actions and Rogue.clitoris_Actions[0].animation_type in ["vibrator", "self_vibrator"]:
        "Rogue_masturbation_vibrator_animation[Rogue.clitoris_Actions[0].mode]"

    if not Player.left_hand_Actions or Rogue not in Player.left_hand_Actions[0].Targets:
        Null()
    elif Player.left_hand_Actions[0].animation_type == "touch_thighs":
        "Rogue_masturbation_male_left_arm_touch_thighs_animation[Player.left_hand_Actions[0].mode]"
    elif Player.left_hand_Actions[0].animation_type == "touch_thighs_higher":
        "Rogue_masturbation_male_left_arm_touch_thighs_higher_animation[Player.left_hand_Actions[0].mode]"
    elif Player.left_hand_Actions[0].animation_type == "touch_breasts" and Rogue.right_breast_Actions and Player.left_hand_Actions[0].animation_type == Rogue.right_breast_Actions[0].animation_type:
        At("Rogue_masturbation_male_left_arm_touch_right_breast_animation[Player.left_hand_Actions[0].mode]", change_offset(Rogue_masturbation_right_breast_position[0], Rogue_masturbation_right_breast_position[1]))
    elif Player.left_hand_Actions[0].animation_type == "touch_breasts" and Rogue.left_breast_Actions and Player.left_hand_Actions[0].animation_type == Rogue.left_breast_Actions[0].animation_type:
        At("Rogue_masturbation_male_left_arm_touch_left_breast_animation[Player.left_hand_Actions[0].mode]", change_offset(Rogue_masturbation_left_breast_position[0], Rogue_masturbation_left_breast_position[1]))
    elif Player.left_hand_Actions[0].animation_type == "pinch_nipples" and Rogue.right_nipple_Actions and Player.left_hand_Actions[0].animation_type == Rogue.right_nipple_Actions[0].animation_type:
        At("Rogue_masturbation_male_left_arm_touch_right_breast_animation[Player.left_hand_Actions[0].mode]", change_offset(Rogue_masturbation_right_nipple_position[0], Rogue_masturbation_right_nipple_position[1]))
    elif Player.left_hand_Actions[0].animation_type == "pinch_nipples" and Rogue.left_nipple_Actions and Player.left_hand_Actions[0].animation_type == Rogue.left_nipple_Actions[0].animation_type:
        At("Rogue_masturbation_male_left_arm_touch_left_breast_animation[Player.left_hand_Actions[0].mode]", change_offset(Rogue_masturbation_left_nipple_position[0], Rogue_masturbation_left_nipple_position[1]))

    if not Player.right_hand_Actions or Rogue not in Player.right_hand_Actions[0].Targets:
        Null()
    elif Player.right_hand_Actions[0].animation_type == "touch_thighs":
        "Rogue_masturbation_male_right_arm_touch_thighs_animation[Player.right_hand_Actions[0].mode]"
    elif Player.right_hand_Actions[0].animation_type == "touch_thighs_higher":
        "Rogue_masturbation_male_right_arm_touch_thighs_higher_animation[Player.right_hand_Actions[0].mode]"
    elif Player.right_hand_Actions[0].animation_type == "touch_breasts" and Rogue.right_breast_Actions and Player.right_hand_Actions[0].animation_type == Rogue.right_breast_Actions[0].animation_type:
        At("Rogue_masturbation_male_right_arm_touch_right_breast_animation[Player.right_hand_Actions[0].mode]", change_offset(Rogue_masturbation_right_breast_position[0], Rogue_masturbation_right_breast_position[1]))
    elif Player.right_hand_Actions[0].animation_type == "touch_breasts" and Rogue.left_breast_Actions and Player.right_hand_Actions[0].animation_type == Rogue.left_breast_Actions[0].animation_type:
        At("Rogue_masturbation_male_right_arm_touch_left_breast_animation[Player.right_hand_Actions[0].mode]", change_offset(Rogue_masturbation_left_breast_position[0], Rogue_masturbation_left_breast_position[1]))
    elif Player.right_hand_Actions[0].animation_type == "pinch_nipples" and Rogue.right_nipple_Actions and Player.right_hand_Actions[0].animation_type == Rogue.right_nipple_Actions[0].animation_type:
        At("Rogue_masturbation_male_right_arm_touch_right_breast_animation[Player.right_hand_Actions[0].mode]", change_offset(Rogue_masturbation_right_nipple_position[0], Rogue_masturbation_right_nipple_position[1]))
    elif Player.right_hand_Actions[0].animation_type == "pinch_nipples" and Rogue.left_nipple_Actions and Player.right_hand_Actions[0].animation_type == Rogue.left_nipple_Actions[0].animation_type:
        At("Rogue_masturbation_male_right_arm_touch_left_breast_animation[Player.right_hand_Actions[0].mode]", change_offset(Rogue_masturbation_left_nipple_position[0], Rogue_masturbation_left_nipple_position[1]))
    
    if not Player.mouth_Actions or Rogue not in Player.mouth_Actions[0].Targets:
        Null()
    elif Player.mouth_Actions[0].animation_type == "suck_nipples" and Rogue.right_nipple_Actions and Rogue.right_nipple_Actions[0].animation_type == "suck_nipples":
        At("Rogue_masturbation_male_head_suck_right_nipple_animation[Player.mouth_Actions[0].mode]", change_offset(Rogue_masturbation_right_nipple_position[0], Rogue_masturbation_right_nipple_position[1]))
    elif Player.mouth_Actions[0].animation_type == "suck_nipples" and Rogue.left_nipple_Actions and Rogue.left_nipple_Actions[0].animation_type == "suck_nipples":
        At("Rogue_masturbation_male_head_suck_left_nipple_animation[Player.mouth_Actions[0].mode]", change_offset(Rogue_masturbation_left_nipple_position[0], Rogue_masturbation_left_nipple_position[1]))
    elif Player.mouth_Actions[0].animation_type == "eat_pussy":
        At("Rogue_masturbation_male_head_eat_pussy_animation[Player.mouth_Actions[0].mode]", change_offset(Rogue_masturbation_pussy_position[0], Rogue_masturbation_pussy_position[1]))
    elif Player.mouth_Actions[0].animation_type == "eat_ass":
        At("Rogue_masturbation_male_head_eat_ass_animation[Player.mouth_Actions[0].mode]", change_offset(Rogue_masturbation_anus_position[0], Rogue_masturbation_anus_position[1]))

    anchor (int(2576*sex_sampling), int(2541*sex_sampling))
    offset (int(2576*sex_sampling), int(2541*sex_sampling))

image Rogue_masturbation_anus_closed:
    "characters/Rogue/images/masturbation/anus_closed.webp"

    anchor (int(2472*sex_sampling), int(2914*sex_sampling))
    offset (int(2472*sex_sampling), int(2914*sex_sampling))

image Rogue_masturbation_anus_open:
    "characters/Rogue/images/masturbation/anus_open.webp"

    anchor (int(2472*sex_sampling), int(2914*sex_sampling))
    offset (int(2472*sex_sampling), int(2914*sex_sampling))

layeredimage Rogue_masturbation_anus_agape:
    if Rogue.anus_Actions[0].mode > 0:
        "characters/Rogue/images/masturbation/anus_agape.webp"
    else:
        "characters/Rogue/images/masturbation/anus_closed.webp"

    anchor (int(2472*sex_sampling), int(2899*sex_sampling))
    offset (int(2472*sex_sampling), int(2899*sex_sampling))

image Rogue_masturbation_pussy_closed:
    "characters/Rogue/images/masturbation/pussy_closed.webp"

    anchor (int(2482*sex_sampling), int(2703*sex_sampling))
    offset (int(2482*sex_sampling), int(2703*sex_sampling))

image Rogue_masturbation_pussy_open:
    "characters/Rogue/images/masturbation/pussy_open.webp"

    anchor (int(2482*sex_sampling), int(2703*sex_sampling))
    offset (int(2482*sex_sampling), int(2703*sex_sampling))

layeredimage Rogue_masturbation_pussy_agape:
    if Rogue.vagina_Actions[0].mode > 0:
        "characters/Rogue/images/masturbation/pussy_agape.webp"
    else:
        "characters/Rogue/images/masturbation/pussy_closed.webp"

    anchor (int(2474*sex_sampling), int(2675*sex_sampling))
    offset (int(2474*sex_sampling), int(2675*sex_sampling))

layeredimage Rogue_masturbation_right_hand:
    always:
        "characters/Rogue/images/masturbation/right_hand_shadow.webp"

    always:
        "characters/Rogue/images/masturbation/right_hand.webp"

    anchor (int(2357*sex_sampling), int(2109*sex_sampling))
    offset (int(2357*sex_sampling), int(2109*sex_sampling))

layeredimage Rogue_masturbation_left_leg:
    always:
        "characters/Rogue/images/masturbation/left_leg.webp"

    if Rogue.vagina_Actions:
        "Rogue_masturbation_left_foot_animation[Rogue.vagina_Actions[0].mode]"
    elif Rogue.anus_Actions:
        "Rogue_masturbation_left_foot_animation[Rogue.anus_Actions[0].mode]"
    else:
        "Rogue_masturbation_left_foot_animation0"

    anchor (int(4161*sex_sampling), int(1625*sex_sampling))
    offset (int(4161*sex_sampling), int(1625*sex_sampling))

layeredimage Rogue_masturbation_left_foot:
    always:
        "characters/Rogue/images/masturbation/left_foot.webp"

    anchor (int(4232*sex_sampling), int(3466*sex_sampling))
    offset (int(4232*sex_sampling), int(3466*sex_sampling))

layeredimage Rogue_masturbation_right_leg:
    always:
        "characters/Rogue/images/masturbation/right_leg.webp"

    if Rogue.vagina_Actions:
        "Rogue_masturbation_right_foot_animation[Rogue.vagina_Actions[0].mode]"
    elif Rogue.anus_Actions:
        "Rogue_masturbation_right_foot_animation[Rogue.anus_Actions[0].mode]"
    else:
        "Rogue_masturbation_right_foot_animation0"

    anchor (int(1031*sex_sampling), int(1428*sex_sampling))
    offset (int(1031*sex_sampling), int(1428*sex_sampling))

layeredimage Rogue_masturbation_right_foot:
    always:
        "characters/Rogue/images/masturbation/right_foot.webp"

    anchor (int(645*sex_sampling), int(3228*sex_sampling))
    offset (int(645*sex_sampling), int(3228*sex_sampling))

image Rogue_masturbation_male_left_arm_finger:
    "characters/Rogue/images/masturbation/male_left_arm_[Player.skin_color]_finger.webp"

    anchor (int(2538*sex_sampling), int(2622*sex_sampling))
    offset (int(2538*sex_sampling), int(2622*sex_sampling))

image Rogue_masturbation_male_right_arm_finger:
    "characters/Rogue/images/masturbation/male_right_arm_[Player.skin_color]_finger.webp"

    anchor (int(2421*sex_sampling), int(2594*sex_sampling))
    offset (int(2421*sex_sampling), int(2605*sex_sampling))

layeredimage Rogue_masturbation_male_left_arm:
    if Player.left_hand_Actions[0].animation_type in ["touch_thighs", "touch_thighs_higher"]:
        "characters/Rogue/images/masturbation/male_hand_shadow_right.webp"

    always:
        "characters/Rogue/images/masturbation/male_left_arm_[Player.skin_color].webp"

    anchor (int(1466*sex_sampling), int(2176*sex_sampling))
    offset (int(1466*sex_sampling), int(2176*sex_sampling))

layeredimage Rogue_masturbation_male_right_arm:
    if Player.right_hand_Actions[0].animation_type in ["touch_thighs", "touch_thighs_higher"]:
        "characters/Rogue/images/masturbation/male_hand_shadow_left.webp"

    always:
        "characters/Rogue/images/masturbation/male_right_arm_[Player.skin_color].webp"

    anchor (int(3664*sex_sampling), int(2460*sex_sampling))
    offset (int(3664*sex_sampling), int(2460*sex_sampling))

image Rogue_masturbation_dildo:
    "characters/Rogue/images/masturbation/dildo.webp"

    anchor (int(2478*sex_sampling), int(2630*sex_sampling))
    offset (int(2478*sex_sampling), int(2630*sex_sampling))

image Rogue_masturbation_vibrator:
    "characters/Rogue/images/masturbation/vibrator.webp"

    anchor (int(2481*sex_sampling), int(2445*sex_sampling))
    offset (int(2481*sex_sampling), int(2445*sex_sampling))

layeredimage Rogue_masturbation_mask_anus:
    if Rogue.anus_Actions[0].animation_type == "finger_ass" and Player.right_hand_Actions and Player.right_hand_Actions[0].animation_type == "finger_ass":
        "characters/Rogue/images/masturbation/mask_anus_right_finger.webp"
    elif Rogue.anus_Actions[0].animation_type == "finger_ass" and Player.left_hand_Actions and Player.left_hand_Actions[0].animation_type == "finger_ass":
        "characters/Rogue/images/masturbation/mask_anus_left_finger.webp"
    elif Rogue.anus_Actions[0].animation_type in ["dildo_ass", "self_dildo_ass"]:
        "characters/Rogue/images/masturbation/mask_anus_dildo.webp"

    anchor (int(2472*sex_sampling), int(2899*sex_sampling))
    offset (int(2472*sex_sampling), int(2899*sex_sampling))

layeredimage Rogue_masturbation_mask_pussy:
    if Rogue.vagina_Actions[0].animation_type == "finger_pussy" and Player.right_hand_Actions and Player.right_hand_Actions[0].animation_type == "finger_pussy":
        "characters/Rogue/images/masturbation/mask_pussy_right_finger.webp"
    elif Rogue.vagina_Actions[0].animation_type == "finger_pussy" and Player.left_hand_Actions and Player.left_hand_Actions[0].animation_type == "finger_pussy":
        "characters/Rogue/images/masturbation/mask_pussy_left_finger.webp"
    elif Rogue.vagina_Actions[0].animation_type in ["dildo_pussy", "self_dildo_pussy"]:
        "characters/Rogue/images/masturbation/mask_pussy_dildo.webp"

    anchor (int(2474*sex_sampling), int(2675*sex_sampling))
    offset (int(2474*sex_sampling), int(2675*sex_sampling))

layeredimage Rogue_masturbation_male_left_arm_fondle:
    if Player.left_hand_Actions[0].animation_type in ["touch_breasts"]:
        "Player_left_arm_fondle"
    elif Player.left_hand_Actions[0].animation_type in ["choke", "pinch_nipples"]:
        "Player_left_arm_pinch"

layeredimage Rogue_masturbation_male_right_arm_fondle:
    if Player.right_hand_Actions[0].animation_type in ["touch_breasts"]:
        "Player_right_arm_fondle"
    elif Player.right_hand_Actions[0].animation_type in ["choke", "pinch_nipples"]:
        "Player_right_arm_pinch"

layeredimage Rogue_masturbation_male_head:
    if Player.body_visible:
        "Player_head"

    if Player.mouth_Actions and Rogue in Player.mouth_Actions[0].Targets and Player.mouth_Actions[0].animation_type in ["suck_nipples", "eat_pussy", "eat_ass"]:
        "Rogue_masturbation_male_tongue_animation[Player.mouth_Actions[0].mode]"

image Rogue_masturbation_male_tongue:
    "Player_tongue"
    
image Rogue_masturbation_hair_back_animation0:
    "Rogue_masturbation_hair_back"

    masturbation_hair_back_animation0
    
image Rogue_masturbation_hair_back_animation1:
    "Rogue_masturbation_hair_back"

    masturbation_hair_back_animation1
    
image Rogue_masturbation_torso_animation0:
    "Rogue_masturbation_torso"

    masturbation_torso_animation0
    
image Rogue_masturbation_torso_animation1:
    "Rogue_masturbation_torso"

    masturbation_torso_animation1
    
image Rogue_masturbation_left_arm_animation0:
    "Rogue_masturbation_left_arm"

    masturbation_left_arm_animation0
    
image Rogue_masturbation_left_arm_animation1:
    "Rogue_masturbation_left_arm"

    masturbation_left_arm_animation1
    
image Rogue_masturbation_breasts_animation0:
    "Rogue_masturbation_breasts"

    masturbation_breasts_animation0
    
image Rogue_masturbation_breasts_animation1:
    "Rogue_masturbation_breasts"

    masturbation_breasts_animation1
    
image Rogue_masturbation_head_animation0:
    "Rogue_masturbation_head"

    masturbation_head_animation0
    
image Rogue_masturbation_head_animation1:
    "Rogue_masturbation_head"

    masturbation_head_animation1
    
image Rogue_masturbation_hair_animation0:
    "Rogue_masturbation_hair"

    masturbation_hair_animation0
    
image Rogue_masturbation_hair_animation1:
    "Rogue_masturbation_hair"

    masturbation_hair_animation1
    
image Rogue_masturbation_right_forearm_animation0:
    "Rogue_masturbation_right_forearm"

    masturbation_right_forearm_animation0
    
image Rogue_masturbation_right_forearm_animation1:
    "Rogue_masturbation_right_forearm"

    masturbation_right_forearm_animation1
    
image Rogue_masturbation_thighs_animation0:
    "Rogue_masturbation_thighs"

    masturbation_thighs_animation0
    
image Rogue_masturbation_thighs_animation1:
    "Rogue_masturbation_thighs"

    masturbation_thighs_animation1
    
image Rogue_masturbation_pussy_left_arm_finger_pussy_animation0:
    "Rogue_masturbation_pussy_closed"

    masturbation_pussy_left_arm_finger_pussy_animation0
    
image Rogue_masturbation_pussy_left_arm_finger_pussy_animation1:
    "Rogue_masturbation_pussy_agape"

    masturbation_pussy_left_arm_finger_pussy_animation1
    
image Rogue_masturbation_anus_left_arm_finger_ass_animation0:
    "Rogue_masturbation_anus_closed"

    masturbation_anus_left_arm_finger_ass_animation0
    
image Rogue_masturbation_anus_left_arm_finger_ass_animation1:
    "Rogue_masturbation_anus_agape"

    masturbation_anus_left_arm_finger_ass_animation1
    
image Rogue_masturbation_pussy_right_arm_finger_pussy_animation0:
    "Rogue_masturbation_pussy_closed"

    masturbation_pussy_right_arm_finger_pussy_animation0
    
image Rogue_masturbation_pussy_right_arm_finger_pussy_animation1:
    "Rogue_masturbation_pussy_agape"

    masturbation_pussy_right_arm_finger_pussy_animation1
    
image Rogue_masturbation_anus_right_arm_finger_ass_animation0:
    "Rogue_masturbation_anus_closed"

    masturbation_anus_right_arm_finger_ass_animation0
    
image Rogue_masturbation_anus_right_arm_finger_ass_animation1:
    "Rogue_masturbation_anus_agape"

    masturbation_anus_right_arm_finger_ass_animation1
    
image Rogue_masturbation_pussy_dildo_pussy_animation0:
    "Rogue_masturbation_pussy_closed"

    masturbation_pussy_dildo_pussy_animation0
    
image Rogue_masturbation_pussy_dildo_pussy_animation1:
    "Rogue_masturbation_pussy_agape"

    masturbation_pussy_dildo_pussy_animation1
    
image Rogue_masturbation_anus_dildo_ass_animation0:
    "Rogue_masturbation_anus_closed"

    masturbation_anus_dildo_ass_animation0
    
image Rogue_masturbation_anus_dildo_ass_animation1:
    "Rogue_masturbation_anus_agape"

    masturbation_anus_dildo_ass_animation1
    
image Rogue_masturbation_right_hand_animation0:
    "Rogue_masturbation_right_hand"

    masturbation_right_hand_animation0
    
image Rogue_masturbation_right_hand_animation1:
    "Rogue_masturbation_right_hand"

    masturbation_right_hand_animation1
    
image Rogue_masturbation_left_leg_animation0:
    "Rogue_masturbation_left_leg"

    masturbation_left_leg_animation0
    
image Rogue_masturbation_left_leg_animation1:
    "Rogue_masturbation_left_leg"

    masturbation_left_leg_animation1

image Rogue_masturbation_left_foot_animation0:
    "Rogue_masturbation_left_foot"

    masturbation_left_foot_animation0
    
image Rogue_masturbation_left_foot_animation1:
    "Rogue_masturbation_left_foot"

    masturbation_left_foot_animation1
    
image Rogue_masturbation_right_leg_animation0:
    "Rogue_masturbation_right_leg"

    masturbation_right_leg_animation0
    
image Rogue_masturbation_right_leg_animation1:
    "Rogue_masturbation_right_leg"

    masturbation_right_leg_animation1
    
image Rogue_masturbation_right_foot_animation0:
    "Rogue_masturbation_right_foot"

    masturbation_right_foot_animation0
    
image Rogue_masturbation_right_foot_animation1:
    "Rogue_masturbation_right_foot"

    masturbation_right_foot_animation1
    
image Rogue_masturbation_male_left_arm_choke_animation0:
    "Rogue_masturbation_male_left_arm_fondle"

    masturbation_male_left_arm_choke_animation0
    
image Rogue_masturbation_male_left_arm_choke_animation1:
    "Rogue_masturbation_male_left_arm_fondle"

    masturbation_male_left_arm_choke_animation1
    
image Rogue_masturbation_male_left_arm_touch_thighs_animation0:
    "Rogue_masturbation_male_left_arm"

    masturbation_male_left_arm_touch_thighs_animation0
    
image Rogue_masturbation_male_left_arm_touch_thighs_animation1:
    "Rogue_masturbation_male_left_arm"

    masturbation_male_left_arm_touch_thighs_animation1
    
image Rogue_masturbation_male_left_arm_touch_thighs_higher_animation0:
    "Rogue_masturbation_male_left_arm"

    masturbation_male_left_arm_touch_thighs_higher_animation0
    
image Rogue_masturbation_male_left_arm_touch_thighs_higher_animation1:
    "Rogue_masturbation_male_left_arm"

    masturbation_male_left_arm_touch_thighs_higher_animation1
    
image Rogue_masturbation_male_left_arm_touch_right_breast_animation0:
    "Rogue_masturbation_male_left_arm_fondle"

    masturbation_male_left_arm_touch_right_breast_animation0
    
image Rogue_masturbation_male_left_arm_touch_right_breast_animation1:
    "Rogue_masturbation_male_left_arm_fondle"

    masturbation_male_left_arm_touch_right_breast_animation1
    
image Rogue_masturbation_male_left_arm_touch_left_breast_animation0:
    "Rogue_masturbation_male_left_arm_fondle"

    masturbation_male_left_arm_touch_left_breast_animation0
    
image Rogue_masturbation_male_left_arm_touch_left_breast_animation1:
    "Rogue_masturbation_male_left_arm_fondle"

    masturbation_male_left_arm_touch_left_breast_animation1

image Rogue_masturbation_male_left_arm_finger_pussy_animation0:
    "Rogue_masturbation_male_left_arm_finger"

    masturbation_male_left_arm_finger_pussy_animation0

image Rogue_masturbation_male_left_arm_finger_pussy_animation1:
    "Rogue_masturbation_male_left_arm_finger"

    masturbation_male_left_arm_finger_pussy_animation1
    
image Rogue_masturbation_male_left_arm_finger_ass_animation0:
    "Rogue_masturbation_male_left_arm_finger"

    masturbation_male_left_arm_finger_ass_animation0
    
image Rogue_masturbation_male_left_arm_finger_ass_animation1:
    "Rogue_masturbation_male_left_arm_finger"

    masturbation_male_left_arm_finger_ass_animation1
    
image Rogue_masturbation_male_right_arm_choke_animation0:
    "Rogue_masturbation_male_right_arm_fondle"

    masturbation_male_right_arm_choke_animation0
    
image Rogue_masturbation_male_right_arm_choke_animation1:
    "Rogue_masturbation_male_right_arm_fondle"

    masturbation_male_right_arm_choke_animation1
    
image Rogue_masturbation_male_right_arm_touch_thighs_animation0:
    "Rogue_masturbation_male_right_arm"

    masturbation_male_right_arm_touch_thighs_animation0
    
image Rogue_masturbation_male_right_arm_touch_thighs_animation1:
    "Rogue_masturbation_male_right_arm"

    masturbation_male_right_arm_touch_thighs_animation1
    
image Rogue_masturbation_male_right_arm_touch_thighs_higher_animation0:
    "Rogue_masturbation_male_right_arm"

    masturbation_male_right_arm_touch_thighs_higher_animation0
    
image Rogue_masturbation_male_right_arm_touch_thighs_higher_animation1:
    "Rogue_masturbation_male_right_arm"

    masturbation_male_right_arm_touch_thighs_higher_animation1
    
image Rogue_masturbation_male_right_arm_touch_right_breast_animation0:
    "Rogue_masturbation_male_right_arm_fondle"

    masturbation_male_right_arm_touch_right_breast_animation0
    
image Rogue_masturbation_male_right_arm_touch_right_breast_animation1:
    "Rogue_masturbation_male_right_arm_fondle"

    masturbation_male_right_arm_touch_right_breast_animation1
    
image Rogue_masturbation_male_right_arm_touch_left_breast_animation0:
    "Rogue_masturbation_male_right_arm_fondle"

    masturbation_male_right_arm_touch_left_breast_animation0
    
image Rogue_masturbation_male_right_arm_touch_left_breast_animation1:
    "Rogue_masturbation_male_right_arm_fondle"

    masturbation_male_right_arm_touch_left_breast_animation1

image Rogue_masturbation_male_right_arm_finger_pussy_animation0:
    "Rogue_masturbation_male_right_arm_finger"

    masturbation_male_right_arm_finger_pussy_animation0

image Rogue_masturbation_male_right_arm_finger_pussy_animation1:
    "Rogue_masturbation_male_right_arm_finger"

    masturbation_male_right_arm_finger_pussy_animation1
    
image Rogue_masturbation_male_right_arm_finger_ass_animation0:
    "Rogue_masturbation_male_right_arm_finger"

    masturbation_male_right_arm_finger_ass_animation0
    
image Rogue_masturbation_male_right_arm_finger_ass_animation1:
    "Rogue_masturbation_male_right_arm_finger"

    masturbation_male_right_arm_finger_ass_animation1
    
image Rogue_masturbation_dildo_pussy_animation0:
    "Rogue_masturbation_dildo"

    masturbation_dildo_pussy_animation0

image Rogue_masturbation_dildo_pussy_animation1:
    "Rogue_masturbation_dildo"

    masturbation_dildo_pussy_animation1
    
image Rogue_masturbation_dildo_ass_animation0:
    "Rogue_masturbation_dildo"

    masturbation_dildo_ass_animation0
    
image Rogue_masturbation_dildo_ass_animation1:
    "Rogue_masturbation_dildo"

    masturbation_dildo_ass_animation1
    
image Rogue_masturbation_vibrator_animation0:
    "Rogue_masturbation_vibrator"

    masturbation_vibrator_animation0
    
image Rogue_masturbation_vibrator_animation1:
    "Rogue_masturbation_vibrator"

    masturbation_vibrator_animation1
    
image Rogue_masturbation_mask_left_arm_finger_pussy_animation0:
    "Rogue_masturbation_mask_pussy"

    masturbation_mask_left_arm_finger_pussy_animation0
    
image Rogue_masturbation_mask_left_arm_finger_pussy_animation1:
    "Rogue_masturbation_mask_pussy"

    masturbation_mask_left_arm_finger_pussy_animation1
    
image Rogue_masturbation_mask_left_arm_finger_ass_animation0:
    "Rogue_masturbation_mask_anus"

    masturbation_mask_left_arm_finger_ass_animation0
    
image Rogue_masturbation_mask_left_arm_finger_ass_animation1:
    "Rogue_masturbation_mask_anus"

    masturbation_mask_left_arm_finger_ass_animation1
    
image Rogue_masturbation_mask_right_arm_finger_pussy_animation0:
    "Rogue_masturbation_mask_pussy"

    masturbation_mask_right_arm_finger_pussy_animation0
    
image Rogue_masturbation_mask_right_arm_finger_pussy_animation1:
    "Rogue_masturbation_mask_pussy"

    masturbation_mask_right_arm_finger_pussy_animation1
    
image Rogue_masturbation_mask_right_arm_finger_ass_animation0:
    "Rogue_masturbation_mask_anus"

    masturbation_mask_right_arm_finger_ass_animation0
    
image Rogue_masturbation_mask_right_arm_finger_ass_animation1:
    "Rogue_masturbation_mask_anus"

    masturbation_mask_right_arm_finger_ass_animation1
    
image Rogue_masturbation_mask_dildo_pussy_animation0:
    "Rogue_masturbation_mask_pussy"

    masturbation_mask_dildo_pussy_animation0
    
image Rogue_masturbation_mask_dildo_pussy_animation1:
    "Rogue_masturbation_mask_pussy"

    masturbation_mask_dildo_pussy_animation1
    
image Rogue_masturbation_mask_dildo_ass_animation0:
    "Rogue_masturbation_mask_anus"

    masturbation_mask_dildo_ass_animation0
    
image Rogue_masturbation_mask_dildo_ass_animation1:
    "Rogue_masturbation_mask_anus"

    masturbation_mask_dildo_ass_animation1
    
image Rogue_masturbation_male_head_suck_left_nipple_animation0:
    "Rogue_masturbation_male_head"

    masturbation_male_head_suck_left_nipple_animation0
    
image Rogue_masturbation_male_head_suck_left_nipple_animation1:
    "Rogue_masturbation_male_head"

    masturbation_male_head_suck_left_nipple_animation1
    
image Rogue_masturbation_male_head_suck_right_nipple_animation0:
    "Rogue_masturbation_male_head"

    masturbation_male_head_suck_right_nipple_animation0
    
image Rogue_masturbation_male_head_suck_right_nipple_animation1:
    "Rogue_masturbation_male_head"

    masturbation_male_head_suck_right_nipple_animation1
    
image Rogue_masturbation_male_head_eat_pussy_animation0:
    "Rogue_masturbation_male_head"

    masturbation_male_head_eat_pussy_animation0
    
image Rogue_masturbation_male_head_eat_pussy_animation1:
    "Rogue_masturbation_male_head"

    masturbation_male_head_eat_pussy_animation1
    
image Rogue_masturbation_male_head_eat_ass_animation0:
    "Rogue_masturbation_male_head"

    masturbation_male_head_eat_ass_animation0
    
image Rogue_masturbation_male_head_eat_ass_animation1:
    "Rogue_masturbation_male_head"

    masturbation_male_head_eat_ass_animation1
    
image Rogue_masturbation_male_tongue_animation0:
    "Rogue_masturbation_male_tongue"

    masturbation_male_tongue_animation0
    
image Rogue_masturbation_male_tongue_animation1:
    "Rogue_masturbation_male_tongue"

    masturbation_male_tongue_animation1

layeredimage Rogue_masturbation_male_left_arm_finger_animations:
    always:
        "Rogue_masturbation_male_left_arm_[Player.left_hand_Actions[0].animation_type]_animation[Player.left_hand_Actions[0].mode]"

layeredimage Rogue_masturbation_male_right_arm_finger_animations:
    always:
        "Rogue_masturbation_male_right_arm_[Player.right_hand_Actions[0].animation_type]_animation[Player.right_hand_Actions[0].mode]"

layeredimage Rogue_masturbation_dildo_pussy_animations:
    always:
        "Rogue_masturbation_dildo_pussy_animation[Rogue.vagina_Actions[0].mode]"

layeredimage Rogue_masturbation_dildo_ass_animations:
    always:
        "Rogue_masturbation_dildo_ass_animation[Rogue.anus_Actions[0].mode]"

layeredimage Rogue_masturbation_mask_anus_animations:
    if Rogue.anus_Actions[0].animation_type == "finger_ass" and Player.left_hand_Actions and Player.left_hand_Actions[0].animation_type == "finger_ass":
        "Rogue_masturbation_mask_left_arm_finger_ass_animation[Rogue.anus_Actions[0].mode]"
    elif Rogue.anus_Actions[0].animation_type == "finger_ass" and Player.right_hand_Actions and Player.right_hand_Actions[0].animation_type == "finger_ass":
        "Rogue_masturbation_mask_right_arm_finger_ass_animation[Rogue.anus_Actions[0].mode]"
    elif Rogue.anus_Actions[0].animation_type in ["dildo_ass", "self_dildo_ass"]:
        "Rogue_masturbation_mask_dildo_ass_animation[Rogue.anus_Actions[0].mode]"

layeredimage Rogue_masturbation_mask_pussy_animations:
    if Rogue.vagina_Actions[0].animation_type == "finger_pussy" and Player.left_hand_Actions and Player.left_hand_Actions[0].animation_type == "finger_pussy":
        "Rogue_masturbation_mask_left_arm_finger_pussy_animation[Rogue.vagina_Actions[0].mode]"
    elif Rogue.vagina_Actions[0].animation_type == "finger_pussy" and Player.right_hand_Actions and Player.right_hand_Actions[0].animation_type == "finger_pussy":
        "Rogue_masturbation_mask_right_arm_finger_pussy_animation[Rogue.vagina_Actions[0].mode]"
    elif Rogue.vagina_Actions[0].animation_type in ["dildo_pussy", "self_dildo_pussy"]:
        "Rogue_masturbation_mask_dildo_pussy_animation[Rogue.vagina_Actions[0].mode]"
    
image Rogue_masturbation_blinking:
    "characters/Rogue/images/masturbation/eyes_[Rogue.eyes].webp"
    choice:
        4.5
    choice:
        4.0
    choice:
        3.5
    "characters/Rogue/images/masturbation/eyes_blink1.webp"
    0.023
    "characters/Rogue/images/masturbation/eyes_blink2.webp"
    0.023
    "characters/Rogue/images/masturbation/eyes_closed.webp"
    0.054
    "characters/Rogue/images/masturbation/eyes_blink2.webp"
    0.018
    "characters/Rogue/images/masturbation/eyes_blink1.webp"
    0.072
    repeat