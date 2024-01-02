transform Ororo_standing_head_animation:
    subpixel True
    transform_anchor True
    animation
    
    pos (0.0, 0.0)
    xzoom 1.0 yzoom 1.0
    rotate 0.0

    block:
        pause 6.7
        ease 2.0 rotate -1
        pause 4.5
        ease 2.0 rotate 1
        pause 5.7
        ease 2.0 rotate 0

        repeat

transform Ororo_standing_right_arm_animation:
    subpixel True
    transform_anchor True
    animation
    
    pos (0.0, 0.0)
    xzoom 1.0 yzoom 1.0
    rotate 0.0

    block:
        pause 2.6
        ease 2.0 rotate -1
        pause 5.3
        ease 2.0 rotate 0
        pause 3.4
        ease 2.0 rotate -2

        repeat

transform Ororo_standing_left_arm_animation:
    subpixel True
    transform_anchor True
    animation
    
    pos (0.0, 0.0)
    xzoom 1.0 yzoom 1.0
    rotate 0.0

    block:
        pause 2.5
        ease 2.0 rotate 0.5
        pause 5.8
        ease 2.0 rotate -0.5
        pause 4.5
        ease 2.0 rotate 0

        repeat
    
image Ororo_sprite standing:
    contains:
        "Ororo_standing_temp"

    xysize (int(2500*character_sampling), int(4500*character_sampling))

layeredimage Ororo_standing_temp:
    if Ororo.hovered:
        "Ororo_standing" at hover
    else:
        "Ororo_standing"

