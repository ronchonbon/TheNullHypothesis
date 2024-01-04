init -1 python:

    def Jean_pink_bra():
        name = "pink bra"
        short_name = "bra"
        string = "pink_bra"
        
        Clothing_type = "bra"

        shop_type = "clothing"
        chapter = 0
        season = 0
        
        thresholds = {
            "accept": [0, 0],
            "wear_in_private": [0, 0],
            "wear_in_public": [0, 0]}
        
        price = 0
        
        shame = [-5, 20]

        available_states = {
            "standing": [0, 1],
            "doggy": [0, 1],
            "hands_and_knees": [0, 1],
            "masturbation": [0, 1],
            "missionary": [0, 1]}
        undressed_states = {
            "standing": 1,
            "doggy": 1,
            "hands_and_knees": 1,
            "masturbation": 1,
            "missionary": 1}
        
        covers = {
            "standing": {
                "breasts": [0]},
            "doggy": {
                "breasts": [0]},
            "hands_and_knees": {
                "breasts": [0]},
            "masturbation": {
                "breasts": [0]},
            "missionary": {
                "breasts": [0]}}
        hides = {
            "standing": {
                "breasts": [0]},
            "doggy": {
                "breasts": [0]},
            "hands_and_knees": {
                "breasts": [0]},
            "masturbation": {
                "breasts": [0]},
            "missionary": {
                "breasts": [0]}}

        covered_by = {
            "blueyellow_classic_suit": [0],
            "pink_top": [0],
            "red_swimsuit": [0, 2]}
        blocked_by = {
            "blueyellow_classic_suit": [0],
            "pink_top": [0, 1],
            "red_swimsuit": [0, 1, 2, 3]}

        supports_breasts = True
        
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

label Jean_pink_bra_shopping_accept:

    return

label Jean_pink_bra_shopping_reject:

    return

label Jean_pink_bra_gift_accept:

    return

label Jean_pink_bra_gift_reject:

    return

label Jean_pink_bra_change_private_before:

    return

label Jean_pink_bra_change_private_after:
    $ Jean.change_face("smirk2")

    ch_Jean "Comfy and cute."

    return

label Jean_pink_bra_change_public_before:

    return

label Jean_pink_bra_change_public_after:
    $ Jean.change_face("smirk2")

    ch_Jean "Comfy and cute."

    return