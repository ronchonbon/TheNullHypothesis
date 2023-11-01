init -1 python:

    def Laura_blueyellow_Wolverine_boots():
        name = "blue-and-yellow Wolverine boots"
        short_name = "boots"
        string = "blueyellow_Wolverine_boots"
        
        Clothing_type = "boots"

        shop_type = "clothing"
        chapter = 1
        season = 4

        thresholds = {
            "accept": [250, 275],
            "wear_in_private": [250, 275],
            "wear_in_public": [275, 300]}

        price = 2

        shame = [0, 0]
        
        available_states = {
            "standing": [0]}
        undressed_states = {
            "standing": 0}
        
        covers = {
            "standing": {
                "feet": [0]}}
        hides = {
            "standing": {
                "feet": [0]}}

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

label Laura_blueyellow_Wolverine_boots_shopping_accept:
    $ Laura.change_face("neutral")

    ch_Laura "I guess more options can't hurt."

    return

label Laura_blueyellow_Wolverine_boots_shopping_reject:
    $ Laura.change_face("confused1")

    ch_Laura "Already have a pair."

    return

label Laura_blueyellow_Wolverine_boots_gift_accept:
    $ Laura.change_face("neutral")

    ch_Laura "Thanks, I do like the colors."

    return

label Laura_blueyellow_Wolverine_boots_gift_reject:
    $ Laura.change_face("confused1")

    ch_Laura "Don't need 'em."
    ch_Laura "My current pair is perfectly fine."

    return

label Laura_blueyellow_Wolverine_boots_change_private_before:

    return

label Laura_blueyellow_Wolverine_boots_change_private_after:
    $ Laura.change_face("confused1", eyes = "down")

    ch_Laura "How did they perfectly match my other pair?"

    $ Laura.eyes = "neutral"

    ch_Laura "Those were custom. . ."

    return

label Laura_blueyellow_Wolverine_boots_change_public_before:
    $ Laura.change_face("neutral")

    ch_Laura "Why not."

    return

label Laura_blueyellow_Wolverine_boots_change_public_after:

    return