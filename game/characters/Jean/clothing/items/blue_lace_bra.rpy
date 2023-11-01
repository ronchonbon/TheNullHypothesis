init -1 python:

    def Jean_blue_lace_bra():
        name = "blue lace bra"
        short_name = "bra"
        string = "blue_lace_bra"
        
        Clothing_type = "bra"

        shop_type = "lingerie"
        chapter = 1
        season = 1
        
        thresholds = {
            "accept": [200, 175],
            "wear_in_private": [200, 175],
            "wear_in_public": [225, 200]}
        
        price = 5
        
        shame = [5, 1000]

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

label Jean_blue_lace_bra_shopping_accept:
    $ Jean.change_face("sexy")

    ch_Jean "Want me to look sexy for you?"

    return

label Jean_blue_lace_bra_shopping_reject:
    $ Jean.change_face("surprised2")

    ch_Jean "*gasp*"
    ch_Jean "No way! That's too skimpy. . ."

    return

label Jean_blue_lace_bra_gift_accept:
    $ Jean.change_face("smirk2")

    ch_Jean "Heh, I bet I'll look fantastic in this."

    return

label Jean_blue_lace_bra_gift_reject:
    $ Jean.change_face("surprised2")

    ch_Jean "What the hell?"
    ch_Jean "Why would you think buying me lingerie was a good idea?!"

    return

label Jean_blue_lace_bra_change_private_before:

    return

label Jean_blue_lace_bra_change_private_after:
    $ Jean.change_face("worried1", eyes = "down")

    ch_Jean "You don't think it's too skimpy?"

    $ Jean.eyes = "neutral"

    return

label Jean_blue_lace_bra_change_public_before:
    $ Jean.change_face("sexy")

    ch_Jean "I know you like how good they make my boobs look."

    return

label Jean_blue_lace_bra_change_public_after:

    return