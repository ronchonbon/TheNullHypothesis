# image Rogue_missionary = Live2D("characters/Rogue/images/missionary/Rogue_missionary.model3.json", loop = True, default_fade = 0.0)

# image 2_x3_male_knees_green_sex = renpy.displayable("Rogue_missionary 2_x3_male_knees_green_sex")
# image 2_x3_base = renpy.displayable("Rogue_missionary 2_x3_base")
# image 2_x3_cock_green_sex = renpy.displayable("Rogue_missionary 2_x3_cock_green_sex")

# layeredimage Rogue_missionary layered:
#     # always:
#     #     "2_x3_right_arm"

#     always:
#         "2_x3_male_knees_green_sex"

#     always:
#         "2_x3_base"

#     # always:
#     #     "2_x3_mouth_happy"

#     # always:
#     #     "2_x3_eyes_neutral"

#     # always:
#     #     "2_x3_brows_neutral"

#     # always:
#     #     "2_x3_anus_sex"

#     # always:
#     #     "2_x3_pussy_sex"

#     # always:
#     #     "2_x3_male_body"

#     # always:
#     #     AlphaMask("2_x3_cock_green_sex", "2_x3_mask_sex")

image Rogue_sprite missionary:
    contains:
        "Rogue_missionary_temp"

    offset (int(300*0.38), int(300*0.38))
            
layeredimage Rogue_missionary_temp:
    if Rogue.hovered:
        At("Rogue_missionary_controls_temp", hover)
    else:
        "Rogue_missionary_controls_temp"
            
layeredimage Rogue_missionary_controls_temp:
    if speed > 2.5 or speed <= 1.75:
        Null()
    elif intensity >= 2.0:
        At(At("Rogue_missionary", speed_200), intensity_200)
    elif intensity >= 1.75:
        At(At("Rogue_missionary", speed_200), intensity_175)
    elif intensity >= 1.5:
        At(At("Rogue_missionary", speed_200), intensity_150)
    elif intensity >= 1.25:
        At(At("Rogue_missionary", speed_200), intensity_125)
    elif intensity >= 1.0:
        At(At("Rogue_missionary", speed_200), intensity_100)
    elif intensity >= 0.75:
        At(At("Rogue_missionary", speed_200), intensity_075)
    elif intensity >= 0.5:
        At(At("Rogue_missionary", speed_200), intensity_050)
    elif intensity >= 0.25:
        At(At("Rogue_missionary", speed_200), intensity_025)
    else:
        At(At("Rogue_missionary", speed_200), intensity_000)

    if speed > 1.75 or speed <= 1.5:
        Null()
    elif intensity >= 2.0:
        At(At("Rogue_missionary", speed_175), intensity_200)
    elif intensity >= 1.75:
        At(At("Rogue_missionary", speed_175), intensity_175)
    elif intensity >= 1.5:
        At(At("Rogue_missionary", speed_175), intensity_150)
    elif intensity >= 1.25:
        At(At("Rogue_missionary", speed_175), intensity_125)
    elif intensity >= 1.0:
        At(At("Rogue_missionary", speed_175), intensity_100)
    elif intensity >= 0.75:
        At(At("Rogue_missionary", speed_175), intensity_075)
    elif intensity >= 0.5:
        At(At("Rogue_missionary", speed_175), intensity_050)
    elif intensity >= 0.25:
        At(At("Rogue_missionary", speed_175), intensity_025)
    else:
        At(At("Rogue_missionary", speed_175), intensity_000)

    if speed > 1.5 or speed <= 1.25:
        Null()
    elif intensity >= 2.0:
        At(At("Rogue_missionary", speed_150), intensity_200)
    elif intensity >= 1.75:
        At(At("Rogue_missionary", speed_150), intensity_175)
    elif intensity >= 1.5:
        At(At("Rogue_missionary", speed_150), intensity_150)
    elif intensity >= 1.25:
        At(At("Rogue_missionary", speed_150), intensity_125)
    elif intensity >= 1.0:
        At(At("Rogue_missionary", speed_150), intensity_100)
    elif intensity >= 0.75:
        At(At("Rogue_missionary", speed_150), intensity_075)
    elif intensity >= 0.5:
        At(At("Rogue_missionary", speed_150), intensity_050)
    elif intensity >= 0.25:
        At(At("Rogue_missionary", speed_150), intensity_025)
    else:
        At(At("Rogue_missionary", speed_150), intensity_000)
 
    if speed > 1.25 or speed <= 1.0:
        Null()
    elif intensity >= 2.0:
        At(At("Rogue_missionary", speed_125), intensity_200)
    elif intensity >= 1.75:
        At(At("Rogue_missionary", speed_125), intensity_175)
    elif intensity >= 1.5:
        At(At("Rogue_missionary", speed_125), intensity_150)
    elif intensity >= 1.25:
        At(At("Rogue_missionary", speed_125), intensity_125)
    elif intensity >= 1.0:
        At(At("Rogue_missionary", speed_125), intensity_100)
    elif intensity >= 0.75:
        At(At("Rogue_missionary", speed_125), intensity_075)
    elif intensity >= 0.5:
        At(At("Rogue_missionary", speed_125), intensity_050)
    elif intensity >= 0.25:
        At(At("Rogue_missionary", speed_125), intensity_025)
    else:
        At(At("Rogue_missionary", speed_125), intensity_000)
 
    if speed > 1.0 or speed <= 0.75:
        Null()
    elif intensity >= 2.0:
        At(At("Rogue_missionary", speed_100), intensity_200)
    elif intensity >= 1.75:
        At(At("Rogue_missionary", speed_100), intensity_175)
    elif intensity >= 1.5:
        At(At("Rogue_missionary", speed_100), intensity_150)
    elif intensity >= 1.25:
        At(At("Rogue_missionary", speed_100), intensity_125)
    elif intensity >= 1.0:
        At(At("Rogue_missionary", speed_100), intensity_100)
    elif intensity >= 0.75:
        At(At("Rogue_missionary", speed_100), intensity_075)
    elif intensity >= 0.5:
        At(At("Rogue_missionary", speed_100), intensity_050)
    elif intensity >= 0.25:
        At(At("Rogue_missionary", speed_100), intensity_025)
    else:
        At(At("Rogue_missionary", speed_100), intensity_000)

    if speed > 0.75 or speed <= 0.5:
        Null()
    elif intensity >= 2.0:
        At(At("Rogue_missionary", speed_075), intensity_200)
    elif intensity >= 1.75:
        At(At("Rogue_missionary", speed_075), intensity_175)
    elif intensity >= 1.5:
        At(At("Rogue_missionary", speed_075), intensity_150)
    elif intensity >= 1.25:
        At(At("Rogue_missionary", speed_075), intensity_125)
    elif intensity >= 1.0:
        At(At("Rogue_missionary", speed_075), intensity_100)
    elif intensity >= 0.75:
        At(At("Rogue_missionary", speed_075), intensity_075)
    elif intensity >= 0.5:
        At(At("Rogue_missionary", speed_075), intensity_050)
    elif intensity >= 0.25:
        At(At("Rogue_missionary", speed_075), intensity_025)
    else:
        At(At("Rogue_missionary", speed_075), intensity_000)

    if speed > 0.5 or speed <= 0.25:
        Null()
    elif intensity >= 2.0:
        At(At("Rogue_missionary", speed_050), intensity_200)
    elif intensity >= 1.75:
        At(At("Rogue_missionary", speed_050), intensity_175)
    elif intensity >= 1.5:
        At(At("Rogue_missionary", speed_050), intensity_150)
    elif intensity >= 1.25:
        At(At("Rogue_missionary", speed_050), intensity_125)
    elif intensity >= 1.0:
        At(At("Rogue_missionary", speed_050), intensity_100)
    elif intensity >= 0.75:
        At(At("Rogue_missionary", speed_050), intensity_075)
    elif intensity >= 0.5:
        At(At("Rogue_missionary", speed_050), intensity_050)
    elif intensity >= 0.25:
        At(At("Rogue_missionary", speed_050), intensity_025)
    else:
        At(At("Rogue_missionary", speed_050), intensity_000)

    if speed > 0.25 or speed <= 0.01:
        Null()
    elif intensity >= 2.0:
        At(At("Rogue_missionary", speed_025), intensity_200)
    elif intensity >= 1.75:
        At(At("Rogue_missionary", speed_025), intensity_175)
    elif intensity >= 1.5:
        At(At("Rogue_missionary", speed_025), intensity_150)
    elif intensity >= 1.25:
        At(At("Rogue_missionary", speed_025), intensity_125)
    elif intensity >= 1.0:
        At(At("Rogue_missionary", speed_025), intensity_100)
    elif intensity >= 0.75:
        At(At("Rogue_missionary", speed_025), intensity_075)
    elif intensity >= 0.5:
        At(At("Rogue_missionary", speed_025), intensity_050)
    elif intensity >= 0.25:
        At(At("Rogue_missionary", speed_025), intensity_025)
    else:
        At(At("Rogue_missionary", speed_025), intensity_000)

    if speed != 0.01:
        Null()
    elif intensity >= 2.0:
        At(At("Rogue_missionary", speed_0001), intensity_200)
    elif intensity >= 1.75:
        At(At("Rogue_missionary", speed_0001), intensity_175)
    elif intensity >= 1.5:
        At(At("Rogue_missionary", speed_0001), intensity_150)
    elif intensity >= 1.25:
        At(At("Rogue_missionary", speed_0001), intensity_125)
    elif intensity >= 1.0:
        At(At("Rogue_missionary", speed_0001), intensity_100)
    elif intensity >= 0.75:
        At(At("Rogue_missionary", speed_0001), intensity_075)
    elif intensity >= 0.5:
        At(At("Rogue_missionary", speed_0001), intensity_050)
    elif intensity >= 0.25:
        At(At("Rogue_missionary", speed_0001), intensity_025)
    else:
        At(At("Rogue_missionary", speed_0001), intensity_000)

    if speed >= 0.01 or speed < 0.0:
        Null()
    elif intensity >= 2.0:
        At(At("Rogue_missionary", speed_000), intensity_200)
    elif intensity >= 1.75:
        At(At("Rogue_missionary", speed_000), intensity_175)
    elif intensity >= 1.5:
        At(At("Rogue_missionary", speed_000), intensity_150)
    elif intensity >= 1.25:
        At(At("Rogue_missionary", speed_000), intensity_125)
    elif intensity >= 1.0:
        At(At("Rogue_missionary", speed_000), intensity_100)
    elif intensity >= 0.75:
        At(At("Rogue_missionary", speed_000), intensity_075)
    elif intensity >= 0.5:
        At(At("Rogue_missionary", speed_000), intensity_050)
    elif intensity >= 0.25:
        At(At("Rogue_missionary", speed_000), intensity_025)
    else:
        At(At("Rogue_missionary", speed_000), intensity_000)
 
