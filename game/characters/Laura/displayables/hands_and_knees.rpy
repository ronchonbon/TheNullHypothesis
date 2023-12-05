image Laura_sprite hands_and_knees:
    contains:
        "Laura_hands_and_knees_temp"
    
    offset (int(200*0.38), int(100*0.38))
            
layeredimage Laura_hands_and_knees_temp:
    if Laura.hovered:
        At("Laura_hands_and_knees_controls_temp", hover)
    else:
        "Laura_hands_and_knees_controls_temp"
            
layeredimage Laura_hands_and_knees_controls_temp:
    if speed > 2.5 or speed <= 1.75:
        Null()
    elif intensity >= 2.0:
        At(At("Laura_hands_and_knees", speed_200), intensity_200)
    elif intensity >= 1.75:
        At(At("Laura_hands_and_knees", speed_200), intensity_175)
    elif intensity >= 1.5:
        At(At("Laura_hands_and_knees", speed_200), intensity_150)
    elif intensity >= 1.25:
        At(At("Laura_hands_and_knees", speed_200), intensity_125)
    elif intensity >= 1.0:
        At(At("Laura_hands_and_knees", speed_200), intensity_100)
    elif intensity >= 0.75:
        At(At("Laura_hands_and_knees", speed_200), intensity_075)
    elif intensity >= 0.5:
        At(At("Laura_hands_and_knees", speed_200), intensity_050)
    elif intensity >= 0.25:
        At(At("Laura_hands_and_knees", speed_200), intensity_025)
    else:
        At(At("Laura_hands_and_knees", speed_200), intensity_000)

    if speed > 1.75 or speed <= 1.5:
        Null()
    elif intensity >= 2.0:
        At(At("Laura_hands_and_knees", speed_175), intensity_200)
    elif intensity >= 1.75:
        At(At("Laura_hands_and_knees", speed_175), intensity_175)
    elif intensity >= 1.5:
        At(At("Laura_hands_and_knees", speed_175), intensity_150)
    elif intensity >= 1.25:
        At(At("Laura_hands_and_knees", speed_175), intensity_125)
    elif intensity >= 1.0:
        At(At("Laura_hands_and_knees", speed_175), intensity_100)
    elif intensity >= 0.75:
        At(At("Laura_hands_and_knees", speed_175), intensity_075)
    elif intensity >= 0.5:
        At(At("Laura_hands_and_knees", speed_175), intensity_050)
    elif intensity >= 0.25:
        At(At("Laura_hands_and_knees", speed_175), intensity_025)
    else:
        At(At("Laura_hands_and_knees", speed_175), intensity_000)

    if speed > 1.5 or speed <= 1.25:
        Null()
    elif intensity >= 2.0:
        At(At("Laura_hands_and_knees", speed_150), intensity_200)
    elif intensity >= 1.75:
        At(At("Laura_hands_and_knees", speed_150), intensity_175)
    elif intensity >= 1.5:
        At(At("Laura_hands_and_knees", speed_150), intensity_150)
    elif intensity >= 1.25:
        At(At("Laura_hands_and_knees", speed_150), intensity_125)
    elif intensity >= 1.0:
        At(At("Laura_hands_and_knees", speed_150), intensity_100)
    elif intensity >= 0.75:
        At(At("Laura_hands_and_knees", speed_150), intensity_075)
    elif intensity >= 0.5:
        At(At("Laura_hands_and_knees", speed_150), intensity_050)
    elif intensity >= 0.25:
        At(At("Laura_hands_and_knees", speed_150), intensity_025)
    else:
        At(At("Laura_hands_and_knees", speed_150), intensity_000)
 
    if speed > 1.25 or speed <= 1.0:
        Null()
    elif intensity >= 2.0:
        At(At("Laura_hands_and_knees", speed_125), intensity_200)
    elif intensity >= 1.75:
        At(At("Laura_hands_and_knees", speed_125), intensity_175)
    elif intensity >= 1.5:
        At(At("Laura_hands_and_knees", speed_125), intensity_150)
    elif intensity >= 1.25:
        At(At("Laura_hands_and_knees", speed_125), intensity_125)
    elif intensity >= 1.0:
        At(At("Laura_hands_and_knees", speed_125), intensity_100)
    elif intensity >= 0.75:
        At(At("Laura_hands_and_knees", speed_125), intensity_075)
    elif intensity >= 0.5:
        At(At("Laura_hands_and_knees", speed_125), intensity_050)
    elif intensity >= 0.25:
        At(At("Laura_hands_and_knees", speed_125), intensity_025)
    else:
        At(At("Laura_hands_and_knees", speed_125), intensity_000)
 
    if speed > 1.0 or speed <= 0.75:
        Null()
    elif intensity >= 2.0:
        At(At("Laura_hands_and_knees", speed_100), intensity_200)
    elif intensity >= 1.75:
        At(At("Laura_hands_and_knees", speed_100), intensity_175)
    elif intensity >= 1.5:
        At(At("Laura_hands_and_knees", speed_100), intensity_150)
    elif intensity >= 1.25:
        At(At("Laura_hands_and_knees", speed_100), intensity_125)
    elif intensity >= 1.0:
        At(At("Laura_hands_and_knees", speed_100), intensity_100)
    elif intensity >= 0.75:
        At(At("Laura_hands_and_knees", speed_100), intensity_075)
    elif intensity >= 0.5:
        At(At("Laura_hands_and_knees", speed_100), intensity_050)
    elif intensity >= 0.25:
        At(At("Laura_hands_and_knees", speed_100), intensity_025)
    else:
        At(At("Laura_hands_and_knees", speed_100), intensity_000)

    if speed > 0.75 or speed <= 0.5:
        Null()
    elif intensity >= 2.0:
        At(At("Laura_hands_and_knees", speed_075), intensity_200)
    elif intensity >= 1.75:
        At(At("Laura_hands_and_knees", speed_075), intensity_175)
    elif intensity >= 1.5:
        At(At("Laura_hands_and_knees", speed_075), intensity_150)
    elif intensity >= 1.25:
        At(At("Laura_hands_and_knees", speed_075), intensity_125)
    elif intensity >= 1.0:
        At(At("Laura_hands_and_knees", speed_075), intensity_100)
    elif intensity >= 0.75:
        At(At("Laura_hands_and_knees", speed_075), intensity_075)
    elif intensity >= 0.5:
        At(At("Laura_hands_and_knees", speed_075), intensity_050)
    elif intensity >= 0.25:
        At(At("Laura_hands_and_knees", speed_075), intensity_025)
    else:
        At(At("Laura_hands_and_knees", speed_075), intensity_000)

    if speed > 0.5 or speed <= 0.25:
        Null()
    elif intensity >= 2.0:
        At(At("Laura_hands_and_knees", speed_050), intensity_200)
    elif intensity >= 1.75:
        At(At("Laura_hands_and_knees", speed_050), intensity_175)
    elif intensity >= 1.5:
        At(At("Laura_hands_and_knees", speed_050), intensity_150)
    elif intensity >= 1.25:
        At(At("Laura_hands_and_knees", speed_050), intensity_125)
    elif intensity >= 1.0:
        At(At("Laura_hands_and_knees", speed_050), intensity_100)
    elif intensity >= 0.75:
        At(At("Laura_hands_and_knees", speed_050), intensity_075)
    elif intensity >= 0.5:
        At(At("Laura_hands_and_knees", speed_050), intensity_050)
    elif intensity >= 0.25:
        At(At("Laura_hands_and_knees", speed_050), intensity_025)
    else:
        At(At("Laura_hands_and_knees", speed_050), intensity_000)

    if speed > 0.25 or speed <= 0.01:
        Null()
    elif intensity >= 2.0:
        At(At("Laura_hands_and_knees", speed_025), intensity_200)
    elif intensity >= 1.75:
        At(At("Laura_hands_and_knees", speed_025), intensity_175)
    elif intensity >= 1.5:
        At(At("Laura_hands_and_knees", speed_025), intensity_150)
    elif intensity >= 1.25:
        At(At("Laura_hands_and_knees", speed_025), intensity_125)
    elif intensity >= 1.0:
        At(At("Laura_hands_and_knees", speed_025), intensity_100)
    elif intensity >= 0.75:
        At(At("Laura_hands_and_knees", speed_025), intensity_075)
    elif intensity >= 0.5:
        At(At("Laura_hands_and_knees", speed_025), intensity_050)
    elif intensity >= 0.25:
        At(At("Laura_hands_and_knees", speed_025), intensity_025)
    else:
        At(At("Laura_hands_and_knees", speed_025), intensity_000)

    if speed != 0.01:
        Null()
    elif intensity >= 2.0:
        At(At("Laura_hands_and_knees", speed_0001), intensity_200)
    elif intensity >= 1.75:
        At(At("Laura_hands_and_knees", speed_0001), intensity_175)
    elif intensity >= 1.5:
        At(At("Laura_hands_and_knees", speed_0001), intensity_150)
    elif intensity >= 1.25:
        At(At("Laura_hands_and_knees", speed_0001), intensity_125)
    elif intensity >= 1.0:
        At(At("Laura_hands_and_knees", speed_0001), intensity_100)
    elif intensity >= 0.75:
        At(At("Laura_hands_and_knees", speed_0001), intensity_075)
    elif intensity >= 0.5:
        At(At("Laura_hands_and_knees", speed_0001), intensity_050)
    elif intensity >= 0.25:
        At(At("Laura_hands_and_knees", speed_0001), intensity_025)
    else:
        At(At("Laura_hands_and_knees", speed_0001), intensity_000)

    if speed >= 0.01 or speed < 0.0:
        Null()
    elif intensity >= 2.0:
        At(At("Laura_hands_and_knees", speed_000), intensity_200)
    elif intensity >= 1.75:
        At(At("Laura_hands_and_knees", speed_000), intensity_175)
    elif intensity >= 1.5:
        At(At("Laura_hands_and_knees", speed_000), intensity_150)
    elif intensity >= 1.25:
        At(At("Laura_hands_and_knees", speed_000), intensity_125)
    elif intensity >= 1.0:
        At(At("Laura_hands_and_knees", speed_000), intensity_100)
    elif intensity >= 0.75:
        At(At("Laura_hands_and_knees", speed_000), intensity_075)
    elif intensity >= 0.5:
        At(At("Laura_hands_and_knees", speed_000), intensity_050)
    elif intensity >= 0.25:
        At(At("Laura_hands_and_knees", speed_000), intensity_025)
    else:
        At(At("Laura_hands_and_knees", speed_000), intensity_000)

