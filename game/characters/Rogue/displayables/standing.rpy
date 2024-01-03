transform Rogue_standing_head_animation:
    subpixel True
    transform_anchor True
    animation
    
    pos (0.0, 0.0)
    xzoom 1.0 yzoom 1.0
    rotate 0.0

    block:
        pause 5.7
        ease 2.0 rotate 1
        pause 6.2
        ease 2.0 rotate -1
        pause 3.9
        ease 2.0 rotate 0

        repeat

transform Rogue_standing_right_arm_animation:
    subpixel True
    transform_anchor True
    animation
    
    pos (0.0, 0.0)
    xzoom 1.0 yzoom 1.0
    rotate 0.0

    block:
        pause 3.8
        ease 2.0 rotate 0
        pause 4.7
        ease 2.0 rotate 2
        pause 6.1
        ease 2.0 rotate -2

        repeat

transform Rogue_standing_left_arm_animation:
    subpixel True
    transform_anchor True
    animation
    
    pos (0.0, 0.0)
    xzoom 1.0 yzoom 1.0
    rotate 0.0

    block:
        pause 4.3
        ease 2.0 rotate 0
        pause 6.8
        ease 2.0 rotate 2
        pause 4.7
        ease 2.0 rotate -2

        repeat
    
image Rogue_sprite standing:
    contains:
        "Rogue_standing_temp"
        
    xysize (int(2500*character_sampling), int(4500*character_sampling))

layeredimage Rogue_standing_temp:
    if Rogue.hovered:
        "Rogue_standing" at hover
    elif Rogue.check_traits("orgasming"):
        "Rogue_standing" at tremble(20)
    else:
        "Rogue_standing"

