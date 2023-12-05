init -1 python:

    def Rogue_yellow_panties():
        name = "yellow panties"
        short_name = "panties"
        string = "yellow_panties"
        
        Clothing_type = "underwear"

        shop_type = "clothing"
        chapter = 0
        season = 0
        
        thresholds = {
            "accept": [0, 0],
            "wear_in_private": [0, 0],
            "wear_in_public": [0, 0]}
        
        price = 0
        
        shame = [-5, 30]
        
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
            "black_jeans": [0],
            "greenyellow_classic_suit": [0]}
        blocked_by = {
            "black_jeans": [0, 1],
            "greenyellow_classic_suit": [0]}

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

label Rogue_yellow_panties_shopping_accept:

    return

label Rogue_yellow_panties_shopping_reject:

    return

label Rogue_yellow_panties_gift_accept:

    return

label Rogue_yellow_panties_gift_reject:

    return

label Rogue_yellow_panties_change_private_before:
    $ Rogue.change_face("smirk2")

    ch_Rogue "Plain, but comfy."

    return

label Rogue_yellow_panties_change_private_after:

    return

label Rogue_yellow_panties_change_public_before:
    $ Rogue.change_face("smirk2")

    ch_Rogue "Plain, but comfy."

    return

label Rogue_yellow_panties_change_public_after:

    return