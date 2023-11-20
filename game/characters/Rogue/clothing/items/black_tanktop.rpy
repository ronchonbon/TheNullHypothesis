init -1 python:

    def Rogue_black_tanktop():
        name = "black tanktop"
        short_name = "tanktop"
        string = "black_tanktop"
        
        Clothing_type = "bra"

        shop_type = "clothing"
        chapter = 0
        season = 0
        
        thresholds = {
            "accept": [0, 0],
            "wear_in_private": [0, 0],
            "wear_in_public": [0, 0]}
        
        price = 0
        
        shame = [5, 10]
        
        available_states = {
            "standing": [0, 1]}
        undressed_states = {
            "standing": 1}
        
        covers = {
            "standing": {
                "breasts": [0]}}
        hides = {
            "standing": {
                "breasts": [0]}}

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

label Rogue_black_tanktop_shopping_accept:
    $ Rogue.change_face("surprised2")

    ch_Rogue "Ah used to wear this kind of thing in high school. . ."

    return

label Rogue_black_tanktop_shopping_reject:
    $ Rogue.change_face("worried1")

    ch_Rogue "Ah'm all set, thank you very much."

    return

label Rogue_black_tanktop_gift_accept:
    $ Rogue.change_face("surprised2")

    ch_Rogue "Where'd ya find this?"

    $ Rogue.change_face("pleased1")

    ch_Rogue "Ah had one just like it in high school. . ."

    return

label Rogue_black_tanktop_gift_reject:
    $ Rogue.change_face("worried1")

    ch_Rogue "Uh. . . no thanks, hon'."

    return

label Rogue_black_tanktop_change_private_before:

    return

label Rogue_black_tanktop_change_private_after:
    $ Rogue.change_face("pleased2", eyes = "down")

    ch_Rogue "Looks just like ah remember. . ."

    $ Rogue.eyes = "neutral"

    return

label Rogue_black_tanktop_change_public_before:

    return

label Rogue_black_tanktop_change_public_after:
    $ Rogue.change_face("smirk2")

    ch_Rogue "Ah do like a classic."

    return