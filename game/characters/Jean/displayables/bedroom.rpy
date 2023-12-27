layeredimage bg_Jean:
    always:
        "characters/Jean/images/bedroom/bg_Jean_[lighting].webp"
        
    if Jean.messy_bed:
        "characters/Jean/images/bedroom/bg_Jean_messy_bed.webp"
    else:
        "characters/Jean/images/bedroom/bg_Jean_bed.webp"
        
    always:
        "characters/Jean/images/bedroom/bg_Jean_[Jean.whiteboard].webp"
        
    if "mystery_novel" in Jean.inventory.keys() and "wholesome_romance_novel" in Jean.inventory.keys():
        "characters/Jean/images/bedroom/bg_Jean_books.webp"
        
    if "plant1" in Jean.inventory.keys() and "plant2" in Jean.inventory.keys() and "plant3" in Jean.inventory.keys():
        "characters/Jean/images/bedroom/bg_Jean_plants.webp"

    if Jean.clothes_on_floor:
        "characters/Jean/images/bedroom/bg_Jean_clothes.webp"

    always:
        "characters/Jean/images/bedroom/bg_Jean_[lighting]_hard_light.webp" at Transform(blend = "multiply")

    if lighting in ["day", "night"]:
        "characters/Jean/images/bedroom/bg_Jean_[lighting]_screen.webp" at Transform(blend = "screen")

    always:
        "characters/Jean/images/bedroom/bg_Jean_[lighting]_linear_dodge.webp" at Transform(blend = "add")

    always:
        "characters/Jean/images/bedroom/bg_Jean_[lighting]_multiply.webp" at Transform(blend = "multiply")