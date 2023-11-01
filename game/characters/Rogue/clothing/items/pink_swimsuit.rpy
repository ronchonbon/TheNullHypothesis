init -1 python:

    def Rogue_pink_swimsuit():
        name = "pink swimsuit"
        short_name = "swimsuit"
        string = "pink_swimsuit"

        Clothing_type = "bodysuit"

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
            "standing": [0, 1],
            "doggy": [0, 2],
            "hands_and_knees": [0, 1],
            "masturbation": [0, 1, 2, 3],
            "missionary": [0, 1, 2, 3]}
        undressed_states = {
            "standing": 1,
            "doggy": 2,
            "hands_and_knees": 1,
            "masturbation": 1,
            "missionary": 1}
        
        covers = {
            "standing": {
                "bra": [0],
                "breasts": [0],
                "back": [0, 1],
                "belly": [0, 1],
                "underwear": [0, 1],
                "pussy": [0, 1],
                "anus": [0, 1]},
            "doggy": {
                "bra": [0, 2],
                "breasts": [0, 2],
                "back": [0, 2],
                "belly": [0, 2],
                "underwear": [0],
                "pussy": [0],
                "anus": [0]},
            "hands_and_knees": {
                "bra": [0],
                "breasts": [0],
                "back": [0, 1],
                "belly": [0, 1],
                "underwear": [0, 1],
                "pussy": [0, 1],
                "anus": [0, 1]},
            "masturbation": {
                "bra": [0, 2],
                "breasts": [0, 2],
                "back": [0, 1, 2, 3],
                "belly": [0, 1, 2, 3],
                "underwear": [0, 1],
                "pussy": [0, 1],
                "anus": [0, 1]},
            "missionary": {
                "bra": [0, 2],
                "breasts": [0, 2],
                "back": [0, 1, 2, 3],
                "belly": [0, 1, 2, 3],
                "underwear": [0, 1],
                "pussy": [0, 1],
                "anus": [0, 1]}}
        hides = {
            "standing": {
                "bra": [0],
                "breasts": [0],
                "back": [0, 1],
                "belly": [0, 1],
                "underwear": [0, 1],
                "pussy": [0, 1],
                "anus": [0, 1]},
            "doggy": {
                "bra": [0, 2],
                "breasts": [0, 2],
                "back": [0, 2],
                "belly": [0, 2],
                "underwear": [0],
                "pussy": [0],
                "anus": [0]},
            "hands_and_knees": {
                "bra": [0],
                "breasts": [0],
                "back": [0, 1],
                "belly": [0, 1],
                "underwear": [0, 1],
                "pussy": [0, 1],
                "anus": [0, 1]},
            "masturbation": {
                "bra": [0, 2],
                "breasts": [0, 2],
                "back": [0, 1, 2, 3],
                "belly": [0, 1, 2, 3],
                "underwear": [0, 1],
                "pussy": [0, 1],
                "anus": [0, 1]},
            "missionary": {
                "bra": [0, 2],
                "breasts": [0, 2],
                "back": [0, 1, 2, 3],
                "belly": [0, 1, 2, 3],
                "underwear": [0, 1],
                "pussy": [0, 1],
                "anus": [0, 1]}}

        covered_by = {
            "black_fishnet_top": [0],
            "black_top": [0],
            "brown_jacket": [0],
            "green_dress": [0],
            "green_mesh_top": [0],
            "green_nighty": [0],
            "NIN_shirt": [0],
            "plaid_coat": [0],
            "towel": [0]}
        blocked_by = {
            "black_fishnet_top": [0, 1],
            "black_shorts": [0, 1, 2],
            "black_jeans": [0, 1, 2],
            "black_top": [0, 1],
            "brown_jacket": [0, 1],
            "green_dress": [0, 1],
            "green_mesh_top": [0, 1],
            "green_nighty": [0, 1],
            "NIN_shirt": [0, 1],
            "plaid_coat": [0, 1],
            "towel": [0]}

        supports_breasts = False

        incompatibilities = [
            "black_bra",
            "black_lace_bra",
            "black_tanktop",
            "green_bikini_top",
            "greenyellow_sports_bra"]

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

label Rogue_pink_swimsuit_shopping_accept:

    return

label Rogue_pink_swimsuit_shopping_reject:

    return

label Rogue_pink_swimsuit_gift_accept:

    return

label Rogue_pink_swimsuit_gift_reject:

    return

label Rogue_pink_swimsuit_change_private_before:

    return

label Rogue_pink_swimsuit_change_private_after:
    $ Rogue.change_face("worried1", mouth = "smirk")

    ch_Rogue "Ah like the sleeves. . ."

    return

label Rogue_pink_swimsuit_change_public_before:

    return

label Rogue_pink_swimsuit_change_public_after:
    $ Rogue.change_face("worried1", mouth = "smirk")

    ch_Rogue "Ah like the sleeves. . ."

    return