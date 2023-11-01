init -1 python:

    def Rogue_black_shorts():
        name = "black shorts"
        short_name = "shorts"
        string = "black_shorts"

        Clothing_type = "pants"

        shop_type = "clothing"
        chapter = 0
        season = 0

        thresholds = {
            "accept": [0, 0],
            "wear_in_private": [0, 0],
            "wear_in_public": [0, 0]}

        price = 0

        shame = [-5, -5]
        
        available_states = {
            "standing": [0, 1, 2]}
        undressed_states = {
            "standing": 2}
        
        covers = {
            "standing": {
                "underwear": [0, 1],
                "ass": [0, 1],
                "pussy": [0, 1],
                "anus": [0, 1]}}
        hides = {
            "standing": {
                "underwear": [0],
                "ass": [0, 1],
                "pussy": [0, 1],
                "anus": [0, 1]}}

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

label Rogue_black_shorts_shopping_accept:

    return

label Rogue_black_shorts_shopping_reject:

    return

label Rogue_black_shorts_gift_accept:

    return

label Rogue_black_shorts_gift_reject:

    return

label Rogue_black_shorts_change_private_before:

    return

label Rogue_black_shorts_change_private_after:
    $ Rogue.change_face("worried1")

    ch_Rogue "They're gettin' a bit tight. . ."

    return

label Rogue_black_shorts_change_public_before:

    return

label Rogue_black_shorts_change_public_after:
    $ Rogue.change_face("worried1")

    ch_Rogue "They're gettin' a bit tight. . ."

    return