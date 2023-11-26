init -1 python:

    def Rogue_green_lace_panties():
        name = "green lace panties"
        short_name = "panties"
        string = "green_lace_panties"
        
        Clothing_type = "underwear"

        shop_type = "lingerie"
        chapter = 1
        season = 1
        
        thresholds = {
            "accept": [225, 225],
            "wear_in_private": [225, 225],
            "wear_in_public": [250, 250]}
        
        price = 5
        
        shame = [-2, 1000]
        
        available_states = {
            "standing": [0, 1]}
        undressed_states = {
            "standing": 1}
        
        covers = {
            "standing": {
                "pussy": [0],
                "anus": [0]}}
        hides = {
            "standing": {
                "pussy": [0],
                "anus": [0]}}

        covered_by = {
            "black_jeans": [0]}
        blocked_by = {
            "black_jeans": [0, 1]}

        supports_breasts = False
        
        incompatibilities = []
        
        return ClothingClass(
            Rogue, 
            name, short_name, string, Clothing_type, 
            shop_type, chapter, season,
            thresholds,
            price = int(price*work_unit*min(max(renpy.random.gauss(1.0, 0.15), 0.85), 1.15)), shame = shame, 
            available_states = available_states, undressed_states = undressed_states,
            covers = covers, hides = hides, 
            covered_by = covered_by, blocked_by = blocked_by,
            supports_breasts = supports_breasts,
            incompatibilities = incompatibilities)

label Rogue_green_lace_panties_shopping_accept:
    $ Rogue.change_face("surprised2")

    pause 1.0

    $ Rogue.change_face("smirk2")

    ch_Rogue "Ah've never had lacy panties before."

    return

label Rogue_green_lace_panties_shopping_reject:
    $ Rogue.change_face("perplexed")

    ch_Rogue "Ah can pick out mah own underwear, thanks."

    return

label Rogue_green_lace_panties_gift_accept:
    $ Rogue.change_face("smirk2")

    ch_Rogue "Ah'll look good in those."

    return

label Rogue_green_lace_panties_gift_reject:
    $ Rogue.change_face("worried1")

    ch_Rogue "Ah don't think that's appropriate. . ."

    return

label Rogue_green_lace_panties_change_private_before:

    return

label Rogue_green_lace_panties_change_private_after:
    $ Rogue.change_face("smirk2", eyes = "down")

    ch_Rogue "Don't mind wearin' these for you."

    $ Rogue.eyes = "neutral"

    return

label Rogue_green_lace_panties_change_public_before:

    return

label Rogue_green_lace_panties_change_public_after:
    $ Rogue.change_face("smirk2")

    ch_Rogue "Ah do look good in 'em."

    return