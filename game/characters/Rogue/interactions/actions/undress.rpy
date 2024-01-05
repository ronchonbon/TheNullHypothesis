label Rogue_not_wearing_Clothing_type(Clothing_type):
    if Clothing_type == "bra":
        $ Rogue.change_face("worried1")

        ch_Rogue "But ah'm not wearin' one. . ."
    elif Clothing_type == "underwear":
        $ Rogue.change_face("worried1")

        ch_Rogue "Ah'm sorry, ah can't. . ."
        ch_Rogue "Ah'm not wearin' any. . ."

    return

label Rogue_get_more_comfortable:
    ch_Rogue "Ah should probably get a little more comfortable. . ."

    return

label Rogue_rejects_undressing:
    $ Rogue.change_face("worried1")

    ch_Rogue "Ah. . . ah don't want to undress right now. . ."

    return

label Rogue_rejects_show_bra:
    $ Rogue.change_face("confused1", blush = 1)

    $ dice_roll = renpy.random.randint(1, 2)

    if Rogue.History.check("seen_bra"):
        if dice_roll == 1:
            ch_Rogue "Ah'm not goin' topless."
        elif dice_roll == 2:
            ch_Rogue "Not happenin' right now."
    else:
        if dice_roll == 1:
            ch_Rogue "Ah'm not showin' you my bra. . ."
        elif dice_roll == 2:
            ch_Rogue "Why would ah show you my bra. . ."

    return

label Rogue_rejects_show_bra_asked_once:
    call Rogue_asked_once("showing") from _call_Rogue_asked_once_1

    if renpy.random.random() > 0.5:
        ch_Rogue "Yer not seein' my bra."

    return

label Rogue_rejects_show_bra_asked_twice:
    call Rogue_asked_twice("showing") from _call_Rogue_asked_twice_1
    call Rogue_kicking_out from _call_Rogue_kicking_out_1
    call getting_kicked_out(Rogue) from _call_getting_kicked_out_45

    return

label Rogue_accepts_show_bra_before_first_time:
    $ Rogue.change_face("surprised2", blush = 1)

    ch_Rogue "You want to see what. . . bra ah'm wearin'?"

    $ Rogue.mouth = "lipbite"
    $ Rogue.blush = 2

    ch_Rogue "Ah guess ah don't mind you seein'. . ."

    return

label Rogue_accepts_show_bra_before_second_time:
    $ Rogue.change_face("worried1", blush = 1)

    ch_Rogue "Ya want another look?"

    $ Rogue.change_face("smirk2")

    ch_Rogue "Alright. . ."

    return

label Rogue_accepts_show_bra_before:
    $ dice_roll = renpy.random.randint(1, 2)

    if Rogue.Clothes["bra"].gift:
        $ Rogue.change_face("smirk2")

        if dice_roll == 1:
            ch_Rogue "Ah'm wearin' the one you got me."
            ch_Rogue "Want a look?"
        elif dice_roll == 2:
            ch_Rogue "Ya want a peek?"
            ch_Rogue "Ah'm wearin' one ah got from you. . ."
    else:
        if dice_roll == 1:
            $ Rogue.change_face("smirk2")

            ch_Rogue "Ya want to see which one ah'm wearin'?"
            ch_Rogue "Sure. . ."
        elif dice_roll == 2:
            $ Rogue.change_face("confused1")

            ch_Rogue "You really like lookin' at my bra?"

            $ Rogue.change_face("smirk2", blush = 1)

            ch_Rogue "Ah don't mind. . ."

    return

