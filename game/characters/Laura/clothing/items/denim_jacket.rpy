init -1 python:

    def Laura_denim_jacket():
        name = "denim jacket"
        short_name = "jacket"
        string = "denim_jacket"

        Clothing_type = "jacket"

        shop_type = "clothing"
        chapter = 0
        season = 0

        thresholds = {
            "accept": [0, 0],
            "wear_in_private": [0, 0],
            "wear_in_public": [0, 0]}

        price = 0

        shame = [-5, -5]
        
        available_states = {
            "standing": [0, 1]}
        undressed_states = {
            "standing": 1}
        
        covers = {
            "standing": {
                "back": [0]}}
        hides = {
            "standing": {
                "back": [0]}}

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

label Laura_denim_jacket_shopping_accept:

    return

label Laura_denim_jacket_shopping_reject:

    return

label Laura_denim_jacket_gift_accept:

    return

label Laura_denim_jacket_gift_reject:

    return

label Laura_denim_jacket_change_private_before:

    return

label Laura_denim_jacket_change_private_after:
    $ Laura.change_face("confused1")

    ch_Laura "I know the leaf on a flag is pretty dumb."

    $ Laura.change_face("neutral")

    ch_Laura "But the jacket is nice."

    return

label Laura_denim_jacket_change_public_before:

    return

label Laura_denim_jacket_change_public_after:
    $ Laura.change_face("confused1")

    ch_Laura "I know the leaf on a flag is pretty dumb."

    $ Laura.change_face("neutral")

    ch_Laura "But the jacket is nice."

    return