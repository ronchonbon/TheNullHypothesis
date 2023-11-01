transform Rogue_standing_head_animation:
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

transform Rogue_standing_right_arm_animation:
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
            choice:
                ease 2.0 rotate 2

        repeat

transform Rogue_standing_left_arm1_animation:
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
            choice:
                ease 2.0 rotate 2

        repeat

transform Rogue_standing_left_arm2_animation:
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
            choice:
                ease 2.0 rotate 2

        repeat
    
image Rogue_sprite standing:
    contains:
        "Rogue_standing_temp"
        
    xysize (int(1650*character_sampling), int(3450*character_sampling))

layeredimage Rogue_standing_temp:
    if Rogue.hovered:
        At("Rogue_standing", hover)
    else:
        "Rogue_standing"

layeredimage Rogue_standing:
    if not Player.left_hand_Actions or Rogue not in Player.left_hand_Actions[0].Targets:
        Null()
    elif Player.left_hand_Actions[0].animation_type == "grab_ass":
        At("Rogue_standing_male_left_arm_grab_ass_animation[Player.left_hand_Actions[0].mode]", change_offset(Rogue_standing_ass_position[0], Rogue_standing_ass_position[1]))

    if not Player.right_hand_Actions or Rogue not in Player.right_hand_Actions[0].Targets:
        Null()
    elif Player.right_hand_Actions[0].animation_type == "grab_ass":
        At("Rogue_standing_male_right_arm_grab_ass_animation[Player.right_hand_Actions[0].mode]", change_offset(Rogue_standing_ass_position[0], Rogue_standing_ass_position[1]))

    if renpy.get_screen("Wardrobe_screen"):
        "Rogue_standing_hair_back"
    else:
        At("Rogue_standing_hair_back", Rogue_standing_head_animation)

    if Rogue.Clothes["jacket"].string in ["leather_jacket", "plaid_coat"]:
        "characters/Rogue/images/standing/jacket_[Rogue.Clothes[jacket].string]_back.webp"

    if renpy.get_screen("Wardrobe_screen"):
        "Rogue_standing_right_arm"
    else:
        At("Rogue_standing_right_arm", Rogue_standing_right_arm_animation)
        
    if Rogue.Clothes["jacket"].string in ["leather_jacket", "plaid_coat"]:
        "characters/Rogue/images/standing/jacket_[Rogue.Clothes[jacket].string]_mid.webp"
    elif Rogue.Clothes["jacket"].string == "NIN_shirt" and Rogue.Clothes["jacket"].state == 0 and Rogue.breasts_supported:
        "characters/Rogue/images/standing/jacket_NIN_shirt_mid_supported.webp"
    elif Rogue.Clothes["jacket"].string == "NIN_shirt" and Rogue.Clothes["jacket"].state == 0:
        "characters/Rogue/images/standing/jacket_NIN_shirt_mid.webp"

    always:
        "Rogue_standing_body"

    if Rogue.left_arm_pose == 2:
        Null()
    elif renpy.get_screen("Wardrobe_screen"):
        "Rogue_standing_left_arm1"
    else:
        At("Rogue_standing_left_arm1", Rogue_standing_left_arm1_animation)

    if Rogue.Clothes["neck"].string == "maroon_scarf":
        "characters/Rogue/images/standing/neck[Rogue.left_arm_pose]_maroon_scarf.webp"
    elif Rogue.Clothes["neck"].string:
        "characters/Rogue/images/standing/neck_[Rogue.Clothes[neck].string].webp"
            
    if not Player.left_hand_Actions or Rogue not in Player.left_hand_Actions[0].Targets:
        Null()
    elif Player.left_hand_Actions[0].animation_type == "choke":
        At("Rogue_standing_male_left_arm_choke_animation[Player.left_hand_Actions[0].mode]", change_offset(Rogue_standing_neck_position[0], Rogue_standing_neck_position[1]))

    if not Player.right_hand_Actions or Rogue not in Player.right_hand_Actions[0].Targets:
        Null()
    elif Player.right_hand_Actions[0].animation_type == "choke":
        At("Rogue_standing_male_right_arm_choke_animation[Player.right_hand_Actions[0].mode]", change_offset(Rogue_standing_neck_position[0], Rogue_standing_neck_position[1]))

    if renpy.get_screen("Wardrobe_screen"):
        "Rogue_standing_head"
    else:
        At("Rogue_standing_head", Rogue_standing_head_animation)

    if Rogue.left_arm_pose == 1:
        Null()
    elif renpy.get_screen("Wardrobe_screen"):
        "Rogue_standing_left_arm2"
    else:
        At("Rogue_standing_left_arm2", Rogue_standing_left_arm2_animation)

    if not Player.left_hand_Actions or Rogue not in Player.left_hand_Actions[0].Targets:
        Null()
    elif Player.left_hand_Actions[0].animation_type == "touch_breasts" and Rogue.right_breast_Actions and Player.left_hand_Actions[0].animation_type == Rogue.right_breast_Actions[0].animation_type:
        At("Rogue_standing_male_left_arm_touch_right_breast_animation[Player.left_hand_Actions[0].mode]", change_offset(Rogue_standing_right_breast_position[0], Rogue_standing_right_breast_position[1]))
    elif Player.left_hand_Actions[0].animation_type == "touch_breasts" and Rogue.left_breast_Actions and Player.left_hand_Actions[0].animation_type == Rogue.left_breast_Actions[0].animation_type:
        At("Rogue_standing_male_left_arm_touch_left_breast_animation[Player.left_hand_Actions[0].mode]", change_offset(Rogue_standing_left_breast_position[0], Rogue_standing_left_breast_position[1]))
    elif Player.left_hand_Actions[0].animation_type == "pinch_nipples" and Rogue.right_nipple_Actions and Player.left_hand_Actions[0].animation_type == Rogue.right_nipple_Actions[0].animation_type:
        At("Rogue_standing_male_left_arm_touch_right_breast_animation[Player.left_hand_Actions[0].mode]", change_offset(Rogue_standing_right_nipple_position[0], Rogue_standing_right_nipple_position[1]))
    elif Player.left_hand_Actions[0].animation_type == "pinch_nipples" and Rogue.left_nipple_Actions and Player.left_hand_Actions[0].animation_type == Rogue.left_nipple_Actions[0].animation_type:
        At("Rogue_standing_male_left_arm_touch_left_breast_animation[Player.left_hand_Actions[0].mode]", change_offset(Rogue_standing_left_nipple_position[0], Rogue_standing_left_nipple_position[1]))
    elif Player.left_hand_Actions[0].animation_type == "touch_thighs":
        At("Rogue_standing_male_left_arm_touch_thighs_animation[Player.left_hand_Actions[0].mode]", change_offset(Rogue_standing_thigh_position[0], Rogue_standing_thigh_position[1]))
    elif Player.left_hand_Actions[0].animation_type == "touch_thighs_higher":
        At("Rogue_standing_male_left_arm_touch_thighs_higher_animation[Player.left_hand_Actions[0].mode]", change_offset(Rogue_standing_thigh_higher_position[0], Rogue_standing_thigh_higher_position[1]))
    elif Player.left_hand_Actions[0].animation_type == "touch_pussy":
        At("Rogue_standing_male_left_arm_touch_pussy_animation[Player.left_hand_Actions[0].mode]", change_offset(Rogue_standing_pussy_position[0], Rogue_standing_pussy_position[1]))

    if not Player.right_hand_Actions or Rogue not in Player.right_hand_Actions[0].Targets:
        Null()
    elif Player.right_hand_Actions[0].animation_type == "touch_breasts" and Rogue.right_breast_Actions and Player.right_hand_Actions[0].animation_type == Rogue.right_breast_Actions[0].animation_type:
        At("Rogue_standing_male_right_arm_touch_right_breast_animation[Player.right_hand_Actions[0].mode]", change_offset(Rogue_standing_right_breast_position[0], Rogue_standing_right_breast_position[1]))
    elif Player.right_hand_Actions[0].animation_type == "touch_breasts" and Rogue.left_breast_Actions and Player.right_hand_Actions[0].animation_type == Rogue.left_breast_Actions[0].animation_type:
        At("Rogue_standing_male_right_arm_touch_left_breast_animation[Player.right_hand_Actions[0].mode]", change_offset(Rogue_standing_left_breast_position[0], Rogue_standing_left_breast_position[1]))
    elif Player.right_hand_Actions[0].animation_type == "pinch_nipples" and Rogue.right_nipple_Actions and Player.right_hand_Actions[0].animation_type == Rogue.right_nipple_Actions[0].animation_type:
        At("Rogue_standing_male_right_arm_touch_right_breast_animation[Player.right_hand_Actions[0].mode]", change_offset(Rogue_standing_right_nipple_position[0], Rogue_standing_right_nipple_position[1]))
    elif Player.right_hand_Actions[0].animation_type == "pinch_nipples" and Rogue.left_nipple_Actions and Player.right_hand_Actions[0].animation_type == Rogue.left_nipple_Actions[0].animation_type:
        At("Rogue_standing_male_right_arm_touch_left_breast_animation[Player.right_hand_Actions[0].mode]", change_offset(Rogue_standing_left_nipple_position[0], Rogue_standing_left_nipple_position[1]))
    elif Player.right_hand_Actions[0].animation_type == "touch_thighs":
        At("Rogue_standing_male_right_arm_touch_thighs_animation[Player.right_hand_Actions[0].mode]", change_offset(Rogue_standing_thigh_position[0], Rogue_standing_thigh_position[1]))
    elif Player.right_hand_Actions[0].animation_type == "touch_thighs_higher":
        At("Rogue_standing_male_right_arm_touch_thighs_higher_animation[Player.right_hand_Actions[0].mode]", change_offset(Rogue_standing_thigh_higher_position[0], Rogue_standing_thigh_higher_position[1]))
    elif Player.right_hand_Actions[0].animation_type == "touch_pussy":
        At("Rogue_standing_male_right_arm_touch_pussy_animation[Player.right_hand_Actions[0].mode]", change_offset(Rogue_standing_pussy_position[0], Rogue_standing_pussy_position[1]))

    if not Player.mouth_Actions or Rogue not in Player.mouth_Actions[0].Targets:
        Null()
    elif Player.mouth_Actions[0].animation_type in ["suck_nipples"] and Rogue.left_nipple_Actions and Player.mouth_Actions[0].animation_type == Rogue.left_nipple_Actions[0].animation_type:
        At("Rogue_standing_male_head_suck_left_nipple_animation[Player.mouth_Actions[0].mode]", change_offset(Rogue_standing_left_nipple_position[0], Rogue_standing_left_nipple_position[1]))
    elif Player.mouth_Actions[0].animation_type in ["suck_nipples"] and Rogue.right_nipple_Actions and Player.mouth_Actions[0].animation_type == Rogue.right_nipple_Actions[0].animation_type:
        At("Rogue_standing_male_head_suck_right_nipple_animation[Player.mouth_Actions[0].mode]", change_offset(Rogue_standing_right_nipple_position[0], Rogue_standing_right_nipple_position[1]))

