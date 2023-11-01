transform Ororo_standing_head_animation:
    subpixel True
    transform_anchor True
    
    pos (0.0, 0.0)
    xzoom 1.0 yzoom 1.0
    rotate 0.0

    block:
        pause 2.0
        ease 2.0 rotate -3
        pause 5.0
        ease 2.0 rotate 0
        pause 10.0
        ease 2.0 rotate 3

        repeat

transform Ororo_standing_right_arm2_animation:
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

transform Ororo_standing_right_arm1_animation:
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

transform Ororo_standing_left_arm_animation:
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
    
image Ororo_sprite standing:
    contains:
        ConditionSwitch(
            "Ororo.hovered", At("Ororo_standing", hover),
            "True", "Ororo_standing")

    xysize (int(1800*character_sampling), int(3650*character_sampling))

layeredimage Ororo_standing:
    if renpy.get_screen("Wardrobe_screen"):
        "Ororo_standing_hair_back"
    else:
        At("Ororo_standing_hair_back", Ororo_standing_head_animation)

    if Ororo.Clothes["cloak"].string:
        "characters/Ororo/images/standing/cloak_[Ororo.Clothes[cloak].string]_back.webp"

    if Ororo.Clothes["towel"].string and Ororo.Clothes["towel"].state > 0:
        "characters/Ororo/images/standing/towel_[Ororo.Clothes[towel].string]_back.webp"

    if Ororo.Clothes["dress"].string:
        "characters/Ororo/images/standing/dress_[Ororo.Clothes[dress].string]_back.webp"

    if Ororo.Clothes["skirt"].string:
        "characters/Ororo/images/standing/skirt_[Ororo.Clothes[skirt].string]_back.webp"

    if Ororo.right_arm_pose == 1:
        Null()
    elif renpy.get_screen("Wardrobe_screen"):
        "Ororo_standing_right_arm2"
    else:
        At("Ororo_standing_right_arm2", Ororo_standing_right_arm2_animation)

    always:
        "Ororo_standing_body"

    if Ororo.right_arm_pose == 2:
        Null()
    elif renpy.get_screen("Wardrobe_screen"):
        "Ororo_standing_right_arm1"
    else:
        At("Ororo_standing_right_arm1", Ororo_standing_right_arm1_animation)

    if renpy.get_screen("Wardrobe_screen"):
        "Ororo_standing_left_arm"
    else:
        At("Ororo_standing_left_arm", Ororo_standing_left_arm_animation)

    if Ororo.Clothes["cloak"].string:
        "characters/Ororo/images/standing/cloak_[Ororo.Clothes[cloak].string].webp"

    if renpy.get_screen("Wardrobe_screen"):
        "Ororo_standing_head"
    else:
        At("Ororo_standing_head", Ororo_standing_head_animation)

layeredimage Ororo_standing_hair_back:
    if not Ororo.wet and "wet" not in Ororo.Clothes["hair"].string:
        "characters/Ororo/images/standing/hair_back_[Ororo.Clothes[hair].string].webp"
    elif "mohawk" in Ororo.Clothes["hair"].string:
        Null()
    else:
        "characters/Ororo/images/standing/hair_back_wet.webp"

    anchor (int(837*character_sampling), int(844*character_sampling))
    offset (int(837*character_sampling), int(844*character_sampling))

layeredimage Ororo_standing_right_arm2:
    always:
        "characters/Ororo/images/standing/right_arm[Ororo.right_arm_pose].webp"

    if Ororo.Clothes["gloves"].string:
        "characters/Ororo/images/standing/gloves_[Ororo.Clothes[gloves].string]_right2.webp"

    if Ororo.Clothes["bodysuit"].string == "Storm_suit":
        "characters/Ororo/images/standing/bodysuit_[Ororo.Clothes[bodysuit].string]_right_sleeve2.webp"

    if Ororo.Clothes["top"].string in ["beige_shirt", "black_shirt"]:
        "characters/Ororo/images/standing/top_[Ororo.Clothes[top].string]_right_sleeve2.webp"

    if Ororo.Clothes["sleeves"].string:
        "characters/Ororo/images/standing/sleeves_[Ororo.Clothes[sleeves].string]_right2.webp"

    if Ororo.Clothes["jacket"].string:
        "characters/Ororo/images/standing/jacket_[Ororo.Clothes[jacket].string]_right_sleeve2.webp"

    if Ororo.spunk["hand"]:
        "characters/Ororo/images/standing/spunk_right_hand2.webp"

    anchor (int(477*character_sampling), int(1140*character_sampling))
    offset (int(477*character_sampling), int(1140*character_sampling))

