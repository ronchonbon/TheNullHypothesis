layeredimage bg_Laura:
    if lighting in ["night", "moonlight"]:
        "characters/Laura/images/bedroom/bg_Laura_night.webp"
    else:
        "characters/Laura/images/bedroom/bg_Laura_day.webp"
        
    if "horror_novel" in Laura.inventory.keys() and "steamy_romance_novel" in Laura.inventory.keys():
        "characters/Laura/images/bedroom/bg_Laura_books.webp"
        
    if "plant1" in Laura.inventory.keys() or "plant2" in Laura.inventory.keys() or "plant3" in Laura.inventory.keys():
        "characters/Laura/images/bedroom/bg_Laura_plants.webp"

    if "motorcycle_helmet" in Laura.inventory.keys():
        "characters/Laura/images/bedroom/bg_Laura_helmet.webp"

    if "motorcycle_posters" in Laura.inventory.keys():
        "characters/Laura/images/bedroom/bg_Laura_motorcycle_posters.webp"

    if "band_posters" in Laura.inventory.keys():
        "characters/Laura/images/bedroom/bg_Laura_band_posters.webp"

    if "boxing_kit" in Laura.inventory.keys():
        "characters/Laura/images/bedroom/bg_Laura_boxing_kit.webp"

    always:
        "characters/Laura/images/bedroom/bg_Laura_dumbbells.webp"

    if "mirror" in Laura.inventory.keys():
        "characters/Laura/images/bedroom/bg_Laura_mirror.webp"

    if Laura.messy_bed:
        "characters/Laura/images/bedroom/bg_Laura_messy_bed.webp"
    else:
        "characters/Laura/images/bedroom/bg_Laura_bed.webp"
        
    if "record_player" in Laura.inventory.keys():
        "characters/Laura/images/bedroom/bg_Laura_record_player.webp"

    if Laura.clothes_on_floor:
        "characters/Laura/images/bedroom/bg_Laura_clothes.webp"

    if "MMA_gloves" in Laura.inventory.keys():
        "characters/Laura/images/bedroom/bg_Laura_gloves.webp"

    always:
        "characters/Laura/images/bedroom/bg_Laura_[lighting]_hard_light.webp" at Transform(blend = "multiply")

    if lighting in ["day"]:
        "characters/Laura/images/bedroom/bg_Laura_[lighting]_screen.webp" at Transform(blend = "screen")

    always:
        "characters/Laura/images/bedroom/bg_Laura_[lighting]_linear_dodge.webp" at Transform(blend = "add")

    always:
        "characters/Laura/images/bedroom/bg_Laura_[lighting]_multiply.webp" at Transform(blend = "multiply")