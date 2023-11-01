label Jean_heart_anal_plug_shopping_accept:
    $ Jean.change_face("worried2")

    ch_Jean "These could work for. . . you know. . ."
    ch_Jean "The large is pretty big though. . ."

    return True

label Jean_heart_anal_plug_shopping_reject:
    $ Jean.change_face("appalled2")

    ch_Jean "The fuck?!"
    ch_Jean "Why would you even bring me into a store like this?"

    return

label Jean_heart_anal_plug_gift_accept:
    $ Jean.change_face("worried2")

    ch_Jean "These could work for. . . the training. . ."

    return True

label Jean_heart_anal_plug_gift_reject:
    $ Jean.change_face("appalled2")

    ch_Jean "The fuck?"
    ch_Jean "Why would you try giving me that?"

    return

label Jean_heart_anal_plug_change(plug_size):
    if plug_size > Jean.anal_training:
        $ Jean.change_face("worried1")

        ch_Jean "Can't fit that size yet. . ."

        return False
    else:
        $ Jean.change_face("smirk2")

        ch_Jean "I actually kinda like it. . ."

    return True

label Jean_heart_anal_plug_change_reject:
    $ Jean.change_face("angry1")

    ch_Jean "No way."

    return

label Jean_heart_anal_plug_change_reject_worn_out:
    $ Jean.change_face("worried2")

    ch_Jean "I just had it in. . . Let's take a break, [Jean.Player_petname]."

    return