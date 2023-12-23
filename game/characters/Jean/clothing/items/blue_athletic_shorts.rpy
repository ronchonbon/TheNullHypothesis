init -1 python:

    def Jean_blue_athletic_shorts():
        name = "blue athletic shorts"
        short_name = "shorts"
        string = "blue_athletic_shorts"

        Clothing_type = "pants"

        shop_type = "clothing"
        chapter = 0
        season = 0

        thresholds = {
            "accept": [0, 0],
            "wear_in_private": [0, 0],
            "wear_in_public": [0, 0]}

        price = 0

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

label Jean_blue_athletic_shorts_shopping_accept:
    $ Jean.change_face("worried1")

    ch_Jean "They're very tight. . ."

    $ Jean.change_face("pleased1")

    ch_Jean "But comfy for sure."

    return

label Jean_blue_athletic_shorts_shopping_reject:
    $ Jean.change_face("confused1")

    ch_Jean "What, think I can't pick out clothes for myself?"

    return

label Jean_blue_athletic_shorts_gift_accept:
    $ Jean.change_face("pleased1")

    ch_Jean "For me?"
    ch_Jean "Thanks, [Jean.Player_petname]. . ."

    return

label Jean_blue_athletic_shorts_gift_reject:
    $ Jean.change_face("confused1")

    ch_Jean "You don't have to worry about my wardrobe. . ."

    return

label Jean_blue_athletic_shorts_change_private_before:

    return

label Jean_blue_athletic_shorts_change_private_after:
    $ Jean.change_face("smirk2")

    ch_Jean "I feel like I could go run a marathon."

    return

label Jean_blue_athletic_shorts_change_public_before:

    return

label Jean_blue_athletic_shorts_change_public_after:
    $ Jean.change_face("confused1")

    $ temp = Jean.Player_petname.capitalize()

    ch_Jean "[temp], you're staring at my butt again. . ."

    $ Jean.change_face("smirk2")

    return