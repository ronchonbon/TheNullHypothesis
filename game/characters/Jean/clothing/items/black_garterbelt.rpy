init -1 python:

    def Jean_black_garterbelt():
        name = "black garterbelt"
        short_name = "garterbelt"
        string = "black_garterbelt"
        
        Clothing_type = "hose"

        shop_type = "lingerie"
        chapter = 1
        season = 3

        thresholds = {
            "accept": [250, 200],
            "wear_in_private": [250, 200],
            "wear_in_public": [275, 225]}
        
        price = 2
        
        shame = [5, 5]

        available_states = {
            "standing": [0],
            "doggy": [0],
            "hands_and_knees": [0],
            "masturbation": [0],
            "missionary": [0]}
        undressed_states = {
            "standing": 0,
            "doggy": 0,
            "hands_and_knees": 0,
            "masturbation": 0,
            "missionary": 0}
        
        covers = {
            "standing": {},
            "doggy": {},
            "hands_and_knees": {},
            "masturbation": {},
            "missionary": {}}
        hides = {
            "standing": {},
            "doggy": {},
            "hands_and_knees": {},
            "masturbation": {},
            "missionary": {}}

        covered_by = {
            "black_pants": [0, 1],
            "blue_athletic_shorts": [0, 1],
            "Jean_suit": [0, 1],
            "khaki_pants": [0, 1]}
        blocked_by = {
            "black_pants": [0, 1, 2],
            "blue_athletic_shorts": [0, 1],
            "Jean_suit": [0, 1],
            "khaki_pants": [0, 1, 2]}

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

label Jean_black_garterbelt_shopping_accept:
    $ Jean.change_face("smirk2")

    ch_Jean "I like the blue. . ."

    return

label Jean_black_garterbelt_shopping_reject:
    $ Jean.change_face("surprised2")

    ch_Jean "I don't think you should be buying me lingerie. . ."

    return

label Jean_black_garterbelt_gift_accept:
    $ Jean.change_face("smirk2")

    ch_Jean "The blue is gonna make me look so good. . ."

    return

label Jean_black_garterbelt_gift_reject:
    $ Jean.change_face("angry1")

    ch_Jean "Really?"
    ch_Jean "Buying me lingerie?"

    return

label Jean_black_garterbelt_change_private_before:

    return

label Jean_black_garterbelt_change_private_after:
    $ Jean.change_face("smirk2", eyes = "down")

    ch_Jean "Not a bad choice."

    $ Jean.eyes = "neutral"

    return

label Jean_black_garterbelt_change_public_before:

    return

label Jean_black_garterbelt_change_public_after:
    $ Jean.change_face("smirk2")

    ch_Jean "I bet you love seeing me in lingerie"

    return