image Rogue_standing_hair_back:
    "characters/Rogue/images/standing/hair_back.webp"

    anchor (int(1088*character_sampling), int(512*character_sampling))
    offset (int(1088*character_sampling), int(512*character_sampling))

layeredimage Rogue_standing_right_arm:
    always:
        "characters/Rogue/images/standing/right_arm[Rogue.right_arm_pose].webp"

    if Rogue.Clothes["gloves"].string == "black_gloves":
        "characters/Rogue/images/standing/gloves_black_gloves_right[Rogue.right_arm_pose].webp"
            
    if Rogue.Clothes["bodysuit"].string:
        "characters/Rogue/images/standing/bodysuit_[Rogue.Clothes[bodysuit].string]_right_sleeve[Rogue.right_arm_pose].webp"

    if Rogue.Clothes["dress"].string == "sweater_dress":
        "characters/Rogue/images/standing/dress_sweater_dress_right_sleeve[Rogue.right_arm_pose].webp"

    if Rogue.Clothes["top"].string and Rogue.Clothes["top"].string not in ["black_top", "green_mesh_top"]:
        "characters/Rogue/images/standing/top_[Rogue.Clothes[top].string]_right_sleeve[Rogue.right_arm_pose].webp"

    if Rogue.Clothes["sleeves"].string:
        "characters/Rogue/images/standing/sleeves_[Rogue.Clothes[sleeves].string]_right[Rogue.right_arm_pose].webp"

    if Rogue.Clothes["top"].string in ["black_top", "green_mesh_top"]:
        "characters/Rogue/images/standing/top_[Rogue.Clothes[top].string]_right_sleeve[Rogue.right_arm_pose].webp"

    if Rogue.Clothes["jacket"].string and Rogue.Clothes["jacket"].string != "NIN_shirt":
        "characters/Rogue/images/standing/jacket_[Rogue.Clothes[jacket].string]_right_sleeve[Rogue.right_arm_pose].webp"
            
    if Rogue.Clothes["gloves"].string == "yellow_gloves":
        "characters/Rogue/images/standing/gloves_yellow_gloves_right[Rogue.right_arm_pose].webp"
            
    if Rogue.spunk["hand"]:
        "characters/Rogue/images/standing/spunk_right_hand[Rogue.right_arm_pose].webp"
    
    anchor (int(787*character_sampling), int(791*character_sampling))
    offset (int(787*character_sampling), int(791*character_sampling))

