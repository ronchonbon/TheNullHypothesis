init -1 python:

    def Rogue_green_mesh_top():
        name = "green mesh top"
        short_name = "mesh top"
        string = "green_mesh_top"
        
        Clothing_type = "top"

        shop_type = "clothing"
        chapter = 1
        season = 1
        
        thresholds = {
            "accept": [175, 175],
            "wear_in_private": [175, 175],
            "wear_in_public": [200, 200]}
        
        price = 3
        
        shame = [10, 10]
        
        available_states = {
            "standing": [0]}
        undressed_states = {
            "standing": 0}
        
        covers = {
            "standing": {
                "bra": [0],
                "breasts": [0],
                "back": [0],
                "belly": [0]}}
        hides = {
            "standing": {}}

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

label Rogue_green_mesh_top_shopping_accept:
    $ Rogue.change_face("surprised2")

    ch_Rogue "Didn't think ah'd ever wear somethin' like this again. . ."

    return

label Rogue_green_mesh_top_shopping_reject:
    $ Rogue.change_face("worried1")

    ch_Rogue "Pretty sure ah can buy my own clothes, sugar."

    return

label Rogue_green_mesh_top_gift_accept:
    $ Rogue.change_face("pleased2")

    ch_Rogue "Heh, ah wore somethin' like this in high school. . ."

    return

label Rogue_green_mesh_top_gift_reject:
    $ Rogue.change_face("surprised2")

    pause 1.0

    $ Rogue.change_face("worried1")

    ch_Rogue "Ah can pick out my own clothes, hon'."

    return

label Rogue_green_mesh_top_change_private_before:

    return

label Rogue_green_mesh_top_change_private_after:
    $ Rogue.change_face("pleased2", eyes = "down")

    ch_Rogue "Even now, ah still like it. . ."

    $ Rogue.eyes = "neutral"
    $ Rogue.blush = 1

    ch_Rogue "Wasn't as tight in the front back then. . ."

    return

label Rogue_green_mesh_top_change_public_before:

    return

label Rogue_green_mesh_top_change_public_after:
    $ Rogue.change_face("smirk2")

    ch_Rogue "Still fashionable."

    return