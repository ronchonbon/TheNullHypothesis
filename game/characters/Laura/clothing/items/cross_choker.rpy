init -1 python:

    def Laura_cross_choker():
        name = "cross choker"
        short_name = "choker"
        string = "cross_choker"
        
        Clothing_type = "neck"

        shop_type = "clothing"
        chapter = 0
        season = 0

        thresholds = {
            "accept": [0, 0],
            "wear_in_private": [0, 0],
            "wear_in_public": [0, 0]}
        
        price = 0
        
        shame = [5, 5]
        
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

label Laura_cross_choker_shopping_accept:
    $ Laura.change_face("confused1")

    ch_Laura "So it's just a necklace, but tighter?"
    ch_Laura "Why?"

    return

label Laura_cross_choker_shopping_reject:
    $ Laura.change_face("confused1")

    ch_Laura "The hell even is a choker?"

    return

label Laura_cross_choker_gift_accept:
    $ Laura.change_face("confused1")

    ch_Laura "Thanks. . . I still don't get it."

    return

label Laura_cross_choker_gift_reject:
    $ Laura.change_face("angry1")

    ch_Laura "Why would I wear something that chokes me?"

    return

label Laura_cross_choker_change_private_before:

    return

label Laura_cross_choker_change_private_after:
    $ Laura.change_face("confused1", eyes = "down")

    ch_Laura "It's not terrible. Goes with leather. . ."

    $ Laura.eyes = "neutral"

    ch_Laura "Still don't understand the point over normal necklaces."

    return

label Laura_cross_choker_change_public_before:
    $ Laura.change_face("smirk2")

    ch_Laura "Fine, weirdo."

    return

label Laura_cross_choker_change_public_after:

    return