layeredimage Rogue_standing_body:
    always:
        "characters/Rogue/images/standing/body.webp"

    if Rogue.breasts_supported:
        "characters/Rogue/images/standing/breasts_supported.webp"
    else:
        "characters/Rogue/images/standing/breasts.webp"

    if not Rogue.tan_lines["full"]:
        Null()
    elif Rogue.breasts_supported:
        "characters/Rogue/images/standing/tan_lines_[Rogue.tan_lines[full]]_supported.webp"
    else:
        "characters/Rogue/images/standing/tan_lines_[Rogue.tan_lines[full]].webp"

    if Rogue.tan_lines["bottom"]:
        "characters/Rogue/images/standing/tan_lines_[Rogue.tan_lines[bottom]].webp"

    if not Rogue.tan_lines["top"]:
        Null()
    elif Rogue.breasts_supported:
        "characters/Rogue/images/standing/tan_lines_[Rogue.tan_lines[top]]_supported.webp"
    else:
        "characters/Rogue/images/standing/tan_lines_[Rogue.tan_lines[top]].webp"

    if Rogue.piercings["labia"] in ["barbell", "both"]:
        "characters/Rogue/images/standing/labia_piercings_barbell.webp"

    if Rogue.piercings["labia"] in ["ring", "both"]:
        "characters/Rogue/images/standing/labia_piercings_ring.webp"

    if Rogue.piercings["belly"]:
        "characters/Rogue/images/standing/belly_piercing.webp"

    if Rogue.piercings["nipple"] in ["barbell", "both"]:
        "characters/Rogue/images/standing/nipple_piercings_barbell.webp"

    if Rogue.piercings["nipple"] in ["ring", "both"]:
        "characters/Rogue/images/standing/nipple_piercings_ring.webp"

    if Rogue.Clothes["nipple_accessories"].string:
        "characters/Rogue/images/standing/nipple_accessories_[Rogue.Clothes[nipple_accessories].string].webp"

    if Rogue.pubes_growing:
        "characters/Rogue/images/standing/pubes_growing.webp"

    if Rogue.pubes:
        "characters/Rogue/images/standing/pubes_[Rogue.pubes].webp"

    if Rogue.remote_vibrator:
        "characters/Rogue/images/standing/remote_vibrator.webp"

    if Rogue.creampie["pussy"]:
        "characters/Rogue/images/standing/creampie.webp"

    if Rogue.Clothes["socks"].string:
        "characters/Rogue/images/standing/socks_[Rogue.Clothes[socks].string].webp"

    if Rogue.Clothes["underwear"].string:
        "characters/Rogue/images/standing/underwear_[Rogue.Clothes[underwear].string]_[Rogue.Clothes[underwear].state].webp"

    if Rogue.Clothes["hose"].string:
        "characters/Rogue/images/standing/hose_[Rogue.Clothes[hose].string]_[Rogue.Clothes[hose].state].webp"

    if Rogue.Clothes["bra"].string and Rogue.Clothes["bodysuit"].string != "Rogue_suit":
        "characters/Rogue/images/standing/bra_[Rogue.Clothes[bra].string]_[Rogue.Clothes[bra].state].webp"

    if Rogue.Clothes["bodysuit"].string:
        "characters/Rogue/images/standing/bodysuit_[Rogue.Clothes[bodysuit].string]_[Rogue.Clothes[bodysuit].state].webp"

    if Rogue.piercings["labia"] not in ["barbell", "both"]:
        Null()
    elif Rogue.Clothes["bodysuit"].string:
        "characters/Rogue/images/standing/labia_piercings_barbell_covered_[Rogue.Clothes[bodysuit].string].webp"
    elif Rogue.Clothes["underwear"].string and Rogue.Clothes["underwear"].state == 0:
        "characters/Rogue/images/standing/labia_piercings_barbell_covered_[Rogue.Clothes[underwear].string].webp"

    if Rogue.piercings["labia"] not in ["ring", "both"]:
        Null()
    elif Rogue.Clothes["bodysuit"].string:
        "characters/Rogue/images/standing/labia_piercings_ring_covered_[Rogue.Clothes[bodysuit].string].webp"
    elif Rogue.Clothes["underwear"].string and Rogue.Clothes["underwear"].state == 0:
        "characters/Rogue/images/standing/labia_piercings_ring_covered_[Rogue.Clothes[underwear].string].webp"

    if Rogue.piercings["belly"] and Rogue.Clothes["bodysuit"].string:
        "characters/Rogue/images/standing/belly_piercing_covered_[Rogue.Clothes[bodysuit].string].webp"

    if not Rogue.grool:
        Null()
    elif Rogue.Clothes["bodysuit"].string:
        "characters/Rogue/images/standing/grool_[Rogue.Clothes[bodysuit].string].webp"
    elif Rogue.Clothes["underwear"].string:
        "characters/Rogue/images/standing/grool_[Rogue.Clothes[underwear].string]_[Rogue.Clothes[underwear].state].webp"

    if Rogue.Clothes["pants"].string:
        "characters/Rogue/images/standing/pants_[Rogue.Clothes[pants].string]_[Rogue.Clothes[pants].state].webp"

    if Rogue.Clothes["boots"].string:
        "characters/Rogue/images/standing/boots_[Rogue.Clothes[boots].string].webp"

    if Rogue.Clothes["skirt"].string:
        "characters/Rogue/images/standing/skirt_[Rogue.Clothes[skirt].string]_[Rogue.Clothes[skirt].state].webp"

    if not Rogue.Clothes["dress"].string:
        Null()
    elif Rogue.breasts_supported and Rogue.Clothes["dress"].string in ["green_dress", "green_nighty"] and Rogue.Clothes["dress"].state == 0:
        "characters/Rogue/images/standing/dress_[Rogue.Clothes[dress].string]_0_supported.webp"
    elif Rogue.breasts_supported and Rogue.Clothes["dress"].string == "sweater_dress":
        "characters/Rogue/images/standing/dress_[Rogue.Clothes[dress].string]_[Rogue.Clothes[dress].state]_supported.webp"
    else:
        "characters/Rogue/images/standing/dress_[Rogue.Clothes[dress].string]_[Rogue.Clothes[dress].state].webp"

    if Rogue.Clothes["belt"].string:
        "characters/Rogue/images/standing/belt_[Rogue.Clothes[belt].string].webp"

    if not Rogue.Clothes["top"].string or Rogue.Clothes["top"].string in ["black_fishnet_top", "green_mesh_top"]:
        Null()
    elif Rogue.breasts_supported and Rogue.Clothes["top"].state == 0:
        "characters/Rogue/images/standing/top_[Rogue.Clothes[top].string]_0_supported.webp"
    else:
        "characters/Rogue/images/standing/top_[Rogue.Clothes[top].string]_[Rogue.Clothes[top].state].webp"

    if Rogue.piercings["nipple"] not in ["barbell", "both"]:
        Null()
    elif Rogue.breasts_supported and Rogue.Clothes["top"].string and Rogue.Clothes["top"].string not in ["black_fishnet_top", "green_mesh_top"] and Rogue.Clothes["top"].state == 0:
        "characters/Rogue/images/standing/nipple_piercings_barbell_covered_[Rogue.Clothes[top].string]_supported.webp"
    elif Rogue.breasts_supported and Rogue.Clothes["dress"].string in ["green_dress", "green_nighty"] and Rogue.Clothes["dress"].state == 0:
        "characters/Rogue/images/standing/nipple_piercings_barbell_covered_[Rogue.Clothes[dress].string]_supported.webp"
    elif Rogue.breasts_supported and Rogue.Clothes["dress"].string in ["sweater_dress"] and Rogue.Clothes["dress"].state in [0, 2]:
        Null()
    elif Rogue.Clothes["top"].string and Rogue.Clothes["top"].string not in ["black_fishnet_top", "green_mesh_top"] and Rogue.Clothes["top"].state == 0:
        "characters/Rogue/images/standing/nipple_piercings_barbell_covered_[Rogue.Clothes[top].string].webp"
    elif Rogue.Clothes["dress"].string in ["green_dress", "green_nighty"] and Rogue.Clothes["dress"].state == 0:
        "characters/Rogue/images/standing/nipple_piercings_barbell_covered_[Rogue.Clothes[dress].string].webp"
    elif Rogue.Clothes["dress"].string in ["sweater_dress"] and Rogue.Clothes["dress"].state in [0, 2]:
        Null()
    elif Rogue.Clothes["bodysuit"].string and Rogue.Clothes["bodysuit"].state == 0:
        "characters/Rogue/images/standing/nipple_piercings_barbell_covered_[Rogue.Clothes[bodysuit].string].webp"
    elif Rogue.Clothes["bra"].string and Rogue.Clothes["bra"].state == 0:
        "characters/Rogue/images/standing/nipple_piercings_barbell_covered_[Rogue.Clothes[bra].string].webp"
    elif Rogue.Clothes["nipple_accessories"].string:
        "characters/Rogue/images/standing/nipple_piercings_barbell_covered_[Rogue.Clothes[nipple_accessories].string].webp"

    if Rogue.piercings["nipple"] not in ["ring", "both"]:
        Null()
    elif Rogue.breasts_supported and Rogue.Clothes["top"].string and Rogue.Clothes["top"].string not in ["black_fishnet_top", "green_mesh_top"] and Rogue.Clothes["top"].state == 0:
        "characters/Rogue/images/standing/nipple_piercings_ring_covered_[Rogue.Clothes[top].string]_supported.webp"
    elif Rogue.breasts_supported and Rogue.Clothes["dress"].string in ["green_dress", "green_nighty"] and Rogue.Clothes["dress"].state == 0:
        "characters/Rogue/images/standing/nipple_piercings_ring_covered_[Rogue.Clothes[dress].string]_supported.webp"
    elif Rogue.breasts_supported and Rogue.Clothes["dress"].string in ["sweater_dress"] and Rogue.Clothes["dress"].state in [0, 2]:
        Null()
    elif Rogue.Clothes["top"].string and Rogue.Clothes["top"].string not in ["black_fishnet_top", "green_mesh_top"] and Rogue.Clothes["top"].state == 0:
        "characters/Rogue/images/standing/nipple_piercings_ring_covered_[Rogue.Clothes[top].string].webp"
    elif Rogue.Clothes["dress"].string in ["green_dress", "green_nighty"] and Rogue.Clothes["dress"].state == 0:
        "characters/Rogue/images/standing/nipple_piercings_ring_covered_[Rogue.Clothes[dress].string].webp"
    elif Rogue.Clothes["dress"].string in ["sweater_dress"] and Rogue.Clothes["dress"].state in [0, 2]:
        Null()
    elif Rogue.Clothes["bodysuit"].string and Rogue.Clothes["bodysuit"].state == 0:
        "characters/Rogue/images/standing/nipple_piercings_ring_covered_[Rogue.Clothes[bodysuit].string].webp"
    elif Rogue.Clothes["bra"].string and Rogue.Clothes["bra"].state == 0:
        "characters/Rogue/images/standing/nipple_piercings_ring_covered_[Rogue.Clothes[bra].string].webp"
    elif Rogue.Clothes["nipple_accessories"].string:
        "characters/Rogue/images/standing/nipple_piercings_ring_covered_[Rogue.Clothes[nipple_accessories].string].webp"

    if not Rogue.Clothes["top"].string or Rogue.Clothes["top"].string not in ["black_fishnet_top", "green_mesh_top"]:
        Null()
    elif Rogue.breasts_supported and Rogue.Clothes["top"].state == 0:
        "characters/Rogue/images/standing/top_[Rogue.Clothes[top].string]_0_supported.webp"
    else:
        "characters/Rogue/images/standing/top_[Rogue.Clothes[top].string]_[Rogue.Clothes[top].state].webp"

    if not Rogue.Clothes["jacket"].string:
        Null()
    elif Rogue.breasts_supported and Rogue.Clothes["jacket"].string in ["brown_jacket", "leather_jacket", "NIN_shirt"]:
        "characters/Rogue/images/standing/jacket_[Rogue.Clothes[jacket].string]_[Rogue.Clothes[jacket].state]_supported.webp"
    else:
        "characters/Rogue/images/standing/jacket_[Rogue.Clothes[jacket].string]_[Rogue.Clothes[jacket].state].webp"

    if Rogue.Clothes["towel"].string:
        "characters/Rogue/images/standing/towel_[Rogue.Clothes[towel].string]_[Rogue.Clothes[towel].state].webp"

    if Rogue.spunk["belly"]:
        "characters/Rogue/images/standing/spunk_belly.webp"

    if Rogue.spunk["breasts"]:
        "characters/Rogue/images/standing/spunk_breasts.webp"

    anchor (int(914*character_sampling), int(1566*character_sampling))
    offset (int(914*character_sampling), int(1566*character_sampling))

