init -1 python:

    def Laura_leather_jacket():
        name = "leather jacket"
        short_name = "jacket"
        string = "leather_jacket"

        Clothing_type = "jacket"

        shop_type = "clothing"
        chapter = 1
        season = 1

        thresholds = {
            "accept": [175, 200],
            "wear_in_private": [175, 200],
            "wear_in_public": [200, 225]}

        price = 4

        shame = [-5, -5]
        
        available_states = {
            "standing": [0, 1]}
        undressed_states = {
            "standing": 1}
        
        covers = {
            "standing": {
                "bra": [0],
                "breasts": [0],
                "back": [0],
                "belly": [0]}}
        hides = {
            "standing": {
                "bra": [0],
                "breasts": [0],
                "back": [0],
                "belly": [0]}}

        covered_by = {
            "towel": [0]}
        blocked_by = {
            "towel": [0]}

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

label Laura_leather_jacket_shopping_accept:
    $ Laura.change_face("pleased1")

    ch_Laura "You know I like leather. . ."

    return

label Laura_leather_jacket_shopping_reject:
    $ Laura.change_face("confused1")

    ch_Laura "You're trying to buy me clothes?"
    ch_Laura "Stop it."

    return

label Laura_leather_jacket_gift_accept:
    $ Laura.change_face("smirk2")

    ch_Laura "Yeah, I would wear this."

    return

label Laura_leather_jacket_gift_reject:
    $ Laura.change_face("angry1")

    ch_Laura "Why would you buy me a jacket?"

    return

label Laura_leather_jacket_change_private_before:

    return

label Laura_leather_jacket_change_private_after:
    $ Laura.change_face("perplexed", eyes = "down")

    ch_Laura "You like it?"

    $ Laura.eyes = "neutral"

    ch_Laura "I do."

    return

label Laura_leather_jacket_change_public_before:
    $ Laura.change_face("neutral")

    ch_Laura "Good choice. . ."

    return

label Laura_leather_jacket_change_public_after:

    return