init -1 python:

    def Laura_blueyellow_Wolverine_mask():
        name = "blue-and-yellow Wolverine mask"
        short_name = "mask"
        string = "blueyellow_Wolverine_mask"

        Clothing_type = "face_outer_accessory"

        shop_type = "clothing"
        chapter = 1
        season = 4

        thresholds = {
            "accept": [250, 275],
            "wear_in_private": [250, 275],
            "wear_in_public": [275, 300]}

        price = 3

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

label Laura_blueyellow_Wolverine_mask_shopping_accept:
    $ Laura.change_face("smirk2")

    ch_Laura "Cool colors."

    return

label Laura_blueyellow_Wolverine_mask_shopping_reject:
    $ Laura.change_face("confused1")

    ch_Laura "Eh, I don't need that."

    return

label Laura_blueyellow_Wolverine_mask_gift_accept:
    $ Laura.change_face("smirk2")

    ch_Laura "Sure, blue's not bad."

    return

label Laura_blueyellow_Wolverine_mask_gift_reject:
    $ Laura.change_face("neutral")

    ch_Laura "Don't need it."

    return

label Laura_blueyellow_Wolverine_mask_change_private_before:

    return

label Laura_blueyellow_Wolverine_mask_change_private_after:
    $ Laura.change_face("confused1")

    ch_Laura "Weird how perfectly matched it is. . ."

    return

label Laura_blueyellow_Wolverine_mask_change_public_before:
    $ Laura.change_face("smirk2")

    ch_Laura "Blue, huh?"

    return

label Laura_blueyellow_Wolverine_mask_change_public_after:

    return