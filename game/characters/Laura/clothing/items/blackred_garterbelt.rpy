init -1 python:

    def Laura_blackred_garterbelt():
        name = "black-and-red garterbelt"
        short_name = "garterbelt"
        string = "blackred_garterbelt"
        
        Clothing_type = "hose"

        shop_type = "lingerie"
        chapter = 1
        season = 3

        thresholds = {
            "accept": [225, 250],
            "wear_in_private": [225, 250],
            "wear_in_public": [250, 275]}
        
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
            "black_athletic_shorts": [0],
            "black_jeans": [0, 1],
            "black_shorts": [0],
            "leather_pants": [0, 1]}
        blocked_by = {
            "black_athletic_shorts": [0, 1],
            "black_jeans": [0, 1, 2],
            "black_shorts": [0, 1],
            "leather_pants": [0, 1, 2]}

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

label Laura_blackred_garterbelt_shopping_accept:
    $ Laura.change_face("perplexed")

    ch_Laura "I still don't know what it is. . ."
    ch_Laura "But it looks well made I guess."

    return

label Laura_blackred_garterbelt_shopping_reject:
    $ Laura.change_face("confused1")

    ch_Laura "What even is that?"
    ch_Laura "Not wearing that."

    return

label Laura_blackred_garterbelt_gift_accept:
    $ Laura.change_face("perplexed")
    
    ch_Laura "Uh. . . thanks."
    ch_Laura "What is this again?"

    return

label Laura_blackred_garterbelt_gift_reject:
    $ Laura.change_face("confused1")

    ch_Laura "Uh. . . I'm good."

    return

label Laura_blackred_garterbelt_change_private_before:

    return

label Laura_blackred_garterbelt_change_private_after:
    $ Laura.change_face("confused1", eyes = "down")

    ch_Laura "It's well-made I guess. . ."

    $ Laura.eyes = "neutral"

    return

label Laura_blackred_garterbelt_change_public_before:
    $ Laura.change_face("smirk2")

    ch_Laura "I don't mind this one. . . now that I know what it is."

    return

label Laura_blackred_garterbelt_change_public_after:

    return