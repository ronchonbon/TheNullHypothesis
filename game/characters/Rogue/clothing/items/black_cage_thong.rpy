init -1 python:

    def Rogue_black_cage_thong():
        name = "black cage thong"
        short_name = "thong"
        string = "black_cage_thong"
        
        Clothing_type = "underwear"

        shop_type = "lingerie"
        chapter = 1
        season = 4
        
        thresholds = {
            "accept": [650, 650],
            "wear_in_private": [650, 650],
            "wear_in_public": [675, 675]}
        
        price = 6
        
        shame = [-2, 35]
        
        available_states = {
            "standing": [0, 1]}
        undressed_states = {
            "standing": 1}
        
        covers = {
            "standing": {
                "pussy": [0],
                "anus": [0]}}
        hides = {
            "standing": {
                "pussy": [0],
                "anus": [0]}}

        covered_by = {
            "black_jeans": [0]}
        blocked_by = {
            "black_jeans": [0, 1]}

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

label Rogue_black_cage_thong_shopping_accept:
    $ Rogue.change_face("surprised2")

    ch_Rogue "Wow, these are sexy."

    $ Rogue.change_face("worried1")

    ch_Rogue "Not {i}too{/i} sexy, right?"

    return

label Rogue_black_cage_thong_shopping_reject:
    $ Rogue.change_face("perplexed")

    ch_Rogue "Yeah. . . no. . ."

    return

label Rogue_black_cage_thong_gift_accept:
    $ Rogue.change_face("surprised2")

    ch_Rogue "Damn, [Player.first_name]."

    $ Rogue.change_face("smirk2")

    ch_Rogue "Ah wonder why you like these. . ."

    return

label Rogue_black_cage_thong_gift_reject:
    $ Rogue.change_face("worried1")

    ch_Rogue "Why would ah even consider it. . . ?"

    return

label Rogue_black_cage_thong_change_private_before:

    return

label Rogue_black_cage_thong_change_private_after:
    $ Rogue.change_face("smirk2", eyes = "down")

    ch_Rogue "Ah wonder why you like these so much. . ."

    $ Rogue.eyes = "neutral"

    return

label Rogue_black_cage_thong_change_public_before:

    return

label Rogue_black_cage_thong_change_public_after:
    $ Rogue.change_face("smirk2")

    ch_Rogue "What do ya think, [Rogue.Player_petname]?"

    return