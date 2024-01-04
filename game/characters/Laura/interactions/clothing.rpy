label Laura_Party_change_into_public_Outfit:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        ch_Laura "Gotta get dressed."
    elif dice_roll == 2:
        ch_Laura "Be right back."
    elif dice_roll == 3:
        ch_Laura "If we're leaving, I should change."

    return

label Laura_change_Outfit_accept_before(Outfit_name):
    if Laura.Wardrobe.Outfits[Outfit_name].shame < 500:
        $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            $ Laura.change_face("confused1")

            ch_Laura "You want me to wear something else?" 
        elif dice_roll == 2:
            $ Laura.change_face("confused1")

            ch_Laura "I don't mind that one." 
        elif dice_roll == 3:
            $ Laura.change_face("confused1", mouth = "smirk")

            ch_Laura "That one is more attractive to you?" 

        $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            $ Laura.change_face("neutral")

            ch_Laura "Fine."
        elif dice_roll == 2:
            $ Laura.change_face("neutral")

            ch_Laura "Okay."
        elif dice_roll == 3:
            $ Laura.change_face("sly")

            ch_Laura "Sure."
    else:
        $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            $ Laura.change_face("appalled2", blush = 1)

            ch_Laura "That one?" 

            $ Laura.change_face("angry1", eyes = "right", mouth = "lipbite", blush = 1)

            ch_Laura "You're serious. . ." 
        elif dice_roll == 2:
            $ Laura.change_face("confused2", blush = 1)

            ch_Laura "Is it normal to dress like that in public?"
        elif dice_roll == 3:
            $ Laura.change_face("confused1", mouth = "lipbite", blush = 1)

            ch_Laura "You'd like that, wouldn't you?" 

        $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            $ Laura.change_face("suspicious1", mouth = "smirk", blush = 1)
            
            ch_Laura "Okay. . ."
        elif dice_roll == 2:
            $ Laura.change_face("sly", blush = 1)

            ch_Laura "The things I do for you. . ." 
            ch_Laura "Be right back."
        elif dice_roll == 3:
            $ Laura.change_face("sly", blush = 1)

            ch_Laura "I'll be right back. . ."

    return

label Laura_change_Outfit_accept_after(Outfit_name):

    return

label Laura_change_Outfit_accept_with_privacy_before(Outfit_name):
    if Laura.Wardrobe.Outfits[Outfit_name].shame < 500:
        $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            $ Laura.change_face("neutral")

            ch_Laura "Fine." 
        elif dice_roll == 2:
            $ Laura.change_face("confused1")

            ch_Laura "That one's not bad."
        elif dice_roll == 3:
            $ Laura.change_face("confused1")

            ch_Laura "Why?" 

            $ Laura.change_face("neutral")

            ch_Laura "Whatever, fine." 
    else:
        $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            $ Laura.change_face("confused1", mouth = "smirk", blush = 1)

            ch_Laura "Really?" 

            $ Laura.change_face("sly", blush = 1)

            ch_Laura "You just want to see more of me." 
            ch_Laura "Fine."
        elif dice_roll == 2:
            $ Laura.change_face("confused2", blush = 1)

            ch_Laura "That one's. . ." 

            $ Laura.change_face("sly", blush = 1)

            ch_Laura "Okay. . ."
        elif dice_roll == 3:
            $ Laura.change_face("sly", blush = 1)

            ch_Laura "Yeah, yeah, I know you like this one."

    return

label Laura_change_Outfit_accept_with_privacy_after(Outfit_name):
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        $ Laura.change_face("confused1")

        ch_Laura "Happy now?"
    elif dice_roll == 2:
        $ Laura.change_face("confused1")

        ch_Laura "Well?"
    elif dice_roll == 3:
        $ Laura.change_face("sly")

        ch_Laura "Does seem like something you would like."

    return
    
label Laura_change_Outfit_reject:
    $ dice_roll = renpy.random.randint(1, 4)

    if dice_roll == 1:
        $ Laura.change_face("confused1")

        ch_Laura "Why would I change?"
    elif dice_roll == 2:
        $ Laura.change_face("confused1")

        ch_Laura "What?" 

        $ Laura.change_face("neutral")

        ch_Laura "No."
    elif dice_roll == 3:
        $ Laura.change_face("neutral")

        ch_Laura "No." 
    elif dice_roll == 4:
        $ Laura.change_face("neutral")

        ch_Laura "Don't want to."

    return
    
label Laura_change_Outfit_reject_asked_once:
    call Laura_asked_once("changing")

    return
    
label Laura_change_Outfit_reject_asked_twice:
    call Laura_asked_twice("changing")
    call Laura_kicking_out
    call getting_kicked_out(Laura) from _call_getting_kicked_out_31

    return
    
label Laura_change_Outfit_reject_mad:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        $ Laura.change_face("suspicious2")

        ch_Laura "{i}Grrrrrr{/i}. . ." 
    elif dice_roll == 2:
        $ Laura.change_face("appalled1")

        ch_Laura "I'm NOT in the mood."
    elif dice_roll == 3:
        $ Laura.change_face("appalled1")

        ch_Laura "Is my sour mood not clear to you?"

    return

