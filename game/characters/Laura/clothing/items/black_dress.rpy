init -1 python:

    def Laura_black_dress():
        name = "black dress"
        short_name = "dress"
        string = "black_dress"
        
        Clothing_type = "dress"

        shop_type = "clothing"
        chapter = 1
        season = 3

        thresholds = {
            "accept": [600, 625],
            "wear_in_private": [600, 625],
            "wear_in_public": [625, 650]}
        
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
                "thighs": [0, 1],
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
            "striped_shirt": [0, 1],
            "towel": [0],
            "white_sweater": [0, 1],
            "yellow_tanktop": [0, 1]}
        blocked_by = {
            "towel": [0, 1],
            "striped_shirt": [0, 1],
            "white_sweater": [0, 1],
            "yellow_tanktop": [0, 1]}

        supports_breasts = False
        
        incompatibilities = [
            "red_skirt",
            "striped_shirt",
            "white_sweater",
            "yellow_tanktop"]
        
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

label Laura_black_dress_shopping_accept:
    $ Laura.change_face("pleased2")

    ch_Laura "I guess it does look nice. . . if a bit restrictive."

    return

label Laura_black_dress_shopping_reject:
    $ Laura.change_face("confused1")

    ch_Laura "Why would I wear something so restrictive?"

    return

label Laura_black_dress_gift_accept:
    $ Laura.change_face("pleased1")

    ch_Laura "How'd you get the size right?"

    $ Laura.change_face("smirk2")

    ch_Laura "It is nice. . ."

    return

label Laura_black_dress_gift_reject:
    $ Laura.change_face("angry1")

    ch_Laura "Who said you could buy clothes for me?"

    return

label Laura_black_dress_change_private_before:
    $ Laura.change_face("confused1", eyes = "down")

    ch_Laura "Kinda hard to move around. . ."

    $ Laura.eyes = "neutral"

    ch_Laura "I don't hate it. . ."

    return

label Laura_black_dress_change_private_after:

    return

label Laura_black_dress_change_public_before:
    $ Laura.change_face("smirk2")

    ch_Laura "Fancy, huh?"

    return

label Laura_black_dress_change_public_after:

    return