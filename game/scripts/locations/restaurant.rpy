layeredimage bg_restaurant_table:
    always:
        "images/backgrounds/base/bg_restaurant_table.webp"

    if food_arrived:
        "images/backgrounds/base/bg_restaurant_Player_plate.webp"

    if drinking_wine:
        "images/backgrounds/base/bg_restaurant_glass.webp"

    if not ordered_food:
        "images/backgrounds/base/bg_restaurant_menu.webp"

    if drinking_wine:
        "images/backgrounds/base/bg_restaurant_bottle.webp"

    if food_arrived:
        "images/backgrounds/base/bg_restaurant_Girl_plate.webp"

    always:
        "images/backgrounds/base/bg_restaurant_shakers.webp"