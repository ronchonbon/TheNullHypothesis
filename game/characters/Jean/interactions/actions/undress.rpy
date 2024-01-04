label Jean_not_wearing_Clothing_type(Clothing_type):
    if Clothing_type == "bra":
        $ Jean.change_face("worried2", mouth = "lipbite", blush = 1)

        ch_Jean "Kinda can't right now. . ." 

        $ Jean.change_face("sexy", blush = 1)

        ch_Jean "Not wearing one. . ."
    elif Clothing_type == "underwear":
        $ Jean.change_face("sly", mouth = "lipbite", blush = 1)

        ch_Jean "I'd show you. . ."
        ch_Jean ". . . if I was wearing any."

    return

label Jean_get_more_comfortable:
    ch_Jean "I'm a bit overdressed. . ."

    return

label Jean_rejects_show_bra:
    if Jean.History.check("seen_bra"):
        $ Jean.change_face("perplexed")

        ch_Jean "My bra? Now?" 

        $ Jean.change_face("confused1")

        ch_Jean "Sorry, no."
    else:
        $ dice_roll = renpy.random.randint(1, 2)

        if dice_roll == 1:
            $ Jean.change_face("perplexed", blush = 1)

            ch_Jean "My bra???" 

            $ Jean.change_face("worried1", mouth = "lipbite", blush = 1) 

            ch_Jean "I'm not ready for you to see that yet. . ."
        elif dice_roll == 2:
            $ Jean.change_face("confused1")

            ch_Jean "That's kinda weird. . ." 

    return

label Jean_rejects_show_bra_asked_once:
    call Jean_asked_once("showing")

    return

label Jean_rejects_show_bra_asked_twice:
    call Jean_asked_twice("showing")   
    call Jean_kicking_out
    call getting_kicked_out(Jean) from _call_getting_kicked_out_1

    return

label Jean_accepts_show_bra_before_first_time:
    $ Jean.change_face("surprised2", blush = 1)

    ch_Jean "You want to see my bra?!" 

    $ Jean.change_face("worried1", mouth = "lipbite", blush = 1)

    ch_Jean ". . . well, it is only you." 

    $ Jean.change_face("smirk2", mouth = "lipbite", blush = 1)

    ch_Jean "Okay fine. . ."

    return

label Jean_accepts_show_bra_before_second_time:
    $ Jean.change_face("sly", blush = 1)

    ch_Jean "You are always staring. . ." 

    $ Jean.change_face("sexy", blush = 1)

    ch_Jean "I guess it couldn't hurt."

    return

label Jean_accepts_show_bra_before:
    if Jean.Clothes["bra"].gift:
        $ dice_roll = renpy.random.randint(1, 4)
    else:
        $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Jean.change_face("sly")

        ch_Jean "Fine, you can have a treat."
    elif dice_roll == 2:
        $ Jean.change_face("confused1", mouth = "smirk")

        ch_Jean "You like looking that much?" 

        $ Jean.change_face("sly") 

        ch_Jean "Well. . . okay, fine." 
    elif dice_roll == 3:
        $ Jean.change_face("confused1", mouth = "smirk")

        ch_Jean "You did get it for me. . ." 

        $ Jean.change_face("sly") 

        ch_Jean "I bet you're dying to see me in this one."
    elif dice_roll == 4:
        $ Jean.change_face("sexy")

        ch_Jean "It's only fair. . ."
        ch_Jean "You got this one for me after all."

    return

