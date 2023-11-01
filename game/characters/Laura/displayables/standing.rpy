transform Laura_standing_head_animation:
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

transform Laura_standing_right_arm_animation:
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

transform Laura_standing_left_arm_animation:
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
                ease 2.0 rotate 0
            choice:
                ease 2.0 rotate 2

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

transform Laura_standing_left_claws1_unsheathe_animation:
    subpixel True
    transform_anchor True

    zoom 0.0
    ease 0.1 zoom 1.0

transform Laura_standing_left_claws1_sheathe_animation:
    subpixel True
    transform_anchor True

    zoom 1.0
    ease 0.2 zoom 0.0

transform Laura_standing_left_claws2_unsheathe_animation:
    subpixel True
    transform_anchor True

    zoom 0.0
    ease 0.1 zoom 1.0

transform Laura_standing_left_claws2_sheathe_animation:
    subpixel True
    transform_anchor True

    zoom 1.0
    ease 0.2 zoom 0.0
    
image Laura_sprite standing:
    contains:
        "Laura_standing_temp"

    xysize (int(1700*character_sampling), int(3650*character_sampling))

layeredimage Laura_standing_temp:
    if Laura.hovered:
        At("Laura_standing", hover)
    else:
        "Laura_standing"

layeredimage Laura_standing:
    if not Player.left_hand_Actions or Laura not in Player.left_hand_Actions[0].Targets:
        Null()
    elif Player.left_hand_Actions[0].animation_type == "grab_ass":
        At("Laura_standing_male_left_arm_grab_ass_animation[Player.left_hand_Actions[0].mode]", change_offset(Laura_standing_ass_position[0], Laura_standing_ass_position[1]))

    if not Player.right_hand_Actions or Laura not in Player.right_hand_Actions[0].Targets:
        Null()
    elif Player.right_hand_Actions[0].animation_type == "grab_ass":
        At("Laura_standing_male_right_arm_grab_ass_animation[Player.right_hand_Actions[0].mode]", change_offset(Laura_standing_ass_position[0], Laura_standing_ass_position[1]))

    if renpy.get_screen("Wardrobe_screen"):
        "Laura_standing_hair_back"
    else:
        At("Laura_standing_hair_back", Laura_standing_head_animation)

    if renpy.get_screen("Wardrobe_screen"):
        "Laura_standing_right_arm"
    else:
        At("Laura_standing_right_arm", Laura_standing_right_arm_animation)

    always:
        "Laura_standing_body"

    if Laura.left_arm_pose == 2:
        Null()
    elif renpy.get_screen("Wardrobe_screen"):
        "Laura_standing_left_arm1"
    else:
        At("Laura_standing_left_arm1", Laura_standing_left_arm_animation)

    if Laura.Clothes["jacket"].string == "winter_coat":
        "characters/Laura/images/standing/jacket_winter_coat_fur2_[Laura.Clothes[jacket].state].webp"

    if not Player.left_hand_Actions or Laura not in Player.left_hand_Actions[0].Targets:
        Null()
    elif Player.left_hand_Actions[0].animation_type == "choke":
        At("Laura_standing_male_left_arm_choke_animation[Player.left_hand_Actions[0].mode]", change_offset(Laura_standing_neck_position[0], Laura_standing_neck_position[1]))

    if not Player.right_hand_Actions or Laura not in Player.right_hand_Actions[0].Targets:
        Null()
    elif Player.right_hand_Actions[0].animation_type == "choke":
        At("Laura_standing_male_right_arm_choke_animation[Player.right_hand_Actions[0].mode]", change_offset(Laura_standing_neck_position[0], Laura_standing_neck_position[1]))

    if renpy.get_screen("Wardrobe_screen"):
        "Laura_standing_head"
    else:
        At("Laura_standing_head", Laura_standing_head_animation)

    if Laura.left_arm_pose == 1:
        Null()
    elif renpy.get_screen("Wardrobe_screen"):
        "Laura_standing_left_arm2"
    else:
        At("Laura_standing_left_arm2", Laura_standing_left_arm_animation)

    if Laura.Clothes["jacket"].string == "winter_coat":
        "characters/Laura/images/standing/jacket[Laura.left_arm_pose]_winter_coat_fur1.webp"

    if not Player.left_hand_Actions or Laura not in Player.left_hand_Actions[0].Targets:
        Null()
    elif Player.left_hand_Actions[0].animation_type == "touch_breasts" and Laura.right_breast_Actions and Player.left_hand_Actions[0].animation_type == Laura.right_breast_Actions[0].animation_type:
        At("Laura_standing_male_left_arm_touch_right_breast_animation[Player.left_hand_Actions[0].mode]", change_offset(Laura_standing_right_breast_position[0], Laura_standing_right_breast_position[1]))
    elif Player.left_hand_Actions[0].animation_type == "touch_breasts" and Laura.left_breast_Actions and Player.left_hand_Actions[0].animation_type == Laura.left_breast_Actions[0].animation_type:
        At("Laura_standing_male_left_arm_touch_left_breast_animation[Player.left_hand_Actions[0].mode]", change_offset(Laura_standing_left_breast_position[0], Laura_standing_left_breast_position[1]))
    elif Player.left_hand_Actions[0].animation_type == "pinch_nipples" and Laura.right_nipple_Actions and Player.left_hand_Actions[0].animation_type == Laura.right_nipple_Actions[0].animation_type:
        At("Laura_standing_male_left_arm_touch_right_breast_animation[Player.left_hand_Actions[0].mode]", change_offset(Laura_standing_right_nipple_position[0], Laura_standing_right_nipple_position[1]))
    elif Player.left_hand_Actions[0].animation_type == "pinch_nipples" and Laura.left_nipple_Actions and Player.left_hand_Actions[0].animation_type == Laura.left_nipple_Actions[0].animation_type:
        At("Laura_standing_male_left_arm_touch_left_breast_animation[Player.left_hand_Actions[0].mode]", change_offset(Laura_standing_left_nipple_position[0], Laura_standing_left_nipple_position[1]))
    elif Player.left_hand_Actions[0].animation_type == "touch_thighs":
        At("Laura_standing_male_left_arm_touch_thighs_animation[Player.left_hand_Actions[0].mode]", change_offset(Laura_standing_thigh_position[0], Laura_standing_thigh_position[1]))
    elif Player.left_hand_Actions[0].animation_type == "touch_thighs_higher":
        At("Laura_standing_male_left_arm_touch_thighs_higher_animation[Player.left_hand_Actions[0].mode]", change_offset(Laura_standing_thigh_higher_position[0], Laura_standing_thigh_higher_position[1]))
    elif Player.left_hand_Actions[0].animation_type == "touch_pussy":
        At("Laura_standing_male_left_arm_touch_pussy_animation[Player.left_hand_Actions[0].mode]", change_offset(Laura_standing_pussy_position[0], Laura_standing_pussy_position[1]))

    if not Player.right_hand_Actions or Laura not in Player.right_hand_Actions[0].Targets:
        Null()
    elif Player.right_hand_Actions[0].animation_type == "touch_breasts" and Laura.right_breast_Actions and Player.right_hand_Actions[0].animation_type == Laura.right_breast_Actions[0].animation_type:
        At("Laura_standing_male_right_arm_touch_right_breast_animation[Player.right_hand_Actions[0].mode]", change_offset(Laura_standing_right_breast_position[0], Laura_standing_right_breast_position[1]))
    elif Player.right_hand_Actions[0].animation_type == "touch_breasts" and Laura.left_breast_Actions and Player.right_hand_Actions[0].animation_type == Laura.left_breast_Actions[0].animation_type:
        At("Laura_standing_male_right_arm_touch_left_breast_animation[Player.right_hand_Actions[0].mode]", change_offset(Laura_standing_left_breast_position[0], Laura_standing_left_breast_position[1]))
    elif Player.right_hand_Actions[0].animation_type == "pinch_nipples" and Laura.right_nipple_Actions and Player.right_hand_Actions[0].animation_type == Laura.right_nipple_Actions[0].animation_type:
        At("Laura_standing_male_right_arm_touch_right_breast_animation[Player.right_hand_Actions[0].mode]", change_offset(Laura_standing_right_nipple_position[0], Laura_standing_right_nipple_position[1]))
    elif Player.right_hand_Actions[0].animation_type == "pinch_nipples" and Laura.left_nipple_Actions and Player.right_hand_Actions[0].animation_type == Laura.left_nipple_Actions[0].animation_type:
        At("Laura_standing_male_right_arm_touch_left_breast_animation[Player.right_hand_Actions[0].mode]", change_offset(Laura_standing_left_nipple_position[0], Laura_standing_left_nipple_position[1]))
    elif Player.right_hand_Actions[0].animation_type == "touch_thighs":
        At("Laura_standing_male_right_arm_touch_thighs_animation[Player.right_hand_Actions[0].mode]", change_offset(Laura_standing_thigh_position[0], Laura_standing_thigh_position[1]))
    elif Player.right_hand_Actions[0].animation_type == "touch_thighs_higher":
        At("Laura_standing_male_right_arm_touch_thighs_higher_animation[Player.right_hand_Actions[0].mode]", change_offset(Laura_standing_thigh_higher_position[0], Laura_standing_thigh_higher_position[1]))
    elif Player.right_hand_Actions[0].animation_type == "touch_pussy":
        At("Laura_standing_male_right_arm_touch_pussy_animation[Player.right_hand_Actions[0].mode]", change_offset(Laura_standing_pussy_position[0], Laura_standing_pussy_position[1]))

    if not Player.mouth_Actions or Laura not in Player.mouth_Actions[0].Targets:
        Null()
    elif Player.mouth_Actions[0].animation_type in ["suck_nipples"] and Laura.left_nipple_Actions and Player.mouth_Actions[0].animation_type == Laura.left_nipple_Actions[0].animation_type:
        At("Laura_standing_male_head_suck_left_nipple_animation[Player.mouth_Actions[0].mode]", change_offset(Laura_standing_left_nipple_position[0], Laura_standing_left_nipple_position[1]))
    elif Player.mouth_Actions[0].animation_type in ["suck_nipples"] and Laura.right_nipple_Actions and Player.mouth_Actions[0].animation_type == Laura.right_nipple_Actions[0].animation_type:
        At("Laura_standing_male_head_suck_right_nipple_animation[Player.mouth_Actions[0].mode]", change_offset(Laura_standing_right_nipple_position[0], Laura_standing_right_nipple_position[1]))

