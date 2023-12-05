init -1 python:

    def Rogue_black_cage_bra():
        name = "black cage bra"
        short_name = "bra"
        string = "black_cage_bra"
        
        Clothing_type = "bra"

        shop_type = "lingerie"
        chapter = 1
        season = 4
        
        thresholds = {
            "accept": [450, 450],
            "wear_in_private": [450, 450],
            "wear_in_public": [475, 475]}
        
        price = 6
        
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

label Rogue_black_cage_bra_shopping_accept:
    $ Rogue.change_face("pleased2")

    ch_Rogue "You think ah could pull this off?"

    return

label Rogue_black_cage_bra_shopping_reject:
    $ Rogue.change_face("worried1")

    ch_Rogue "Ah'm not interested in your bra preferences."

    return

label Rogue_black_cage_bra_gift_accept:
    $ Rogue.change_face("sexy")

    ch_Rogue "Ah could wear this for you. . ."

    return

label Rogue_black_cage_bra_gift_reject:
    $ Rogue.change_face("surprised2")

    ch_Rogue "Ah'd rather you not buy me bras. . ."

    return

label Rogue_black_cage_bra_change_private_before:
    $ Rogue.change_face("worried1", eyes = "down")

    ch_Rogue "This one's pretty sexy. . . but if it's only you. . ."

    $ Rogue.eyes = "neutral"

    return

label Rogue_black_cage_bra_change_private_after:

    return

label Rogue_black_cage_bra_change_public_before:

    return

label Rogue_black_cage_bra_change_public_after:
    $ Rogue.change_face("smirk2")

    ch_Rogue "Ah love this bra. . ."

    return