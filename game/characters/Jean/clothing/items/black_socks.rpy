init -1 python:

    def Jean_black_socks():
        name = "black socks"
        short_name = "socks"
        string = "black_socks"
        
        Clothing_type = "socks"

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
            "standing": [0],
            "doggy": [0],
            "hands_and_knees": [0],
            "masturbation": [0],
            "missionary": [0]}
        undressed_states = {
            "standing": 0,
            "doggy": 0,
            "hands_and_knees": 0,
            "masturbation": 0,
            "missionary": 0}
        
        covers = {
            "standing": {
                "feet": [0]},
            "doggy": {
                "feet": [0]},
            "hands_and_knees": {
                "feet": [0]},
            "masturbation": {
                "feet": [0]},
            "missionary": {
                "feet": [0]}}
        hides = {
            "standing": {
                "feet": [0]},
            "doggy": {
                "feet": [0]},
            "hands_and_knees": {
                "feet": [0]},
            "masturbation": {
                "feet": [0]},
            "missionary": {
                "feet": [0]}}

        covered_by = {
            "black_pants": [0, 1],
            "blue_boots": [0],
            "Jean_suit": [0, 1],
            "khaki_pants": [0, 1]}
        blocked_by = {
            "black_pants": [0, 1],
            "blue_boots": [0],
            "Jean_suit": [0, 1],
            "khaki_pants": [0, 1]}

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

label Jean_black_socks_shopping_accept:

    return

label Jean_black_socks_shopping_reject:

    return

label Jean_black_socks_gift_accept:

    return

label Jean_black_socks_gift_reject:

    return

label Jean_black_socks_change_private_before:

    return

label Jean_black_socks_change_private_after:
    $ Jean.change_face("smirk2")

    ch_Jean "Like how they make my legs look?"

    return

label Jean_black_socks_change_public_before:

    return

label Jean_black_socks_change_public_after:
    $ Jean.change_face("smirk2")

    ch_Jean "Like how they make my legs look?"

    return