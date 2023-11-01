init -1 python:

    def Jean_yellow_bikini_top():
        name = "yellow bikini top"
        short_name = "bikini top"
        string = "yellow_bikini_top"
        
        Clothing_type = "bra"

        shop_type = "clothing"
        chapter = 0
        season = 0
        
        thresholds = {
            "accept": [275, 225],
            "wear_in_private": [275, 225],
            "wear_in_public": [275, 250]}
        
        price = 2
        
        shame = [5, 15]

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

label Jean_yellow_bikini_top_shopping_accept:
    $ Jean.change_face("pleased2")

    ch_Jean "It's a bit revealing. . ."

    $ Jean.change_face("sly")

    ch_Jean "But cute. . ."

    return

label Jean_yellow_bikini_top_shopping_reject:
    $ Jean.change_face("confused2")

    ch_Jean "Just. . . no. . ."

    return

label Jean_yellow_bikini_top_gift_accept:
    $ Jean.change_face("surprised2")

    ch_Jean "Damn. . ."

    $ Jean.change_face("sly")

    ch_Jean "I bet you're dying to see me in this. . ."

    return

label Jean_yellow_bikini_top_gift_reject:
    $ Jean.change_face("confused2")

    ch_Jean "The hell. . ."
    ch_Jean "Why would you buy me a swimsuit?"

    return

label Jean_yellow_bikini_top_change_private_before:

    return

label Jean_yellow_bikini_top_change_private_after:
    $ Jean.change_face("smirk2")

    ch_Jean "My eyes are up here."

    return

label Jean_yellow_bikini_top_change_public_before:

    return

label Jean_yellow_bikini_top_change_public_after:
    $ Jean.change_face("smirk2")

    ch_Jean "My eyes are up here."

    return