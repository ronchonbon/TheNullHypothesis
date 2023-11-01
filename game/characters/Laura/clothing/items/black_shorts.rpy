init -1 python:

    def Laura_black_shorts():
        name = "black shorts"
        short_name = "shorts"
        string = "black_shorts"

        Clothing_type = "pants"

        shop_type = "clothing"
        chapter = 1
        season = 3

        thresholds = {
            "accept": [200, 225],
            "wear_in_private": [200, 225],
            "wear_in_public": [225, 250]}

        price = 4

        shame = [0, 0]
        
        available_states = {
            "standing": [0, 1, 2]}
        undressed_states = {
            "standing": 2}
        
        covers = {
            "standing": {
                "underwear": [0, 1],
                "ass": [0, 1],
                "pussy": [0, 1],
                "anus": [0, 1]}}
        hides = {
            "standing": {
                "underwear": [0],
                "ass": [0, 1],
                "pussy": [0, 1],
                "anus": [0, 1]}}

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

label Laura_black_shorts_shopping_accept:
    $ Laura.change_face("neutral")

    ch_Laura "Bit tight. But cool."

    return

label Laura_black_shorts_shopping_reject:
    $ Laura.change_face("confused1")

    ch_Laura "Why are you trying to buy me clothes?"

    return

label Laura_black_shorts_gift_accept:
    $ Laura.change_face("neutral")

    ch_Laura "Not sure I can move very quickly in these."
    ch_Laura "They are cool, though."

    return

label Laura_black_shorts_gift_reject:
    $ Laura.change_face("confused1")

    ch_Laura "What? No."

    return

label Laura_black_shorts_change_private_before:

    return

label Laura_black_shorts_change_private_after:
    $ Laura.change_face("neutral")

    ch_Laura "I guess they are comfortable."

    return

label Laura_black_shorts_change_public_before:

    return

label Laura_black_shorts_change_public_after:
    $ Laura.change_face("pleased1")

    ch_Laura "I don't mind them."

    return