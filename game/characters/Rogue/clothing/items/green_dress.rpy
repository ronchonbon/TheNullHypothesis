init -1 python:

    def Rogue_green_dress():
        name = "green dress"
        short_name = "dress"
        string = "green_dress"
        
        Clothing_type = "dress"

        shop_type = "clothing"
        chapter = 1
        season = 3
        
        thresholds = {
            "accept": [650, 650],
            "wear_in_private": [650, 650],
            "wear_in_public": [675, 675]}
        
        price = 7
        
        shame = [25, 25]
        
        available_states = {
            "standing": [0, 1]}
        undressed_states = {
            "standing": 1}
        
        covers = {
            "standing": {
                "bra": [0],
                "breasts": [0],
                "back": [0, 1],
                "belly": [0, 1],
                "thighs": [0, 1],
                "underwear": [0, 1],
                "ass": [0, 1],
                "pussy": [0, 1],
                "anus": [0, 1]}}
        hides = {
            "standing": {
                "bra": [0],
                "breasts": [0],
                "back": [0, 1],
                "belly": [0, 1],
                "thighs": [0, 1],
                "underwear": [0, 1],
                "ass": [0, 1],
                "pussy": [0, 1],
                "anus": [0, 1]}}

        covered_by = {
            "black_fishnet_top": [0, 1],
            "brown_jacket": [0],
            "green_mesh_top": [0, 1],
            "plaid_coat": [0],
            "towel": [0]}
        blocked_by = {
            "black_fishnet_top": [0, 1],
            "brown_jacket": [0],
            "green_mesh_top": [0, 1],
            "plaid_coat": [0],
            "towel": [0]}

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

label Rogue_green_dress_shopping_accept:
    $ Rogue.change_face("pleased1")

    ch_Rogue "Good taste, hon'. Ah was really needin' a dress."

    return

label Rogue_green_dress_shopping_reject:
    $ Rogue.change_face("confused1")

    ch_Rogue "A dress? What do ah need that for?"

    return

label Rogue_green_dress_gift_accept:
    $ Rogue.change_face("pleased2")

    ch_Rogue "Ya got me a dress?"

    $ Rogue.change_face("smirk2")

    ch_Rogue "Ah'd look great in that, thanks hon'."

    return

label Rogue_green_dress_gift_reject:
    $ Rogue.change_face("confused1")

    ch_Rogue "Ah don't think you should be buyin' dresses for me. . ."

    return

label Rogue_green_dress_change_private_before:

    return

label Rogue_green_dress_change_private_after:
    $ Rogue.change_face("pleased1", eyes = "down")

    ch_Rogue "This dress is so nice."

    $ Rogue.eyes = "neutral"

    return

label Rogue_green_dress_change_public_before:

    return

label Rogue_green_dress_change_public_after:
    $ Rogue.change_face("pleased1")

    ch_Rogue "Ah do love feelin' fancy."

    return