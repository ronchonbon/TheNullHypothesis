init -1 python:

    def Laura_blueyellow_Wolverine_suit():
        name = "blue-and-yellow Wolverine suit"
        short_name = "suit"
        string = "blueyellow_Wolverine_suit"

        Clothing_type = "bodysuit"

        shop_type = "clothing"
        chapter = 1
        season = 4

        thresholds = {
            "accept": [250, 275],
            "wear_in_private": [250, 275],
            "wear_in_public": [275, 300]}

        price = 6

        shame = [-10, -10]
        
        available_states = {
            "standing": [0, 1]}
        undressed_states = {
            "standing": 1}
        
        covers = {
            "standing": {
                "bra": [0],
                "breasts": [0],
                "back": [0, 1],
                "belly": [0, 1],
                "thighs": [0, 1],
                "underwear": [0, 1],
                "ass": [0, 1],
                "pussy": [0, 1],
                "anus": [0, 1]}}
        hides = {
            "standing": {
                "bra": [0],
                "breasts": [0],
                "back": [0, 1],
                "belly": [0, 1],
                "thighs": [0, 1],
                "underwear": [0, 1],
                "ass": [0, 1],
                "pussy": [0, 1],
                "anus": [0, 1]}}

        covered_by = {
            "black_dress": [0, 1],
            "blackyellow_Wolverine_gloves": [0, 1],
            "blueyellow_Wolverine_gloves": [0, 1],
            "denim_jacket": [0],
            "leather_jacket": [0],
            "striped_shirt": [0, 1],
            "towel": [0, 1],
            "white_sweater": [0, 1],
            "winter_coat": [0],
            "yellow_tanktop": [0, 1]}
        blocked_by = {
            "black_athletic_shorts": [0, 1],
            "black_dress": [0, 1],
            "black_jeans": [0, 1],
            "black_shorts": [0, 1, 2],
            "blackyellow_Wolverine_boots": [0],
            "blackyellow_Wolverine_gloves": [0, 1],
            "blueyellow_Wolverine_boots": [0],
            "blueyellow_Wolverine_gloves": [0, 1],
            "combat_boots": [0],
            "denim_jacket": [0, 1],
            "leather_jacket": [0, 1],
            "leather_pants": [0, 1, 2],
            "striped_shirt": [0, 1],
            "thighhigh_boots": [0],
            "towel": [0, 1],
            "white_sweater": [0, 1],
            "winter_coat": [0, 1],
            "Wolverine_belt": [0],
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

label Laura_blueyellow_Wolverine_suit_shopping_accept:
    $ Laura.change_face("confused1")

    ch_Laura "I don't mind the blue. . ."

    return

label Laura_blueyellow_Wolverine_suit_shopping_reject:
    $ Laura.change_face("perplexed")

    ch_Laura "Why would I need it in a different color?"
    ch_Laura "And how do they even have this?! Mine was custom-made. . ."

    return

label Laura_blueyellow_Wolverine_suit_gift_accept:
    $ Laura.change_face("confused1")

    ch_Laura "Thanks . . How did you even get this? Mine was custom. . ."

    return

label Laura_blueyellow_Wolverine_suit_gift_reject:
    $ Laura.change_face("confused1")

    ch_Laura "I already have basically the same thing."

    return

label Laura_blueyellow_Wolverine_suit_change_private_before:

    return

label Laura_blueyellow_Wolverine_suit_change_private_after:
    $ Laura.change_face("confused1", eyes = "down")

    ch_Laura "Fits perfectly."

    return

label Laura_blueyellow_Wolverine_suit_change_public_before:
    $ Laura.change_face("smirk2")

    ch_Laura "Blue and yellow is a good look."

    return

label Laura_blueyellow_Wolverine_suit_change_public_after:

    return