layeredimage Laura_hands_and_knees:
    if Player.orgasming and focused_Companion == Laura:
        "Laura_hands_and_knees_ass_handjob_animation0"
    elif Player.cock_Actions and Laura in Player.cock_Actions[0].Actors:
        "Laura_hands_and_knees_ass_[Player.cock_Actions[0].animation_type]_animation[Player.cock_Actions[0].mode]"
    else: 
        "Laura_hands_and_knees_ass_handjob_animation0"

    if not Player.body_visible:
        Null()
    elif Player.orgasming and focused_Companion == Laura:
        "Laura_hands_and_knees_male_left_foot_animation0"
    elif Player.cock_Actions and Laura in Player.cock_Actions[0].Actors:
        "Laura_hands_and_knees_male_left_foot_animation[Player.cock_Actions[0].mode]"
    else: 
        "Laura_hands_and_knees_male_left_foot_animation0"

    if Player.orgasming == "cumshot" and focused_Companion == Laura:
        "Laura_hands_and_knees_torso_handjob_animation0"
    elif Player.orgasming in ["cum_in_mouth", "cum_down_throat"] and focused_Companion == Laura:
        "Laura_hands_and_knees_torso_[Player.orgasming]_animation"
    elif Player.cock_Actions and Laura in Player.cock_Actions[0].Actors:
        "Laura_hands_and_knees_torso_[Player.cock_Actions[0].animation_type]_animation[Player.cock_Actions[0].mode]"
    else: 
        "Laura_hands_and_knees_torso_handjob_animation0"

    if Player.orgasming == "cumshot" and focused_Companion == Laura:
        "Laura_hands_and_knees_head_handjob_animation0"
    elif Player.orgasming in ["cum_in_mouth", "cum_down_throat"] and focused_Companion == Laura:
        "Laura_hands_and_knees_head_[Player.orgasming]_animation"
    elif Player.cock_Actions and Laura in Player.cock_Actions[0].Actors:
        "Laura_hands_and_knees_head_[Player.cock_Actions[0].animation_type]_animation[Player.cock_Actions[0].mode]"
    else: 
        "Laura_hands_and_knees_head_handjob_animation0"

    if not Player.body_visible:
        Null()
    elif Player.cock_Actions and Laura in Player.cock_Actions[0].Actors:
        "Laura_hands_and_knees_male_body_[Player.cock_Actions[0].animation_type]_animation[Player.cock_Actions[0].mode]"
    else: 
        "Laura_hands_and_knees_male_body_handjob_animation0"

    if Player.orgasming in ["cumshot", "cum_in_mouth"] and focused_Companion == Laura:
        "Laura_hands_and_knees_thumb_[Player.orgasming]_animation"
    elif Player.orgasming == "cum_down_throat" and focused_Companion == Laura:
        Null()
    elif Player.cock_Actions and Laura in Player.cock_Actions[0].Actors and Player.cock_Actions[0].animation_type != "deepthroat":
        "Laura_hands_and_knees_thumb_[Player.cock_Actions[0].animation_type]_animation[Player.cock_Actions[0].mode]"
    elif Player.cock_Actions and Laura in Player.cock_Actions[0].Actors and Player.cock_Actions[0].animation_type == "deepthroat":
        Null()
    else: 
        "Laura_hands_and_knees_thumb_handjob_animation0"

    if Player.orgasming in ["cum_in_mouth", "cum_down_throat"] and focused_Companion == Laura:
        AlphaMask("Laura_hands_and_knees_cock_animations", "Laura_hands_and_knees_mask_animations")
    elif Player.orgasming and focused_Companion == Laura:
        "Laura_hands_and_knees_cock_animations"
    elif Laura.mouth_Actions and ((Laura.mouth_Actions[0].animation_type == "blowjob" and Laura.mouth_Actions[0].mode == 3) or Laura.mouth_Actions[0].animation_type == "deepthroat"):
        AlphaMask("Laura_hands_and_knees_cock_animations", "Laura_hands_and_knees_mask_animations")
    elif Player.cock_Actions and Laura in Player.cock_Actions[0].Actors:
        "Laura_hands_and_knees_cock_animations"
    else:
        "Laura_hands_and_knees_cock_handjob_animation0"

    if Player.orgasming == "cumshot" and focused_Companion == Laura:
        "Laura_hands_and_knees_cumshot"

    if Player.orgasming in ["cumshot", "cum_in_mouth"] and focused_Companion == Laura:
        "Laura_hands_and_knees_hand_[Player.orgasming]_animation"
    elif Player.orgasming == "cum_down_throat" and focused_Companion == Laura:
        Null()
    elif Player.cock_Actions and Laura in Player.cock_Actions[0].Actors and Player.cock_Actions[0].animation_type != "deepthroat":
        "Laura_hands_and_knees_hand_[Player.cock_Actions[0].animation_type]_animation[Player.cock_Actions[0].mode]"
    elif Player.cock_Actions and Laura in Player.cock_Actions[0].Actors and Player.cock_Actions[0].animation_type == "deepthroat":
        Null()
    else: 
        "Laura_hands_and_knees_hand_handjob_animation0"

layeredimage Laura_hands_and_knees_ass:
    always:
        "characters/Laura/images/hands_and_knees/ass.webp"

    if Laura.tan_lines["bottom"]:
        "characters/Laura/images/hands_and_knees/tan_lines_[Laura.tan_lines[bottom]].webp"

    if Laura.tan_lines["full"]:
        "characters/Laura/images/hands_and_knees/tan_lines_[Laura.tan_lines[full]]_ass.webp"

    if Laura.spunk["ass"]:
        "characters/Laura/images/hands_and_knees/spunk_ass.webp"

    anchor (int(1705*sex_sampling), int(1614*sex_sampling))
    offset (int(1705*sex_sampling), int(1614*sex_sampling))

image Laura_hands_and_knees_male_left_foot:
    "characters/Laura/images/hands_and_knees/male_left_foot_[Player.skin_color].webp"

    anchor (int(1316*sex_sampling), int(2877*sex_sampling))
    offset (int(1316*sex_sampling), int(2877*sex_sampling))

layeredimage Laura_hands_and_knees_torso:
    if Player.orgasming in ["cumshot", "cum_down_throat"] and focused_Companion == Laura:
        "Laura_hands_and_knees_left_arm_handjob_animation0"
    elif Player.orgasming == "cum_in_mouth" and focused_Companion == Laura:
        "Laura_hands_and_knees_left_arm_cum_in_mouth_animation"
    elif Player.cock_Actions and Laura in Player.cock_Actions[0].Actors:
        "Laura_hands_and_knees_left_arm_[Player.cock_Actions[0].animation_type]_animation[Player.cock_Actions[0].mode]"
    else:
        "Laura_hands_and_knees_left_arm_handjob_animation0"

    if Laura.right_hand_Actions and Laura.right_hand_Actions[0].animation_type == "self_touch_pussy":
        "characters/Laura/images/hands_and_knees/torso_finger.webp"
    elif Laura.right_hand_Actions and Laura.right_hand_Actions[0].animation_type == "fondle_balls":
        "characters/Laura/images/hands_and_knees/torso_fondle.webp"
    else:
        "characters/Laura/images/hands_and_knees/torso.webp"

    if Player.orgasming and focused_Companion == Laura:
        "Laura_hands_and_knees_right_arm_handjob_animation0"
    elif Laura.right_hand_Actions and Laura.right_hand_Actions[0].animation_type == "self_touch_pussy":
        Null()
    elif Player.cock_Actions and Laura in Player.cock_Actions[0].Actors:
        "Laura_hands_and_knees_right_arm_[Player.cock_Actions[0].animation_type]_animation[Player.cock_Actions[0].mode]"
    else:
        "Laura_hands_and_knees_right_arm_handjob_animation0"

    if Player.orgasming and focused_Companion == Laura:
        "Laura_hands_and_knees_breasts_handjob_animation0"
    elif Player.cock_Actions and Laura in Player.cock_Actions[0].Actors:
        "Laura_hands_and_knees_breasts_[Player.cock_Actions[0].animation_type]_animation[Player.cock_Actions[0].mode]"
    else:
        "Laura_hands_and_knees_breasts_handjob_animation0"

    if Player.orgasming and focused_Companion == Laura:
        Null()
    elif Laura.right_hand_Actions and Laura.right_hand_Actions[0].animation_type == "fondle_balls":
        "Laura_hands_and_knees_right_forearm_fondle_balls_animation[Laura.right_hand_Actions[0].mode]"

    if Player.orgasming and focused_Companion == Laura:
        "Laura_hands_and_knees_hair_back_handjob_animation0"
    elif Player.cock_Actions and Laura in Player.cock_Actions[0].Actors:
        "Laura_hands_and_knees_hair_back_[Player.cock_Actions[0].animation_type]_animation[Player.cock_Actions[0].mode]"
    else:
        "Laura_hands_and_knees_hair_back_handjob_animation0"

    anchor (int(2011*sex_sampling), int(1801*sex_sampling))
    offset (int(2011*sex_sampling), int(1801*sex_sampling))

