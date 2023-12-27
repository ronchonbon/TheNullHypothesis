layeredimage bg_Rogue:
    if lighting in ["night", "moonlight"]:
        "characters/Rogue/images/bedroom/bg_Rogue_night.webp"
    else:
        "characters/Rogue/images/bedroom/bg_Rogue_day.webp"
        
    if "occult_posters" in Rogue.inventory.keys():
        "characters/Rogue/images/bedroom/bg_Rogue_posters.webp"
        
    if "baseball_flag" in Rogue.inventory.keys():
        "characters/Rogue/images/bedroom/bg_Rogue_baseball_flag.webp"
        
    if "camera" in Rogue.inventory.keys():
        "characters/Rogue/images/bedroom/bg_Rogue_camera.webp"
        
    if "plant1" in Rogue.inventory.keys() and "plant2" in Rogue.inventory.keys() and "plant3" in Rogue.inventory.keys():
        "characters/Rogue/images/bedroom/bg_Rogue_plants.webp"

    if "mirror" in Rogue.inventory.keys():
        "characters/Rogue/images/bedroom/bg_Rogue_mirror.webp"

    if Rogue.messy_bed:
        "characters/Rogue/images/bedroom/bg_Rogue_messy_bed.webp"
    else:
        "characters/Rogue/images/bedroom/bg_Rogue_bed.webp"
        
    if "acoustic_guitar" in Rogue.inventory.keys():
        "characters/Rogue/images/bedroom/bg_Rogue_guitar.webp"

    if Rogue.clothes_on_floor:
        "characters/Rogue/images/bedroom/bg_Rogue_clothes.webp"

    if "candle" in Rogue.inventory.keys():
        "characters/Rogue/images/bedroom/bg_Rogue_candles.webp"

    if lighting in ["candlelit"]:
        "characters/Rogue/images/bedroom/bg_Rogue_moonlight_hard_light.webp" at Transform(blend = "multiply")
    elif lighting == "evening":
        "characters/Rogue/images/bedroom/bg_Rogue_day_hard_light.webp" at Transform(blend = "multiply")
    else:
        "characters/Rogue/images/bedroom/bg_Rogue_[lighting]_hard_light.webp" at Transform(blend = "multiply")

    if lighting in ["day"]:
        "characters/Rogue/images/bedroom/bg_Rogue_[lighting]_screen.webp" at Transform(blend = "screen")

    if lighting in ["candlelit"]:
        "characters/Rogue/images/bedroom/bg_Rogue_moonlight_linear_dodge.webp" at Transform(blend = "add")
    elif lighting == "evening":
        "characters/Rogue/images/bedroom/bg_Rogue_day_linear_dodge.webp" at Transform(blend = "add")
    else:
        "characters/Rogue/images/bedroom/bg_Rogue_[lighting]_linear_dodge.webp" at Transform(blend = "add")

    if lighting in ["candlelit"]:
        "characters/Rogue/images/bedroom/bg_Rogue_moonlight_multiply.webp" at Transform(blend = "multiply")
    elif lighting == "evening":
        "characters/Rogue/images/bedroom/bg_Rogue_day_multiply.webp" at Transform(blend = "multiply")
    else:
        "characters/Rogue/images/bedroom/bg_Rogue_[lighting]_multiply.webp" at Transform(blend = "multiply")

    if lighting in ["night"]:
        "characters/Rogue/images/bedroom/bg_Rogue_light_linear_dodge.webp" at Transform(blend = "add")
    elif lighting in ["candlelit"]:
        "characters/Rogue/images/bedroom/bg_Rogue_candlelight_linear_dodge.webp" at Transform(blend = "add")