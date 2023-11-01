init -1 python:

    def Laura_black_boyshorts():
        name = "black boyshorts"
        short_name = "boyshorts"
        string = "black_boyshorts"
        
        Clothing_type = "underwear"

        shop_type = "lingerie"
        chapter = 1
        season = 2

        thresholds = {
            "accept": [200, 225],
            "wear_in_private": [200, 225],
            "wear_in_public": [225, 250]}
        
        price = 3
        
        shame = [-10, 5]
        
        available_states = {
            "standing": [0, 1],
            "doggy": [0],
            "hands_and_knees": [0, 1],
            "masturbation": [0],
            "missionary": [0]}
        undressed_states = {
            "standing": 1,
            "doggy": 0,
            "hands_and_knees": 1,
            "masturbation": 0,
            "missionary": 0}
        
        covers = {
            "standing": {
                "ass": [0],
                "pussy": [0],
                "anus": [0]},
            "doggy": {
                "ass": [0],
                "pussy": [0],
                "anus": [0]},
            "hands_and_knees": {
                "ass": [0],
                "pussy": [0],
                "anus": [0]},
            "masturbation": {
                "ass": [0],
                "pussy": [0],
                "anus": [0]},
            "missionary": {
                "ass": [0],
                "pussy": [0],
                "anus": [0]}}
        hides = {
            "standing": {
                "ass": [0],
                "pussy": [0],
                "anus": [0]},
            "doggy": {
                "ass": [0],
                "pussy": [0],
                "anus": [0]},
            "hands_and_knees": {
                "ass": [0],
                "pussy": [0],
                "anus": [0]},
            "masturbation": {
                "ass": [0],
                "pussy": [0],
                "anus": [0]},
            "missionary": {
                "ass": [0],
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

label Laura_black_boyshorts_shopping_accept:
    $ Laura.change_face("neutral")

    ch_Laura "Huh, good choice."

    return

label Laura_black_boyshorts_shopping_reject:
    $ Laura.change_face("angry1")

    ch_Laura "Don't even think about it."

    return

label Laura_black_boyshorts_gift_accept:
    $ Laura.change_face("neutral")

    ch_Laura "You picked out a nice pair."

    return

label Laura_black_boyshorts_gift_reject:
    $ Laura.change_face("confused1")

    ch_Laura "No."

    return

label Laura_black_boyshorts_change_private_before:

    return

label Laura_black_boyshorts_change_private_after:
    $ Laura.change_face("pleased1")

    ch_Laura "I really like them. . ."

    return

label Laura_black_boyshorts_change_public_before:

    return

label Laura_black_boyshorts_change_public_after:
    $ Laura.change_face("pleased1")

    ch_Laura "Come feel how soft they are."

    return