layeredimage Ororo_standing:
    if Ororo.check_traits("ground_shadow"):
        "characters/Ororo/images/standing/ground_shadow.webp" at Transform(blend = "multiply")

    if renpy.get_screen("Wardrobe_screen"):
        "Ororo_standing_hair_back"
    else:
        "Ororo_standing_hair_back" at Ororo_standing_head_animation

    if Ororo.Clothes["cloak"].string:
        "characters/Ororo/images/standing/cloak_[Ororo.Clothes[cloak].string]_back.webp"

    if Ororo.right_arm in ["bra"]:
        "characters/Ororo/images/standing/right_forearm_[Ororo.right_arm].webp"

    if not Ororo.Clothes["bodysuit"].string:
        Null()
    elif Ororo.Clothes["bodysuit"].string in ["black_classic_suit"] and Ororo.Clothes["bodysuit"].state == 1:
        Null()
    elif Ororo.right_arm in ["bra"]:
        "characters/Ororo/images/standing/bodysuit_[Ororo.Clothes[bodysuit].string]_right_forearm_sleeve_[Ororo.right_arm].webp"

    if not Ororo.Clothes["gloves"].string:
        Null()
    elif Ororo.right_arm in ["bra"]:
        "characters/Ororo/images/standing/gloves_[Ororo.Clothes[gloves].string]_right_[Ororo.right_arm].webp"

    if Ororo.left_arm in ["bra", "storm1", "touch_ass"]:
        "characters/Ororo/images/standing/left_forearm_[Ororo.left_arm].webp"

    if not Ororo.Clothes["bodysuit"].string:
        Null()
    elif Ororo.Clothes["bodysuit"].string in ["black_classic_suit"] and Ororo.Clothes["bodysuit"].state == 1:
        Null()
    elif Ororo.left_arm in ["bra", "storm1", "touch_ass"]:
        "characters/Ororo/images/standing/bodysuit_[Ororo.Clothes[bodysuit].string]_left_forearm_sleeve_[Ororo.left_arm].webp"

    if not Ororo.Clothes["gloves"].string:
        Null()
    elif Ororo.left_arm in ["bra", "storm1", "touch_ass"]:
        "characters/Ororo/images/standing/gloves_[Ororo.Clothes[gloves].string]_left_[Ororo.left_arm].webp"

    always:
        "Ororo_standing_body"

    if Ororo.right_arm in ["hip", "touch_pussy"]:
        "characters/Ororo/images/standing/right_forearm_[Ororo.right_arm]_shadow.webp" at Transform(blend = "multiply")

    if Ororo.right_arm in ["crossed", "hip", "touch_pussy"]:
        "characters/Ororo/images/standing/right_forearm_[Ororo.right_arm].webp"

    if not Ororo.Clothes["bodysuit"].string:
        Null()
    elif Ororo.Clothes["bodysuit"].string in ["black_classic_suit"] and Ororo.Clothes["bodysuit"].state == 1:
        Null()
    elif Ororo.left_arm == "crossed" and Ororo.right_arm == "crossed":
        "characters/Ororo/images/standing/bodysuit_[Ororo.Clothes[bodysuit].string]_sleeves_crossed.webp"
    elif Ororo.right_arm in ["hip", "touch_pussy"]:
        "characters/Ororo/images/standing/bodysuit_[Ororo.Clothes[bodysuit].string]_right_forearm_sleeve_[Ororo.right_arm].webp"

    if not Ororo.Clothes["gloves"].string:
        Null()
    elif Ororo.left_arm == "crossed" and Ororo.right_arm == "crossed":
        "characters/Ororo/images/standing/gloves_[Ororo.Clothes[gloves].string]_crossed.webp"
    elif Ororo.right_arm in ["hip", "touch_pussy"]:
        "characters/Ororo/images/standing/gloves_[Ororo.Clothes[gloves].string]_right_[Ororo.right_arm].webp"

    if Ororo.left_arm in ["grope", "hip"]:
        "characters/Ororo/images/standing/left_forearm_[Ororo.left_arm]_shadow.webp" at Transform(blend = "multiply")

    if Ororo.left_arm in ["grope", "hip"]:
        "characters/Ororo/images/standing/left_forearm_[Ororo.left_arm].webp"

    if not Ororo.Clothes["bodysuit"].string:
        Null()
    elif Ororo.Clothes["bodysuit"].string in ["black_classic_suit"] and Ororo.Clothes["bodysuit"].state == 1:
        Null()
    elif Ororo.left_arm in ["grope", "hip"]:
        "characters/Ororo/images/standing/bodysuit_[Ororo.Clothes[bodysuit].string]_left_forearm_sleeve_[Ororo.left_arm].webp"

    if not Ororo.Clothes["gloves"].string:
        Null()
    elif Ororo.left_arm in ["grope", "hip"]:
        "characters/Ororo/images/standing/gloves_[Ororo.Clothes[gloves].string]_left_[Ororo.left_arm].webp"

    if renpy.get_screen("Wardrobe_screen"):
        "Ororo_standing_head"
    else:
        "Ororo_standing_head" at Ororo_standing_head_animation

    if Ororo.right_arm in ["extended", "fight", "storm1"]:
        "characters/Ororo/images/standing/right_forearm_[Ororo.right_arm].webp"

    if not Ororo.Clothes["bodysuit"].string:
        Null()
    elif Ororo.Clothes["bodysuit"].string in ["black_classic_suit"] and Ororo.Clothes["bodysuit"].state == 1:
        Null()
    elif Ororo.right_arm in ["extended", "fight"]:
        "characters/Ororo/images/standing/bodysuit_[Ororo.Clothes[bodysuit].string]_right_forearm_sleeve_[Ororo.right_arm].webp"

    if not Ororo.Clothes["gloves"].string:
        Null()
    elif Ororo.right_arm in ["extended", "fight", "storm1"]:
        "characters/Ororo/images/standing/gloves_[Ororo.Clothes[gloves].string]_right_[Ororo.right_arm].webp"

    if Ororo.left_arm in ["rub_neck"]:
        "characters/Ororo/images/standing/left_forearm_[Ororo.left_arm]_shadow.webp" at Transform(blend = "multiply")

    if Ororo.left_arm in ["fight", "rub_neck"]:
        "characters/Ororo/images/standing/left_forearm_[Ororo.left_arm].webp"

    if not Ororo.Clothes["bodysuit"].string:
        Null()
    elif Ororo.Clothes["bodysuit"].string in ["black_classic_suit"] and Ororo.Clothes["bodysuit"].state == 1:
        Null()
    elif Ororo.left_arm in ["fight", "rub_neck"]:
        "characters/Ororo/images/standing/bodysuit_[Ororo.Clothes[bodysuit].string]_left_forearm_sleeve_[Ororo.left_arm].webp"

    if not Ororo.Clothes["gloves"].string:
        Null()
    elif Ororo.left_arm in ["fight", "rub_neck"]:
        "characters/Ororo/images/standing/gloves_[Ororo.Clothes[gloves].string]_left_[Ororo.left_arm].webp"

layeredimage Ororo_standing_hair_back:
    # if not Ororo.check_traits("wet") and "wet" not in Ororo.Clothes["hair"].string:
    always:
        "characters/Ororo/images/standing/hair_back_[Ororo.Clothes[hair].string].webp"
    # elif "mohawk" in Ororo.Clothes["hair"].string:
    #     Null()
    # else:
    #     "characters/Ororo/images/standing/hair_back_wet.webp"

    anchor (int(1290*character_sampling), int(1190*character_sampling))
    offset (int(1290*character_sampling), int(1190*character_sampling))

