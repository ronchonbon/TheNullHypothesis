layeredimage bg_Rogue:
    always:
        "characters/Rogue/images/bedroom/bg_Rogue_[lighting].webp"
        
    if "occult_posters" in Rogue.inventory.keys():
        "characters/Rogue/images/bedroom/bg_Rogue_posters_[lighting].webp"
        
    if "baseball_flag" in Rogue.inventory.keys():
        "characters/Rogue/images/bedroom/bg_Rogue_baseball_flag_[lighting].webp"
        
    if "camera" in Rogue.inventory.keys():
        "characters/Rogue/images/bedroom/bg_Rogue_camera_[lighting].webp"
        
    if "plant1" in Rogue.inventory.keys() and "plant2" in Rogue.inventory.keys() and "plant3" in Rogue.inventory.keys():
        "characters/Rogue/images/bedroom/bg_Rogue_plants_[lighting].webp"

    if "mirror" in Rogue.inventory.keys():
        "characters/Rogue/images/bedroom/bg_Rogue_mirror_[lighting].webp"

    if Rogue.messy_bed:
        "characters/Rogue/images/bedroom/bg_Rogue_messy_bed_[lighting].webp"
    else:
        "characters/Rogue/images/bedroom/bg_Rogue_bed_[lighting].webp"
        
    if "acoustic_guitar" in Rogue.inventory.keys():
        "characters/Rogue/images/bedroom/bg_Rogue_guitar_[lighting].webp"

    if Rogue.clothes_on_floor:
        "characters/Rogue/images/bedroom/bg_Rogue_clothes_[lighting].webp"

    if "candle" in Rogue.inventory.keys():
        "characters/Rogue/images/bedroom/bg_Rogue_candles_[lighting].webp"