layeredimage Laura_standing_hair_back:
    if Laura.Clothes["face_outer_accessory"].string:
        "characters/Laura/images/standing/hair_back_mask.webp"
    else:
        "characters/Laura/images/standing/hair_back.webp"

    anchor (int(763*character_sampling), int(693*character_sampling))
    offset (int(763*character_sampling), int(693*character_sampling))

layeredimage Laura_standing_right_arm:
    if Laura.claws and Laura.unsheathing_claws:
        At("Laura_standing_right_claws", Laura_standing_right_claws_unsheathe_animation)
    elif Laura.claws:
        "Laura_standing_right_claws"
    elif Laura.sheathing_claws:
        At("Laura_standing_right_claws", Laura_standing_right_claws_sheathe_animation)

    always:
        "characters/Laura/images/standing/right_arm.webp"

    if Laura.Clothes["gloves"].string == "black_long_gloves":
        "characters/Laura/images/standing/gloves_black_long_gloves_right.webp"

    if Laura.Clothes["bodysuit"].string in ["blackyellow_Wolverine_suit", "blueyellow_Wolverine_suit", "leather_teddy"]:
        "characters/Laura/images/standing/bodysuit_[Laura.Clothes[bodysuit].string]_right_sleeve.webp"

    if Laura.Clothes["top"].string in ["striped_shirt", "white_sweater"] and not Laura.Clothes["jacket"].string:
        "characters/Laura/images/standing/top_[Laura.Clothes[top].string]_right_sleeve.webp"

    if Laura.Clothes["gloves"].string in ["blackyellow_Wolverine_gloves", "blueyellow_Wolverine_gloves"]:
        "characters/Laura/images/standing/gloves_[Laura.Clothes[gloves].string]_right.webp"

    if Laura.Clothes["jacket"].string:
        "characters/Laura/images/standing/jacket_[Laura.Clothes[jacket].string]_right_sleeve.webp"

    if not Laura.Clothes["jacket"].string:
        Null()
    elif Laura.Clothes["jacket"].string == "leather_jacket" and Laura.Clothes["jacket"].state == 0:
        Null()
    else:
        "characters/Laura/images/standing/jacket_[Laura.Clothes[jacket].string]_mid.webp"

    anchor (int(494*character_sampling), int(1014*character_sampling))
    offset (int(494*character_sampling), int(1014*character_sampling))