layeredimage Rogue_missionary:
    if Player.orgasming and focused_Character == Rogue:
        "Rogue_missionary_thighs_animation0"
    elif Player.cock_Actions and Rogue in Player.cock_Actions[0].Targets:
        "Rogue_missionary_thighs_animation[Player.cock_Actions[0].mode]"
    else:
        "Rogue_missionary_thighs_animation0"
    
layeredimage Rogue_missionary_thighs:
    if Player.orgasming and focused_Character == Rogue:
        "Rogue_missionary_torso_animation0"
    elif Player.cock_Actions and Rogue in Player.cock_Actions[0].Targets and Rogue.orgasming:
        At("Rogue_missionary_torso_animation[Player.cock_Actions[0].mode]", tremble(20))
    elif Player.cock_Actions and Rogue in Player.cock_Actions[0].Targets:
        "Rogue_missionary_torso_animation[Player.cock_Actions[0].mode]"
    elif Rogue.orgasming:
        At("Rogue_missionary_torso_animation0", tremble(20))
    else:
        "Rogue_missionary_torso_animation0"

    always:
        "characters/Rogue/images/missionary/thighs.webp"

    if Player.orgasming == "anal_creampie" and focused_Character == Rogue:
        "Rogue_missionary_anus_anal_creampie_animation"
    elif not Rogue.anus_Actions:
        "Rogue_missionary_anus_closed"
    elif Rogue.anus_Actions[0].animation_type == "eat_ass":
        "Rogue_missionary_anus_open"
    elif Rogue.anus_Actions[0].animation_type in ["dildo_ass", "self_dildo_ass"]:
        "Rogue_missionary_anus_dildo_ass_animation[Rogue.anus_Actions[0].mode]"
    elif Rogue.anus_Actions[0].animation_type == "finger_ass":
        "Rogue_missionary_anus_finger_ass_animation[Rogue.anus_Actions[0].mode]"
    elif Player.orgasming and focused_Character == Rogue:
        "Rogue_missionary_anus_closed"
    else:
        "Rogue_missionary_anus_[Rogue.anus_Actions[0].animation_type]_animation[Rogue.anus_Actions[0].mode]"

    if Player.orgasming == "creampie" and focused_Character == Rogue:
        "Rogue_missionary_pussy_creampie_animation"
    elif Rogue.vagina_Actions and Rogue.vagina_Actions[0].animation_type in ["dildo_pussy", "self_dildo_pussy"]:
        "Rogue_missionary_pussy_dildo_pussy_animation[Rogue.vagina_Actions[0].mode]"
    elif Rogue.vagina_Actions and Rogue.vagina_Actions[0].animation_type in ["finger_pussy", "self_touch_pussy"]:
        "Rogue_missionary_pussy_[Rogue.vagina_Actions[0].animation_type]_animation[Rogue.vagina_Actions[0].mode]"
    elif Player.orgasming and focused_Character == Rogue:
        "Rogue_missionary_pussy_closed"
    elif Rogue.vagina_Actions:
        "Rogue_missionary_pussy_[Rogue.vagina_Actions[0].animation_type]_animation[Rogue.vagina_Actions[0].mode]"
    elif Rogue.clitoris_Actions:
        "Rogue_missionary_pussy_closed"
    else:
        "Rogue_missionary_pussy_closed"

    if Rogue.tan_lines["bottom"]:
        "characters/Rogue/images/missionary/tan_lines_[Rogue.tan_lines[bottom]].webp"

    if Rogue.tan_lines["full"]:
        "characters/Rogue/images/missionary/tan_lines_[Rogue.tan_lines[full]]_thighs.webp"

    if Player.orgasming == "anal_creampie" and focused_Character == Rogue:
        "Rogue_missionary_anal_creampie"
    elif not Rogue.creampie["anus"]:
        Null()
    elif Rogue.anus_Actions and Rogue.anus_Actions[0].animation_type == "eat_ass":
        "characters/Rogue/images/missionary/creampie_anus_open.webp"
    elif Rogue.anus_Actions:
        "characters/Rogue/images/missionary/creampie_anus_agape.webp"
    else:
        "characters/Rogue/images/missionary/creampie_anus_closed.webp"

    if not Rogue.buttplug:
        Null()
    elif Rogue.buttplug.string == "heart_anal_plug":
        "characters/Rogue/images/missionary/buttplug_heart.webp"
    elif Rogue.buttplug.string == "round_anal_plug":
        "characters/Rogue/images/missionary/buttplug_round.webp"

    if Rogue.anus_Actions and Rogue.anus_Actions[0].animation_type in ["dildo_ass", "self_dildo_ass"]:
        AlphaMask("Rogue_missionary_dildo_ass_animations", "Rogue_missionary_mask_anus_animations")

    if not Player.body_visible:
        Null()
    elif Player.orgasming and focused_Character == Rogue:
        "Rogue_missionary_male_body_[Player.orgasming]_animation"
    elif Player.cock_Actions and Rogue in Player.cock_Actions[0].Targets:
        "Rogue_missionary_male_body_[Player.cock_Actions[0].animation_type]_animation[Player.cock_Actions[0].mode]"

    if Player.orgasming == "creampie" and focused_Character == Rogue:
        "Rogue_missionary_creampie"
    elif not Rogue.creampie["pussy"]:
        Null()
    elif Rogue.vagina_Actions:
        "characters/Rogue/images/missionary/creampie_pussy_agape.webp"
    elif Rogue.clitoris_Actions:
        "characters/Rogue/images/missionary/creampie_pussy_open.webp"
    else:
        "characters/Rogue/images/missionary/creampie_pussy_closed.webp"

    if Rogue.piercings["labia"] in ["barbell", "both"]:
        "characters/Rogue/images/missionary/labia_piercings_barbell.webp"

    if Rogue.piercings["labia"] in ["ring", "both"]:
        "characters/Rogue/images/missionary/labia_piercings_ring.webp"

    if "pubic" in Rogue.body_hair_growing.keys():
        "characters/Rogue/images/missionary/pubes_growing.webp"

    if not Rogue.body_hair["pubic"]:
        Null()
    elif "triangle" in Rogue.body_hair["pubic"]:
        "characters/Rogue/images/missionary/pubes_triangle.webp"
    elif "strip" in Rogue.body_hair["pubic"]:
        "characters/Rogue/images/missionary/pubes_strip.webp"
    else:
        "characters/Rogue/images/missionary/pubes_[Rogue.body_hair[pubic]].webp"

    if Rogue.remote_vibrator is not None:
        "characters/Rogue/images/missionary/remote_vibrator.webp"

    if Player.orgasming and focused_Character == Rogue:
        Null()
    elif not Rogue.anus_Actions or Rogue.anus_Actions[0].animation_type != "finger_ass":
        Null()
    elif Player.left_hand_Actions and Rogue in Player.left_hand_Actions[0].Targets and Player.left_hand_Actions[0].animation_type == "finger_ass":
        AlphaMask("Rogue_missionary_male_left_arm_finger_animations", "Rogue_missionary_mask_anus_animations")
    elif Player.right_hand_Actions and Rogue in Player.right_hand_Actions[0].Targets and Player.right_hand_Actions[0].animation_type == "finger_ass":
        AlphaMask("Rogue_missionary_male_right_arm_finger_animations", "Rogue_missionary_mask_anus_animations")

    if Player.orgasming == "anal_creampie" and focused_Character == Rogue:
        AlphaMask("Rogue_missionary_cock_animations", "Rogue_missionary_mask_anus_animations")
    elif Player.orgasming and focused_Character == Rogue:
        Null()
    elif Player.cock_Actions and Rogue in Player.cock_Actions[0].Targets and Player.cock_Actions[0].animation_type == "anal":
        AlphaMask("Rogue_missionary_cock_animations", "Rogue_missionary_mask_anus_animations")

    if Player.orgasming and focused_Character == Rogue:
        Null()
    elif not Rogue.vagina_Actions or Rogue.vagina_Actions[0].animation_type != "finger_pussy":
        Null()
    elif Player.left_hand_Actions and Rogue in Player.left_hand_Actions[0].Targets and Player.left_hand_Actions[0].animation_type == "finger_pussy":
        AlphaMask("Rogue_missionary_male_left_arm_finger_animations", "Rogue_missionary_mask_pussy_animations")
    elif Player.right_hand_Actions and Rogue in Player.right_hand_Actions[0].Targets and Player.right_hand_Actions[0].animation_type == "finger_pussy":
        AlphaMask("Rogue_missionary_male_right_arm_finger_animations", "Rogue_missionary_mask_pussy_animations")

    if Rogue.vagina_Actions and Rogue.vagina_Actions[0].animation_type in ["dildo_pussy", "self_dildo_pussy"]:
        AlphaMask("Rogue_missionary_dildo_pussy_animations", "Rogue_missionary_mask_pussy_animations")

    if Player.orgasming == "creampie" and focused_Character == Rogue:
        AlphaMask("Rogue_missionary_cock_animations", "Rogue_missionary_mask_pussy_animations")
    elif Player.orgasming and focused_Character == Rogue:
        Null()
    elif Player.cock_Actions and Rogue in Player.cock_Actions[0].Targets and Player.cock_Actions[0].animation_type == "sex":
        AlphaMask("Rogue_missionary_cock_animations", "Rogue_missionary_mask_pussy_animations")

    if Rogue.right_hand_Actions and Rogue.right_hand_Actions[0].animation_type == "self_touch_pussy":
        "Rogue_missionary_right_forearm_self_touch_pussy_animation[Rogue.right_hand_Actions[0].mode]"

    if Player.orgasming and focused_Character == Rogue:
        "Rogue_missionary_left_leg_animation0"
    elif Player.cock_Actions and Rogue in Player.cock_Actions[0].Targets and Rogue.orgasming:
        At("Rogue_missionary_left_leg_animation[Player.cock_Actions[0].mode]", tremble(20))
    elif Player.cock_Actions and Rogue in Player.cock_Actions[0].Targets:
        "Rogue_missionary_left_leg_animation[Player.cock_Actions[0].mode]"
    elif Rogue.orgasming:
        At("Rogue_missionary_left_leg_animation0", tremble(20))
    else:
        "Rogue_missionary_left_leg_animation0"

    if Player.orgasming and focused_Character == Rogue:
        "Rogue_missionary_right_leg_animation0"
    elif Player.cock_Actions and Rogue in Player.cock_Actions[0].Targets and Rogue.orgasming:
        At("Rogue_missionary_right_leg_animation[Player.cock_Actions[0].mode]", tremble(20))
    elif Player.cock_Actions and Rogue in Player.cock_Actions[0].Targets:
        "Rogue_missionary_right_leg_animation[Player.cock_Actions[0].mode]"
    elif Rogue.orgasming:
        At("Rogue_missionary_right_leg_animation0", tremble(20))
    else:
        "Rogue_missionary_right_leg_animation0"

    if Rogue.clitoris_Actions and Rogue.clitoris_Actions[0].animation_type in ["vibrator", "self_vibrator"]:
        "Rogue_missionary_vibrator_animation[Rogue.clitoris_Actions[0].mode]"

    if Player.orgasming == "cumshot" and focused_Character == Rogue:
        "Rogue_missionary_cock_animations"
    elif Player.cock_Actions and Rogue in Player.cock_Actions[0].Targets and Player.cock_Actions[0].animation_type in ["grind_pussy", "grind_ass"]:
        "Rogue_missionary_cock_animations"
        
    if Player.orgasming == "cumshot" and focused_Character == Rogue:
        "Rogue_missionary_cumshot"

    if not Player.body_visible:
        Null()
    elif Player.orgasming and focused_Character == Rogue:
        "Rogue_missionary_male_knees_[Player.orgasming]_animation"
    elif Player.cock_Actions and Rogue in Player.cock_Actions[0].Targets:
        "Rogue_missionary_male_knees_[Player.cock_Actions[0].animation_type]_animation[Player.cock_Actions[0].mode]"

    if not Player.left_hand_Actions or Rogue not in Player.left_hand_Actions[0].Targets:
        Null()
    elif Player.left_hand_Actions[0].animation_type == "touch_breasts" and Rogue.right_breast_Actions and Player.left_hand_Actions[0].animation_type == Rogue.right_breast_Actions[0].animation_type:
        At("Rogue_missionary_male_left_arm_touch_right_breast_animation[Player.left_hand_Actions[0].mode]", change_offset(Rogue_missionary_right_breast_position[0], Rogue_missionary_right_breast_position[1]))
    elif Player.left_hand_Actions[0].animation_type == "touch_breasts" and Rogue.left_breast_Actions and Player.left_hand_Actions[0].animation_type == Rogue.left_breast_Actions[0].animation_type:
        At("Rogue_missionary_male_left_arm_touch_left_breast_animation[Player.left_hand_Actions[0].mode]", change_offset(Rogue_missionary_left_breast_position[0], Rogue_missionary_left_breast_position[1]))
    elif Player.left_hand_Actions[0].animation_type == "pinch_nipples" and Rogue.right_nipple_Actions and Player.left_hand_Actions[0].animation_type == Rogue.right_nipple_Actions[0].animation_type:
        At("Rogue_missionary_male_left_arm_touch_right_breast_animation[Player.left_hand_Actions[0].mode]", change_offset(Rogue_missionary_right_nipple_position[0], Rogue_missionary_right_nipple_position[1]))
    elif Player.left_hand_Actions[0].animation_type == "pinch_nipples" and Rogue.left_nipple_Actions and Player.left_hand_Actions[0].animation_type == Rogue.left_nipple_Actions[0].animation_type:
        At("Rogue_missionary_male_left_arm_touch_left_breast_animation[Player.left_hand_Actions[0].mode]", change_offset(Rogue_missionary_left_nipple_position[0], Rogue_missionary_left_nipple_position[1]))

    if not Player.right_hand_Actions or Rogue not in Player.right_hand_Actions[0].Targets:
        Null()
    elif Player.right_hand_Actions[0].animation_type == "touch_breasts" and Rogue.right_breast_Actions and Player.right_hand_Actions[0].animation_type == Rogue.right_breast_Actions[0].animation_type:
        At("Rogue_missionary_male_right_arm_touch_right_breast_animation[Player.right_hand_Actions[0].mode]", change_offset(Rogue_missionary_right_breast_position[0], Rogue_missionary_right_breast_position[1]))
    elif Player.right_hand_Actions[0].animation_type == "touch_breasts" and Rogue.left_breast_Actions and Player.right_hand_Actions[0].animation_type == Rogue.left_breast_Actions[0].animation_type:
        At("Rogue_missionary_male_right_arm_touch_left_breast_animation[Player.right_hand_Actions[0].mode]", change_offset(Rogue_missionary_left_breast_position[0], Rogue_missionary_left_breast_position[1]))
    elif Player.right_hand_Actions[0].animation_type == "pinch_nipples" and Rogue.right_nipple_Actions and Player.right_hand_Actions[0].animation_type == Rogue.right_nipple_Actions[0].animation_type:
        At("Rogue_missionary_male_right_arm_touch_right_breast_animation[Player.right_hand_Actions[0].mode]", change_offset(Rogue_missionary_right_nipple_position[0], Rogue_missionary_right_nipple_position[1]))
    elif Player.right_hand_Actions[0].animation_type == "pinch_nipples" and Rogue.left_nipple_Actions and Player.right_hand_Actions[0].animation_type == Rogue.left_nipple_Actions[0].animation_type:
        At("Rogue_missionary_male_right_arm_touch_left_breast_animation[Player.right_hand_Actions[0].mode]", change_offset(Rogue_missionary_left_nipple_position[0], Rogue_missionary_left_nipple_position[1]))

    if Player.orgasming and focused_Character == Rogue:
        Null()
    elif not Player.mouth_Actions or Rogue not in Player.mouth_Actions[0].Targets:
        Null()
    elif Player.mouth_Actions[0].animation_type == "suck_nipples" and Rogue.right_nipple_Actions and Rogue.right_nipple_Actions[0].animation_type == "suck_nipples":
        At("Rogue_missionary_male_head_suck_right_nipple_animation[Player.mouth_Actions[0].mode]", change_offset(Rogue_missionary_right_nipple_position[0], Rogue_missionary_right_nipple_position[1]))
    elif Player.mouth_Actions[0].animation_type == "suck_nipples" and Rogue.left_nipple_Actions and Rogue.left_nipple_Actions[0].animation_type == "suck_nipples":
        At("Rogue_missionary_male_head_suck_left_nipple_animation[Player.mouth_Actions[0].mode]", change_offset(Rogue_missionary_left_nipple_position[0], Rogue_missionary_left_nipple_position[1]))
    elif Player.mouth_Actions[0].animation_type == "eat_pussy":
        At("Rogue_missionary_male_head_eat_pussy_animation[Player.mouth_Actions[0].mode]", change_offset(Rogue_missionary_pussy_position[0], Rogue_missionary_pussy_position[1]))
    elif Player.mouth_Actions[0].animation_type == "eat_ass":
        At("Rogue_missionary_male_head_eat_ass_animation[Player.mouth_Actions[0].mode]", change_offset(Rogue_missionary_anus_position[0], Rogue_missionary_anus_position[1]))

    anchor (int(1992*sex_sampling), int(2446*sex_sampling))
    offset (int(1992*sex_sampling), int(2446*sex_sampling))
    