layeredimage Ororo_standing_body:
    if Ororo.Clothes["jacket"].string == "grey_peacoat":
        "characters/Ororo/images/standing/jacket_[Ororo.Clothes[jacket].string]_mid.webp"
    
    always:
        "characters/Ororo/images/standing/body.webp"

    always:
        "characters/Ororo/images/standing/breasts.webp"

    if Ororo.tan_lines["full"]:
        "characters/Ororo/images/standing/tan_lines_[Ororo.tan_lines[full]].webp"

    if Ororo.tan_lines["bottom"]:
        "characters/Ororo/images/standing/tan_lines_[Ororo.tan_lines[bottom]].webp"

    if Ororo.tan_lines["top"]:
        "characters/Ororo/images/standing/tan_lines_[Ororo.tan_lines[top]].webp"

    if Ororo.piercings["labia"] in ["barbell", "both"]:
        "characters/Ororo/images/standing/labia_piercings_barbell.webp"

    if Ororo.piercings["labia"] in ["ring", "both"]:
        "characters/Ororo/images/standing/labia_piercings_ring.webp"

    if Ororo.piercings["belly"]:
        "characters/Ororo/images/standing/belly_piercing.webp"

    if Ororo.piercings["nipple"] in ["barbell", "both"]:
        "characters/Ororo/images/standing/nipple_piercings_barbell.webp"

    if Ororo.piercings["nipple"] in ["ring", "both"]:
        "characters/Ororo/images/standing/nipple_piercings_ring.webp"

    if Ororo.Clothes["nipple_accessories"].string:
        "characters/Ororo/images/standing/nipple_accessories_[Ororo.Clothes[nipple_accessories].string].webp"

    if Ororo.pubes_growing:
        "characters/Ororo/images/standing/pubes_growing.webp"

    if Ororo.pubes:
        "characters/Ororo/images/standing/pubes_[Ororo.pubes].webp"

    if Ororo.remote_vibrator:
        "characters/Ororo/images/standing/remote_vibrator.webp"

    if Ororo.creampie["pussy"]:
        "characters/Ororo/images/standing/creampie.webp"

    if Ororo.Clothes["socks"].string:
        "characters/Ororo/images/standing/socks_[Ororo.Clothes[socks].string].webp"

    if Ororo.Clothes["underwear"].string:
        "characters/Ororo/images/standing/underwear_[Ororo.Clothes[underwear].string]_[Ororo.Clothes[underwear].state].webp"

    if Ororo.Clothes["hose"].string:
        "characters/Ororo/images/standing/hose_[Ororo.Clothes[hose].string].webp"

    if Ororo.piercings["labia"] not in ["barbell", "both"]:
        Null()
    elif Ororo.Clothes["underwear"].string and Ororo.Clothes["underwear"].state == 0:
        "characters/Ororo/images/standing/labia_piercings_barbell_covered_[Ororo.Clothes[underwear].string].webp"

    if Ororo.piercings["labia"] not in ["ring", "both"]:
        Null()
    elif Ororo.Clothes["underwear"].string and Ororo.Clothes["underwear"].state == 0:
        "characters/Ororo/images/standing/labia_piercings_ring_covered_[Ororo.Clothes[underwear].string].webp"

    if not Ororo.grool:
        Null()
    elif Ororo.Clothes["underwear"].string:
        "characters/Ororo/images/standing/grool_[Ororo.Clothes[underwear].string]_[Ororo.Clothes[underwear].state].webp"

    if Ororo.Clothes["bra"].string:
        "characters/Ororo/images/standing/bra_[Ororo.Clothes[bra].string]_[Ororo.Clothes[bra].state].webp"

    if Ororo.Clothes["bodysuit"].string:
        "characters/Ororo/images/standing/bodysuit_[Ororo.Clothes[bodysuit].string]_[Ororo.Clothes[bodysuit].state].webp"

    if Ororo.piercings["belly"] and Ororo.Clothes["bodysuit"].string:
        "characters/Ororo/images/standing/belly_piercing_covered_[Ororo.Clothes[bodysuit].string].webp"

    if Ororo.Clothes["pants"].string:
        "characters/Ororo/images/standing/pants_[Ororo.Clothes[pants].string]_[Ororo.Clothes[pants].state].webp"

    if Ororo.Clothes["skirt"].string:
        "characters/Ororo/images/standing/skirt_[Ororo.Clothes[skirt].string]_[Ororo.Clothes[skirt].state].webp"

    if Ororo.Clothes["dress"].string:
        "characters/Ororo/images/standing/dress_[Ororo.Clothes[dress].string]_[Ororo.Clothes[dress].state].webp"

    if Ororo.Clothes["top"].string:
        "characters/Ororo/images/standing/top_[Ororo.Clothes[top].string]_[Ororo.Clothes[top].state].webp"
        
    if Ororo.piercings["nipple"] not in ["barbell", "both"]:
        Null()
    elif Ororo.Clothes["top"].string and Ororo.Clothes["top"].state == 0:
        "characters/Ororo/images/standing/nipple_piercings_barbell_covered_[Ororo.Clothes[top].string].webp"
    elif Ororo.Clothes["dress"].string and Ororo.Clothes["dress"].state == 0:
        "characters/Ororo/images/standing/nipple_piercings_barbell_covered_[Ororo.Clothes[dress].string].webp"
    elif Ororo.Clothes["bodysuit"].string and Ororo.Clothes["bodysuit"].state == 0:
        "characters/Ororo/images/standing/nipple_piercings_barbell_covered_[Ororo.Clothes[bodysuit].string].webp"
    elif Ororo.Clothes["bra"].string and Ororo.Clothes["bra"].state == 0:
        "characters/Ororo/images/standing/nipple_piercings_barbell_covered_[Ororo.Clothes[bra].string].webp"
    elif Ororo.Clothes["nipple_accessories"].string:
        "characters/Ororo/images/standing/nipple_piercings_barbell_covered_[Ororo.Clothes[nipple_accessories].string].webp"
        
    if Ororo.piercings["nipple"] not in ["ring", "both"]:
        Null()
    elif Ororo.Clothes["top"].string and Ororo.Clothes["top"].state == 0:
        "characters/Ororo/images/standing/nipple_piercings_ring_covered_[Ororo.Clothes[top].string].webp"
    elif Ororo.Clothes["dress"].string and Ororo.Clothes["dress"].state == 0:
        "characters/Ororo/images/standing/nipple_piercings_ring_covered_[Ororo.Clothes[dress].string].webp"
    elif Ororo.Clothes["bodysuit"].string and Ororo.Clothes["bodysuit"].state == 0:
        "characters/Ororo/images/standing/nipple_piercings_ring_covered_[Ororo.Clothes[bodysuit].string].webp"
    elif Ororo.Clothes["bra"].string and Ororo.Clothes["bra"].state == 0:
        "characters/Ororo/images/standing/nipple_piercings_ring_covered_[Ororo.Clothes[bra].string].webp"
    elif Ororo.Clothes["nipple_accessories"].string:
        "characters/Ororo/images/standing/nipple_piercings_ring_covered_[Ororo.Clothes[nipple_accessories].string].webp"

    if Ororo.Clothes["jacket"].string:
        "characters/Ororo/images/standing/jacket_[Ororo.Clothes[jacket].string]_[Ororo.Clothes[jacket].state].webp"

    if Ororo.Clothes["towel"].string:
        "characters/Ororo/images/standing/towel_[Ororo.Clothes[towel].string]_[Ororo.Clothes[towel].state].webp"

    if Ororo.spunk["belly"]:
        "characters/Ororo/images/standing/spunk_belly.webp"

    if Ororo.spunk["breasts"]:
        "characters/Ororo/images/standing/spunk_breasts.webp"

    anchor (int(827*character_sampling), int(1831*character_sampling))
    offset (int(827*character_sampling), int(1831*character_sampling))

