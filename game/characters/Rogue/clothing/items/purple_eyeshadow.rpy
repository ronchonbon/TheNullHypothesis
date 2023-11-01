init -1 python:

    def Rogue_purple_eyeshadow():
        name = "purple eyeshadow"
        short_name = "eyeshadow"
        string = "purple_eyeshadow"
        
        Clothing_type = "makeup"

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
            "standing": [0],
            "doggy": [0],
            "hands_and_knees": [0],
            "masturbation": [0],
            "missionary": [0]}
        undressed_states = {
            "standing": 0,
            "doggy": 0,
            "hands_and_knees": 0,
            "masturbation": 0,
            "missionary": 0}
        
        covers = {
            "standing": {},
            "doggy": {},
            "hands_and_knees": {},
            "masturbation": {},
            "missionary": {}}
        hides = {
            "standing": {},
            "doggy": {},
            "hands_and_knees": {},
            "masturbation": {},
            "missionary": {}}

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

label Rogue_purple_eyeshadow_shopping_accept:

    return

label Rogue_purple_eyeshadow_shopping_reject:

    return

label Rogue_purple_eyeshadow_gift_accept:

    return

label Rogue_purple_eyeshadow_gift_reject:

    return

label Rogue_purple_eyeshadow_change_private_before:
    ch_Rogue "Eyeshadow? Sure."

    return

label Rogue_purple_eyeshadow_change_private_after:

    return

label Rogue_purple_eyeshadow_change_public_before:
    ch_Rogue "Eyeshadow? Sure."

    return

label Rogue_purple_eyeshadow_change_public_after:

    return