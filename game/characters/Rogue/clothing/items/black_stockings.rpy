init -1 python:

    def Rogue_black_stockings():
        name = "black stockings"
        short_name = "stockings"
        string = "black_stockings"
        
        Clothing_type = "socks"

        shop_type = "lingerie"
        chapter = 1
        season = 3
        
        thresholds = {
            "accept": [250, 250],
            "wear_in_private": [250, 250],
            "wear_in_public": [275, 275]}
        
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
            "black_jeans": [0, 1],
            "black_shorts": [0, 1],
            "Rogue_suit": [0],
            "thighhigh_boots": [0],
            "yellow_boots": [0]}
        blocked_by = {
            "black_jeans": [0, 1, 2],
            "black_shorts": [0, 1, 2],
            "Rogue_suit": [0],
            "thighhigh_boots": [0],
            "yellow_boots": [0]}

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

label Rogue_black_stockings_shopping_accept:
    $ Rogue.change_face("pleased1")

    ch_Rogue "Good choice, hon'."

    return

label Rogue_black_stockings_shopping_reject:
    $ Rogue.change_face("worried1")

    ch_Rogue "Stockin's? Ah don't really need those right now. . ."

    return

label Rogue_black_stockings_gift_accept:
    $ Rogue.change_face("smirk2")

    ch_Rogue "Stockin's? You must really like my legs."

    return

label Rogue_black_stockings_gift_reject:
    $ Rogue.change_face("confused1")

    ch_Rogue "Giftin' me lingerie?"

    $ Rogue.change_face("neutral")

    ch_Rogue "Ah'm good, thanks."

    return

label Rogue_black_stockings_change_private_before:

    return

label Rogue_black_stockings_change_private_after:
    ch_Rogue "Think they look good on me?"

    return

label Rogue_black_stockings_change_public_before:

    return

label Rogue_black_stockings_change_public_after:
    $ Rogue.change_face("smirk2")

    ch_Rogue "They are pretty nice."

    return