layeredimage Rogue_standing:
    if not Player.left_hand_Actions or Rogue not in Player.left_hand_Actions[0].Targets:
        Null()
    elif Player.left_hand_Actions[0].animation_type == "grab_ass":
        "Rogue_standing_male_left_arm_grab_ass_animation[Player.left_hand_Actions[0].mode]" at change_offset(Rogue_standing_ass_position[0], Rogue_standing_ass_position[1])

    if not Player.right_hand_Actions or Rogue not in Player.right_hand_Actions[0].Targets:
        Null()
    elif Player.right_hand_Actions[0].animation_type == "grab_ass":
        "Rogue_standing_male_right_arm_grab_ass_animation[Player.right_hand_Actions[0].mode]" at change_offset(Rogue_standing_ass_position[0], Rogue_standing_ass_position[1])

    if Rogue.check_traits("ground_shadow"):
        "characters/Rogue/images/standing/ground_shadow.webp" at Transform(blend = "multiply")

    if renpy.get_screen("Wardrobe_screen"):
        "Rogue_standing_hair_back"
    else:
        "Rogue_standing_hair_back" at Rogue_standing_head_animation

    if Rogue.left_arm in ["bra", "touch_ass"]:
        "characters/Rogue/images/standing/left_forearm_[Rogue.left_arm].webp"

    if not Rogue.Clothes["bodysuit"].string:
        Null()
    elif Rogue.Clothes["bodysuit"].string in ["greenyellow_classic_suit"] and Rogue.Clothes["bodysuit"].state == 1:
        Null()
    elif Rogue.left_arm in ["bra", "touch_ass"]:
        "characters/Rogue/images/standing/bodysuit_[Rogue.Clothes[bodysuit].string]_left_forearm_sleeve_[Rogue.left_arm].webp"

    if not Rogue.Clothes["top"].string:
        Null()
    elif Rogue.left_arm in ["bra", "touch_ass"]:
        "characters/Rogue/images/standing/top_[Rogue.Clothes[top].string]_left_forearm_sleeve_[Rogue.left_arm].webp"

    if Rogue.Clothes["gloves"].string not in ["yellow_gloves"]:
        Null()
    elif Rogue.left_arm in ["bra", "touch_ass"]:
        "characters/Rogue/images/standing/gloves_[Rogue.Clothes[gloves].string]_left_[Rogue.left_arm].webp"

    if not Rogue.Clothes["sleeves"].string:
        Null()
    elif Rogue.left_arm in ["bra", "touch_ass"]:
        "characters/Rogue/images/standing/sleeves_[Rogue.Clothes[sleeves].string]_left_[Rogue.left_arm].webp"

    if Rogue.right_arm not in ["bra", "extended", "fight", "fist", "hip", "neutral", "touch_pussy"]:
        Null()
    elif renpy.get_screen("Wardrobe_screen"):
        "Rogue_standing_right_arm"
    elif Rogue.right_arm == "neutral":
        "Rogue_standing_right_arm" at Rogue_standing_right_arm_animation
    else:
        "Rogue_standing_right_arm"

    always:
        "Rogue_standing_body"

    if Rogue.left_arm in ["fist", "hip", "neutral"]:
        "characters/Rogue/images/standing/left_arm_[Rogue.left_arm]_shadow.webp" at Transform(blend = "multiply")

    if Rogue.left_arm not in ["bra", "extended", "fight", "fist", "grope", "hip", "neutral", "rub_neck", "touch_ass"]:
        Null()
    elif renpy.get_screen("Wardrobe_screen"):
        "Rogue_standing_left_arm"
    elif Rogue.left_arm == "neutral":
        "Rogue_standing_left_arm" at Rogue_standing_left_arm_animation
    else:
        "Rogue_standing_left_arm"

    if not Rogue.Clothes["bra"].string or Rogue.Clothes["bodysuit"].string or Rogue.Clothes["jacket"].string:
        Null()
    elif Rogue.left_arm == "crossed" and Rogue.right_arm == "crossed":
        "characters/Rogue/images/standing/bra_[Rogue.Clothes[bra].string]_left_shoulder_[Rogue.Clothes[bra].state]_crossed.webp"
    elif Rogue.left_arm == "grope" and Rogue.Clothes["bra"].state == 1:
        "characters/Rogue/images/standing/bra_[Rogue.Clothes[bra].string]_left_shoulder_1_grope.webp"
    else:
        "characters/Rogue/images/standing/bra_[Rogue.Clothes[bra].string]_left_shoulder_[Rogue.Clothes[bra].state].webp"

    if Rogue.left_arm not in ["bra", "fight", "fist", "grope", "hip", "neutral", "rub_neck", "touch_ass"]:
        Null()
    elif renpy.get_screen("Wardrobe_screen"):
        "Rogue_standing_left_sleeve"
    elif Rogue.left_arm == "neutral":
        "Rogue_standing_left_sleeve" at Rogue_standing_left_arm_animation
    else:
        "Rogue_standing_left_sleeve"

    if Rogue.right_arm in ["hip", "touch_pussy"]:
        "characters/Rogue/images/standing/right_forearm_[Rogue.right_arm]_shadow.webp" at Transform(blend = "multiply")

    if Rogue.right_arm in ["hip", "touch_pussy"]:
        "characters/Rogue/images/standing/right_forearm_[Rogue.right_arm].webp"

    if not Rogue.Clothes["bodysuit"].string:
        Null()
    elif Rogue.Clothes["bodysuit"].string in ["greenyellow_classic_suit"] and Rogue.Clothes["bodysuit"].state == 1:
        Null()
    elif Rogue.right_arm in ["hip", "touch_pussy"]:
        "characters/Rogue/images/standing/bodysuit_[Rogue.Clothes[bodysuit].string]_right_forearm_sleeve_[Rogue.right_arm].webp"

    if Rogue.Clothes["gloves"].string not in ["black_gloves"]:
        Null()
    elif Rogue.right_arm in ["hip", "touch_pussy"]:
        "characters/Rogue/images/standing/gloves_[Rogue.Clothes[gloves].string]_right_[Rogue.right_arm].webp"

    if not Rogue.Clothes["top"].string:
        Null()
    elif Rogue.right_arm in ["hip", "touch_pussy"]:
        "characters/Rogue/images/standing/top_[Rogue.Clothes[top].string]_right_forearm_sleeve_[Rogue.right_arm].webp"

    if Rogue.Clothes["gloves"].string not in ["yellow_gloves"]:
        Null()
    elif Rogue.right_arm in ["hip", "touch_pussy"]:
        "characters/Rogue/images/standing/gloves_[Rogue.Clothes[gloves].string]_right_[Rogue.right_arm].webp"
        
    if not Rogue.Clothes["sleeves"].string:
        Null()
    elif Rogue.right_arm in ["hip", "touch_pussy"]:
        "characters/Rogue/images/standing/sleeves_[Rogue.Clothes[sleeves].string]_right_[Rogue.right_arm].webp"
        
    if Rogue.left_arm in ["grope"]:
        "characters/Rogue/images/standing/left_forearm_[Rogue.left_arm].webp"

    if not Rogue.Clothes["bodysuit"].string:
        Null()
    elif Rogue.Clothes["bodysuit"].string in ["greenyellow_classic_suit"] and Rogue.Clothes["bodysuit"].state == 1:
        Null()
    elif Rogue.left_arm in ["grope"]:
        "characters/Rogue/images/standing/bodysuit_[Rogue.Clothes[bodysuit].string]_left_forearm_sleeve_[Rogue.left_arm].webp"

    if Rogue.Clothes["gloves"].string not in ["black_gloves"]:
        Null()
    elif Rogue.left_arm in ["grope"]:
        "characters/Rogue/images/standing/gloves_[Rogue.Clothes[gloves].string]_left_[Rogue.left_arm].webp"

    if not Rogue.Clothes["top"].string:
        Null()
    elif Rogue.left_arm in ["grope"]:
        "characters/Rogue/images/standing/top_[Rogue.Clothes[top].string]_left_forearm_sleeve_[Rogue.left_arm].webp"

    if Rogue.Clothes["gloves"].string not in ["yellow_gloves"]:
        Null()
    elif Rogue.left_arm in ["grope"]:
        "characters/Rogue/images/standing/gloves_[Rogue.Clothes[gloves].string]_left_[Rogue.left_arm].webp"

    if not Rogue.Clothes["sleeves"].string:
        Null()
    elif Rogue.left_arm in ["grope"]:
        "characters/Rogue/images/standing/sleeves_[Rogue.Clothes[sleeves].string]_left_[Rogue.left_arm].webp"

    if not Rogue.Clothes["jacket"].string:
        Null()
    elif Rogue.left_arm in ["grope"]:
        "characters/Rogue/images/standing/jacket_[Rogue.Clothes[jacket].string]_left_forearm_sleeve_[Rogue.left_arm].webp"

    if not Player.left_hand_Actions or Rogue not in Player.left_hand_Actions[0].Targets:
        Null()
    elif Player.left_hand_Actions[0].animation_type == "choke":
        "Rogue_standing_male_left_arm_choke_animation[Player.left_hand_Actions[0].mode]" at change_offset(Rogue_standing_neck_position[0], Rogue_standing_neck_position[1])

    if not Player.right_hand_Actions or Rogue not in Player.right_hand_Actions[0].Targets:
        Null()
    elif Player.right_hand_Actions[0].animation_type == "choke":
        "Rogue_standing_male_right_arm_choke_animation[Player.right_hand_Actions[0].mode]" at change_offset(Rogue_standing_neck_position[0], Rogue_standing_neck_position[1])

    if renpy.get_screen("Wardrobe_screen"):
        "Rogue_standing_head"
    else:
        "Rogue_standing_head" at Rogue_standing_head_animation

    if Rogue.right_arm in ["fight"]:
        "characters/Rogue/images/standing/right_forearm_[Rogue.right_arm].webp"

    if not Rogue.Clothes["bodysuit"].string:
        Null()
    elif Rogue.right_arm in ["fight"]:
        "characters/Rogue/images/standing/bodysuit_[Rogue.Clothes[bodysuit].string]_right_forearm_sleeve_[Rogue.right_arm].webp"

    if Rogue.Clothes["gloves"].string not in ["black_gloves"]:
        Null()
    elif Rogue.right_arm in ["fight"]:
        "characters/Rogue/images/standing/gloves_[Rogue.Clothes[gloves].string]_right_[Rogue.right_arm].webp"

    if not Rogue.Clothes["top"].string:
        Null()
    elif Rogue.right_arm in ["fight"]:
        "characters/Rogue/images/standing/top_[Rogue.Clothes[top].string]_right_forearm_sleeve_[Rogue.right_arm].webp"

    if Rogue.Clothes["gloves"].string not in ["yellow_gloves"]:
        Null()
    elif Rogue.right_arm in ["fight"]:
        "characters/Rogue/images/standing/gloves_[Rogue.Clothes[gloves].string]_right_[Rogue.right_arm].webp"
        
    if not Rogue.Clothes["sleeves"].string:
        Null()
    elif Rogue.right_arm in ["fight"]:
        "characters/Rogue/images/standing/sleeves_[Rogue.Clothes[sleeves].string]_right_[Rogue.right_arm].webp"

    if not Rogue.Clothes["jacket"].string:
        Null()
    elif Rogue.right_arm in ["fight"]:
        "characters/Rogue/images/standing/jacket_[Rogue.Clothes[jacket].string]_right_forearm_sleeve_[Rogue.right_arm].webp"
        
    if Rogue.left_arm in ["rub_neck"]:
        "characters/Rogue/images/standing/left_forearm_[Rogue.left_arm]_shadow.webp" at Transform(blend = "multiply")

    if Rogue.left_arm in ["fight", "rub_neck"]:
        "characters/Rogue/images/standing/left_forearm_[Rogue.left_arm].webp"

    if not Rogue.Clothes["bodysuit"].string:
        Null()
    elif Rogue.left_arm in ["extended", "fight", "rub_neck"]:
        "characters/Rogue/images/standing/bodysuit_[Rogue.Clothes[bodysuit].string]_left_forearm_sleeve_[Rogue.left_arm].webp"

    if Rogue.Clothes["gloves"].string not in ["black_gloves"]:
        Null()
    elif Rogue.left_arm in ["extended", "fight", "rub_neck"]:
        "characters/Rogue/images/standing/gloves_[Rogue.Clothes[gloves].string]_left_[Rogue.left_arm].webp"

    if not Rogue.Clothes["top"].string:
        Null()
    elif Rogue.left_arm in ["extended", "fight", "rub_neck"]:
        "characters/Rogue/images/standing/top_[Rogue.Clothes[top].string]_left_forearm_sleeve_[Rogue.left_arm].webp"

    if Rogue.Clothes["gloves"].string not in ["yellow_gloves"]:
        Null()
    elif Rogue.left_arm in ["extended", "fight", "rub_neck"]:
        "characters/Rogue/images/standing/gloves_[Rogue.Clothes[gloves].string]_left_[Rogue.left_arm].webp"

    if not Rogue.Clothes["sleeves"].string:
        Null()
    elif Rogue.left_arm in ["extended", "fight", "rub_neck"]:
        "characters/Rogue/images/standing/sleeves_[Rogue.Clothes[sleeves].string]_left_[Rogue.left_arm].webp"

    if not Rogue.Clothes["jacket"].string:
        Null()
    elif Rogue.left_arm in ["extended"]:
        "characters/Rogue/images/standing/jacket_[Rogue.Clothes[jacket].string]_left_forearm_sleeve_[Rogue.left_arm].webp"

    if Rogue.spunk["hand"] and Rogue.right_arm in ["extended"]:
        "characters/Rogue/images/standing/spunk_hand1.webp"

    if Rogue.spunk["hand"] == 2 and Rogue.right_arm in ["extended"]:
        "characters/Rogue/images/standing/spunk_hand2.webp"

    if not Player.left_hand_Actions or Rogue not in Player.left_hand_Actions[0].Targets:
        Null()
    elif Player.left_hand_Actions[0].animation_type == "touch_breasts" and Rogue.right_breast_Actions and Player.left_hand_Actions[0].animation_type == Rogue.right_breast_Actions[0].animation_type:
        "Rogue_standing_male_left_arm_touch_right_breast_animation[Player.left_hand_Actions[0].mode]" at change_offset(Rogue_standing_right_breast_position[0], Rogue_standing_right_breast_position[1])
    elif Player.left_hand_Actions[0].animation_type == "touch_breasts" and Rogue.left_breast_Actions and Player.left_hand_Actions[0].animation_type == Rogue.left_breast_Actions[0].animation_type:
        "Rogue_standing_male_left_arm_touch_left_breast_animation[Player.left_hand_Actions[0].mode]" at change_offset(Rogue_standing_left_breast_position[0], Rogue_standing_left_breast_position[1])
    elif Player.left_hand_Actions[0].animation_type == "pinch_nipples" and Rogue.right_nipple_Actions and Player.left_hand_Actions[0].animation_type == Rogue.right_nipple_Actions[0].animation_type:
        "Rogue_standing_male_left_arm_touch_right_breast_animation[Player.left_hand_Actions[0].mode]" at change_offset(Rogue_standing_right_nipple_position[0], Rogue_standing_right_nipple_position[1])
    elif Player.left_hand_Actions[0].animation_type == "pinch_nipples" and Rogue.left_nipple_Actions and Player.left_hand_Actions[0].animation_type == Rogue.left_nipple_Actions[0].animation_type:
        "Rogue_standing_male_left_arm_touch_left_breast_animation[Player.left_hand_Actions[0].mode]" at change_offset(Rogue_standing_left_nipple_position[0], Rogue_standing_left_nipple_position[1])
    elif Player.left_hand_Actions[0].animation_type == "touch_thighs":
        "Rogue_standing_male_left_arm_touch_thighs_animation[Player.left_hand_Actions[0].mode]" at change_offset(Rogue_standing_thigh_position[0], Rogue_standing_thigh_position[1])
    elif Player.left_hand_Actions[0].animation_type == "touch_thighs_higher":
        "Rogue_standing_male_left_arm_touch_thighs_higher_animation[Player.left_hand_Actions[0].mode]" at change_offset(Rogue_standing_thigh_higher_position[0], Rogue_standing_thigh_higher_position[1])
    elif Player.left_hand_Actions[0].animation_type == "touch_pussy":
        "Rogue_standing_male_left_arm_touch_pussy_animation[Player.left_hand_Actions[0].mode]" at change_offset(Rogue_standing_pussy_position[0], Rogue_standing_pussy_position[1])

    if not Player.right_hand_Actions or Rogue not in Player.right_hand_Actions[0].Targets:
        Null()
    elif Player.right_hand_Actions[0].animation_type == "touch_breasts" and Rogue.right_breast_Actions and Player.right_hand_Actions[0].animation_type == Rogue.right_breast_Actions[0].animation_type:
        "Rogue_standing_male_right_arm_touch_right_breast_animation[Player.right_hand_Actions[0].mode]" at change_offset(Rogue_standing_right_breast_position[0], Rogue_standing_right_breast_position[1])
    elif Player.right_hand_Actions[0].animation_type == "touch_breasts" and Rogue.left_breast_Actions and Player.right_hand_Actions[0].animation_type == Rogue.left_breast_Actions[0].animation_type:
        "Rogue_standing_male_right_arm_touch_left_breast_animation[Player.right_hand_Actions[0].mode]" at change_offset(Rogue_standing_left_breast_position[0], Rogue_standing_left_breast_position[1])
    elif Player.right_hand_Actions[0].animation_type == "pinch_nipples" and Rogue.right_nipple_Actions and Player.right_hand_Actions[0].animation_type == Rogue.right_nipple_Actions[0].animation_type:
        "Rogue_standing_male_right_arm_touch_right_breast_animation[Player.right_hand_Actions[0].mode]" at change_offset(Rogue_standing_right_nipple_position[0], Rogue_standing_right_nipple_position[1])
    elif Player.right_hand_Actions[0].animation_type == "pinch_nipples" and Rogue.left_nipple_Actions and Player.right_hand_Actions[0].animation_type == Rogue.left_nipple_Actions[0].animation_type:
        "Rogue_standing_male_right_arm_touch_left_breast_animation[Player.right_hand_Actions[0].mode]" at change_offset(Rogue_standing_left_nipple_position[0], Rogue_standing_left_nipple_position[1])
    elif Player.right_hand_Actions[0].animation_type == "touch_thighs":
        "Rogue_standing_male_right_arm_touch_thighs_animation[Player.right_hand_Actions[0].mode]" at change_offset(Rogue_standing_thigh_position[0], Rogue_standing_thigh_position[1])
    elif Player.right_hand_Actions[0].animation_type == "touch_thighs_higher":
        "Rogue_standing_male_right_arm_touch_thighs_higher_animation[Player.right_hand_Actions[0].mode]" at change_offset(Rogue_standing_thigh_higher_position[0], Rogue_standing_thigh_higher_position[1])
    elif Player.right_hand_Actions[0].animation_type == "touch_pussy":
        "Rogue_standing_male_right_arm_touch_pussy_animation[Player.right_hand_Actions[0].mode]" at change_offset(Rogue_standing_pussy_position[0], Rogue_standing_pussy_position[1])

    if not Player.mouth_Actions or Rogue not in Player.mouth_Actions[0].Targets:
        Null()
    elif Player.mouth_Actions[0].animation_type in ["suck_nipples"] and Rogue.left_nipple_Actions and Player.mouth_Actions[0].animation_type == Rogue.left_nipple_Actions[0].animation_type:
        "Rogue_standing_male_head_suck_left_nipple_animation[Player.mouth_Actions[0].mode]" at change_offset(Rogue_standing_left_nipple_position[0], Rogue_standing_left_nipple_position[1])
    elif Player.mouth_Actions[0].animation_type in ["suck_nipples"] and Rogue.right_nipple_Actions and Player.mouth_Actions[0].animation_type == Rogue.right_nipple_Actions[0].animation_type:
        "Rogue_standing_male_head_suck_right_nipple_animation[Player.mouth_Actions[0].mode]" at change_offset(Rogue_standing_right_nipple_position[0], Rogue_standing_right_nipple_position[1])