layeredimage Ororo_standing_right_arm1:
    always:
        "characters/Ororo/images/standing/right_arm[Ororo.right_arm_pose].webp"

    if Ororo.Clothes["gloves"].string:
        "characters/Ororo/images/standing/gloves_[Ororo.Clothes[gloves].string]_right1.webp"

    if Ororo.Clothes["bodysuit"].string == "Storm_suit":
        "characters/Ororo/images/standing/bodysuit_[Ororo.Clothes[bodysuit].string]_right_sleeve1.webp"

    if not Ororo.Clothes["top"].string:
        Null()
    elif Ororo.Clothes["top"].string == "black_shirt":
        "characters/Ororo/images/standing/top_[Ororo.Clothes[top].string]_right_sleeve1_[Ororo.Clothes[top].state].webp"
    elif Ororo.Clothes["top"].string == "beige_shirt":
        "characters/Ororo/images/standing/top_[Ororo.Clothes[top].string]_right_sleeve1.webp"
            
    if Ororo.Clothes["sleeves"].string:
        "characters/Ororo/images/standing/sleeves_[Ororo.Clothes[sleeves].string]_right1.webp"

    if Ororo.Clothes["jacket"].string == "grey_peacoat":
        "characters/Ororo/images/standing/jacket_[Ororo.Clothes[jacket].string]_right_sleeve1_[Ororo.Clothes[jacket].state].webp"

    if Ororo.spunk["hand"]:
        "characters/Ororo/images/standing/spunk_right_hand1.webp"

    anchor (int(477*character_sampling), int(1140*character_sampling))
    offset (int(477*character_sampling), int(1140*character_sampling))

