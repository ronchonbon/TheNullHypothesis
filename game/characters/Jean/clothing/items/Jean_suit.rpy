init -1 python:

    def Jean_Jean_suit():
        name = "Jean suit"
        short_name = "suit"
        string = "Jean_suit"

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
            "black_shirt": [0],
            "black_trenchcoat": [0],
            "blue_nighty": [0],
            "college_shirt": [0],
            "denim_jacket": [0],
            "pink_shirt": [0],
            "puffy_jacket": [0],
            "towel": [0],
            "white_cami": [0],
            "white_sweater": [0],
            "yellow_dress": [0]}
        blocked_by = {
            "black_pants": [0, 1, 2],
            "black_shirt": [0, 1],
            "black_trenchcoat": [0, 1],
            "blue_athletic_shorts": [0, 1],
            "blue_boots": [0],
            "blue_gauntlets": [0],
            "blue_nighty": [0, 1],
            "blue_pleated_skirt": [0, 1],
            "college_shirt": [0, 1],
            "denim_jacket": [0, 1],
            "khaki_pants": [0, 1, 2],
            "pink_shirt": [0, 1],
            "puffy_jacket": [0, 1],
            "towel": [0, 1],
            "white_cami": [0, 1],
            "white_sweater": [0, 1],
            "yellow_dress": [0, 1]}

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

label Jean_Jean_suit_shopping_accept:

    return

label Jean_Jean_suit_shopping_reject:

    return

label Jean_Jean_suit_gift_accept:

    return

label Jean_Jean_suit_gift_reject:

    return

label Jean_Jean_suit_change_private_before:

    return

label Jean_Jean_suit_change_private_after:
    $ Jean.change_face("smirk2")

    ch_Jean "Helped design it myself, awesome right?"

    return

label Jean_Jean_suit_change_public_before:

    return

label Jean_Jean_suit_change_public_after:
    $ Jean.change_face("smirk2")

    ch_Jean "Helped design it myself, awesome right?"

    return