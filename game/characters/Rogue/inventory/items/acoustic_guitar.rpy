label Rogue_acoustic_guitar_shopping_accept:
    $ Rogue.change_face("worried1", eyes = "down")

    pause 1.0

    $ Rogue.change_face("worried2", blush = 1)

    $ petname = Rogue.Player_petname.capitalize()

    ch_Rogue "[petname], this ain't what ah think it is, right?"

    $ Rogue.change_face("worried1", eyes = "down", blush = 1)

    ch_Player "Depends on what you think it is."
    "She opens the case, revealing a beautifully lacquered Martin acoustic guitar."
    "Her fingers carefully strum the strings as she holds the guitar reverently, before carefully putting it away."

    $ Rogue.change_face("worried1", mouth = "smirk", blush = 1)

    ch_Rogue "It sure is a thing of beauty."
    ch_Rogue "Ah hope ah could hear ya play it sometime. . ."

    $ Rogue.change_face("worried3", blush = 1)

    ch_Player "Hear me play it? [Rogue.name], that guitar is all yours."

    $ Rogue.change_face("worried1", eyes = "down", blush = 1)

    ch_Rogue "Yer jokin'. . ."
    ch_Player "Not at all."

    $ Rogue.change_face("worried1", mouth = "smirk", blush = 1)

    ch_Rogue "Thank you. . ."

    $ Rogue.change_face("worried1", eyes = "down", blush = 1)

    ch_Rogue ". . . so much."

    return True

label Rogue_acoustic_guitar_shopping_reject:

    return

label Rogue_acoustic_guitar_gift_accept:
    $ Rogue.change_face("worried1", eyes = "down")

    pause 1.0

    $ Rogue.change_face("worried2", blush = 1)

    $ petname = Rogue.Player_petname.capitalize()

    ch_Rogue "[petname], this ain't what ah think it is, right?"

    $ Rogue.change_face("worried1", eyes = "down", blush = 1)

    ch_Player "Depends on what you think it is."
    "She opens the case, revealing a beautifully lacquered Martin acoustic guitar."
    "Her fingers carefully strum the strings as she holds the guitar reverently, before carefully putting it away."

    $ Rogue.change_face("worried1", mouth = "smirk", blush = 1)

    ch_Rogue "It sure is a thing of beauty."
    ch_Rogue "Ah hope ah could hear ya play it sometime. . ."

    $ Rogue.change_face("worried3", blush = 1)

    ch_Player "Hear me play it? [Rogue.name], that guitar is all yours."

    $ Rogue.change_face("worried1", eyes = "down", blush = 1)

    ch_Rogue "Yer jokin'. . ."
    ch_Player "Not at all."

    $ Rogue.change_face("worried1", mouth = "smirk", blush = 1)

    ch_Rogue "Thank you. . ."

    $ Rogue.change_face("worried1", eyes = "down", blush = 1)

    ch_Rogue ". . . so much."

    return True

label Rogue_acoustic_guitar_gift_reject:

    return