label Rogue_accepts_show_bra_before_love:
    if Rogue.status["nympho"]:
        $ Rogue.change_face("sexy", blush = 2)
        
        ch_Rogue "Ah hope yer plannin' on doin' more than look later. . ."
    elif Rogue.status["horny"]:
        $ Rogue.change_face("worried1", blush = 1)

        ch_Rogue "Could ya. . . maybe do somethin' more with 'em later?"
    elif Rogue.check_traits("quirk"):
        $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

        if Rogue.Clothes["bra"].gift:
            $ dice_roll = renpy.random.randint(1, 4)
        else:
            $ dice_roll = renpy.random.randint(1, 2)

        if dice_roll == 1:
            ch_Rogue "If ya want a look at my bra, you can always just move my top out of the way. . ."
            ch_Rogue "Don't need to ask. . ."
        elif dice_roll == 2:
            ch_Rogue "You don't need to ask. . . just move my top out of the way. . ."
        elif dice_roll == 3:
            ch_Rogue "You bought this one for me. . . don't need my permission to see it. . ."
            ch_Rogue "Just take a peek whenever. . ."
        elif dice_roll == 4:
            ch_Rogue "You don't need permission. . ."
            ch_Rogue "You gave me this one anyway. . ."
            ch_Rogue "Just take a peek whenever. . ."
    else:
        $ Rogue.change_face("smirk2", blush = 1)

        if Rogue.Clothes["bra"].gift:
            $ dice_roll = renpy.random.randint(1, 4)
        else:
            $ dice_roll = renpy.random.randint(1, 2)

        if dice_roll == 1:
            ch_Rogue "Ya want to see which one ah'm wearin'?"

            if Rogue.History.check("seen_bra"):
                ch_Rogue "Not like you haven't seen it a million times by now. . ."
        elif dice_roll == 2:
            ch_Rogue "Ah never mind givin' ya a peek. . ."
        elif dice_roll == 3:
            ch_Rogue "Wanna see which one ah'm wearin'?"
            ch_Rogue "The one you gave me. . ."
            ch_Rogue "Not like you really have to ask."
        elif dice_roll == 4:
            ch_Rogue "Ah'm wearin' the one you got me. . ."
            ch_Rogue "You know ah never mind if you want a peek. . ."

    return

label Rogue_accepts_show_bra_after_first_time:

    return

label Rogue_accepts_show_bra_after_second_time:

    return

label Rogue_accepts_show_bra_after:

    return

label Rogue_accepts_show_bra_after_love:

    return

label Rogue_rejects_show_underwear:
    if Rogue.History.check("seen_underwear"):
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Rogue.change_face("confused1", blush = 1) 

        ch_Rogue "Not takin' my bottoms off."
    if dice_roll == 2:
        if Rogue.History.check("seen_underwear"):
            $ Rogue.change_face("neutral")

            ch_Rogue "Not right now. . ."
        else:
            $ Rogue.change_face("confused1")

            ch_Rogue "Now why would ah show you that?"

    return

label Rogue_rejects_show_underwear_asked_once:
    call Rogue_asked_once("showing") from _call_Rogue_asked_once_2

    return

label Rogue_rejects_show_underwear_asked_twice:
    call Rogue_asked_twice("showing") from _call_Rogue_asked_twice_2
    call Rogue_kicking_out from _call_Rogue_kicking_out_2
    call getting_kicked_out(Rogue) from _call_getting_kicked_out_46

    return

label Rogue_accepts_show_underwear_before_first_time:
    $ Rogue.change_face("worried1", blush = 1)

    ch_Rogue "You want to see my. . . underwear?"

    $ Rogue.blush = 2

    ch_Rogue "Here. . ."

    return

label Rogue_accepts_show_underwear_before_second_time:
    $ Rogue.change_face("worried1")

    ch_Rogue "Again?"

    $ Rogue.blush = 1

    ch_Rogue "Alright. . ."

    return

label Rogue_accepts_show_underwear_before:
    if Rogue.Clothes["underwear"].gift:
        $ dice_roll = renpy.random.randint(1, 2)

        if dice_roll == 1:
            $ Rogue.change_face("sexy", blush = 1)

            ch_Rogue "Wearin' the ones you got me. . ." 
            ch_Rogue "Take a look."
        elif dice_roll == 2:
            $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

            ch_Rogue "Ah'm wearin' the ones ya got me." 
            ch_Rogue "Ah really like 'em too. . ."
    else:
        $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

            ch_Rogue "You want to see which ones ah'm wearin'?" 
            ch_Rogue "Alright. . ."
        elif dice_roll == 2:
            $ Rogue.change_face("sexy", blush = 1)

            ch_Rogue "Ah never mind showing' you. . ."
        elif dice_roll == 3:
            $ Rogue.change_face("confused1", mouth = "smirk", blush = 1)

            ch_Rogue "Again?" 

            $ Rogue.change_face("sexy", blush = 1)

            ch_Rogue "Ah guess you really like lookin'. . ."

    return

