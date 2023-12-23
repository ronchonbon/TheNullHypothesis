init -1 python:

    def Jean_blue_gauntlets():
        name = "blue gauntlets"
        short_name = "gauntlets"
        string = "blue_gauntlets"
        
        Clothing_type = "sleeves"

        shop_type = "clothing"
        chapter = 0
        season = 0
        
        thresholds = {
            "accept": [0, 0],
            "wear_in_private": [0, 0],
            "wear_in_public": [0, 0]}
        
        price = 0
        
        shame = [0, 0]

        available_states = {
            "standing": [0]}
        undressed_states = {
            "standing": 0}
        
        covers = {
            "standing": {}}
        hides = {
            "standing": {}}

        covered_by = {}
        blocked_by = {}

        supports_breasts = False
        
        incompatibilities = []
        
        return ClothingClass(
            Jean, 
            name, short_name, string, Clothing_type, 
            shop_type, chapter, season,
            thresholds,
            price = int(price*work_unit*min(max(renpy.random.gauss(1.0, 0.15), 0.85), 1.15)), shame = shame, 
            available_states = available_states, undressed_states = undressed_states,
            covers = covers, hides = hides, 
            covered_by = covered_by, blocked_by = blocked_by,
            supports_breasts = supports_breasts,
            incompatibilities = incompatibilities)

label Jean_blue_gauntlets_shopping_accept:

    return

label Jean_blue_gauntlets_shopping_reject:

    return

label Jean_blue_gauntlets_gift_accept:

    return

label Jean_blue_gauntlets_gift_reject:

    return

label Jean_blue_gauntlets_change_private_before:

    return

label Jean_blue_gauntlets_change_private_after:
    $ Jean.change_face("smirk2")

    ch_Jean "They look cool, right?"

    return

label Jean_blue_gauntlets_change_public_before:

    return

label Jean_blue_gauntlets_change_public_after:
    $ Jean.change_face("smirk2")

    ch_Jean "They look cool, right?"

    return