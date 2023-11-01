init -1 python:

    def Jean_black_pants():
        name = "black pants"
        short_name = "pants"
        string = "black_pants"

        Clothing_type = "pants"

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
            "standing": [0, 1, 2]}
        undressed_states = {
            "standing": 2}
        
        covers = {
            "standing": {
                "thighs": [0, 1],
                "underwear": [0, 1],
                "ass": [0, 1],
                "pussy": [0, 1],
                "anus": [0, 1]}}
        hides = {
            "standing": {
                "thighs": [0, 1],
                "underwear": [0],
                "ass": [0, 1],
                "pussy": [0, 1],
                "anus": [0, 1]}}

        covered_by = {
            "blue_boots": [0]}
        blocked_by = {
            "blue_boots": [0]}

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

label Jean_black_pants_shopping_accept:
    $ Jean.change_face("pleased2")

    ch_Jean "I can make these work."

    return

label Jean_black_pants_shopping_reject:
    $ Jean.change_face("surprised2")

    pause 1.0

    $ Jean.change_face("confused1")

    ch_Jean "Why are you trying to buy me pants. . . ?"

    return

label Jean_black_pants_gift_accept:
    $ Jean.change_face("surprised2")

    ch_Jean "I don't mind these. . ."

    $ Jean.change_face("confused1")

    ch_Jean "How'd you get the size right?"

    return

label Jean_black_pants_gift_reject:
    $ Jean.change_face("confused2")

    ch_Jean "Why would you buy me. . . pants?"
    ch_Jean "Weird. . ."

    return

label Jean_black_pants_change_private_before:

    return

label Jean_black_pants_change_private_after:
    $ Jean.change_face("smirk2", eyes = "down")

    ch_Jean "They look good."

    $ Jean.eyes = "neutral"

    return

label Jean_black_pants_change_public_before:

    return

label Jean_black_pants_change_public_after:
    $ Jean.change_face("smirk2")

    ch_Jean "Like how they show off my. . . ass?"

    return