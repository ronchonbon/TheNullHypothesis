init -1 python:

    def Rogue_black_gloves():
        name = "black gloves"
        short_name = "gloves"
        string = "black_gloves"
        
        Clothing_type = "gloves"

        shop_type = "clothing"
        chapter = 0
        season = 0
        
        thresholds = {
            "accept": [0, 0],
            "wear_in_private": [0, 0],
            "wear_in_public": [0, 0]}
        
        price = 0
        
        shame = [-2, -2]
        
        available_states = {
            "standing": [0]}
        undressed_states = {
            "standing": 0}
        
        covers = {
            "standing": {}}
        hides = {
            "standing": {}}

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

label Rogue_black_gloves_shopping_accept:

    return

label Rogue_black_gloves_shopping_reject:

    return

label Rogue_black_gloves_gift_accept:

    return

label Rogue_black_gloves_gift_reject:

    return

label Rogue_black_gloves_change_private_before:

    return

label Rogue_black_gloves_change_private_after:
    $ Rogue.change_face("worried1")

    ch_Rogue "Sometimes ah wish ah didn't need 'em."

    return

label Rogue_black_gloves_change_public_before:

    return

label Rogue_black_gloves_change_public_after:
    $ Rogue.change_face("worried1")

    ch_Rogue "Sometimes ah wish ah didn't need 'em."

    return