layeredimage Rogue_missionary_torso:
    if Player.orgasming and focused_Character == Rogue:
        "Rogue_missionary_left_arm_animation0"
    elif Player.cock_Actions and Rogue in Player.cock_Actions[0].Targets:
        "Rogue_missionary_left_arm_animation[Player.cock_Actions[0].mode]"
    else:
        "Rogue_missionary_left_arm_animation0"

    if Rogue.right_hand_Actions and Rogue.right_hand_Actions[0].animation_type == "self_touch_pussy":
        Null()
    elif Player.orgasming and focused_Character == Rogue:
        "Rogue_missionary_right_arm_animation0"
    elif Player.cock_Actions and Rogue in Player.cock_Actions[0].Targets:
        "Rogue_missionary_right_arm_animation[Player.cock_Actions[0].mode]"
    else:
        "Rogue_missionary_right_arm_animation0"

    always:
        "characters/Rogue/images/missionary/torso.webp"

    if Rogue.piercings["belly"]:
        "characters/Rogue/images/missionary/belly_piercing.webp"

    if Rogue.spunk["belly"]:
        "characters/Rogue/images/missionary/spunk_belly.webp"

    if Rogue.right_hand_Actions and Rogue.right_hand_Actions[0].animation_type == "self_touch_pussy":
        "Rogue_missionary_right_arm_self_touch_pussy_animation[Rogue.right_hand_Actions[0].mode]"

    if Player.orgasming and focused_Character == Rogue:
        "Rogue_missionary_breasts_animation0"
    elif Player.cock_Actions and Rogue in Player.cock_Actions[0].Targets:
        "Rogue_missionary_breasts_animation[Player.cock_Actions[0].mode]"
    else:
        "Rogue_missionary_breasts_animation0"

    if not Player.left_hand_Actions or Rogue not in Player.left_hand_Actions[0].Targets:
        Null()
    elif Player.left_hand_Actions[0].animation_type == "choke":
        At("Rogue_missionary_male_left_arm_choke_animation[Player.left_hand_Actions[0].mode]", change_offset(Rogue_missionary_neck_position[0], Rogue_missionary_neck_position[1]))

    if not Player.right_hand_Actions or Rogue not in Player.right_hand_Actions[0].Targets:
        Null()
    elif Player.right_hand_Actions[0].animation_type == "choke":
        At("Rogue_missionary_male_right_arm_choke_animation[Player.right_hand_Actions[0].mode]", change_offset(Rogue_missionary_neck_position[0], Rogue_missionary_neck_position[1]))

    if Player.orgasming and focused_Character == Rogue:
        "Rogue_missionary_head_animation0"
    elif Player.cock_Actions and Rogue in Player.cock_Actions[0].Targets:
        "Rogue_missionary_head_animation[Player.cock_Actions[0].mode]"
    else:
        "Rogue_missionary_head_animation0"

    anchor (int(1992*sex_sampling), int(2446*sex_sampling))
    offset (int(1992*sex_sampling), int(2446*sex_sampling))
    