image Laura_standing_right_claws:
    "characters/Laura/images/standing/right_claws.webp"

    anchor (int(192*character_sampling), int(2225*character_sampling))
    offset (int(192*character_sampling), int(2225*character_sampling))

layeredimage Laura_standing_body:
    always:
        "characters/Laura/images/standing/body.webp"

    always:
        "characters/Laura/images/standing/breasts.webp"

    if Laura.tan_lines["full"]:
        "characters/Laura/images/standing/tan_lines_[Laura.tan_lines[full]].webp"

    if Laura.tan_lines["bottom"]:
        "characters/Laura/images/standing/tan_lines_[Laura.tan_lines[bottom]].webp"

    if Laura.tan_lines["top"]:
        "characters/Laura/images/standing/tan_lines_[Laura.tan_lines[top]].webp"

    if Laura.piercings["labia"] in ["barbell", "both"]:
        "characters/Laura/images/standing/labia_piercings_barbell.webp"

    if Laura.piercings["labia"] in ["ring", "both"]:
        "characters/Laura/images/standing/labia_piercings_ring.webp"

    if Laura.piercings["belly"]:
        "characters/Laura/images/standing/belly_piercing.webp"

    if Laura.piercings["nipple"] in ["barbell", "both"]:
        "characters/Laura/images/standing/nipple_piercings_barbell.webp"

    if Laura.piercings["nipple"] in ["ring", "both"]:
        "characters/Laura/images/standing/nipple_piercings_ring.webp"

    if Laura.Clothes["nipple_accessories"].string:
        "characters/Laura/images/standing/nipple_accessories_[Laura.Clothes[nipple_accessories].string].webp"

    if Laura.pubes_growing:
        "characters/Laura/images/standing/pubes_growing.webp"

    if Laura.pubes:
        "characters/Laura/images/standing/pubes_[Laura.pubes].webp"

    if Laura.remote_vibrator:
        "characters/Laura/images/standing/remote_vibrator.webp"

    if Laura.creampie["pussy"]:
        "characters/Laura/images/standing/creampie.webp"

    if Laura.Clothes["socks"].string:
        "characters/Laura/images/standing/socks_[Laura.Clothes[socks].string].webp"

    if Laura.Clothes["underwear"].string:
        "characters/Laura/images/standing/underwear_[Laura.Clothes[underwear].string]_[Laura.Clothes[underwear].state].webp"

    if Laura.Clothes["hose"].string:
        "characters/Laura/images/standing/hose_[Laura.Clothes[hose].string].webp"

    if Laura.Clothes["bra"].string and (Laura.Clothes["bodysuit"].string not in ["blackyellow_Wolverine_suit", "blueyellow_Wolverine_suit"] or Laura.Clothes["bodysuit"].state == 1):
        "characters/Laura/images/standing/bra_[Laura.Clothes[bra].string]_[Laura.Clothes[bra].state].webp"

    if Laura.Clothes["bodysuit"].string:
        "characters/Laura/images/standing/bodysuit_[Laura.Clothes[bodysuit].string]_[Laura.Clothes[bodysuit].state].webp"

    if Laura.piercings["labia"] not in ["barbell", "both"]:
        Null()
    elif Laura.Clothes["bodysuit"].string and Laura.Clothes["bodysuit"].string != "leather_teddy":
        "characters/Laura/images/standing/labia_piercings_barbell_covered_[Laura.Clothes[bodysuit].string].webp"
    elif Laura.Clothes["bodysuit"].string == "leather_teddy":
        Null()
    elif Laura.Clothes["underwear"].string and Laura.Clothes["underwear"].state == 0:
        "characters/Laura/images/standing/labia_piercings_barbell_covered_[Laura.Clothes[underwear].string].webp"

    if Laura.piercings["labia"] not in ["ring", "both"]:
        Null()
    elif Laura.Clothes["bodysuit"].string and Laura.Clothes["bodysuit"].string != "leather_teddy":
        "characters/Laura/images/standing/labia_piercings_ring_covered_[Laura.Clothes[bodysuit].string].webp"
    elif Laura.Clothes["bodysuit"].string == "leather_teddy":
        Null()
    elif Laura.Clothes["underwear"].string and Laura.Clothes["underwear"].state == 0:
        "characters/Laura/images/standing/labia_piercings_ring_covered_[Laura.Clothes[underwear].string].webp"

    if not Laura.grool:
        Null()
    elif Laura.Clothes["bodysuit"].string in ["blackyellow_Wolverine_suit", "blueyellow_Wolverine_suit"]:
        "characters/Laura/images/standing/grool_[Laura.Clothes[bodysuit].string].webp"
    elif Laura.Clothes["underwear"].string in ["black_boyshorts", "grey_panties"]:
        "characters/Laura/images/standing/grool_[Laura.Clothes[underwear].string]_[Laura.Clothes[underwear].state].webp"

    if Laura.Clothes["pants"].string:
        "characters/Laura/images/standing/pants_[Laura.Clothes[pants].string]_[Laura.Clothes[pants].state].webp"

    if Laura.Clothes["boots"].string:
        "characters/Laura/images/standing/boots_[Laura.Clothes[boots].string].webp"

    if Laura.Clothes["skirt"].string:
        "characters/Laura/images/standing/skirt_[Laura.Clothes[skirt].string]_[Laura.Clothes[skirt].state].webp"

    if not Laura.Clothes["belt"].string:
        Null()
    elif Laura.Clothes["bodysuit"].string in ["blackyellow_Wolverine_suit", "blueyellow_Wolverine_suit"]:
        "characters/Laura/images/standing/belt_[Laura.Clothes[belt].string]_high.webp"
    else:
        "characters/Laura/images/standing/belt_[Laura.Clothes[belt].string]_low.webp"

    if Laura.Clothes["dress"].string:
        "characters/Laura/images/standing/dress_[Laura.Clothes[dress].string]_[Laura.Clothes[dress].state].webp"

    if Laura.Clothes["top"].string:
        "characters/Laura/images/standing/top_[Laura.Clothes[top].string]_[Laura.Clothes[top].state].webp"

    if Laura.piercings["nipple"] not in ["barbell", "both"]:
        Null()
    elif Laura.Clothes["top"].string == "yellow_tanktop" and Laura.Clothes["top"].state == 0:
        "characters/Laura/images/standing/nipple_piercings_barbell_covered_[Laura.Clothes[top].string].webp"
    elif Laura.Clothes["dress"].string and Laura.Clothes["dress"].state == 0:
        "characters/Laura/images/standing/nipple_piercings_barbell_covered_[Laura.Clothes[dress].string].webp"
    elif Laura.Clothes["bodysuit"].string and Laura.Clothes["bodysuit"].state == 0:
        "characters/Laura/images/standing/nipple_piercings_barbell_covered_[Laura.Clothes[bodysuit].string].webp"
    elif Laura.Clothes["bra"].string and Laura.Clothes["bra"].string not in ["blackred_corset"] and Laura.Clothes["bra"].state == 0:
        "characters/Laura/images/standing/nipple_piercings_barbell_covered_[Laura.Clothes[bra].string].webp"
    elif Laura.Clothes["nipple_accessories"].string:
        "characters/Laura/images/standing/nipple_piercings_barbell_covered_[Laura.Clothes[nipple_accessories].string].webp"
        
    if Laura.piercings["nipple"] not in ["ring", "both"]:
        Null()
    elif Laura.Clothes["top"].string == "yellow_tanktop" and Laura.Clothes["top"].state == 0:
        "characters/Laura/images/standing/nipple_piercings_ring_covered_[Laura.Clothes[top].string].webp"
    elif Laura.Clothes["dress"].string and Laura.Clothes["dress"].state == 0:
        "characters/Laura/images/standing/nipple_piercings_ring_covered_[Laura.Clothes[dress].string].webp"
    elif Laura.Clothes["bodysuit"].string and Laura.Clothes["bodysuit"].state == 0:
        "characters/Laura/images/standing/nipple_piercings_ring_covered_[Laura.Clothes[bodysuit].string].webp"
    elif Laura.Clothes["bra"].string and Laura.Clothes["bra"].string not in ["blackred_corset"] and Laura.Clothes["bra"].state == 0:
        "characters/Laura/images/standing/nipple_piercings_ring_covered_[Laura.Clothes[bra].string].webp"
    elif Laura.Clothes["nipple_accessories"].string:
        "characters/Laura/images/standing/nipple_piercings_ring_covered_[Laura.Clothes[nipple_accessories].string].webp"

    if Laura.Clothes["neck"].string and Laura.Clothes["neck"].string != "grey_scarf":
        "characters/Laura/images/standing/neck_[Laura.Clothes[neck].string].webp"

    if not Laura.Clothes["jacket"].string:
        Null()
    elif Laura.Clothes["jacket"].string in ["denim_jacket", "leather_jacket"] and Laura.Clothes["top"].string in ["striped_shirt", "white_sweater"]:
        "characters/Laura/images/standing/jacket_[Laura.Clothes[jacket].string]_[Laura.Clothes[jacket].state]_top.webp"
    else:
        "characters/Laura/images/standing/jacket_[Laura.Clothes[jacket].string]_[Laura.Clothes[jacket].state].webp"

    if Laura.Clothes["towel"].string:
        "characters/Laura/images/standing/towel_[Laura.Clothes[towel].string]_[Laura.Clothes[towel].state].webp"

    if Laura.Clothes["neck"].string == "grey_scarf":
        "characters/Laura/images/standing/neck_grey_scarf.webp"

    if Laura.spunk["belly"]:
        "characters/Laura/images/standing/spunk_belly.webp"

    if Laura.spunk["breasts"]:
        "characters/Laura/images/standing/spunk_breasts.webp"

    anchor (int(640*character_sampling), int(1806*character_sampling))
    offset (int(640*character_sampling), int(1806*character_sampling))

