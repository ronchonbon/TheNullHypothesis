init -1 python:

    def Laura_thighhigh_boots():
        name = "thigh-high boots"
        short_name = "boots"
        string = "thighhigh_boots"
        
        Clothing_type = "boots"

        shop_type = "clothing"
        chapter = 1
        season = 3

        thresholds = {
            "accept": [275, 275],
            "wear_in_private": [275, 275],
            "wear_in_public": [300, 300]}
        
        price = 3
        
        shame = [5, 5]
        
        available_states = {
            "standing": [0]}
        undressed_states = {
            "standing": 0}
        
        covers = {
            "standing": {
                "feet": [0]}}
        hides = {
            "standing": {
                "feet": [0]}}

        covered_by = {}
        blocked_by = {}

        supports_breasts = False
        
        incompatibilities = []
        
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

label Laura_thighhigh_boots_shopping_accept:
    $ Laura.change_face("pleased1")

    ch_Laura "I do like boots. . ."

    return

label Laura_thighhigh_boots_shopping_reject:
    $ Laura.change_face("confused1")

    ch_Laura "Why would I want that?"

    return

label Laura_thighhigh_boots_gift_accept:
    $ Laura.change_face("confused1", mouth = "smirk")

    ch_Laura "Yeah. . . I could wear these."

    return

label Laura_thighhigh_boots_gift_reject:
    $ Laura.change_face("angry1")

    ch_Laura "Why are you buying me shit?"

    return

label Laura_thighhigh_boots_change_private_before:

    return

label Laura_thighhigh_boots_change_private_after:
    $ Laura.change_face("perplexed", eyes = "down")

    ch_Laura "Who came up with these?"

    $ Laura.eyes = "neutral"

    ch_Laura "They're. . . nice."

    return

label Laura_thighhigh_boots_change_public_before:

    return

label Laura_thighhigh_boots_change_public_after:
    $ Laura.change_face("confused1")

    ch_Laura "Not sure why they're so high. . . but they work."

    return