layeredimage Rogue_missionary_left_arm:
    always:
        "characters/Rogue/images/missionary/left_arm.webp"

    anchor (int(2712*sex_sampling), int(1289*sex_sampling))
    offset (int(2712*sex_sampling), int(1289*sex_sampling))
    
layeredimage Rogue_missionary_right_arm:
    always:
        "characters/Rogue/images/missionary/right_arm.webp"

    anchor (int(1830*sex_sampling), int(1241*sex_sampling))
    offset (int(1830*sex_sampling), int(1241*sex_sampling))
    
layeredimage Rogue_missionary_right_arm_self_touch_pussy:
    always:
        "characters/Rogue/images/missionary/right_arm_finger_shadow.webp"

    always:
        "characters/Rogue/images/missionary/right_arm_finger.webp"

    anchor (int(1808*sex_sampling), int(1244*sex_sampling))
    offset (int(1808*sex_sampling), int(1244*sex_sampling))
    
layeredimage Rogue_missionary_breasts:
    always:
        "characters/Rogue/images/missionary/breasts.webp"

    if Rogue.tan_lines["top"]:
        "characters/Rogue/images/missionary/tan_lines_[Rogue.tan_lines[top]].webp"

    if Rogue.tan_lines["full"]:
        "characters/Rogue/images/missionary/tan_lines_[Rogue.tan_lines[full]]_torso.webp"

    if Rogue.piercings["nipple"] in ["barbell", "both"]:
        "characters/Rogue/images/missionary/nipple_piercings_barbell.webp"

    if Rogue.piercings["nipple"] in ["ring", "both"]:
        "characters/Rogue/images/missionary/nipple_piercings_ring.webp"

    if Rogue.spunk["breasts"]:
        "characters/Rogue/images/missionary/spunk_breasts.webp"

    anchor (int(1992*sex_sampling), int(2446*sex_sampling))
    offset (int(1992*sex_sampling), int(2446*sex_sampling))
    
layeredimage Rogue_missionary_head:
    always:
        "characters/Rogue/images/missionary/head_[Rogue.mouth].webp"

    if Rogue.eyes in ["closed", "down", "left", "right", "squint", "up"]:
        "characters/Rogue/images/missionary/eyes_[Rogue.eyes].webp"
    else:
        "Rogue_missionary_blinking"

    always:
        "characters/Rogue/images/missionary/brows_[Rogue.brows].webp"

    if Rogue.blush:
            "characters/Rogue/images/missionary/blush[Rogue.blush].webp"
        
    if Rogue.spunk["tongue"] and Rogue.mouth in ["agape", "tongue"]:
        "characters/Rogue/images/missionary/spunk_tongue.webp"

    if Rogue.spunk["mouth"] and Rogue.mouth in ["agape", "tongue"]:
        "characters/Rogue/images/missionary/spunk_mouth.webp"
        
    if Rogue.spunk["chin"]:
        "characters/Rogue/images/missionary/spunk_chin.webp"
        
    if Rogue.spunk["face"]:
        "characters/Rogue/images/missionary/spunk_face.webp"

    if Player.orgasming and focused_Character == Rogue:
        "Rogue_missionary_hair_animation0"
    elif Player.cock_Actions and Rogue in Player.cock_Actions[0].Targets:
        "Rogue_missionary_hair_animation[Player.cock_Actions[0].mode]"
    else:
        "Rogue_missionary_hair_animation0"

    anchor (int(2299*sex_sampling), int(1031*sex_sampling))
    offset (int(2299*sex_sampling), int(1031*sex_sampling))
    
