init -1 python:

    def Laura_black_long_gloves():
        name = "black long gloves"
        short_name = "gloves"
        string = "black_long_gloves"
        
        Clothing_type = "gloves"

        shop_type = "clothing"
        chapter = 0
        season = 0

        thresholds = {
            "accept": [0, 0],
            "wear_in_private": [0, 0],
            "wear_in_public": [0, 0]}
        
        price = 0
        
        shame = [0, 0]
        
        available_states = {
            "standing": [0]}
        undressed_states = {
            "standing": 0}
        
        covers = {
            "standing": {}}
        hides = {
            "standing": {}}

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

label Laura_black_long_gloves_shopping_accept:
    $ Laura.change_face("confused1")

    ch_Laura "I guess, if you think they'll look good."

    return

label Laura_black_long_gloves_shopping_reject:
    $ Laura.change_face("neutral")

    ch_Laura "Already have gloves, don't need em'."

    return

label Laura_black_long_gloves_gift_accept:
    $ Laura.change_face("confused1")

    ch_Laura "Thanks. . . you think they look good?"

    return

label Laura_black_long_gloves_gift_reject:
    $ Laura.change_face("confused1")

    ch_Laura "Uhm. . . Why would I want fingerless gloves?"

    return

label Laura_black_long_gloves_change_private_before:
    $ Laura.change_face("confused1", eyes = "down")

    ch_Laura "I guess I won't rip through them if I have to use my claws."

    return

label Laura_black_long_gloves_change_private_after:
    $ Laura.eyes = "neutral"
    
    call Laura_unsheathes_claws from _call_Laura_unsheathes_claws

    pause 2.0

    call Laura_sheathes_claws from _call_Laura_sheathes_claws

    return

label Laura_black_long_gloves_change_public_before:

    return

label Laura_black_long_gloves_change_public_after:
    $ Laura.change_face("smirk2")

    ch_Laura "Cool, right?"

    return