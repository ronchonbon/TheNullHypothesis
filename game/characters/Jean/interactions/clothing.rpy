label Jean_Party_change_into_public_Outfit:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        $ Jean.change_face("worried1")

        ch_Jean "Be right back, gonna change!"
    elif dice_roll == 2:
        $ Jean.change_face("smirk1")

        ch_Jean "Give me one sec."
    elif dice_roll == 3:
        $ Jean.change_face("surprised1")

        ch_Jean "We're leaving?"

        $ Jean.change_face("worried1")

        ch_Jean "Okay, let me get dressed."

    return

label Jean_change_Outfit_accept_before(Outfit_name):
    if Jean.Wardrobe.Outfits[Outfit_name].shame < 500:
        if Jean.check_traits("quirk"):
            $ dice_roll = renpy.random.randint(1, 4)
        else:
            $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 4:
            $ Jean.change_face("confused1", mouth = "smirk")

            ch_Jean "If you say please."

            $ Jean.change_face("sly", blush = 1)

            ch_Player "Please. . ." 
            ch_Jean "Good, I'll be right back."
        else:
            if dice_roll == 1:
                $ Jean.change_face("confused1", mouth = "smirk") 

                ch_Jean "You want me in that one?" 
            elif dice_roll == 2:
                $ Jean.change_face("confused1", mouth = "smirk") 

                ch_Jean "You want me to change?"
            elif dice_roll == 3:
                $ Jean.change_face("sly")

                ch_Jean "Hmm. . ."

            $ dice_roll = renpy.random.randint(1, 3)

            if dice_roll == 1:
                $ Jean.change_face("sly") 

                ch_Jean "Okay, fine, be right back."
            elif dice_roll == 2:
                $ Jean.change_face("smirk2")

                ch_Jean "Okay, gimme a sec."
            elif dice_roll == 3:
                ch_Jean "Okay, [Jean.Player_petname]."

                $ Jean.change_face("smirk2")

                ch_Jean "I can go put that one on."
    else:
        $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            $ Jean.change_face("surprised2", blush = 1)

            pause 1.0

            $ Jean.change_face("worried1", eyes = "right", blush = 1)

            ch_Jean "Well. . ." 
        elif dice_roll == 2:
            $ Jean.change_face("surprised2", blush = 1)

            ch_Jean "That one???" 

            $ Jean.change_face("confused1", mouth = "lipbite", blush = 1)

            ch_Jean ". . . maybe."
        elif dice_roll == 3:
            $ Jean.change_face("worried3", blush = 1)

            ch_Jean "But that one's. . ." 

            $ Jean.change_face("worried1", eyes = "right", mouth = "lipbite", blush = 1)

            pause 1.0

        $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            $ Jean.change_face("sexy", blush = 1)

            ch_Jean "Screw it." 
            ch_Jean "Let me go put it on."
        elif dice_roll == 2:
            $ Jean.change_face("sexy", blush = 1)

            ch_Jean "Okay, fine, be right back."
        elif dice_roll == 3:
            ch_Jean "Oh, screw it." 

            $ Jean.change_face("sexy", blush = 1)

            ch_Jean "Be right back."

    return

label Jean_change_Outfit_accept_after(Outfit_name):

    return

label Jean_change_Outfit_accept_with_privacy_before(Outfit_name):
    if Jean.Wardrobe.Outfits[Outfit_name].shame < 500:
        $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            $ Jean.change_face("happy")

            ch_Jean "Sure!"
        elif dice_roll == 2:
            $ Jean.change_face("smirk2")

            ch_Jean "Okay, I can throw it on real quick."
        elif dice_roll == 3:
            $ Jean.change_face("confused1", mouth = "smirk")

            ch_Jean "Oh, okay, fine." 

            $ Jean.change_face("smirk2")

            ch_Jean "I can throw that on."
    else:
        if Jean.check_traits("quirk"):
            $ dice_roll = renpy.random.randint(1, 3)
        else:
            $ dice_roll = renpy.random.randint(1, 2)

        if dice_roll == 1:
            $ Jean.change_face("perplexed", blush = 1)

            ch_Jean "You're joking. . ." 

            $ Jean.change_face("confused1", mouth = "lipbite", blush = 1) 

            ch_Jean ". . . you're not joking." 

            $ Jean.change_face("sly", mouth = "lipbite", blush = 1)  

            ch_Jean "Hmmm. . . be right back. . ."
        elif dice_roll == 2:
            $ Jean.change_face("worried1", mouth = "lipbite", blush = 1) 

            ch_Jean "But that one's skimpy. . ." 

            $ Jean.change_face("sexy", blush = 1)

            ch_Jean "Oh alright, [Jean.Player_petname]." 
            ch_Jean "I'll put it on just for you."
        elif dice_roll == 3:
            $ Jean.change_face("surprised2", blush = 1)

            ch_Jean "That one?!"

            $ Jean.change_face("sexy", blush = 1)

            ch_Jean "You have been good lately. . ."
            ch_Jean "Oh okay. . ."

    return