layeredimage Rogue_missionary_hair:
    # if Rogue.wet or Rogue.Clothes["hair"].string == "wet":
    #     "characters/Rogue/images/missionary/hair_shadow_wet.webp"
    # else:
    always:
        "characters/Rogue/images/missionary/hair_shadow_[Rogue.Clothes[hair].string].webp"

    # if Rogue.wet or Rogue.Clothes["hair"].string == "wet":
    #     "characters/Rogue/images/missionary/hair_wet.webp"
    # else:
    always:
        "characters/Rogue/images/missionary/hair_[Rogue.Clothes[hair].string].webp"

    if Rogue.spunk["hair"]:
        "characters/Rogue/images/missionary/spunk_hair.webp"

    anchor (int(2299*sex_sampling), int(1031*sex_sampling))
    offset (int(2299*sex_sampling), int(1031*sex_sampling))
    
image Rogue_missionary_anus_closed:
    "characters/Rogue/images/missionary/anus_closed.webp"

    anchor (int(2017*sex_sampling), int(2985*sex_sampling))
    offset (int(2017*sex_sampling), int(2985*sex_sampling))

image Rogue_missionary_anus_open:
    "characters/Rogue/images/missionary/anus_open.webp"

    anchor (int(2017*sex_sampling), int(2985*sex_sampling))
    offset (int(2017*sex_sampling), int(2985*sex_sampling))

image Rogue_missionary_anus_agape:
    "characters/Rogue/images/missionary/anus_agape.webp"

    anchor (int(2016*sex_sampling), int(2977*sex_sampling))
    offset (int(2016*sex_sampling), int(2977*sex_sampling))
    
image Rogue_missionary_pussy_closed:
    "characters/Rogue/images/missionary/pussy_closed.webp"

    anchor (int(2007*sex_sampling), int(2884*sex_sampling))
    offset (int(2007*sex_sampling), int(2884*sex_sampling))

image Rogue_missionary_pussy_open:
    "characters/Rogue/images/missionary/pussy_open.webp"

    anchor (int(2007*sex_sampling), int(2884*sex_sampling))
    offset (int(2007*sex_sampling), int(2884*sex_sampling))

image Rogue_missionary_pussy_agape:
    "characters/Rogue/images/missionary/pussy_agape.webp"

    anchor (int(2003*sex_sampling), int(2877*sex_sampling))
    offset (int(2003*sex_sampling), int(2877*sex_sampling))
    
layeredimage Rogue_missionary_right_forearm_self_touch_pussy:
    always:
        "characters/Rogue/images/missionary/right_forearm_finger.webp"

    anchor (int(1512*sex_sampling), int(1832*sex_sampling))
    offset (int(1512*sex_sampling), int(1832*sex_sampling))
    
layeredimage Rogue_missionary_left_leg:
    always:
        "characters/Rogue/images/missionary/left_leg.webp"

    if Player.orgasming and focused_Character == Rogue:
        "Rogue_missionary_left_foot_animation0"
    elif Player.cock_Actions and Rogue in Player.cock_Actions[0].Targets:
        "Rogue_missionary_left_foot_animation[Player.cock_Actions[0].mode]"
    else:
        "Rogue_missionary_left_foot_animation0"

    anchor (int(3618*sex_sampling), int(2693*sex_sampling))
    offset (int(3618*sex_sampling), int(2693*sex_sampling))
    
layeredimage Rogue_missionary_left_foot:
    always:
        "characters/Rogue/images/missionary/left_foot.webp"

    anchor (int(3240*sex_sampling), int(4002*sex_sampling))
    offset (int(3240*sex_sampling), int(4002*sex_sampling))
    
layeredimage Rogue_missionary_right_leg:
    always:
        "characters/Rogue/images/missionary/right_leg.webp"

    if Player.orgasming and focused_Character == Rogue:
        "Rogue_missionary_right_foot_animation0"
    elif Player.cock_Actions and Rogue in Player.cock_Actions[0].Targets:
        "Rogue_missionary_right_foot_animation[Player.cock_Actions[0].mode]"
    else:
        "Rogue_missionary_right_foot_animation0"

    anchor (int(574*sex_sampling), int(2327*sex_sampling))
    offset (int(574*sex_sampling), int(2327*sex_sampling))
    
layeredimage Rogue_missionary_right_foot:
    always:
        "characters/Rogue/images/missionary/right_foot.webp"

    anchor (int(967*sex_sampling), int(3809*sex_sampling))
    offset (int(967*sex_sampling), int(3809*sex_sampling))
    
image Rogue_missionary_male_body:
    "characters/Rogue/images/missionary/male_body_[Player.skin_color].webp"

    anchor (int(2012*sex_sampling), int(3071*sex_sampling))
    offset (int(2012*sex_sampling), int(3071*sex_sampling))
    
image Rogue_missionary_cock:
    "characters/Rogue/images/missionary/cock_[Player.skin_color].webp"

    anchor (int(2012*sex_sampling), int(3071*sex_sampling))
    offset (int(2012*sex_sampling), int(3071*sex_sampling))

image Rogue_missionary_spunk_tip:
    "characters/Rogue/images/missionary/spunk_tip.webp"

    anchor (int(2012*sex_sampling), int(3071*sex_sampling))
    offset (int(2012*sex_sampling), int(3071*sex_sampling))
    
image Rogue_missionary_male_knees:
    "characters/Rogue/images/missionary/male_knees_[Player.skin_color].webp"

    anchor (int(2012*sex_sampling), int(3071*sex_sampling))
    offset (int(2012*sex_sampling), int(3071*sex_sampling))

image Rogue_missionary_male_left_arm_finger:
    "characters/Rogue/images/missionary/male_left_arm_[Player.skin_color]_finger.webp"

    anchor (int(2025*sex_sampling), int(2795*sex_sampling))
    offset (int(2025*sex_sampling), int(2795*sex_sampling))

image Rogue_missionary_male_right_arm_finger:
    "characters/Rogue/images/missionary/male_right_arm_[Player.skin_color]_finger.webp"

    anchor (int(2025*sex_sampling), int(2795*sex_sampling))
    offset (int(2025*sex_sampling), int(2795*sex_sampling))

image Rogue_missionary_dildo:
    "characters/Rogue/images/missionary/dildo.webp"

    anchor (int(2017*sex_sampling), int(2850*sex_sampling))
    offset (int(2017*sex_sampling), int(2850*sex_sampling))

image Rogue_missionary_vibrator:
    "characters/Rogue/images/missionary/vibrator.webp"

    anchor (int(2020*sex_sampling), int(2778*sex_sampling))
    offset (int(2020*sex_sampling), int(2778*sex_sampling))

image Rogue_missionary_mask_anus:
    "characters/Rogue/images/missionary/mask_anus.webp"

    anchor (int(2016*sex_sampling), int(2977*sex_sampling))
    offset (int(2016*sex_sampling), int(2977*sex_sampling))

image Rogue_missionary_mask_pussy:
    "characters/Rogue/images/missionary/mask_pussy.webp"

    anchor (int(2003*sex_sampling), int(2877*sex_sampling))
    offset (int(1997*sex_sampling), int(2890*sex_sampling))

layeredimage Rogue_missionary_male_left_arm_fondle:
    if Player.left_hand_Actions[0].animation_type in ["touch_breasts"]:
        "Player_left_arm_fondle"
    elif Player.left_hand_Actions[0].animation_type in ["choke", "pinch_nipples"]:
        "Player_left_arm_pinch"

layeredimage Rogue_missionary_male_right_arm_fondle:
    if Player.right_hand_Actions[0].animation_type in ["touch_breasts"]:
        "Player_right_arm_fondle"
    elif Player.right_hand_Actions[0].animation_type in ["choke", "pinch_nipples"]:
        "Player_right_arm_pinch"

layeredimage Rogue_missionary_male_head:
    if Player.body_visible:
        "Player_head"

    if Player.mouth_Actions and Rogue in Player.mouth_Actions[0].Targets and Player.mouth_Actions[0].animation_type in ["suck_nipples", "eat_pussy", "eat_ass"]:
        "Rogue_missionary_male_tongue_animation[Player.mouth_Actions[0].mode]"

image Rogue_missionary_male_tongue:
    "Player_tongue"

image Rogue_missionary_left_arm_animation0:
    "Rogue_missionary_left_arm"

    missionary_left_arm_animation0

image Rogue_missionary_left_arm_animation1:
    "Rogue_missionary_left_arm"

    missionary_left_arm_animation1

image Rogue_missionary_left_arm_animation2:
    "Rogue_missionary_left_arm"

    missionary_left_arm_animation2

image Rogue_missionary_right_arm_animation0:
    "Rogue_missionary_right_arm"

    missionary_right_arm_animation0

image Rogue_missionary_right_arm_animation1:
    "Rogue_missionary_right_arm"

    missionary_right_arm_animation1

image Rogue_missionary_right_arm_animation2:
    "Rogue_missionary_right_arm"

    missionary_right_arm_animation2

image Rogue_missionary_torso_animation0:
    "Rogue_missionary_torso"

    missionary_torso_animation0

