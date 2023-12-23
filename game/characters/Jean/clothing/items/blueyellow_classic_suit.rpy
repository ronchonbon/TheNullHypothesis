init -1 python:

    def Jean_blueyellow_classic_suit():
        name = "blue-and-yellow classic suit"
        short_name = "suit"
        string = "blueyellow_classic_suit"

        Clothing_type = "bodysuit"

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
            "standing": [0, 1]}
        undressed_states = {
            "standing": 1}
        
        covers = {
            "standing": {
                "bra": [0],
                "breasts": [0],
                "back": [0],
                "belly": [0],
                "thighs": [0, 1],
                "underwear": [0, 1],
                "ass": [0, 1],
                "pussy": [0, 1],
                "anus": [0, 1]}}
        hides = {
            "standing": {
                "bra": [0],
                "breasts": [0],
                "back": [0],
                "belly": [0],
                "thighs": [0, 1],
                "underwear": [0, 1],
                "ass": [0, 1],
                "pussy": [0, 1],
                "anus": [0, 1]}}

        covered_by = {
            "blue_gauntlets": [0],
            "pink_top": [0, 1]}
        blocked_by = {
            "blue_athletic_shorts": [0, 1],
            "blue_boots": [0],
            "blue_gauntlets": [0],
            "khaki_pants": [0, 1],
            "pink_top": [0, 1]}

        supports_breasts = False

        incompatibilities = []

        return ClothingClass(
            Jean, 
            name, short_name, string, Clothing_type, 
            shop_type, chapter, season,
            thresholds,
            price = int(price*work_unit*min(max(renpy.random.gauss(1.0, 0.15), 0.85), 1.15)), shame = shame, 
            available_states = available_states, undressed_states = undressed_states,
            covers = covers, hides = hides, 
            covered_by = covered_by, blocked_by = blocked_by,
            supports_breasts = supports_breasts,
            incompatibilities = incompatibilities)

label Jean_blueyellow_classic_suit_shopping_accept:

    return

label Jean_blueyellow_classic_suit_shopping_reject:

    return

label Jean_blueyellow_classic_suit_gift_accept:

    return

label Jean_blueyellow_classic_suit_gift_reject:

    return

label Jean_blueyellow_classic_suit_change_private_before:

    return

label Jean_blueyellow_classic_suit_change_private_after:
    $ Jean.change_face("smirk2")

    ch_Jean "Helped design it myself, awesome right?"

    return

label Jean_blueyellow_classic_suit_change_public_before:

    return

label Jean_blueyellow_classic_suit_change_public_after:
    $ Jean.change_face("smirk2")

    ch_Jean "Helped design it myself, awesome right?"

    return