layeredimage Rogue_standing_hair_back: 
    if Rogue.check_traits("wet") or Rogue.Clothes["hair"].string == "wet":
        "characters/Rogue/images/standing/hair_back_wet.webp"
    else:
        "characters/Rogue/images/standing/hair_back_[Rogue.Clothes[hair].string].webp"

    anchor (int(1340*character_sampling), int(1300*character_sampling))
    offset (int(1340*character_sampling), int(1300*character_sampling))

layeredimage Rogue_standing_right_arm:
    always:
        "characters/Rogue/images/standing/right_arm_[Rogue.right_arm].webp"

    if not Rogue.Clothes["bodysuit"].string:
        Null()
    elif Rogue.Clothes["bodysuit"].string in ["greenyellow_classic_suit"] and Rogue.Clothes["bodysuit"].state == 1:
        Null()
    elif Rogue.Clothes["bodysuit"].string in ["greenyellow_classic_suit"] and Rogue.right_arm in ["bra", "extended", "fist", "neutral"]:
        "characters/Rogue/images/standing/bodysuit_[Rogue.Clothes[bodysuit].string]_right_sleeve_[Rogue.right_arm].webp"

    if Rogue.Clothes["gloves"].string not in ["black_gloves"]:
        Null()
    elif Rogue.right_arm in ["extended", "fist", "neutral"]:
        "characters/Rogue/images/standing/gloves_[Rogue.Clothes[gloves].string]_right_[Rogue.right_arm].webp"

    if not Rogue.Clothes["top"].string:
        Null()
    elif Rogue.Clothes["top"].string in ["black_lowcut_top"] and Rogue.right_arm in ["extended", "fight", "fist", "neutral"]:
        "characters/Rogue/images/standing/top_[Rogue.Clothes[top].string]_right_sleeve_[Rogue.right_arm].webp"
    elif Rogue.Clothes["top"].string in ["green_mesh_top"] and Rogue.right_arm in ["bra", "extended", "neutral"]:
        "characters/Rogue/images/standing/top_[Rogue.Clothes[top].string]_right_sleeve_[Rogue.right_arm].webp"

    if Rogue.Clothes["gloves"].string not in ["yellow_gloves"]:
        Null()
    elif Rogue.right_arm in ["extended", "fist", "neutral"]:
        "characters/Rogue/images/standing/gloves_[Rogue.Clothes[gloves].string]_right_[Rogue.right_arm].webp"

    if not Rogue.Clothes["sleeves"].string:
        Null()
    elif Rogue.right_arm in ["extended", "fist", "neutral"]:
        "characters/Rogue/images/standing/sleeves_[Rogue.Clothes[sleeves].string]_right_[Rogue.right_arm].webp"

    if not Rogue.Clothes["jacket"].string:
        Null()
    elif Rogue.right_arm == "fist":
        "characters/Rogue/images/standing/jacket_[Rogue.Clothes[jacket].string]_right_sleeve_neutral.webp"
    elif Rogue.Clothes["jacket"].string in ["brown_classic_jacket"] and Rogue.right_arm in ["extended", "neutral", "touch_pussy"]:
        "characters/Rogue/images/standing/jacket_[Rogue.Clothes[jacket].string]_right_sleeve_[Rogue.right_arm].webp"

    anchor (int(1075*character_sampling), int(1545*character_sampling))
    offset (int(1075*character_sampling), int(1545*character_sampling))

