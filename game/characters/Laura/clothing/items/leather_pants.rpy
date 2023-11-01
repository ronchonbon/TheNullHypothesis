init -1 python:

    def Laura_leather_pants():
        name = "leather pants"
        short_name = "pants"
        string = "leather_pants"

        Clothing_type = "pants"

        shop_type = "clothing"
        chapter = 0
        season = 0

        thresholds = {
            "accept": [0, 0],
            "wear_in_private": [0, 0],
            "wear_in_public": [0, 0]}

        price = 0

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
            "Wolverine_belt": [0]}
        blocked_by = {
            "blackyellow_Wolverine_boots": [0],
            "blueyellow_Wolverine_boots": [0],
            "combat_boots": [0],
            "thighhigh_boots": [0],
            "Wolverine_belt": [0]}

        supports_breasts = False

        incompatibilities = [
            "red_skirt"]

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

label Laura_leather_pants_shopping_accept:

    return

label Laura_leather_pants_shopping_reject:

    return

label Laura_leather_pants_gift_accept:

    return

label Laura_leather_pants_gift_reject:

    return

label Laura_leather_pants_change_private_before:
    $ Laura.change_face("smirk2")

    ch_Laura "Leather, cool."

    return

label Laura_leather_pants_change_private_after:

    return

label Laura_leather_pants_change_public_before:
    $ Laura.change_face("smirk2")

    ch_Laura "Leather, cool."

    return

label Laura_leather_pants_change_public_after:

    return