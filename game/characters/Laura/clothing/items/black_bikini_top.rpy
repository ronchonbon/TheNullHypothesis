init -1 python:

    def Laura_black_bikini_top():
        name = "black bikini top"
        short_name = "bikini top"
        string = "black_bikini_top"
        
        Clothing_type = "bra"

        shop_type = "clothing"
        chapter = 1
        season = 2

        thresholds = {
            "accept": [200, 225],
            "wear_in_private": [200, 225],
            "wear_in_public": [225, 250]}
        
        price = 3
        
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
            "black_dress": [0],
            "black_swimsuit": [0],
            "blackyellow_Wolverine_suit": [0],
            "blueyellow_Wolverine_suit": [0],
            "denim_jacket": [0],
            "leather_jacket": [0],
            "leather_teddy": [0, 2],
            "striped_shirt": [0],
            "towel": [0],
            "white_sweater": [0],
            "winter_coat": [0],
            "yellow_tanktop": [0]}
        blocked_by = {
            "black_dress": [0],
            "black_swimsuit": [0],
            "blackyellow_Wolverine_suit": [0, 1],
            "blueyellow_Wolverine_suit": [0, 1],
            "denim_jacket": [0],
            "leather_jacket": [0],
            "leather_teddy": [0, 1, 2, 3],
            "striped_shirt": [0, 1],
            "towel": [0],
            "white_sweater": [0, 1],
            "winter_coat": [0],
            "yellow_tanktop": [0, 1]}

        supports_breasts = False
        
        incompatibilities = []
        
        return ClothingClass(
            Laura, 
            name, short_name, string, Clothing_type, 
            shop_type, chapter, season,
            thresholds,
            price = int(price*work_unit*min(max(renpy.random.gauss(1.0, 0.15), 0.85), 1.15)), shame = shame, 
            available_states = available_states, undressed_states = undressed_states,
            covers = covers, hides = hides, 
            covered_by = covered_by, blocked_by = blocked_by,
            supports_breasts = supports_breasts,
            incompatibilities = incompatibilities)

label Laura_black_bikini_top_shopping_accept:
    $ Laura.change_face("pleased1")

    ch_Laura "It is. . . not bad."

    return

label Laura_black_bikini_top_shopping_reject:
    $ Laura.change_face("confused1")

    ch_Laura "You really trying to buy that for me?"

    $ Laura.change_face("angry1")

    ch_Laura "No."

    return

label Laura_black_bikini_top_gift_accept:
    $ Laura.change_face("sly")

    ch_Laura "You really like this one?"
    ch_Laura ". . . fine."

    return

label Laura_black_bikini_top_gift_reject:
    $ Laura.change_face("angry1")

    ch_Laura "The fuck? Why are you buying me stuff like that?"

    return

label Laura_black_bikini_top_change_private_before:
    $ Laura.change_face("perplexed", eyes = "down")

    ch_Laura "I know you're a fan of this one. . ."
    
    $ Laura.change_face("sly")

    ch_Laura "Weirdo."

    return

label Laura_black_bikini_top_change_private_after:

    return

label Laura_black_bikini_top_change_public_before:
    $ Laura.change_face("smirk2")

    ch_Laura "Yeah, it's not bad. . ."

    return

label Laura_black_bikini_top_change_public_after:

    return