label Rogue_accepts_show_underwear_before_love:
    if Rogue.check_traits("quirk"):
        if Rogue.Clothes["underwear"].gift:
            if Rogue.status["horny"] or Rogue.status["nympho"]:
                $ dice_roll = renpy.random.randint(1, 6)
            else:
                $ dice_roll = renpy.random.randint(1, 4)
        else:
            $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            $ Rogue.change_face("worried2", mouth = "lipbite", blush = 1)

            ch_Rogue "Sorry. . . they might be bit wet 'cause of you. . ."
        elif dice_roll == 2:
            $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

            ch_Rogue "Ah'd tell you if they were wet or not if ya wanted to know. . ."
        elif dice_roll == 3:
            $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

            ch_Rogue "Not like ya really need my permission. . ." 
        elif dice_roll == 4:
            $ Rogue.change_face("sexy", blush = 1)

            ch_Rogue "You got me these. . ." 

            $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

            ch_Rogue "Not like you need permission to see me in 'em."
        elif dice_roll == 5:
            $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

            ch_Rogue "Ah'm sorry [Rogue.Player_petname]. . ." 
            ch_Rogue "Ah couldn't help gettin' yer gift wet. . ."
    else:
        if Rogue.Clothes["underwear"].gift:
            $ dice_roll = renpy.random.randint(1, 5)
        else:
            $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            $ Rogue.change_face("sly", mouth = "lipbite", blush = 1)

            ch_Rogue "Ah know you like peekin'. . ."
        elif dice_roll == 2:
            $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

            ch_Rogue "They might still be a bit wet. . ."

            $ Rogue.change_face("sly", mouth = "lipbite", blush = 1)

            ch_Rogue "And it's all yer fault. . ."
        elif dice_roll == 3:
            $ Rogue.change_face("sly", mouth = "lipbite", blush = 1)

            ch_Rogue "Wanna see which one's ah'm wearin'?" 
        elif dice_roll == 4:
            $ Rogue.change_face("sly", mouth = "lipbite", blush = 1)

            ch_Rogue "Wanna see?" 
            ch_Rogue "You got 'em for me after all. . ."
        elif dice_roll == 5:
            $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

            ch_Rogue "They're quite nice. . ." 
            ch_Rogue "Ah still appreciate the gift. . ."

    return

label Rogue_accepts_show_underwear_after_first_time:

    return

label Rogue_accepts_show_underwear_after_second_time:

    return

label Rogue_accepts_show_underwear_after:

    return

label Rogue_accepts_show_underwear_after_love:

    return

label Rogue_rejects_show_breasts:
    if Rogue.History.check("seen_underwear") and not Rogue.History.check("seen_breasts"):
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    if dice_roll == 1:
        if Rogue.History.check("seen_breasts"):
            $ Rogue.change_face("confused1")

            ch_Rogue "Ah'm not doin' that right now. . ."
        else:
            $ Rogue.change_face("worried1")
            
            ch_Rogue "Ah'm not showin' you my. . ."
    if dice_roll == 2:
        $ Rogue.change_face("neutral", eyes = "squint", blush = 1) 

        ch_Rogue "Ah let you see my underwear, that's enough for now."

    return

label Rogue_rejects_show_breasts_asked_once:
    call Rogue_asked_once("showing") from _call_Rogue_asked_once_3

    return

label Rogue_rejects_show_breasts_asked_twice:
    call Rogue_asked_twice("showing") from _call_Rogue_asked_twice_3
    call Rogue_kicking_out from _call_Rogue_kicking_out_3
    call getting_kicked_out(Rogue) from _call_getting_kicked_out_47

    return

label Rogue_accepts_show_breasts_before_first_time:
    $ Rogue.change_face("worried2", mouth = "lipbite", blush = 1)

    ch_Rogue "Well. . ."

    $ Rogue.change_face("worried1", mouth = "smirk", blush = 1)

    ch_Rogue "If it's you, ah don't mind. . ."

    return

label Rogue_accepts_show_breasts_before_second_time:
    $ Rogue.change_face("worried1", mouth = "smirk", blush = 1)

    ch_Rogue "So you really do like 'em. . ."

    return

label Rogue_accepts_show_breasts_before:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        $ Rogue.change_face("worried1", mouth = "smirk", blush = 1)

        ch_Rogue "Makes me happy knowin' you like 'em. . ."
    elif dice_roll == 2:
        $ Rogue.change_face("sly", mouth = "lipbite", blush = 1)

        ch_Rogue "Wanna touch em' later?"
    elif dice_roll == 3:
        $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

        ch_Rogue "Ah never mind showin' you. . ."

    return

