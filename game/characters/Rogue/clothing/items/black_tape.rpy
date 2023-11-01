init -1 python:

    def Rogue_black_tape():
        name = "black nipple tape"
        short_name = "nipple tape"
        string = "black_tape"
        
        Clothing_type = "nipple_accessories"

        shop_type = "lingerie"
        chapter = 1
        season = 4
        
        thresholds = {
            "accept": [750, 750],
            "wear_in_private": [750, 750],
            "wear_in_public": [775, 775]}
        
        price = 2
        
        shame = [10, 1000]

        available_states = {
            "standing": [0],
            "doggy": [0],
            "hands_and_knees": [0],
            "masturbation": [0],
            "missionary": [0]}
        undressed_states = {
            "standing": 0,
            "doggy": 0,
            "hands_and_knees": 0,
            "masturbation": 0,
            "missionary": 0}
        
        covers = {
            "standing": {
                "breasts": [0]},
            "doggy": {
                "breasts": [0]},
            "hands_and_knees": {
                "breasts": [0]},
            "masturbation": {
                "breasts": [0]},
            "missionary": {
                "breasts": [0]}}
        hides = {
            "standing": {},
            "doggy": {},
            "hands_and_knees": {},
            "masturbation": {},
            "missionary": {}}

        covered_by = {
            "black_bra": [0],
            "black_cage_bra": [0],
            "black_fishnet_top": [0],
            "black_keyhole_bra": [0],
            "black_lace_bra": [0],
            "black_tanktop": [0],
            "black_top": [0],
            "brown_jacket": [0],
            "green_bikini_top": [0],
            "green_dress": [0],
            "green_mesh_top": [0],
            "green_nighty": [0],
            "greenyellow_spors_bra": [0],
            "NIN_shirt": [0],
            "pink_swimsuit": [0],
            "plaid_coat": [0],
            "Rogue_suit": [0],
            "sweater_dress": [0, 2],
            "towel": [0]}
        blocked_by = {
            "black_bra": [0],
            "black_cage_bra": [0],
            "black_fishnet_top": [0],
            "black_keyhole_bra": [0],
            "black_lace_bra": [0],
            "black_tanktop": [0],
            "black_top": [0],
            "brown_jacket": [0],
            "green_bikini_top": [0],
            "green_dress": [0],
            "green_mesh_top": [0],
            "green_nighty": [0],
            "greenyellow_spors_bra": [0],
            "NIN_shirt": [0],
            "pink_swimsuit": [0],
            "plaid_coat": [0],
            "Rogue_suit": [0],
            "sweater_dress": [0, 2],
            "towel": [0]}

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

label Rogue_black_tape_shopping_accept:
    $ Rogue.change_face("confused1")

    ch_Rogue "Tape? Ah don't get it. . ."

    $ Rogue.change_face("surprised1")

    ch_Rogue "Oh!"

    $ Rogue.change_face("smirk2")

    return

label Rogue_black_tape_shopping_reject:
    $ Rogue.change_face("confused1")

    ch_Rogue "Ah'm confused. No thanks, [Rogue.Player_petname]."

    return

label Rogue_black_tape_gift_accept:
    $ Rogue.change_face("sly")

    ch_Rogue "Ah could be convinced. . ."

    return

label Rogue_black_tape_gift_reject:
    $ Rogue.change_face("confused1")

    ch_Rogue "Not really my style, [Player.first_name]. . ."

    return

label Rogue_black_tape_change_private_before:

    return

label Rogue_black_tape_change_private_after:
    $ Rogue.change_face("smirk2", eyes = "down")

    ch_Rogue "This what you wanted, [Rogue.Player_petname]?"

    $ Rogue.eyes = "neutral"

    return

label Rogue_black_tape_change_public_before:

    return

label Rogue_black_tape_change_public_after:
    $ Rogue.change_face("sexy")

    ch_Rogue "What do ya think?"

    return