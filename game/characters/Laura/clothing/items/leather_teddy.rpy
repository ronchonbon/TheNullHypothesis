init -1 python:

    def Laura_leather_teddy():
        name = "leather teddy"
        short_name = "teddy"
        string = "leather_teddy"

        Clothing_type = "bodysuit"

        shop_type = "lingerie"
        chapter = 1
        season = 4

        thresholds = {
            "accept": [625, 650],
            "wear_in_private": [625, 650],
            "wear_in_public": [650, 675]}

        price = 5

        shame = [30, 30]

        available_states = {
            "standing": [0, 1],
            "doggy": [0, 2],
            "hands_and_knees": [0, 1],
            "masturbation": [0, 1, 2, 3],
            "missionary": [0, 1, 2, 3]}
        undressed_states = {
            "standing": 1,
            "doggy": 2,
            "hands_and_knees": 1,
            "masturbation": 1,
            "missionary": 1}
        
        covers = {
            "standing": {
                "bra": [0],
                "breasts": [0],
                "back": [0, 1],
                "belly": [0, 1],
                "underwear": [0, 1],
                "pussy": [0, 1],
                "anus": [0, 1]},
            "doggy": {
                "bra": [0, 2],
                "breasts": [0, 2],
                "back": [0, 2],
                "belly": [0, 2],
                "underwear": [0],
                "pussy": [0],
                "anus": [0]},
            "hands_and_knees": {
                "bra": [0],
                "breasts": [0],
                "back": [0, 1],
                "belly": [0, 1],
                "underwear": [0, 1],
                "pussy": [0, 1],
                "anus": [0, 1]},
            "masturbation": {
                "bra": [0, 2],
                "breasts": [0, 2],
                "back": [0, 1, 2, 3],
                "belly": [0, 1, 2, 3],
                "underwear": [0, 1],
                "pussy": [0, 1],
                "anus": [0, 1]},
            "missionary": {
                "bra": [0, 2],
                "breasts": [0, 2],
                "back": [0, 1, 2, 3],
                "belly": [0, 1, 2, 3],
                "underwear": [0, 1],
                "pussy": [0, 1],
                "anus": [0, 1]}}
        hides = {
            "standing": {
                "bra": [0],
                "breasts": [0],
                "back": [0, 1],
                "belly": [0, 1],
                "underwear": [0, 1],
                "pussy": [0, 1],
                "anus": [0, 1]},
            "doggy": {
                "bra": [0, 2],
                "breasts": [0, 2],
                "back": [0, 2],
                "belly": [0, 2],
                "underwear": [0],
                "pussy": [0],
                "anus": [0]},
            "hands_and_knees": {
                "bra": [0],
                "breasts": [0],
                "back": [0, 1],
                "belly": [0, 1],
                "underwear": [0, 1],
                "pussy": [0, 1],
                "anus": [0, 1]},
            "masturbation": {
                "bra": [0, 2],
                "breasts": [0, 2],
                "back": [0, 1, 2, 3],
                "belly": [0, 1, 2, 3],
                "underwear": [0, 1],
                "pussy": [0, 1],
                "anus": [0, 1]},
            "missionary": {
                "bra": [0, 2],
                "breasts": [0, 2],
                "back": [0, 1, 2, 3],
                "belly": [0, 1, 2, 3],
                "underwear": [0, 1],
                "pussy": [0, 1],
                "anus": [0, 1]}}

        covered_by = {
            "black_dress": [0],
            "blackyellow_Wolverine_gloves": [0, 1],
            "blueyellow_Wolverine_gloves": [0, 1],
            "denim_jacket": [0],
            "leather_jacket": [0],
            "striped_shirt": [0],
            "towel": [0],
            "white_sweater": [0],
            "winter_coat": [0],
            "yellow_tanktop": [0]}
        blocked_by = {
            "black_athletic_shorts": [0, 1],
            "black_dress": [0, 1],
            "black_jeans": [0, 1],
            "black_shorts": [0, 1, 2],
            "blackyellow_Wolverine_gloves": [0, 1],
            "blueyellow_Wolverine_gloves": [0, 1],
            "denim_jacket": [0, 1],
            "leather_jacket": [0, 1],
            "leather_pants": [0, 1, 2],
            "striped_shirt": [0, 1],
            "towel": [0, 1],
            "white_sweater": [0, 1],
            "winter_coat": [0, 1],
            "Wolverine_belt": [0],
            "yellow_tanktop": [0, 1]}

        supports_breasts = False

        incompatibilities = [
            "black_corset",
            "blackred_corset"]

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

label Laura_leather_teddy_shopping_accept:
    $ Laura.change_face("confused1")

    ch_Laura "Well. . . I don't hate it."

    return

label Laura_leather_teddy_shopping_reject:
    $ Laura.change_face("confused1")

    ch_Laura "Definitely don't want whatever the hell that is."

    return

label Laura_leather_teddy_gift_accept:
    $ Laura.change_face("confused1")

    ch_Laura "You really want me to take this?"
    ch_Laura ". . . I guess."

    return

label Laura_leather_teddy_gift_reject:
    $ Laura.change_face("angry1")

    ch_Laura "I'm not taking. . . whatever that is. . ."

    return

label Laura_leather_teddy_change_private_before:

    return

label Laura_leather_teddy_change_private_after:
    $ Laura.change_face("perplexed", eyes = "down")

    ch_Laura "It's. . . not horrible."

    $ Laura.eyes = "neutral"

    return

label Laura_leather_teddy_change_public_before:

    return

label Laura_leather_teddy_change_public_after:
    $ Laura.change_face("sly")

    ch_Laura "Why is it called a teddy. . ."

    return