label Rogue_Party_change_into_public_Outfit:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        $ Rogue.change_face("worried1")

        ch_Rogue "Ah should make myself decent. . ."
    elif dice_roll == 2:
        $ Rogue.change_face("surprised1")

        ch_Rogue "Oh, we're leaving?"

        $ Rogue.change_face("worried1")

        ch_Rogue "Be right back."
    elif dice_roll == 3:
        $ Rogue.change_face("smirk1")

        ch_Rogue "Ah'll be right back."

    return

label Rogue_change_Outfit_accept_before(Outfit_name):
    if Rogue.Wardrobe.Outfits[Outfit_name].shame < 500:
        $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            ch_Rogue "Alright, ah'll put that one on."
        elif dice_roll == 2:
            ch_Rogue "Want me to change into that? Alright."
        elif dice_roll == 3:
            ch_Rogue "Sure, [Rogue.Player_petname]. Ah don't mind wearin' that."

        $ dice_roll = renpy.random.randint(1, 2)

        if dice_roll == 1:
            ch_Rogue "Be right back."
        elif dice_roll == 2:
            ch_Rogue "Ah'll be right back."
    else:
        $ Rogue.change_face("surprised2", blush = 2)

        $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            ch_Rogue "That one? Here?"
        elif dice_roll == 2:
            ch_Rogue "Want me to change into that? Alright."
        elif dice_roll == 3:
            ch_Rogue "Sure, [Rogue.Player_petname]. Ah don't mind wearin' that."

        $ Rogue.change_face("surprised1", mouth = "lipbite", blush = 1)

        if dice_roll == 1:
            ch_Rogue "Oh, alright." 
            
        $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            ch_Rogue "Ah'll be right back."
        elif dice_roll == 2:
            ch_Rogue "Let me go put it on."
        elif dice_roll == 3:
            ch_Rogue "Ah'll go put it on."

        $ Rogue.change_face("neutral")

    return

label Rogue_change_Outfit_accept_after(Outfit_name):

    return

label Rogue_change_Outfit_accept_with_privacy_before(Outfit_name):
    if Rogue.Wardrobe.Outfits[Outfit_name].shame < 500:
        $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            ch_Rogue "Alright."
        elif dice_roll == 2:
            ch_Rogue "Sure, ah'll put that on."
        elif dice_roll == 3:
            ch_Rogue "No problem, ah'll be right back."
    else:
        $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            $ Rogue.change_face("surprised2", blush = 1)

            ch_Rogue "That one?!"
            ch_Rogue ". . . Ah guess it's only you. . ."
        elif dice_roll == 2:
            $ Rogue.change_face("smirk2", blush = 1)

            ch_Rogue "Oh, alright. . ."
        elif dice_roll == 3:
            $ Rogue.change_face("smirk2", blush = 1)

            ch_Rogue "Heh, ah know you like this one." 

        $ Rogue.change_face("neutral")

    return

label Rogue_change_Outfit_accept_with_privacy_after(Outfit_name):
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        $ Rogue.change_face("smirk2")

        ch_Rogue "How do ah look?"
    elif dice_roll == 2:
        $ Rogue.change_face("smirk2")
        
        ch_Rogue "Ah like this one."
    elif dice_roll == 3:
        $ Rogue.change_face("pleased1")

        ch_Rogue "Whatcha think?"

    return
    
label Rogue_change_Outfit_reject:
    $ dice_roll = renpy.random.randint(1, 4)

    if dice_roll == 1:
        $ Rogue.change_face("confused1")

        ch_Rogue "Ah'm not puttin' that one on right now. . ."
    elif dice_roll == 2:
        $ Rogue.change_face("confused1")

        ch_Rogue "Why would ah change into that right now?"
    elif dice_roll == 3:
        $ Rogue.change_face("worried1")

        ch_Rogue "Sorry, [Rogue.Player_petname]. Ah'm not changin'."
    elif dice_roll == 4:
        $ Rogue.change_face("worried1")

        ch_Rogue "You want me to change?"
        ch_Rogue "Sorry. . . ah don't wanna right now."

    return
    
label Rogue_change_Outfit_reject_asked_once:
    call Rogue_asked_once("changing")

    return
    
label Rogue_change_Outfit_reject_asked_twice:
    call Rogue_asked_once("changing")
    call Rogue_kicking_out
    call getting_kicked_out(Rogue) from _call_getting_kicked_out_53

    return
    
label Rogue_change_Outfit_reject_mad:
    $ dice_roll = renpy.random.randint(1, 3)

    $ Rogue.change_face("angry1")

    if dice_roll == 1:
        ch_Rogue "Really think askin' me to do that right now is a good idea?"
    elif dice_roll == 2:
        ch_Rogue "That's all yer worried about right now?"
    elif dice_roll == 3:
        ch_Rogue "You tryin' to get a rise out of me?"

    return

label Rogue_rejected_Clothing_once:
    $ dice_roll = renpy.random.randint(1, 3)

    $ Rogue.change_face("angry1")

    if dice_roll == 1:
        ch_Rogue "Ah already said ah'm not takin' it."
    elif dice_roll == 2:
        ch_Rogue "Ah. Don't. Want. It."
    elif dice_roll == 3:
        ch_Rogue "Cut it out. . ."

    return

