init -1 python:

    def Laura_combat_boots():
        name = "combat boots"
        short_name = "boots"
        string = "combat_boots"
        
        Clothing_type = "boots"

        shop_type = "clothing"
        chapter = 1
        season = 1

        thresholds = {
            "accept": [150, 175],
            "wear_in_private": [150, 175],
            "wear_in_public": [175, 200]}
        
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

label Laura_combat_boots_shopping_accept:
    $ Laura.change_face("confused1")

    ch_Laura "They do look sturdy."

    $ Laura.change_face("neutral")

    ch_Laura "Maybe they won't wear out so quickly."

    return

label Laura_combat_boots_shopping_reject:
    $ Laura.change_face("confused1")

    ch_Laura "Already have boots."

    return

label Laura_combat_boots_gift_accept:
    $ Laura.change_face("confused1")

    ch_Laura "Thanks, they look like a good backup pair."

    return

label Laura_combat_boots_gift_reject:
    $ Laura.change_face("confused1")

    ch_Laura "Why would you buy me new boots?"
    ch_Laura "My current ones aren't even worn out yet."

    return

label Laura_combat_boots_change_private_before:

    return

label Laura_combat_boots_change_private_after:
    $ Laura.change_face("confused1", eyes = "down")

    ch_Laura "These are comfortable."

    $ Laura.eyes = "neutral"

    return

label Laura_combat_boots_change_public_before:
    $ Laura.change_face("smirk2")

    ch_Laura "Good thing you got me these."
    ch_Laura "Wore my other ones out already."

    return

label Laura_combat_boots_change_public_after:

    return