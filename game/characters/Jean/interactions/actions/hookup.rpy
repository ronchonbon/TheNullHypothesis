label Jean_rejects_hookup:
    $ Jean.change_face("surprised2", blush = 1)

    pause 1.0

    $ Jean.change_face("worried1", mouth  = "lipbite", blush = 1)

    ch_Jean "That's naughty, [Jean.Player_petname], we're not there yet. . ."

    return

label Jean_rejects_hookup_later:

    return

label Jean_rejects_hookup_mad:
    $ Jean.change_face("appalled2")

    pause 1.0

    $ Jean.change_face("furious")

    ch_Jean "You really think I wanna fool around right {i}now{/i}?!"

    $ Jean.change_face("angry1", eyes = "right")

    ch_Jean "It's like you don't even care about how I feel."

    return

label Jean_rejects_hookup_public:
    $ Jean.change_face("surprised3", blush = 1)

    pause 1.0

    $ Jean.change_face("worried3", eyes = "left", blush = 1)

    ch_Jean "We're in public, [Jean.Player_petname]!"

    $ Jean.change_face("confused1", eyes = "squint", blush = 1)

    ch_Jean "We only do that stuff in private."

    return

label Jean_rejects_hookup_threesome:
    $ Jean.change_face("surprised3", eyes = "right", blush = 1)

    python:
        for C in Present:
            if C in all_Companions and C != Jean:
                C.change_face("suspicious1", blush = 1)

    pause 1.0

    $ Jean.change_face("perplexed", blush = 1)

    ch_Jean "What the hell, [Jean.Player_petname]."

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
    if Jean.check_traits("quirk"):
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
    call Jean_asked_once("sex")

    return

label Jean_rejects_Action_asked_twice:    
    call Jean_asked_twice("sex")   
    call Jean_kicking_out
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

label Jean_bored_by_Action(Action):
    $ dice_roll = renpy.random.radint(1, 3)

    if dice_roll == 1:
        $ Jean.change_face("confused1", eyes = "left")

        "[Jean.name] seems a little disinterested."
    elif dice_roll == 2:
        $ Jean.change_face("confused1", eyes = "right")
        
        "You think you see [Jean.name] checking the time."
    elif dice_roll == 3:
        $ Jean.change_face("worried1")

        ch_Jean "Maybe we could move on, [Jean.Player_name]?"

    return

label Jean_not_warmed_up_for_Action(Action):
    if Action.Action_type in insertion_Action_types:
        $ dice_roll = renpy.random.radint(1, 3)
    else:
        $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        "[Jean.name] doesn't seem super into what you're doing."
    elif dice_roll == 2:
        ch_Jean "Could we slow it down just a little, [Jean.Player_petname]?"
    elif dice_roll == 3:
        $ Jean.change_face("grimace")

        ch_Jean "Oof, I don't think I'm ready for that, [Player.first_name]."

    return

label Jean_hookup_summary(total_Character_orgasms, total_Player_orgasms, total_unique_Actions, score):
    if score >= 8.0:
        ch_Jean "Mmm, you're incredible, [Jean.Player_petname]. . ."
    elif score >= 4.0:
        ch_Jean "Damn, you're really good at this, [Jean.Player_petname]!"
    elif score >= 2.0:
        ch_Jean "That was fun!"
    else:
        ch_Jean "Huh."

    if total_Character_orgasms >= 4:
        ch_Jean "I thought I was going to pass out there. . ."
    elif total_Character_orgasms >= 2:
        ch_Jean "You made me cum so hard. . ."
    elif total_Character_orgasms:
        ch_Jean "You made me feel so good. . ."
    else:
        if total_Player_orgasms:
            ch_Jean "Was it good for you?"
        else:
            ch_Jean "We're just going to. . . ? Okay. . ."

            return

    if total_unique_Actions >= 20:
        ch_Jean "Everything we did felt so good. . ."
    elif total_unique_Actions >= 10:
        ch_Jean "I really like all the things we tried. . ."
    elif total_unique_Actions < 2:
        ch_Jean "I wouldn't mind switching things up more, though."

    if total_Player_orgasms >= 3:
        ch_Jean "I really can't believe how much you came. . ."
    elif total_Player_orgasms >= 2:
        ch_Jean "You're a real stud, huh?"
    elif not total_Player_orgasms:
        ch_Jean "But are you sure you're satisfied?"

    return

label Jean_weekly_summary(average_score):
    if average_score >= 8.0:
        ch_Jean "God, this is all I can think about these days. . ."
    elif average_score >= 4.0:
        ch_Jean "I've been thinking about how good you make me feel. . ."
    elif average_score >= 2.0:
        ch_Jean "I really enjoyed last time!"
    else:
        ch_Jean "Sure, why not?"
        ch_Jean "This time, maybe we could. . . ah, never mind."

    return