init -1 python:

    def Rogue_black_tall_socks():
        name = "black tall socks"
        short_name = "socks"
        string = "black_tall_socks"
        
        Clothing_type = "socks"

        shop_type = "clothing"
        chapter = 1
        season = 2
        
        thresholds = {
            "accept": [175, 175],
            "wear_in_private": [175, 175],
            "wear_in_public": [200, 200]}
        
        price = 2
        
        shame = [-5, -5]
        
        available_states = {
            "standing": [0]}
        undressed_states = {
            "standing": 0}
        
        covers = {
            "standing": {
                "feet": [0]}}
        hides = {
            "standing": {
                "feet": [0]}}

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

label Rogue_black_tall_socks_shopping_accept:
    $ Rogue.change_face("pleased1")

    ch_Rogue "They look comfy. . ."

    return

label Rogue_black_tall_socks_shopping_reject:
    $ Rogue.change_face("worried1")

    ch_Rogue "Uhm . . Ah'm okay, thanks. . ."

    return

label Rogue_black_tall_socks_gift_accept:
    $ Rogue.change_face("smirk2")

    ch_Rogue "Think they'd look good? Could be nice."

    return

label Rogue_black_tall_socks_gift_reject:
    $ Rogue.change_face("confused1")

    ch_Rogue "Ah don't really need socks. . ."

    return

label Rogue_black_tall_socks_change_private_before:

    return

label Rogue_black_tall_socks_change_private_after:
    $ Rogue.change_face("pleased1", eyes = "down")
    
    pause 1.0

    $ Rogue.eyes = "neutral"

    ch_Rogue "Like 'em?"

    return

label Rogue_black_tall_socks_change_public_before:

    return

label Rogue_black_tall_socks_change_public_after:
    $ Rogue.change_face("smirk2")

    ch_Rogue "They are comfy."

    return