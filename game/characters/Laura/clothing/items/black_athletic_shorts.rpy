init -1 python:

    def Laura_black_athletic_shorts():
        name = "black athletic shorts"
        short_name = "shorts"
        string = "black_athletic_shorts"

        Clothing_type = "pants"

        shop_type = "clothing"
        chapter = 1
        season = 2

        thresholds = {
            "accept": [125, 150],
            "wear_in_private": [125, 150],
            "wear_in_public": [150, 175]}

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

label Laura_black_athletic_shorts_shopping_accept:
    $ Laura.change_face("pleased1")

    ch_Laura "Now these are comfortable."

    return

label Laura_black_athletic_shorts_shopping_reject:
    $ Laura.change_face("confused1")

    ch_Laura "I can buy my own clothes."

    return

label Laura_black_athletic_shorts_gift_accept:
    $ Laura.change_face("pleased1")

    ch_Laura "Oh."
    ch_Laura "These are nice."

    return

label Laura_black_athletic_shorts_gift_reject:
    $ Laura.change_face("confused1")

    ch_Laura "I'm good."

    return

label Laura_black_athletic_shorts_change_private_before:

    return

label Laura_black_athletic_shorts_change_private_after:
    $ Laura.change_face("pleased1")

    ch_Laura "I really like these."

    return

label Laura_black_athletic_shorts_change_public_before:

    return

label Laura_black_athletic_shorts_change_public_after:
    $ Laura.change_face("pleased1")

    ch_Laura "I could wear these all day."

    return