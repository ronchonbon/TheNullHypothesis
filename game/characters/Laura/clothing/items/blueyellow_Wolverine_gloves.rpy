init -1 python:

    def Laura_blueyellow_Wolverine_gloves():
        name = "blue-and-yellow Wolverine gloves"
        short_name = "gloves"
        string = "blueyellow_Wolverine_gloves"
        
        Clothing_type = "gloves"

        shop_type = "clothing"
        chapter = 1
        season = 4

        thresholds = {
            "accept": [250, 275],
            "wear_in_private": [250, 275],
            "wear_in_public": [275, 300]}

        price = 2

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
        
        incompatibilities = [
            "striped_shirt",
            "white_sweater"]
        
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

label Laura_blueyellow_Wolverine_gloves_shopping_accept:

    return

label Laura_blueyellow_Wolverine_gloves_shopping_reject:

    return

label Laura_blueyellow_Wolverine_gloves_gift_accept:

    return

label Laura_blueyellow_Wolverine_gloves_gift_reject:

    return

label Laura_blueyellow_Wolverine_gloves_change_private_before:

    return

label Laura_blueyellow_Wolverine_gloves_change_private_after:

    return

label Laura_blueyellow_Wolverine_gloves_change_public_before:

    return

label Laura_blueyellow_Wolverine_gloves_change_public_after:

    return