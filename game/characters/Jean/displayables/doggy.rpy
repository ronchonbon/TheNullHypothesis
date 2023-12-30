image Jean_sprite doggy:
    contains:
        "Jean_doggy_temp"

    offset (-int(500*0.38), 0)
            
layeredimage Jean_doggy_temp:
    if Jean.hovered:
        At("Jean_doggy_controls_temp", hover)
    else:
        "Jean_doggy_controls_temp"
            
layeredimage Jean_doggy_controls_temp:
    if speed > 2.5 or speed <= 1.75:
        Null()
    elif intensity >= 2.0:
        At(At("Jean_doggy", speed_200), intensity_200)
    elif intensity >= 1.75:
        At(At("Jean_doggy", speed_200), intensity_175)
    elif intensity >= 1.5:
        At(At("Jean_doggy", speed_200), intensity_150)
    elif intensity >= 1.25:
        At(At("Jean_doggy", speed_200), intensity_125)
    elif intensity >= 1.0:
        At(At("Jean_doggy", speed_200), intensity_100)
    elif intensity >= 0.75:
        At(At("Jean_doggy", speed_200), intensity_075)
    elif intensity >= 0.5:
        At(At("Jean_doggy", speed_200), intensity_050)
    elif intensity >= 0.25:
        At(At("Jean_doggy", speed_200), intensity_025)
    else:
        At(At("Jean_doggy", speed_200), intensity_000)

    if speed > 1.75 or speed <= 1.5:
        Null()
    elif intensity >= 2.0:
        At(At("Jean_doggy", speed_175), intensity_200)
    elif intensity >= 1.75:
        At(At("Jean_doggy", speed_175), intensity_175)
    elif intensity >= 1.5:
        At(At("Jean_doggy", speed_175), intensity_150)
    elif intensity >= 1.25:
        At(At("Jean_doggy", speed_175), intensity_125)
    elif intensity >= 1.0:
        At(At("Jean_doggy", speed_175), intensity_100)
    elif intensity >= 0.75:
        At(At("Jean_doggy", speed_175), intensity_075)
    elif intensity >= 0.5:
        At(At("Jean_doggy", speed_175), intensity_050)
    elif intensity >= 0.25:
        At(At("Jean_doggy", speed_175), intensity_025)
    else:
        At(At("Jean_doggy", speed_175), intensity_000)

    if speed > 1.5 or speed <= 1.25:
        Null()
    elif intensity >= 2.0:
        At(At("Jean_doggy", speed_150), intensity_200)
    elif intensity >= 1.75:
        At(At("Jean_doggy", speed_150), intensity_175)
    elif intensity >= 1.5:
        At(At("Jean_doggy", speed_150), intensity_150)
    elif intensity >= 1.25:
        At(At("Jean_doggy", speed_150), intensity_125)
    elif intensity >= 1.0:
        At(At("Jean_doggy", speed_150), intensity_100)
    elif intensity >= 0.75:
        At(At("Jean_doggy", speed_150), intensity_075)
    elif intensity >= 0.5:
        At(At("Jean_doggy", speed_150), intensity_050)
    elif intensity >= 0.25:
        At(At("Jean_doggy", speed_150), intensity_025)
    else:
        At(At("Jean_doggy", speed_150), intensity_000)
 
    if speed > 1.25 or speed <= 1.0:
        Null()
    elif intensity >= 2.0:
        At(At("Jean_doggy", speed_125), intensity_200)
    elif intensity >= 1.75:
        At(At("Jean_doggy", speed_125), intensity_175)
    elif intensity >= 1.5:
        At(At("Jean_doggy", speed_125), intensity_150)
    elif intensity >= 1.25:
        At(At("Jean_doggy", speed_125), intensity_125)
    elif intensity >= 1.0:
        At(At("Jean_doggy", speed_125), intensity_100)
    elif intensity >= 0.75:
        At(At("Jean_doggy", speed_125), intensity_075)
    elif intensity >= 0.5:
        At(At("Jean_doggy", speed_125), intensity_050)
    elif intensity >= 0.25:
        At(At("Jean_doggy", speed_125), intensity_025)
    else:
        At(At("Jean_doggy", speed_125), intensity_000)
 
    if speed > 1.0 or speed <= 0.75:
        Null()
    elif intensity >= 2.0:
        At(At("Jean_doggy", speed_100), intensity_200)
    elif intensity >= 1.75:
        At(At("Jean_doggy", speed_100), intensity_175)
    elif intensity >= 1.5:
        At(At("Jean_doggy", speed_100), intensity_150)
    elif intensity >= 1.25:
        At(At("Jean_doggy", speed_100), intensity_125)
    elif intensity >= 1.0:
        At(At("Jean_doggy", speed_100), intensity_100)
    elif intensity >= 0.75:
        At(At("Jean_doggy", speed_100), intensity_075)
    elif intensity >= 0.5:
        At(At("Jean_doggy", speed_100), intensity_050)
    elif intensity >= 0.25:
        At(At("Jean_doggy", speed_100), intensity_025)
    else:
        At(At("Jean_doggy", speed_100), intensity_000)

    if speed > 0.75 or speed <= 0.5:
        Null()
    elif intensity >= 2.0:
        At(At("Jean_doggy", speed_075), intensity_200)
    elif intensity >= 1.75:
        At(At("Jean_doggy", speed_075), intensity_175)
    elif intensity >= 1.5:
        At(At("Jean_doggy", speed_075), intensity_150)
    elif intensity >= 1.25:
        At(At("Jean_doggy", speed_075), intensity_125)
    elif intensity >= 1.0:
        At(At("Jean_doggy", speed_075), intensity_100)
    elif intensity >= 0.75:
        At(At("Jean_doggy", speed_075), intensity_075)
    elif intensity >= 0.5:
        At(At("Jean_doggy", speed_075), intensity_050)
    elif intensity >= 0.25:
        At(At("Jean_doggy", speed_075), intensity_025)
    else:
        At(At("Jean_doggy", speed_075), intensity_000)

    if speed > 0.5 or speed <= 0.25:
        Null()
    elif intensity >= 2.0:
        At(At("Jean_doggy", speed_050), intensity_200)
    elif intensity >= 1.75:
        At(At("Jean_doggy", speed_050), intensity_175)
    elif intensity >= 1.5:
        At(At("Jean_doggy", speed_050), intensity_150)
    elif intensity >= 1.25:
        At(At("Jean_doggy", speed_050), intensity_125)
    elif intensity >= 1.0:
        At(At("Jean_doggy", speed_050), intensity_100)
    elif intensity >= 0.75:
        At(At("Jean_doggy", speed_050), intensity_075)
    elif intensity >= 0.5:
        At(At("Jean_doggy", speed_050), intensity_050)
    elif intensity >= 0.25:
        At(At("Jean_doggy", speed_050), intensity_025)
    else:
        At(At("Jean_doggy", speed_050), intensity_000)

    if speed > 0.25 or speed <= 0.01:
        Null()
    elif intensity >= 2.0:
        At(At("Jean_doggy", speed_025), intensity_200)
    elif intensity >= 1.75:
        At(At("Jean_doggy", speed_025), intensity_175)
    elif intensity >= 1.5:
        At(At("Jean_doggy", speed_025), intensity_150)
    elif intensity >= 1.25:
        At(At("Jean_doggy", speed_025), intensity_125)
    elif intensity >= 1.0:
        At(At("Jean_doggy", speed_025), intensity_100)
    elif intensity >= 0.75:
        At(At("Jean_doggy", speed_025), intensity_075)
    elif intensity >= 0.5:
        At(At("Jean_doggy", speed_025), intensity_050)
    elif intensity >= 0.25:
        At(At("Jean_doggy", speed_025), intensity_025)
    else:
        At(At("Jean_doggy", speed_025), intensity_000)

    if speed != 0.01:
        Null()
    elif intensity >= 2.0:
        At(At("Jean_doggy", speed_0001), intensity_200)
    elif intensity >= 1.75:
        At(At("Jean_doggy", speed_0001), intensity_175)
    elif intensity >= 1.5:
        At(At("Jean_doggy", speed_0001), intensity_150)
    elif intensity >= 1.25:
        At(At("Jean_doggy", speed_0001), intensity_125)
    elif intensity >= 1.0:
        At(At("Jean_doggy", speed_0001), intensity_100)
    elif intensity >= 0.75:
        At(At("Jean_doggy", speed_0001), intensity_075)
    elif intensity >= 0.5:
        At(At("Jean_doggy", speed_0001), intensity_050)
    elif intensity >= 0.25:
        At(At("Jean_doggy", speed_0001), intensity_025)
    else:
        At(At("Jean_doggy", speed_0001), intensity_000)

    if speed >= 0.01 or speed < 0.0:
        Null()
    elif intensity >= 2.0:
        At(At("Jean_doggy", speed_000), intensity_200)
    elif intensity >= 1.75:
        At(At("Jean_doggy", speed_000), intensity_175)
    elif intensity >= 1.5:
        At(At("Jean_doggy", speed_000), intensity_150)
    elif intensity >= 1.25:
        At(At("Jean_doggy", speed_000), intensity_125)
    elif intensity >= 1.0:
        At(At("Jean_doggy", speed_000), intensity_100)
    elif intensity >= 0.75:
        At(At("Jean_doggy", speed_000), intensity_075)
    elif intensity >= 0.5:
        At(At("Jean_doggy", speed_000), intensity_050)
    elif intensity >= 0.25:
        At(At("Jean_doggy", speed_000), intensity_025)
    else:
        At(At("Jean_doggy", speed_000), intensity_000)
 
