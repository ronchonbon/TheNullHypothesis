init -1 python:

    def Laura_blackred_ripped_stockings():
        name = "black-and-red ripped stockings"
        short_name = "stockings"
        string = "blackred_ripped_stockings"
        
        Clothing_type = "socks"

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
            "black_jeans": [0],
            "blackyellow_Wolverine_boots": [0],
            "blackyellow_Wolverine_suit": [0, 1],
            "blueyellow_Wolverine_boots": [0],
            "blueyellow_Wolverine_suit": [0, 1],
            "combat_boots": [0],
            "leather_pants": [0],
            "thighhigh_boots": [0]}
        blocked_by = {
            "black_jeans": [0, 1],
            "blackyellow_Wolverine_boots": [0],
            "blackyellow_Wolverine_suit": [0, 1],
            "blueyellow_Wolverine_boots": [0],
            "blueyellow_Wolverine_suit": [0, 1],
            "combat_boots": [0],
            "leather_pants": [0, 1],
            "thighhigh_boots": [0]}

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

label Laura_blackred_ripped_stockings_shopping_accept:
    $ Laura.change_face("smirk2")

    ch_Laura "I guess they do make my legs look good."

    return

label Laura_blackred_ripped_stockings_shopping_reject:
    $ Laura.change_face("confused1")

    ch_Laura "What would I need those for?"

    return

label Laura_blackred_ripped_stockings_gift_accept:
    $ Laura.change_face("pleased1")

    ch_Laura "You really do like my muscular legs, huh. . ."

    return

label Laura_blackred_ripped_stockings_gift_reject:
    $ Laura.change_face("perplexed")

    ch_Laura "Why?"
    ch_Laura "And. . . they're ripped already. . ."

    return

label Laura_blackred_ripped_stockings_change_private_before:
    $ Laura.change_face("confused1", eyes = "down")

    ch_Laura "Why are these ripped already again?"

    return

label Laura_blackred_ripped_stockings_change_private_after:
    $ Laura.eyes = "neutral"

    ch_Laura "Don't mind the look, though. . ."

    return

label Laura_blackred_ripped_stockings_change_public_before:
    $ Laura.change_face("smirk2")

    ch_Laura "You like em' too?"
    ch_Laura "Heh, I probably would've ended up ripping them anyway."

    return

label Laura_blackred_ripped_stockings_change_public_after:

    return