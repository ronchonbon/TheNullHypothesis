init -1 python:

    def Rogue_Rogue_suit():
        name = "Rogue suit"
        short_name = "suit"
        string = "Rogue_suit"

        Clothing_type = "bodysuit"

        shop_type = "clothing"
        chapter = 0
        season = 0

        thresholds = {
            "accept": [0, 0],
            "wear_in_private": [0, 0],
            "wear_in_public": [0, 0]}

        price = 0

        shame = [15, 15]
        
        available_states = {
            "standing": [0]}
        undressed_states = {
            "standing": 0}
        
        covers = {
            "standing": {
                "bra": [0],
                "breasts": [0],
                "back": [0],
                "belly": [0],
                "thighs": [0],
                "underwear": [0],
                "ass": [0],
                "pussy": [0],
                "anus": [0]}}
        hides = {
            "standing": {
                "bra": [0],
                "breasts": [0],
                "back": [0],
                "belly": [0],
                "thighs": [0],
                "underwear": [0],
                "ass": [0],
                "pussy": [0],
                "anus": [0]}}

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
            "thighhigh_boots": [0],
            "towel": [0],
            "yellow_boots": [0]}

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

label Rogue_Rogue_suit_shopping_accept:

    return

label Rogue_Rogue_suit_shopping_reject:

    return

label Rogue_Rogue_suit_gift_accept:

    return

label Rogue_Rogue_suit_gift_reject:

    return

label Rogue_Rogue_suit_change_private_before:
    $ Rogue.change_face("smirk2")

    ch_Rogue "Ah love the colors."

    return

label Rogue_Rogue_suit_change_private_after:
    ch_Rogue "A bit form fittin', though. . ."

    return

label Rogue_Rogue_suit_change_public_before:
    $ Rogue.change_face("smirk2")

    ch_Rogue "Ah love the colors."

    return

label Rogue_Rogue_suit_change_public_after:
    ch_Rogue "A bit form fittin', though. . ."

    return