label Laura_round_anal_plug_shopping_accept:
    $ Laura.change_face("confused1")

    ch_Laura "These could work for. . . training."

    return True

label Laura_round_anal_plug_shopping_reject:
    $ Laura.change_face("appalled1")

    ch_Laura "The fuck are those for?"

    return

label Laura_round_anal_plug_gift_accept:
    $ Laura.change_face("confused1")

    ch_Laura "Might work for. . . training."

    return True

label Laura_round_anal_plug_gift_reject:
    $ Laura.change_face("appalled1")

    ch_Laura "The fuck are those? No thanks."

    return

label Laura_round_anal_plug_change(plug_size):
    if plug_size > Laura.anal_training:
        $ Laura.change_face("neutral")

        ch_Laura "Too big."

        return False
    else:
        $ Laura.change_face("smirk2")

        ch_Laura "They feel kinda good. . ."

    return True

label Laura_round_anal_plug_change_reject:
    $ Laura.change_face("angry1")

    ch_Laura "Not happening."

    return

label Laura_round_anal_plug_change_reject_worn_out:
    $ Laura.change_face("angry1")

    ch_Laura "Again? I'd rather not."

    return