image Laura_hands_and_knees_left_arm:
    "characters/Laura/images/hands_and_knees/left_arm.webp"

    anchor (int(2624*sex_sampling), int(1754*sex_sampling))
    offset (int(2624*sex_sampling), int(1754*sex_sampling))

layeredimage Laura_hands_and_knees_right_arm:
    if Player.orgasming and focused_Companion == Laura:
        "characters/Laura/images/hands_and_knees/right_arm.webp"
    elif Laura.right_hand_Actions and Laura.right_hand_Actions[0].animation_type == "fondle_balls":
        "characters/Laura/images/hands_and_knees/right_arm_fondle.webp"
    else:
        "characters/Laura/images/hands_and_knees/right_arm.webp"

    anchor (int(1484*sex_sampling), int(2004*sex_sampling))
    offset (int(1484*sex_sampling), int(2004*sex_sampling))

layeredimage Laura_hands_and_knees_breasts:
    if Laura.breasts_supported and Laura.right_hand_Actions and Laura.right_hand_Actions[0].animation_type == "self_touch_pussy":
        "characters/Laura/images/hands_and_knees/breasts_supported_finger.webp"
    elif Laura.breasts_supported and Laura.right_hand_Actions and Laura.right_hand_Actions[0].animation_type == "fondle_balls":
        "characters/Laura/images/hands_and_knees/breasts_supported_fondle.webp"
    elif Laura.breasts_supported:
        "characters/Laura/images/hands_and_knees/breasts_supported.webp"
    elif Laura.right_hand_Actions and Laura.right_hand_Actions[0].animation_type == "self_touch_pussy":
        "characters/Laura/images/hands_and_knees/breasts_finger.webp"
    elif Laura.right_hand_Actions and Laura.right_hand_Actions[0].animation_type == "fondle_balls":
        "characters/Laura/images/hands_and_knees/breasts_fondle.webp"
    else:
        "characters/Laura/images/hands_and_knees/breasts.webp"

    if Laura.tan_lines["top"]:
        "characters/Laura/images/hands_and_knees/tan_lines_[Laura.tan_lines[top]].webp"

    if Laura.tan_lines["full"]:
        "characters/Laura/images/hands_and_knees/tan_lines_[Laura.tan_lines[full]]_torso.webp"

    if Laura.piercings["nipple"] in ["barbell", "both"]:
        "characters/Laura/images/hands_and_knees/nipple_piercings_barbell.webp"

    if Laura.piercings["nipple"] in ["ring", "both"]:
        "characters/Laura/images/hands_and_knees/nipple_piercings_ring.webp"

    if Laura.spunk["breasts"]:
        "characters/Laura/images/hands_and_knees/spunk_breasts.webp"

    anchor (int(2011*sex_sampling), int(1801*sex_sampling))
    offset (int(2011*sex_sampling), int(1801*sex_sampling))

layeredimage Laura_hands_and_knees_right_forearm:
    always:
        "characters/Laura/images/hands_and_knees/right_forearm_fondle.webp"

    anchor (int(990*sex_sampling), int(2877*sex_sampling))
    offset (int(990*sex_sampling), int(2877*sex_sampling))

image Laura_hands_and_knees_hair_back:
    "characters/Laura/images/hands_and_knees/hair_back.webp"

    anchor (int(2138*sex_sampling), int(1585*sex_sampling))
    offset (int(2138*sex_sampling), int(1585*sex_sampling))

layeredimage Laura_hands_and_knees_head:
    if Player.orgasming == "cum_in_mouth" and focused_Companion == Laura:
        "characters/Laura/images/hands_and_knees/head_agape.webp"
    elif Player.orgasming == "cum_down_throat" and focused_Companion == Laura:
        "characters/Laura/images/hands_and_knees/head_deepthroat.webp"
    elif (Player.orgasming and focused_Companion == Laura) or not Laura.mouth_Actions:
        "characters/Laura/images/hands_and_knees/head_[Laura.mouth].webp"
    elif Laura.mouth_Actions[0].animation_type == "deepthroat":
        "characters/Laura/images/hands_and_knees/head_deepthroat.webp"
    elif Laura.mouth_Actions[0].mode > 1:
        "characters/Laura/images/hands_and_knees/head_agape.webp"
    else:
        "characters/Laura/images/hands_and_knees/head_kiss.webp"

    if Player.orgasming == "cum_down_throat" and focused_Companion == Laura:
        Null()
    elif (Player.orgasming and focused_Companion == Laura) or not Laura.mouth_Actions:
        "characters/Laura/images/hands_and_knees/eyes_[Laura.eyes].webp"
    elif Laura.mouth_Actions[0].animation_type == "deepthroat":
        Null()
    elif Laura.eyes in ["closed", "down", "left", "right", "squint", "up"]:
        "characters/Laura/images/hands_and_knees/eyes_[Laura.eyes].webp"
    else:
        "Laura_hands_and_knees_blinking"

    if Player.orgasming == "cum_down_throat" and focused_Companion == Laura:
        Null()
    elif (Player.orgasming and focused_Companion == Laura) or not Laura.mouth_Actions:
        "characters/Laura/images/hands_and_knees/brows_[Laura.brows].webp"
    elif Laura.mouth_Actions[0].animation_type != "deepthroat":
        "characters/Laura/images/hands_and_knees/brows_[Laura.brows].webp"

    if Player.orgasming in ["cum_in_mouth", "cum_down_throat"] and focused_Companion == Laura:
        "Laura_hands_and_knees_mouth_[Player.orgasming]_animation"
    elif (Player.orgasming and focused_Companion == Laura) or not Laura.mouth_Actions:
        Null()
    elif Laura.mouth_Actions[0].animation_type == "deepthroat":
        "Laura_hands_and_knees_mouth_deepthroat_animation[Laura.mouth_Actions[0].mode]"
    elif Laura.mouth_Actions[0].mode != 2:
        "Laura_hands_and_knees_mouth_blowjob_animation[Laura.mouth_Actions[0].mode]"

    if Player.orgasming and focused_Companion == Laura:
        Null()
    elif Laura.mouth_Actions and Laura.mouth_Actions[0].animation_type == "blowjob" and Laura.mouth_Actions[0].mode == 2:
        "Laura_hands_and_knees_tongue_blowjob_animation[Laura.mouth_Actions[0].mode]"

    if not Laura.blush:
        Null()
    elif Player.orgasming == "cum_down_throat" and focused_Companion == Laura:
        "characters/Laura/images/hands_and_knees/blush[Laura.blush]_deepthroat.webp"
    elif (Player.orgasming and focused_Companion == Laura) or not Laura.mouth_Actions:
        "characters/Laura/images/hands_and_knees/blush[Laura.blush].webp"
    elif Laura.mouth_Actions[0].animation_type == "deepthroat":
        "characters/Laura/images/hands_and_knees/blush[Laura.blush]_deepthroat.webp"

    if not Laura.spunk["chin"]:
        Null()
    elif Player.orgasming in ["cum_in_mouth", "cum_down_throat"] and focused_Companion == Laura:
        Null()
    elif Laura.mouth_Actions and Laura.mouth_Actions[0].animation_type == "deepthroat":
        Null()
    elif (Laura.mouth_Actions and Laura.mouth_Actions[0].mode > 1) or Laura.mouth in ["agape", "tongue"]:
        "characters/Laura/images/hands_and_knees/spunk_chin_open.webp"
    else:
        "characters/Laura/images/hands_and_knees/spunk_chin.webp"

    if Laura.spunk["face"]:
        "characters/Laura/images/hands_and_knees/spunk_face.webp"

    if Player.orgasming and focused_Companion == Laura:
        "Laura_hands_and_knees_hair_handjob_animation0"
    elif Player.cock_Actions and Laura in Player.cock_Actions[0].Actors:
        "Laura_hands_and_knees_hair_[Player.cock_Actions[0].animation_type]_animation[Player.cock_Actions[0].mode]"
    else:
        "Laura_hands_and_knees_hair_handjob_animation0"

    anchor (int(2138*sex_sampling), int(1585*sex_sampling))
    offset (int(2145*sex_sampling), int(1585*sex_sampling))

image Laura_hands_and_knees_mouth_kiss:
    "characters/Laura/images/hands_and_knees/mouth_kiss.webp"

    anchor (int(2171*sex_sampling), int(1867*sex_sampling))
    offset (int(2171*sex_sampling), int(1867*sex_sampling))

