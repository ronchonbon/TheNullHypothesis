layeredimage bg_Jean:
    always:
        "characters/Jean/images/bedroom/bg_Jean_[lighting].webp"
        
    if Jean.messy_bed:
        "characters/Jean/images/bedroom/bg_Jean_messy_bed_[lighting].webp"
    else:
        "characters/Jean/images/bedroom/bg_Jean_bed_[lighting].webp"
        
    always:
        "characters/Jean/images/bedroom/bg_Jean_[Jean.whiteboard]_[lighting].webp"
        
    if "mystery_novel" in Jean.inventory.keys() and "wholesome_romance_novel" in Jean.inventory.keys():
        "characters/Jean/images/bedroom/bg_Jean_books_[lighting].webp"
        
    if "plant1" in Jean.inventory.keys() and "plant2" in Jean.inventory.keys() and "plant3" in Jean.inventory.keys():
        "characters/Jean/images/bedroom/bg_Jean_plants_[lighting].webp"

    if Jean.clothes_on_floor:
        "characters/Jean/images/bedroom/bg_Jean_clothes_[lighting].webp"