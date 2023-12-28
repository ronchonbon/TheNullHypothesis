layeredimage bg_infirmary:
    if time_index >= 3:
        "images/backgrounds/base/bg_infirmary_dark.webp"
    else:
        "images/backgrounds/base/bg_infirmary.webp"

    if infirmary_in_bed:
        "images/backgrounds/base/bg_infirmary_bed.webp"
    elif infirmary_bed:
        "images/backgrounds/base/bg_infirmary_bed_empty.webp"
    
    if infirmary_in_bed:
        "images/backgrounds/base/bg_infirmary_screenlight.webp"

    if infirmary_screen1:
        "images/backgrounds/base/bg_infirmary_screens1.webp"

    if infirmary_screen2:
        "images/backgrounds/base/bg_infirmary_screens2.webp"

    if infirmary_screen3:
        "images/backgrounds/base/bg_infirmary_screens3.webp"

    if time_index >= 3:
        "images/backgrounds/base/bg_infirmary_night_hard_light.webp" at Transform(blend = "multiply")

    if time_index >= 3:
        "images/backgrounds/base/bg_infirmary_night_linear_dodge.webp" at Transform(blend = "add")