image Rogue_missionary_torso_animation1:
    "Rogue_missionary_torso"

    missionary_torso_animation1

image Rogue_missionary_torso_animation2:
    "Rogue_missionary_torso"

    missionary_torso_animation2

image Rogue_missionary_right_arm_self_touch_pussy_animation0:
    "Rogue_missionary_right_arm_self_touch_pussy"

    missionary_right_arm_self_touch_pussy_animation0

image Rogue_missionary_right_arm_self_touch_pussy_animation1:
    "Rogue_missionary_right_arm_self_touch_pussy"

    missionary_right_arm_self_touch_pussy_animation1

image Rogue_missionary_right_arm_self_touch_pussy_animation2:
    "Rogue_missionary_right_arm_self_touch_pussy"

    missionary_right_arm_self_touch_pussy_animation2

image Rogue_missionary_breasts_animation0:
    "Rogue_missionary_breasts"

    missionary_breasts_animation0

image Rogue_missionary_breasts_animation1:
    "Rogue_missionary_breasts"

    missionary_breasts_animation1

image Rogue_missionary_breasts_animation2:
    "Rogue_missionary_breasts"

    missionary_breasts_animation2

image Rogue_missionary_head_animation0:
    "Rogue_missionary_head"

    missionary_head_animation0

image Rogue_missionary_head_animation1:
    "Rogue_missionary_head"

    missionary_head_animation1

image Rogue_missionary_head_animation2:
    "Rogue_missionary_head"

    missionary_head_animation2

image Rogue_missionary_hair_animation0:
    "Rogue_missionary_hair"

    missionary_hair_animation0

image Rogue_missionary_hair_animation1:
    "Rogue_missionary_hair"

    missionary_hair_animation1

image Rogue_missionary_hair_animation2:
    "Rogue_missionary_hair"

    missionary_hair_animation2

image Rogue_missionary_thighs_animation0:
    "Rogue_missionary_thighs"

    missionary_thighs_animation0

image Rogue_missionary_thighs_animation1:
    "Rogue_missionary_thighs"

    missionary_thighs_animation1

image Rogue_missionary_thighs_animation2:
    "Rogue_missionary_thighs"

    missionary_thighs_animation2

image Rogue_missionary_pussy_finger_pussy_animation0:
    "Rogue_missionary_pussy_closed"

    missionary_pussy_finger_pussy_animation0

image Rogue_missionary_pussy_finger_pussy_animation1:
    "Rogue_missionary_pussy_agape"

    missionary_pussy_finger_pussy_animation1

image Rogue_missionary_anus_finger_ass_animation0:
    "Rogue_missionary_anus_closed"

    missionary_anus_finger_ass_animation0

image Rogue_missionary_anus_finger_ass_animation1:
    "Rogue_missionary_anus_agape"

    missionary_anus_finger_ass_animation1

image Rogue_missionary_pussy_sex_animation0:
    "Rogue_missionary_pussy_closed"

    missionary_pussy_sex_animation0

image Rogue_missionary_pussy_sex_animation1:
    "Rogue_missionary_pussy_agape"

    missionary_pussy_sex_animation1

image Rogue_missionary_pussy_sex_animation2:
    "Rogue_missionary_pussy_agape"

    missionary_pussy_sex_animation2

image Rogue_missionary_anus_anal_animation0:
    "Rogue_missionary_anus_closed"

    missionary_anus_anal_animation0

image Rogue_missionary_anus_anal_animation1:
    "Rogue_missionary_anus_agape"

    missionary_anus_anal_animation1

image Rogue_missionary_anus_anal_animation2:
    "Rogue_missionary_anus_agape"

    missionary_anus_anal_animation2

image Rogue_missionary_pussy_grind_pussy_animation0:
    "Rogue_missionary_pussy_closed"

    missionary_pussy_grind_pussy_animation0

image Rogue_missionary_pussy_grind_pussy_animation2:
    "Rogue_missionary_pussy_open"

    missionary_pussy_grind_pussy_animation2

image Rogue_missionary_anus_grind_ass_animation0:
    "Rogue_missionary_anus_closed"

    missionary_anus_grind_ass_animation0

image Rogue_missionary_anus_grind_ass_animation2:
    "Rogue_missionary_anus_open"

    missionary_anus_grind_ass_animation2

image Rogue_missionary_pussy_dildo_pussy_animation0:
    "Rogue_missionary_pussy_closed"

    missionary_pussy_dildo_pussy_animation0

image Rogue_missionary_pussy_dildo_pussy_animation1:
    "Rogue_missionary_pussy_agape"

    missionary_pussy_dildo_pussy_animation1

image Rogue_missionary_anus_dildo_ass_animation0:
    "Rogue_missionary_anus_closed"

    missionary_anus_dildo_ass_animation0

image Rogue_missionary_anus_dildo_ass_animation1:
    "Rogue_missionary_anus_agape"

    missionary_anus_dildo_ass_animation1

image Rogue_missionary_right_forearm_self_touch_pussy_animation0:
    "Rogue_missionary_right_forearm_self_touch_pussy"

    missionary_right_forearm_self_touch_pussy_animation0

image Rogue_missionary_right_forearm_self_touch_pussy_animation1:
    "Rogue_missionary_right_forearm_self_touch_pussy"

    missionary_right_forearm_self_touch_pussy_animation1

image Rogue_missionary_left_leg_animation0:
    "Rogue_missionary_left_leg"

    missionary_left_leg_animation0

image Rogue_missionary_left_leg_animation1:
    "Rogue_missionary_left_leg"

    missionary_left_leg_animation1

image Rogue_missionary_left_leg_animation2:
    "Rogue_missionary_left_leg"

    missionary_left_leg_animation2

image Rogue_missionary_left_foot_animation0:
    "Rogue_missionary_left_foot"

    missionary_left_foot_animation0

image Rogue_missionary_left_foot_animation1:
    "Rogue_missionary_left_foot"

    missionary_left_foot_animation1

image Rogue_missionary_left_foot_animation2:
    "Rogue_missionary_left_foot"

    missionary_left_foot_animation2

image Rogue_missionary_right_leg_animation0:
    "Rogue_missionary_right_leg"

    missionary_right_leg_animation0

image Rogue_missionary_right_leg_animation1:
    "Rogue_missionary_right_leg"

    missionary_right_leg_animation1

image Rogue_missionary_right_leg_animation2:
    "Rogue_missionary_right_leg"

    missionary_right_leg_animation2

image Rogue_missionary_right_foot_animation0:
    "Rogue_missionary_right_foot"

    missionary_right_foot_animation0

image Rogue_missionary_right_foot_animation1:
    "Rogue_missionary_right_foot"

    missionary_right_foot_animation1

image Rogue_missionary_right_foot_animation2:
    "Rogue_missionary_right_foot"

    missionary_right_foot_animation2

image Rogue_missionary_male_body_sex_animation0:
    "Rogue_missionary_male_body"

    missionary_cock_sex_animation0

image Rogue_missionary_male_body_sex_animation1:
    "Rogue_missionary_male_body"

    missionary_cock_sex_animation1

image Rogue_missionary_male_body_sex_animation2:
    "Rogue_missionary_male_body"

    missionary_cock_sex_animation2

image Rogue_missionary_male_body_anal_animation0:
    "Rogue_missionary_male_body"

    missionary_cock_anal_animation0

image Rogue_missionary_male_body_anal_animation1:
    "Rogue_missionary_male_body"

    missionary_cock_anal_animation1

image Rogue_missionary_male_body_anal_animation2:
    "Rogue_missionary_male_body"

    missionary_cock_anal_animation2

image Rogue_missionary_male_body_grind_pussy_animation0:
    "Rogue_missionary_male_body"

    missionary_cock_grind_pussy_animation0

image Rogue_missionary_male_body_grind_pussy_animation2:
    "Rogue_missionary_male_body"

    missionary_cock_grind_pussy_animation2

image Rogue_missionary_male_body_grind_ass_animation0:
    "Rogue_missionary_male_body"

    missionary_cock_grind_ass_animation0

image Rogue_missionary_male_body_grind_ass_animation2:
    "Rogue_missionary_male_body"

    missionary_cock_grind_ass_animation2

image Rogue_missionary_cock_sex_animation0:
    "Rogue_missionary_cock"

    missionary_cock_sex_animation0

image Rogue_missionary_cock_sex_animation1:
    "Rogue_missionary_cock"

    missionary_cock_sex_animation1

image Rogue_missionary_cock_sex_animation2:
    "Rogue_missionary_cock"

    missionary_cock_sex_animation2

image Rogue_missionary_cock_anal_animation0:
    "Rogue_missionary_cock"

    missionary_cock_anal_animation0

image Rogue_missionary_cock_anal_animation1:
    "Rogue_missionary_cock"

    missionary_cock_anal_animation1

