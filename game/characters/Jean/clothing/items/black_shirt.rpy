init -1 python:

    def Jean_black_shirt():
        name = "black shirt"
        short_name = "shirt"
        string = "black_shirt"
        
        Clothing_type = "top"

        shop_type = "clothing"
        chapter = 1
        season = 1
        
        thresholds = {
            "accept": [200, 175],
            "wear_in_private": [200, 175],
            "wear_in_public": [225, 200]}
        
        price = 3

        shame = [-10, -10]
        
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

label Jean_black_shirt_shopping_accept:
    $ Jean.change_face("pleased2")

    ch_Jean "It's not what I'd normally wear. . . but I can rock it."

    return

label Jean_black_shirt_shopping_reject:
    $ Jean.change_face("surprised2")

    ch_Jean "I don't. . . really wear black. . ."

    return

label Jean_black_shirt_gift_accept:
    $ Jean.change_face("surprised2")

    pause 1.0

    $ Jean.change_face("smirk2")

    ch_Jean "Think I'd look good in black?"
    ch_Jean "Sure, I'll try it out."

    return

label Jean_black_shirt_gift_reject:
    $ Jean.change_face("confused2")

    ch_Jean "Why are you buying me clothes. . . ?"

    return

label Jean_black_shirt_change_private_before:

    return

label Jean_black_shirt_change_private_after:
    $ Jean.change_face("smirk2", eyes = "down")

    ch_Jean "You like it?"

    $ Jean.eyes = "neutral"

    ch_Jean "Right?"

    return

label Jean_black_shirt_change_public_before:

    return

label Jean_black_shirt_change_public_after:
    $ Jean.change_face("smirk2")

    ch_Jean "I look hot even in a turtleneck, right?"

    return