label Jean_accepts_show_bra_before_love:
    if Jean.status["nympho"]:
        $ Jean.change_face("sexy", blush = 1)

        ch_Jean "You're gonna do more than just look later. . ."
    elif Jean.status["horny"]:
        $ Jean.change_face("worried2", mouth = "lipbite", blush = 1)

        ch_Jean "Fine, but I'm gonna need some attention later. . ."
    elif Jean.check_traits("quirk"):
        if Jean.Clothes["bra"].gift:
            $ dice_roll = renpy.random.randint(1, 5)
        else:
            $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            $ Jean.change_face("sly", mouth = "lipbite", blush = 1)

            ch_Jean "You have been a good little brother lately. . ." 
            ch_Jean "Fine, take a peek."
        elif dice_roll == 2:
            $ Jean.change_face("confused1", mouth = "lipbite", blush = 1)

            ch_Jean "Wanna see big sister's bra that badly?" 

            $ Jean.change_face("sly", mouth = "lipbite", blush = 1)

            ch_Jean "Fine, you can look."  
        elif dice_roll == 3:
            $ Jean.change_face("sly", blush = 1)

            ch_Jean "I bet you're hoping to see something poke through, huh." 
        elif dice_roll == 4:
            $ Jean.change_face("confused1", mouth = "lipbite", blush = 1)

            ch_Jean "You want to see the pretty bra you bought for your big sister?" 

            $ Jean.change_face("sly", mouth = "lipbite", blush = 1)

            ch_Jean "Okay, I'll give you a little treat."
        elif dice_roll == 5:
            $ Jean.change_face("confused1", mouth = "lipbite", blush = 1)

            ch_Jean "You just want to see me wearing the bra you bought." 

            $ Jean.change_face("sexy", blush = 1)

            ch_Jean "Say pretty please."
            ch_Player "Pretty please. . ." 

            $ Jean.change_face("sly", mouth = "lipbite", blush = 1)

            ch_Jean "Good boy, here. . ."
    else:
        if Jean.Clothes["bra"].gift:
            $ dice_roll = renpy.random.randint(1, 5)
        else:
            $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            $ Jean.change_face("sexy", blush = 1)

            ch_Jean "Oh okay, fine." 
            ch_Jean "Only a quick peek."
        elif dice_roll == 2:
            $ Jean.change_face("sexy", blush = 1)

            ch_Jean "Fiiiine." 
            ch_Jean "Only a quick peek though."
        elif dice_roll == 3:
            $ Jean.change_face("sly", blush = 1)

            ch_Jean "I bet you're hoping to see something poke through, huh." 
        elif dice_roll == 4:
            $ Jean.change_face("confused1", mouth = "lipbite", blush = 1)

            ch_Jean "Weeell you did buy me this one. . ." 

            $ Jean.change_face("sexy", blush = 1)

            ch_Jean "It's only fair."
        elif dice_roll == 5:
            $ Jean.change_face("sexy", blush = 1)

            ch_Jean "Fine, you can take a peek." 

            $ Jean.change_face("worried1", mouth = "lipbite", blush = 1)

            ch_Jean "I do appreciate the gift. . ."

    return

label Jean_accepts_show_bra_after_first_time:

    return

label Jean_accepts_show_bra_after_second_time:

    return

label Jean_accepts_show_bra_after:

    return

label Jean_accepts_show_bra_after_love:

    return

label Jean_rejects_show_underwear:
    if Jean.History.check("seen_underwear"):
        $ Jean.change_face("confused1")

        ch_Jean "I'm not in the mood right now."
    else:
        $ Jean.change_face("perplexed", blush = 1)

        ch_Jean "My panties?!" 

        $ Jean.change_face("confused1", blush = 1)

        ch_Jean "Why the hell would I show you those right now. . ." 

    return

label Jean_rejects_show_underwear_asked_once:
    call Jean_asked_once("showing")

    return

label Jean_rejects_show_underwear_asked_twice:  
    call Jean_asked_twice("showing")     
    call Jean_kicking_out
    call getting_kicked_out(Jean) from _call_getting_kicked_out_2

    return

label Jean_accepts_show_underwear_before_first_time:
    $ Jean.change_face("worried2", mouth = "lipbite", blush = 1)

    ch_Jean "My panties?!" 

    $ Jean.change_face("worried1", eyes = "right", mouth = "lipbite", blush = 1)

    ch_Jean "Well. . ." 

    $ Jean.change_face("sexy", blush = 1)

    ch_Jean "Screw it, here." 

    return

label Jean_accepts_show_underwear_before_second_time:
    $ Jean.change_face("confused1", mouth = "lipbite", blush = 1)

    ch_Jean "Again?" 

    $ Jean.change_face("sexy", blush = 1)

    ch_Jean "Heh, kinda weird. . . but I don't mind if it's you." 

    return

