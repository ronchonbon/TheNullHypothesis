init -1 python:

    def Laura_winter_coat():
        name = "winter coat"
        short_name = "coat"
        string = "winter_coat"

        Clothing_type = "jacket"

        shop_type = "clothing"
        chapter = 0
        season = 0

        thresholds = {
            "accept": [0, 0],
            "wear_in_private": [0, 0],
            "wear_in_public": [0, 0]}

        price = 0

        shame = [-10, -10]
        
        available_states = {
            "standing": [0, 1]}
        undressed_states = {
            "standing": 1}
        
        covers = {
            "standing": {}}
        hides = {
            "standing": {}}

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

label Laura_winter_coat_shopping_accept:

    return

label Laura_winter_coat_shopping_reject:

    return

label Laura_winter_coat_gift_accept:

    return

label Laura_winter_coat_gift_reject:

    return

label Laura_winter_coat_change_private_before:

    return

label Laura_winter_coat_change_private_after:
    $ Laura.change_face("neutral")

    ch_Laura "Comfy."

    return

label Laura_winter_coat_change_public_before:

    return

label Laura_winter_coat_change_public_after:
    $ Laura.change_face("neutral")

    ch_Laura "Comfy."

    return