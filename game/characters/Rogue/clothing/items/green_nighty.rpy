init -1 python:

    def Rogue_green_nighty():
        name = "green nighty"
        short_name = "nighty"
        string = "green_nighty"
        
        Clothing_type = "dress"

        shop_type = "lingerie"
        chapter = 1
        season = 4
        
        thresholds = {
            "accept": [650, 650],
            "wear_in_private": [650, 650],
            "wear_in_public": [675, 675]}
        
        price = 5
        
        shame = [35, 35]
        
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
        
        incompatibilities = [
            "black_fishnet_top"]
        
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

label Rogue_green_nighty_shopping_accept:
    $ Rogue.change_face("pleased1")

    ch_Rogue "A nighty? Ah guess it does look nice."

    return

label Rogue_green_nighty_shopping_reject:
    $ Rogue.change_face("confused1")

    ch_Rogue "Ah'd rather wear my own pajamas, thanks. . ."

    return

label Rogue_green_nighty_gift_accept:
    $ Rogue.change_face("pleased1")

    ch_Rogue "This is really nice, ah wouldn't mind wearin' it in bed."

    return

label Rogue_green_nighty_gift_reject:
    $ Rogue.change_face("worried1")

    ch_Rogue "Ah don't really wanna wear somethin' like that to bed. . ."

    return

label Rogue_green_nighty_change_private_before:

    return

label Rogue_green_nighty_change_private_after:
    $ Rogue.change_face("surprised1", eyes = "down")

    ch_Rogue "Want me to wear this in bed?"

    $ Rogue.eyes = "neutral"

    return

label Rogue_green_nighty_change_public_before:

    return

label Rogue_green_nighty_change_public_after:
    $ Rogue.change_face("pleased1")

    ch_Rogue "Looks real nice, right?"
    ch_Rogue "Also comfy to sleep in. . ."

    return