layeredimage Rogue_standing_body:
    if Rogue.Clothes["jacket"].string:
        "characters/Rogue/images/standing/jacket_[Rogue.Clothes[jacket].string]_back.webp"

    always:
        "characters/Rogue/images/standing/body.webp"

    always:
        "characters/Rogue/images/standing/right_foot.webp"
        
    always:
        "characters/Rogue/images/standing/left_foot.webp"

    if Rogue.piercings["labia"] in ["barbell", "both"]:
        "characters/Rogue/images/standing/labia_piercings_barbell.webp"

    if Rogue.piercings["labia"] in ["ring", "both"]:
        "characters/Rogue/images/standing/labia_piercings_ring.webp"

    if Rogue.desire >= 75 or Rogue.History.check("orgasmed", tracker = "recent"):
        "characters/Rogue/images/standing/grool.webp"
    elif Rogue.desire >= 50:
        "characters/Rogue/images/standing/grool.webp" at Transform(alpha = 0.5)
    elif Rogue.desire >= 25:
        "characters/Rogue/images/standing/grool.webp" at Transform(alpha = 0.1)

    if Rogue.creampie["pussy"]:
        "characters/Rogue/images/standing/creampie1.webp"

    if Rogue.creampie["pussy"] == 2:
        "characters/Rogue/images/standing/creampie2.webp"

    if "pubic" in Rogue.body_hair_growing.keys():
        "characters/Rogue/images/standing/pubes_growing.webp"

    if Rogue.body_hair["pubic"]:
        "characters/Rogue/images/standing/pubes_[Rogue.body_hair[pubic]].webp"

    if Rogue.remote_vibrator is None:
        Null()
    elif Rogue.remote_vibrator > 0.0:
        "characters/Rogue/images/standing/remote_vibrator.webp" at vibrating
    else:
        "characters/Rogue/images/standing/remote_vibrator.webp"

    if Rogue.piercings["belly"]:
        "characters/Rogue/images/standing/belly_piercing.webp"

    if Rogue.spunk["belly"]:
        "characters/Rogue/images/standing/spunk_belly1.webp"

    if Rogue.spunk["belly"] == 2:
        "characters/Rogue/images/standing/spunk_belly2.webp"

    if Rogue.Clothes["underwear"].string:
        "characters/Rogue/images/standing/underwear_[Rogue.Clothes[underwear].string]_[Rogue.Clothes[underwear].state].webp"

    if Rogue.Clothes["bodysuit"].string:
        "characters/Rogue/images/standing/bodysuit_[Rogue.Clothes[bodysuit].string]_lower.webp"

    if Rogue.Clothes["pants"].string:
        "characters/Rogue/images/standing/pants_[Rogue.Clothes[pants].string]_[Rogue.Clothes[pants].state].webp"

    if Rogue.Clothes["belt"].string:
        "characters/Rogue/images/standing/belt_[Rogue.Clothes[belt].string].webp"

    if Rogue.Clothes["footwear"].string:
        "characters/Rogue/images/standing/footwear_[Rogue.Clothes[footwear].string].webp"

    if not Rogue.Clothes["bodysuit"].string:
        Null()
    elif Rogue.Clothes["bodysuit"].string in ["greenyellow_classic_suit"] and Rogue.Clothes["bodysuit"].state == 1:
        Null()
    elif Rogue.right_arm == "fist":
        "characters/Rogue/images/standing/bodysuit_[Rogue.Clothes[bodysuit].string]_right_shoulder_neutral.webp"
    elif Rogue.right_arm in ["bra", "extended", "fight", "hip", "neutral", "touch_pussy"]:
        "characters/Rogue/images/standing/bodysuit_[Rogue.Clothes[bodysuit].string]_right_shoulder_[Rogue.right_arm].webp"

    if not Rogue.Clothes["top"].string:
        Null()
    elif Rogue.Clothes["top"].string in ["black_lowcut_top"] and Rogue.right_arm in ["bra", "hip", "touch_pussy"]:
        "characters/Rogue/images/standing/top_[Rogue.Clothes[top].string]_right_shoulder_[Rogue.right_arm].webp"

    if not Rogue.Clothes["jacket"].string:
        Null()
    elif Rogue.right_arm == "fist":
        "characters/Rogue/images/standing/jacket_[Rogue.Clothes[jacket].string]_right_shoulder_neutral.webp"
    elif Rogue.Clothes["jacket"].string == "brown_classic_jacket" and Rogue.right_arm in ["bra", "extended", "fight", "hip", "neutral", "touch_pussy"]:
        "characters/Rogue/images/standing/jacket_[Rogue.Clothes[jacket].string]_right_shoulder_[Rogue.right_arm].webp"

    if Rogue.right_arm in ["crossed"]:
        "characters/Rogue/images/standing/right_arm_[Rogue.right_arm].webp"

    if Rogue.left_arm in ["crossed"]:
        "characters/Rogue/images/standing/left_arm_[Rogue.left_arm].webp"

    if Rogue.right_arm in ["hip"]:
        "characters/Rogue/images/standing/right_forearm_[Rogue.right_arm].webp"

    if not Rogue.Clothes["bodysuit"].string:
        Null()
    elif Rogue.Clothes["bodysuit"].string in ["greenyellow_classic_suit"] and Rogue.Clothes["bodysuit"].state == 1:
        Null()
    elif Rogue.right_arm in ["hip"]:
        "characters/Rogue/images/standing/bodysuit_[Rogue.Clothes[bodysuit].string]_right_forearm_sleeve_[Rogue.right_arm].webp"

    if Rogue.Clothes["gloves"].string not in ["black_gloves"]:
        Null()
    elif Rogue.right_arm in ["hip"]:
        "characters/Rogue/images/standing/gloves_[Rogue.Clothes[gloves].string]_right_[Rogue.right_arm].webp"

    if not Rogue.Clothes["top"].string:
        Null()
    elif Rogue.right_arm in ["hip"]:
        "characters/Rogue/images/standing/top_[Rogue.Clothes[top].string]_right_forearm_sleeve_[Rogue.right_arm].webp"

    if Rogue.Clothes["gloves"].string not in ["yellow_gloves"]:
        Null()
    elif Rogue.right_arm in ["hip"]:
        "characters/Rogue/images/standing/gloves_[Rogue.Clothes[gloves].string]_right_[Rogue.right_arm].webp"

    if not Rogue.Clothes["sleeves"].string:
        Null()
    elif Rogue.right_arm in ["hip"]:
        "characters/Rogue/images/standing/sleeves_[Rogue.Clothes[sleeves].string]_right_[Rogue.right_arm].webp"

    if Rogue.left_arm == "crossed" and Rogue.right_arm == "crossed":
        "characters/Rogue/images/standing/breasts_crossed_shadow.webp" at Transform(blend = "multiply")
    elif Rogue.check_traits("breasts_supported"):
        "characters/Rogue/images/standing/breasts_supported_shadow.webp" at Transform(blend = "multiply")
    else:
        "characters/Rogue/images/standing/breasts_shadow.webp" at Transform(blend = "multiply")

    if Rogue.left_arm == "crossed" and Rogue.right_arm == "crossed":
        "characters/Rogue/images/standing/breasts_crossed.webp"
    elif Rogue.check_traits("breasts_supported"):
        "characters/Rogue/images/standing/breasts_supported.webp"
    else:
        "characters/Rogue/images/standing/breasts.webp"

    if Rogue.left_arm == "grope":
        "characters/Rogue/images/standing/breasts_grope.webp"

    if Rogue.piercings["nipple"] not in ["barbell", "both"]:
        Null()
    elif Rogue.left_arm == "crossed" and Rogue.right_arm == "crossed":
        "characters/Rogue/images/standing/nipple_piercings_barbell_crossed.webp"
    elif Rogue.check_traits("breasts_supported"):
        "characters/Rogue/images/standing/nipple_piercings_barbell_supported.webp"
    elif Rogue.left_arm == "grope":
        "characters/Rogue/images/standing/nipple_piercings_barbell_grope.webp"
    else:
        "characters/Rogue/images/standing/nipple_piercings_barbell.webp"

    if Rogue.piercings["nipple"] not in ["ring", "both"]:
        Null()
    elif Rogue.left_arm == "crossed" and Rogue.right_arm == "crossed":
        "characters/Rogue/images/standing/nipple_piercings_ring_crossed.webp"
    elif Rogue.check_traits("breasts_supported"):
        "characters/Rogue/images/standing/nipple_piercings_ring_supported.webp"
    elif Rogue.left_arm == "grope":
        "characters/Rogue/images/standing/nipple_piercings_ring_grope.webp"
    else:
        "characters/Rogue/images/standing/nipple_piercings_ring.webp"

    if Rogue.spunk["breasts"]:
        "characters/Rogue/images/standing/spunk_breasts1.webp"

    if Rogue.spunk["breasts"] == 2:
        "characters/Rogue/images/standing/spunk_breasts2.webp"
        
    if not Rogue.Clothes["bra"].string:
        Null()
    elif Rogue.Clothes["bodysuit"].string in ["greenyellow_classic_suit"]:
        Null()
    elif Rogue.left_arm == "crossed" and Rogue.right_arm == "crossed":
        "characters/Rogue/images/standing/bra_[Rogue.Clothes[bra].string]_[Rogue.Clothes[bra].state]_crossed.webp"
    elif Rogue.left_arm == "grope" and Rogue.Clothes["bra"].state == 1:
        "characters/Rogue/images/standing/bra_[Rogue.Clothes[bra].string]_1_grope.webp"
    else:
        "characters/Rogue/images/standing/bra_[Rogue.Clothes[bra].string]_[Rogue.Clothes[bra].state].webp"

    if not Rogue.Clothes["bodysuit"].string:
        Null()
    elif Rogue.left_arm == "crossed" and Rogue.right_arm == "crossed" and Rogue.Clothes["bodysuit"].state != 1:
        "characters/Rogue/images/standing/bodysuit_[Rogue.Clothes[bodysuit].string]_[Rogue.Clothes[bodysuit].state]_crossed.webp"
    else:
        "characters/Rogue/images/standing/bodysuit_[Rogue.Clothes[bodysuit].string]_[Rogue.Clothes[bodysuit].state].webp"

    if not Rogue.Clothes["top"].string:
        Null()
    elif Rogue.left_arm == "crossed" and Rogue.right_arm == "crossed":
        "characters/Rogue/images/standing/top_[Rogue.Clothes[top].string]_[Rogue.Clothes[top].state]_crossed.webp"
    elif Rogue.left_arm == "grope" and Rogue.Clothes["top"].state == 1 and not Rogue.check_traits("breasts_supported"):
        "characters/Rogue/images/standing/top_[Rogue.Clothes[top].string]_1_grope.webp"
    elif Rogue.check_traits("breasts_supported"):
        "characters/Rogue/images/standing/top_[Rogue.Clothes[top].string]_[Rogue.Clothes[top].state]_supported.webp"
    else:
        "characters/Rogue/images/standing/top_[Rogue.Clothes[top].string]_[Rogue.Clothes[top].state].webp"

    if not Rogue.Clothes["jacket"].string:
        Null()
    elif Rogue.left_arm == "crossed" and Rogue.right_arm == "crossed":
        "characters/Rogue/images/standing/jacket_[Rogue.Clothes[jacket].string]_[Rogue.Clothes[jacket].state]_crossed.webp"
    elif Rogue.left_arm == "grope" and Rogue.Clothes["jacket"].string in ["brown_classic_jacket"]:
        "characters/Rogue/images/standing/jacket_[Rogue.Clothes[jacket].string]_1_grope.webp"
    elif Rogue.left_arm == "grope" and Rogue.Clothes["jacket"].state == 1:
        "characters/Rogue/images/standing/jacket_[Rogue.Clothes[jacket].string]_1_grope.webp"
    else:
        "characters/Rogue/images/standing/jacket_[Rogue.Clothes[jacket].string]_[Rogue.Clothes[jacket].state].webp"

