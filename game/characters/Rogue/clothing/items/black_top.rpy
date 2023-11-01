init -1 python:

    def Rogue_black_top():
        name = "black top"
        short_name = "top"
        string = "black_top"
        
        Clothing_type = "top"

        shop_type = "clothing"
        chapter = 0
        season = 0
        
        thresholds = {
            "accept": [0, 0],
            "wear_in_private": [0, 0],
            "wear_in_public": [0, 0]}
        
        price = 0
        
        shame = [5, 5]
        
        available_states = {
            "standing": [0, 1]}
        undressed_states = {
            "standing": 1}
        
        covers = {
            "standing": {
                "bra": [0],
                "breasts": [0],
                "back": [0],
                "belly": [0]}}
        hides = {
            "standing": {
                "bra": [0],
                "breasts": [0],
                "back": [0],
                "belly": [0]}}

        covered_by = {
            "brown_jacket": [0],
            "NIN_shirt": [0],
            "plaid_coat": [0],
            "towel": [0]}
        blocked_by = {
            "brown_jacket": [0, 1],
            "NIN_shirt": [0, 1],
            "plaid_coat": [0, 1],
            "towel": [0]}

        supports_breasts = False
        
        incompatibilities = [
            "sweater_dress"]
        
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

label Rogue_black_top_shopping_accept:

    return

label Rogue_black_top_shopping_reject:

    return

label Rogue_black_top_gift_accept:

    return

label Rogue_black_top_gift_reject:

    return

label Rogue_black_top_change_private_before:
    $ Rogue.change_face("smirk2")

    ch_Rogue "This one's real nice."

    return

label Rogue_black_top_change_private_after:

    return

label Rogue_black_top_change_public_before:
    $ Rogue.change_face("smirk2")

    ch_Rogue "This one's real nice."

    return

label Rogue_black_top_change_public_after:

    return