layeredimage Rogue_standing_left_arm1:
    always:
        "characters/Rogue/images/standing/left_arm1.webp"

    if Rogue.Clothes["gloves"].string == "black_gloves":
        "characters/Rogue/images/standing/gloves_black_gloves_left1.webp"

    if Rogue.Clothes["bodysuit"].string and Rogue.Clothes["jacket"].string != "plaid_coat":
        "characters/Rogue/images/standing/bodysuit_[Rogue.Clothes[bodysuit].string]_left_sleeve1.webp"
            
    if Rogue.Clothes["dress"].string == "sweater_dress" and Rogue.Clothes["jacket"].string != "plaid_coat":
        "characters/Rogue/images/standing/dress_sweater_dress_left_sleeve1.webp"
            
    if Rogue.Clothes["top"].string and Rogue.Clothes["top"].string not in ["black_top", "green_mesh_top"]:
        "characters/Rogue/images/standing/top_[Rogue.Clothes[top].string]_left_sleeve1.webp"
            
    if Rogue.Clothes["sleeves"].string:
        "characters/Rogue/images/standing/sleeves_[Rogue.Clothes[sleeves].string]_left1.webp"

    if Rogue.Clothes["top"].string in ["black_top", "green_mesh_top"]:
        "characters/Rogue/images/standing/top_[Rogue.Clothes[top].string]_left_sleeve1.webp"

    if not Rogue.Clothes["jacket"].string:
        Null()
    elif Rogue.Clothes["jacket"].string in ["brown_jacket", "NIN_shirt"]:
        "characters/Rogue/images/standing/jacket_[Rogue.Clothes[jacket].string]_left_sleeve1_[Rogue.Clothes[jacket].state].webp"
    else:
        "characters/Rogue/images/standing/jacket_[Rogue.Clothes[jacket].string]_left_sleeve1.webp"

    if Rogue.Clothes["gloves"].string == "yellow_gloves":
        "characters/Rogue/images/standing/gloves_yellow_gloves_left1.webp"

    anchor (int(1425*character_sampling), int(782*character_sampling))
    offset (int(1425*character_sampling), int(782*character_sampling))