image Rogue_standing_left_arm:
    "characters/Rogue/images/standing/left_arm_[Rogue.left_arm].webp"

    anchor (int(1590*character_sampling), int(1530*character_sampling))
    offset (int(1590*character_sampling), int(1530*character_sampling))

layeredimage Rogue_standing_left_sleeve:
    if not Rogue.Clothes["bodysuit"].string:
        Null()
    elif Rogue.Clothes["bodysuit"].string in ["greenyellow_classic_suit"] and Rogue.Clothes["bodysuit"].state == 1:
        Null()
    else:
        "characters/Rogue/images/standing/bodysuit_[Rogue.Clothes[bodysuit].string]_left_sleeve_[Rogue.left_arm].webp"

    if Rogue.Clothes["gloves"].string not in ["black_gloves"]:
        Null()
    elif Rogue.left_arm in ["fist", "hip", "neutral"]:
        "characters/Rogue/images/standing/gloves_[Rogue.Clothes[gloves].string]_left_[Rogue.left_arm].webp"

    if not Rogue.Clothes["top"].string:
        Null()
    elif Rogue.Clothes["top"].string not in ["black_lowcut_top"] and Rogue.left_arm == "fist":
        "characters/Rogue/images/standing/top_[Rogue.Clothes[top].string]_left_sleeve_neutral.webp"
    else:
        "characters/Rogue/images/standing/top_[Rogue.Clothes[top].string]_left_sleeve_[Rogue.left_arm].webp"

    if Rogue.Clothes["gloves"].string not in ["yellow_gloves"]:
        Null()
    elif Rogue.left_arm in ["fist", "hip", "neutral"]:
        "characters/Rogue/images/standing/gloves_[Rogue.Clothes[gloves].string]_left_[Rogue.left_arm].webp"

    if not Rogue.Clothes["sleeves"].string:
        Null()
    elif Rogue.left_arm in ["fist", "hip", "neutral"]:
        "characters/Rogue/images/standing/sleeves_[Rogue.Clothes[sleeves].string]_left_[Rogue.left_arm].webp"

    if not Rogue.Clothes["jacket"].string:
        Null()
    elif Rogue.left_arm == "fist":
        "characters/Rogue/images/standing/jacket_[Rogue.Clothes[jacket].string]_left_sleeve_neutral.webp"
    else:
        "characters/Rogue/images/standing/jacket_[Rogue.Clothes[jacket].string]_left_sleeve_[Rogue.left_arm].webp"

    anchor (int(1590*character_sampling), int(1530*character_sampling))
    offset (int(1590*character_sampling), int(1530*character_sampling))

