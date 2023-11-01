init -1 python:

    def Laura_black_bikini_bottoms():
        name = "black bikini bottoms"
        short_name = "bikini bottoms"
        string = "black_bikini_bottoms"
        
        Clothing_type = "underwear"

        shop_type = "clothing"
        chapter = 1
        season = 2

        thresholds = {
            "accept": [200, 225],
            "wear_in_private": [200, 225],
            "wear_in_public": [225, 250]}
        
        price = 3
        
        shame = [5, 15]
        
        available_states = {
            "standing": [0, 1],
            "doggy": [0, 1],
            "hands_and_knees": [0, 1],
            "masturbation": [0, 1],
            "missionary": [0, 1]}
        undressed_states = {
            "standing": 1,
            "doggy": 1,
            "hands_and_knees": 1,
            "masturbation": 1,
            "missionary": 1}
        
        covers = {
            "standing": {
                "pussy": [0],
                "anus": [0]},
            "doggy": {
                "pussy": [0],
                "anus": [0]},
            "hands_and_knees": {
                "pussy": [0],
                "anus": [0]},
            "masturbation": {
                "pussy": [0],
                "anus": [0]},
            "missionary": {
                "pussy": [0],
                "anus": [0]}}
        hides = {
            "standing": {
                "pussy": [0],
                "anus": [0]},
            "doggy": {
                "pussy": [0],
                "anus": [0]},
            "hands_and_knees": {
                "pussy": [0],
                "anus": [0]},
            "masturbation": {
                "pussy": [0],
                "anus": [0]},
            "missionary": {
                "pussy": [0],
                "anus": [0]}}

        covered_by = {
            "black_athletic_shorts": [0],
            "black_jeans": [0, 1],
            "black_shorts": [0, 1],
            "black_swimsuit": [0, 1],
            "blackred_garterbelt": [0],
            "blackyellow_Wolverine_suit": [0, 1],
            "blueyellow_Wolverine_suit": [0, 1],
            "leather_pants": [0, 1],
            "leather_teddy": [0, 1]}
        blocked_by = {
            "black_athletic_shorts": [0, 1],
            "black_jeans": [0, 1, 2],
            "black_shorts": [0, 1, 2],
            "black_swimsuit": [0, 1, 2, 3],
            "blackred_garterbelt": [0],
            "blackyellow_Wolverine_suit": [0, 1],
            "blueyellow_Wolverine_suit": [0, 1],
            "leather_pants": [0, 1, 2],
            "leather_teddy": [0, 1, 2, 3]}

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

label Laura_black_bikini_bottoms_shopping_accept:
    $ Laura.change_face("pleased1")

    ch_Laura "At least it won't be restrictive. . ."

    return

label Laura_black_bikini_bottoms_shopping_reject:
    $ Laura.change_face("confused1")

    ch_Laura "Don't even try."

    return

label Laura_black_bikini_bottoms_gift_accept:
    $ Laura.change_face("confused1")

    ch_Laura "It's a bit. . . small."

    return

label Laura_black_bikini_bottoms_gift_reject:
    $ Laura.change_face("angry1")

    ch_Laura "Why are you buying things for me?"

    $ Laura.change_face("suspicious")

    return

label Laura_black_bikini_bottoms_change_private_before:
    $ Laura.change_face("perplexed", eyes = "down")

    ch_Laura "You really think I should swim in this?"

    $ Laura.eyes = "neutral"

    ch_Laura "It's. . . small."

    return

label Laura_black_bikini_bottoms_change_private_after:

    return

label Laura_black_bikini_bottoms_change_public_before:
    $ Laura.change_face("sly")

    ch_Laura "I know why you like this one. . ."

    return

label Laura_black_bikini_bottoms_change_public_after:

    return