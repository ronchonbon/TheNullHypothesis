init -1 python:

    def Laura_cross_necklace():
        name = "cross necklace"
        short_name = "necklace"
        string = "cross_necklace"
        
        Clothing_type = "neck"

        shop_type = "clothing"
        chapter = 0
        season = 0

        thresholds = {
            "accept": [0, 0],
            "wear_in_private": [0, 0],
            "wear_in_public": [0, 0]}
        
        price = 0
        
        shame = [0, 0]
        
        available_states = {
            "standing": [0]}
        undressed_states = {
            "standing": 0}
        
        covers = {
            "standing": {}}
        hides = {
            "standing": {}}

        covered_by = {}
        blocked_by = {}

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

label Laura_cross_necklace_shopping_accept:
    $ Laura.change_face("neutral")

    ch_Laura "Fine, I'll take it."

    return

label Laura_cross_necklace_shopping_reject:
    $ Laura.change_face("confused1")

    ch_Laura "Why do I need a necklace?"

    return

label Laura_cross_necklace_gift_accept:
    $ Laura.change_face("neutral")

    ch_Laura "I guess it would look good. . ."

    return

label Laura_cross_necklace_gift_reject:
    $ Laura.change_face("confused1")

    ch_Laura "A necklace? Nah."

    return

label Laura_cross_necklace_change_private_before:

    return

label Laura_cross_necklace_change_private_after:
    $ Laura.change_face("confused1", eyes = "down")

    ch_Laura "I actually don't mind it. . ."

    $ Laura.eyes = "neutral"

    return

label Laura_cross_necklace_change_public_before:

    return

label Laura_cross_necklace_change_public_after:
    $ Laura.change_face("neutral")

    ch_Laura "Actually kinda like this one. . ."

    return