image Laura_hands_and_knees_mouth_agape:
    "characters/Laura/images/hands_and_knees/mouth_agape.webp"

    anchor (int(2171*sex_sampling), int(1867*sex_sampling))
    offset (int(2171*sex_sampling), int(1867*sex_sampling))

image Laura_hands_and_knees_mouth_deepthroat:
    "characters/Laura/images/hands_and_knees/mouth_deepthroat.webp"

    anchor (int(2196*sex_sampling), int(1924*sex_sampling))
    offset (int(2196*sex_sampling), int(1924*sex_sampling))

layeredimage Laura_hands_and_knees_tongue:
    always:
        "characters/Laura/images/hands_and_knees/tongue.webp"

    if Laura.spunk["mouth"] or Laura.spunk["tongue"]:
        "characters/Laura/images/hands_and_knees/spunk_tongue.webp"

    anchor (int(2175*sex_sampling), int(1849*sex_sampling))
    offset (int(2175*sex_sampling), int(1849*sex_sampling))

layeredimage Laura_hands_and_knees_hair:
    # if (Laura.wet or Laura.Clothes["hair"].string == "wet") and Player.orgasming == "cum_on_face" and focused_Companion == Laura:
    #     "characters/Laura/images/hands_and_knees/hair_shadow_wet.webp"
    # elif (Laura.wet or Laura.Clothes["hair"].string == "wet") and Player.orgasming == "cum_down_throat" and focused_Companion == Laura:
    #     "characters/Laura/images/hands_and_knees/hair_shadow_wet_deepthroat.webp"
    # elif (Laura.wet or Laura.Clothes["hair"].string == "wet") and Laura.mouth_Actions and Laura.mouth_Actions[0].animation_type == "deepthroat":
    #     "characters/Laura/images/hands_and_knees/hair_shadow_wet_deepthroat.webp"
    # elif Laura.wet or Laura.Clothes["hair"].string == "wet":
    #     "characters/Laura/images/hands_and_knees/hair_shadow_wet.webp"
    if Player.orgasming == "cum_on_face" and focused_Companion == Laura:
        "characters/Laura/images/hands_and_knees/hair_shadow_[Laura.Clothes[hair].string].webp"
    elif Player.orgasming == "cum_down_throat" and focused_Companion == Laura:
        "characters/Laura/images/hands_and_knees/hair_shadow_[Laura.Clothes[hair].string]_deepthroat.webp"
    elif Laura.mouth_Actions and Laura.mouth_Actions[0].animation_type == "deepthroat":
        "characters/Laura/images/hands_and_knees/hair_shadow_[Laura.Clothes[hair].string]_deepthroat.webp"
    else:
        "characters/Laura/images/hands_and_knees/hair_shadow_[Laura.Clothes[hair].string].webp"

    # if (Laura.wet or Laura.Clothes["hair"].string == "wet") and Player.orgasming == "cum_on_face" and focused_Companion == Laura:
    #     "characters/Laura/images/hands_and_knees/hair_wet.webp"
    # elif (Laura.wet or Laura.Clothes["hair"].string == "wet") and Player.orgasming == "cum_down_throat" and focused_Companion == Laura:
    #     "characters/Laura/images/hands_and_knees/hair_wet_deepthroat.webp"
    # elif (Laura.wet or Laura.Clothes["hair"].string == "wet") and Laura.mouth_Actions and Laura.mouth_Actions[0].animation_type == "deepthroat":
    #     "characters/Laura/images/hands_and_knees/hair_wet_deepthroat.webp"
    # elif Laura.wet or Laura.Clothes["hair"].string == "wet":
    #     "characters/Laura/images/hands_and_knees/hair_wet.webp"
    if Player.orgasming == "cum_on_face" and focused_Companion == Laura:
        "characters/Laura/images/hands_and_knees/hair_[Laura.Clothes[hair].string].webp"
    elif Player.orgasming == "cum_down_throat" and focused_Companion == Laura:
        "characters/Laura/images/hands_and_knees/hair_[Laura.Clothes[hair].string]_deepthroat.webp"
    elif Laura.mouth_Actions and Laura.mouth_Actions[0].animation_type == "deepthroat":
        "characters/Laura/images/hands_and_knees/hair_[Laura.Clothes[hair].string]_deepthroat.webp"
    else:
        "characters/Laura/images/hands_and_knees/hair_[Laura.Clothes[hair].string].webp"

    if Laura.spunk["hair"]:
        "characters/Laura/images/hands_and_knees/spunk_hair.webp"

    anchor (int(2138*sex_sampling), int(1585*sex_sampling))
    offset (int(2138*sex_sampling), int(1585*sex_sampling))

image Laura_hands_and_knees_male_body:
    "characters/Laura/images/hands_and_knees/male_body_[Player.skin_color].webp"

    anchor (int(2285*sex_sampling), int(2966*sex_sampling))
    offset (int(2285*sex_sampling), int(2966*sex_sampling))

image Laura_hands_and_knees_thumb:
    "characters/Laura/images/hands_and_knees/thumb.webp"

    anchor (int(2816*sex_sampling), int(2651*sex_sampling))
    offset (int(2816*sex_sampling), int(2651*sex_sampling))

image Laura_hands_and_knees_cock:
    "characters/Laura/images/hands_and_knees/cock_[Player.skin_color].webp"

    anchor (int(2285*sex_sampling), int(2966*sex_sampling))
    offset (int(2285*sex_sampling), int(2966*sex_sampling))

image Laura_hands_and_knees_saliva:
    "characters/Laura/images/hands_and_knees/saliva.webp"

    anchor (int(2285*sex_sampling), int(2966*sex_sampling))
    offset (int(2285*sex_sampling), int(2966*sex_sampling))

image Laura_hands_and_knees_spunk_tip:
    "characters/Laura/images/hands_and_knees/spunk_tip.webp"

    anchor (int(2285*sex_sampling), int(2966*sex_sampling))
    offset (int(2285*sex_sampling), int(2966*sex_sampling))

image Laura_hands_and_knees_mask_agape:
    "characters/Laura/images/hands_and_knees/mask_agape.webp"

    anchor (int(2171*sex_sampling), int(1867*sex_sampling))
    offset (int(2171*sex_sampling), int(1867*sex_sampling))

image Laura_hands_and_knees_mask_deepthroat:
    "characters/Laura/images/hands_and_knees/mask_deepthroat.webp"

    anchor (int(2196*sex_sampling), int(1924*sex_sampling))
    offset (int(2210*sex_sampling), int(1945*sex_sampling))

layeredimage Laura_hands_and_knees_hand:
    always:
        "characters/Laura/images/hands_and_knees/hand.webp"

    anchor (int(2816*sex_sampling), int(2651*sex_sampling))
    offset (int(2816*sex_sampling), int(2651*sex_sampling))

image Laura_hands_and_knees_ass_handjob_animation0:
    "Laura_hands_and_knees_ass"

    hands_and_knees_ass_handjob_animation0

image Laura_hands_and_knees_ass_handjob_animation1:
    "Laura_hands_and_knees_ass"

    hands_and_knees_ass_handjob_animation1

image Laura_hands_and_knees_ass_blowjob_animation0:
    "Laura_hands_and_knees_ass"

    hands_and_knees_ass_blowjob_animation0

image Laura_hands_and_knees_ass_blowjob_animation1:
    "Laura_hands_and_knees_ass"

    hands_and_knees_ass_blowjob_animation1

image Laura_hands_and_knees_ass_blowjob_animation2:
    "Laura_hands_and_knees_ass"

    hands_and_knees_ass_blowjob_animation2

image Laura_hands_and_knees_ass_blowjob_animation3:
    "Laura_hands_and_knees_ass"

    hands_and_knees_ass_blowjob_animation3

image Laura_hands_and_knees_ass_deepthroat_animation0:
    "Laura_hands_and_knees_ass"

    hands_and_knees_ass_deepthroat_animation0

image Laura_hands_and_knees_ass_deepthroat_animation1:
    "Laura_hands_and_knees_ass"

    hands_and_knees_ass_deepthroat_animation1
    
image Laura_hands_and_knees_male_left_foot_animation0:
    "Laura_hands_and_knees_male_left_foot"

    hands_and_knees_male_left_foot_animation0

image Laura_hands_and_knees_male_left_foot_animation1:
    "Laura_hands_and_knees_male_left_foot"

    hands_and_knees_male_left_foot_animation1

image Laura_hands_and_knees_male_left_foot_animation2:
    "Laura_hands_and_knees_male_left_foot"

    hands_and_knees_male_left_foot_animation2

image Laura_hands_and_knees_male_left_foot_animation3:
    "Laura_hands_and_knees_male_left_foot"

    hands_and_knees_male_left_foot_animation3

image Laura_hands_and_knees_male_left_foot_animation4:
    "Laura_hands_and_knees_male_left_foot"

    hands_and_knees_male_left_foot_animation4

image Laura_hands_and_knees_left_arm_handjob_animation0:
    "Laura_hands_and_knees_left_arm"

    hands_and_knees_left_arm_handjob_animation0

image Laura_hands_and_knees_left_arm_handjob_animation1:
    "Laura_hands_and_knees_left_arm"

    hands_and_knees_left_arm_handjob_animation1

