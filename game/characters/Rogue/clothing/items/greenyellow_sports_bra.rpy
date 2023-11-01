init -1 python:

    def Rogue_greenyellow_sports_bra():
        name = "green-and-yellow sports bra"
        short_name = "bra"
        string = "greenyellow_sports_bra"
        
        Clothing_type = "bra"

        shop_type = "clothing"
        chapter = 0
        season = 0
        
        thresholds = {
            "accept": [0, 0],
            "wear_in_private": [0, 0],
            "wear_in_public": [0, 0]}
        
        price = 0
        
        shame = [-5, 10]
        
        available_states = {
            "standing": [0, 1],
            "doggy": [0, 1],
            "hands_and_knees": [0, 1],
            "masturbation": [0, 1],
            "missionary": [0, 1]}
        undressed_states = {
            "standing": 1,
            "doggy": 1,
            "hands_and_knees": 1,
            "masturbation": 1,
            "missionary": 1}
        
        covers = {
            "standing": {
                "breasts": [0]},
            "doggy": {
                "breasts": [0]},
            "hands_and_knees": {
                "breasts": [0]},
            "masturbation": {
                "breasts": [0]},
            "missionary": {
                "breasts": [0]}}
        hides = {
            "standing": {
                "breasts": [0]},
            "doggy": {
                "breasts": [0]},
            "hands_and_knees": {
                "breasts": [0]},
            "masturbation": {
                "breasts": [0]},
            "missionary": {
                "breasts": [0]}}

        covered_by = {
            "black_fishnet_top": [0],
            "black_top": [0],
            "brown_jacket": [0],
            "green_dress": [0],
            "green_mesh_top": [0],
            "green_nighty": [0],
            "NIN_shirt": [0],
            "pink_swimsuit": [0],
            "plaid_coat": [0],
            "Rogue_suit": [0],
            "sweater_dress": [0, 2],
            "towel": [0]}
        blocked_by = {
            "black_fishnet_top": [0, 1],
            "black_top": [0, 1],
            "brown_jacket": [0, 1],
            "green_dress": [0],
            "green_mesh_top": [0, 1],
            "green_nighty": [0],
            "NIN_shirt": [0, 1],
            "pink_swimsuit": [0, 1],
            "plaid_coat": [0, 1],
            "Rogue_suit": [0],
            "sweater_dress": [0, 2],
            "towel": [0]}

        supports_breasts = True
        
        incompatibilities = [
            "pink_swimsuit"]
        
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

label Rogue_greenyellow_sports_bra_shopping_accept:

    return

label Rogue_greenyellow_sports_bra_shopping_reject:

    return

label Rogue_greenyellow_sports_bra_gift_accept:

    return

label Rogue_greenyellow_sports_bra_gift_reject:

    return

label Rogue_greenyellow_sports_bra_change_private_before:
    ch_Rogue "Ah do like the support. . ."

    return

label Rogue_greenyellow_sports_bra_change_private_after:

    return

label Rogue_greenyellow_sports_bra_change_public_before:
    ch_Rogue "Ah do like the support. . ."

    return

label Rogue_greenyellow_sports_bra_change_public_after:

    return