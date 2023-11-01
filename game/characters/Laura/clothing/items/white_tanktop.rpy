init -1 python:

    def Laura_white_tanktop():
        name = "white tanktop"
        short_name = "tanktop"
        string = "white_tanktop"
        
        Clothing_type = "bra"

        shop_type = "clothing"
        chapter = 0
        season = 0

        thresholds = {
            "accept": [0, 0],
            "wear_in_private": [0, 0],
            "wear_in_public": [0, 0]}
        
        price = 0

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
            "standing": {},
            "doggy": {},
            "hands_and_knees": {},
            "masturbation": {},
            "missionary": {}}
        hides = {
            "standing": {},
            "doggy": {},
            "hands_and_knees": {},
            "masturbation": {},
            "missionary": {}}

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

label Laura_white_tanktop_shopping_accept:

    return

label Laura_white_tanktop_shopping_reject:

    return

label Laura_white_tanktop_gift_accept:

    return

label Laura_white_tanktop_gift_reject:

    return

label Laura_white_tanktop_change_private_before:

    return

label Laura_white_tanktop_change_private_after:
    $ Laura.change_face("neutral")

    ch_Laura "This one's fine."

    return

label Laura_white_tanktop_change_public_before:

    return

label Laura_white_tanktop_change_public_after:
    $ Laura.change_face("neutral")

    ch_Laura "This one's fine."

    return