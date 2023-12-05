init -1 python:

    def Rogue_yellow_classic_boots():
        name = "yellow classic boots"
        short_name = "boots"
        string = "yellow_classic_boots"
        
        Clothing_type = "footwear"

        shop_type = "clothing"
        chapter = 0
        season = 0
        
        thresholds = {
            "accept": [0, 0],
            "wear_in_private": [0, 0],
            "wear_in_public": [0, 0]}

        price = 0

        shame = [0, 0]
        
        available_states = {
            "standing": [0]}
        undressed_states = {
            "standing": 0}
        
        covers = {
            "standing": {
                "feet": [0]}}
        hides = {
            "standing": {
                "feet": [0]}}

        covered_by = {}
        blocked_by = {}

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

label Rogue_yellow_classic_boots_shopping_accept:

    return

label Rogue_yellow_classic_boots_shopping_reject:

    return

label Rogue_yellow_classic_boots_gift_accept:

    return

label Rogue_yellow_classic_boots_gift_reject:

    return

label Rogue_yellow_classic_boots_change_private_before:

    return

label Rogue_yellow_classic_boots_change_private_after:
    $ Rogue.change_face("smirk2")

    ch_Rogue "Ah like 'em."

    return

label Rogue_yellow_classic_boots_change_public_before:

    return

label Rogue_yellow_classic_boots_change_public_after:
    $ Rogue.change_face("smirk2")

    ch_Rogue "Ah like 'em."

    return