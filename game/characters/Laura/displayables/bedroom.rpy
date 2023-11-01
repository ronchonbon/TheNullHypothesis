layeredimage bg_Laura:
    always:
        "characters/Laura/images/bedroom/bg_Laura_[lighting].webp"
        
    if "horror_novel" in Laura.inventory.keys() and "steamy_romance_novel" in Laura.inventory.keys():
        "characters/Laura/images/bedroom/bg_Laura_books_[lighting].webp"
        
    if "plant1" in Laura.inventory.keys() or "plant2" in Laura.inventory.keys() or "plant3" in Laura.inventory.keys():
        "characters/Laura/images/bedroom/bg_Laura_plants_[lighting].webp"

    if "motorcycle_helmet" in Laura.inventory.keys():
        "characters/Laura/images/bedroom/bg_Laura_helmet_[lighting].webp"

    if "motorcycle_posters" in Laura.inventory.keys():
        "characters/Laura/images/bedroom/bg_Laura_motorcycle_posters_[lighting].webp"

    if "band_posters" in Laura.inventory.keys():
        "characters/Laura/images/bedroom/bg_Laura_band_posters_[lighting].webp"

    if "boxing_kit" in Laura.inventory.keys():
        "characters/Laura/images/bedroom/bg_Laura_boxing_kit_[lighting].webp"

    always:
        "characters/Laura/images/bedroom/bg_Laura_dumbbells_[lighting].webp"

    if "mirror" in Laura.inventory.keys():
        "characters/Laura/images/bedroom/bg_Laura_mirror_[lighting].webp"

    if Laura.messy_bed:
        "characters/Laura/images/bedroom/bg_Laura_messy_bed_[lighting].webp"
    else:
        "characters/Laura/images/bedroom/bg_Laura_bed_[lighting].webp"
        
    if "record_player" in Laura.inventory.keys():
        "characters/Laura/images/bedroom/bg_Laura_record_player_[lighting].webp"

    if Laura.clothes_on_floor:
        "characters/Laura/images/bedroom/bg_Laura_clothes_[lighting].webp"

    if "MMA_gloves" in Laura.inventory.keys():
        "characters/Laura/images/bedroom/bg_Laura_gloves_[lighting].webp"

    zoom background_adjustment