label Jean_accepts_show_underwear_before:
    if Jean.Clothes["underwear"].gift:
        $ dice_roll = renpy.random.randint(1, 5)
    else:
        $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        $ Jean.change_face("confused1", mouth = "lipbite", blush = 1)

        ch_Jean "You like looking?" 

        $ Jean.change_face("sexy", blush = 1)

        ch_Jean "Fine, here."
    elif dice_roll == 2:
        $ Jean.change_face("sexy", blush = 1)

        ch_Jean "Sure." 

        $ Jean.change_face("sexy", eyes = "down", blush = 1)

        ch_Jean "If you show me yours as well. . ." 
    elif dice_roll == 3:
        $ Jean.change_face("worried1", mouth = "lipbite", blush = 1)

        ch_Jean "You're really into this, huh. . ." 

        $ Jean.change_face("sly", mouth = "lipbite", blush = 1)

        ch_Jean "Not saying I'm not as well. . ."
    elif dice_roll == 4:
        $ Jean.change_face("sly", mouth = "lipbite", blush = 1)

        ch_Jean "They do look great on me." 

        $ Jean.change_face("sly", eyes = "down", mouth = "lipbite", blush = 1)

        ch_Jean "Thanks for the gift. . ."
    elif dice_roll == 5:
        $ Jean.change_face("sexy", blush = 1)

        ch_Jean "You have great taste." 

        $ Jean.change_face("sexy", eyes = "down", blush = 1)

        ch_Jean "I look fantastic in them." 
        
    return

label Jean_accepts_show_underwear_before_love:
    if Jean.check_traits("quirk"):
        if Jean.Clothes["underwear"].gift:
            if Jean.status["horny"] or Jean.status["nympho"]:
                $ dice_roll = renpy.random.randint(1, 6)
            else:
                $ dice_roll = renpy.random.randint(1, 5)
        else:
            $ dice_roll = renpy.random.randint(1, 4)

        if dice_roll == 1:
            $ Jean.change_face("confused1", mouth = "lipbite", blush = 1)

            ch_Jean "Wanna see your big sister's panties?" 

            $ Jean.change_face("sly", mouth = "lipbite", blush = 1)

            ch_Jean "Give me a peek at your underwear and maybe I'll let you."

            $ Jean.change_face("sexy", eyes = "down", blush = 1)

            "You do as she says."
            ch_Jean "Good boy, here."
        elif dice_roll == 2:
            $ Jean.change_face("confused1", mouth = "lipbite", blush = 1)

            ch_Jean "Remember to say please."

            $ Jean.change_face("sly", mouth = "lipbite", blush = 1)

            ch_Player "Please, [Jean.petname]?" 
            ch_Jean "Anything for you. . ."
        elif dice_roll == 3:
            $ Jean.change_face("confused1", mouth = "lipbite", blush = 1)

            ch_Jean "Wanna see them?" 

            $ Jean.change_face("sexy", eyes = "down", blush = 1)

            ch_Jean "Okay. . ."
        elif dice_roll == 4:
            $ Jean.change_face("confused1", eyes = "squint", mouth = "lipbite", blush = 1)

            ch_Jean "How badly do you wanna see them?" 
            ch_Player "Pretty badly. . ." 

            $ Jean.change_face("sly", mouth = "lipbite", blush = 1)

            ch_Jean "Gimme a kiss and I'll let you."

            $ Jean.change_face("kiss2", blush = 1)

            "You lean over and give her a quick kiss on the lips." 

            $ Jean.change_face("sexy", blush = 1)

            ch_Jean "Good boy, here."
        elif dice_roll == 5:
            $ Jean.change_face("sly", mouth = "lipbite", blush = 1)

            ch_Jean "I bet you're dying to see me in those panties you bought." 

            $ Jean.change_face("confused1", eyes = "squint", mouth = "lipbite", blush = 1)

            ch_Jean "Well you have been a good little brother." 

            $ Jean.change_face("sexy", eyes = "down", blush = 1)

            ch_Jean "Here, take a peek." 
        elif dice_roll == 6:
            $ Jean.change_face("confused1", eyes = "squint", mouth = "lipbite", blush = 1)

            ch_Jean "Trying to see if your big sister's panties are all wet?" 

            $ Jean.change_face("sexy", eyes = "down", blush = 1)

            ch_Jean "Take a peek. . ."
    else:
        if Jean.Clothes["underwear"].gift:
            if Jean.status["horny"] or Jean.status["nympho"]:
                $ dice_roll = renpy.random.randint(1, 6)
            else:
                $ dice_roll = renpy.random.randint(1, 5)
        else:
            $ dice_roll = renpy.random.randint(1, 4)

        if dice_roll == 1:
            $ Jean.change_face("sexy", eyes = "down", blush = 1)

            ch_Jean "It's not like I ever mind giving you a look. . ."
        elif dice_roll == 2:
            $ Jean.change_face("sly", mouth = "lipbite", blush = 1)

            ch_Jean "If you want to see more, you'll have to find me later. . ."
        elif dice_roll == 3:
            $ Jean.change_face("confused1", mouth = "lipbite", blush = 1)

            ch_Jean "This color looks great on me, right?"
        elif dice_roll == 4:
            $ Jean.change_face("confused1", mouth = "lipbite", blush = 1)

            ch_Jean "Wanna see them?" 

            $ Jean.change_face("sexy", eyes = "down", blush = 1)

            ch_Jean "Okay. . ."
        elif dice_roll == 5:
            $ Jean.change_face("confused1", mouth = "lipbite", blush = 1)

            ch_Jean "This color looks great on me, right?"
        elif dice_roll == 5:
            $ Jean.change_face("sexy", eyes = "down", blush = 1)

            ch_Jean "I really like this color. . . you chose well." 
        elif dice_roll == 6:
            $ Jean.change_face("sexy", eyes = "down", blush = 1)

            ch_Jean "I made the ones you got me wet. . ."

            $ Jean.change_face("confused1", mouth = "lipbite", blush = 1)

            ch_Jean  "I bet that makes you hard, huh."

    return