layeredimage Jean_doggy:
    if Player.orgasming and focused_Character == Jean:
        "Jean_doggy_ass_animation0"
    elif Player.cock_Actions and Jean in Player.cock_Actions[0].Targets:
        "Jean_doggy_ass_animation[Player.cock_Actions[0].mode]"
    else: 
        "Jean_doggy_ass_animation0"
    
layeredimage Jean_doggy_ass:
    if Player.orgasming and focused_Character == Jean:
        "Jean_doggy_left_leg_animation0"
    elif Player.cock_Actions and Jean in Player.cock_Actions[0].Targets and Jean.orgasming:
        At("Jean_doggy_left_leg_animation[Player.cock_Actions[0].mode]", tremble(20))
    elif Player.cock_Actions and Jean in Player.cock_Actions[0].Targets:
        "Jean_doggy_left_leg_animation[Player.cock_Actions[0].mode]"
    elif Jean.orgasming:
        At("Jean_doggy_left_leg_animation0", tremble(20))
    else:
        "Jean_doggy_left_leg_animation0"

    if Player.orgasming and focused_Character == Jean:
        "Jean_doggy_right_leg_animation0"
    elif Player.cock_Actions and Jean in Player.cock_Actions[0].Targets and Jean.orgasming:
        At("Jean_doggy_right_leg_animation[Player.cock_Actions[0].mode]", tremble(20))
    elif Player.cock_Actions and Jean in Player.cock_Actions[0].Targets:
        "Jean_doggy_right_leg_animation[Player.cock_Actions[0].mode]"
    elif Jean.orgasming:
        At("Jean_doggy_right_leg_animation0", tremble(20))
    else:
        "Jean_doggy_right_leg_animation0"
        
    if Player.orgasming and focused_Character == Jean:
        "Jean_doggy_torso_animation0"
    elif Player.cock_Actions and Jean in Player.cock_Actions[0].Targets and Jean.orgasming:
        At("Jean_doggy_torso_animation[Player.cock_Actions[0].mode]", tremble(20))
    elif Player.cock_Actions and Jean in Player.cock_Actions[0].Targets:
        "Jean_doggy_torso_animation[Player.cock_Actions[0].mode]"
    elif Jean.orgasming:
        At("Jean_doggy_torso_animation0", tremble(20))
    else:
        "Jean_doggy_torso_animation0"
        
    if not Player.body_visible:
        Null()
    elif Player.orgasming and focused_Character == Jean:
        "Jean_doggy_male_body_[Player.orgasming]_animation"
    elif Player.cock_Actions and Jean in Player.cock_Actions[0].Targets:
        "Jean_doggy_male_body_[Player.cock_Actions[0].animation_type]_animation[Player.cock_Actions[0].mode]"
            
    if Jean.Clothes["underwear"].string and Jean.Clothes["underwear"].state == 0:
        Null()
    elif "pubic" in Jean.body_hair_growing.keys():
        "characters/Jean/images/doggy/pubes_growing.webp"

    if not Jean.body_hair["pubic"] or (Jean.Clothes["underwear"].string and Jean.Clothes["underwear"].state == 0):
        Null()
    elif "triangle" in Jean.body_hair["pubic"]:
        "characters/Jean/images/doggy/pubes_triangle.webp"
    elif "strip" in Jean.body_hair["pubic"]:
        "characters/Jean/images/doggy/pubes_strip.webp"
    else:
        "characters/Jean/images/doggy/pubes_[Jean.body_hair[pubic]].webp"

    if Jean.Clothes["underwear"].string and Jean.Clothes["underwear"].state == 0:
        Null()
    elif Jean.piercings["labia"] in ["ring", "both"]:
        "characters/Jean/images/doggy/labia_piercings_ring.webp"

    always:
        "characters/Jean/images/doggy/ass.webp"

    if Player.orgasming == "creampie" and focused_Character == Jean:
        "Jean_doggy_pussy_creampie_animation"
    elif not Jean.vagina_Actions:
        "Jean_doggy_pussy_closed"
    elif Jean.vagina_Actions[0].animation_type == "grind_pussy":
        "Jean_doggy_pussy_grind_pussy_animation[Jean.vagina_Actions[0].mode]"
    elif Jean.vagina_Actions[0].animation_type in ["dildo_pussy", "self_dildo_pussy"]:
        "Jean_doggy_pussy_dildo_pussy_animation[Jean.vagina_Actions[0].mode]"
    elif Jean.vagina_Actions[0].animation_type == "finger_pussy":
        "Jean_doggy_pussy_finger_pussy_animation[Jean.vagina_Actions[0].mode]"
    elif Player.orgasming and focused_Character == Jean:
        "Jean_doggy_pussy_closed"
    else:
        "Jean_doggy_pussy_[Jean.vagina_Actions[0].animation_type]_animation[Jean.vagina_Actions[0].mode]"

    if Player.orgasming == "anal_creampie" and focused_Character == Jean:
        "Jean_doggy_anus_anal_creampie_animation"
    elif not Jean.anus_Actions or Jean.anus_Actions[0].animation_type == "eat_ass":
        "Jean_doggy_anus_closed"
    elif Jean.anus_Actions[0].animation_type == "self_finger_ass":
        "Jean_doggy_anus_open"
    elif Jean.anus_Actions[0].animation_type == "grind_ass":
        "Jean_doggy_anus_grind_ass_animation[Jean.anus_Actions[0].mode]"
    elif Jean.anus_Actions[0].animation_type in ["dildo_ass", "self_dildo_ass"]:
        "Jean_doggy_anus_dildo_ass_animation[Jean.anus_Actions[0].mode]"
    elif Jean.anus_Actions[0].animation_type == "finger_ass":
        "Jean_doggy_anus_finger_ass_animation[Jean.anus_Actions[0].mode]"
    elif Player.orgasming and focused_Character == Jean:
        "Jean_doggy_anus_closed"
    else:
        "Jean_doggy_anus_[Jean.anus_Actions[0].animation_type]_animation[Jean.anus_Actions[0].mode]"

    if Player.orgasming == "creampie" and focused_Character == Jean:
        "Jean_doggy_creampie"
    elif not Jean.creampie["pussy"]:
        Null()
    elif Jean.vagina_Actions and Jean.vagina_Actions[0].animation_type in ["finger_pussy", "eat_pussy", "grind_pussy"]:
        "characters/Jean/images/doggy/creampie_pussy_open.webp"
    elif Jean.vagina_Actions:
        "characters/Jean/images/doggy/creampie_pussy_agape.webp"
    else:
        "characters/Jean/images/doggy/creampie_pussy_closed.webp"

    if Jean.remote_vibrator is not None:
        "characters/Jean/images/doggy/remote_vibrator.webp"

    if Player.cock_Actions and Jean in Player.cock_Actions[0].Targets:
        Null()
    elif Jean.clitoris_Actions and Jean.clitoris_Actions[0].animation_type in ["vibrator", "self_vibrator"]:
        "Jean_doggy_vibrator_animation[Jean.clitoris_Actions[0].mode]"

    if Player.orgasming == "anal_creampie" and focused_Character == Jean:
        "Jean_doggy_anal_creampie"
    elif not Jean.creampie["anus"]:
        Null()
    elif Jean.anus_Actions and Jean.anus_Actions[0].animation_type in ["finger_ass", "eat_ass", "self_finger_ass", "grind_ass"]:
        "characters/Jean/images/doggy/creampie_anus_open.webp"
    elif Jean.anus_Actions:
        "characters/Jean/images/doggy/creampie_anus_agape.webp"
    else:
        "characters/Jean/images/doggy/creampie_anus_closed.webp"

    if not Jean.buttplug:
        Null()
    elif Jean.buttplug.string == "heart_anal_plug":
        "characters/Jean/images/doggy/buttplug_heart.webp"
    elif Jean.buttplug.string == "round_anal_plug":
        "characters/Jean/images/doggy/buttplug_round.webp"

    if Jean.spunk["ass"]:
        "characters/Jean/images/doggy/spunk_ass.webp"

    if Jean.spunk["back"]:
        "characters/Jean/images/doggy/spunk_back.webp"

    if Player.cock_Actions and Jean in Player.cock_Actions[0].Targets and Player.cock_Actions[0].animation_type == "anal":
        Null()
    elif Jean.vagina_Actions and Jean.vagina_Actions[0].animation_type in ["dildo_pussy", "self_dildo_pussy"]:
        AlphaMask("Jean_doggy_dildo_pussy_animations", "Jean_doggy_mask_pussy_animations")

    if Player.orgasming == "cumshot" and focused_Character == Jean:
        Null()
    elif Player.orgasming == "creampie" and focused_Character == Jean:
        AlphaMask("Jean_doggy_cock_animations", "Jean_doggy_mask_pussy_animations")
    elif Player.orgasming == "anal_creampie" and focused_Character == Jean:
        AlphaMask("Jean_doggy_cock_animations", "Jean_doggy_mask_anus_animations")
    elif Player.cock_Actions and Jean in Player.cock_Actions[0].Targets and Player.cock_Actions[0].animation_type == "sex":
        AlphaMask("Jean_doggy_cock_animations", "Jean_doggy_mask_pussy_animations")
    elif Player.cock_Actions and Jean in Player.cock_Actions[0].Targets and Player.cock_Actions[0].animation_type == "anal":
        AlphaMask("Jean_doggy_cock_animations", "Jean_doggy_mask_anus_animations")

    if Jean.anus_Actions and Jean.anus_Actions[0].animation_type in ["dildo_ass", "self_dildo_ass"]:
        AlphaMask("Jean_doggy_dildo_ass_animations", "Jean_doggy_mask_anus_animations")

    if Player.orgasming == "cumshot" and focused_Character == Jean:
        "Jean_doggy_cock_animations"
    elif Player.cock_Actions and Jean in Player.cock_Actions[0].Targets and Player.cock_Actions[0].animation_type in ["grind_pussy", "grind_ass"]:
        "Jean_doggy_cock_animations"

    if Player.orgasming == "cumshot" and focused_Character == Jean:
        "Jean_doggy_cumshot"

    if Player.orgasming and focused_Character == Jean:
        Null()
    elif not Player.right_hand_Actions or Jean not in Player.right_hand_Actions[0].Targets:
        Null()
    elif Player.right_hand_Actions[0].animation_type == "finger_pussy":
        AlphaMask("Jean_doggy_male_right_arm_finger_animations", "Jean_doggy_mask_pussy_animations")
    elif Player.right_hand_Actions[0].animation_type == "finger_ass":
        AlphaMask("Jean_doggy_male_right_arm_finger_animations", "Jean_doggy_mask_anus_animations")

    if not Jean.right_hand_Actions or Jean.right_hand_Actions[0].animation_type != "self_finger_ass":
        Null()
    elif Player.orgasming == "anal_creampie" and focused_Character == Jean:
        Null()
    elif Jean.right_hand_Actions and Jean.right_hand_Actions[0].animation_type == "self_finger_ass":
        "Jean_doggy_right_forearm_self_finger_ass_animation[Jean.right_hand_Actions[0].mode]"

    if not Player.body_visible:
        Null()
    elif Player.left_hand_Actions and Jean in Player.left_hand_Actions[0].Targets and Player.left_hand_Actions[0].animation_type == "grab_ass":
        "Jean_doggy_male_left_arm_animation0"
    elif Player.left_hand_Actions:
        Null()
    elif Player.orgasming and focused_Character == Jean:
        "Jean_doggy_male_left_arm_animation0"
    elif Player.cock_Actions and Jean in Player.cock_Actions[0].Targets:
        "Jean_doggy_male_left_arm_animation[Player.cock_Actions[0].mode]"

    if not Player.body_visible:
        Null()
    elif Player.right_hand_Actions and Jean in Player.right_hand_Actions[0].Targets and Player.right_hand_Actions[0].animation_type == "grab_ass":
        "Jean_doggy_male_right_arm_animation0"
    elif Player.right_hand_Actions:
        Null()
    elif Player.orgasming and focused_Character == Jean:
        "Jean_doggy_male_right_arm_animation0"
    elif Player.cock_Actions and Jean in Player.cock_Actions[0].Targets:
        "Jean_doggy_male_right_arm_animation[Player.cock_Actions[0].mode]"

    if Player.orgasming and focused_Character == Jean:
        Null()
    elif not Player.mouth_Actions or Jean not in Player.mouth_Actions[0].Targets:
        Null()
    elif Player.mouth_Actions[0].animation_type == "eat_pussy":
        At("Jean_doggy_male_head_eat_pussy_animation[Player.mouth_Actions[0].mode]", change_offset(Jean_doggy_pussy_position[0], Jean_doggy_pussy_position[1]))
    elif Player.mouth_Actions[0].animation_type == "eat_ass":
        At("Jean_doggy_male_head_eat_ass_animation[Player.mouth_Actions[0].mode]", change_offset(Jean_doggy_anus_position[0], Jean_doggy_anus_position[1]))

    anchor (int(2101*sex_sampling), int(2097*sex_sampling))
    offset (int(2101*sex_sampling), int(2097*sex_sampling))
    
