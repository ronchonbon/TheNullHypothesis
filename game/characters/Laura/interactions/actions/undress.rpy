label Laura_not_wearing_Clothing_type(Clothing_type):
    if Clothing_type == "bra":
        $ Laura.change_face("confused1", eyes = "squint", mouth = "lipbite", blush = 1)

        ch_Laura "Like you didn't know I wasn't wearing one." 
    elif Clothing_type == "underwear":
        $ Laura.change_face("sly", blush = 1)

        ch_Laura "Not wearing any. . ." 

        $ Laura.change_face("sexy", eyes = "down", blush = 1)

        ch_Laura "Maybe you should go take yours off too. . ."

    return

label Laura_get_more_comfortable:
    ch_Laura "I have some clothing in the way."

    return

label Laura_rejects_show_bra:
    $ dice_roll = renpy.random.randint(1, 2)

    if Laura.History.check("seen_bra"):
        if dice_roll == 1:
            $ Laura.change_face("neutral", eyes = "squint", blush = 1)

            ch_Laura "I'm not taking my top off."
        elif dice_roll == 2:
            $ Laura.change_face("angry1")

            ch_Laura "Not now."
    else:
        if dice_roll == 1:
            $ Laura.change_face("confused1")

            ch_Laura "Why would you want to see that?"
        elif dice_roll == 2:
            $ Laura.change_face("suspicious1")

            ch_Laura "Like I just go around showing people that."

    return

label Laura_rejects_show_bra_asked_once:
    call Laura_asked_once("showing")

    return

label Laura_rejects_show_bra_asked_twice:
    call Laura_asked_twice("showing")
    call Laura_kicking_out
    call getting_kicked_out(Laura) from _call_getting_kicked_out_23

    return

label Laura_accepts_show_bra_before_first_time:
    $ Laura.change_face("confused2", blush = 1)

    ch_Laura "Do guys like that kind of thing?" 

    $ Laura.change_face("sly", blush = 1)

    ch_Laura "I'll let you see it."

    return

label Laura_accepts_show_bra_before_second_time:
    $ Laura.change_face("confused1", mouth = "smirk", blush = 1)

    ch_Laura "Again?"

    $ Laura.change_face("sly", blush = 1)

    ch_Laura "Fine."

    return

label Laura_accepts_show_bra_before:
    $ dice_roll = renpy.random.randint(1, 2)

    if Laura.Clothes["bra"].gift:
        if dice_roll == 1:
            $ Laura.change_face("sly", blush = 1)

            ch_Laura "I'm wearing the one you bought me." 

            $ Laura.change_face("smirk2", eyes = "down", blush = 1)

            ch_Laura "Surprisingly comfortable."
        elif dice_roll == 2:
            $ Laura.change_face("smirk2", eyes = "down", blush = 1)

            ch_Laura "Take a look." 
            ch_Laura "It's the one you got me."
    else:
        if dice_roll == 1:
            $ Laura.change_face("sly", blush = 1)

            ch_Laura ". . ."
        elif dice_roll == 2:
            $ Laura.change_face("confused1", mouth = "smirk", blush = 1)

            ch_Laura "Kinda weird. . ." 

            $ Laura.change_face("sly", blush = 1)

            ch_Laura "Whatever."

    return

