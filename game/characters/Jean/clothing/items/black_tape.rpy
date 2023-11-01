init -1 python:

    def Jean_black_tape():
        name = "black nipple tape"
        short_name = "nipple tape"
        string = "black_tape"
        
        Clothing_type = "nipple_accessories"

        shop_type = "lingerie"
        chapter = 1
        season = 4
        
        thresholds = {
            "accept": [750, 700],
            "wear_in_private": [750, 700],
            "wear_in_public": [775, 725]}
        
        price = 2
        
        shame = [10, 1000]

        available_states = {
            "standing": [0],
            "doggy": [0],
            "hands_and_knees": [0],
            "masturbation": [0],
            "missionary": [0]}
        undressed_states = {
            "standing": 0,
            "doggy": 0,
            "hands_and_knees": 0,
            "masturbation": 0,
            "missionary": 0}
        
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
            "standing": {},
            "doggy": {},
            "hands_and_knees": {},
            "masturbation": {},
            "missionary": {}}

        covered_by = {
            "black_balconette_bra": [0],
            "black_cage_bra": [0],
            "black_shirt": [0],
            "black_trenchcoat": [0],
            "blue_lace_bra": [0],
            "blue_nighty": [0],
            "college_shirt": [0],
            "denim_jacket": [0],
            "Jean_suit": [0],
            "pink_bra": [0],
            "pink_shirt": [0],
            "puffy_jacket": [0],
            "red_corset": [0],
            "red_swimsuit": [0, 2],
            "towel": [0],
            "white_cami": [0],
            "white_sweater": [0],
            "yellow_bikini_top": [0],
            "yellow_dress": [0],
            "yellow_sports_bra": [0]}
        blocked_by = {
            "black_balconette_bra": [0],
            "black_cage_bra": [0],
            "black_shirt": [0],
            "black_trenchcoat": [0],
            "blue_lace_bra": [0],
            "blue_nighty": [0],
            "college_shirt": [0],
            "denim_jacket": [0],
            "Jean_suit": [0],
            "pink_bra": [0],
            "pink_shirt": [0],
            "puffy_jacket": [0],
            "red_corset": [0],
            "red_swimsuit": [0, 2],
            "towel": [0],
            "white_cami": [0],
            "white_sweater": [0],
            "yellow_bikini_top": [0],
            "yellow_dress": [0],
            "yellow_sports_bra": [0]}

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

label Jean_black_tape_shopping_accept:
    $ Jean.change_face("confused1")

    ch_Jean "You really want me to put these on?"

    return

label Jean_black_tape_shopping_reject:
    $ Jean.change_face("confused1")

    ch_Jean "What is this for. . . ?"
    ch_Jean "No thanks, [Player.first_name]. . ."

    return

label Jean_black_tape_gift_accept:
    $ Jean.change_face("sexy")

    ch_Jean "That's pretty kinky, [Player.first_name]. . ."

    return

label Jean_black_tape_gift_reject:
    $ Jean.change_face("confused1")

    ch_Jean "I don't get it and I don't want to."

    return

label Jean_black_tape_change_private_before:

    return

label Jean_black_tape_change_private_after:
    $ Jean.change_face("smirk2", eyes = "down")

    ch_Jean "This feels naughty. . ."

    $ Jean.eyes = "neutral"

    ch_Jean "You like?"

    return

label Jean_black_tape_change_public_before:

    return

label Jean_black_tape_change_public_after:
    $ Jean.change_face("sexy")

    ch_Jean "Well, what do you think?"

    return