layeredimage Laura_standing_left_arm1:
    always:
        "characters/Laura/images/standing/left_arm1.webp"

    if Laura.Clothes["gloves"].string == "black_long_gloves":
        "characters/Laura/images/standing/gloves_black_long_gloves_left1.webp"

    if Laura.Clothes["bodysuit"].string in ["blackyellow_Wolverine_suit", "blueyellow_Wolverine_suit", "leather_teddy"]:
        "characters/Laura/images/standing/bodysuit_[Laura.Clothes[bodysuit].string]_left_sleeve1.webp"

    if Laura.Clothes["top"].string in ["striped_shirt", "white_sweater"] and not Laura.Clothes["jacket"].string:
        "characters/Laura/images/standing/top_[Laura.Clothes[top].string]_left_sleeve1.webp"

    if Laura.Clothes["gloves"].string in ["blackyellow_Wolverine_gloves", "blueyellow_Wolverine_gloves"]:
        "characters/Laura/images/standing/gloves_[Laura.Clothes[gloves].string]_left1.webp"

    if Laura.Clothes["jacket"].string:
        "characters/Laura/images/standing/jacket_[Laura.Clothes[jacket].string]_left_sleeve1.webp"

    if Laura.claws and Laura.unsheathing_claws:
        At("Laura_standing_left_claws1", Laura_standing_left_claws1_unsheathe_animation)
    elif Laura.claws:
        "Laura_standing_left_claws1"
    elif Laura.sheathing_claws:
        At("Laura_standing_left_claws1", Laura_standing_left_claws1_sheathe_animation)

    if Laura.spunk["hand"]:
        "characters/Laura/images/standing/spunk_left_hand1.webp"

    anchor (int(1121*character_sampling), int(949*character_sampling))
    offset (int(1121*character_sampling), int(949*character_sampling))

