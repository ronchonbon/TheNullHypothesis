init -1 python:

    def Jean_white_sweater():
        name = "white sweater"
        short_name = "sweater"
        string = "white_sweater"
        
        Clothing_type = "top"

        shop_type = "clothing"
        chapter = 0
        season = 0
        
        thresholds = {
            "accept": [0, 0],
            "wear_in_private": [0, 0],
            "wear_in_public": [0, 0]}
        
        price = 0
        
        shame = [-15, -15]
        
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
            "black_trenchcoat": [0],
            "denim_jacket": [0],
            "puffy_jacket": [0],
            "towel": [0]}
        blocked_by = {
            "black_trenchcoat": [0, 1],
            "denim_jacket": [0, 1],
            "puffy_jacket": [0, 1],
            "towel": [0]}

        supports_breasts = False
        
        incompatibilities = []
        
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

label Jean_white_sweater_shopping_accept:

    return

label Jean_white_sweater_shopping_reject:

    return

label Jean_white_sweater_gift_accept:

    return

label Jean_white_sweater_gift_reject:

    return

label Jean_white_sweater_change_private_before:
    $ Jean.change_face("smirk2")

    ch_Jean "Think I look good in a sweater?"

    return

label Jean_white_sweater_change_private_after:

    return

label Jean_white_sweater_change_public_before:
    $ Jean.change_face("smirk2")

    ch_Jean "Think I look good in a sweater?"

    return

label Jean_white_sweater_change_public_after:

    return