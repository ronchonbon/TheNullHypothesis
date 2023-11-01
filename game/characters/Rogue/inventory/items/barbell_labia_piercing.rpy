label Rogue_barbell_labia_piercings_accept:
    if "barbell_labia_piercings" in Rogue.inventory.keys():
        $ Rogue.change_face("sexy")

        ch_Rogue "Sure, ah like the way it looks too."
    else:
        $ Rogue.change_face("worried2")

        ch_Rogue "Ah've been thinkin' about it. . ."
        ch_Rogue "Hope it doesn't hurt much."

    return

label Rogue_barbell_labia_piercings_reject:
    $ Rogue.change_face("confused3")

    ch_Rogue "You want me to get {i}what{/i} pierced?!"

    $ Rogue.change_face("angry1")

    ch_Rogue "Not happenin'."

    return