layeredimage Jean_doggy_left_leg:
    always:
        "characters/Jean/images/doggy/left_leg.webp"

    anchor (int(832*sex_sampling), int(2550*sex_sampling))
    offset (int(832*sex_sampling), int(2550*sex_sampling))

layeredimage Jean_doggy_right_leg:
    always:
        "characters/Jean/images/doggy/right_leg.webp"

    anchor (int(3365*sex_sampling), int(2531*sex_sampling))
    offset (int(3365*sex_sampling), int(2531*sex_sampling))

layeredimage Jean_doggy_torso:
    if Player.orgasming == "anal_creampie" and focused_Character == Jean:
        "Jean_doggy_right_arm_animation0"
    elif Jean.right_hand_Actions and Jean.right_hand_Actions[0].animation_type == "self_finger_ass":
        Null()
    elif Player.orgasming and focused_Character == Jean:
        "Jean_doggy_right_arm_animation0"
    elif Player.cock_Actions and Jean in Player.cock_Actions[0].Targets:
        "Jean_doggy_right_arm_animation[Player.cock_Actions[0].mode]"
    else:
        "Jean_doggy_right_arm_animation0"

    if Player.orgasming and focused_Character == Jean:
        "Jean_doggy_head_animation0"
    elif Player.cock_Actions and Jean in Player.cock_Actions[0].Targets:
        "Jean_doggy_head_animation[Player.cock_Actions[0].mode]"
    else:
        "Jean_doggy_head_animation0"

    always:
        "characters/Jean/images/doggy/torso.webp"

    if not Jean.right_hand_Actions or Jean.right_hand_Actions[0].animation_type != "self_finger_ass":
        Null()
    elif Player.orgasming and Player.orgasming != "anal_creampie" and focused_Character == Jean:
        "Jean_doggy_right_arm_self_finger_ass_animation0"
    elif Jean.right_hand_Actions and Jean.right_hand_Actions[0].animation_type == "self_finger_ass":
        "Jean_doggy_right_arm_self_finger_ass_animation[Jean.right_hand_Actions[0].mode]"

    if Player.orgasming and focused_Character == Jean:
        "Jean_doggy_left_arm_animation0"
    elif Player.cock_Actions and Jean in Player.cock_Actions[0].Targets:
        "Jean_doggy_left_arm_animation[Player.cock_Actions[0].mode]"
    else:
        "Jean_doggy_left_arm_animation0"

    if Player.orgasming and focused_Character == Jean:
        "Jean_doggy_hair_animation0"
    elif Player.cock_Actions and Jean in Player.cock_Actions[0].Targets:
        "Jean_doggy_hair_animation[Player.cock_Actions[0].mode]"
    else:
        "Jean_doggy_hair_animation0"

    if Jean.psychic:
        "characters/Jean/images/doggy/psychic.webp"

    anchor (int(2101*sex_sampling), int(2097*sex_sampling))
    offset (int(2101*sex_sampling), int(2097*sex_sampling))
    