layeredimage Ororo_standing_left_arm:
    always:
        "characters/Ororo/images/standing/left_arm.webp"

    if Ororo.Clothes["gloves"].string:
        "characters/Ororo/images/standing/gloves_[Ororo.Clothes[gloves].string]_left.webp"

    if Ororo.Clothes["bodysuit"].string == "Storm_suit":
        "characters/Ororo/images/standing/bodysuit_[Ororo.Clothes[bodysuit].string]_left_sleeve.webp"

    if Ororo.Clothes["top"].string == "beige_shirt":
        "characters/Ororo/images/standing/top_beige_shirt_left_sleeve.webp"

    if Ororo.Clothes["sleeves"].string:
        "characters/Ororo/images/standing/sleeves_[Ororo.Clothes[sleeves].string]_left.webp"

    if Ororo.Clothes["jacket"].string == "grey_peacoat":
        "characters/Ororo/images/standing/jacket_[Ororo.Clothes[jacket].string]_left_sleeve_[Ororo.Clothes[jacket].state].webp"

    anchor (int(1201*character_sampling), int(1111*character_sampling))
    offset (int(1201*character_sampling), int(1111*character_sampling))

layeredimage Ororo_standing_head:
    always:
        "characters/Ororo/images/standing/head.webp"

    always:
        "characters/Ororo/images/standing/mouth_[Ororo.mouth].webp"

    if Ororo.white or Ororo.electricity:
        "characters/Ororo/images/standing/eyes_white.webp"
    elif Ororo.eyes in ["closed", "down", "left", "right", "squint", "up"]:
        "characters/Ororo/images/standing/eyes_[Ororo.eyes].webp"
    else:
        "Ororo_standing_blinking"

    always:
        "characters/Ororo/images/standing/brows_[Ororo.brows].webp"

    if Ororo.blush:
        "characters/Ororo/images/standing/blush[Ororo.blush].webp"

    if Ororo.Clothes["makeup"].string:
        "characters/Ororo/images/standing/makeup_[Ororo.Clothes[makeup].string].webp"

    if not Ororo.wet and "wet" not in Ororo.Clothes["hair"].string:
        "characters/Ororo/images/standing/hair_[Ororo.Clothes[hair].string].webp"
    elif "mohawk" in Ororo.Clothes["hair"].string:
        "characters/Ororo/images/standing/hair_wet_mohawk.webp"
    else:
        "characters/Ororo/images/standing/hair_wet.webp"

    if Ororo.Clothes["face_inner_accessory"].string:
        "characters/Ororo/images/standing/face_inner_accessory_[Ororo.Clothes[face_inner_accessory].string].webp"

    if Ororo.spunk["tongue"] and Ororo.mouth in ["agape", "tongue"]:
        "characters/Ororo/images/standing/spunk_tongue.webp"

    if Ororo.spunk["mouth"] and Ororo.mouth in ["agape", "tongue"]:
        "characters/Ororo/images/standing/spunk_mouth.webp"

    if not Ororo.spunk["chin"]:
        Null()
    elif Ororo.mouth in ["agape", "tongue"]:
        "characters/Ororo/images/standing/spunk_chin_open.webp"
    else:
        "characters/Ororo/images/standing/spunk_chin.webp"

    if Ororo.spunk["face"]:
        "characters/Ororo/images/standing/spunk_face.webp"

    if Ororo.spunk["hair"]:
        "characters/Ororo/images/standing/spunk_hair.webp"

    if Ororo.electricity:
        "characters/Ororo/images/standing/electricity.webp"

    anchor (int(837*character_sampling), int(844*character_sampling))
    offset (int(837*character_sampling), int(844*character_sampling))

image Ororo_standing_blinking:
    "characters/Ororo/images/standing/eyes_[Ororo.eyes].webp"
    choice:
        4.5
    choice:
        4.0
    choice:
        3.5
    "characters/Ororo/images/standing/eyes_blink1.webp"
    0.027
    "characters/Ororo/images/standing/eyes_blink2.webp"
    0.027
    "characters/Ororo/images/standing/eyes_closed.webp"
    0.054
    "characters/Ororo/images/standing/eyes_blink2.webp"
    0.018
    "characters/Ororo/images/standing/eyes_blink1.webp"
    0.072
    repeat