image Laura_standing_left_claws1:
    "characters/Laura/images/standing/left_claws1.webp"

    anchor (int(1419*character_sampling), int(2290*character_sampling))
    offset (int(1419*character_sampling), int(2290*character_sampling))

layeredimage Laura_standing_head:
    always:
        "characters/Laura/images/standing/head.webp"
    
    if Laura.Clothes["face_outer_accessory"].string:
        "characters/Laura/images/standing/hair_mask.webp"
    
    always:
        "characters/Laura/images/standing/mouth_[Laura.mouth].webp"
    
    if Laura.eyes in ["closed", "down", "left", "right", "squint", "up"]:
        "characters/Laura/images/standing/eyes_[Laura.eyes].webp"
    else:
        "Laura_standing_blinking"

    always:
        "characters/Laura/images/standing/brows_[Laura.brows].webp"
    
    if Laura.blush:
        "characters/Laura/images/standing/blush[Laura.blush].webp"

    if Laura.Clothes["makeup"].string:
        "characters/Laura/images/standing/makeup_[Laura.Clothes[makeup].string].webp"

    if Laura.Clothes["face_outer_accessory"].string:
        Null()
    elif Laura.wet:
        "characters/Laura/images/standing/hair_shadow_wet.webp"
    else:
        "characters/Laura/images/standing/hair_shadow_[Laura.Clothes[hair].string].webp"

    if Laura.Clothes["face_outer_accessory"].string:
        Null()
    elif Laura.wet:
        "characters/Laura/images/standing/hair_wet.webp"
    else:
        "characters/Laura/images/standing/hair_[Laura.Clothes[hair].string].webp"

    if not Laura.Clothes["face_outer_accessory"].string:
        Null()
    elif Laura.mouth in ["agape", "open", "tongue"]:
        "characters/Laura/images/standing/face_outer_accessory_[Laura.Clothes[face_outer_accessory].string]_open.webp"
    else:
        "characters/Laura/images/standing/face_outer_accessory_[Laura.Clothes[face_outer_accessory].string].webp"

    if Laura.spunk["tongue"] and Laura.mouth in ["agape", "tongue"]:
        "characters/Laura/images/standing/spunk_tongue.webp"

    if Laura.spunk["mouth"] and Laura.mouth in ["agape", "tongue"]:
        "characters/Laura/images/standing/spunk_mouth.webp"

    if not Laura.spunk["chin"]:
        Null()
    elif Laura.mouth in ["agape", "tongue"]:
        "characters/Laura/images/standing/spunk_chin_open.webp"
    else:
        "characters/Laura/images/standing/spunk_chin.webp"

    if Laura.spunk["face"]:
        "characters/Laura/images/standing/spunk_face.webp"

    if Laura.spunk["hair"]:
        "characters/Laura/images/standing/spunk_hair.webp"

    anchor (int(763*character_sampling), int(693*character_sampling))
    offset (int(763*character_sampling), int(693*character_sampling))