label Jean_change_Outfit_accept_with_privacy_after(Outfit_name):
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        $ Jean.change_face("confused1", mouth = "smirk")

        ch_Jean "Looks great, right?"
    elif dice_roll == 2:
        $ Jean.change_face("confused1", mouth = "smirk")

        ch_Jean "You like?"
    elif dice_roll == 3:
        $ Jean.change_face("smirk1")

        ch_Jean "Well?"

    return
    
label Jean_change_Outfit_reject:
    if Jean.check_traits("quirk"):
        $ dice_roll = renpy.random.randint(1, 4)
    else:
        $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        $ Jean.change_face("confused1")

        ch_Jean "Uhhh. . . I'd rather not change right now."
    elif dice_roll == 2:
        $ Jean.change_face("neutral")

        ch_Jean "Nah, I'm good."
    elif dice_roll == 3:
        $ Jean.change_face("worried1", mouth = "smirk")

        ch_Jean "Sorry, [Jean.Player_petname]." 
        ch_Jean "Don't really wanna."
    elif dice_roll == 4:
        $ Jean.change_face("confused1")

        ch_Jean "Why would I change?" 

        $ Jean.change_face("smirk2", eyes = "down")

        ch_Jean "I look great in this outfit."

    return
    
label Jean_change_Outfit_reject_asked_once:
    call Jean_asked_once("changing") from _call_Jean_asked_once_7

    return
    
label Jean_change_Outfit_reject_asked_twice:
    call Jean_asked_twice("changing") from _call_Jean_asked_twice_7
    call Jean_kicking_out from _call_Jean_kicking_out_9
    call getting_kicked_out(Jean) from _call_getting_kicked_out_9

    return
    
label Jean_change_Outfit_reject_mad:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        $ Jean.change_face("appalled3")

        ch_Jean "That's all you're worried about right now?!" 

        $ Jean.change_face("angry1", eyes = "right")
    elif dice_roll == 2:
        $ Jean.change_face("appalled2")

        ch_Jean "Seriously?!" 

        $ Jean.change_face("furious")

        ch_Jean "Read the room, [Jean.Player_petname]." 
    elif dice_roll == 3:
        $ Jean.change_face("furious")

        ch_Jean "Ugh, don't even ask." 

        $ Jean.change_face("angry1", eyes = "right")

        ch_Jean "I'm not in the mood." 

    return

label Jean_rejected_Clothing_once:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        $ Jean.change_face("angry1")

        ch_Jean "I already said I don't want that, [Jean.Player_petname]." 
    elif dice_roll == 2:
        $ Jean.change_face("confused1")

        ch_Jean "Why would I take that now?" 

        $ Jean.change_face("angry1")

        ch_Jean "I already told you I don't want it."
    elif dice_roll == 3:
        $ Jean.change_face("confused1")

        ch_Jean "Not sure why you're trying again."

    return

label Jean_rejected_Clothing_twice:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        $ Jean.change_face("appalled1")

        ch_Jean "You better stop trying to give me that." 
    elif dice_roll == 2:
        $ Jean.change_face("appalled1")

        ch_Jean "No means NO!" 
    elif dice_roll == 3:
        $ Jean.change_face("angry1")

        ch_Jean "What the hell, [Player.first_name]?"
        
    call Jean_kicking_out from _call_Jean_kicking_out_10
    call getting_kicked_out(Jean) from _call_getting_kicked_out_10

    return

label Jean_accept_private_Outfit(Outfit):
    if Outfit.shame < 500:
        $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            $ Jean.change_face("smirk2", eyes = "down")

            ch_Jean "I like it."
        elif dice_roll == 2:
            $ Jean.change_face("pleased2", eyes = "down")

            ch_Jean "Not too bad. . ."
        elif dice_roll == 3:
            $ Jean.change_face("smirk2", eyes = "down")

            ch_Jean "I mean, obviously I look great. . ."

        $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            $ Jean.change_face("sexy")

            ch_Jean "I'd totally wear it for you. . ."
        elif dice_roll == 2:
            $ Jean.change_face("smirk2")

            ch_Jean "I'll wear it, for you."
        elif dice_roll == 3:
            $ Jean.change_face("sexy")

            ch_Jean "Sure, just for you."
    else:
        $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            $ Jean.change_face("worried1", eyes = "down", mouth = "lipbite", blush = 1)

            ch_Jean "I don't know about wearing this in public. . ." 
        elif dice_roll == 2:
            $ Jean.change_face("worried1", eyes = "down", blush = 1)

            ch_Jean "It's a little skimpy. . ." 
        elif dice_roll == 3:
            $ Jean.change_face("worried1", eyes = "down", blush = 1)

            ch_Jean "Just this, huh?" 
            ch_Jean "Pretty risqué, [Player.first_name]. . ."

        $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            $ Jean.change_face("sexy")

            ch_Jean "But when I'm alone with you. . ."
            ch_Jean "Yeah."
        elif dice_roll == 2:
            $ Jean.change_face("smirk2")

            ch_Jean "I'll wear it just for you, though. . ."
        elif dice_roll == 3:
            $ Jean.change_face("sexy")

            ch_Jean "Well, maybe just for you and me."

    return