label Jean_accepts_show_underwear_after_first_time:

    return

label Jean_accepts_show_underwear_after_second_time:

    return

label Jean_accepts_show_underwear_after:

    return

label Jean_accepts_show_underwear_after_love:

    return

label Jean_rejects_show_breasts:
    if Jean.History.check("seen_breasts"):
        $ Jean.change_face("worried1")

        ch_Jean "I'm not really in the mood. . ."
    else:
        $ Jean.change_face("worried2", mouth = "lipbite", blush = 1)

        ch_Jean "I'm not ready to show them. . . to anyone yet. . ."

    return

label Jean_rejects_show_breasts_asked_once:
    call Jean_asked_once("showing")

    return

label Jean_rejects_show_breasts_asked_twice:
    call Jean_asked_twice("showing")     
    call Jean_kicking_out
    call getting_kicked_out(Jean) from _call_getting_kicked_out_3

    return

label Jean_accepts_show_breasts_before_first_time:
    $ Jean.change_face("worried2", blush = 1)

    pause 1.0

    $ Jean.change_face("worried1", mouth = "lipbite", blush = 1)  

    ch_Jean "I know you've been dreaming about seeing them. . ." 
    ch_Jean "I think I'm ready to show you. . ." 

    $ Jean.change_face("sly", mouth = "lipbite", blush = 1)  

    ch_Jean "God, you're the luckiest guy in the world right now."

    return

label Jean_accepts_show_breasts_before_second_time:
    $ Jean.change_face("sly", mouth = "lipbite", blush = 1)

    ch_Jean "I knew you loved them."
    ch_Jean "Can't get enough, huh?" 

    return

label Jean_accepts_show_breasts_before:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        $ Jean.change_face("worried1", mouth = "lipbite", blush = 1)

        ch_Jean "So you really do like them. . ."
    elif dice_roll == 2:
        $ Jean.change_face("sly", mouth = "lipbite", blush = 1)

        ch_Jean "I think you should touch them too. . . later. . ."
    elif dice_roll == 3:
        $ Jean.change_face("worried1", mouth = "lipbite", blush = 1)

        ch_Jean "They look great today too, right?"

    return

label Jean_accepts_show_breasts_before_love:
    if Jean.status["nympho"]:
        $ Jean.change_face("sly", mouth = "lipbite", blush = 1)

        ch_Jean "I'm totally making you play with them later. . ."
    elif Jean.status["horny"]:
        $ Jean.change_face("sexy", blush = 1)

        ch_Jean "I might need you for. . ." 

        $ Jean.change_face("sly", mouth = "lipbite", blush = 1)

        ch_Jean "I {i}will{/i} need you to take care of them later. . ."
    elif Jean.check_traits("quirk"):
        $ dice_roll = renpy.random.randint(1, 4)

        if dice_roll == 1:
            $ Jean.change_face("confused1", mouth = "lipbite", blush = 1)

            ch_Jean "Want to see your big sister's tits?" 
            ch_Jean "Only if you promise to keep being a good little brother. . ."

            $ Jean.change_face("sly", mouth = "lipbite", blush = 1)

            ch_Player "I promise. . ."
            ch_Jean "Good. . ."
        elif dice_roll == 2:
            $ Jean.change_face("sly", mouth = "lipbite", blush = 1)

            ch_Jean "I know you're in love with them." 
            ch_Jean "Maybe I'll let you touch them later too. . ." 
        elif dice_roll == 3:
            $ Jean.change_face("sly", mouth = "lipbite", blush = 1)

            ch_Jean "Makes me happy, knowing little brother likes them so much. . ."
        elif dice_roll == 4:
            $ Jean.change_face("confused1", mouth = "smirk", blush = 1)

            ch_Jean "I bet you just want to see if it's cold in here. . ."
    else:
        $ dice_roll = renpy.random.randint(1, 4)

        if dice_roll == 1:
            $ Jean.change_face("worried1", mouth = "lipbite", blush = 1)

            ch_Jean "So you agree, they're perfect, right?"
        elif dice_roll == 2:
            $ Jean.change_face("sly", mouth = "lipbite", blush = 1)

            ch_Jean "You really are the luckiest guy. . ."
        elif dice_roll == 3:
            $ Jean.change_face("worried1", mouth = "lipbite", blush = 1)

            ch_Jean "It makes me happy. . . knowing you like them so much. . ."
        elif dice_roll == 4:
            $ Jean.change_face("confused1", mouth = "smirk", blush = 1)

            ch_Jean "I bet you just want to see if it's cold in here. . ."

    return

