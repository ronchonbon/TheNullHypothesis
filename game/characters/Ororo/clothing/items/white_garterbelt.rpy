init -1 python:

    def Ororo_white_garterbelt():
        name = "white garterbelt"
        short_name = "garterbelt"
        string = "white_garterbelt"
        
        Clothing_type = "hose"

        shop_type = "lingerie"
        chapter = 0
        season = 0
        
        thresholds = {
            "accept": [0, 0],
            "wear_in_private": [0, 0],
            "wear_in_public": [0, 0]}
        
        price = 40
        
        shame = [0, 0]
        
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
            Ororo, 
            name, short_name, string, Clothing_type, 
            shop_type, chapter, season,
            thresholds,
            price = int(price*work_unit*min(max(renpy.random.gauss(1.0, 0.15), 0.85), 1.15)), shame = shame, 
            available_states = available_states, undressed_states = undressed_states,
            covers = covers, hides = hides, 
            covered_by = covered_by, blocked_by = blocked_by,
            supports_breasts = supports_breasts,
            incompatibilities = incompatibilities)

label Ororo_white_garterbelt_shopping_accept:

    return

label Ororo_white_garterbelt_shopping_reject:

    return

label Ororo_white_garterbelt_gift_accept:

    return

label Ororo_white_garterbelt_gift_reject:

    return

label Ororo_white_garterbelt_change_private_before:

    return

label Ororo_white_garterbelt_change_private_after:

    return

label Ororo_white_garterbelt_change_public_before:

    return

label Ororo_white_garterbelt_change_public_after:

    return