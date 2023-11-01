init -1 python:

    def Rogue_green_bikini_top():
        name = "green bikini top"
        short_name = "bikini top"
        string = "green_bikini_top"
        
        Clothing_type = "bra"

        shop_type = "clothing"
        chapter = 1
        season = 2
        
        thresholds = {
            "accept": [250, 250],
            "wear_in_private": [250, 250],
            "wear_in_public": [275, 275]}
        
        price = 3
        
        shame = [5, 15]
        
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

label Rogue_green_bikini_top_shopping_accept:
    $ Rogue.change_face("pleased2")

    ch_Rogue "Ah do like the green. . ."

    return

label Rogue_green_bikini_top_shopping_reject:
    $ Rogue.change_face("worried1")

    ch_Rogue "Ah'm not really comfortable with you pickin' out bikinis for me. . ."

    return

label Rogue_green_bikini_top_gift_accept:
    $ Rogue.change_face("worried1")

    pause 1.0

    $ Rogue.change_face("smirk2")

    ch_Rogue "It is nice. . ."

    return

label Rogue_green_bikini_top_gift_reject:
    $ Rogue.change_face("surprised2")

    pause 1.0

    $ Rogue.change_face("confused1")

    ch_Rogue "Why would you try giftin' me a bikini. . ."

    return

label Rogue_green_bikini_top_change_private_before:

    return

label Rogue_green_bikini_top_change_private_after:
    $ Rogue.change_face("worried1", eyes = "down")

    ch_Rogue "A bit skimpy. . . but ah like the green."

    $ Rogue.eyes = "neutral"

    return

label Rogue_green_bikini_top_change_public_before:

    return

label Rogue_green_bikini_top_change_public_after:
    $ Rogue.change_face("smirk2")

    ch_Rogue "Ya like the look?"

    return