image Laura_hands_and_knees_left_arm_blowjob_animation0:
    "Laura_hands_and_knees_left_arm"

    hands_and_knees_left_arm_blowjob_animation0

image Laura_hands_and_knees_left_arm_blowjob_animation1:
    "Laura_hands_and_knees_left_arm"

    hands_and_knees_left_arm_blowjob_animation1

image Laura_hands_and_knees_left_arm_blowjob_animation2:
    "Laura_hands_and_knees_left_arm"

    hands_and_knees_left_arm_blowjob_animation2

image Laura_hands_and_knees_left_arm_blowjob_animation3:
    "Laura_hands_and_knees_left_arm"

    hands_and_knees_left_arm_blowjob_animation3

image Laura_hands_and_knees_left_arm_deepthroat_animation0:
    "Laura_hands_and_knees_left_arm"

    hands_and_knees_left_arm_deepthroat_animation0

image Laura_hands_and_knees_left_arm_deepthroat_animation1:
    "Laura_hands_and_knees_left_arm"

    hands_and_knees_left_arm_deepthroat_animation1

image Laura_hands_and_knees_torso_handjob_animation0:
    "Laura_hands_and_knees_torso"

    hands_and_knees_torso_handjob_animation0

image Laura_hands_and_knees_torso_handjob_animation1:
    "Laura_hands_and_knees_torso"

    hands_and_knees_torso_handjob_animation1

image Laura_hands_and_knees_torso_blowjob_animation0:
    "Laura_hands_and_knees_torso"

    hands_and_knees_torso_blowjob_animation0

image Laura_hands_and_knees_torso_blowjob_animation1:
    "Laura_hands_and_knees_torso"

    hands_and_knees_torso_blowjob_animation1

image Laura_hands_and_knees_torso_blowjob_animation2:
    "Laura_hands_and_knees_torso"

    hands_and_knees_torso_blowjob_animation2

image Laura_hands_and_knees_torso_blowjob_animation3:
    "Laura_hands_and_knees_torso"

    hands_and_knees_torso_blowjob_animation3

image Laura_hands_and_knees_torso_deepthroat_animation0:
    "Laura_hands_and_knees_torso"

    hands_and_knees_torso_deepthroat_animation0

image Laura_hands_and_knees_torso_deepthroat_animation1:
    "Laura_hands_and_knees_torso"

    hands_and_knees_torso_deepthroat_animation1

image Laura_hands_and_knees_right_arm_handjob_animation0:
    "Laura_hands_and_knees_right_arm"

    hands_and_knees_right_arm_handjob_animation0

image Laura_hands_and_knees_right_arm_handjob_animation1:
    "Laura_hands_and_knees_right_arm"

    hands_and_knees_right_arm_handjob_animation1

image Laura_hands_and_knees_right_arm_blowjob_animation0:
    "Laura_hands_and_knees_right_arm"

    hands_and_knees_right_arm_blowjob_animation0

image Laura_hands_and_knees_right_arm_blowjob_animation1:
    "Laura_hands_and_knees_right_arm"

    hands_and_knees_right_arm_blowjob_animation1

image Laura_hands_and_knees_right_arm_blowjob_animation2:
    "Laura_hands_and_knees_right_arm"

    hands_and_knees_right_arm_blowjob_animation2

image Laura_hands_and_knees_right_arm_blowjob_animation3:
    "Laura_hands_and_knees_right_arm"

    hands_and_knees_right_arm_blowjob_animation3

image Laura_hands_and_knees_right_arm_deepthroat_animation0:
    "Laura_hands_and_knees_right_arm"

    hands_and_knees_right_arm_deepthroat_animation0

image Laura_hands_and_knees_right_arm_deepthroat_animation1:
    "Laura_hands_and_knees_right_arm"

    hands_and_knees_right_arm_deepthroat_animation1

image Laura_hands_and_knees_breasts_handjob_animation0:
    "Laura_hands_and_knees_breasts"

    hands_and_knees_breasts_handjob_animation0

image Laura_hands_and_knees_breasts_handjob_animation1:
    "Laura_hands_and_knees_breasts"

    hands_and_knees_breasts_handjob_animation1

image Laura_hands_and_knees_breasts_blowjob_animation0:
    "Laura_hands_and_knees_breasts"

    hands_and_knees_breasts_blowjob_animation0

image Laura_hands_and_knees_breasts_blowjob_animation1:
    "Laura_hands_and_knees_breasts"

    hands_and_knees_breasts_blowjob_animation1

image Laura_hands_and_knees_breasts_blowjob_animation2:
    "Laura_hands_and_knees_breasts"

    hands_and_knees_breasts_blowjob_animation2

image Laura_hands_and_knees_breasts_blowjob_animation3:
    "Laura_hands_and_knees_breasts"

    hands_and_knees_breasts_blowjob_animation3

image Laura_hands_and_knees_breasts_deepthroat_animation0:
    "Laura_hands_and_knees_breasts"

    hands_and_knees_breasts_deepthroat_animation0

image Laura_hands_and_knees_breasts_deepthroat_animation1:
    "Laura_hands_and_knees_breasts"

    hands_and_knees_breasts_deepthroat_animation1

image Laura_hands_and_knees_right_forearm_fondle_balls_animation0:
    "Laura_hands_and_knees_right_forearm"

    hands_and_knees_right_forearm_fondle_balls_animation0

image Laura_hands_and_knees_right_forearm_fondle_balls_animation1:
    "Laura_hands_and_knees_right_forearm"

    hands_and_knees_right_forearm_fondle_balls_animation1

image Laura_hands_and_knees_right_forearm_deepthroat_animation0:
    "Laura_hands_and_knees_right_forearm"

    hands_and_knees_right_forearm_deepthroat_animation0

image Laura_hands_and_knees_right_forearm_deepthroat_animation1:
    "Laura_hands_and_knees_right_forearm"

    hands_and_knees_right_forearm_deepthroat_animation1

image Laura_hands_and_knees_hair_back_handjob_animation0:
    "Laura_hands_and_knees_hair_back"

    hands_and_knees_hair_back_handjob_animation0

image Laura_hands_and_knees_hair_back_handjob_animation1:
    "Laura_hands_and_knees_hair_back"

    hands_and_knees_hair_back_handjob_animation1

image Laura_hands_and_knees_hair_back_blowjob_animation0:
    "Laura_hands_and_knees_hair_back"

    hands_and_knees_hair_back_blowjob_animation0

image Laura_hands_and_knees_hair_back_blowjob_animation1:
    "Laura_hands_and_knees_hair_back"

    hands_and_knees_hair_back_blowjob_animation1

image Laura_hands_and_knees_hair_back_blowjob_animation2:
    "Laura_hands_and_knees_hair_back"

    hands_and_knees_hair_back_blowjob_animation2

image Laura_hands_and_knees_hair_back_blowjob_animation3:
    "Laura_hands_and_knees_hair_back"

    hands_and_knees_hair_back_blowjob_animation3

image Laura_hands_and_knees_hair_back_deepthroat_animation0:
    "Laura_hands_and_knees_hair_back"

    hands_and_knees_hair_back_deepthroat_animation0

image Laura_hands_and_knees_hair_back_deepthroat_animation1:
    "Laura_hands_and_knees_hair_back"

    hands_and_knees_hair_back_deepthroat_animation1

image Laura_hands_and_knees_head_handjob_animation0:
    "Laura_hands_and_knees_head"

    hands_and_knees_head_handjob_animation0

image Laura_hands_and_knees_head_handjob_animation1:
    "Laura_hands_and_knees_head"

    hands_and_knees_head_handjob_animation1

image Laura_hands_and_knees_head_blowjob_animation0:
    "Laura_hands_and_knees_head"

    hands_and_knees_head_blowjob_animation0

image Laura_hands_and_knees_head_blowjob_animation1:
    "Laura_hands_and_knees_head"

    hands_and_knees_head_blowjob_animation1

image Laura_hands_and_knees_head_blowjob_animation2:
    "Laura_hands_and_knees_head"

    hands_and_knees_head_blowjob_animation2

image Laura_hands_and_knees_head_blowjob_animation3:
    "Laura_hands_and_knees_head"

    hands_and_knees_head_blowjob_animation3

image Laura_hands_and_knees_head_deepthroat_animation0:
    "Laura_hands_and_knees_head"

    hands_and_knees_head_deepthroat_animation0

image Laura_hands_and_knees_head_deepthroat_animation1:
    "Laura_hands_and_knees_head"

    hands_and_knees_head_deepthroat_animation1
    
image Laura_hands_and_knees_mouth_blowjob_animation0:
    Null()

    hands_and_knees_mouth_blowjob_animation0

image Laura_hands_and_knees_mouth_blowjob_animation1:
    "Laura_hands_and_knees_mouth_kiss"

    hands_and_knees_mouth_blowjob_animation1

image Laura_hands_and_knees_mouth_blowjob_animation2:
    "Laura_hands_and_knees_mouth_agape"

    hands_and_knees_mouth_blowjob_animation2

image Laura_hands_and_knees_mouth_blowjob_animation3:
    "Laura_hands_and_knees_mouth_agape"

    hands_and_knees_mouth_blowjob_animation3

