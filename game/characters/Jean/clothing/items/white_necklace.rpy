init -1 python:

    def Jean_white_necklace():
        name = "white necklace"
        short_name = "necklace"
        string = "white_necklace"
        
        Clothing_type = "neck"

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

label Jean_white_necklace_shopping_accept:

    return

label Jean_white_necklace_shopping_reject:

    return

label Jean_white_necklace_gift_accept:

    return

label Jean_white_necklace_gift_reject:

    return

label Jean_white_necklace_change_private_before:
    $ Jean.change_face("pleased2")

    ch_Jean "It {i}is{/i} pretty."

    return

label Jean_white_necklace_change_private_after:

    return

label Jean_white_necklace_change_public_before:
    $ Jean.change_face("pleased2")

    ch_Jean "It {i}is{/i} pretty."

    return

label Jean_white_necklace_change_public_after:

    return