image Jean_doggy_right_arm:
    "characters/Jean/images/doggy/right_arm.webp"

    anchor (int(2525*sex_sampling), int(1128*sex_sampling))
    offset (int(2525*sex_sampling), int(1128*sex_sampling))
    
layeredimage Jean_doggy_head:
    if Player.orgasming and focused_Character == Jean:
        "Jean_doggy_hair_front_animation0"
    elif Player.cock_Actions and Jean in Player.cock_Actions[0].Targets:
        "Jean_doggy_hair_front_animation[Player.cock_Actions[0].mode]"
    else:
        "Jean_doggy_hair_front_animation0"

    always:
        "characters/Jean/images/doggy/head_[Jean.mouth].webp"

    if Jean.eyes in ["closed", "down", "left", "right", "squint", "up"]:
        "characters/Jean/images/doggy/eyes_[Jean.eyes].webp"
    else:
        "Jean_doggy_blinking"

    always:
        "characters/Jean/images/doggy/brows_[Jean.brows].webp"

    if Jean.blush:
            "characters/Jean/images/doggy/blush[Jean.blush].webp"
        
    if Jean.spunk["tongue"] and Jean.mouth in ["agape", "tongue"]:
        "characters/Jean/images/doggy/spunk_tongue.webp"

    if Jean.spunk["mouth"] and Jean.mouth in ["agape", "tongue"]:
        "characters/Jean/images/doggy/spunk_mouth.webp"
        
    if Jean.spunk["chin"]:
        "characters/Jean/images/doggy/spunk_chin.webp"
        
    if Jean.spunk["face"]:
        "characters/Jean/images/doggy/spunk_face.webp"

    anchor (int(1945*sex_sampling), int(940*sex_sampling))
    offset (int(1945*sex_sampling), int(940*sex_sampling))

layeredimage Jean_doggy_hair_front:
    # if Jean.wet or Jean.Clothes["hair"].string == "wet":
    #     "characters/Jean/images/doggy/hair_front_wet.webp"
    # else:
    always:
        "characters/Jean/images/doggy/hair_front_[Jean.Clothes[hair].string].webp"

    anchor (int(1945*sex_sampling), int(940*sex_sampling))
    offset (int(1945*sex_sampling), int(940*sex_sampling))
    
image Jean_doggy_right_arm_self_finger_ass:
    "characters/Jean/images/doggy/right_arm_finger.webp"

    anchor (int(1474*sex_sampling), int(1200*sex_sampling))
    offset (int(1474*sex_sampling), int(1200*sex_sampling))
    
image Jean_doggy_left_arm:
    "characters/Jean/images/doggy/left_arm.webp"

    anchor (int(1474*sex_sampling), int(1200*sex_sampling))
    offset (int(1474*sex_sampling), int(1200*sex_sampling))

