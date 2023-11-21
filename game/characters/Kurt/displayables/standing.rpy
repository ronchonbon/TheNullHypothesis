transform Kurt_standing_tail_animation:
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

transform Kurt_standing_right_arm_animation:
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

transform Kurt_standing_left_arm_animation:
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

transform Kurt_standing_head_animation:
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

transform fade_in(delay):
    alpha 0.0
    linear delay alpha 1.0

transform fade_out(delay):
    linear delay alpha 0.0
    
image Kurt_sprite:
    contains:
        "Kurt_standing_temp"

    xysize (int(2500*character_sampling), int(4500*character_sampling))

layeredimage Kurt_standing_temp:
    if Kurt.hovered:
        At("Kurt_standing", hover)
    else:
        "Kurt_standing"

layeredimage Kurt_standing:
    if Kurt.teleporting_out or Kurt.smoke or not Kurt.ground_shadow:
        Null()
    else:
        "characters/Kurt/images/ground_shadow.webp"

    if Kurt.teleporting_out or Kurt.smoke or Kurt.tail_hidden:
        Null()
    else:
        At("Kurt_standing_tail", Kurt_standing_tail_animation)

    if Kurt.teleporting_out or Kurt.smoke:
        Null()
    else:
        At("Kurt_standing_right_arm", Kurt_standing_right_arm_animation)

    if Kurt.teleporting_out or Kurt.smoke:
        Null()
    else:
        "characters/Kurt/images/body.webp"

    if Kurt.teleporting_out or Kurt.smoke:
        Null()
    else:
        "characters/Kurt/images/right_foot.webp"

    if Kurt.teleporting_out or Kurt.smoke:
        Null()
    else:
        "characters/Kurt/images/left_foot.webp"

    if Kurt.teleporting_out or Kurt.smoke:
        Null()
    else:
        "characters/Kurt/images/left_arm_shadow.webp"

    if Kurt.teleporting_out or Kurt.smoke:
        Null()
    else:
        At("Kurt_standing_left_arm", Kurt_standing_left_arm_animation)

    if Kurt.teleporting_out or Kurt.smoke:
        Null()
    else:
        At("Kurt_standing_head", Kurt_standing_head_animation)

    if not Kurt.teleporting_out and not Kurt.teleporting_in and not Kurt.smoke:
        Null()
    else:
        "Kurt_smoke"

image Kurt_standing_tail:
    "characters/Kurt/images/tail.webp"
    
    anchor (int(1250*character_sampling), int(2400*character_sampling))
    offset (int(1250*character_sampling), int(2400*character_sampling))

image Kurt_standing_right_arm:
    "characters/Kurt/images/right_arm.webp"
    
    anchor (int(900*character_sampling), int(1630*character_sampling))
    offset (int(900*character_sampling), int(1630*character_sampling))

image Kurt_standing_left_arm:
    "characters/Kurt/images/left_arm.webp"
    
    anchor (int(1615*character_sampling), int(1620*character_sampling))
    offset (int(1615*character_sampling), int(1620*character_sampling))

layeredimage Kurt_standing_head:
    always:
        "characters/Kurt/images/head.webp"

    always:
        "characters/Kurt/images/mouth_neutral.webp"

    always:
        "characters/Kurt/images/eyes_neutral.webp"

    always:
        "characters/Kurt/images/brows_neutral.webp"

    always:
        "characters/Kurt/images/hair_quiff.webp"

    anchor (int(1250*character_sampling), int(1275*character_sampling))
    offset (int(1250*character_sampling), int(1275*character_sampling))

layeredimage Kurt_smoke:
    if Kurt.smoke:
        At("characters/Kurt/images/purple_smoke.webp", fade_in(0.1))
    else:
        At("characters/Kurt/images/purple_smoke.webp", fade_out(3.0))

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