label Jean_accepts_show_breasts_after_first_time:
    $ Jean.change_face("worried1", blush = 1) 
    
    ch_Jean "Well. . ." 
    ch_Jean "They're perfect, right?" 

    menu:
        extend ""
        "Absolutely perfect. . .":
            call change_Character_stat(Jean, "love", tiny_stat) from _call_change_Character_stat_27

            $ Jean.change_face("worried1", mouth = "lipbite", blush = 1)
        "They are pretty great.":
            $ Jean.change_face("smirk2")

            pause 1.0
            
            $ Jean.change_face("worried1", mouth = "lipbite", blush = 1)
        "They're. . . not bad. . .":
            call change_Character_stat(Jean, "love", -tiny_stat) from _call_change_Character_stat_381

            $ Jean.change_face("worried2", blush = 1) 

    return

label Jean_accepts_show_breasts_after_second_time:

    return

label Jean_accepts_show_breasts_after:

    return

label Jean_accepts_show_breasts_after_love:

    return

label Jean_rejects_show_pussy:
    if Jean.History.check("seen_pussy"):
        $ Jean.change_face("worried1", blush = 1)

        ch_Jean "Maybe later. . ."
    else:
        $ Jean.change_face("perplexed", blush = 1)

        ch_Jean "As if I'd show you my. . . right now. . ." 

    return

label Jean_rejects_show_pussy_asked_once:
    call Jean_asked_once("showing")

    return

label Jean_rejects_show_pussy_asked_twice:
    call Jean_asked_twice("showing")     
    call Jean_kicking_out
    call getting_kicked_out(Jean) from _call_getting_kicked_out_4

    return

label Jean_accepts_show_pussy_before_first_time:
    $ Jean.change_face("worried3", blush = 1)

    pause 1.0

    $ Jean.change_face("worried1", mouth = "lipbite", blush = 1)

    ch_Jean "You really want to see. . . my. . ." 

    $ Jean.change_face("sexy", blush = 1)

    ch_Jean "You better be thankful I like you so much." 

    $ Jean.change_face("worried1", mouth = "lipbite", blush = 1)

    ch_Jean "I've never shown anyone before. . ." 

    return

label Jean_accepts_show_pussy_before_second_time:
    $ Jean.change_face("sexy", eyes = "down", blush = 1)

    ch_Jean "It's pretty, right?" 

    return

label Jean_accepts_show_pussy_before:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        $ Jean.change_face("sly", mouth = "lipbite", blush = 1)

        ch_Jean "Heh, okay. . ." 
        ch_Jean "Maybe I'll let you touch it later. . ."
    elif dice_roll == 2:
        $ Jean.change_face("worried1", mouth = "lipbite", blush = 1)

        ch_Jean "You better be thankful. . ."
    elif dice_roll == 3:
        $ Jean.change_face("sexy", blush = 1)

        ch_Jean "Mmm, take a peek. . ."

    return

