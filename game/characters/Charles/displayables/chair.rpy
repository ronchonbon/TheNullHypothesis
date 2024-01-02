transform Charles_chair_head_animation:
    subpixel True
    transform_anchor True
    animation
    
    pos (0.0, 0.0)
    xzoom 1.0 yzoom 1.0
    rotate 0.0

    block:
        pause 3.2
        ease 2.0 rotate -2
        pause 4.6
        ease 2.0 rotate 2
        pause 6.2
        ease 2.0 rotate 0

        repeat

transform Charles_chair_psychic_animation:
    subpixel True
    transform_anchor True
    
    pos (0.0, 0.0)
    xzoom 1.0 yzoom 1.0
    rotate 0.0

    block:
        linear 1.0 alpha 0.75
        linear 1.0 alpha 1.0
        repeat

transform Charles_chair_activating_psychic_animation:
    subpixel True
    transform_anchor True
    
    pos (0.0, 0.0)
    xzoom 1.0 yzoom 1.0
    rotate 0.0

    alpha 0.0
    ease 0.5 alpha 1.0
    
transform Charles_chair_deactivating_psychic_animation:
    subpixel True
    transform_anchor True
    
    pos (0.0, 0.0)
    xzoom 1.0 yzoom 1.0
    rotate 0.0

    ease 0.5 alpha 0.0
    
image Charles_sprite:
    contains:
        "Charles_chair_temp"

    xysize (int(2500*character_sampling), int(4000*character_sampling))

layeredimage Charles_chair_temp:
    if Charles.hovered:
        "Charles_chair" at hover
    else:
        "Charles_chair"

    xysize (int(2500*character_sampling), int(4000*character_sampling))

layeredimage Charles_chair:
    if Charles.check_traits("ground_shadow"):
        "characters/Charles/images/ground_shadow.webp" at Transform(blend = "multiply")

    always:
        "characters/Charles/images/body.webp"

    always:
        "characters/Charles/images/arms_shadow.webp" at Transform(blend = "multiply")

    always:
        "characters/Charles/images/arms.webp"

    always:
        "Charles_chair_head" at Charles_chair_head_animation

layeredimage Charles_chair_head:
    always:
        "characters/Charles/images/head.webp"

    always:
        "characters/Charles/images/mouth_[Charles.mouth].webp"

    if Charles.eyes in ["closed", "down", "left", "right", "squint", "up", "wink"]:
        "characters/Charles/images/standing/eyes_[Charles.eyes].webp"
    else:
        "Charles_blinking"

    always:
        "characters/Charles/images/brows_[Charles.brows].webp"

    if Charles.blush:
        "characters/Charles/images/standing/blush[Charles.blush].webp"

    if Charles.psychic and Charles.activating_psychic:
        "Charles_chair_psychic" at Charles_chair_activating_psychic_animation
    elif Charles.psychic:
        "Charles_chair_psychic" at Charles_chair_psychic_animation
    elif Charles.deactivating_psychic:
        "Charles_chair_psychic" at Charles_chair_deactivating_psychic_animation

    anchor (int(1200*character_sampling), int(1770*character_sampling))
    offset (int(1200*character_sampling), int(1770*character_sampling))

image Charles_chair_psychic:
    "characters/Charles/images/psychic.webp"

    anchor (int(1225*character_sampling), int(1500*character_sampling))
    offset (int(1225*character_sampling), int(1500*character_sampling))

image Charles_blinking:
    "characters/Charles/images/eyes_[Charles.eyes].webp"
    choice:
        4.5
    choice:
        4.0
    choice:
        3.5
    "characters/Charles/images/eyes_blink1.webp"
    0.023
    "characters/Charles/images/eyes_blink2.webp"
    0.023
    "characters/Charles/images/eyes_closed.webp"
    0.054
    "characters/Charles/images/eyes_blink2.webp"
    0.018
    "characters/Charles/images/eyes_blink1.webp"
    0.072
    repeat