layeredimage Rogue_standing_head:
    always:
        "characters/Rogue/images/standing/head.webp"

    always:
        "characters/Rogue/images/standing/mouth_[Rogue.mouth].webp"

    if Rogue.eyes in ["closed", "down", "left", "right", "squint", "up"]:
        "characters/Rogue/images/standing/eyes_[Rogue.eyes].webp"
    else:
        "Rogue_standing_blinking"

    always:
        "characters/Rogue/images/standing/brows_[Rogue.brows].webp"

    if Rogue.blush:
        "characters/Rogue/images/standing/blush[Rogue.blush].webp"

    if Rogue.Clothes["makeup"].string:
        "characters/Rogue/images/standing/makeup_[Rogue.Clothes[makeup].string].webp"

    if Rogue.Clothes["face_inner_accessory"].string:
        "characters/Rogue/images/standing/face_inner_accessory_[Rogue.Clothes[face_inner_accessory].string].webp"

    if Rogue.wet or Rogue.Clothes["hair"].string == "wet":
        "characters/Rogue/images/standing/hair_wet.webp"
    else:
        "characters/Rogue/images/standing/hair_[Rogue.Clothes[hair].string].webp"

    if Rogue.spunk["tongue"] and Rogue.mouth in ["agape", "tongue"]:
        "characters/Rogue/images/standing/spunk_tongue.webp"

    if Rogue.spunk["mouth"] and Rogue.mouth in ["agape", "tongue"]:
        "characters/Rogue/images/standing/spunk_mouth.webp"

    if not Rogue.spunk["chin"]:
        Null()
    elif Rogue.mouth in ["agape", "tongue"]:
        "characters/Rogue/images/standing/spunk_chin_open.webp"
    else:
        "characters/Rogue/images/standing/spunk_chin.webp"

    if Rogue.spunk["face"]:
        "characters/Rogue/images/standing/spunk_face.webp"

    if Rogue.spunk["hair"]:
        "characters/Rogue/images/standing/spunk_hair.webp"

    anchor (int(1088*character_sampling), int(512*character_sampling))
    offset (int(1088*character_sampling), int(512*character_sampling))

