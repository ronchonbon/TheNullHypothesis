init -1 python:

    def Jean_black_cage_bra():
        name = "black cage bra"
        short_name = "bra"
        string = "black_cage_bra"
        
        Clothing_type = "bra"

        shop_type = "lingerie"
        chapter = 1
        season = 4
        
        thresholds = {
            "accept": [425, 375],
            "wear_in_private": [425, 375],
            "wear_in_public": [450, 350]}
        
        price = 6
        
        shame = [5, 25]

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
            "black_shirt": [0],
            "black_trenchcoat": [0],
            "blue_nighty": [0],
            "college_shirt": [0],
            "denim_jacket": [0],
            "Jean_suit": [0],
            "pink_shirt": [0],
            "puffy_jacket": [0],
            "red_swimsuit": [0, 2],
            "towel": [0],
            "white_cami": [0],
            "white_sweater": [0],
            "yellow_dress": [0]}
        blocked_by = {
            "black_shirt": [0, 1],
            "black_trenchcoat": [0],
            "blue_nighty": [0],
            "college_shirt": [0, 1],
            "denim_jacket": [0],
            "Jean_suit": [0],
            "pink_shirt": [0, 1],
            "puffy_jacket": [0],
            "red_swimsuit": [0, 2],
            "towel": [0],
            "white_cami": [0, 1],
            "white_sweater": [0, 1],
            "yellow_dress": [0]}
        
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

label Jean_black_cage_bra_shopping_accept:
    $ Jean.change_face("smirk2")

    ch_Jean "Kinda kinky, [Jean.Player_petname]."

    return

label Jean_black_cage_bra_shopping_reject:
    $ Jean.change_face("surprised2")

    ch_Jean "Get away from me with that."

    return

label Jean_black_cage_bra_gift_accept:
    $ Jean.change_face("smirk2")

    ch_Jean "Mmm. . ."
    ch_Jean "Very subtle, [Jean.Player_petname]. . ."

    return

label Jean_black_cage_bra_gift_reject:
    $ Jean.change_face("surprised3")

    ch_Jean "There's no way I would take that from you {i}or{/i} wear it!"

    return

label Jean_black_cage_bra_change_private_before:

    return

label Jean_black_cage_bra_change_private_after:
    $ Jean.change_face("worried1", eyes = "down")

    ch_Jean "You don't think it's too much?"

    $ Jean.eyes = "neutral"

    return

label Jean_black_cage_bra_change_public_before:

    return

label Jean_black_cage_bra_change_public_after:
    $ Jean.change_face("sexy")

    ch_Jean "I really do spoil you."

    return