label Laura_accepts_show_bra_before_love:
    if Laura.status["nympho"]:
        $ Laura.change_face("angry1", mouth = "lipbite", blush = 1)

        ch_Laura "Better be ready to work on them later."
    elif Laura.status["horny"]:
        $ Laura.change_face("sly", mouth = "lipbite", blush = 1)

        ch_Laura "I bet you just want to look at my nipples poking through."
    elif Laura.check_traits("quirk"):
        if Laura.Clothes["bra"].gift:
            $ dice_roll = renpy.random.randint(1, 5)
        else:
            $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            $ Laura.change_face("confused1", mouth = "lipbite", blush = 1)

            ch_Laura "It makes you hard, right?" 

            $ Laura.change_face("sexy", eyes = "down", blush = 1)

            "As she shows you, she reaches down and grabs your crotch." 

            $ Laura.change_face("sly", mouth = "lipbite", blush = 1)

            ch_Laura "Knew it."
        elif dice_roll == 2:
            $ Laura.change_face("sly", mouth = "lipbite", blush = 1)

            ch_Laura "Fine." 
            ch_Laura "As long as you're mine, you can see it whenever you want."
        elif dice_roll == 3:
            $ Laura.change_face("sly", mouth = "lipbite", blush = 1)

            ch_Laura "I bet you're trying to imagine what I look like without them on."
        elif dice_roll == 4:
            $ Laura.change_face("confused1", eyes = "squint", mouth = "lipbite", blush = 1)

            ch_Laura "Trying to see the bra you bought me?" 

            $ Laura.change_face("sly", mouth = "lipbite", blush = 1)

            ch_Laura "Fine."
        elif dice_roll == 5:
            $ Laura.change_face("sly", mouth = "lipbite", blush = 1)

            ch_Laura "It's the one you bought for me." 
            ch_Laura "I know you get off on that."
    else:
        if Laura.Clothes["bra"].gift:
            $ dice_roll = renpy.random.randint(1, 5)
        else:
            $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            $ Laura.change_face("confused1", mouth = "lipbite", blush = 1)

            ch_Laura "Fine, I'll give you a look." 

            $ Laura.change_face("sly", mouth = "lipbite", blush = 1)

            ch_Laura "You're always staring anyway."
        elif dice_roll == 2:
            $ Laura.change_face("sly", mouth = "lipbite", blush = 1)

            ch_Laura "Trying to find an excuse to look at my tits?"
        elif dice_roll == 3:
            $ Laura.change_face("sly", mouth = "lipbite", blush = 1)

            ch_Laura "I bet you're trying to imagine what I look like without them on."
        elif dice_roll == 4:
            $ Laura.change_face("sly", mouth = "lipbite", blush = 1)

            ch_Laura "I'm wearing the one you bought."
            ch_Laura "You're welcome."
        elif dice_roll == 5:
            $ Laura.change_face("confused1", mouth = "lipbite", blush = 1)
                
            ch_Laura "Again? Weirdo." 

            $ Laura.change_face("sly", mouth = "lipbite", blush = 1)

            ch_Laura "Whatever, you're my weirdo."

    return

label Laura_accepts_show_bra_after_first_time:

    return

label Laura_accepts_show_bra_after_second_time:

    return

label Laura_accepts_show_bra_after:

    return

label Laura_accepts_show_bra_after_love:

    return

label Laura_rejects_show_underwear:
    if Laura.History.check("seen_underwear"):
        $ Laura.change_face("neutral")

        ch_Laura "Not in the mood."
    else:
        $ dice_roll = renpy.random.randint(1, 2)

        if dice_roll == 1:
            $ Laura.change_face("neutral", eyes = "squint", blush = 1)

            ch_Laura "Pants stay on."
        elif dice_roll == 2:
            $ Laura.change_face("confused1")

            ch_Laura "Yeah, not doing that."

    return

label Laura_rejects_show_underwear_asked_once:
    call Laura_asked_once("showing")

    return

label Laura_rejects_show_underwear_asked_twice:     
    call Laura_asked_twice("showing") 
    call Laura_kicking_out
    call getting_kicked_out(Laura) from _call_getting_kicked_out_24

    return

label Laura_accepts_show_underwear_before_first_time:
    $ Laura.change_face("confused3", blush = 1)

    ch_Laura "You want to look at it?" 

    $ Laura.change_face("sexy", eyes = "down", blush = 1) 

    ch_Laura "Let me see yours, and I'll show you. . ." 
    "You pull your pants down a bit, exposing your underwear."
    ch_Laura ". . . here."

    return