layeredimage Jean_doggy_hair:
    # if Jean.wet or Jean.Clothes["hair"].string == "wet":
    #     "characters/Jean/images/doggy/hair_shadow_wet.webp"
    # else:
    always:
        "characters/Jean/images/doggy/hair_shadow_[Jean.Clothes[hair].string].webp"

    # if Jean.wet or Jean.Clothes["hair"].string == "wet":
    #     "characters/Jean/images/doggy/hair_wet.webp"
    # else:
    always:
        "characters/Jean/images/doggy/hair_[Jean.Clothes[hair].string].webp"

    if Jean.spunk["hair"]:
        "characters/Jean/images/doggy/spunk_hair.webp"

    anchor (int(1945*sex_sampling), int(940*sex_sampling))
    offset (int(1945*sex_sampling), int(940*sex_sampling))

image Jean_doggy_male_body:
    "characters/Jean/images/doggy/male_body_[Player.skin_color].webp"

    anchor (int(2078*sex_sampling), int(3267*sex_sampling))
    offset (int(2078*sex_sampling), int(3267*sex_sampling))

layeredimage Jean_doggy_pussy_closed:
    always:
        "characters/Jean/images/doggy/pussy_closed.webp"

    if Jean.body_hair["pubic"] == "hairy":
        "characters/Jean/images/doggy/pubes_top_hairy_closed.webp"

    anchor (int(2106*sex_sampling), int(3186*sex_sampling))
    offset (int(2106*sex_sampling), int(3186*sex_sampling))

layeredimage Jean_doggy_pussy_open:
    always:
        "characters/Jean/images/doggy/pussy_open.webp"

    if Jean.body_hair["pubic"] == "hairy":
        "characters/Jean/images/doggy/pubes_top_hairy_open.webp"

    anchor (int(2106*sex_sampling), int(3186*sex_sampling))
    offset (int(2106*sex_sampling), int(3186*sex_sampling))

    subpixel True
    transform_anchor True

    xzoom 0.7

layeredimage Jean_doggy_pussy_agape:
    always:
        "characters/Jean/images/doggy/pussy_agape.webp"

    if Jean.body_hair["pubic"] == "hairy":
        "characters/Jean/images/doggy/pubes_top_hairy_agape.webp"

    anchor (int(2102*sex_sampling), int(3144*sex_sampling))
    offset (int(2102*sex_sampling), int(3144*sex_sampling))

image Jean_doggy_anus_closed:
    "characters/Jean/images/doggy/anus_closed.webp"

    anchor (int(2108*sex_sampling), int(2875*sex_sampling))
    offset (int(2108*sex_sampling), int(2875*sex_sampling))

image Jean_doggy_anus_open:
    "characters/Jean/images/doggy/anus_open.webp"

    anchor (int(2108*sex_sampling), int(2875*sex_sampling))
    offset (int(2108*sex_sampling), int(2875*sex_sampling))

image Jean_doggy_anus_agape:
    "characters/Jean/images/doggy/anus_agape.webp"

    anchor (int(2113*sex_sampling), int(2850*sex_sampling))
    offset (int(2113*sex_sampling), int(2850*sex_sampling))

image Jean_doggy_vibrator:
    "characters/Jean/images/doggy/vibrator.webp"

    anchor (int(2105*sex_sampling), int(3169*sex_sampling))
    offset (int(2105*sex_sampling), int(3169*sex_sampling))

layeredimage Jean_doggy_right_forearm_self_finger_ass:
    always:
        "characters/Jean/images/doggy/right_forearm_finger_shadow.webp"

    always:
        "characters/Jean/images/doggy/right_forearm_finger.webp"

    anchor (int(2602*sex_sampling), int(1669*sex_sampling))
    offset (int(2602*sex_sampling), int(1669*sex_sampling))

image Jean_doggy_dildo:
    "characters/Jean/images/doggy/dildo.webp"

    anchor (int(2112*sex_sampling), int(3822*sex_sampling))
    offset (int(2102*sex_sampling), int(3822*sex_sampling))

image Jean_doggy_cock:
    "characters/Jean/images/doggy/cock_[Player.skin_color].webp"

    anchor (int(2078*sex_sampling), int(3267*sex_sampling))
    offset (int(2078*sex_sampling), int(3267*sex_sampling))

image Jean_doggy_spunk_tip:
    "characters/Jean/images/doggy/spunk_tip.webp"

    anchor (int(2078*sex_sampling), int(3267*sex_sampling))
    offset (int(2078*sex_sampling), int(3267*sex_sampling))
        
image Jean_doggy_male_left_arm:
    "characters/Jean/images/doggy/male_left_arm_[Player.skin_color].webp"

    anchor (int(1298*sex_sampling), int(2474*sex_sampling))
    offset (int(1298*sex_sampling), int(2474*sex_sampling))

image Jean_doggy_male_right_arm:
    "characters/Jean/images/doggy/male_right_arm_[Player.skin_color].webp"

    anchor (int(2874*sex_sampling), int(2415*sex_sampling))
    offset (int(2874*sex_sampling), int(2415*sex_sampling))

image Jean_doggy_male_left_arm_finger:
    "characters/Jean/images/doggy/male_left_arm_[Player.skin_color]_finger.webp"

    anchor (int(2111*sex_sampling), int(2055*sex_sampling))
    offset (int(2111*sex_sampling), int(2055*sex_sampling))

layeredimage Jean_doggy_mask_pussy:
    if Player.orgasming == "creampie" and focused_Character == Jean:
        "characters/Jean/images/doggy/mask_pussy.webp"
    elif Jean.vagina_Actions[0].animation_type == "finger_pussy":
        "characters/Jean/images/doggy/mask_pussy_finger.webp"
    elif Jean.vagina_Actions[0].animation_type in ["dildo_pussy", "self_dildo_pussy", "sex"]:
        "characters/Jean/images/doggy/mask_pussy.webp"

    anchor (int(2102*sex_sampling), int(3144*sex_sampling))
    offset (int(2102*sex_sampling), int(3144*sex_sampling))

layeredimage Jean_doggy_mask_anus:
    if Player.orgasming == "anal_creampie" and focused_Character == Jean:
        "characters/Jean/images/doggy/mask_anus.webp"
    elif Jean.anus_Actions[0].animation_type == "finger_ass":
        "characters/Jean/images/doggy/mask_anus_finger.webp"
    elif Jean.anus_Actions[0].animation_type in ["dildo_ass", "self_dildo_ass", "anal"]:
        "characters/Jean/images/doggy/mask_anus.webp"

    anchor (int(2113*sex_sampling), int(2850*sex_sampling))
    offset (int(2113*sex_sampling), int(2850*sex_sampling))

layeredimage Jean_doggy_male_head:
    if Player.body_visible:
        "Player_head"

    if Player.mouth_Actions and Jean in Player.mouth_Actions[0].Targets and Player.mouth_Actions[0].animation_type in ["suck_nipples", "eat_pussy", "eat_ass"]:
        "Jean_doggy_male_tongue_animation[Player.mouth_Actions[0].mode]"

image Jean_doggy_male_tongue:
    "Player_tongue"

image Jean_doggy_left_leg_animation0:
    "Jean_doggy_left_leg"

    doggy_left_leg_animation0

image Jean_doggy_left_leg_animation1:
    "Jean_doggy_left_leg"

    doggy_left_leg_animation1

image Jean_doggy_left_leg_animation2:
    "Jean_doggy_left_leg"

    doggy_left_leg_animation2

image Jean_doggy_right_leg_animation0:
    "Jean_doggy_right_leg"

    doggy_right_leg_animation0