label Jean_accepts_show_pussy_before_love:
    if Jean.status["nympho"]:
        $ Jean.change_face("sly", mouth = "lipbite", blush = 1) 

        ch_Jean "I'm making you take care of it later. . ."
    elif Jean.status["horny"]:
        $ Jean.change_face("sexy", eyes = "down", blush = 1) 

        ch_Jean "Wanna see me drip?"
    elif Jean.check_traits("quirk"):
        $ dice_roll = renpy.random.randint(1, 4)

        if dice_roll == 1:
            $ Jean.change_face("sly", mouth = "lipbite", blush = 1)

            ch_Jean "Let me see yours and you can see mine. . ."

            $ Jean.change_face("sexy", eyes = "down", blush = 1)

            "You pull your pants down just enough." 
            ch_Jean ". . ." 
            ch_Jean "Mmm. . . here."
        elif dice_roll == 2:
            $ Jean.change_face("confused1", mouth = "lipbite", blush = 1)

            ch_Jean "Want a peek?" 

            $ Jean.change_face("sly", mouth = "lipbite", blush = 1)

            ch_Jean "You have been good lately. . ." 
            ch_Jean "Fine, only a quick one though." 
        elif dice_roll == 3:
            $ Jean.change_face("sexy", eyes = "down", blush = 1)

            ch_Jean "Okay, but first. . ."
            "She pulls your pants down just enough to expose you."

            $ Jean.change_face("sly", mouth = "lipbite", blush = 1) 

            ch_Jean "Now you get to see mine. . ."
        elif dice_roll == 4:
            $ Jean.change_face("confused1", mouth = "lipbite", blush = 1)

            ch_Jean "You just want to see if I'm wet. . ." 

            $ Jean.change_face("sly", mouth = "lipbite", blush = 1) 

            ch_Jean "You make it kinda hard not to be. . ."
    else:
        $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            $ Jean.change_face("sexy", eyes = "down", blush = 1)

            ch_Jean "Take a peek. . ."
        elif dice_roll == 2:
            $ Jean.change_face("sexy", eyes = "down", blush = 1)

            ch_Jean "I know you love it. . ." 
        elif dice_roll == 3:
            $ Jean.change_face("confused1", mouth = "lipbite", blush = 1)

            ch_Jean "You just want to see if I'm wet. . ." 

            $ Jean.change_face("sly", mouth = "lipbite", blush = 1) 

            ch_Jean "You make it kinda hard not to be. . ."

    return

label Jean_accepts_show_pussy_after_first_time:
    ch_Jean "You like it. . . right?" 

    menu:
        extend ""
        "It's beautiful.":
            call change_Character_stat(Jean, "love", tiny_stat) from _call_change_Character_stat_28
            
            $ Jean.change_face("sexy", blush = 1) 
            
            ch_Jean "I knew you would." 
        "Yeah, it's great. . .":
            $ Jean.change_face("worried1", mouth = "smirk", blush = 1) 
            
            ch_Jean "I knew it."
        "It's. . . fine.":
            call change_Character_stat(Jean, "love", -tiny_stat) from _call_change_Character_stat_382

            $ Jean.change_face("worried2", mouth = "lipbite", blush = 1) 
            
            ch_Jean "Fine?"

    return

label Jean_accepts_show_pussy_after_second_time:

    return

label Jean_accepts_show_pussy_after:

    return

label Jean_accepts_show_pussy_after_love:

    return

label Jean_rejects_give_bra:

    return

label Jean_rejects_give_bra_asked_once:

    return

label Jean_rejects_give_bra_asked_twice:  
    call Jean_kicking_out      
    call getting_kicked_out(Jean) from _call_getting_kicked_out_5

    return

label Jean_accepts_give_bra_before_first_time:

    return

label Jean_accepts_give_bra_before_second_time:

    return

label Jean_accepts_give_bra_before:

    return

label Jean_accepts_give_bra_before_love:

    return

label Jean_accepts_give_bra_after_first_time:

    return

label Jean_accepts_give_bra_after_second_time:

    return

label Jean_accepts_give_bra_after:

    return

label Jean_accepts_give_bra_after_love:

    return

label Jean_rejects_give_underwear:

    return

label Jean_rejects_give_underwear_asked_once:

    return

label Jean_rejects_give_underwear_asked_twice: 
    call Jean_kicking_out       
    call getting_kicked_out(Jean) from _call_getting_kicked_out_6

    return

label Jean_accepts_give_underwear_before_first_time:

    return

label Jean_accepts_give_underwear_before_second_time:

    return

label Jean_accepts_give_underwear_before:

    return

label Jean_accepts_give_underwear_before_love:

    return

label Jean_accepts_give_underwear_after_first_time:

    return

label Jean_accepts_give_underwear_after_second_time:

    return

label Jean_accepts_give_underwear_after:

    return

label Jean_accepts_give_underwear_after_love:

    return