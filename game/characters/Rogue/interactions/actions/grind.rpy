label Rogue_rejects_grind_pussy:
    $ Rogue.change_face("confused2", blush = 1)

    if not Rogue.History.check("grind_pussy"):
        ch_Rogue ". . . we ain't that familiar yet, sugar."
    else:
        ch_Rogue "Yeah. . . no thanks. . ."

    return

label Rogue_accepts_grind_pussy_first_time:
    $ Rogue.change_face("confused1", mouth = "lipbite", blush = 1) 

    ch_Rogue ". . . Grindin'?" 

    $ Rogue.change_face("smirk2", mouth = "lipbite", blush = 1)  

    ch_Rogue "Sure, we can try it."

    return

label Rogue_accepts_grind_pussy_second_time:

    return

label Rogue_accepts_grind_pussy:
    $ Rogue.change_face("sexy", blush = 1) 

    "She doesn't say anything and just presses herself up against you."

    $ Rogue.change_face("sexy", blush = 2) 

    ch_Rogue "It feels nice, bein' so close to you. . ."

    return

label Rogue_accepts_grind_pussy_love:

    return

label Rogue_rejects_grind_ass:
    $ Rogue.change_face("confused2", blush = 1)

    if not Rogue.History.check("grind_ass"):
        ch_Rogue ". . . we ain't that familiar yet, sugar."
    else:
        ch_Rogue "Yeah. . . no thanks. . ."

    return

label Rogue_accepts_grind_ass_first_time:
    $ Rogue.change_face("confused1", mouth = "lipbite", blush = 1) 

    ch_Rogue ". . . Grindin'?" 

    $ Rogue.change_face("smirk2", mouth = "lipbite", blush = 1)  

    ch_Rogue "Sure, we can try it."

    return

label Rogue_accepts_grind_ass_second_time:

    return

label Rogue_accepts_grind_ass:
    $ Rogue.change_face("sexy", blush = 1) 

    "She doesn't say anything and just presses herself up against you."

    $ Rogue.change_face("sexy", blush = 2) 

    ch_Rogue "It feels nice, bein' so close to you. . ."

    return

label Rogue_accepts_grind_ass_love:

    return