init -1 python:

    def Laura_red_skirt():
        name = "red skirt"
        short_name = "skirt"
        string = "red_skirt"
        
        Clothing_type = "skirt"

        shop_type = "clothing"
        chapter = 1
        season = 3

        thresholds = {
            "accept": [225, 250],
            "wear_in_private": [225, 250],
            "wear_in_public": [250, 275]}
        
        price = 4
        
        shame = [15, 15]
        
        available_states = {
            "standing": [0, 1]}
        undressed_states = {
            "standing": 1}
        
        covers = {
            "standing": {
                "underwear": [0],
                "ass": [0],
                "pussy": [0],
                "anus": [0]}}
        hides = {
            "standing": {
                "underwear": [0],
                "ass": [0],
                "pussy": [0],
                "anus": [0]}}

        covered_by = {}
        blocked_by = {}

        supports_breasts = False
        
        incompatibilities = [
            "black_athletic_shorts",
            "black_dress",
            "black_jeans",
            "black_shorts",
            "leather_pants",
            "Wolverine_belt"]
        
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

label Laura_red_skirt_shopping_accept:
    $ Laura.change_face("pleased1")

    ch_Laura "Never owned a skirt before. . ."

    return

label Laura_red_skirt_shopping_reject:
    $ Laura.change_face("confused1")

    ch_Laura "A skirt?"
    ch_Laura "Yeah, no."

    return

label Laura_red_skirt_gift_accept:
    $ Laura.change_face("surprised2")

    ch_Laura "It is. . ."
    
    $ Laura.change_face("smirk2")

    ch_Laura "Pretty cool looking."

    return

label Laura_red_skirt_gift_reject:
    $ Laura.change_face("angry1")

    ch_Laura "Why the hell would you buy me that?"

    return

label Laura_red_skirt_change_private_before:

    return

label Laura_red_skirt_change_private_after:
    $ Laura.change_face("perplexed", eyes = "down")

    ch_Laura "What do you think?"

    $ Laura.eyes = "neutral"

    ch_Laura "It's. . . cool."

    return

label Laura_red_skirt_change_public_before:

    return

label Laura_red_skirt_change_public_after:
    $ Laura.change_face("neutral", eyes = "down", blush = 1)

    ch_Laura "I kinda like skirts now. . ."

    $ Laura.eyes = "neutral"
    $ Laura.blush = 0

    return