init -1 python:

    def Rogue_green_bikini_bottoms():
        name = "green bikini bottoms"
        short_name = "bikini bottoms"
        string = "green_bikini_bottoms"
        
        Clothing_type = "underwear"

        shop_type = "clothing"
        chapter = 1
        season = 2
        
        thresholds = {
            "accept": [250, 250],
            "wear_in_private": [250, 250],
            "wear_in_public": [275, 275]}
        
        price = 3
        
        shame = [5, 15]
        
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

label Rogue_green_bikini_bottoms_shopping_accept:
    $ Rogue.change_face("worried1")

    pause 1.0

    $ Rogue.change_face("pleased2")

    ch_Rogue "Really? Ah guess it is cute. . ."

    return

label Rogue_green_bikini_bottoms_shopping_reject:
    $ Rogue.change_face("worried1")

    pause 1.0

    $ Rogue.change_face("confused1")

    ch_Rogue "Ya really thought ah'd be okay with ya pickin' out bikini bottoms for me. . . ?"

    return

label Rogue_green_bikini_bottoms_gift_accept:
    $ Rogue.change_face("worried1")

    pause 1.0

    $ Rogue.change_face("pleased1")

    ch_Rogue "Ah. . . well. . . they are nice. . ."

    return

label Rogue_green_bikini_bottoms_gift_reject:
    $ Rogue.change_face("worried1")

    pause 1.0

    $ Rogue.change_face("perplexed")

    ch_Rogue "Skimpy bikini bottoms. . . really hon'?"

    return

label Rogue_green_bikini_bottoms_change_private_before:

    return

label Rogue_green_bikini_bottoms_change_private_after:
    $ Rogue.change_face("worried1", eyes = "down")

    ch_Rogue "A bit skimpy. . . but ah would swim in 'em. . ."

    $ Rogue.eyes = "neutral"

    return

label Rogue_green_bikini_bottoms_change_public_before:
    $ Rogue.change_face("smirk2")

    ch_Rogue "Like the green, or that they're skimpy?"

    $ Rogue.change_face("sly")

    return

label Rogue_green_bikini_bottoms_change_public_after:

    return