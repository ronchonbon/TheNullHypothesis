init -1 python:

    def Jean_red_corset():
        name = "red corset"
        short_name = "corset"
        string = "red_corset"
        
        Clothing_type = "bra"

        shop_type = "lingerie"
        chapter = 1
        season = 4
        
        thresholds = {
            "accept": [450, 425],
            "wear_in_private": [450, 425],
            "wear_in_public": [475, 450]}
        
        price = 6
        
        shame = [5, 35]

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
                "breasts": [0],
                "back": [0, 1]},
            "doggy": {
                "breasts": [0],
                "back": [0, 1]},
            "hands_and_knees": {
                "breasts": [0],
                "back": [0, 1]},
            "masturbation": {
                "breasts": [0],
                "back": [0, 1]},
            "missionary": {
                "breasts": [0],
                "back": [0, 1]}}
        hides = {
            "standing": {
                "breasts": [0],
                "back": [0, 1]},
            "doggy": {
                "breasts": [0],
                "back": [0, 1]},
            "hands_and_knees": {
                "breasts": [0],
                "back": [0, 1]},
            "masturbation": {
                "breasts": [0],
                "back": [0, 1]},
            "missionary": {
                "breasts": [0],
                "back": [0, 1]}}

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
            "black_trenchcoat": [0, 1],
            "blue_nighty": [0, 1],
            "college_shirt": [0, 1],
            "denim_jacket": [0, 1],
            "Jean_suit": [0, 1],
            "pink_shirt": [0, 1],
            "puffy_jacket": [0, 1],
            "red_swimsuit": [0, 1, 2, 3],
            "towel": [0],
            "white_cami": [0, 1],
            "white_sweater": [0, 1],
            "yellow_dress": [0, 1]}

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

label Jean_red_corset_shopping_accept:
    $ Jean.change_face("surprised1")

    ch_Jean "Oh! This is. . . nice. . ."

    return

label Jean_red_corset_shopping_reject:
    $ Jean.change_face("confused1")

    ch_Jean "Very funny, [Player.first_name]."

    return

label Jean_red_corset_gift_accept:
    $ Jean.change_face("smirk2")

    ch_Jean "A corset, huh?"
    ch_Jean "I'd consider it. . ."

    return

label Jean_red_corset_gift_reject:
    $ Jean.change_face("surprised2")

    pause 1.0

    $ Jean.change_face("confused1")

    ch_Jean "Why make things weird by buying me a corset?"

    return

label Jean_red_corset_change_private_before:

    return

label Jean_red_corset_change_private_after:
    $ Jean.change_face("worried1", eyes = "down")

    ch_Jean "Not too. . . too much?"

    $ Jean.eyes = "neutral"

    return

label Jean_red_corset_change_public_before:

    return

label Jean_red_corset_change_public_after:
    $ Jean.change_face("sexy")

    ch_Jean "If you could only see the look on your face."

    return