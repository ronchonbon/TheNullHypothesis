label Jean_rejects_hookup:
    $ Jean.change_face("surprised2", blush = 1)

    pause 0.5

    $ Jean.change_face("worried1", mouth  = "lipbite", blush = 1)

    ch_Jean "That's naughty, [Jean.Player_petname], we're not there yet. . ."

    return

label Jean_rejects_hookup_mad:
    $ Jean.change_face("appalled2")

    pause 0.5

    $ Jean.change_face("furious")

    ch_Jean "You really think I wanna fool around right {i}now{/i}?!"

    $ Jean.change_face("angry1", eyes = "right")

    ch_Jean "It's like you don't even care about how I feel."

    return

label Jean_rejects_hookup_public:
    $ Jean.change_face("surprised3", blush = 1)

    pause 0.5

    $ Jean.change_face("worried3", eyes = "left", blush = 1)

    ch_Jean "We're in public, [Jean.Player_petname]!"

    $ Jean.change_face("confused1", eyes = "squint", blush = 1)

    ch_Jean "We only do that stuff in private."

    return

label Jean_rejects_hookup_threesome:
    $ Jean.change_face("surprised3", eyes = "right", blush = 1)

    python:
        for G in Present:
            if G in all_Girls and G != Jean:
                G.change_face("suspicious1", blush = 1)

    pause 1.0

    $ Jean.change_face("perplexed", blush = 1)

    ch_Jean "What the hell, [Jean.Player_petname]."

    call change_Girl_stat(Jean, "love", -6) from _call_change_Girl_stat_1598

    $ Jean.change_face("suspicious1")

    ch_Jean "You know we're not alone."

    return

label Jean_accepts_hookup_first_time:
    $ Jean.change_face("smirk2", mouth = "lipbite", blush = 1) 

    ch_Jean "You wanna fool around. . . ?" 
    ch_Jean "Okay. For a bit." 

    return

label Jean_accepts_hookup_second_time:

    return

label Jean_accepts_hookup:
    if Jean.quirk:
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    if dice_roll == 1:
        $ Jean.change_face("sexy", blush = 1) 

        ch_Jean "How'd you know I was in the mood?" 
    elif dice_roll == 2:
        $ Jean.change_face("sly", mouth = "lipbite", blush = 1) 

        ch_Jean "Wanna play around with your big sister?" 
        ch_Jean "I was just thinking about all the fun stuff we could do. . ." 

    return

label Jean_accepts_hookup_love:

    return

label Jean_rejects_Action_asked_once:

    return

label Jean_rejects_Action_asked_twice:        
    call getting_kicked_out(Jean) from _call_getting_kicked_out

    return

label Jean_accepts_Action_again:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        $ Jean.change_face("sly", mouth = "lipbite", blush = 1)

        ch_Jean "You're really insatiable. . ."

        $ Jean.change_face("smirk2", mouth = "lipbite", blush = 1)

        ch_Jean "Fine, c'mere. . ."
    elif dice_roll == 2:
        $ Jean.change_face("worried1", mouth = "lipbite", blush = 1) 

        ch_Jean "You're gonna wear me out. . ."

        $ Jean.change_face("sly", mouth = "lipbite", blush = 1)

        ch_Jean "I won't complain. . ."
    elif dice_roll == 3:
        $ Jean.change_face("confused1", mouth = "lipbite", blush = 1) 

        ch_Jean "Again so soon?"

        $ Jean.change_face("sexy", blush = 1)

        ch_Jean "I'm down. . ."

    return