layeredimage Rogue_standing_head:
    always:
        "characters/Rogue/images/standing/head.webp"

    always:
        "characters/Rogue/images/standing/mouth_[Rogue.mouth].webp"

    if Rogue.eyes in ["closed", "down", "left", "right", "squint", "up", "wink"]:
        "characters/Rogue/images/standing/eyes_[Rogue.eyes].webp"
    else:
        "Rogue_standing_blinking"

    always:
        "characters/Rogue/images/standing/brows_[Rogue.brows].webp"

    if Rogue.blush:
        "characters/Rogue/images/standing/blush[Rogue.blush].webp"

    always:
        "characters/Rogue/images/standing/makeup_purple_eyeshadow.webp"

    if Rogue.Clothes["face_inner_accessory"].string:
        "characters/Rogue/images/standing/face_inner_accessory_[Rogue.Clothes[face_inner_accessory].string].webp"

    if Rogue.spunk["mouth"] and Rogue.mouth in ["agape", "open"]:
        "characters/Rogue/images/standing/spunk_mouth1_agape.webp"

    if Rogue.spunk["mouth"] == 2 and Rogue.mouth in ["agape", "open"]:
        "characters/Rogue/images/standing/spunk_mouth2_agape.webp"

    if Rogue.spunk["mouth"] and Rogue.mouth in ["tongue"]:
        "characters/Rogue/images/standing/spunk_mouth1_tongue.webp"

    if Rogue.spunk["mouth"] == 2 and Rogue.mouth in ["tongue"]:
        "characters/Rogue/images/standing/spunk_mouth2_tongue.webp"

    if not Rogue.spunk["chin"]:
        Null()
    elif Rogue.mouth in ["agape", "open", "tongue"]:
        "characters/Rogue/images/standing/spunk_chin1_open.webp"
    else:
        "characters/Rogue/images/standing/spunk_chin1.webp"

    if Rogue.spunk["chin"] != 2:
        Null()
    elif Rogue.mouth in ["agape", "open", "tongue"]:
        "characters/Rogue/images/standing/spunk_chin2_open.webp"
    else:
        "characters/Rogue/images/standing/spunk_chin2.webp"

    if Rogue.spunk["face"]:
        "characters/Rogue/images/standing/spunk_face1.webp"

    if Rogue.spunk["face"] == 2:
        "characters/Rogue/images/standing/spunk_face2.webp"

    if Rogue.check_traits("wet") or Rogue.Clothes["hair"].string == "wet":
        "characters/Rogue/images/standing/hair_wet_shadow.webp" at Transform(blend = "multiply")
    else:
        "characters/Rogue/images/standing/hair_[Rogue.Clothes[hair].string]_shadow.webp" at Transform(blend = "multiply")

    if Rogue.check_traits("wet") or Rogue.Clothes["hair"].string == "wet":
        "characters/Rogue/images/standing/hair_wet.webp"
    else:
        "characters/Rogue/images/standing/hair_[Rogue.Clothes[hair].string].webp"

    if Rogue.spunk["hair"]:
        "characters/Rogue/images/standing/spunk_hair1_[Rogue.Clothes[hair].string].webp"

    if Rogue.spunk["hair"] == 2:
        "characters/Rogue/images/standing/spunk_hair2_[Rogue.Clothes[hair].string].webp"

    anchor (int(1340*character_sampling), int(1300*character_sampling))
    offset (int(1340*character_sampling), int(1300*character_sampling))