label Laura_accepts_show_underwear_before_second_time:
    $ Laura.change_face("confused1", eyes = "squint", mouth = "smirk", blush = 1) 

    ch_Laura "Just looking?" 
    ch_Laura "Fine." 
    ch_Laura ". . . weirdo." 

    return

label Laura_accepts_show_underwear_before:
    if Laura.Clothes["underwear"].gift:
        $ dice_roll = renpy.random.randint(1, 5)
    else:
        $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        $ Laura.change_face("confused1", blush = 1)

        ch_Laura "Again?" 

        $ Laura.change_face("sly", blush = 1)

        ch_Laura "Fine." 
    elif dice_roll == 2:
        $ Laura.change_face("sly", blush = 1)

        ch_Laura "Fine." 
        ch_Laura "Don't mind giving you a look. . . occasionally." 
    elif dice_roll == 3:
        $ Laura.change_face("confused1", blush = 1)

        ch_Laura "Another look?" 
        ch_Laura "Is this some weird 'fetish' thing?"
    elif dice_roll == 4:
        $ Laura.change_face("sly", blush = 1)

        ch_Laura "You bought me these." 
        ch_Laura "Surprisingly comfortable."
    elif dice_roll == 5:
        $ Laura.change_face("sly", blush = 1)

        ch_Laura "Only fair since you bought them. . ." 

    return

label Laura_accepts_show_underwear_before_love:
    if Laura.check_traits("quirk"):
        if Laura.Clothes["underwear"].gift:
            if Laura.status["horny"] or Laura.status["nympho"]:
                $ dice_roll = renpy.random.randint(1, 6)
            else:
                $ dice_roll = renpy.random.randint(1, 5)
        else:
            $ dice_roll = renpy.random.randint(1, 4)

        if dice_roll == 1:
            $ Laura.change_face("sly", mouth = "lipbite", blush = 1)

            ch_Laura "You can look." 
            ch_Laura "But you're doing more than that, later." 

            $ Laura.change_face("sexy", eyes = "down", blush = 1)

            "After showing you, she reaches over and looks down your pants as well."
        elif dice_roll == 2:
            $ Laura.change_face("confused1", mouth = "lipbite", blush = 1)

            ch_Laura "Just looking?" 

            $ Laura.change_face("sly", mouth = "lipbite", blush = 1)

            ch_Laura "Fine, I'll just make you touch it later." 
        elif dice_roll == 3:
            $ Laura.change_face("confused1", mouth = "lipbite", blush = 1)

            ch_Laura "Trying to see if my underwear is wet?" 

            $ Laura.change_face("sly", mouth = "lipbite", blush = 1)

            ch_Laura "You're going to deal with it later anyway."
        elif dice_roll == 4:
            $ Laura.change_face("sly", blush = 1)

            ch_Laura "Needed an excuse to look at my crotch?"
        elif dice_roll == 5:
            $ Laura.change_face("sexy", blush = 1)

            ch_Laura "You got me these." 

            $ Laura.change_face("sly", mouth = "lipbite", blush = 1)

            ch_Laura "I bet that makes you hard or something."
            ch_Laura "Weirdo." 
        elif dice_roll == 6:
            $ Laura.change_face("sexy", blush = 1)

            ch_Laura "I soaked through your gift." 

            $ Laura.change_face("sly", mouth = "lipbite", blush = 1)

            ch_Laura "I know you get off on that."
    else:
        if Laura.Clothes["underwear"].gift:
            $ dice_roll = renpy.random.randint(1, 6)
        else:
            $ dice_roll = renpy.random.randint(1, 4)

        if dice_roll == 1:
            $ Laura.change_face("confused1", mouth = "lipbite", blush = 1)

            ch_Laura "Still don't really get it."

            $ Laura.change_face("sexy", blush = 1)

            ch_Laura "But fine."
        elif dice_roll == 2:
            $ Laura.change_face("confused1", mouth = "lipbite", blush = 1)

            if Laura.History.check("seen_underwear"):
                ch_Laura "Again?" 

                ch_Laura "Not like you haven't seen them a million times."
        elif dice_roll == 3:
            $ Laura.change_face("sexy", blush = 1)

            ch_Laura "Fine, only a quick one."
        elif dice_roll == 4:
            $ Laura.change_face("sly", blush = 1)

            ch_Laura "Needed an excuse to look at my crotch?"
        elif dice_roll == 5:
            $ Laura.change_face("sexy", blush = 1)

            ch_Laura "Take a look." 

            $ Laura.change_face("sexy", eyes = "down", blush = 1)

            ch_Laura "Was a good gift in hindsight. . ." 
            ch_Laura "Thanks."
        elif dice_roll == 6:
            $ Laura.change_face("sexy", blush = 1)

            ch_Laura "Wore them during training the other day. . ." 
            ch_Laura "Good gift, thanks." 

            $ Laura.change_face("sexy", eyes = "down", blush = 1)

            ch_Laura "Like how they look?"

    return

