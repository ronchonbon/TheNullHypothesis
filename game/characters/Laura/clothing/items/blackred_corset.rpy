init -1 python:

    def Laura_blackred_corset():
        name = "black-and-red corset"
        short_name = "corset"
        string = "blackred_corset"
        
        Clothing_type = "bra"

        shop_type = "clothing"
        chapter = 1
        season = 3

        thresholds = {
            "accept": [225, 250],
            "wear_in_private": [225, 250],
            "wear_in_public": [250, 275]}
        
        price = 4
        
        shame = [10, 10]
        
        available_states = {
            "standing": [0, 1],
            "doggy": [0],
            "hands_and_knees": [0, 1],
            "masturbation": [0, 1],
            "missionary": [0, 1]}
        undressed_states = {
            "standing": 1,
            "doggy": 0,
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
            "black_dress": [0, 1],
            "black_swimsuit": [0, 1],
            "blackyellow_Wolverine_suit": [0, 1],
            "blueyellow_Wolverine_suit": [0, 1],
            "denim_jacket": [0, 1],
            "leather_jacket": [0, 1],
            "leather_teddy": [0, 1, 2, 3],
            "striped_shirt": [0, 1],
            "towel": [0],
            "white_sweater": [0, 1],
            "winter_coat": [0],
            "yellow_tanktop": [0, 1]}

        supports_breasts = False
        
        incompatibilities = [
            "leather_teddy"]
        
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

label Laura_blackred_corset_shopping_accept:
    $ Laura.change_face("pleased1")

    ch_Laura "Not very functional. . . but. . . pretty cool."

    return

label Laura_blackred_corset_shopping_reject:
    $ Laura.change_face("confused1")

    ch_Laura "The hell is this thing?"

    return

label Laura_blackred_corset_gift_accept:
    $ Laura.change_face("neutral")

    ch_Laura "I. . . don't hate it."

    return

label Laura_blackred_corset_gift_reject:
    $ Laura.change_face("angry1")

    ch_Laura "Why would you buy me a. . . the hell even is this?"

    return

label Laura_blackred_corset_change_private_before:
    $ Laura.change_face("perplexed", eyes = "down")

    ch_Laura "Really?"

    return

label Laura_blackred_corset_change_private_after:
    $ Laura.eyes = "neutral"

    ch_Laura "It's. . . not terrible."

    return

label Laura_blackred_corset_change_public_before:

    return

label Laura_blackred_corset_change_public_after:
    $ Laura.change_face("surprised1")

    ch_Laura "It's pretty restricting. . ."

    $ Laura.change_face("sly")

    ch_Laura "But looks good."

    return