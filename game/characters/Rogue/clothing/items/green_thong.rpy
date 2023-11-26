init -1 python:

    def Rogue_green_thong():
        name = "green thong"
        short_name = "thong"
        string = "green_thong"
        
        Clothing_type = "underwear"

        shop_type = "lingerie"
        chapter = 1
        season = 3
        
        thresholds = {
            "accept": [600, 600],
            "wear_in_private": [600, 600],
            "wear_in_public": [625, 625]}
        
        price = 4
        
        shame = [-2, 5]
        
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

label Rogue_green_thong_shopping_accept:

    return

label Rogue_green_thong_shopping_reject:

    return

label Rogue_green_thong_gift_accept:

    return

label Rogue_green_thong_gift_reject:

    return

label Rogue_green_thong_change_private_before:

    return

label Rogue_green_thong_change_private_after:

    return

label Rogue_green_thong_change_public_before:

    return

label Rogue_green_thong_change_public_after:

    return