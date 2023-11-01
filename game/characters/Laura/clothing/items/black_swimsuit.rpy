init -1 python:

    def Laura_black_swimsuit():
        name = "black swimsuit"
        short_name = "swimsuit"
        string = "black_swimsuit"

        Clothing_type = "bodysuit"

        shop_type = "clothing"
        chapter = 0
        season = 0

        thresholds = {
            "accept": [0, 0],
            "wear_in_private": [0, 0],
            "wear_in_public": [0, 0]}

        price = 0

        shame = [5, 15]

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
            "black_dress": [0],
            "leather_jacket": [0],
            "striped_shirt": [0],
            "towel": [0],
            "white_sweater": [0],
            "yellow_tanktop": [0]}
        blocked_by = {
            "black_athletic_shorts": [0, 1],
            "black_dress": [0, 1],
            "black_jeans": [0, 1],
            "black_shorts": [0, 1, 2],
            "leather_jacket": [0, 1],
            "leather_pants": [0, 1, 2],
            "striped_shirt": [0, 1],
            "towel": [0, 1],
            "white_sweater": [0, 1],
            "Wolverine_belt": [0],
            "yellow_tanktop": [0, 1]}

        supports_breasts = False

        incompatibilities = []

        return ClothingClass(
            Laura, 
            name, short_name, string, Clothing_type, 
            shop_type, chapter, season,
            thresholds,
            price = int(price*work_unit*min(max(renpy.random.gauss(1.0, 0.15), 0.85), 1.15)), shame = shame, 
            available_states = available_states, undressed_states = undressed_states,
            covers = covers, hides = hides, 
            covered_by = covered_by, blocked_by = blocked_by,
            supports_breasts = supports_breasts,
            incompatibilities = incompatibilities)

label Laura_black_swimsuit_shopping_accept:

    return

label Laura_black_swimsuit_shopping_reject:

    return

label Laura_black_swimsuit_gift_accept:

    return

label Laura_black_swimsuit_gift_reject:

    return

label Laura_black_swimsuit_change_private_before:

    return

label Laura_black_swimsuit_change_private_after:

    return

label Laura_black_swimsuit_change_public_before:

    return

label Laura_black_swimsuit_change_public_after:
    $ Laura.change_face("neutral")

    ch_Laura "Not sure why one-pieces aren't more popular. . ."

    return