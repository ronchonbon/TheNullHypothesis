init -1 python:

    def Jean_yellow_dress():
        name = "yellow dress"
        short_name = "dress"
        string = "yellow_dress"
        
        Clothing_type = "dress"

        shop_type = "clothing"
        chapter = 1
        season = 3
        
        thresholds = {
            "accept": [650, 600],
            "wear_in_private": [650, 600],
            "wear_in_public": [675, 625]}
        
        price = 7
        
        shame = [25, 25]
        
        available_states = {
            "standing": [0, 1]}
        undressed_states = {
            "standing": 1}
        
        covers = {
            "standing": {
                "bra": [0],
                "breasts": [0],
                "back": [0, 1],
                "belly": [0, 1],
                "underwear": [0, 1],
                "ass": [0, 1],
                "pussy": [0, 1],
                "anus": [0, 1]}}
        hides = {
            "standing": {
                "bra": [0],
                "breasts": [0],
                "back": [0, 1],
                "belly": [0, 1],
                "underwear": [0, 1],
                "ass": [0, 1],
                "pussy": [0, 1],
                "anus": [0, 1]}}

        covered_by = {
            "black_shirt": [0],
            "college_shirt": [0],
            "pink_shirt": [0],
            "white_cami": [0],
            "white_sweater": [0]}
        blocked_by = {
            "black_shirt": [0, 1],
            "college_shirt": [0, 1],
            "pink_shirt": [0, 1],
            "white_cami": [0, 1],
            "white_sweater": [0, 1]}

        supports_breasts = False
        
        incompatibilities = [
            "blue_pleated_skirt",
            "white_cami"]
        
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

label Jean_yellow_dress_shopping_accept:
    $ Jean.change_face("pleased2")

    ch_Jean "That's actually really cute, good choice."

    return

label Jean_yellow_dress_shopping_reject:
    $ Jean.change_face("surprised2")

    ch_Jean "Uhm. . . I don't think you should be buying me dresses."

    return

label Jean_yellow_dress_gift_accept:
    $ Jean.change_face("surprised2")

    ch_Jean "Wow, I love this!"
    ch_Jean "You have good taste."

    return

label Jean_yellow_dress_gift_reject:
    $ Jean.change_face("confused2")

    ch_Jean "Why would you buy me a dress?"
    ch_Jean "Kinda weird. . ."

    return

label Jean_yellow_dress_change_private_before:

    return

label Jean_yellow_dress_change_private_after:
    $ Jean.change_face("smirk2", eyes = "down")

    ch_Jean "God, I look fantastic."

    $ Jean.eyes = "neutral"

    return

label Jean_yellow_dress_change_public_before:

    return

label Jean_yellow_dress_change_public_after:
    $ Jean.change_face("smirk2")

    ch_Jean "Doesn't it look amazing?"

    return