layeredimage Ororo_standing_body:
    always:
        "characters/Ororo/images/standing/body.webp"

    always:
        "characters/Ororo/images/standing/right_foot.webp"

    always:
        "characters/Ororo/images/standing/left_foot.webp"

    if Ororo.Clothes["bodysuit"].string:
        "characters/Ororo/images/standing/bodysuit_[Ororo.Clothes[bodysuit].string]_lower.webp"

    if Ororo.Clothes["footwear"].string:
        "characters/Ororo/images/standing/footwear_[Ororo.Clothes[footwear].string].webp"

    if Ororo.Clothes["pants"].string:
        "characters/Ororo/images/standing/pants_[Ororo.Clothes[pants].string]_[Ororo.Clothes[pants].state].webp"

    if Ororo.left_arm == "crossed" and Ororo.right_arm == "crossed":
        "characters/Ororo/images/standing/arms_crossed_shadow.webp" at Transform(blend = "multiply")

    if Ororo.left_arm == "crossed" and Ororo.right_arm == "crossed":
        "characters/Ororo/images/standing/arms_crossed.webp"

    if Ororo.right_arm in ["neutral"]:
        "characters/Ororo/images/standing/right_arm_[Ororo.right_arm]_shadow.webp" at Transform(blend = "multiply")

    if Ororo.right_arm not in ["bra", "extended", "fight", "fist", "hip", "neutral", "storm1", "storm2", "touch_pussy"]:
        Null()
    elif renpy.get_screen("Wardrobe_screen"):
        "Ororo_standing_right_arm"
    elif Ororo.right_arm == "neutral":
        "Ororo_standing_right_arm" at Ororo_standing_right_arm_animation
    else:
        "Ororo_standing_right_arm"

    if Ororo.left_arm not in ["bra", "extended", "fight", "fist", "hip", "neutral", "rub_neck", "storm1", "storm2", "touch_ass"]:
        Null()
    elif renpy.get_screen("Wardrobe_screen"):
        "Ororo_standing_left_arm"
    elif Ororo.left_arm == "neutral":
        "Ororo_standing_left_arm" at Ororo_standing_left_arm_animation
    else:
        "Ororo_standing_left_arm"

    if Ororo.left_arm == "crossed" and Ororo.right_arm == "crossed":
        "characters/Ororo/images/standing/breasts_crossed_shadow.webp" at Transform(blend = "multiply")
    elif Ororo.left_arm == "grope":
        "characters/Ororo/images/standing/breasts_grope_shadow.webp" at Transform(blend = "multiply")
    else:
        "characters/Ororo/images/standing/breasts_shadow.webp" at Transform(blend = "multiply")

    if Ororo.left_arm == "crossed" and Ororo.right_arm == "crossed":
        "characters/Ororo/images/standing/breasts_crossed.webp"
    elif Ororo.left_arm == "grope":
        "characters/Ororo/images/standing/breasts_grope.webp"
    else:
        "characters/Ororo/images/standing/breasts.webp"

    if not Ororo.Clothes["bodysuit"].string:
        Null()
    elif Ororo.Clothes["bodysuit"].string in ["black_classic_suit"] and Ororo.Clothes["bodysuit"].state == 1:
        "characters/Ororo/images/standing/bodysuit_[Ororo.Clothes[bodysuit].string]_[Ororo.Clothes[bodysuit].state].webp"
    elif Ororo.left_arm == "crossed" and Ororo.right_arm == "crossed":
        "characters/Ororo/images/standing/bodysuit_[Ororo.Clothes[bodysuit].string]_[Ororo.Clothes[bodysuit].state]_crossed.webp"
    else:
        "characters/Ororo/images/standing/bodysuit_[Ororo.Clothes[bodysuit].string]_[Ororo.Clothes[bodysuit].state].webp"

    if not Ororo.Clothes["top"].string:
        Null()
    elif Ororo.Clothes["top"].string in ["white_top"] and Ororo.Clothes["top"].state == 1:
        "characters/Ororo/images/standing/top_[Ororo.Clothes[top].string]_[Ororo.Clothes[top].state].webp"
    elif Ororo.left_arm == "crossed" and Ororo.right_arm == "crossed":
        "characters/Ororo/images/standing/top_[Ororo.Clothes[top].string]_[Ororo.Clothes[top].state]_crossed.webp"
    else:
        "characters/Ororo/images/standing/top_[Ororo.Clothes[top].string]_[Ororo.Clothes[top].state].webp"

    if not Ororo.Clothes["cloak"].string:
        Null()
    elif Ororo.right_arm in ["crossed", "fist"]:
        "characters/Ororo/images/standing/cloak_[Ororo.Clothes[cloak].string]_right_shoulder_neutral.webp"
    elif Ororo.right_arm in ["bra", "extended", "fight", "hip", "neutral", "storm1", "storm2", "touch_pussy"]:
        "characters/Ororo/images/standing/cloak_[Ororo.Clothes[cloak].string]_right_shoulder_[Ororo.right_arm].webp"

    if not Ororo.Clothes["cloak"].string:
        Null()
    elif Ororo.left_arm in ["crossed", "fist"]:
        "characters/Ororo/images/standing/cloak_[Ororo.Clothes[cloak].string]_left_shoulder_neutral.webp"
    elif Ororo.left_arm in ["bra", "extended", "fight", "hip", "neutral", "rub_neck", "storm1", "storm2", "touch_ass"]:
        "characters/Ororo/images/standing/cloak_[Ororo.Clothes[cloak].string]_left_shoulder_[Ororo.left_arm].webp"

