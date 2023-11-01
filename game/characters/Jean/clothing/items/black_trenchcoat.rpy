init -1 python:

    def Jean_black_trenchcoat():
        name = "black trenchcoat"
        short_name = "coat"
        string = "black_trenchcoat"

        Clothing_type = "jacket"

        shop_type = "clothing"
        chapter = 1
        season = 1

        thresholds = {
            "accept": [200, 175],
            "wear_in_private": [200, 175],
            "wear_in_public": [225, 200]}

        price = 3

        shame = [-15, -15]
        
        available_states = {
            "standing": [0, 1]}
        undressed_states = {
            "standing": 1}
        
        covers = {
            "standing": {
                "bra": [0],
                "breasts": [0],
                "back": [0, 1],
                "belly": [0],
                "thighs": [0],
                "underwear": [0],
                "ass": [0, 1],
                "pussy": [0],
                "anus": [0, 1]}}
        hides = {
            "standing": {
                "bra": [0],
                "breasts": [0],
                "back": [0, 1],
                "belly": [0],
                "thighs": [0],
                "underwear": [0],
                "ass": [0, 1],
                "pussy": [0],
                "anus": [0, 1]}}

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

label Jean_black_trenchcoat_shopping_accept:
    $ Jean.change_face("confused1")

    ch_Jean "I mean, not something I'd normally wear. . ."

    $ Jean.change_face("smirk2")

    ch_Jean "I can still rock it, though."

    return

label Jean_black_trenchcoat_shopping_reject:
    $ Jean.change_face("surprised2")

    pause 1.0

    $ Jean.change_face("confused1")

    ch_Jean "Uhm. . . a trenchcoat?"
    ch_Jean "Really?"

    return

label Jean_black_trenchcoat_gift_accept:
    $ Jean.change_face("surprised2")

    pause 1.0

    $ Jean.change_face("confused1")

    ch_Jean "A trenchcoat?"

    $ Jean.change_face("smirk2")

    ch_Jean "Eh, why not."

    return

label Jean_black_trenchcoat_gift_reject:
    $ Jean.change_face("confused2")

    ch_Jean "Why would you buy me a trenchcoat?"
    ch_Jean "Kinda weird. . ."

    return

label Jean_black_trenchcoat_change_private_before:

    return

label Jean_black_trenchcoat_change_private_after:
    $ Jean.change_face("smirk2", eyes = "down")

    ch_Jean "It's growing on me."

    $ Jean.eyes = "neutral"

    ch_Jean "Like it?"

    return

label Jean_black_trenchcoat_change_public_before:
    $ Jean.change_face("smirk2")

    ch_Jean "Someone's gotta be fashionable around here."

    return

label Jean_black_trenchcoat_change_public_after:

    return