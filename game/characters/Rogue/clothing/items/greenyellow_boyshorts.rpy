init -1 python:

    def Rogue_greenyellow_boyshorts():
        name = "green-and-yellow boyshorts"
        short_name = "boyshorts"
        string = "greenyellow_boyshorts"
        
        Clothing_type = "underwear"

        shop_type = "clothing"
        chapter = 1
        season = 2
        
        thresholds = {
            "accept": [225, 225],
            "wear_in_private": [225, 225],
            "wear_in_public": [250, 250]}
        
        price = 3
        
        shame = [-10, 10]
        
        available_states = {
            "standing": [0, 1],
            "doggy": [0],
            "hands_and_knees": [0],
            "masturbation": [0],
            "missionary": [0]}
        undressed_states = {
            "standing": 1,
            "doggy": 0,
            "hands_and_knees": 0,
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
            "black_garterbelt": [0],
            "black_jeans": [0, 1],
            "black_shorts": [0, 1],
            "black_tights": [0],
            "pink_swimsuit": [0, 1],
            "Rogue_suit": [0]}
        blocked_by = {
            "black_garterbelt": [0],
            "black_jeans": [0, 1, 2],
            "black_shorts": [0, 1, 2],
            "black_tights": [0, 1],
            "pink_swimsuit": [0, 1, 2, 3],
            "Rogue_suit": [0]}

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

label Rogue_greenyellow_boyshorts_shopping_accept:
    $ Rogue.change_face("pleased2")

    ch_Rogue "Ah love 'em!"

    return

label Rogue_greenyellow_boyshorts_shopping_reject:
    $ Rogue.change_face("perplexed")

    ch_Rogue "Ah can buy my own clothes, thank you."

    return

label Rogue_greenyellow_boyshorts_gift_accept:
    $ Rogue.change_face("surprised2")

    ch_Rogue "Oh, thank you!"

    return

label Rogue_greenyellow_boyshorts_gift_reject:
    $ Rogue.change_face("worried1")

    ch_Rogue "No thank you, [Player.first_name]."

    return

label Rogue_greenyellow_boyshorts_change_private_before:

    return

label Rogue_greenyellow_boyshorts_change_private_after:
    $ Rogue.change_face("pleased2", eyes = "down")

    ch_Rogue "So comfy!"

    $ Rogue.eyes = "neutral"

    return

label Rogue_greenyellow_boyshorts_change_public_before:

    return

label Rogue_greenyellow_boyshorts_change_public_after:
    $ Rogue.change_face("pleased2", eyes = "down")

    ch_Rogue "These are some of my favorites."

    $ Rogue.eyes = "neutral"

    return