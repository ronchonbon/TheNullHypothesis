init -1 python:

    def Jean_black_stockings():
        name = "black stockings"
        short_name = "stockings"
        string = "black_stockings"
        
        Clothing_type = "socks"

        shop_type = "lingerie"
        chapter = 1
        season = 3
        
        thresholds = {
            "accept": [250, 225],
            "wear_in_private": [250, 225],
            "wear_in_public": [275, 250]}
        
        price = 4
        
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
            "standing": {
                "feet": [0]},
            "doggy": {
                "feet": [0]},
            "hands_and_knees": {
                "feet": [0]},
            "masturbation": {
                "feet": [0]},
            "missionary": {
                "feet": [0]}}
        hides = {
            "standing": {},
            "doggy": {},
            "hands_and_knees": {},
            "masturbation": {},
            "missionary": {}}

        covered_by = {
            "black_pants": [0, 1],
            "blue_boots": [0],
            "Jean_suit": [0, 1],
            "khaki_pants": [0, 1]}
        blocked_by = {
            "black_pants": [0, 1],
            "blue_boots": [0],
            "Jean_suit": [0, 1],
            "khaki_pants": [0, 1]}

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

label Jean_black_stockings_shopping_accept:
    $ Jean.change_face("smirk2")

    ch_Jean "Like my legs, huh?"

    return

label Jean_black_stockings_shopping_reject:
    $ Jean.change_face("surprised2")

    ch_Jean "Uhm. . . I'm not cool with you buying me stuff like this."

    return

label Jean_black_stockings_gift_accept:
    $ Jean.change_face("sexy")

    ch_Jean "You just know I'll look fantastic with these on."

    return

label Jean_black_stockings_gift_reject:
    $ Jean.change_face("angry1")

    ch_Jean "You shouldn't be buying me these kinds of things."

    return

label Jean_black_stockings_change_private_before:

    return

label Jean_black_stockings_change_private_after:
    $ Jean.change_face("smirk2", eyes = "down")

    ch_Jean "They show off my legs really nicely."

    $ Jean.eyes = "neutral"

    ch_Jean "I know you're into that."

    return

label Jean_black_stockings_change_public_before:

    return

label Jean_black_stockings_change_public_after:
    $ Jean.change_face("sexy")

    ch_Jean "I look even sexier, right?"

    return