image Jean_doggy_right_leg_animation1:
    "Jean_doggy_right_leg"

    doggy_right_leg_animation1

image Jean_doggy_right_leg_animation2:
    "Jean_doggy_right_leg"

    doggy_right_leg_animation2

image Jean_doggy_right_arm_animation0:
    "Jean_doggy_right_arm"

    doggy_right_arm_animation0

image Jean_doggy_right_arm_animation1:
    "Jean_doggy_right_arm"

    doggy_right_arm_animation1

image Jean_doggy_right_arm_animation2:
    "Jean_doggy_right_arm"

    doggy_right_arm_animation2

image Jean_doggy_hair_front_animation0:
    "Jean_doggy_hair_front"

    doggy_hair_front_animation0

image Jean_doggy_hair_front_animation1:
    "Jean_doggy_hair_front"

    doggy_hair_front_animation1

image Jean_doggy_hair_front_animation2:
    "Jean_doggy_hair_front"

    doggy_hair_front_animation2

image Jean_doggy_head_animation0:
    "Jean_doggy_head"

    doggy_head_animation0

image Jean_doggy_head_animation1:
    "Jean_doggy_head"

    doggy_head_animation1

image Jean_doggy_head_animation2:
    "Jean_doggy_head"

    doggy_head_animation2

image Jean_doggy_torso_animation0:
    "Jean_doggy_torso"

    doggy_torso_animation0

image Jean_doggy_torso_animation1:
    "Jean_doggy_torso"

    doggy_torso_animation1

image Jean_doggy_torso_animation2:
    "Jean_doggy_torso"

    doggy_torso_animation2

image Jean_doggy_right_arm_self_finger_ass_animation0:
    "Jean_doggy_right_arm_self_finger_ass"

    doggy_right_arm_self_finger_ass_animation0

image Jean_doggy_right_arm_self_finger_ass_animation1:
    "Jean_doggy_right_arm_self_finger_ass"

    doggy_right_arm_self_finger_ass_animation1

image Jean_doggy_left_arm_animation0:
    "Jean_doggy_left_arm"

    doggy_left_arm_animation0

image Jean_doggy_left_arm_animation1:
    "Jean_doggy_left_arm"

    doggy_left_arm_animation1

image Jean_doggy_left_arm_animation2:
    "Jean_doggy_left_arm"

    doggy_left_arm_animation2

image Jean_doggy_hair_animation0:
    "Jean_doggy_hair"

    doggy_hair_animation0

image Jean_doggy_hair_animation1:
    "Jean_doggy_hair"

    doggy_hair_animation1

image Jean_doggy_hair_animation2:
    "Jean_doggy_hair"

    doggy_hair_animation2

image Jean_doggy_male_body_grind_pussy_animation0:
    "Jean_doggy_male_body"

    doggy_cock_grind_pussy_animation0

image Jean_doggy_male_body_grind_pussy_animation2:
    "Jean_doggy_male_body"

    doggy_cock_grind_pussy_animation2

image Jean_doggy_male_body_grind_ass_animation0:
    "Jean_doggy_male_body"

    doggy_cock_grind_ass_animation0

image Jean_doggy_male_body_grind_ass_animation2:
    "Jean_doggy_male_body"

    doggy_cock_grind_ass_animation2

image Jean_doggy_male_body_sex_animation0:
    "Jean_doggy_male_body"

    doggy_cock_sex_animation0

image Jean_doggy_male_body_sex_animation1:
    "Jean_doggy_male_body"

    doggy_cock_sex_animation1

image Jean_doggy_male_body_sex_animation2:
    "Jean_doggy_male_body"

    doggy_cock_sex_animation2

image Jean_doggy_male_body_anal_animation0:
    "Jean_doggy_male_body"

    doggy_cock_anal_animation0

image Jean_doggy_male_body_anal_animation1:
    "Jean_doggy_male_body"

    doggy_cock_anal_animation1

image Jean_doggy_male_body_anal_animation2:
    "Jean_doggy_male_body"

    doggy_cock_anal_animation2

image Jean_doggy_ass_animation0:
    "Jean_doggy_ass"

    doggy_ass_animation0

image Jean_doggy_ass_animation1:
    "Jean_doggy_ass"

    doggy_ass_animation1

image Jean_doggy_ass_animation2:
    "Jean_doggy_ass"

    doggy_ass_animation2

image Jean_doggy_pussy_finger_pussy_animation0:
    "Jean_doggy_pussy_closed"

    doggy_pussy_finger_pussy_animation0

image Jean_doggy_pussy_finger_pussy_animation1:
    "Jean_doggy_pussy_open"

    doggy_pussy_finger_pussy_animation1

image Jean_doggy_anus_finger_ass_animation0:
    "Jean_doggy_anus_closed"

    doggy_anus_finger_ass_animation0

image Jean_doggy_anus_finger_ass_animation1:
    "Jean_doggy_anus_open"

    doggy_anus_finger_ass_animation1

image Jean_doggy_pussy_sex_animation0:
    "Jean_doggy_pussy_closed"

    doggy_pussy_sex_animation0

image Jean_doggy_pussy_sex_animation1:
    "Jean_doggy_pussy_agape"

    doggy_pussy_sex_animation1

image Jean_doggy_pussy_sex_animation2:
    "Jean_doggy_pussy_agape"

    doggy_pussy_sex_animation2

image Jean_doggy_anus_anal_animation0:
    "Jean_doggy_anus_closed"

    doggy_anus_anal_animation0

image Jean_doggy_anus_anal_animation1:
    "Jean_doggy_anus_agape"

    doggy_anus_anal_animation1

image Jean_doggy_anus_anal_animation2:
    "Jean_doggy_anus_agape"

    doggy_anus_anal_animation2

image Jean_doggy_pussy_grind_pussy_animation0:
    "Jean_doggy_pussy_closed"

    doggy_pussy_grind_pussy_animation0

image Jean_doggy_pussy_grind_pussy_animation2:
    "Jean_doggy_pussy_open"

    doggy_pussy_grind_pussy_animation2

image Jean_doggy_anus_grind_ass_animation0:
    "Jean_doggy_anus_closed"

    doggy_anus_grind_ass_animation0

image Jean_doggy_anus_grind_ass_animation2:
    "Jean_doggy_anus_open"

    doggy_anus_grind_ass_animation2

image Jean_doggy_pussy_dildo_pussy_animation0:
    "Jean_doggy_pussy_closed"

    doggy_pussy_dildo_pussy_animation0

image Jean_doggy_pussy_dildo_pussy_animation1:
    "Jean_doggy_pussy_agape"

    doggy_pussy_dildo_pussy_animation1

image Jean_doggy_anus_dildo_ass_animation0:
    "Jean_doggy_anus_closed"

    doggy_anus_dildo_ass_animation0

image Jean_doggy_anus_dildo_ass_animation1:
    "Jean_doggy_anus_agape"

    doggy_anus_dildo_ass_animation1

image Jean_doggy_cock_sex_animation0:
    "Jean_doggy_cock"

    doggy_cock_sex_animation0

image Jean_doggy_cock_sex_animation1:
    "Jean_doggy_cock"

    doggy_cock_sex_animation1