image Rogue_standing_blinking:
    "characters/Rogue/images/standing/eyes_[Rogue.eyes].webp"
    choice:
        4.5
    choice:
        4.0
    choice:
        3.5
    "characters/Rogue/images/standing/eyes_blink1.webp"
    0.023
    "characters/Rogue/images/standing/eyes_blink2.webp"
    0.023
    "characters/Rogue/images/standing/eyes_closed.webp"
    0.054
    "characters/Rogue/images/standing/eyes_blink2.webp"
    0.018
    "characters/Rogue/images/standing/eyes_blink1.webp"
    0.072
    repeat

layeredimage Rogue_standing_male_left_arm:
    if Player.left_hand_Actions[0].animation_type in ["touch_thighs", "touch_thighs_higher", "touch_breasts", "touch_pussy", "grab_ass"]:
        "Player_left_arm_fondle"
    elif Player.left_hand_Actions[0].animation_type in ["choke", "pinch_nipples"]:
        "Player_left_arm_pinch"

layeredimage Rogue_standing_male_right_arm:
    if Player.right_hand_Actions[0].animation_type in ["touch_thighs", "touch_thighs_higher", "touch_breasts", "touch_pussy", "grab_ass"]:
        "Player_right_arm_fondle"
    elif Player.right_hand_Actions[0].animation_type in ["choke", "pinch_nipples"]:
        "Player_right_arm_pinch"