image Laura_hands_and_knees_mouth_deepthroat_animation0:
    "Laura_hands_and_knees_mouth_deepthroat"

    hands_and_knees_mouth_deepthroat_animation0

image Laura_hands_and_knees_mouth_deepthroat_animation1:
    "Laura_hands_and_knees_mouth_deepthroat"

    hands_and_knees_mouth_deepthroat_animation1

image Laura_hands_and_knees_tongue_blowjob_animation2:
    "Laura_hands_and_knees_tongue"

    hands_and_knees_tongue_blowjob_animation2

image Laura_hands_and_knees_hair_handjob_animation0:
    "Laura_hands_and_knees_hair"

    hands_and_knees_hair_handjob_animation0

image Laura_hands_and_knees_hair_handjob_animation1:
    "Laura_hands_and_knees_hair"

    hands_and_knees_hair_handjob_animation1

image Laura_hands_and_knees_hair_blowjob_animation0:
    "Laura_hands_and_knees_hair"

    hands_and_knees_hair_blowjob_animation0

image Laura_hands_and_knees_hair_blowjob_animation1:
    "Laura_hands_and_knees_hair"

    hands_and_knees_hair_blowjob_animation1

image Laura_hands_and_knees_hair_blowjob_animation2:
    "Laura_hands_and_knees_hair"

    hands_and_knees_hair_blowjob_animation2

image Laura_hands_and_knees_hair_blowjob_animation3:
    "Laura_hands_and_knees_hair"

    hands_and_knees_hair_blowjob_animation3

image Laura_hands_and_knees_hair_deepthroat_animation0:
    "Laura_hands_and_knees_hair"

    hands_and_knees_hair_deepthroat_animation0

image Laura_hands_and_knees_hair_deepthroat_animation1:
    "Laura_hands_and_knees_hair"

    hands_and_knees_hair_deepthroat_animation1

image Laura_hands_and_knees_male_body_handjob_animation0:
    "Laura_hands_and_knees_male_body"

    hands_and_knees_male_body_handjob_animation0

image Laura_hands_and_knees_male_body_handjob_animation1:
    "Laura_hands_and_knees_male_body"

    hands_and_knees_male_body_handjob_animation1

image Laura_hands_and_knees_male_body_blowjob_animation0:
    "Laura_hands_and_knees_male_body"

    hands_and_knees_male_body_blowjob_animation0

image Laura_hands_and_knees_male_body_blowjob_animation1:
    "Laura_hands_and_knees_male_body"

    hands_and_knees_male_body_blowjob_animation1

image Laura_hands_and_knees_male_body_blowjob_animation2:
    "Laura_hands_and_knees_male_body"

    hands_and_knees_male_body_blowjob_animation2

image Laura_hands_and_knees_male_body_blowjob_animation3:
    "Laura_hands_and_knees_male_body"

    hands_and_knees_male_body_blowjob_animation3

image Laura_hands_and_knees_male_body_deepthroat_animation0:
    "Laura_hands_and_knees_male_body"

    hands_and_knees_male_body_deepthroat_animation0

image Laura_hands_and_knees_male_body_deepthroat_animation1:
    "Laura_hands_and_knees_male_body"

    hands_and_knees_male_body_deepthroat_animation1

image Laura_hands_and_knees_thumb_handjob_animation0:
    "Laura_hands_and_knees_thumb"

    hands_and_knees_hand_handjob_animation0

image Laura_hands_and_knees_thumb_handjob_animation1:
    "Laura_hands_and_knees_thumb"

    hands_and_knees_hand_handjob_animation1

image Laura_hands_and_knees_thumb_blowjob_animation0:
    "Laura_hands_and_knees_thumb"

    hands_and_knees_hand_blowjob_animation0

image Laura_hands_and_knees_thumb_blowjob_animation1:
    "Laura_hands_and_knees_thumb"

    hands_and_knees_hand_blowjob_animation1

image Laura_hands_and_knees_thumb_blowjob_animation2:
    "Laura_hands_and_knees_thumb"

    hands_and_knees_hand_blowjob_animation2

image Laura_hands_and_knees_thumb_blowjob_animation3:
    "Laura_hands_and_knees_thumb"

    hands_and_knees_hand_blowjob_animation3

image Laura_hands_and_knees_cock_handjob_animation0:
    "Laura_hands_and_knees_cock"

    hands_and_knees_cock_handjob_animation0

image Laura_hands_and_knees_cock_handjob_animation1:
    "Laura_hands_and_knees_cock"

    hands_and_knees_cock_handjob_animation1

image Laura_hands_and_knees_cock_blowjob_animation0:
    "Laura_hands_and_knees_cock"

    hands_and_knees_cock_blowjob_animation0

image Laura_hands_and_knees_cock_blowjob_animation1:
    "Laura_hands_and_knees_cock"

    hands_and_knees_cock_blowjob_animation1

image Laura_hands_and_knees_cock_blowjob_animation2:
    "Laura_hands_and_knees_cock"

    hands_and_knees_cock_blowjob_animation2

image Laura_hands_and_knees_cock_blowjob_animation3:
    "Laura_hands_and_knees_cock"

    hands_and_knees_cock_blowjob_animation3

image Laura_hands_and_knees_cock_deepthroat_animation0:
    "Laura_hands_and_knees_cock"

    hands_and_knees_cock_deepthroat_animation0

image Laura_hands_and_knees_cock_deepthroat_animation1:
    "Laura_hands_and_knees_cock"

    hands_and_knees_cock_deepthroat_animation1

image Laura_hands_and_knees_saliva_handjob_animation0:
    "Laura_hands_and_knees_saliva"

    hands_and_knees_cock_handjob_animation0

image Laura_hands_and_knees_saliva_handjob_animation1:
    "Laura_hands_and_knees_saliva"

    hands_and_knees_cock_handjob_animation1

image Laura_hands_and_knees_saliva_blowjob_animation0:
    "Laura_hands_and_knees_saliva"

    hands_and_knees_cock_blowjob_animation0

image Laura_hands_and_knees_saliva_blowjob_animation1:
    "Laura_hands_and_knees_saliva"

    hands_and_knees_cock_blowjob_animation1

image Laura_hands_and_knees_saliva_blowjob_animation2:
    "Laura_hands_and_knees_saliva"

    hands_and_knees_cock_blowjob_animation2

image Laura_hands_and_knees_saliva_blowjob_animation3:
    "Laura_hands_and_knees_saliva"

    hands_and_knees_cock_blowjob_animation3

image Laura_hands_and_knees_saliva_deepthroat_animation0:
    "Laura_hands_and_knees_saliva"

    hands_and_knees_cock_deepthroat_animation0

image Laura_hands_and_knees_saliva_deepthroat_animation1:
    "Laura_hands_and_knees_saliva"

    hands_and_knees_cock_deepthroat_animation1

image Laura_hands_and_knees_spunk_tip_handjob_animation0:
    "Laura_hands_and_knees_spunk_tip"

    hands_and_knees_cock_handjob_animation0

image Laura_hands_and_knees_spunk_tip_handjob_animation1:
    "Laura_hands_and_knees_spunk_tip"

    hands_and_knees_cock_handjob_animation1

image Laura_hands_and_knees_spunk_tip_blowjob_animation0:
    "Laura_hands_and_knees_spunk_tip"

    hands_and_knees_cock_blowjob_animation0

image Laura_hands_and_knees_spunk_tip_blowjob_animation1:
    "Laura_hands_and_knees_spunk_tip"

    hands_and_knees_cock_blowjob_animation1

image Laura_hands_and_knees_spunk_tip_blowjob_animation2:
    "Laura_hands_and_knees_spunk_tip"

    hands_and_knees_cock_blowjob_animation2

image Laura_hands_and_knees_spunk_tip_blowjob_animation3:
    "Laura_hands_and_knees_spunk_tip"

    hands_and_knees_cock_blowjob_animation3

image Laura_hands_and_knees_spunk_tip_deepthroat_animation0:
    "Laura_hands_and_knees_spunk_tip"

    hands_and_knees_cock_deepthroat_animation0

image Laura_hands_and_knees_spunk_tip_deepthroat_animation1:
    "Laura_hands_and_knees_spunk_tip"

    hands_and_knees_cock_deepthroat_animation1

image Laura_hands_and_knees_mask_blowjob_animation3:
    "Laura_hands_and_knees_mask_agape"

    parallel:
        hands_and_knees_mask_blowjob_animation3
    parallel:
        hands_and_knees_head_blowjob_animation3

image Laura_hands_and_knees_mask_deepthroat_animation0:
    "Laura_hands_and_knees_mask_deepthroat"

    parallel:
        hands_and_knees_mask_deepthroat_animation0
    parallel:
        hands_and_knees_head_deepthroat_animation0

image Laura_hands_and_knees_mask_deepthroat_animation1:
    "Laura_hands_and_knees_mask_deepthroat"

    parallel:
        hands_and_knees_mask_deepthroat_animation1
    parallel:
        hands_and_knees_head_deepthroat_animation1

image Laura_hands_and_knees_hand_handjob_animation0:
    "Laura_hands_and_knees_hand"

    hands_and_knees_hand_handjob_animation0

image Laura_hands_and_knees_hand_handjob_animation1:
    "Laura_hands_and_knees_hand"

    hands_and_knees_hand_handjob_animation1