label Jean_reject_private_Outfit(Outfit):
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        $ Jean.change_face("confused1", eyes = "down")

        ch_Jean "You actually want me to wear this?"
    elif dice_roll == 2:
        $ Jean.change_face("confused1", eyes = "down")

        ch_Jean "In what world. . ."
    elif dice_roll == 3:
        $ Jean.change_face("worried1", eyes = "down")

        ch_Jean ". . ."

    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        $ Jean.change_face("confused1")

        ch_Jean "Yeah, not gonna happen. Sorry."
    elif dice_roll == 2:
        $ Jean.change_face("confused1")

        ch_Jean "Maybe in your dreams, [Jean.Player_petname]. . ."
    elif dice_roll == 3:
        $ Jean.change_face("confused1")

        ch_Jean "I don't think so."

    return

label Jean_accept_public_Outfit(Outfit):
    if Outfit.shame < 500:
        $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            $ Jean.change_face("smirk2", eyes = "down")

            ch_Jean "Yeah, this is pretty nice."
        elif dice_roll == 2:
            $ Jean.change_face("pleased1", eyes = "down")

            ch_Jean "Huh, not bad. . ."
        elif dice_roll == 3:
            $ Jean.change_face("smirk2", eyes = "down")

            ch_Jean "I'm actually impressed, [Jean.Player_petname]."

        $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            $ Jean.change_face("smirk2")

            ch_Jean "I'll wear it around if you want."
        elif dice_roll == 2:
            $ Jean.change_face("happy")

            ch_Jean "I'll definitely wear it!"
        elif dice_roll == 3:
            $ Jean.change_face("smirk2")

            ch_Jean "I'll add it to the wardrobe."
    else:
        $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            $ Jean.change_face("worried1", eyes = "down", mouth = "lipbite", blush = 1)

            ch_Jean "You want me to wear this in public?" 
        elif dice_roll == 2:
            $ Jean.change_face("worried1", eyes = "down", blush = 1)

            ch_Jean "This, in public?"
        elif dice_roll == 3:
            $ Jean.change_face("worried1", eyes = "down", blush = 1)

            ch_Jean "I'm not sure. . ."

        $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            $ Jean.change_face("worried1", mouth = "lipbite", blush = 1)

            ch_Jean "Well. . . it's not that bad. . ."
            ch_Jean "Okay, fine."
        elif dice_roll == 2:
            $ Jean.change_face("worried1", blush = 1)

            ch_Jean ". . . I suppose I could wear it."
        elif dice_roll == 3:
            $ Jean.change_face("worried1", blush = 1)

            ch_Jean "I guess it could be alright."

    return

label Jean_reject_public_Outfit(Outfit):
    if Outfit.shame >= 500:
        $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            $ Jean.change_face("perplexed", blush = 1)

            ch_Jean "That was a joke, right?"
        elif dice_roll == 2:
            $ Jean.change_face("perplexed", blush = 1)

            ch_Jean "Really?"
        elif dice_roll == 3:
            $ Jean.change_face("confused1", blush = 1)

            ch_Jean "Very funny. . ."
    elif not Jean.check_traits("pussy_covered"):
        if not Jean.check_traits("breasts_covered"):
            $ Jean.change_face("confused1", blush = 1)

            ch_Jean "Ha Ha, very funny." 

            $ Jean.change_face("sly", blush = 1)

            ch_Jean "You just wanted an excuse to see me basically naked." 
            ch_Jean "Funny joke." 

            $ Jean.change_face("suspicious1", blush = 1)

            ch_Jean "It was a joke, right?" 

            $ Jean.change_face("angry1", blush = 1) 

            ch_Jean "As if I'd go walking around basically naked."
        else:
            $ Jean.change_face("confused1", eyes = "down", blush = 1)

            ch_Jean "You forgot the underwear part. . ."

            $ Jean.change_face("confused1", blush = 1)

            ch_Jean "I'd never wear something like this in public. . ."
    elif not Jean.check_traits("breasts_covered"):
        $ Jean.change_face("appalled2", blush = 1)

        ch_Jean "Do I really seem like the type of girl to walk around with her tits out?!"
    else:
        $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            $ Jean.change_face("confused1", mouth = "smirk")

            ch_Jean "You actually want to make an outfit for me?" 
            ch_Jean "Cute, but I can dress myself. . ."
        elif dice_roll == 2:
            $ Jean.change_face("confused1")

            ch_Jean "I like dressing myself."
        elif dice_roll == 3:
            $ Jean.change_face("confused1")

            ch_Jean "Don't need your help choosing outfits, [Player.first_name]."

    return

label Jean_reject_contextual_Outfit(Outfit):
    $ Jean.change_face("perplexed", blush = 1)

    ch_Jean "Kind of a weird place to wear this, [Jean.Player_petname]. . ."

    return