init -1 python:

    def Rogue_black_sports_bra():
        name = "black sports bra"
        short_name = "bra"
        string = "black_sports_bra"
        
        Clothing_type = "bra"

        shop_type = "clothing"
        chapter = 0
        season = 0
        
        thresholds = {
            "accept": [0, 0],
            "wear_in_private": [0, 0],
            "wear_in_public": [0, 0]}
        
        price = 0
        
        shame = [-5, 10]
        
        available_states = {
            "standing": [0, 1]}
        undressed_states = {
            "standing": 1}
        
        covers = {
            "standing": {
                "breasts": [0]}}
        hides = {
            "standing": {
                "breasts": [0]}}

        covered_by = {
            "black_lowcut_top": [0],
            "brown_classic_jacket": [0],
            "greenyellow_classic_suit": [0]}
        blocked_by = {
            "black_lowcut_top": [0],
            "brown_classic_jacket": [0],
            "greenyellow_classic_suit": [0]}

        supports_breasts = True
        
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

label Rogue_black_sports_bra_shopping_accept:

    return

label Rogue_black_sports_bra_shopping_reject:

    return

label Rogue_black_sports_bra_gift_accept:

    return

label Rogue_black_sports_bra_gift_reject:

    return

label Rogue_black_sports_bra_change_private_before:
    ch_Rogue "Ah do like the support. . ."

    return

label Rogue_black_sports_bra_change_private_after:

    return

label Rogue_black_sports_bra_change_public_before:
    ch_Rogue "Ah do like the support. . ."

    return

label Rogue_black_sports_bra_change_public_after:

    return