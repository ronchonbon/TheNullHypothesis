init -1 python:

    def Jean_blue_lace_panties():
        name = "blue lace panties"
        short_name = "panties"
        string = "blue_lace_panties"
        
        Clothing_type = "underwear"

        shop_type = "lingerie"
        chapter = 1
        season = 1
        
        thresholds = {
            "accept": [225, 200],
            "wear_in_private": [225, 200],
            "wear_in_public": [250, 225]}
        
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
                "pussy": [0],
                "anus": [0]},
            "doggy": {
                "pussy": [0],
                "anus": [0]},
            "hands_and_knees": {
                "pussy": [0],
                "anus": [0]},
            "masturbation": {
                "pussy": [0],
                "anus": [0]},
            "missionary": {
                "pussy": [0],
                "anus": [0]}}
        hides = {
            "standing": {
                "pussy": [0],
                "anus": [0]},
            "doggy": {
                "pussy": [0],
                "anus": [0]},
            "hands_and_knees": {
                "pussy": [0],
                "anus": [0]},
            "masturbation": {
                "pussy": [0],
                "anus": [0]},
            "missionary": {
                "pussy": [0],
                "anus": [0]}}

        covered_by = {
            "black_pants": [0, 1],
            "blue_athletic_shorts": [0],
            "Jean_suit": [0, 1],
            "khaki_pants": [0, 1],
            "red_swimsuit": [0, 1]}
        blocked_by = {
            "black_garterbelt": [0],
            "black_pants": [0, 1, 2],
            "blue_athletic_shorts": [0, 1],
            "Jean_suit": [0, 1],
            "khaki_pants": [0, 1, 2],
            "red_swimsuit": [0, 1]}

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

label Jean_blue_lace_panties_shopping_accept:
    $ Jean.change_face("smirk2")

    ch_Jean "Hmm. . . I would look hot in those."

    return

label Jean_blue_lace_panties_shopping_reject:
    $ Jean.change_face("confused3")

    ch_Jean "I don't think you should be buying panties for me. . ."

    return

label Jean_blue_lace_panties_gift_accept:
    $ Jean.change_face("surprised1")

    pause 1.0

    $ Jean.change_face("sexy")

    ch_Jean "Wouldn't mind putting these on for you sometime. . ."

    return

label Jean_blue_lace_panties_gift_reject:
    $ Jean.change_face("angry1")

    ch_Jean "What the fuck."
    ch_Jean "Really? Buying me panties?"

    return

label Jean_blue_lace_panties_change_private_before:

    return

label Jean_blue_lace_panties_change_private_after:
    $ Jean.change_face("worried2", eyes = "down")

    ch_Jean "You can see right through them. . ."

    $ Jean.change_face("smirk2")

    ch_Jean "I bet you like that."

    return

label Jean_blue_lace_panties_change_public_before:
    $ Jean.change_face("sexy")

    ch_Jean "Only for you. . ."

    return

label Jean_blue_lace_panties_change_public_after:

    return