label Rogue_accepts_show_breasts_before_love:
    if Rogue.status["nympho"]:
        $ Rogue.change_face("worried2", mouth = "lipbite", blush = 1)

        ch_Rogue "Ah sure hope you plan on doin' more than just lookin'. . ."
    elif Rogue.status["horny"]:
        $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

        ch_Rogue "They're beggin' for you to touch 'em. . ."
    elif Rogue.check_traits("quirk"):
        $ dice_roll = renpy.random.randint(1, 4)

        if dice_roll == 1:
            $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

            ch_Rogue "Ah'm sorry, [Rogue.Player_petname]."
            ch_Rogue "Ah didn't mean to make ya think you had to actually ask first. . ." 

            $ Rogue.change_face("sexy", blush = 1)

            ch_Rogue "Just pull my top out of the way whenever ya want a look. . ."
        elif dice_roll == 2:
            $ Rogue.change_face("sexy", blush = 1)

            ch_Rogue "Ya'know they're all yours to see. . ."
        elif dice_roll == 3:
            $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

            ch_Rogue "Thank you. . ." 
            ch_Rogue "It makes me happy knowin' you like em' so much." 
            ch_Rogue "Don't even ask first next time. . ." 
        elif dice_roll == 4:
            $ Rogue.change_face("sly", mouth = "lipbite", blush = 1)

            ch_Rogue "Tryin' to see if my nipples are hard?"
    else:
        $ dice_roll = renpy.random.randint(1, 4)

        if dice_roll == 1:
            $ Rogue.change_face("sexy", blush = 1)

            ch_Rogue "Look whenever ya like." 
        elif dice_roll == 2:
            $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

            ch_Rogue "Ya really do love 'em, huh?"
        elif dice_roll == 3:
            $ Rogue.change_face("confused1", mouth = "lipbite", blush = 1)

            ch_Rogue "You gonna touch 'em too?"
        elif dice_roll == 4:
            $ Rogue.change_face("sly", mouth = "lipbite", blush = 1)

            ch_Rogue "Tryin' to see if my nipples are hard?"

    return

label Rogue_accepts_show_breasts_after_first_time:
    $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1) 
    
    ch_Rogue "Are they. . . any good?"

    menu:
        extend ""
        "Any good? They're perfect.":
            call change_Character_stat(Laura, "love", tiny_stat) from _call_change_Character_stat_476

            $ Rogue.change_face("worried1", mouth = "smirk", blush = 1) 
        "They are more than good.":
            $ Rogue.change_face("worried1", mouth = "smirk", blush = 1)
        "They're. . . okay. . .":
            call change_Character_stat(Rogue, "love", -tiny_stat) from _call_change_Character_stat_477

            $ Rogue.change_face("worried1", eyes = "down", blush = 1)

    return

label Rogue_accepts_show_breasts_after_second_time:

    return

label Rogue_accepts_show_breasts_after:

    return

label Rogue_accepts_show_breasts_after_love:

    return

label Rogue_rejects_show_pussy:
    if Rogue.History.check("seen_pussy"):
        $ Rogue.change_face("worried1")

        ch_Rogue "Not right now, ah'm not in the mood." 
    else:
        if Rogue.History.check("seen_underwear"):
            $ dice_roll = renpy.random.randint(1, 2)
        else:
            $ dice_roll = renpy.random.randint(1, 1)

        if dice_roll == 1:
            $ Rogue.change_face("perplexed")

            ch_Rogue "My. . . why would ah just show you that?!"
        elif dice_roll == 2:
            $ Rogue.change_face("smirk2", eyes = "squint", blush = 1) 

            ch_Rogue "A look at my underwear is all yer gettin'." 

    return

label Rogue_rejects_show_pussy_asked_once:
    call Rogue_asked_once("showing") from _call_Rogue_asked_once_4

    return

label Rogue_rejects_show_pussy_asked_twice:      
    call Rogue_asked_twice("showing") from _call_Rogue_asked_twice_4
    call Rogue_kicking_out from _call_Rogue_kicking_out_4
    call getting_kicked_out(Rogue) from _call_getting_kicked_out_48

    return

label Rogue_accepts_show_pussy_before_first_time:
    $ Rogue.change_face("worried3", blush = 1)

    ch_Rogue "You want to see my. . ."

    if not approval_check(Rogue, threshold = "touch_pussy"):
        $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

        ch_Rogue "Alright, but no touchin' yet please. . ."

    return

label Rogue_accepts_show_pussy_before_second_time:
    $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

    ch_Rogue "Oh alright. . . only real quick. . ."

    return

label Rogue_accepts_show_pussy_before:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        $ Rogue.change_face("sexy", blush = 1)

        ch_Rogue "You sure do like lookin' at it, huh?"
    elif dice_roll == 2:
        $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

        ch_Rogue "Ah don't mind, but. . ." 
        ch_Rogue "Oh alright. . ."
    elif dice_roll == 3:
        $ Rogue.change_face("sly", blush = 1)

        ch_Rogue "Here, ah'll let ya have a peek. . ."

    return

