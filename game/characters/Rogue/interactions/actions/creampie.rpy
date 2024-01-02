label Rogue_rejects_creampie:
    if Rogue.check_trait("birth_control"):
        $ Rogue.change_face("worried2", mouth = "lipbite", blush = 1)

        ch_Rogue "Ah don't want you to finish inside. . ."
    else:
        $ Rogue.change_face("worried2", mouth = "lipbite", blush = 1)

        ch_Rogue "Ah'm not tryin' to get knocked up. . ." 

        $ Rogue.change_face("worried1", mouth = "lipbite", blush = 2)

        ch_Rogue "Let me get on birth control first."

    return

label Rogue_accepts_creampie_first_time:
    if Rogue.check_trait("birth_control"):
        $ Rogue.change_face("worried1", mouth = "lipbite", blush = 2) 

        ch_Rogue "Ah am on the pill." 

    $ Rogue.change_face("sexy", blush = 2) 

    ch_Rogue "You can do it inside if ya want. . ."

    return

label Rogue_accepts_creampie_second_time:

    return

label Rogue_accepts_creampie:
    $ Rogue.change_face("worried2", mouth = "lipbite", blush = 2) 

    ch_Rogue "Oh lord, please do." 

    $ Rogue.change_face("sexy", blush = 2) 

    ch_Rogue "Ah want it inside me. . ."

    return

label Rogue_accepts_creampie_love:

    return

label Rogue_rejects_anal_creampie:
    $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

    ch_Rogue "Ah'd rather not have to clean that out. . ."

    return

label Rogue_accepts_anal_creampie_first_time:
    $ Rogue.change_face("confused2", mouth = "lipbite", blush = 2) 

    ch_Rogue "In there?" 

    $ Rogue.change_face("sexy", blush = 2) 

    ch_Rogue "Why not. . ."

    return

label Rogue_accepts_anal_creampie_second_time:

    return

label Rogue_accepts_anal_creampie:
    $ Rogue.change_face("worried2", mouth = "lipbite", blush = 2) 

    ch_Rogue "Up there?" 

    $ Rogue.change_face("sexy", blush = 2) 

    ch_Rogue "Do it as deep as ya can, please. . ."

    return

label Rogue_accepts_anal_creampie_love:

    return

label Rogue_rejects_cum_in_mouth:
    $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

    if not Rogue.History.check("cum_in_mouth") and not Rogue.History.check("swallow_cum"):
        ch_Rogue "Ah'm not ready to taste that yet. . ."
    else:
        ch_Rogue "No. . ."

    return

label Rogue_accepts_cum_in_mouth_first_time:
    $ Rogue.change_face("manic", blush = 1) 

    if not Rogue.History.check("cum_in_mouth") and not Rogue.History.check("swallow_cum"):
        ch_Rogue "Ah've been wonderin' what it tastes like. . ."
    else:
        ch_Rogue "Ah guess it can't hurt. . ."

    return

label Rogue_accepts_cum_in_mouth_second_time:

    return

label Rogue_accepts_cum_in_mouth:
    $ Rogue.change_face("manic", blush = 1) 

    "She wraps her lips around you as you blow."

    return

label Rogue_accepts_cum_in_mouth_love:

    return
    
label Rogue_rejects_cum_down_throat:
    $ Rogue.change_face("worried2", mouth = "lipbite", blush = 1)

    if not Rogue.History.check("cum_down_throat"):
        ch_Rogue "Ah can't even fit you that deep yet. . ."
    else:
        ch_Rogue "Ah don't think so. . ."

    return

label Rogue_accepts_cum_down_throat_first_time:
    $ Rogue.change_face("worried2", mouth = "lipbite", blush = 1) 

    ch_Rogue "Down my throat?" 

    $ Rogue.change_face("worried1", mouth = "lipbite", blush = 2) 

    ch_Rogue "Ah'll try and keep it down. . ."

    return

label Rogue_accepts_cum_down_throat_second_time:

    return

label Rogue_accepts_cum_down_throat:
    $ Rogue.change_face("worried2", mouth = "lipbite", blush = 1) 

    ch_Rogue "Down my throat?" 
    ch_Rogue "If ya want, [Rogue.Player_petname]."

    $ Rogue.change_face("worried1", mouth = "lipbite", blush = 2) 

    "She doesn't protest as you push yourself as deep as possible."
    "She gags slightly, but does her best to keep it down."

    return

label Rogue_accepts_cum_down_throat_love:

    return