label Laura_accepts_show_underwear_after_first_time:

    return

label Laura_accepts_show_underwear_after_second_time:

    return

label Laura_accepts_show_underwear_after:

    return

label Laura_accepts_show_underwear_after_love:

    return

label Laura_rejects_show_breasts:
    if Laura.History.check("seen_breasts"):
        $ Laura.change_face("neutral")

        ch_Laura "Not right now."
    else:
        if Laura.History.check("seen_bra"):
            $ dice_roll = renpy.random.randint(1, 2)
        else:
            $ dice_roll = renpy.random.randint(1, 1)

        if dice_roll == 1:
            $ Laura.change_face("confused3", blush = 1)

            ch_Laura "The hell?" 

            $ Laura.change_face("angry1", blush = 1)

            ch_Laura "No."
        elif dice_roll == 2:
            ch_Laura "You already saw my bra, that's enough."

    return

label Laura_rejects_show_breasts_asked_once:
    call Laura_asked_once("showing")

    return

label Laura_rejects_show_breasts_asked_twice:
    call Laura_asked_twice("showing") 
    call Laura_kicking_out
    call getting_kicked_out(Laura) from _call_getting_kicked_out_25

    return

label Laura_accepts_show_breasts_before_first_time:
    $ Laura.change_face("confused2", blush = 1)

    ch_Laura "You want to see them?" 
    ch_Laura "Is that normal, or are you just. . ."

    $ Laura.change_face("sexy", blush = 1)

    ch_Laura "Fine, you can look."

    return

label Laura_accepts_show_breasts_before_second_time:
    $ Laura.change_face("confused1", mouth = "smirk", blush = 1)

    ch_Laura "Again? Really?" 

    $ Laura.change_face("sexy", blush = 1)

    ch_Laura "Fine." 
    ch_Laura "I know you like them."

    return

label Laura_accepts_show_breasts_before:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        $ Laura.change_face("sly", blush = 1)

        ch_Laura "Fine." 
        ch_Laura "Take a peek, weirdo."
    elif dice_roll == 2:
        $ Laura.change_face("confused1", mouth = "smirk", blush = 1)

        ch_Laura "Wanna see them again?" 

        $ Laura.change_face("sexy", blush = 1)

        ch_Laura "Fine."
    elif dice_roll == 3:
        $ Laura.change_face("confused1", mouth = "smirk", blush = 1)

        ch_Laura "Haven't seen them enough yet?" 

        $ Laura.change_face("sexy", blush = 1)

        ch_Laura "Fine."

    return

