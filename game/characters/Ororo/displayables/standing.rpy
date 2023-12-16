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
        ConditionSwitch(
            "Ororo.hovered", At("Ororo_standing", hover),
            "True", "Ororo_standing")

    xysize (int(2500*character_sampling), int(4500*character_sampling))

layeredimage Ororo_standing:
    if Ororo.ground_shadow:
        "characters/Ororo/images/standing/ground_shadow.webp"

    if renpy.get_screen("Wardrobe_screen"):
        "Ororo_standing_hair_back"
    else:
        At("Ororo_standing_hair_back", Ororo_standing_head_animation)

    if Ororo.right_arm in ["bra"]:
        "characters/Ororo/images/standing/right_forearm_[Ororo.right_arm].webp"

    if Ororo.left_arm in ["bra", "storm1", "touch_ass"]:
        "characters/Ororo/images/standing/left_forearm_[Ororo.left_arm].webp"

    always:
        "Ororo_standing_body"

    if Ororo.right_arm in ["touch_pussy"]:
        "characters/Ororo/images/standing/right_forearm_[Ororo.right_arm]_shadow.webp"

    if Ororo.right_arm in ["crossed", "touch_pussy"]:
        "characters/Ororo/images/standing/right_forearm_[Ororo.right_arm].webp"

    if Ororo.left_arm in ["grope"]:
        "characters/Ororo/images/standing/left_forearm_[Ororo.left_arm]_shadow.webp"

    if Ororo.left_arm in ["grope"]:
        "characters/Ororo/images/standing/left_forearm_[Ororo.left_arm].webp"

    if renpy.get_screen("Wardrobe_screen"):
        "Ororo_standing_head"
    else:
        At("Ororo_standing_head", Ororo_standing_head_animation)

    if Ororo.right_arm in ["extended", "fight", "storm1"]:
        "characters/Ororo/images/standing/right_forearm_[Ororo.right_arm].webp"

    if Ororo.left_arm in ["rub_neck"]:
        "characters/Ororo/images/standing/left_forearm_[Ororo.left_arm]_shadow.webp"

    if Ororo.left_arm in ["fight", "rub_neck"]:
        "characters/Ororo/images/standing/left_forearm_[Ororo.left_arm].webp"

layeredimage Ororo_standing_hair_back:
    # if not Ororo.wet and "wet" not in Ororo.Clothes["hair"].string:
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

    if Ororo.left_arm == "crossed" and Ororo.right_arm == "crossed":
        "characters/Ororo/images/standing/arms_crossed_shadow.webp"

    if Ororo.left_arm == "crossed" and Ororo.right_arm == "crossed":
        "characters/Ororo/images/standing/arms_crossed.webp"

    if Ororo.right_arm in ["hip", "neutral"]:
        "characters/Ororo/images/standing/right_arm_[Ororo.right_arm]_shadow.webp"

    if Ororo.right_arm not in ["bra", "extended", "fight", "fist", "hip", "neutral", "storm1", "storm2", "touch_pussy"]:
        Null()
    elif renpy.get_screen("Wardrobe_screen"):
        "Ororo_standing_right_arm"
    elif Ororo.right_arm == "neutral":
        At("Ororo_standing_right_arm", Ororo_standing_right_arm_animation)
    else:
        "Ororo_standing_right_arm"

    if Ororo.left_arm in ["hip"]:
        "characters/Ororo/images/standing/left_arm_[Ororo.left_arm]_shadow.webp"

    if Ororo.left_arm not in ["bra", "extended", "fight", "fist", "hip", "neutral", "rub_neck", "storm1", "storm2", "touch_ass"]:
        Null()
    elif renpy.get_screen("Wardrobe_screen"):
        "Ororo_standing_left_arm"
    elif Ororo.left_arm == "neutral":
        At("Ororo_standing_left_arm", Ororo_standing_left_arm_animation)
    else:
        "Ororo_standing_left_arm"

    if Ororo.left_arm == "crossed" and Ororo.right_arm == "crossed":
        "characters/Ororo/images/standing/breasts_crossed_shadow.webp"
    elif Ororo.left_arm == "grope":
        "characters/Ororo/images/standing/breasts_grope_shadow.webp"
    else:
        "characters/Ororo/images/standing/breasts_shadow.webp"

    if Ororo.left_arm == "crossed" and Ororo.right_arm == "crossed":
        "characters/Ororo/images/standing/breasts_crossed.webp"
    elif Ororo.left_arm == "grope":
        "characters/Ororo/images/standing/breasts_grope.webp"
    else:
        "characters/Ororo/images/standing/breasts.webp"

layeredimage Ororo_standing_right_arm:
    always:
        "characters/Ororo/images/standing/right_arm_[Ororo.right_arm].webp"

    anchor (int(940*character_sampling), int(1420*character_sampling))
    offset (int(940*character_sampling), int(1420*character_sampling))

layeredimage Ororo_standing_left_arm:
    always:
        "characters/Ororo/images/standing/left_arm_[Ororo.left_arm].webp"

    anchor (int(1600*character_sampling), int(1460*character_sampling))
    offset (int(1600*character_sampling), int(1460*character_sampling))

layeredimage Ororo_standing_head:
    always:
        "characters/Ororo/images/standing/head.webp"

    always:
        "characters/Ororo/images/standing/mouth_[Ororo.mouth].webp"

    if Ororo.white or Ororo.electricity:
        "characters/Ororo/images/standing/eyes_white.webp"
    elif Ororo.eyes in ["closed", "down", "left", "right", "squint", "up", "wink"]:
        "characters/Ororo/images/standing/eyes_[Ororo.eyes].webp"
    else:
        "Ororo_standing_blinking"

    always:
        "characters/Ororo/images/standing/brows_[Ororo.brows].webp"

    if Ororo.blush:
        "characters/Ororo/images/standing/blush[Ororo.blush].webp"

    # if not Ororo.wet and "wet" not in Ororo.Clothes["hair"].string:
    always:
        "characters/Ororo/images/standing/hair_[Ororo.Clothes[hair].string]_shadow.webp"
    # elif "mohawk" in Ororo.Clothes["hair"].string:
    #     "characters/Ororo/images/standing/hair_wet_mohawk_shadow.webp"
    # else:
    #     "characters/Ororo/images/standing/hair_wet_shadow.webp"

    # if not Ororo.wet and "wet" not in Ororo.Clothes["hair"].string:
    always:
        "characters/Ororo/images/standing/hair_[Ororo.Clothes[hair].string].webp"
    # elif "mohawk" in Ororo.Clothes["hair"].string:
    #     "characters/Ororo/images/standing/hair_wet_mohawk.webp"
    # else:
    #     "characters/Ororo/images/standing/hair_wet.webp"

    if Ororo.electricity:
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