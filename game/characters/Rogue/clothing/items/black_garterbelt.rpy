init -1 python:

    def Rogue_black_garterbelt():
        name = "black garterbelt"
        short_name = "garterbelt"
        string = "black_garterbelt"
        
        Clothing_type = "hose"

        shop_type = "lingerie"
        chapter = 1
        season = 3
        
        thresholds = {
            "accept": [250, 250],
            "wear_in_private": [250, 250],
            "wear_in_public": [275, 275]}
        
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
            "black_jeans": [0, 1],
            "black_shorts": [0, 1],
            "pink_swimsuit": [0, 1],
            "Rogue_suit": [0]}
        blocked_by = {
            "black_jeans": [0, 1, 2],
            "black_shorts": [0, 1, 2],
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

label Rogue_black_garterbelt_shopping_accept:
    $ Rogue.change_face("surprised1")

    ch_Rogue "Ah do like the pattern. . ."

    return

label Rogue_black_garterbelt_shopping_reject:
    $ Rogue.change_face("confused1")

    ch_Rogue "Why do ah need somethin' like that, hon'?"

    return

label Rogue_black_garterbelt_gift_accept:
    $ Rogue.change_face("pleased1")

    ch_Rogue "A garterbelt?."
    ch_Rogue "Interestin'."

    $ Rogue.change_face("smirk2")

    return

label Rogue_black_garterbelt_gift_reject:
    $ Rogue.change_face("worried1")

    ch_Rogue "Ah'm not really cool with you giftin' me lingerie. . ."

    return

label Rogue_black_garterbelt_change_private_before:

    return

label Rogue_black_garterbelt_change_private_after:
    $ Rogue.change_face("smirk2", eyes = "down")

    ch_Rogue "You really guessed my waist size perfectly. . ."

    $ Rogue.eyes = "neutral"

    return

label Rogue_black_garterbelt_change_public_before:

    return

label Rogue_black_garterbelt_change_public_after:
    $ Rogue.change_face("smirk2")

    ch_Rogue "Ya like this one too?"

    return