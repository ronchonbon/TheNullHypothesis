init -1 python:

    def Jean_blue_pleated_skirt():
        name = "blue pleated skirt"
        short_name = "skirt"
        string = "blue_pleated_skirt"

        Clothing_type = "skirt"

        shop_type = "clothing"
        chapter = 0
        season = 0

        thresholds = {
            "accept": [0, 0],
            "wear_in_private": [0, 0],
            "wear_in_public": [0, 0]}

        price = 0

        shame = [10, 10]
        
        available_states = {
            "standing": [0, 1]}
        undressed_states = {
            "standing": 1}

        covers = {
            "standing": {
                "thighs": [0],
                "underwear": [0],
                "ass": [0],
                "pussy": [0],
                "anus": [0]}}
        hides = {
            "standing": {
                "underwear": [0],
                "ass": [0],
                "pussy": [0],
                "anus": [0]}}

        covered_by = {}
        blocked_by = {}

        supports_breasts = False

        incompatibilities = [
            "black_pants",
            "blue_nighty",
            "khaki_pants",
            "yellow_dress"]

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

label Jean_blue_pleated_skirt_shopping_accept:

    return

label Jean_blue_pleated_skirt_shopping_reject:

    return

label Jean_blue_pleated_skirt_gift_accept:

    return

label Jean_blue_pleated_skirt_gift_reject:

    return

label Jean_blue_pleated_skirt_change_private_before:
    $ Jean.change_face("smirk2")

    ch_Jean "I look amazing in a skirt."

    return

label Jean_blue_pleated_skirt_change_private_after:

    return

label Jean_blue_pleated_skirt_change_public_before:
    $ Jean.change_face("smirk2")

    ch_Jean "I look amazing in a skirt."

    return

label Jean_blue_pleated_skirt_change_public_after:

    return