layeredimage Rogue_standing_male_head:
    if Player.check_traits("body_visible"):
        "Player_head"

    if Player.mouth_Actions and Rogue in Player.mouth_Actions[0].Targets and Player.mouth_Actions[0].animation_type in ["suck_nipples", "eat_pussy", "eat_ass"]:
        "Rogue_standing_male_tongue_animation[Player.mouth_Actions[0].mode]"

image Rogue_standing_male_tongue:
    "Player_tongue"
    
image Rogue_standing_male_left_arm_choke_animation0:
    "Rogue_standing_male_left_arm"

    standing_male_left_arm_choke_animation0

image Rogue_standing_male_left_arm_choke_animation1:
    "Rogue_standing_male_left_arm"

    standing_male_left_arm_choke_animation1

image Rogue_standing_male_left_arm_touch_thighs_animation0:
    "Rogue_standing_male_left_arm"

    standing_male_left_arm_touch_thighs_animation0

image Rogue_standing_male_left_arm_touch_thighs_animation1:
    "Rogue_standing_male_left_arm"

    standing_male_left_arm_touch_thighs_animation1

image Rogue_standing_male_left_arm_touch_thighs_higher_animation0:
    "Rogue_standing_male_left_arm"

    standing_male_left_arm_touch_thighs_higher_animation0

image Rogue_standing_male_left_arm_touch_thighs_higher_animation1:
    "Rogue_standing_male_left_arm"

    standing_male_left_arm_touch_thighs_higher_animation1

image Rogue_standing_male_left_arm_touch_left_breast_animation0:
    "Rogue_standing_male_left_arm"

    standing_male_left_arm_touch_left_breast_animation0

image Rogue_standing_male_left_arm_touch_left_breast_animation1:
    "Rogue_standing_male_left_arm"

    standing_male_left_arm_touch_left_breast_animation1

image Rogue_standing_male_left_arm_touch_right_breast_animation0:
    "Rogue_standing_male_left_arm"

    standing_male_left_arm_touch_right_breast_animation0

image Rogue_standing_male_left_arm_touch_right_breast_animation1:
    "Rogue_standing_male_left_arm"

    standing_male_left_arm_touch_right_breast_animation1

image Rogue_standing_male_left_arm_touch_pussy_animation0:
    "Rogue_standing_male_left_arm"

    standing_male_left_arm_touch_pussy_animation0

image Rogue_standing_male_left_arm_touch_pussy_animation1:
    "Rogue_standing_male_left_arm"

    standing_male_left_arm_touch_pussy_animation1

image Rogue_standing_male_left_arm_grab_ass_animation0:
    "Rogue_standing_male_left_arm"

    standing_male_left_arm_grab_ass_animation0

image Rogue_standing_male_left_arm_grab_ass_animation1:
    "Rogue_standing_male_left_arm"

    standing_male_left_arm_grab_ass_animation1
    
image Rogue_standing_male_right_arm_choke_animation0:
    "Rogue_standing_male_right_arm"

    standing_male_right_arm_choke_animation0

image Rogue_standing_male_right_arm_choke_animation1:
    "Rogue_standing_male_right_arm"

    standing_male_right_arm_choke_animation1

image Rogue_standing_male_right_arm_touch_thighs_animation0:
    "Rogue_standing_male_right_arm"

    standing_male_right_arm_touch_thighs_animation0

image Rogue_standing_male_right_arm_touch_thighs_animation1:
    "Rogue_standing_male_right_arm"

    standing_male_right_arm_touch_thighs_animation1

image Rogue_standing_male_right_arm_touch_thighs_higher_animation0:
    "Rogue_standing_male_right_arm"

    standing_male_right_arm_touch_thighs_higher_animation0

image Rogue_standing_male_right_arm_touch_thighs_higher_animation1:
    "Rogue_standing_male_right_arm"

    standing_male_right_arm_touch_thighs_higher_animation1

image Rogue_standing_male_right_arm_touch_left_breast_animation0:
    "Rogue_standing_male_right_arm"

    standing_male_right_arm_touch_left_breast_animation0

image Rogue_standing_male_right_arm_touch_left_breast_animation1:
    "Rogue_standing_male_right_arm"

    standing_male_right_arm_touch_left_breast_animation1

image Rogue_standing_male_right_arm_touch_right_breast_animation0:
    "Rogue_standing_male_right_arm"

    standing_male_right_arm_touch_right_breast_animation0

image Rogue_standing_male_right_arm_touch_right_breast_animation1:
    "Rogue_standing_male_right_arm"

    standing_male_right_arm_touch_right_breast_animation1

image Rogue_standing_male_right_arm_touch_pussy_animation0:
    "Rogue_standing_male_right_arm"

    standing_male_right_arm_touch_pussy_animation0

image Rogue_standing_male_right_arm_touch_pussy_animation1:
    "Rogue_standing_male_right_arm"

    standing_male_right_arm_touch_pussy_animation1

image Rogue_standing_male_right_arm_grab_ass_animation0:
    "Rogue_standing_male_right_arm"

    standing_male_right_arm_grab_ass_animation0

image Rogue_standing_male_right_arm_grab_ass_animation1:
    "Rogue_standing_male_right_arm"

    standing_male_right_arm_grab_ass_animation1

image Rogue_standing_male_head_suck_left_nipple_animation0:
    "Rogue_standing_male_head"

    standing_male_head_suck_left_nipple_animation0

image Rogue_standing_male_head_suck_left_nipple_animation1:
    "Rogue_standing_male_head"

    standing_male_head_suck_left_nipple_animation1

image Rogue_standing_male_head_suck_right_nipple_animation0:
    "Rogue_standing_male_head"

    standing_male_head_suck_right_nipple_animation0

image Rogue_standing_male_head_suck_right_nipple_animation1:
    "Rogue_standing_male_head"

    standing_male_head_suck_right_nipple_animation1

image Rogue_standing_male_tongue_animation0:
    "Rogue_standing_male_tongue"

    standing_male_tongue_animation0

image Rogue_standing_male_tongue_animation1:
    "Rogue_standing_male_tongue"

    standing_male_tongue_animation1