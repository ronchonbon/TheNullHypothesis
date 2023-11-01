init -1 python:

    def Jean_blue_nighty():
        name = "blue nighty"
        short_name = "nighty"
        string = "blue_nighty"
        
        Clothing_type = "dress"

        shop_type = "lingerie"
        chapter = 1
        season = 4
        
        thresholds = {
            "accept": [675, 625],
            "wear_in_private": [675, 625],
            "wear_in_public": [700, 650]}
        
        price = 5
        
        shame = [35, 35]
        
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
            "blue_pleated_skirt"]
        
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

label Jean_blue_nighty_shopping_accept:
    $ Jean.change_face("surprised1")

    ch_Jean "I guess it is a pretty color. . ."

    return

label Jean_blue_nighty_shopping_reject:
    $ Jean.change_face("confused2")

    ch_Jean "I'm not wearing something like that to bed. . ."

    return

label Jean_blue_nighty_gift_accept:
    $ Jean.change_face("smirk2")

    ch_Jean "I bet you'd love to see me sleep in that."

    return

label Jean_blue_nighty_gift_reject:
    $ Jean.change_face("appalled1")

    ch_Jean "Really?"
    ch_Jean "What makes you think you should be buying me stuff like that?"

    return

label Jean_blue_nighty_change_private_before:

    return

label Jean_blue_nighty_change_private_after:
    $ Jean.change_face("surprised1", eyes = "down")

    ch_Jean "It's surprisingly comfortable."

    $ Jean.change_face("smirk2")

    ch_Jean "Makes me look great too."

    return

label Jean_blue_nighty_change_public_before:

    return

label Jean_blue_nighty_change_public_after:
    $ Jean.change_face("smirk2")

    ch_Jean "You like this one too?"

    return