init -1 python:

    def Rogue_green_lace_bra():
        name = "green lace bra"
        short_name = "bra"
        string = "green_lace_bra"
        
        Clothing_type = "bra"

        shop_type = "lingerie"
        chapter = 1
        season = 1
        
        thresholds = {
            "accept": [200, 200],
            "wear_in_private": [200, 200],
            "wear_in_public": [225, 225]}
        
        price = 5
        
        shame = [5, 1000]
        
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

label Rogue_green_lace_bra_shopping_accept:
    $ Rogue.change_face("pleased2")

    ch_Rogue "You think ah'd look good in somethin' like that?"

    return

label Rogue_green_lace_bra_shopping_reject:
    $ Rogue.change_face("worried1")

    ch_Rogue "Ah'm not really comfortable with you pickin' out bras for me."

    return

label Rogue_green_lace_bra_gift_accept:
    $ Rogue.change_face("sexy")

    ch_Rogue "If yer lucky, ah'll wear it for ya sometime."

    return

label Rogue_green_lace_bra_gift_reject:
    $ Rogue.change_face("surprised2")

    ch_Rogue "Ah think it's a bit too soon for gifts like that. . ."

    return

label Rogue_green_lace_bra_change_private_before:
    $ Rogue.change_face("worried1", eyes = "down")

    ch_Rogue "A bit skimpy. . . but if it's only you. . ."

    $ Rogue.eyes = "neutral"

    return

label Rogue_green_lace_bra_change_private_after:

    return

label Rogue_green_lace_bra_change_public_before:

    return

label Rogue_green_lace_bra_change_public_after:
    $ Rogue.change_face("smirk2")

    ch_Rogue "Ah like how it makes em' look too."

    return