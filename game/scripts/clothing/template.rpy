init -1 python:

    def Clothing_template():
        name = "lace panties"
        short_name = "panties"
        string = "lace_panties"

        Clothing_type = "underwear"

        shop_type = "lingerie"
        chapter = 0
        season = 0

        thresholds = {
            "accept": [0, 0],
            "wear_in_private": [0, 0],
            "wear_in_public": [0, 0]}

        price = 50

        shame = [0, 0]

        available_states = {
            "standing": [0, 1]}
        undressed_states = {
            "standing": [1]}

        covers = {
            "standing": {
                "ass": [0],
                "pussy": [0]}}
        hides = {
            "standing": {
                "ass": [0],
                "pussy": [0]}}

        covered_by = {
            "blue_pants": [0]}
        blocked_by = {
            "blue_pants": [0, 1]}

        supports_breasts = False
        
        incompatibilities = [
            "green_jacket"]

        return ClothingClass(
            Character, 
            name, short_name, string, Clothing_type, 
            shop_type, chapter, season,
            thresholds,
            price = int(price*work_unit*min(max(renpy.random.gauss(1.0, 0.15), 0.85), 1.15)), shame = shame, 
            available_states = available_states, undressed_states = undressed_states,
            covers = covers, hides = hides, 
            covered_by = covered_by, blocked_by = blocked_by,
            supports_breasts = supports_breasts,
            incompatibilities = incompatibilities)

label Character_string_shopping_accept:

    return

label Character_string_shopping_reject:

    return

label Character_string_gift_accept:

    return

label Character_string_gift_reject:

    return

label Character_string_change_private_before:

    return

label Character_string_change_private_after:

    return

label Character_string_change_public_before:

    return

label Character_string_change_public_after:

    return
