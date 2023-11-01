init -1 python:

    def Rogue_black_tights():
        name = "black tights"
        short_name = "tights"
        string = "black_tights"
        
        Clothing_type = "hose"

        shop_type = "clothing"
        chapter = 0
        season = 0
        
        thresholds = {
            "accept": [0, 0],
            "wear_in_private": [0, 0],
            "wear_in_public": [0, 0]}
        
        price = 0
        
        shame = [-5, 5]
        
        available_states = {
            "standing": [0, 1]}
        undressed_states = {
            "standing": 1}
        
        covers = {
            "standing": {
                "thighs": [0],
                "underwear": [0],
                "ass": [0],
                "pussy": [0],
                "anus": [0]}}
        hides = {
            "standing": {
                "thighs": [0],
                "underwear": [0],
                "ass": [0],
                "pussy": [0],
                "anus": [0]}}

        covered_by = {
            "black_jeans": [0, 1],
            "black_shorts": [0, 1],
            "pink_swimsuit": [0, 1],
            "Rogue_suit": [0],
            "thighhigh_boots": [0],
            "yellow_boots": [0]}
        blocked_by = {
            "black_jeans": [0, 1, 2],
            "black_shorts": [0, 1, 2],
            "pink_swimsuit": [0, 1, 2, 3],
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

label Rogue_black_tights_shopping_accept:
    $ Rogue.change_face("surprised2")

    ch_Rogue "These look mighty familiar. . ."

    return

label Rogue_black_tights_shopping_reject:
    $ Rogue.change_face("worried1")

    ch_Rogue "Ah can buy my own clothes, thank you."

    return

label Rogue_black_tights_gift_accept:
    $ Rogue.change_face("pleased2")

    ch_Rogue "Just like my old high school pair."

    return

label Rogue_black_tights_gift_reject:
    $ Rogue.change_face("worried1")

    ch_Rogue "Ah can buy my own clothes, thank you."

    return

label Rogue_black_tights_change_private_before:

    return

label Rogue_black_tights_change_private_after:
    $ Rogue.change_face("pleased1", eyes = "down")

    ch_Rogue "Ah don't remember these bein' so sheer. . ."

    $ Rogue.eyes = "neutral"

    return

label Rogue_black_tights_change_public_before:

    return

label Rogue_black_tights_change_public_after:
    $ Rogue.change_face("smirk2")

    ch_Rogue "Still comfy."

    return