label Laura_accepts_show_breasts_before_love:
    if Laura.status["nympho"]:
        $ Laura.change_face("sly", mouth = "lipbite", blush = 1)

        ch_Laura "You can look for now. . ." 
        ch_Laura "Better be prepared to get pounced on later."
    elif Laura.status["horny"]:
        $ Laura.change_face("sly", mouth = "lipbite", blush = 1)

        ch_Laura "Here." 
        ch_Laura "I think you can tell they want your attention."
    elif Laura.check_traits("quirk"):
        $ dice_roll = renpy.random.randint(1, 4)

        if dice_roll == 1:
            $ Laura.change_face("confused1", mouth = "lipbite", blush = 1)

            ch_Laura "Makes you hard looking at them, right?" 

            $ Laura.change_face("sly", mouth = "lipbite", blush = 1)

            ch_Laura "Fine, but don't be surprised when I make you take your shirt off later. . ."
        elif dice_roll == 2:
            $ Laura.change_face("sly", mouth = "lipbite", blush = 1)

            ch_Laura "Fine, but first." 

            $ Laura.change_face("sexy", eyes = "down", blush = 1)

            "She reaches down and gropes you, leaving her hand on your crotch." 

            $ Laura.change_face("sly", mouth = "lipbite", blush = 1)

            ch_Laura "I want to feel you get hard."
        elif dice_roll == 3:
            $ Laura.change_face("sly", mouth = "lipbite", blush = 1)

            ch_Laura "Fine, but don't be surprised when I make you touch them later."
        elif dice_roll == 4:
            $ Laura.change_face("sly", mouth = "lipbite", blush = 1)

            ch_Laura "I bet you just want to see if my nipples are hard." 
            ch_Laura "Weirdo."
    else:
        $ dice_roll = renpy.random.randint(1, 4)

        if dice_roll == 1:
            $ Laura.change_face("confused1", mouth = "lipbite", blush = 1)

            ch_Laura "You like them that much?" 

            $ Laura.change_face("sexy", blush = 1)

            ch_Laura "Take a look."
            ch_Laura "I like making you hard."
        elif dice_roll == 2:
            $ Laura.change_face("sly", mouth = "lipbite", blush = 1)

            ch_Laura "Fine, but you better do something with them later."
        elif dice_roll == 3:
            $ Laura.change_face("confused1", mouth = "lipbite", blush = 1)

            ch_Laura "Not gonna touch them?" 

            $ Laura.change_face("sly", mouth = "lipbite", blush = 1)

            ch_Laura "You will later."
        elif dice_roll == 4:
            $ Laura.change_face("sly", mouth = "lipbite", blush = 1)

            ch_Laura "I bet you just want to see if my nipples are hard." 
            ch_Laura "Weirdo."

    return

label Laura_accepts_show_breasts_after_first_time:
    $ Laura.change_face("confused1", mouth = "lipbite", blush = 1) 
    
    ch_Laura "Happy?" 

    menu:
        extend ""
        "Very. . . happy.":
            call change_Character_stat(Laura, "love", tiny_stat) from _call_change_Character_stat_37

            $ Laura.change_face("sexy", eyes = "down", blush = 1) 
        "They're pretty nice.":
            $ Laura.change_face("sexy", eyes = "down", blush = 1)
        "They're. . . fine.":
            call change_Character_stat(Laura, "love", -tiny_stat) from _call_change_Character_stat_1063

            $ Laura.change_face("confused1", eyes = "down", blush = 1) 

    return

label Laura_accepts_show_breasts_after_second_time:

    return

label Laura_accepts_show_breasts_after:

    return

label Laura_accepts_show_breasts_after_love:

    return

label Laura_rejects_show_pussy:
    if Laura.History.check("seen_pussy"):
        $ dice_roll = renpy.random.randint(1, 2)

        if dice_roll == 1:
            $ Laura.change_face("neutral", eyes = "squint", blush = 1)

            ch_Laura "I'm not exposing myself."
        elif dice_roll == 2:
            $ Laura.change_face("neutral")

            ch_Laura "No, not now."
    else:
        $ Laura.change_face("confused1")

        ch_Laura "Yeah, I'm not showing you that. . ." 

        $ Laura.change_face("angry1")

        ch_Laura "Even I know you don't go around showing just anyone."

    return

label Laura_rejects_show_pussy_asked_once:
    call Laura_asked_once("showing")

    return

