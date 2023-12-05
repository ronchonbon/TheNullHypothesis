init -1 python:

    def Rogue_green_headband():
        name = "green headband"
        short_name = "headband"
        string = "green_headband"
        
        Clothing_type = "face_inner_accessory"

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

label Rogue_green_headband_shopping_accept:

    return

label Rogue_green_headband_shopping_reject:

    return

label Rogue_green_headband_gift_accept:

    return

label Rogue_green_headband_gift_reject:

    return

label Rogue_green_headband_change_private_before:

    return

label Rogue_green_headband_change_private_after:
    $ Rogue.change_face("smirk2")

    ch_Rogue "Iconic."

    return

label Rogue_green_headband_change_public_before:

    return

label Rogue_green_headband_change_public_after:
    $ Rogue.change_face("smirk2")

    ch_Rogue "Iconic."

    return