image Laura_hands_and_knees_hand_blowjob_animation0:
    "Laura_hands_and_knees_hand"

    hands_and_knees_hand_blowjob_animation0

image Laura_hands_and_knees_hand_blowjob_animation1:
    "Laura_hands_and_knees_hand"

    hands_and_knees_hand_blowjob_animation1

image Laura_hands_and_knees_hand_blowjob_animation2:
    "Laura_hands_and_knees_hand"

    hands_and_knees_hand_blowjob_animation2

image Laura_hands_and_knees_hand_blowjob_animation3:
    "Laura_hands_and_knees_hand"

    hands_and_knees_hand_blowjob_animation3

image Laura_hands_and_knees_torso_cum_in_mouth_animation:
    "Laura_hands_and_knees_torso"

    hands_and_knees_torso_cum_in_mouth_animation

image Laura_hands_and_knees_torso_cum_down_throat_animation:
    "Laura_hands_and_knees_torso"

    hands_and_knees_torso_cum_down_throat_animation

image Laura_hands_and_knees_left_arm_cum_in_mouth_animation:
    "Laura_hands_and_knees_left_arm"

    hands_and_knees_left_arm_cum_in_mouth_animation

image Laura_hands_and_knees_head_cum_in_mouth_animation:
    "Laura_hands_and_knees_head"

    hands_and_knees_head_cum_in_mouth_animation

image Laura_hands_and_knees_head_cum_down_throat_animation:
    "Laura_hands_and_knees_head"

    hands_and_knees_head_cum_down_throat_animation

image Laura_hands_and_knees_thumb_cumshot_animation:
    "Laura_hands_and_knees_thumb"

    hands_and_knees_hand_cumshot_animation

image Laura_hands_and_knees_thumb_cum_in_mouth_animation:
    "Laura_hands_and_knees_thumb"

    hands_and_knees_hand_cum_in_mouth_animation

image Laura_hands_and_knees_cock_cum_in_mouth_animation:
    "Laura_hands_and_knees_cock"

    hands_and_knees_cock_cum_in_mouth_animation

image Laura_hands_and_knees_cock_cumshot_animation:
    "Laura_hands_and_knees_cock"

    hands_and_knees_cock_cumshot_animation

image Laura_hands_and_knees_cock_cum_in_mouth_animation:
    "Laura_hands_and_knees_cock"

    hands_and_knees_cock_cum_in_mouth_animation

image Laura_hands_and_knees_cock_cum_down_throat_animation:
    "Laura_hands_and_knees_cock"

    hands_and_knees_cock_cum_down_throat_animation

image Laura_hands_and_knees_saliva_cumshot_animation:
    "Laura_hands_and_knees_saliva"

    hands_and_knees_cock_cumshot_animation

image Laura_hands_and_knees_saliva_cum_in_mouth_animation:
    "Laura_hands_and_knees_saliva"

    hands_and_knees_cock_cum_in_mouth_animation

image Laura_hands_and_knees_saliva_cum_down_throat_animation:
    "Laura_hands_and_knees_saliva"

    hands_and_knees_cock_cum_down_throat_animation

image Laura_hands_and_knees_spunk_tip_cumshot_animation:
    "Laura_hands_and_knees_spunk_tip"

    hands_and_knees_cock_cumshot_animation

image Laura_hands_and_knees_spunk_tip_cum_in_mouth_animation:
    "Laura_hands_and_knees_spunk_tip"

    hands_and_knees_cock_cum_in_mouth_animation

image Laura_hands_and_knees_spunk_tip_cum_down_throat_animation:
    "Laura_hands_and_knees_spunk_tip"

    hands_and_knees_cock_cum_down_throat_animation

image Laura_hands_and_knees_hand_cumshot_animation:
    "Laura_hands_and_knees_hand"

    hands_and_knees_hand_cumshot_animation

image Laura_hands_and_knees_hand_cum_in_mouth_animation:
    "Laura_hands_and_knees_hand"

    hands_and_knees_hand_cum_in_mouth_animation

image Laura_hands_and_knees_mouth_cum_in_mouth_animation:
    "Laura_hands_and_knees_mouth_agape"

    hands_and_knees_mouth_cum_in_mouth_animation

image Laura_hands_and_knees_mouth_cum_down_throat_animation:
    "Laura_hands_and_knees_mouth_deepthroat"

    hands_and_knees_mouth_cum_down_throat_animation

image Laura_hands_and_knees_mask_cum_in_mouth_animation:
    "Laura_hands_and_knees_mask_agape"

    parallel:
        hands_and_knees_mask_cum_in_mouth_animation
    parallel:
        hands_and_knees_head_cum_in_mouth_animation

image Laura_hands_and_knees_mask_cum_down_throat_animation:
    "Laura_hands_and_knees_mask_deepthroat"

    parallel:
        hands_and_knees_mask_cum_down_throat_animation
    parallel:
        hands_and_knees_head_cum_down_throat_animation
        
layeredimage Laura_hands_and_knees_cock_animations:
    if Player.orgasming and focused_Companion == Laura:
        "Laura_hands_and_knees_cock_[Player.orgasming]_animation"
    else:
        "Laura_hands_and_knees_cock_[Player.cock_Actions[0].animation_type]_animation[Player.cock_Actions[0].mode]"

    if not Player.saliva:
        Null()
    elif Player.orgasming and focused_Companion == Laura:
        "Laura_hands_and_knees_saliva_[Player.orgasming]_animation"
    else:
        "Laura_hands_and_knees_saliva_[Player.cock_Actions[0].animation_type]_animation[Player.cock_Actions[0].mode]"

    if not Player.spunk and not Player.orgasming:
        Null()
    elif Player.orgasming and focused_Companion == Laura:
        "Laura_hands_and_knees_spunk_tip_[Player.orgasming]_animation"
    else:
        "Laura_hands_and_knees_spunk_tip_[Player.cock_Actions[0].animation_type]_animation[Player.cock_Actions[0].mode]"

