label Rogue_round_anal_plug_shopping_accept:
    $ Rogue.change_face("sexy")

    ch_Rogue "These'll work for our. . . training."

    return True

label Rogue_round_anal_plug_shopping_reject:
    $ Rogue.change_face("appalled2")

    ch_Rogue "What makes ya think ah need somethin' like that. . ."

    return

label Rogue_round_anal_plug_gift_accept:
    $ Rogue.change_face("sexy")

    ch_Rogue "These'll work for. . . you know what."

    return True

label Rogue_round_anal_plug_gift_reject:
    $ Rogue.change_face("appalled2")

    ch_Rogue "What the hell, hon'?"
    ch_Rogue "Why would ah need those. . ."

    return

label Rogue_round_anal_plug_change(plug_size):
    if plug_size > Rogue.anal_training:
        $ Rogue.change_face("worried1")

        ch_Rogue "Ah can't fit that one yet, it's too big."

        return False
    else:
        $ Rogue.change_face("sexy")

        ch_Rogue "Ah am startin' to get used to it. . ."

        $ Rogue.blush = 1

        ch_Rogue "Feels good."

    return True

label Rogue_round_anal_plug_change_reject:
    $ Rogue.change_face("angry1")

    ch_Rogue "Not right now."

    return

label Rogue_round_anal_plug_change_reject_worn_out:
    $ Rogue.change_face("worried2")

    ch_Rogue "Ah don't know if ah can do more today, [Rogue.Player_petname]. . ."

    return