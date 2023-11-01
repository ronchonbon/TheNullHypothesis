init -1 python:

    def Laura_black_tape():
        name = "black nipple tape"
        short_name = "nipple tape"
        string = "black_tape"
        
        Clothing_type = "nipple_accessories"

        shop_type = "lingerie"
        chapter = 1
        season = 4
        
        thresholds = {
            "accept": [725, 750],
            "wear_in_private": [725, 750],
            "wear_in_public": [750, 775]}
        
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
            "black_bikini_top": [0],
            "black_cage_bra": [0],
            "black_corset": [0],
            "black_dress": [0],
            "black_lace_bra": [0],
            "black_swimsuit": [0],
            "blackred_corset": [0],
            "blackyellow_Wolverine_suit": [0],
            "blueyellow_Wolverine_suit": [0],
            "denim_jacket": [0],
            "leather_jacket": [0],
            "leather_teddy": [0, 2],
            "striped_shirt": [0],
            "towel": [0],
            "white_sweater": [0],
            "white_tanktop": [0],
            "winter_coat": [0],
            "yellow_sports_bra": [0],
            "yellow_tanktop": [0]}
        blocked_by = {
            "black_bikini_top": [0],
            "black_cage_bra": [0],
            "black_corset": [0],
            "black_dress": [0],
            "black_lace_bra": [0],
            "black_swimsuit": [0],
            "blackred_corset": [0],
            "blackyellow_Wolverine_suit": [0],
            "blueyellow_Wolverine_suit": [0],
            "denim_jacket": [0],
            "leather_jacket": [0],
            "leather_teddy": [0, 2],
            "striped_shirt": [0],
            "towel": [0],
            "white_sweater": [0],
            "white_tanktop": [0],
            "winter_coat": [0],
            "yellow_sports_bra": [0],
            "yellow_tanktop": [0]}

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

label Laura_black_tape_shopping_accept:
    $ Laura.change_face("confused1")

    ch_Laura "They go over my. . . ?"

    return

label Laura_black_tape_shopping_reject:
    $ Laura.change_face("confused1")

    ch_Laura "I don't get it, so no."

    return

label Laura_black_tape_gift_accept:
    $ Laura.change_face("sly")

    ch_Laura "If that's what you like."

    return

label Laura_black_tape_gift_reject:
    $ Laura.change_face("confused1")

    ch_Laura "Weird gift, [Player.first_name]."
    ch_Laura "Not interested."

    return

label Laura_black_tape_change_private_before:

    return

label Laura_black_tape_change_private_after:
    $ Laura.change_face("sly", eyes = "down")

    ch_Laura "You like this huh?"

    $ Laura.eyes = "neutral"

    return

label Laura_black_tape_change_public_before:

    return

label Laura_black_tape_change_public_after:
    $ Laura.change_face("sexy")

    ch_Laura "Sexy?"

    return