label Rogue_rejected_Clothing_twice:
    $ dice_roll = renpy.random.randint(1, 3)

    $ Rogue.change_face("appalled2")

    if dice_roll == 1:
        ch_Rogue "Stop tryin' to get me to take it."
    elif dice_roll == 2:
        ch_Rogue "You better quit tryin' to give me that."
    elif dice_roll == 3:
        ch_Rogue "Just stop, [Player.first_name]!"
        
    call getting_kicked_out(Rogue) from _call_getting_kicked_out_54

    return

label Rogue_accept_private_Outfit(Outfit):
    if Outfit.shame < 500:
        $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            $ Rogue.change_face("smirk2")

            ch_Rogue "Sure, [Rogue.Player_petname]. Ah'll wear this when we're in private."
        elif dice_roll == 2:
            $ Rogue.change_face("smirk2")

            ch_Rogue "Ah do kinda like it. . ."
        elif dice_roll == 3:
            $ Rogue.change_face("smirk2")

            ch_Rogue "It is kinda cute for just you and me."
    else:
        $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            $ Rogue.change_face("surprised2", mouth = "lipbite", blush = 1)

            ch_Rogue "Ah guess ah'll wear it. . . only in private with you. . ."
        elif dice_roll == 2:
            $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

            ch_Rogue "Ah can try it on every now and then. . ."
        elif dice_roll == 3:
            $ Rogue.change_face("surprised2", mouth = "lipbite", blush = 1)

            ch_Rogue "If you're sure. . ."

    return

label Rogue_reject_private_Outfit(Outfit):
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        $ Rogue.change_face("worried1")

        ch_Rogue "Ah don't really wanna wear somethin' like that. . . even in private. . ."
    elif dice_roll == 2:
        $ Rogue.change_face("worried1")

        ch_Rogue "That's a little too skimpy. . . way too skimpy. . ."
    elif dice_roll == 3:
        $ Rogue.change_face("worried1")

        ch_Rogue "Ah would really rather not. . ."

    return

label Rogue_accept_public_Outfit(Outfit):
    if Outfit.shame < 500:
        $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            $ Rogue.change_face("smirk2")

            ch_Rogue "Ah like it. Sure, ah'll wear it around."
        elif dice_roll == 2:
            $ Rogue.change_face("smirk2")

            ch_Rogue "It's pretty cute actually."
        elif dice_roll == 3:
            $ Rogue.change_face("happy")

            ch_Rogue "Ah look cute!"
    else:
        $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            $ Rogue.change_face("worried2", mouth = "lipbite", blush = 1)
            
            ch_Rogue "Ah guess ah can wear it around. . ."
        elif dice_roll == 2:
            $ Rogue.change_face("worried2", mouth = "lipbite", blush = 1)
            
            ch_Rogue "You're sure it's not too much?"
        elif dice_roll == 3:
            $ Rogue.change_face("worried2", blush = 1)
            
            ch_Rogue "Ah can try it on every now and then. . ."

    return

label Rogue_reject_public_Outfit(Outfit):
    if Outfit.shame >= 500:
        $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            $ Rogue.change_face("worried2", blush = 1)

            ch_Rogue "Ah'm definitely not willin' to wear somethin' like that in public. . ."
        elif dice_roll == 2:
            $ Rogue.change_face("worried2", blush = 1)

            ch_Rogue "Just what kind of girl do you think I am, [Player.first_name]?"
        elif dice_roll == 3:
            $ Rogue.change_face("worried1", blush = 1)

            ch_Rogue "Ah would never wear this out. . ."
    elif not Rogue.check_traits("pussy_covered"):
        if not Rogue.check_traits("breasts_covered"):
            $ Rogue.change_face("appalled3", blush = 3)

            ch_Rogue "Ah sure as hell ain't walkin' 'round in my birthday suit. . ."
        else:
            $ Rogue.change_face("worried3", blush = 2)

            ch_Rogue "My. . . isn't even covered!"

            $ Rogue.change_face("worried2")

            ch_Rogue "Ah definitely can't go out like this. . ."
    elif not Rogue.check_traits("breasts_covered"):
        $ Rogue.change_face("worried3", blush = 2)

        ch_Rogue "My breasts aren't even covered!"

        $ Rogue.change_face("worried2")

        ch_Rogue "Ah can't go out like this. . ."
    else:
        $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            $ Rogue.change_face("worried1")

            ch_Rogue "Ah'm sorry, ah don't wanna wear that in public. . ."
        elif dice_roll == 2:
            $ Rogue.change_face("worried1")

            ch_Rogue "Ah'd rather dress myself, [Rogue.Player_petname]. . ."
        elif dice_roll == 3:
            $ Rogue.change_face("worried1")

            ch_Rogue "Ah'm actually good on outfits. . ."

    return

label Rogue_reject_contextual_Outfit(Outfit):
    $ Rogue.change_face("worried1", blush = 1)

    ch_Rogue "Ah. . . don't think this is the right place for this outfit."

    return