transform Kurt_standing_tail_animation:
    subpixel True
    transform_anchor True
    animation
    
    pos (0.0, 0.0)
    xzoom 1.0 yzoom 1.0
    rotate 0.0

    block:
        pause 4.2
        ease 2.0 rotate 1
        pause 2.5
        ease 2.0 rotate -1
        pause 5.6
        ease 2.0 rotate 0

        repeat
    
transform Kurt_standing_head_animation:
    subpixel True
    transform_anchor True
    animation
    
    pos (0.0, 0.0)
    xzoom 1.0 yzoom 1.0
    rotate 0.0

    block:
        pause 2.3
        ease 2.0 rotate -1
        pause 5.7
        ease 2.0 rotate 1
        pause 7.4
        ease 2.0 rotate 0

        repeat

transform Kurt_standing_right_arm_animation:
    subpixel True
    transform_anchor True
    animation
    
    pos (0.0, 0.0)
    xzoom 1.0 yzoom 1.0
    rotate 0.0

    block:
        pause 4.3
        ease 2.0 rotate 2
        pause 4.5
        ease 2.0 rotate 0
        pause 3.6
        ease 2.0 rotate -2

        repeat

transform Kurt_standing_left_arm_animation:
    subpixel True
    transform_anchor True
    animation
    
    pos (0.0, 0.0)
    xzoom 1.0 yzoom 1.0
    rotate 0.0

    block:
        pause 6.2
        ease 2.0 rotate 0
        pause 5.1
        ease 2.0 rotate -2
        pause 4.5
        ease 2.0 rotate 2

        repeat
    
image Kurt_sprite:
    contains:
        "Kurt_standing_temp"

    xysize (int(2500*character_sampling), int(4500*character_sampling))

layeredimage Kurt_standing_temp:
    if Kurt.hovered:
        "Kurt_standing" at hover
    else:
        "Kurt_standing"

layeredimage Kurt_standing:
    if Kurt.check_traits("teleporting_out") or Kurt.check_traits("smoke") or not Kurt.check_traits("ground_shadow"):
        Null()
    else:
        "characters/Kurt/images/ground_shadow.webp" at Transform(blend = "multiply")

    if Kurt.check_traits("teleporting_out") or Kurt.check_traits("smoke") or Kurt.check_traits("tail_hidden"):
        Null()
    else:
        "Kurt_standing_tail" at Kurt_standing_tail_animation

    if Kurt.check_traits("teleporting_out") or Kurt.check_traits("smoke"):
        Null()
    elif Kurt.left_arm in ["rub_neck"]:
        "characters/Kurt/images/left_forearm_[Kurt.left_arm].webp"

    if Kurt.check_traits("teleporting_out") or Kurt.check_traits("smoke"):
        Null()
    elif Kurt.right_arm in ["crossed", "extended", "fight", "fist", "neutral", "question"]:
        "Kurt_standing_right_arm" at Kurt_standing_right_arm_animation

    if Kurt.check_traits("teleporting_out") or Kurt.check_traits("smoke"):
        Null()
    else:
        "characters/Kurt/images/body.webp"

    if Kurt.check_traits("teleporting_out") or Kurt.check_traits("smoke"):
        Null()
    else:
        "characters/Kurt/images/right_foot.webp"

    if Kurt.check_traits("teleporting_out") or Kurt.check_traits("smoke"):
        Null()
    else:
        "characters/Kurt/images/left_foot.webp"

    if Kurt.check_traits("teleporting_out") or Kurt.check_traits("smoke"):
        Null()
    elif Kurt.left_arm in ["crossed", "fist", "neutral", "rub_neck"]:
        "characters/Kurt/images/left_arm_[Kurt.left_arm]_shadow.webp" at Transform(blend = "multiply")

    if Kurt.check_traits("teleporting_out") or Kurt.check_traits("smoke"):
        Null()
    elif Kurt.left_arm in ["crossed", "fight", "fist", "neutral", "rub_neck"]:
        "Kurt_standing_left_arm" at Kurt_standing_left_arm_animation

    if Kurt.check_traits("teleporting_out") or Kurt.check_traits("smoke"):
        Null()
    else:
        "Kurt_standing_head" at Kurt_standing_head_animation

    if Kurt.check_traits("teleporting_out") or Kurt.check_traits("smoke"):
        Null()
    elif Kurt.right_arm in ["fight", "question"]:
        "characters/Kurt/images/right_forearm_[Kurt.right_arm].webp"

    if Kurt.check_traits("teleporting_out") or Kurt.check_traits("smoke"):
        Null()
    elif Kurt.left_arm in ["extended", "fight"]:
        "characters/Kurt/images/left_forearm_[Kurt.left_arm].webp"

    if not Kurt.check_traits("teleporting_out") and not Kurt.check_traits("teleporting_in") and not Kurt.check_traits("smoke"):
        Null()
    else:
        "Kurt_smoke"

image Kurt_standing_tail:
    "characters/Kurt/images/tail.webp"
    
    anchor (int(1250*character_sampling), int(2400*character_sampling))
    offset (int(1250*character_sampling), int(2400*character_sampling))

image Kurt_standing_right_arm:
    "characters/Kurt/images/right_arm_[Kurt.right_arm].webp"
    
    anchor (int(900*character_sampling), int(1630*character_sampling))
    offset (int(900*character_sampling), int(1630*character_sampling))

image Kurt_standing_left_arm:
    "characters/Kurt/images/left_arm_[Kurt.left_arm].webp"
    
    anchor (int(1615*character_sampling), int(1620*character_sampling))
    offset (int(1615*character_sampling), int(1620*character_sampling))

layeredimage Kurt_standing_head:
    always:
        "characters/Kurt/images/head.webp"

    always:
        "characters/Kurt/images/mouth_[Kurt.mouth].webp"

    if Kurt.beard:
        "characters/Kurt/images/beard_[Kurt.beard]_shadow.webp" at Transform(blend = "multiply")

    if Kurt.beard:
        "characters/Kurt/images/beard_[Kurt.beard].webp"

    if Kurt.eyes in ["closed", "down", "left", "right", "squint", "up", "wink"]:
        "characters/Kurt/images/eyes_[Kurt.eyes].webp"
    else:
        "Kurt_blinking"

    always:
        "characters/Kurt/images/brows_[Kurt.brows].webp"

    if Kurt.blush:
        "characters/Kurt/images/blush[Kurt.blush].webp"

    if Kurt.hair:
        "characters/Kurt/images/hair_[Kurt.hair]_shadow.webp" at Transform(blend = "multiply")

    if Kurt.hair:
        "characters/Kurt/images/hair_[Kurt.hair].webp"

    anchor (int(1250*character_sampling), int(1275*character_sampling))
    offset (int(1250*character_sampling), int(1275*character_sampling))

layeredimage Kurt_smoke:
    if Kurt.check_traits("smoke"):
        "characters/Kurt/images/purple_smoke.webp" at fade_in(0.1)
    else:
        "characters/Kurt/images/purple_smoke.webp" at fade_out(3.0)

image Kurt_blinking:
    "characters/Kurt/images/eyes_[Kurt.eyes].webp"
    choice:
        4.5
    choice:
        4.0
    choice:
        3.5
    "characters/Kurt/images/eyes_blink1.webp"
    0.023
    "characters/Kurt/images/eyes_blink2.webp"
    0.023
    "characters/Kurt/images/eyes_closed.webp"
    0.054
    "characters/Kurt/images/eyes_blink2.webp"
    0.018
    "characters/Kurt/images/eyes_blink1.webp"
    0.072
    repeat