layeredimage Laura_standing_left_arm2:
    always:
        "characters/Laura/images/standing/left_arm2.webp"

    if Laura.Clothes["gloves"].string == "black_long_gloves":
        "characters/Laura/images/standing/gloves_black_long_gloves_left2.webp"

    if Laura.Clothes["bodysuit"].string in ["blackyellow_Wolverine_suit", "blueyellow_Wolverine_suit", "leather_teddy"]:
        "characters/Laura/images/standing/bodysuit_[Laura.Clothes[bodysuit].string]_left_sleeve2.webp"

    if Laura.Clothes["top"].string in ["striped_shirt", "white_sweater"] and not Laura.Clothes["jacket"].string:
        "characters/Laura/images/standing/top_[Laura.Clothes[top].string]_left_sleeve2.webp"

    if Laura.Clothes["gloves"].string in ["blackyellow_Wolverine_gloves", "blueyellow_Wolverine_gloves"]:
        "characters/Laura/images/standing/gloves_[Laura.Clothes[gloves].string]_left2.webp"

    if Laura.Clothes["jacket"].string:
        "characters/Laura/images/standing/jacket_[Laura.Clothes[jacket].string]_left_sleeve2.webp"

    if Laura.claws and Laura.unsheathing_claws:
        At("Laura_standing_left_claws2", Laura_standing_left_claws2_unsheathe_animation)
    elif Laura.claws:
        "Laura_standing_left_claws2"
    elif Laura.sheathing_claws:
        At("Laura_standing_left_claws2", Laura_standing_left_claws2_sheathe_animation)

    if Laura.spunk["hand"]:
        "characters/Laura/images/standing/spunk_left_hand2.webp"

    anchor (int(1090*character_sampling), int(920*character_sampling))
    offset (int(1090*character_sampling), int(920*character_sampling))

image Laura_standing_left_claws2:
    "characters/Laura/images/standing/left_claws2.webp"

    anchor (int(1047*character_sampling), int(860*character_sampling))
    offset (int(1047*character_sampling), int(860*character_sampling))

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
    if Player.body_visible:
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