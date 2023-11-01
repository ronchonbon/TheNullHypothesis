init -1 python:

    def Rogue_NIN_shirt():
        name = "NIN shirt"
        short_name = "shirt"
        string = "NIN_shirt"
        
        Clothing_type = "jacket"

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
                "back": [0]}}
        hides = {
            "standing": {
                "bra": [0],
                "breasts": [0],
                "back": [0]}}

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

label Rogue_NIN_shirt_shopping_accept:

    return

label Rogue_NIN_shirt_shopping_reject:

    return

label Rogue_NIN_shirt_gift_accept:

    return

label Rogue_NIN_shirt_gift_reject:

    return

label Rogue_NIN_shirt_change_private_before:

    return

label Rogue_NIN_shirt_change_private_after:
    ch_Rogue "Ah'm a big Reznor fan."

    return

label Rogue_NIN_shirt_change_public_before:

    return

label Rogue_NIN_shirt_change_public_after:
    ch_Rogue "Ah'm a big Reznor fan."

    return