init -1 python:

    def Rogue_green_athletic_shorts():
        name = "green athletic shorts"
        short_name = "shorts"
        string = "green_athletic_shorts"

        Clothing_type = "pants"

        shop_type = "clothing"
        chapter = 1
        season = 2

        thresholds = {
            "accept": [175, 175],
            "wear_in_private": [175, 175],
            "wear_in_public": [200, 200]}

        price = 2

        shame = [5, 5]
        
        available_states = {
            "standing": [0, 1]}
        undressed_states = {
            "standing": 1}
        
        covers = {
            "standing": {
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

        incompatibilities = []

        return ClothingClass(
            Rogue, 
            name, short_name, string, Clothing_type, 
            shop_type, chapter, season,
            thresholds,
            price = int(price*work_unit*min(max(renpy.random.gauss(1.0, 0.15), 0.85), 1.15)), shame = shame, 
            available_states = available_states, undressed_states = undressed_states,
            covers = covers, hides = hides, 
            covered_by = covered_by, blocked_by = blocked_by,
            supports_breasts = supports_breasts,
            incompatibilities = incompatibilities)

label Rogue_green_athletic_shorts_shopping_accept:
    $ Rogue.change_face("pleased2")

    ch_Rogue "Some comfy shorts? Good call."

    return

label Rogue_green_athletic_shorts_shopping_reject:
    $ Rogue.change_face("worried1")

    ch_Rogue "Ah can pick out my own clothes, thank you."

    return

label Rogue_green_athletic_shorts_gift_accept:
    $ Rogue.change_face("pleased2")

    ch_Rogue "These look comfy. . ."

    return

label Rogue_green_athletic_shorts_gift_reject:
    $ Rogue.change_face("worried1")

    ch_Rogue "Ah can buy out my own shorts, thank you."

    return

label Rogue_green_athletic_shorts_change_private_before:

    return

label Rogue_green_athletic_shorts_change_private_after:
    $ Rogue.change_face("worried1")

    ch_Rogue "Are they {i}too{/i} short?"

    return

label Rogue_green_athletic_shorts_change_public_before:

    return

label Rogue_green_athletic_shorts_change_public_after:
    $ Rogue.change_face("worried1")

    ch_Rogue "Are they {i}too{/i} short?"

    return