image Rogue_missionary_cock_anal_animation2:
    "Rogue_missionary_cock"

    missionary_cock_anal_animation2

image Rogue_missionary_cock_grind_pussy_animation0:
    "Rogue_missionary_cock"

    missionary_cock_grind_pussy_animation0

image Rogue_missionary_cock_grind_pussy_animation2:
    "Rogue_missionary_cock"

    missionary_cock_grind_pussy_animation2

image Rogue_missionary_cock_grind_ass_animation0:
    "Rogue_missionary_cock"

    missionary_cock_grind_ass_animation0

image Rogue_missionary_cock_grind_ass_animation2:
    "Rogue_missionary_cock"

    missionary_cock_grind_ass_animation2

image Rogue_missionary_spunk_tip_sex_animation0:
    "Rogue_missionary_spunk_tip"

    missionary_cock_sex_animation0

image Rogue_missionary_spunk_tip_sex_animation1:
    "Rogue_missionary_spunk_tip"

    missionary_cock_sex_animation1

image Rogue_missionary_spunk_tip_sex_animation2:
    "Rogue_missionary_spunk_tip"

    missionary_cock_sex_animation2

image Rogue_missionary_spunk_tip_anal_animation0:
    "Rogue_missionary_spunk_tip"

    missionary_cock_anal_animation0

image Rogue_missionary_spunk_tip_anal_animation1:
    "Rogue_missionary_spunk_tip"

    missionary_cock_anal_animation1

image Rogue_missionary_spunk_tip_anal_animation2:
    "Rogue_missionary_spunk_tip"

    missionary_cock_anal_animation2

image Rogue_missionary_spunk_tip_grind_pussy_animation0:
    "Rogue_missionary_spunk_tip"

    missionary_cock_grind_pussy_animation0

image Rogue_missionary_spunk_tip_grind_pussy_animation2:
    "Rogue_missionary_spunk_tip"

    missionary_cock_grind_pussy_animation2

image Rogue_missionary_spunk_tip_grind_ass_animation0:
    "Rogue_missionary_spunk_tip"

    missionary_cock_grind_ass_animation0

image Rogue_missionary_spunk_tip_grind_ass_animation2:
    "Rogue_missionary_spunk_tip"

    missionary_cock_grind_ass_animation2

image Rogue_missionary_male_knees_sex_animation0:
    "Rogue_missionary_male_knees"

    missionary_cock_sex_animation0

image Rogue_missionary_male_knees_sex_animation1:
    "Rogue_missionary_male_knees"

    missionary_cock_sex_animation1

image Rogue_missionary_male_knees_sex_animation2:
    "Rogue_missionary_male_knees"

    missionary_cock_sex_animation2

image Rogue_missionary_male_knees_anal_animation0:
    "Rogue_missionary_male_knees"

    missionary_cock_anal_animation0

image Rogue_missionary_male_knees_anal_animation1:
    "Rogue_missionary_male_knees"

    missionary_cock_anal_animation1

image Rogue_missionary_male_knees_anal_animation2:
    "Rogue_missionary_male_knees"

    missionary_cock_anal_animation2

image Rogue_missionary_male_knees_grind_pussy_animation0:
    "Rogue_missionary_male_knees"

    missionary_cock_grind_pussy_animation0

image Rogue_missionary_male_knees_grind_pussy_animation2:
    "Rogue_missionary_male_knees"

    missionary_cock_grind_pussy_animation2

image Rogue_missionary_male_knees_grind_ass_animation0:
    "Rogue_missionary_male_knees"

    missionary_cock_grind_ass_animation0

image Rogue_missionary_male_knees_grind_ass_animation2:
    "Rogue_missionary_male_knees"

    missionary_cock_grind_ass_animation2

image Rogue_missionary_male_left_arm_choke_animation0:
    "Rogue_missionary_male_left_arm_fondle"

    missionary_male_left_arm_choke_animation0

image Rogue_missionary_male_left_arm_choke_animation1:
    "Rogue_missionary_male_left_arm_fondle"

    missionary_male_left_arm_choke_animation1

image Rogue_missionary_male_left_arm_touch_left_breast_animation0:
    "Rogue_missionary_male_left_arm_fondle"

    missionary_male_left_arm_touch_left_breast_animation0

image Rogue_missionary_male_left_arm_touch_left_breast_animation1:
    "Rogue_missionary_male_left_arm_fondle"
    
    missionary_male_left_arm_touch_left_breast_animation1

image Rogue_missionary_male_left_arm_touch_right_breast_animation0:
    "Rogue_missionary_male_left_arm_fondle"

    missionary_male_left_arm_touch_right_breast_animation0

image Rogue_missionary_male_left_arm_touch_right_breast_animation1:
    "Rogue_missionary_male_left_arm_fondle"

    missionary_male_left_arm_touch_right_breast_animation1

image Rogue_missionary_male_left_arm_finger_pussy_animation0:
    "Rogue_missionary_male_left_arm_finger"

    missionary_male_left_arm_finger_pussy_animation0

image Rogue_missionary_male_left_arm_finger_pussy_animation1:
    "Rogue_missionary_male_left_arm_finger"

    missionary_male_left_arm_finger_pussy_animation1

image Rogue_missionary_male_left_arm_finger_ass_animation0:
    "Rogue_missionary_male_left_arm_finger"

    missionary_male_left_arm_finger_ass_animation0

image Rogue_missionary_male_left_arm_finger_ass_animation1:
    "Rogue_missionary_male_left_arm_finger"

    missionary_male_left_arm_finger_ass_animation1

image Rogue_missionary_male_right_arm_choke_animation0:
    "Rogue_missionary_male_right_arm_fondle"

    missionary_male_right_arm_choke_animation0

image Rogue_missionary_male_right_arm_choke_animation1:
    "Rogue_missionary_male_right_arm_fondle"

    missionary_male_right_arm_choke_animation1

image Rogue_missionary_male_right_arm_touch_left_breast_animation0:
    "Rogue_missionary_male_right_arm_fondle"

    missionary_male_right_arm_touch_left_breast_animation0

image Rogue_missionary_male_right_arm_touch_left_breast_animation1:
    "Rogue_missionary_male_right_arm_fondle"

    missionary_male_right_arm_touch_left_breast_animation1

image Rogue_missionary_male_right_arm_touch_right_breast_animation0:
    "Rogue_missionary_male_right_arm_fondle"

    missionary_male_right_arm_touch_right_breast_animation0

image Rogue_missionary_male_right_arm_touch_right_breast_animation1:
    "Rogue_missionary_male_right_arm_fondle"

    missionary_male_right_arm_touch_right_breast_animation1

image Rogue_missionary_male_right_arm_finger_pussy_animation0:
    "Rogue_missionary_male_right_arm_finger"

    missionary_male_right_arm_finger_pussy_animation0

image Rogue_missionary_male_right_arm_finger_pussy_animation1:
    "Rogue_missionary_male_right_arm_finger"

    missionary_male_right_arm_finger_pussy_animation1

image Rogue_missionary_male_right_arm_finger_ass_animation0:
    "Rogue_missionary_male_right_arm_finger"

    missionary_male_right_arm_finger_ass_animation0

image Rogue_missionary_male_right_arm_finger_ass_animation1:
    "Rogue_missionary_male_right_arm_finger"

    missionary_male_right_arm_finger_ass_animation1

image Rogue_missionary_dildo_pussy_animation0:
    "Rogue_missionary_dildo"

    missionary_dildo_pussy_animation0

image Rogue_missionary_dildo_pussy_animation1:
    "Rogue_missionary_dildo"

    missionary_dildo_pussy_animation1
    
image Rogue_missionary_dildo_ass_animation0:
    "Rogue_missionary_dildo"

    missionary_dildo_ass_animation0
    
image Rogue_missionary_dildo_ass_animation1:
    "Rogue_missionary_dildo"

    missionary_dildo_ass_animation1

image Rogue_missionary_vibrator_animation0:
    "Rogue_missionary_vibrator"

    missionary_vibrator_animation0

image Rogue_missionary_vibrator_animation1:
    "Rogue_missionary_vibrator"

    missionary_vibrator_animation1

image Rogue_missionary_mask_finger_pussy_animation0:
    "Rogue_missionary_mask_pussy"

    missionary_mask_finger_pussy_animation0

image Rogue_missionary_mask_finger_pussy_animation1:
    "Rogue_missionary_mask_pussy"

    missionary_mask_finger_pussy_animation1

image Rogue_missionary_mask_finger_ass_animation0:
    "Rogue_missionary_mask_anus"

    missionary_mask_finger_ass_animation0

image Rogue_missionary_mask_finger_ass_animation1:
    "Rogue_missionary_mask_anus"

    missionary_mask_finger_ass_animation1

image Rogue_missionary_mask_sex_animation0:
    "Rogue_missionary_mask_pussy"

    missionary_mask_sex_animation0

