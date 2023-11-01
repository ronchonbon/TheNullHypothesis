init -1 python:

    def Rogue_leather_skirt():
        name = "leather skirt"
        short_name = "skirt"
        string = "leather_skirt"
        
        Clothing_type = "skirt"

        shop_type = "clothing"
        chapter = 1
        season = 1
        
        thresholds = {
            "accept": [175, 175],
            "wear_in_private": [175, 175],
            "wear_in_public": [200, 200]}
        
        price = 3
        
        shame = [5, 5]
        
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

label Rogue_leather_skirt_shopping_accept:
    $ Rogue.change_face("surprised2")

    ch_Rogue "Ah'd been thinkin' 'bout gettin' another skirt. . ."

    $ Rogue.change_face("pleased1")

    ch_Rogue "Wore one all the time in high school."

    return

label Rogue_leather_skirt_shopping_reject:
    $ Rogue.change_face("worried1")

    ch_Rogue "Mmm, no thanks, hon'."

    return

label Rogue_leather_skirt_gift_accept:
    $ Rogue.change_face("pleased2")

    ch_Rogue "Ah had one exactly like this in high school. . ."

    return

label Rogue_leather_skirt_gift_reject:
    $ Rogue.change_face("worried1")

    ch_Rogue "Ah don't love you buyin' me clothes. . ."

    return

label Rogue_leather_skirt_change_private_before:

    return

label Rogue_leather_skirt_change_private_after:
    $ Rogue.change_face("pleased2", eyes = "down")

    ch_Rogue "Ah missed wearin' this kind of skirt."

    $ Rogue.eyes = "neutral"

    return

label Rogue_leather_skirt_change_public_before:

    return

label Rogue_leather_skirt_change_public_after:
    $ Rogue.change_face("smirk2")

    ch_Rogue "Nostalgic."

    return