label Rogue_accepts_show_pussy_before_love:
    if Rogue.status["nympho"]:
        $ Rogue.change_face("worried2", mouth = "lipbite", blush = 1)

        ch_Rogue "Please don't just look. . ." 
        ch_Rogue "Do somethin' about it. . ."
    elif Rogue.status["horny"]:
        $ Rogue.change_face("sly", mouth = "lipbite", blush = 1)

        ch_Rogue "Ah know ya like to see it drippin'. . ."
        ch_Rogue "It always happens when ah think of you."
    elif Rogue.check_traits("quirk"):
        $ dice_roll = renpy.random.randint(1, 4)

        if dice_roll == 1:
            $ Rogue.change_face("sly", mouth = "lipbite", blush = 1)

            ch_Rogue "It's yers to look at whenever ya want. . ."
        elif dice_roll == 2:
            $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

            ch_Rogue "Ah don't know why ya even asked. . ." 
            ch_Rogue "Don't need my permission. . ."
        elif dice_roll == 3:
            $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

            ch_Rogue "Why are ya even askin'. . ." 
            ch_Rogue "It's yours. . ."
        elif dice_roll == 4:
            $ Rogue.change_face("sly", mouth = "lipbite", blush = 1)

            ch_Rogue "Tryin' to see if ah'm wet or not?"
    else:
        $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            $ Rogue.change_face("sly", mouth = "lipbite", blush = 1)

            ch_Rogue "Want a look? Just say the word. . ."
        elif dice_roll == 2:
            $ Rogue.change_face("sexy", blush = 1)

            ch_Rogue "Ah'm glad ya like it. . ."
        elif dice_roll == 3:
            $ Rogue.change_face("sly", mouth = "lipbite", blush = 1)

            ch_Rogue "Tryin' to see if ah'm wet or not?"

    return

label Rogue_accepts_show_pussy_after_first_time:
    $ Rogue.change_face("worried2", mouth = "lipbite", blush = 1) 
    
    ch_Rogue "Do you. . . like it?" 

    menu:
        extend ""
        ". . . I love it.":
            call change_Character_stat(Laura, "love", tiny_stat) from _call_change_Character_stat_478
            
            $ Rogue.change_face("worried1", mouth = "smirk", blush = 1) 
        "I do, it's beautiful.":
            $ Rogue.change_face("worried1", mouth = "smirk", blush = 1)
        "It's. . . okay. . .":
            call change_Character_stat(Rogue, "love", -tiny_stat) from _call_change_Character_stat_479

            $ Rogue.change_face("worried1", eyes = "down", blush = 1) 

    return

label Rogue_accepts_show_pussy_after_second_time:

    return

label Rogue_accepts_show_pussy_after:

    return

label Rogue_accepts_show_pussy_after_love:

    return

label Rogue_rejects_give_bra:

    return

label Rogue_rejects_give_bra_asked_once:

    return

label Rogue_rejects_give_bra_asked_twice:        
    call Rogue_kicking_out from _call_Rogue_kicking_out_5
    call getting_kicked_out(Rogue) from _call_getting_kicked_out_49

    return

label Rogue_accepts_give_bra_before_first_time:

    return

label Rogue_accepts_give_bra_before_second_time:

    return

label Rogue_accepts_give_bra_before:

    return

label Rogue_accepts_give_bra_before_love:

    return

label Rogue_accepts_give_bra_after_first_time:

    return

label Rogue_accepts_give_bra_after_second_time:

    return

label Rogue_accepts_give_bra_after:

    return

label Rogue_accepts_give_bra_after_love:

    return

label Rogue_rejects_give_underwear:

    return

label Rogue_rejects_give_underwear_asked_once:

    return

label Rogue_rejects_give_underwear_asked_twice:  
    call Rogue_kicking_out from _call_Rogue_kicking_out_6      
    call getting_kicked_out(Rogue) from _call_getting_kicked_out_50

    return

label Rogue_accepts_give_underwear_before_first_time:

    return

label Rogue_accepts_give_underwear_before_second_time:

    return

label Rogue_accepts_give_underwear_before:

    return

label Rogue_accepts_give_underwear_before_love:

    return

label Rogue_accepts_give_underwear_after_first_time:

    return

label Rogue_accepts_give_underwear_after_second_time:

    return

label Rogue_accepts_give_underwear_after:

    return

label Rogue_accepts_give_underwear_after_love:

    return