image Rogue_missionary_mask_sex_animation1:
    "Rogue_missionary_mask_pussy"

    missionary_mask_sex_animation1

image Rogue_missionary_mask_sex_animation2:
    "Rogue_missionary_mask_pussy"

    missionary_mask_sex_animation2

image Rogue_missionary_mask_anal_animation0:
    "Rogue_missionary_mask_anus"

    missionary_mask_anal_animation0

image Rogue_missionary_mask_anal_animation1:
    "Rogue_missionary_mask_anus"

    missionary_mask_anal_animation1

image Rogue_missionary_mask_anal_animation2:
    "Rogue_missionary_mask_anus"

    missionary_mask_anal_animation2

image Rogue_missionary_mask_dildo_pussy_animation0:
    "Rogue_missionary_mask_pussy"

    missionary_mask_dildo_pussy_animation0

image Rogue_missionary_mask_dildo_pussy_animation1:
    "Rogue_missionary_mask_pussy"

    missionary_mask_dildo_pussy_animation1

image Rogue_missionary_mask_dildo_ass_animation0:
    "Rogue_missionary_mask_anus"

    missionary_mask_dildo_ass_animation0

image Rogue_missionary_mask_dildo_ass_animation1:
    "Rogue_missionary_mask_anus"

    missionary_mask_dildo_ass_animation1
    
image Rogue_missionary_male_head_suck_left_nipple_animation0:
    "Rogue_missionary_male_head"

    missionary_male_head_suck_left_nipple_animation0
    
image Rogue_missionary_male_head_suck_left_nipple_animation1:
    "Rogue_missionary_male_head"

    missionary_male_head_suck_left_nipple_animation1
    
image Rogue_missionary_male_head_suck_right_nipple_animation0:
    "Rogue_missionary_male_head"

    missionary_male_head_suck_right_nipple_animation0
    
image Rogue_missionary_male_head_suck_right_nipple_animation1:
    "Rogue_missionary_male_head"

    missionary_male_head_suck_right_nipple_animation1
    
image Rogue_missionary_male_head_eat_pussy_animation0:
    "Rogue_missionary_male_head"

    missionary_male_head_eat_pussy_animation0
    
image Rogue_missionary_male_head_eat_pussy_animation1:
    "Rogue_missionary_male_head"

    missionary_male_head_eat_pussy_animation1
    
image Rogue_missionary_male_head_eat_ass_animation0:
    "Rogue_missionary_male_head"

    missionary_male_head_eat_ass_animation0
    
image Rogue_missionary_male_head_eat_ass_animation1:
    "Rogue_missionary_male_head"

    missionary_male_head_eat_ass_animation1
    
image Rogue_missionary_male_tongue_animation0:
    "Rogue_missionary_male_tongue"

    missionary_male_tongue_animation0
    
image Rogue_missionary_male_tongue_animation1:
    "Rogue_missionary_male_tongue"

    missionary_male_tongue_animation1

image Rogue_missionary_male_body_cumshot_animation:
    "Rogue_missionary_male_body"

    missionary_cock_cumshot_animation

image Rogue_missionary_male_body_creampie_animation:
    "Rogue_missionary_male_body"

    missionary_cock_creampie_animation

image Rogue_missionary_male_body_anal_creampie_animation:
    "Rogue_missionary_male_body"

    missionary_cock_anal_creampie_animation

image Rogue_missionary_cock_cumshot_animation:
    "Rogue_missionary_cock"

    missionary_cock_cumshot_animation

image Rogue_missionary_cock_creampie_animation:
    "Rogue_missionary_cock"

    missionary_cock_creampie_animation

image Rogue_missionary_cock_anal_creampie_animation:
    "Rogue_missionary_cock"

    missionary_cock_anal_creampie_animation

image Rogue_missionary_spunk_tip_cumshot_animation:
    "Rogue_missionary_spunk_tip"

    missionary_cock_cumshot_animation

image Rogue_missionary_spunk_tip_creampie_animation:
    "Rogue_missionary_spunk_tip"

    missionary_cock_creampie_animation

image Rogue_missionary_spunk_tip_anal_creampie_animation:
    "Rogue_missionary_spunk_tip"

    missionary_cock_anal_creampie_animation

image Rogue_missionary_male_knees_cumshot_animation:
    "Rogue_missionary_male_knees"

    missionary_cock_cumshot_animation

image Rogue_missionary_male_knees_creampie_animation:
    "Rogue_missionary_male_knees"

    missionary_cock_creampie_animation

image Rogue_missionary_male_knees_anal_creampie_animation:
    "Rogue_missionary_male_knees"

    missionary_cock_anal_creampie_animation

image Rogue_missionary_pussy_creampie_animation:
    "Rogue_missionary_pussy_agape"

    missionary_pussy_creampie_animation

image Rogue_missionary_anus_anal_creampie_animation:
    "Rogue_missionary_anus_agape"

    missionary_anus_anal_creampie_animation

image Rogue_missionary_mask_creampie_animation:
    "Rogue_missionary_mask_pussy"

    missionary_mask_creampie_animation

image Rogue_missionary_mask_anal_creampie_animation:
    "Rogue_missionary_mask_anus"

    missionary_mask_anal_creampie_animation

layeredimage Rogue_missionary_cock_animations:
    if Player.orgasming and focused_Character == Rogue:
        "Rogue_missionary_cock_[Player.orgasming]_animation"
    else:
        "Rogue_missionary_cock_[Player.cock_Actions[0].animation_type]_animation[Player.cock_Actions[0].mode]"

    if not Player.spunk and not Player.orgasming:
        Null()
    elif Player.orgasming and focused_Character == Rogue:
        "Rogue_missionary_spunk_tip_[Player.orgasming]_animation"
    else:
        "Rogue_missionary_spunk_tip_[Player.cock_Actions[0].animation_type]_animation[Player.cock_Actions[0].mode]"

layeredimage Rogue_missionary_male_left_arm_finger_animations:
    always:
        "Rogue_missionary_male_left_arm_[Player.left_hand_Actions[0].animation_type]_animation[Player.left_hand_Actions[0].mode]"

layeredimage Rogue_missionary_male_right_arm_finger_animations:
    always:
        "Rogue_missionary_male_right_arm_[Player.right_hand_Actions[0].animation_type]_animation[Player.right_hand_Actions[0].mode]"

layeredimage Rogue_missionary_dildo_pussy_animations:
    always:
        "Rogue_missionary_dildo_pussy_animation[Rogue.vagina_Actions[0].mode]"

layeredimage Rogue_missionary_dildo_ass_animations:
    always:
        "Rogue_missionary_dildo_ass_animation[Rogue.anus_Actions[0].mode]"

layeredimage Rogue_missionary_mask_anus_animations:
    if Player.orgasming == "anal_creampie" and focused_Character == Rogue:
        "Rogue_missionary_mask_anal_creampie_animation"
    elif Rogue.anus_Actions[0].animation_type in ["dildo_ass", "self_dildo_ass"]:
        "Rogue_missionary_mask_dildo_ass_animation[Rogue.anus_Actions[0].mode]"
    else:
        "Rogue_missionary_mask_[Rogue.anus_Actions[0].animation_type]_animation[Rogue.anus_Actions[0].mode]"

layeredimage Rogue_missionary_mask_pussy_animations:
    if Player.orgasming == "creampie" and focused_Character == Rogue:
        "Rogue_missionary_mask_creampie_animation"
    elif Rogue.vagina_Actions[0].animation_type in ["dildo_pussy", "self_dildo_pussy"]:
        "Rogue_missionary_mask_dildo_pussy_animation[Rogue.vagina_Actions[0].mode]"
    else:
        "Rogue_missionary_mask_[Rogue.vagina_Actions[0].animation_type]_animation[Rogue.vagina_Actions[0].mode]"
    
image Rogue_missionary_blinking:
    "characters/Rogue/images/missionary/eyes_[Rogue.eyes].webp"
    choice:
        4.5
    choice:
        4.0
    choice:
        3.5
    "characters/Rogue/images/missionary/eyes_blink1.webp"
    0.023
    "characters/Rogue/images/missionary/eyes_blink2.webp"
    0.023
    "characters/Rogue/images/missionary/eyes_closed.webp"
    0.054
    "characters/Rogue/images/missionary/eyes_blink2.webp"
    0.018
    "characters/Rogue/images/missionary/eyes_blink1.webp"
    0.072
    repeat

image Rogue_missionary_cumshot:
    "characters/Rogue/images/missionary/spunk_jet.webp"

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

image Rogue_missionary_creampie:
    "characters/Rogue/images/missionary/creampie_pussy_agape.webp"

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

image Rogue_missionary_anal_creampie:
    "characters/Rogue/images/missionary/creampie_anus_agape.webp"

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