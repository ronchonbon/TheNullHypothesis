init -1 python:

    def Laura_yellow_tanktop():
        name = "yellow tanktop"
        short_name = "tanktop"
        string = "yellow_tanktop"
        
        Clothing_type = "top"

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
            "standing": [0, 1],
            "doggy": [0, 1],
            "hands_and_knees": [0, 1],
            "masturbation": [0, 1],
            "missionary": [0, 1]}
        undressed_states = {
            "standing": 1,
            "doggy": 1,
            "hands_and_knees": 1,
            "masturbation": 1,
            "missionary": 1}
        
        covers = {
            "standing": {
                "breasts": [0]},
            "doggy": {
                "breasts": [0]},
            "hands_and_knees": {
                "breasts": [0]},
            "masturbation": {
                "breasts": [0]},
            "missionary": {
                "breasts": [0]}}
        hides = {
            "standing": {
                "breasts": [0]},
            "doggy": {
                "breasts": [0]},
            "hands_and_knees": {
                "breasts": [0]},
            "masturbation": {
                "breasts": [0]},
            "missionary": {
                "breasts": [0]}}

        covered_by = {
            "denim_jacket": [0],
            "leather_jacket": [0],
            "towel": [0],
            "winter_coat": [0]}
        blocked_by = {
            "denim_jacket": [0, 1],
            "leather_jacket": [0, 1],
            "towel": [0],
            "winter_coat": [0, 1]}

        supports_breasts = True
        
        incompatibilities = [
            "black_bikini_top",
            "black_cage_bra",
            "black_corset",
            "black_dress",
            "blackred_corset",
            "white_tanktop",
            "yellow_sports_bra"]
        
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

label Laura_yellow_tanktop_shopping_accept:

    return

label Laura_yellow_tanktop_shopping_reject:

    return

label Laura_yellow_tanktop_gift_accept:

    return

label Laura_yellow_tanktop_gift_reject:

    return

label Laura_yellow_tanktop_change_private_before:

    return

label Laura_yellow_tanktop_change_private_after:

    return

label Laura_yellow_tanktop_change_public_before:

    return

label Laura_yellow_tanktop_change_public_after:

    return