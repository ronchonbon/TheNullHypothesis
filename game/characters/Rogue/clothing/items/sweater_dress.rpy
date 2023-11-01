init -1 python:

    def Rogue_sweater_dress():
        name = "sweater dress"
        short_name = "dress"
        string = "sweater_dress"
        
        Clothing_type = "dress"

        shop_type = "clothing"
        chapter = 0
        season = 0
        
        thresholds = {
            "accept": [0, 0],
            "wear_in_private": [0, 0],
            "wear_in_public": [0, 0]}
        
        price = 0
        
        shame = [10, 10]
        
        available_states = {
            "standing": [0, 2]}
        undressed_states = {
            "standing": 2}
        
        covers = {
            "standing": {
                "bra": [0, 2],
                "breasts": [0, 2],
                "back": [0, 2],
                "belly": [0, 2],
                "underwear": [0],
                "ass": [0],
                "pussy": [0],
                "anus": [0]}}
        hides = {
            "standing": {
                "bra": [0, 2],
                "breasts": [0, 2],
                "back": [0, 2],
                "belly": [0, 2],
                "underwear": [0],
                "ass": [0],
                "pussy": [0],
                "anus": [0]}}

        covered_by = {
            "black_fishnet_top": [0, 2],
            "brown_jacket": [0, 2],
            "green_mesh_top": [0, 2],
            "plaid_coat": [0, 2],
            "towel": [0]}
        blocked_by = {
            "black_fishnet_top": [0, 2],
            "brown_jacket": [0, 2],
            "green_mesh_top": [0, 2],
            "plaid_coat": [0, 2],
            "towel": [0]}

        supports_breasts = False
        
        incompatibilities = [
            "black_fishnet_top",
            "black_top",
            "green_mesh_top"]
        
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

label Rogue_sweater_dress_shopping_accept:

    return

label Rogue_sweater_dress_shopping_reject:

    return

label Rogue_sweater_dress_gift_accept:

    return

label Rogue_sweater_dress_gift_reject:

    return

label Rogue_sweater_dress_change_private_before:
    $ Rogue.change_face("smirk2")

    ch_Rogue "Mmm, ah like this one."

    return

label Rogue_sweater_dress_change_private_after:
    ch_Rogue "Nice and warm."

    return

label Rogue_sweater_dress_change_public_before:
    $ Rogue.change_face("smirk2")

    ch_Rogue "Mmm, ah like this one."

    return

label Rogue_sweater_dress_change_public_after:
    ch_Rogue "Nice and warm."

    return