label Laura_rejected_Clothing_once:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        $ Laura.change_face("appalled1")

        ch_Laura "Did you not hear what I said?" 
    elif dice_roll == 2:
        $ Laura.change_face("appalled1")

        ch_Laura "You must not be listening. . ."
    elif dice_roll == 3:
        $ Laura.change_face("angry1")

        ch_Laura "Why do I have to repeat myself?"

    return

label Laura_rejected_Clothing_twice:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        $ Laura.change_face("suspicious2")
        $ Laura.change_arms("claws")

        call Laura_unsheathes_claws from _call_Laura_unsheathes_claws_3

        ch_Laura "I can take it and tear it up if you want instead?"

        pause 1.5

        call Laura_sheathes_claws from _call_Laura_sheathes_claws_3

        $ Laura.change_arms("neutral")
    elif dice_roll == 2:
        $ Laura.change_face("suspicious2")

        ch_Laura "Stop."
    elif dice_roll == 3:
        $ Laura.change_face("angry1")

        ch_Laura "Not. Cute."
        
    call Laura_kicking_out
    call getting_kicked_out(Laura) from _call_getting_kicked_out_32

    return

label Laura_accept_private_Outfit(Outfit):
    if Outfit.shame < 500:
        $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            $ Laura.change_face("confused1", eyes = "down")

            ch_Laura "Yeah, fine." 
        elif dice_roll == 2:
            $ Laura.change_face("neutral", eyes = "down")

            ch_Laura "You like this, huh?" 
        elif dice_roll == 3:
            $ Laura.change_face("neutral", eyes = "down")

            ch_Laura "Hmmm. . ."

        $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            $ Laura.change_face("smirk2")

            ch_Laura "It's not bad."
        elif dice_roll == 2:
            $ Laura.change_face("neutral")

            ch_Laura "I can live with it."
        elif dice_roll == 3:
            $ Laura.change_face("smirk2")

            ch_Laura "I don't hate it."
    else:
        $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            $ Laura.change_face("sly")

            ch_Laura "Fine, but only for you. . ."
            ch_Laura "Weirdo."
        elif dice_roll == 2:
            $ Laura.change_face("smirk1")

            ch_Laura "You would like this. . ."
        elif dice_roll == 3:
            $ Laura.change_face("sexy")

            ch_Laura "How typical. . ."

    return

label Laura_reject_private_Outfit(Outfit):
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        $ Laura.change_face("angry1")

        ch_Laura "Nope."
    elif dice_roll == 2:
        $ Laura.change_face("suspicious1")

        ch_Laura "Not a chance."
    elif dice_roll == 3:
        $ Laura.change_face("angry1")

        ch_Laura ". . ."
        ch_Laura "Obviously not."

    return

label Laura_accept_public_Outfit(Outfit):
    if Outfit.shame < 500:
        $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            $ Laura.change_face("smirk2", eyes = "down")

            ch_Laura "Yeah, this is cool."
        elif dice_roll == 2:
            $ Laura.change_face("smirk2", eyes = "down")
            
            ch_Laura "I. . . actually like it."
        elif dice_roll == 3:
            $ Laura.change_face("neutral", eyes = "down")
            
            ch_Laura "Not too bad."
    else:
        $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            $ Laura.change_face("confused1", eyes = "down", blush = 1)

            ch_Laura "At least it covers the important parts."
        elif dice_roll == 2:
            $ Laura.change_face("confused1", eyes = "down", blush = 1)

            ch_Laura "Really?"
        elif dice_roll == 3:
            $ Laura.change_face("smirk1", eyes = "down", blush = 1)

            ch_Laura "Typical. . ."

        $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            $ Laura.change_face("sly", blush = 1)

            ch_Laura "Fine, weirdo. . ." 
        elif dice_roll == 2:
            $ Laura.change_face("smirk1", blush = 1)

            ch_Laura "I suppose I can wear it." 
        elif dice_roll == 3:
            $ Laura.change_face("smirk1", blush = 1)

            ch_Laura "Fine."

    return

label Laura_reject_public_Outfit(Outfit):
    if Outfit.shame >= 500:
        $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            $ Laura.change_face("angry1", blush = 1)

            ch_Laura "Really thought I'd go for something like this?"
        elif dice_roll == 2:
            $ Laura.change_face("angry1", blush = 1)

            ch_Laura "What are you thinking?"
        elif dice_roll == 3:
            $ Laura.change_face("neutral", blush = 1)

            ch_Laura "What? No. . ."
    elif not Laura.check_traits("pussy_covered"):
        if not Laura.check_traits("breasts_covered"):
            $ Laura.change_face("appalled3", blush = 1)

            ch_Laura "The hell?" 

            $ Laura.change_face("suspicious2", blush = 1)

            ch_Laura "Why would I walk around effectively naked?"
        else:
            $ Laura.change_face("suspicious2", blush = 1)

            ch_Laura "Why would I walk around with. . . that exposed?"
    elif not Laura.check_traits("breasts_covered"):
        $ Laura.change_face("suspicious2", blush = 1)

        ch_Laura "What would makes you think I'd walk around exposed like this?"
    else:
        $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            $ Laura.change_face("angry1")

            ch_Laura "I don't need you to make an outfit for me."
        elif dice_roll == 2:
            ch_Laura "Don't need the help."
        elif dice_roll == 3:
            ch_Laura "Not interested."

    return

label Laura_reject_contextual_Outfit(Outfit):
    $ Laura.change_face("perplexed", blush = 1)

    ch_Laura ". . . Not here."

    return