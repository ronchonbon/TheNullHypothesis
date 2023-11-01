label Jean_barbell_nipple_piercings_accept:
    if "barbell_nipple_piercings" in Jean.inventory.keys():
        $ Jean.change_face("sexy")

        ch_Jean "Good decision, they look great. Right?"
    else:
        $ Jean.change_face("worried2")

        ch_Jean "I guess I can get them pierced. . ."

    return

label Jean_barbell_nipple_piercings_reject:
    $ Jean.change_face("confused3")

    ch_Jean "Really?!"

    $ Jean.change_face("angry1")

    ch_Jean "You wish."

    return