layeredimage Rogue_standing_left_arm2:
    always:
        "characters/Rogue/images/standing/left_arm2.webp"

    if Rogue.Clothes["gloves"].string == "black_gloves":
        "characters/Rogue/images/standing/gloves_black_gloves_left2.webp"

    if Rogue.Clothes["bodysuit"].string:
        "characters/Rogue/images/standing/bodysuit_[Rogue.Clothes[bodysuit].string]_left2.webp"

    if Rogue.Clothes["dress"].string == "sweater_dress":
        "characters/Rogue/images/standing/dress_sweater_dress_left_sleeve2.webp"

    if Rogue.Clothes["top"].string and Rogue.Clothes["top"].string not in ["black_top", "green_mesh_top"]:
        "characters/Rogue/images/standing/top_[Rogue.Clothes[top].string]_left_sleeve2.webp"

    if Rogue.Clothes["sleeves"].string:
        "characters/Rogue/images/standing/sleeves_[Rogue.Clothes[sleeves].string]_left2.webp"

    if Rogue.Clothes["top"].string in ["black_top", "green_mesh_top"]:
        "characters/Rogue/images/standing/top_[Rogue.Clothes[top].string]_left_sleeve2.webp"

    if not Rogue.Clothes["jacket"].string:
        Null()
    elif Rogue.Clothes["jacket"].string in ["brown_jacket", "NIN_shirt"]:
        "characters/Rogue/images/standing/jacket_[Rogue.Clothes[jacket].string]_left_sleeve2_[Rogue.Clothes[jacket].state].webp"
    else:
        "characters/Rogue/images/standing/jacket_[Rogue.Clothes[jacket].string]_left_sleeve2.webp"

    if Rogue.Clothes["gloves"].string == "yellow_gloves":
        "characters/Rogue/images/standing/gloves_yellow_gloves_left2.webp"

    anchor (int(1390*character_sampling), int(758*character_sampling))
    offset (int(1390*character_sampling), int(758*character_sampling))

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
    if Player.body_visible:
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