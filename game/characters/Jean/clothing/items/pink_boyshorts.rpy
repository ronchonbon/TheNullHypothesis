init -1 python:

    def Jean_pink_boyshorts():
        name = "pink boyshorts"
        short_name = "boyshorts"
        string = "pink_boyshorts"
        
        Clothing_type = "underwear"

        shop_type = "clothing"
        chapter = 0
        season = 0
        
        thresholds = {
            "accept": [0, 0],
            "wear_in_private": [0, 0],
            "wear_in_public": [0, 0]}
        
        price = 0
        
        shame = [-10, 10]

        available_states = {
            "standing": [0, 1],
            "doggy": [0],
            "hands_and_knees": [0, 1],
            "masturbation": [0],
            "missionary": [0]}
        undressed_states = {
            "standing": 1,
            "doggy": 0,
            "hands_and_knees": 1,
            "masturbation": 0,
            "missionary": 0}
        
        covers = {
            "standing": {
                "ass": [0],
                "pussy": [0],
                "anus": [0]},
            "doggy": {
                "ass": [0],
                "pussy": [0],
                "anus": [0]},
            "hands_and_knees": {
                "ass": [0],
                "pussy": [0],
                "anus": [0]},
            "masturbation": {
                "ass": [0],
                "pussy": [0],
                "anus": [0]},
            "missionary": {
                "ass": [0],
                "pussy": [0],
                "anus": [0]}}
        hides = {
            "standing": {
                "ass": [0],
                "pussy": [0],
                "anus": [0]},
            "doggy": {
                "ass": [0],
                "pussy": [0],
                "anus": [0]},
            "hands_and_knees": {
                "ass": [0],
                "pussy": [0],
                "anus": [0]},
            "masturbation": {
                "ass": [0],
                "pussy": [0],
                "anus": [0]},
            "missionary": {
                "ass": [0],
                "pussy": [0],
                "anus": [0]}}

        covered_by = {
            "blue_athletic_shorts": [0],
            "khaki_pants": [0],
            "red_swimsuit": [0, 1, 2, 3]}
        blocked_by = {
            "blue_athletic_shorts": [0, 1],
            "khaki_pants": [0, 1],
            "red_swimsuit": [0, 1, 2, 3]}

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

label Jean_pink_boyshorts_shopping_accept:
    $ Jean.change_face("smirk2")

    ch_Jean "Aw, good choice!"

    return

label Jean_pink_boyshorts_shopping_reject:
    $ Jean.change_face("confused1")

    ch_Jean "I can buy my own underwear. . ."

    return

label Jean_pink_boyshorts_gift_accept:
    $ Jean.change_face("surprised1")

    pause 1.0

    $ Jean.change_face("pleased1")

    ch_Jean "Hey, these actually look really nice. . ."
    ch_Jean "Thanks, [Jean.Player_petname]!"

    return

label Jean_pink_boyshorts_gift_reject:
    $ Jean.change_face("confused2")

    ch_Jean "I really don't need those."

    return

label Jean_pink_boyshorts_change_private_before:

    return

label Jean_pink_boyshorts_change_private_after:
    $ Jean.change_face("pleased22", eyes = "down")

    ch_Jean "Sooo comfortable."

    $ Jean.change_face("smirk2")

    return

label Jean_pink_boyshorts_change_public_before:

    return

label Jean_pink_boyshorts_change_public_after:
    $ Jean.change_face("smirk2")

    ch_Jean "You like me in these too?"

    return