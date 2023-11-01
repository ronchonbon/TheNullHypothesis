init -1 python:

    def Jean_white_cami():
        name = "white cami"
        short_name = "cami"
        string = "white_cami"
        
        Clothing_type = "top"

        shop_type = "clothing"
        chapter = 1
        season = 3
        
        thresholds = {
            "accept": [250, 225],
            "wear_in_private": [250, 225],
            "wear_in_public": [275, 250]}
        
        price = 4
        
        shame = [-2, -2]

        available_states = {
            "standing": [0, 1],
            "doggy": [0, 1],
            "hands_and_knees": [0, 1],
            "masturbation": [0, 1],
            "missionary": [0, 1]}
        undressed_states = {
            "standing": 1,
            "doggy": 1,
            "hands_and_knees": 1,
            "masturbation": 1,
            "missionary": 1}
        
        covers = {
            "standing": {},
            "doggy": {},
            "hands_and_knees": {},
            "masturbation": {},
            "missionary": {}}
        hides = {
            "standing": {},
            "doggy": {},
            "hands_and_knees": {},
            "masturbation": {},
            "missionary": {}}

        covered_by = {
            "black_trenchcoat": [0],
            "denim_jacket": [0],
            "puffy_jacket": [0],
            "towel": [0]}
        blocked_by = {
            "black_trenchcoat": [0, 1],
            "denim_jacket": [0, 1],
            "puffy_jacket": [0, 1],
            "towel": [0]}

        supports_breasts = True
        
        incompatibilities = [
            "red_swimsuit",
            "yellow_dress"]
        
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

label Jean_white_cami_shopping_accept:
    $ Jean.change_face("smirk2")

    ch_Jean "You have good taste, [Player.first_name]."

    return

label Jean_white_cami_shopping_reject:
    $ Jean.change_face("confused1")

    ch_Jean "I'm good, thanks."

    return

label Jean_white_cami_gift_accept:
    $ Jean.change_face("smirk2")

    ch_Jean "Oh, cute, [Player.first_name]!"

    return

label Jean_white_cami_gift_reject:
    $ Jean.change_face("confused1")

    ch_Jean "You didn't buy this for me, did you?"

    return

label Jean_white_cami_change_private_before:

    return

label Jean_white_cami_change_private_after:
    $ Jean.change_face("pleased1")

    ch_Jean "What a cute top."

    return

label Jean_white_cami_change_public_before:

    return

label Jean_white_cami_change_public_after:
    $ Jean.change_face("pleased1")

    ch_Jean "Say it, I look amazing."

    return