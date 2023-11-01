init -1 python:

    def Jean_towel():
        name = "towel"
        short_name = "towel"
        string = "towel"

        Clothing_type = "towel"

        shop_type = "clothing"
        chapter = 0
        season = 0

        thresholds = {
            "accept": [0, 0],
            "wear_in_private": [0, 0],
            "wear_in_public": [0, 0]}

        price = 0

        shame = [20, 20]

        available_states = {
            "standing": [0, 1],
            "doggy": [0],
            "hands_and_knees": [0],
            "masturbation": [0, 1],
            "missionary": [0, 1]}
        undressed_states = {
            "standing": 1,
            "doggy": 0,
            "hands_and_knees": 0,
            "masturbation": 1,
            "missionary": 1}
        
        covers = {
            "standing": {
                "bra": [0],
                "breasts": [0],
                "back": [0, 1],
                "belly": [0],
                "underwear": [0],
                "ass": [0],
                "pussy": [0],
                "anus": [0]},
            "doggy": {
                "bra": [0],
                "breasts": [0],
                "back": [0],
                "belly": [0]},
            "hands_and_knees": {
                "bra": [0],
                "breasts": [0],
                "back": [0],
                "belly": [0],
                "underwear": [0],
                "ass": [0],
                "pussy": [0],
                "anus": [0]},
            "masturbation": {
                "bra": [0],
                "breasts": [0],
                "back": [0, 1],
                "belly": [0, 1]},
            "missionary": {
                "bra": [0],
                "breasts": [0],
                "back": [0, 1],
                "belly": [0, 1]}}
        hides = {
            "standing": {
                "bra": [0],
                "breasts": [0],
                "back": [0, 1],
                "belly": [0],
                "underwear": [0],
                "ass": [0],
                "pussy": [0],
                "anus": [0]},
            "doggy": {
                "bra": [0],
                "breasts": [0],
                "back": [0],
                "belly": [0]},
            "hands_and_knees": {
                "bra": [0],
                "breasts": [0],
                "back": [0],
                "belly": [0],
                "underwear": [0],
                "ass": [0],
                "pussy": [0],
                "anus": [0]},
            "masturbation": {
                "bra": [0],
                "breasts": [0],
                "back": [0, 1],
                "belly": [0, 1]},
            "missionary": {
                "bra": [0],
                "breasts": [0],
                "back": [0, 1],
                "belly": [0, 1]}}

        covered_by = {}
        blocked_by = {}

        supports_breasts = True

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

label Jean_towel_shopping_accept:

    return

label Jean_towel_shopping_reject:

    return

label Jean_towel_gift_accept:

    return

label Jean_towel_gift_reject:

    return

label Jean_towel_change_private_before:
    $ Jean.change_face("confused1")

    ch_Jean "Uh, sure?"

    return

label Jean_towel_change_private_after:

    return

label Jean_towel_change_public_before:
    $ Jean.change_face("confused1")

    ch_Jean "Uh, sure?"

    return

label Jean_towel_change_public_after:

    return