image Jean_doggy_cock_sex_animation2:
    "Jean_doggy_cock"

    doggy_cock_sex_animation2

image Jean_doggy_cock_anal_animation0:
    "Jean_doggy_cock"

    doggy_cock_anal_animation0

image Jean_doggy_cock_anal_animation1:
    "Jean_doggy_cock"

    doggy_cock_anal_animation1

image Jean_doggy_cock_anal_animation2:
    "Jean_doggy_cock"

    doggy_cock_anal_animation2

image Jean_doggy_cock_grind_pussy_animation0:
    "Jean_doggy_cock"

    doggy_cock_grind_pussy_animation0

image Jean_doggy_cock_grind_pussy_animation2:
    "Jean_doggy_cock"

    doggy_cock_grind_pussy_animation2

image Jean_doggy_cock_grind_ass_animation0:
    "Jean_doggy_cock"

    doggy_cock_grind_ass_animation0

image Jean_doggy_cock_grind_ass_animation2:
    "Jean_doggy_cock"

    doggy_cock_grind_ass_animation2

image Jean_doggy_spunk_tip_sex_animation0:
    "Jean_doggy_spunk_tip"

    doggy_cock_sex_animation0

image Jean_doggy_spunk_tip_sex_animation1:
    "Jean_doggy_spunk_tip"

    doggy_cock_sex_animation1

image Jean_doggy_spunk_tip_sex_animation2:
    "Jean_doggy_spunk_tip"

    doggy_cock_sex_animation2

image Jean_doggy_spunk_tip_anal_animation0:
    "Jean_doggy_spunk_tip"

    doggy_cock_anal_animation0

image Jean_doggy_spunk_tip_anal_animation1:
    "Jean_doggy_spunk_tip"

    doggy_cock_anal_animation1

image Jean_doggy_spunk_tip_anal_animation2:
    "Jean_doggy_spunk_tip"

    doggy_cock_anal_animation2

image Jean_doggy_spunk_tip_grind_pussy_animation0:
    "Jean_doggy_spunk_tip"

    doggy_cock_grind_pussy_animation0

image Jean_doggy_spunk_tip_grind_pussy_animation2:
    "Jean_doggy_spunk_tip"

    doggy_cock_grind_pussy_animation2

image Jean_doggy_spunk_tip_grind_ass_animation0:
    "Jean_doggy_spunk_tip"

    doggy_cock_grind_ass_animation0

image Jean_doggy_spunk_tip_grind_ass_animation2:
    "Jean_doggy_spunk_tip"

    doggy_cock_grind_ass_animation2
    
image Jean_doggy_vibrator_animation0:
    "Jean_doggy_vibrator"

    doggy_vibrator_animation0
    
image Jean_doggy_vibrator_animation1:
    "Jean_doggy_vibrator"

    doggy_vibrator_animation1
    
image Jean_doggy_dildo_pussy_animation0:
    "Jean_doggy_dildo"

    doggy_dildo_pussy_animation0
    
image Jean_doggy_dildo_pussy_animation1:
    "Jean_doggy_dildo"

    doggy_dildo_pussy_animation1
    
image Jean_doggy_dildo_ass_animation0:
    "Jean_doggy_dildo"

    doggy_dildo_ass_animation0
    
image Jean_doggy_dildo_ass_animation1:
    "Jean_doggy_dildo"

    doggy_dildo_ass_animation1

image Jean_doggy_male_left_arm_animation0:
    "Jean_doggy_male_left_arm"

    doggy_male_left_arm_animation0

image Jean_doggy_male_left_arm_animation1:
    "Jean_doggy_male_left_arm"

    doggy_male_left_arm_animation1

image Jean_doggy_male_left_arm_animation2:
    "Jean_doggy_male_left_arm"

    doggy_male_left_arm_animation2

image Jean_doggy_male_right_arm_animation0:
    "Jean_doggy_male_right_arm"

    doggy_male_right_arm_animation0

image Jean_doggy_male_right_arm_animation1:
    "Jean_doggy_male_right_arm"

    doggy_male_right_arm_animation1

image Jean_doggy_male_right_arm_animation2:
    "Jean_doggy_male_right_arm"

    doggy_male_right_arm_animation2

image Jean_doggy_male_left_arm_finger_pussy_animation0:
    "Jean_doggy_male_left_arm_finger"

    doggy_male_left_arm_finger_pussy_animation0

image Jean_doggy_male_left_arm_finger_pussy_animation1:
    "Jean_doggy_male_left_arm_finger"

    doggy_male_left_arm_finger_pussy_animation1

image Jean_doggy_male_left_arm_finger_ass_animation1:
    "Jean_doggy_male_left_arm_finger"

    doggy_male_left_arm_finger_ass_animation1

image Jean_doggy_right_forearm_self_finger_ass_animation0:
    "Jean_doggy_right_forearm_self_finger_ass"

    doggy_right_forearm_self_finger_ass_animation0

image Jean_doggy_right_forearm_self_finger_ass_animation1:
    "Jean_doggy_right_forearm_self_finger_ass"

    doggy_right_forearm_self_finger_ass_animation1

image Jean_doggy_mask_finger_pussy_animation0:
    "Jean_doggy_mask_pussy"

    doggy_mask_finger_pussy_animation0

image Jean_doggy_mask_finger_pussy_animation1:
    "Jean_doggy_mask_pussy"

    doggy_mask_finger_pussy_animation1

image Jean_doggy_mask_finger_ass_animation0:
    "Jean_doggy_mask_anus"

    doggy_mask_finger_ass_animation0

image Jean_doggy_mask_finger_ass_animation1:
    "Jean_doggy_mask_anus"

    doggy_mask_finger_ass_animation1

image Jean_doggy_mask_sex_animation0:
    "Jean_doggy_mask_pussy"

    doggy_mask_sex_animation0

image Jean_doggy_mask_sex_animation1:
    "Jean_doggy_mask_pussy"

    doggy_mask_sex_animation1

image Jean_doggy_mask_sex_animation2:
    "Jean_doggy_mask_pussy"

    doggy_mask_sex_animation2

image Jean_doggy_mask_anal_animation0:
    "Jean_doggy_mask_anus"

    doggy_mask_anal_animation0

image Jean_doggy_mask_anal_animation1:
    "Jean_doggy_mask_anus"

    doggy_mask_anal_animation1

image Jean_doggy_mask_anal_animation2:
    "Jean_doggy_mask_anus"

    doggy_mask_anal_animation2

image Jean_doggy_mask_dildo_pussy_animation0:
    "Jean_doggy_mask_pussy"

    doggy_mask_dildo_pussy_animation0

image Jean_doggy_mask_dildo_pussy_animation1:
    "Jean_doggy_mask_pussy"

    doggy_mask_dildo_pussy_animation1

image Jean_doggy_mask_dildo_ass_animation0:
    "Jean_doggy_mask_anus"

    doggy_mask_dildo_ass_animation0

image Jean_doggy_mask_dildo_ass_animation1:
    "Jean_doggy_mask_anus"

    doggy_mask_dildo_ass_animation1
    
image Jean_doggy_male_head_eat_pussy_animation0:
    "Jean_doggy_male_head"

    doggy_male_head_eat_pussy_animation0
    