layeredimage Laura_hands_and_knees_mask_animations:
    if speed > 2.5 or speed <= 1.75:
        Null()
    elif intensity >= 2.0:
        At(At("Laura_hands_and_knees_mask_animations_temp", speed_200), intensity_200)
    elif intensity >= 1.75:
        At(At("Laura_hands_and_knees_mask_animations_temp", speed_200), intensity_175)
    elif intensity >= 1.5:
        At(At("Laura_hands_and_knees_mask_animations_temp", speed_200), intensity_150)
    elif intensity >= 1.25:
        At(At("Laura_hands_and_knees_mask_animations_temp", speed_200), intensity_125)
    elif intensity >= 1.0:
        At(At("Laura_hands_and_knees_mask_animations_temp", speed_200), intensity_100)
    elif intensity >= 0.75:
        At(At("Laura_hands_and_knees_mask_animations_temp", speed_200), intensity_075)
    elif intensity >= 0.5:
        At(At("Laura_hands_and_knees_mask_animations_temp", speed_200), intensity_050)
    elif intensity >= 0.25:
        At(At("Laura_hands_and_knees_mask_animations_temp", speed_200), intensity_025)
    else:
        At(At("Laura_hands_and_knees_mask_animations_temp", speed_200), intensity_000)

    if speed > 1.75 or speed <= 1.5:
        Null()
    elif intensity >= 2.0:
        At(At("Laura_hands_and_knees_mask_animations_temp", speed_175), intensity_200)
    elif intensity >= 1.75:
        At(At("Laura_hands_and_knees_mask_animations_temp", speed_175), intensity_175)
    elif intensity >= 1.5:
        At(At("Laura_hands_and_knees_mask_animations_temp", speed_175), intensity_150)
    elif intensity >= 1.25:
        At(At("Laura_hands_and_knees_mask_animations_temp", speed_175), intensity_125)
    elif intensity >= 1.0:
        At(At("Laura_hands_and_knees_mask_animations_temp", speed_175), intensity_100)
    elif intensity >= 0.75:
        At(At("Laura_hands_and_knees_mask_animations_temp", speed_175), intensity_075)
    elif intensity >= 0.5:
        At(At("Laura_hands_and_knees_mask_animations_temp", speed_175), intensity_050)
    elif intensity >= 0.25:
        At(At("Laura_hands_and_knees_mask_animations_temp", speed_175), intensity_025)
    else:
        At(At("Laura_hands_and_knees_mask_animations_temp", speed_175), intensity_000)

    if speed > 1.5 or speed <= 1.25:
        Null()
    elif intensity >= 2.0:
        At(At("Laura_hands_and_knees_mask_animations_temp", speed_150), intensity_200)
    elif intensity >= 1.75:
        At(At("Laura_hands_and_knees_mask_animations_temp", speed_150), intensity_175)
    elif intensity >= 1.5:
        At(At("Laura_hands_and_knees_mask_animations_temp", speed_150), intensity_150)
    elif intensity >= 1.25:
        At(At("Laura_hands_and_knees_mask_animations_temp", speed_150), intensity_125)
    elif intensity >= 1.0:
        At(At("Laura_hands_and_knees_mask_animations_temp", speed_150), intensity_100)
    elif intensity >= 0.75:
        At(At("Laura_hands_and_knees_mask_animations_temp", speed_150), intensity_075)
    elif intensity >= 0.5:
        At(At("Laura_hands_and_knees_mask_animations_temp", speed_150), intensity_050)
    elif intensity >= 0.25:
        At(At("Laura_hands_and_knees_mask_animations_temp", speed_150), intensity_025)
    else:
        At(At("Laura_hands_and_knees_mask_animations_temp", speed_150), intensity_000)
 
    if speed > 1.25 or speed <= 1.0:
        Null()
    elif intensity >= 2.0:
        At(At("Laura_hands_and_knees_mask_animations_temp", speed_125), intensity_200)
    elif intensity >= 1.75:
        At(At("Laura_hands_and_knees_mask_animations_temp", speed_125), intensity_175)
    elif intensity >= 1.5:
        At(At("Laura_hands_and_knees_mask_animations_temp", speed_125), intensity_150)
    elif intensity >= 1.25:
        At(At("Laura_hands_and_knees_mask_animations_temp", speed_125), intensity_125)
    elif intensity >= 1.0:
        At(At("Laura_hands_and_knees_mask_animations_temp", speed_125), intensity_100)
    elif intensity >= 0.75:
        At(At("Laura_hands_and_knees_mask_animations_temp", speed_125), intensity_075)
    elif intensity >= 0.5:
        At(At("Laura_hands_and_knees_mask_animations_temp", speed_125), intensity_050)
    elif intensity >= 0.25:
        At(At("Laura_hands_and_knees_mask_animations_temp", speed_125), intensity_025)
    else:
        At(At("Laura_hands_and_knees_mask_animations_temp", speed_125), intensity_000)
 
    if speed > 1.0 or speed <= 0.75:
        Null()
    elif intensity >= 2.0:
        At(At("Laura_hands_and_knees_mask_animations_temp", speed_100), intensity_200)
    elif intensity >= 1.75:
        At(At("Laura_hands_and_knees_mask_animations_temp", speed_100), intensity_175)
    elif intensity >= 1.5:
        At(At("Laura_hands_and_knees_mask_animations_temp", speed_100), intensity_150)
    elif intensity >= 1.25:
        At(At("Laura_hands_and_knees_mask_animations_temp", speed_100), intensity_125)
    elif intensity >= 1.0:
        At(At("Laura_hands_and_knees_mask_animations_temp", speed_100), intensity_100)
    elif intensity >= 0.75:
        At(At("Laura_hands_and_knees_mask_animations_temp", speed_100), intensity_075)
    elif intensity >= 0.5:
        At(At("Laura_hands_and_knees_mask_animations_temp", speed_100), intensity_050)
    elif intensity >= 0.25:
        At(At("Laura_hands_and_knees_mask_animations_temp", speed_100), intensity_025)
    else:
        At(At("Laura_hands_and_knees_mask_animations_temp", speed_100), intensity_000)

    if speed > 0.75 or speed <= 0.5:
        Null()
    elif intensity >= 2.0:
        At(At("Laura_hands_and_knees_mask_animations_temp", speed_075), intensity_200)
    elif intensity >= 1.75:
        At(At("Laura_hands_and_knees_mask_animations_temp", speed_075), intensity_175)
    elif intensity >= 1.5:
        At(At("Laura_hands_and_knees_mask_animations_temp", speed_075), intensity_150)
    elif intensity >= 1.25:
        At(At("Laura_hands_and_knees_mask_animations_temp", speed_075), intensity_125)
    elif intensity >= 1.0:
        At(At("Laura_hands_and_knees_mask_animations_temp", speed_075), intensity_100)
    elif intensity >= 0.75:
        At(At("Laura_hands_and_knees_mask_animations_temp", speed_075), intensity_075)
    elif intensity >= 0.5:
        At(At("Laura_hands_and_knees_mask_animations_temp", speed_075), intensity_050)
    elif intensity >= 0.25:
        At(At("Laura_hands_and_knees_mask_animations_temp", speed_075), intensity_025)
    else:
        At(At("Laura_hands_and_knees_mask_animations_temp", speed_075), intensity_000)

    if speed > 0.5 or speed <= 0.25:
        Null()
    elif intensity >= 2.0:
        At(At("Laura_hands_and_knees_mask_animations_temp", speed_050), intensity_200)
    elif intensity >= 1.75:
        At(At("Laura_hands_and_knees_mask_animations_temp", speed_050), intensity_175)
    elif intensity >= 1.5:
        At(At("Laura_hands_and_knees_mask_animations_temp", speed_050), intensity_150)
    elif intensity >= 1.25:
        At(At("Laura_hands_and_knees_mask_animations_temp", speed_050), intensity_125)
    elif intensity >= 1.0:
        At(At("Laura_hands_and_knees_mask_animations_temp", speed_050), intensity_100)
    elif intensity >= 0.75:
        At(At("Laura_hands_and_knees_mask_animations_temp", speed_050), intensity_075)
    elif intensity >= 0.5:
        At(At("Laura_hands_and_knees_mask_animations_temp", speed_050), intensity_050)
    elif intensity >= 0.25:
        At(At("Laura_hands_and_knees_mask_animations_temp", speed_050), intensity_025)
    else:
        At(At("Laura_hands_and_knees_mask_animations_temp", speed_050), intensity_000)

    if speed > 0.25 or speed <= 0.01:
        Null()
    elif intensity >= 2.0:
        At(At("Laura_hands_and_knees_mask_animations_temp", speed_025), intensity_200)
    elif intensity >= 1.75:
        At(At("Laura_hands_and_knees_mask_animations_temp", speed_025), intensity_175)
    elif intensity >= 1.5:
        At(At("Laura_hands_and_knees_mask_animations_temp", speed_025), intensity_150)
    elif intensity >= 1.25:
        At(At("Laura_hands_and_knees_mask_animations_temp", speed_025), intensity_125)
    elif intensity >= 1.0:
        At(At("Laura_hands_and_knees_mask_animations_temp", speed_025), intensity_100)
    elif intensity >= 0.75:
        At(At("Laura_hands_and_knees_mask_animations_temp", speed_025), intensity_075)
    elif intensity >= 0.5:
        At(At("Laura_hands_and_knees_mask_animations_temp", speed_025), intensity_050)
    elif intensity >= 0.25:
        At(At("Laura_hands_and_knees_mask_animations_temp", speed_025), intensity_025)
    else:
        At(At("Laura_hands_and_knees_mask_animations_temp", speed_025), intensity_000)

    if speed > 0.01 or speed < 0.0:
        Null()
    elif intensity >= 2.0:
        At(At("Laura_hands_and_knees_mask_animations_temp", speed_000), intensity_200)
    elif intensity >= 1.75:
        At(At("Laura_hands_and_knees_mask_animations_temp", speed_000), intensity_175)
    elif intensity >= 1.5:
        At(At("Laura_hands_and_knees_mask_animations_temp", speed_000), intensity_150)
    elif intensity >= 1.25:
        At(At("Laura_hands_and_knees_mask_animations_temp", speed_000), intensity_125)
    elif intensity >= 1.0:
        At(At("Laura_hands_and_knees_mask_animations_temp", speed_000), intensity_100)
    elif intensity >= 0.75:
        At(At("Laura_hands_and_knees_mask_animations_temp", speed_000), intensity_075)
    elif intensity >= 0.5:
        At(At("Laura_hands_and_knees_mask_animations_temp", speed_000), intensity_050)
    elif intensity >= 0.25:
        At(At("Laura_hands_and_knees_mask_animations_temp", speed_000), intensity_025)
    else:
        At(At("Laura_hands_and_knees_mask_animations_temp", speed_000), intensity_000)

layeredimage Laura_hands_and_knees_mask_animations_temp:
    if Player.orgasming in ["cum_in_mouth", "cum_down_throat"] and focused_Companion == Laura:
        "Laura_hands_and_knees_mask_[Player.orgasming]_animation"
    elif Laura.mouth_Actions and ((Laura.mouth_Actions[0].animation_type == "blowjob" and Laura.mouth_Actions[0].mode == 3) or Laura.mouth_Actions[0].animation_type == "deepthroat"):
        "Laura_hands_and_knees_mask_[Player.cock_Actions[0].animation_type]_animation[Player.cock_Actions[0].mode]"

image Laura_hands_and_knees_blinking:
    "characters/Laura/images/hands_and_knees/eyes_[Laura.eyes].webp"
    choice:
        4.5
    choice:
        4.0
    choice:
        3.5
    "characters/Laura/images/hands_and_knees/eyes_blink1.webp"
    0.023
    "characters/Laura/images/hands_and_knees/eyes_blink2.webp"
    0.023
    "characters/Laura/images/hands_and_knees/eyes_closed.webp"
    0.054
    "characters/Laura/images/hands_and_knees/eyes_blink2.webp"
    0.018
    "characters/Laura/images/hands_and_knees/eyes_blink1.webp"
    0.072
    repeat

image Laura_hands_and_knees_cumshot:
    "characters/Laura/images/hands_and_knees/spunk_jet.webp"

    anchor (int(2260*sex_sampling), int(2080*sex_sampling))
    offset (int(2260*sex_sampling), int(2080*sex_sampling))

    subpixel True
    transform_anchor True

    pos (0.0*sex_sampling, 0.0*sex_sampling)

    block:
        yzoom 0.0 alpha 1.0
        easein_cubic 0.2 yzoom 1.0 alpha 0.5
        linear 0.1 alpha 0.0
        pause 1.0
        repeat

        repeat