label Laura_rejects_show_pussy_asked_twice:
    if approval_check(Laura, threshold = "relationship") and renpy.random.random() > 0.25:
        $ Laura.change_face("appalled2")

        ch_Laura "It's almost like you want me to kick you in the crotch." 
        
        menu:
            extend ""
            "Well. . . could you?":
                $ Laura.change_face("confused3", blush = 1) 
                
                pause 1.0 
                
                $ Laura.change_face("sly", blush = 1) 
                
                show expression "images/effects/smack.webp" as smack onlayer effects:
                    anchor (0.5, 0.5) pos (0.5, 0.7)

                    zoom 0.0
                    alpha 0.0
                    ease 0.1 zoom 1.0 alpha 1.0
                    ease 1.0 alpha 0.0

                with small_screenshake
                
                "She doesn't kick you, but instead smacks your crotch hard enough to make you wince." 
                
                ch_Laura "Weirdo. . ."
            "Sorry. . .":
                pass
    else:
        call Laura_asked_twice("showing") 
        call Laura_kicking_out
        call getting_kicked_out(Laura) from _call_getting_kicked_out_26

    return

label Laura_accepts_show_pussy_before_first_time:
    $ Laura.change_face("confused2", mouth = "lipbite", blush = 1)

    ch_Laura "You actually want to see. . . down there?" 

    $ Laura.change_face("sexy", blush = 1)

    ch_Laura "Seeing it arouses you?"
    ch_Laura "Well, here."

    return

label Laura_accepts_show_pussy_before_second_time:
    $ Laura.change_face("confused1", mouth = "smirk", blush = 1)

    ch_Laura "Want another look?" 

    $ Laura.change_face("sexy", blush = 1)

    ch_Laura "Fine."

    return

label Laura_accepts_show_pussy_before:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        $ Laura.change_face("confused1", mouth = "lipbite", blush = 1)

        ch_Laura "You like it so much?" 

        $ Laura.change_face("sexy", blush = 1)

        ch_Laura "Maybe you should actually touch it sometime soon. . ."
    elif dice_roll == 2:
        $ Laura.change_face("confused1", mouth = "lipbite", blush = 1)

        ch_Laura "Really? Again?" 

        $ Laura.change_face("sexy", blush = 1)

        ch_Laura "Fine." 
    elif dice_roll == 3:
        $ Laura.change_face("sly", mouth = "lipbite", blush = 1)

        ch_Laura "You enjoy looking that much?"

    return

label Laura_accepts_show_pussy_before_love:
    if Laura.status["nympho"]:
        $ Laura.change_face("sly", mouth = "lipbite", blush = 1)

        ch_Laura "We're going to have {i}fun{/i} later."
        ch_Laura "For hours. . ." 
        ch_Laura "And hours. . ."
    elif Laura.status["horny"]:
        $ Laura.change_face("sly", mouth = "lipbite", blush = 1)

        ch_Laura "It's always wet when I think about you." 

        $ Laura.change_face("confused1", mouth = "lipbite", blush = 1)

        ch_Laura "Does that make you hard?"
    elif Laura.check_traits("quirk"):
        $ dice_roll = renpy.random.randint(1, 4)

        if dice_roll == 1:
            $ Laura.change_face("sly", mouth = "lipbite", blush = 1)

            ch_Laura "Show me yours first." 

            $ Laura.change_face("sexy", eyes = "down", blush = 1)

            "You expose yourself enough to give her a good look." 

            $ Laura.change_face("sexy", eyes = "down", blush = 1)

            ch_Laura "Mmm. . ." 
            ch_Laura "Take a look."
        elif dice_roll == 2:
            $ Laura.change_face("confused1", mouth = "lipbite", blush = 1)

            ch_Laura "What, thinking about it isn't enough to make you hard?" 

            $ Laura.change_face("sexy", eyes = "down", blush = 1) 

            ch_Laura "Or is it. . ." 

            $ Laura.change_face("sly", mouth = "lipbite", blush = 1)

            ch_Laura "Fine, here."
        elif dice_roll == 3:
            $ Laura.change_face("sexy", eyes = "down", blush = 1) 

            ch_Laura "First. . ."
            "She reaches a hand down the front of your pants, and gropes you." 

            $ Laura.change_face("sly", mouth = "lipbite", blush = 1)

            ch_Laura "Now you can look."
        elif dice_roll == 4:
            $ Laura.change_face("confused1", mouth = "lipbite", blush = 1)

            ch_Laura "Want to see it again?" 

            $ Laura.change_face("sly", mouth = "lipbite", blush = 1)

            ch_Laura "Only if you do something with it later. . ."
    else:
        $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            $ Laura.change_face("confused1", mouth = "lipbite", blush = 1)

            ch_Laura "Looking at it gets you hard?" 

            $ Laura.change_face("sly", mouth = "lipbite", blush = 1)

            ch_Laura "Looking at yours has a similar effect on me. . ." 
        elif dice_roll == 2:
            $ Laura.change_face("sly", mouth = "lipbite", blush = 1)

            ch_Laura "I can tell you like it a lot." 

            $ Laura.change_face("sexy", eyes = "down", blush = 1)

            ch_Laura "I like yours. . . too."
        elif dice_roll == 3:
            $ Laura.change_face("confused1", mouth = "lipbite", blush = 1)

            ch_Laura "Want to see it again?" 

            $ Laura.change_face("sly", mouth = "lipbite", blush = 1)

            ch_Laura "Only if you do something with it later. . ."

    return

