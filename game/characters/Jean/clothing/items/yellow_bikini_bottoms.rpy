init -1 python:

    def Jean_yellow_bikini_bottoms():
        name = "yellow bikini bottoms"
        short_name = "bikini bottoms"
        string = "yellow_bikini_bottoms"
        
        Clothing_type = "underwear"

        shop_type = "clothing"
        chapter = 0
        season = 0
        
        thresholds = {
            "accept": [275, 225],
            "wear_in_private": [275, 225],
            "wear_in_public": [275, 250]}
        
        price = 2
        
        shame = [5, 15]

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
            "standing": {
                "pussy": [0],
                "anus": [0]},
            "doggy": {
                "pussy": [0],
                "anus": [0]},
            "hands_and_knees": {
                "pussy": [0],
                "anus": [0]},
            "masturbation": {
                "pussy": [0],
                "anus": [0]},
            "missionary": {
                "pussy": [0],
                "anus": [0]}}
        hides = {
            "standing": {
                "pussy": [0],
                "anus": [0]},
            "doggy": {
                "pussy": [0],
                "anus": [0]},
            "hands_and_knees": {
                "pussy": [0],
                "anus": [0]},
            "masturbation": {
                "pussy": [0],
                "anus": [0]},
            "missionary": {
                "pussy": [0],
                "anus": [0]}}

        covered_by = {
            "black_pants": [0, 1],
            "blue_athletic_shorts": [0],
            "Jean_suit": [0, 1],
            "khaki_pants": [0, 1],
            "red_swimsuit": [0, 1]}
        blocked_by = {
            "black_garterbelt": [0],
            "black_pants": [0, 1, 2],
            "blue_athletic_shorts": [0, 1],
            "Jean_suit": [0, 1],
            "khaki_pants": [0, 1, 2],
            "red_swimsuit": [0, 1]}

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

label Jean_yellow_bikini_bottoms_shopping_accept:
    $ Jean.change_face("pleased2")

    ch_Jean "I do think they're pretty cute. . ."

    return

label Jean_yellow_bikini_bottoms_shopping_reject:
    $ Jean.change_face("confused2")

    ch_Jean "Just. . . no. . ."

    return

label Jean_yellow_bikini_bottoms_gift_accept:
    $ Jean.change_face("sly")

    ch_Jean "Reaaaal subtle, [Jean.Player_petname]."

    return

label Jean_yellow_bikini_bottoms_gift_reject:
    $ Jean.change_face("confused2")

    ch_Jean "The hell. . ."
    ch_Jean "Why would you buy me a swimsuit?"

    return

label Jean_yellow_bikini_bottoms_change_private_before:

    return

label Jean_yellow_bikini_bottoms_change_private_after:
    $ Jean.change_face("smirk2")

    ch_Jean "Super cute."

    return

label Jean_yellow_bikini_bottoms_change_public_before:

    return

label Jean_yellow_bikini_bottoms_change_public_after:
    $ Jean.change_face("smirk2")

    ch_Jean "Super cute."

    return