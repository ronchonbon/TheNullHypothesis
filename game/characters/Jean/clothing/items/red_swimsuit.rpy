init -1 python:

    def Jean_red_swimsuit():
        name = "red swimsuit"
        short_name = "swimsuit"
        string = "red_swimsuit"

        Clothing_type = "bodysuit"

        shop_type = "clothing"
        chapter = 0
        season = 0

        thresholds = {
            "accept": [0, 0],
            "wear_in_private": [0, 0],
            "wear_in_public": [0, 0]}

        price = 0

        shame = [5, 20]

        available_states = {
            "standing": [0, 1, 2, 3]}
        undressed_states = {
            "standing": 1}
        
        covers = {
            "standing": {
                "bra": [0, 2],
                "breasts": [0, 2],
                "back": [0, 1, 2, 3],
                "belly": [0, 1, 2, 3],
                "underwear": [0, 1],
                "pussy": [0, 1],
                "anus": [0, 1]}}
        hides = {
            "standing": {
                "breasts": [0, 2],
                "back": [0, 1, 2, 3],
                "belly": [0, 1, 2, 3],
                "pussy": [0, 1],
                "anus": [0, 1]}}

        covered_by = {
            "pink_top": [0, 1]}
        blocked_by = {
            "blue_athletic_shorts": [0, 1],
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

label Jean_red_swimsuit_shopping_accept:
    $ Jean.change_face("pleased2")

    ch_Jean "It's a bit revealing. . ."

    $ Jean.blush = 1

    ch_Jean "But god, I'd look so hot in that."

    return

label Jean_red_swimsuit_shopping_reject:
    $ Jean.change_face("surprised2")

    pause 1.0

    $ Jean.change_face("confused2")

    ch_Jean "Definitely not enough coverage around the. . ."

    $ Jean.blush = 1

    return

label Jean_red_swimsuit_gift_accept:
    $ Jean.change_face("surprised2")

    ch_Jean "Damn. . ."

    $ Jean.change_face("sly")

    ch_Jean "I bet you're dying to see me in this. . ."

    return

label Jean_red_swimsuit_gift_reject:
    $ Jean.change_face("confused2")

    ch_Jean "The hell. . ."
    ch_Jean "Why would you buy me a swimsuit?"

    return

label Jean_red_swimsuit_change_private_before:

    return

label Jean_red_swimsuit_change_private_after:
    $ Jean.change_face("smirk2", eyes = "down")

    ch_Jean "It's not too skimpy. . ."

    $ Jean.eyes = "neutral"

    ch_Jean "Right?"

    return

label Jean_red_swimsuit_change_public_before:
    $ Jean.change_face("smirk2")

    ch_Jean "I know you love this one."
    ch_Jean "Perv."

    $ Jean.change_face("sly")

    return

label Jean_red_swimsuit_change_public_after:

    return