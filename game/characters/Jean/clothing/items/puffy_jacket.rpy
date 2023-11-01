init -1 python:

    def Jean_puffy_jacket():
        name = "puffy jacket"
        short_name = "jacket"
        string = "puffy_jacket"

        Clothing_type = "jacket"

        shop_type = "clothing"
        chapter = 0
        season = 0

        thresholds = {
            "accept": [0, 0],
            "wear_in_private": [0, 0],
            "wear_in_public": [0, 0]}

        price = 0
        
        shame = [-2, -2]
        
        available_states = {
            "standing": [0, 1]}
        undressed_states = {
            "standing": 1}
        
        covers = {
            "standing": {
                "bra": [0],
                "breasts": [0],
                "back": [0]}}
        hides = {
            "standing": {
                "breasts": [0],
                "back": [0]}}

        covered_by = {
            "towel": [0]}
        blocked_by = {
            "towel": [0, 1]}

        supports_breasts = False

        incompatibilities = [
            "blue_gauntlets"]

        return ClothingClass(
            Jean, 
            name, short_name, string, Clothing_type, 
            shop_type, chapter, season,
            thresholds,
            price = int(price*work_unit*min(max(renpy.random.gauss(1.0, 0.15), 0.85), 1.15)), shame = shame, 
            available_states = available_states, undressed_states = undressed_states,
            covers = covers, hides = hides, 
            covered_by = covered_by, blocked_by = blocked_by,
            supports_breasts = supports_breasts,
            incompatibilities = incompatibilities)

label Jean_puffy_jacket_shopping_accept:

    return

label Jean_puffy_jacket_shopping_reject:

    return

label Jean_puffy_jacket_gift_accept:

    return

label Jean_puffy_jacket_gift_reject:

    return

label Jean_puffy_jacket_change_private_before:

    return

label Jean_puffy_jacket_change_private_after:
    $ Jean.change_face("smirk2")

    ch_Jean "Cute and warm. . ."

    return

label Jean_puffy_jacket_change_public_before:

    return

label Jean_puffy_jacket_change_public_after:
    $ Jean.change_face("smirk2")

    ch_Jean "Cute and warm. . ."

    return