layeredimage Ororo_standing_right_arm:
    always:
        "characters/Ororo/images/standing/right_arm_[Ororo.right_arm].webp"

    if not Ororo.Clothes["bodysuit"].string:
        Null()
    elif Ororo.Clothes["bodysuit"].string in ["black_classic_suit"] and Ororo.Clothes["bodysuit"].state == 1:
        Null()
    else:
        "characters/Ororo/images/standing/bodysuit_[Ororo.Clothes[bodysuit].string]_right_sleeve_[Ororo.right_arm].webp"

    if not Ororo.Clothes["gloves"].string:
        Null()
    elif Ororo.right_arm in ["fist", "hip", "neutral", "storm2"]:
        "characters/Ororo/images/standing/gloves_[Ororo.Clothes[gloves].string]_right_[Ororo.right_arm].webp"

    anchor (int(940*character_sampling), int(1420*character_sampling))
    offset (int(940*character_sampling), int(1420*character_sampling))

layeredimage Ororo_standing_left_arm:
    always:
        "characters/Ororo/images/standing/left_arm_[Ororo.left_arm].webp"

    if not Ororo.Clothes["bodysuit"].string:
        Null()
    elif Ororo.Clothes["bodysuit"].string in ["black_classic_suit"] and Ororo.Clothes["bodysuit"].state == 1:
        Null()
    else:
        "characters/Ororo/images/standing/bodysuit_[Ororo.Clothes[bodysuit].string]_left_sleeve_[Ororo.left_arm].webp"

    if not Ororo.Clothes["gloves"].string:
        Null()
    elif Ororo.left_arm in ["extended", "fist", "hip", "neutral", "storm2"]:
        "characters/Ororo/images/standing/gloves_[Ororo.Clothes[gloves].string]_left_[Ororo.left_arm].webp"

    anchor (int(1600*character_sampling), int(1460*character_sampling))
    offset (int(1600*character_sampling), int(1460*character_sampling))

layeredimage Ororo_standing_head:
    always:
        "characters/Ororo/images/standing/head.webp"

    always:
        "characters/Ororo/images/standing/mouth_[Ororo.mouth].webp"

    if Ororo.check_traits("white") or Ororo.check_traits("electricity"):
        "characters/Ororo/images/standing/eyes_white.webp"
    elif Ororo.eyes in ["closed", "down", "left", "right", "squint", "up", "wink"]:
        "characters/Ororo/images/standing/eyes_[Ororo.eyes].webp"
    else:
        "Ororo_standing_blinking"

    always:
        "characters/Ororo/images/standing/brows_[Ororo.brows].webp"

    if Ororo.blush:
        "characters/Ororo/images/standing/blush[Ororo.blush].webp"

    # if not Ororo.check_traits("wet") and "wet" not in Ororo.Clothes["hair"].string:
    always:
        "characters/Ororo/images/standing/hair_[Ororo.Clothes[hair].string]_shadow.webp" at Transform(blend = "multiply")
    # elif "mohawk" in Ororo.Clothes["hair"].string:
    #     "characters/Ororo/images/standing/hair_wet_mohawk_shadow.webp" at Transform(blend = "multiply")
    # else:
    #     "characters/Ororo/images/standing/hair_wet_shadow.webp" at Transform(blend = "multiply")

    # if not Ororo.check_traits("wet") and "wet" not in Ororo.Clothes["hair"].string:
    always:
        "characters/Ororo/images/standing/hair_[Ororo.Clothes[hair].string].webp"
    # elif "mohawk" in Ororo.Clothes["hair"].string:
    #     "characters/Ororo/images/standing/hair_wet_mohawk.webp"
    # else:
    #     "characters/Ororo/images/standing/hair_wet.webp"

    if Ororo.Clothes["face_inner_accessory"].string:
        "characters/Ororo/images/standing/face_inner_accessory_[Ororo.Clothes[face_inner_accessory].string].webp"

    if Ororo.check_traits("electricity"):
        "characters/Ororo/images/standing/electricity.webp"

    anchor (int(1290*character_sampling), int(1190*character_sampling))
    offset (int(1290*character_sampling), int(1190*character_sampling))

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