label Laura_accepts_show_pussy_after_first_time:
    $ Laura.change_face("sly", mouth = "lipbite", blush = 1) 
    
    ch_Laura "I can tell at least your body is happy. . ."

    menu:
        extend ""
        "Can't help it. . . your. . . is perfect.":
            call change_Character_stat(Laura, "love", tiny_stat) from _call_change_Character_stat_38
            
            $ Laura.change_face("confused2", mouth = "lipbite", blush = 1) 
            
            ch_Laura "It is?"
        "Well yeah. . . it's great.":
            $ Laura.change_face("confused1", mouth = "lipbite", blush = 1) 
            
            ch_Laura "Really?"
        "Yeah. . . it's not bad. . .":
            call change_Character_stat(Laura, "love", -tiny_stat) from _call_change_Character_stat_1065 

            $ Laura.change_face("confused1", blush = 1) 
            
            ch_Laura "What does that mean?" 

    return

label Laura_accepts_show_pussy_after_second_time:

    return

label Laura_accepts_show_pussy_after:

    return

label Laura_accepts_show_pussy_after_love:

    return

label Laura_rejects_give_bra:

    return

label Laura_rejects_give_bra_asked_once:

    return

label Laura_rejects_give_bra_asked_twice:      
    call Laura_kicking_out  
    call getting_kicked_out(Laura) from _call_getting_kicked_out_27

    return

label Laura_accepts_give_bra_before_first_time:

    return

label Laura_accepts_give_bra_before_second_time:

    return

label Laura_accepts_give_bra_before:

    return

label Laura_accepts_give_bra_before_love:

    return

label Laura_accepts_give_bra_after_first_time:

    return

label Laura_accepts_give_bra_after_second_time:

    return

label Laura_accepts_give_bra_after:

    return

label Laura_accepts_give_bra_after_love:

    return

label Laura_rejects_give_underwear:

    return

label Laura_rejects_give_underwear_asked_once:

    return

label Laura_rejects_give_underwear_asked_twice:      
    call Laura_kicking_out  
    call getting_kicked_out(Laura) from _call_getting_kicked_out_28

    return

label Laura_accepts_give_underwear_before_first_time:

    return

label Laura_accepts_give_underwear_before_second_time:

    return

label Laura_accepts_give_underwear_before:

    return

label Laura_accepts_give_underwear_before_love:

    return

label Laura_accepts_give_underwear_after_first_time:

    return

label Laura_accepts_give_underwear_after_second_time:

    return

label Laura_accepts_give_underwear_after:

    return

label Laura_accepts_give_underwear_after_love:

    return