image Jean_doggy_male_head_eat_pussy_animation1:
    "Jean_doggy_male_head"

    doggy_male_head_eat_pussy_animation1
    
image Jean_doggy_male_head_eat_ass_animation0:
    "Jean_doggy_male_head"

    doggy_male_head_eat_ass_animation0
    
image Jean_doggy_male_head_eat_ass_animation1:
    "Jean_doggy_male_head"

    doggy_male_head_eat_ass_animation1
    
image Jean_doggy_male_tongue_animation0:
    "Jean_doggy_male_tongue"

    doggy_male_tongue_animation0
    
image Jean_doggy_male_tongue_animation1:
    "Jean_doggy_male_tongue"

    doggy_male_tongue_animation1

image Jean_doggy_male_body_cumshot_animation:
    "Jean_doggy_male_body"

    doggy_cock_cumshot_animation

image Jean_doggy_male_body_creampie_animation:
    "Jean_doggy_male_body"

    doggy_cock_creampie_animation

image Jean_doggy_male_body_anal_creampie_animation:
    "Jean_doggy_male_body"

    doggy_cock_anal_creampie_animation

image Jean_doggy_cock_cumshot_animation:
    "Jean_doggy_cock"

    doggy_cock_cumshot_animation

image Jean_doggy_cock_creampie_animation:
    "Jean_doggy_cock"

    doggy_cock_creampie_animation

image Jean_doggy_cock_anal_creampie_animation:
    "Jean_doggy_cock"

    doggy_cock_anal_creampie_animation

image Jean_doggy_spunk_tip_cumshot_animation:
    "Jean_doggy_spunk_tip"

    doggy_cock_cumshot_animation

image Jean_doggy_spunk_tip_creampie_animation:
    "Jean_doggy_spunk_tip"

    doggy_cock_creampie_animation

image Jean_doggy_spunk_tip_anal_creampie_animation:
    "Jean_doggy_spunk_tip"

    doggy_cock_anal_creampie_animation

image Jean_doggy_pussy_creampie_animation:
    "Jean_doggy_pussy_agape"

    doggy_pussy_creampie_animation

image Jean_doggy_anus_anal_creampie_animation:
    "Jean_doggy_anus_agape"

    doggy_anus_anal_creampie_animation

image Jean_doggy_mask_creampie_animation:
    "Jean_doggy_mask_pussy"

    doggy_mask_creampie_animation

image Jean_doggy_mask_anal_creampie_animation:
    "Jean_doggy_mask_anus"

    doggy_mask_anal_creampie_animation

layeredimage Jean_doggy_cock_animations:
    if Player.orgasming and focused_Character == Jean:
        "Jean_doggy_cock_[Player.orgasming]_animation"
    else:
        "Jean_doggy_cock_[Player.cock_Actions[0].animation_type]_animation[Player.cock_Actions[0].mode]"

    if not Player.spunk and not Player.orgasming:
        Null()
    elif Player.orgasming and focused_Character == Jean:
        "Jean_doggy_spunk_tip_[Player.orgasming]_animation"
    else:
        "Jean_doggy_spunk_tip_[Player.cock_Actions[0].animation_type]_animation[Player.cock_Actions[0].mode]"

layeredimage Jean_doggy_male_left_arm_finger_animations:
    always:
        "Jean_doggy_male_left_arm_[Player.left_hand_Actions[0].animation_type]_animation[Player.left_hand_Actions[0].mode]"

layeredimage Jean_doggy_dildo_pussy_animations:
    always:
        "Jean_doggy_dildo_pussy_animation[Jean.vagina_Actions[0].mode]"

layeredimage Jean_doggy_dildo_ass_animations:
    always:
        "Jean_doggy_dildo_ass_animation[Jean.anus_Actions[0].mode]"

layeredimage Jean_doggy_mask_pussy_animations:
    if Player.orgasming == "creampie" and focused_Character == Jean:
        "Jean_doggy_mask_creampie_animation"
    elif Jean.vagina_Actions[0].animation_type in ["dildo_pussy", "self_dildo_pussy"]:
        "Jean_doggy_mask_dildo_pussy_animation[Jean.vagina_Actions[0].mode]"
    else:
        "Jean_doggy_mask_[Jean.vagina_Actions[0].animation_type]_animation[Jean.vagina_Actions[0].mode]"

layeredimage Jean_doggy_mask_anus_animations:
    if Player.orgasming == "anal_creampie" and focused_Character == Jean:
        "Jean_doggy_mask_anal_creampie_animation"
    elif Jean.anus_Actions[0].animation_type in ["dildo_ass", "self_dildo_ass"]:
        "Jean_doggy_mask_dildo_ass_animation[Jean.anus_Actions[0].mode]"
    else:
        "Jean_doggy_mask_[Jean.anus_Actions[0].animation_type]_animation[Jean.anus_Actions[0].mode]"

image Jean_doggy_blinking:
    "characters/Jean/images/doggy/eyes_[Jean.eyes].webp"
    choice:
        4.5
    choice:
        4.0
    choice:
        3.5
    "characters/Jean/images/doggy/eyes_blink1.webp"
    0.023
    "characters/Jean/images/doggy/eyes_blink2.webp"
    0.023
    "characters/Jean/images/doggy/eyes_closed.webp"
    0.054
    "characters/Jean/images/doggy/eyes_blink2.webp"
    0.018
    "characters/Jean/images/doggy/eyes_blink1.webp"
    0.072
    repeat

image Jean_doggy_cumshot:
    "characters/Jean/images/doggy/spunk_jet.webp"

    subpixel True
    transform_anchor True

    anchor (int(2053*sex_sampling), int(2144*sex_sampling))
    offset (int(2053*sex_sampling), int(2144*sex_sampling))
    pos (0.006*sex_sampling/0.38, 0.2*sex_sampling/0.38)

    parallel:
        ease 1.25 ypos 0.2*sex_sampling/0.38
        ease 1.75 ypos 0.2*sex_sampling/0.38
        pause 1.5
        repeat
    parallel:
        yzoom 0.0 alpha 1.0
        easein_cubic 0.2 yzoom 1.0 alpha 0.5
        linear 0.1 alpha 0.0
        pause 1.0
        repeat

image Jean_doggy_creampie:
    "characters/Jean/images/doggy/creampie_pussy_agape.webp"

    anchor (int(2102*sex_sampling), int(3144*sex_sampling))
    offset (int(2102*sex_sampling), int(3144*sex_sampling))

    subpixel True
    transform_anchor True

    yzoom 0.5

    block:
        xzoom 0.0 alpha 1.0
        easein_cubic 0.2 xzoom 1.5 alpha 0.5
        linear 0.1 alpha 0.0
        pause 1.0

        repeat

image Jean_doggy_anal_creampie:
    "characters/Jean/images/doggy/creampie_anus_agape.webp"

    anchor (int(2113*sex_sampling), int(2850*sex_sampling))
    offset (int(2113*sex_sampling), int(2850*sex_sampling))

    subpixel True
    transform_anchor True

    yzoom 0.5

    block:
        xzoom 0.0 alpha 1.0
        easein_cubic 0.2 xzoom 1.5 alpha 0.5
        linear 0.1 alpha 0.0
        pause 1.0

        repeat