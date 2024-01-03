label Jean_summon_in_love:
    if Jean.History.check("seen_Player", tracker = "recent"):
        $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            call receive_text(Jean, "Ooh, you want me to follow you? Omw") from _call_receive_text_52
        elif dice_roll == 2:
            call receive_text(Jean, "Sure, I can follow you!") from _call_receive_text_53
        elif dice_roll == 3:
            call receive_text(Jean, "But you were just here?") from _call_receive_text_54
            call receive_text(Jean, "Ooh, are we playing a game?") from _call_receive_text_55
            call receive_text(Jean, "Omw!") from _call_receive_text_56
    elif Jean.History.check("seen_Player", tracker = "last"):
        $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            call receive_text(Jean, "I was just with you!") from _call_receive_text_57
            call receive_text(Jean, "You must really love me") from _call_receive_text_58
            call receive_text(Jean, "Comingggg") from _call_receive_text_59
        elif dice_roll == 2:
            call receive_text(Jean, "Again?") from _call_receive_text_60
            call receive_text(Jean, "I can never say no to you") from _call_receive_text_61
            call receive_text(Jean, "Be right there") from _call_receive_text_62
        elif dice_roll == 3:
            call receive_text(Jean, "Haha, but we were just together!") from _call_receive_text_63
            call receive_text(Jean, "Okay, okay, coming") from _call_receive_text_64
    else:
        if Jean.check_traits("quirk"):
            $ dice_roll = renpy.random.randint(1, 4)
        else:
            $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            call receive_text(Jean, "Of coursee") from _call_receive_text_262
        elif dice_roll == 2:
            call receive_text(Jean, "Def, I'm on my way!") from _call_receive_text_277
        elif dice_roll == 3:
            call receive_text(Jean, "Missed me?") from _call_receive_text_72
            call receive_text(Jean, "Of course I want to") from _call_receive_text_73
            call receive_text(Jean, "Be right there <3") from _call_receive_text_74
        elif dice_roll == 4:
            call receive_text(Jean, "Missed your big sis?") from _call_receive_text_69
            call receive_text(Jean, "Of course you did") from _call_receive_text_70
            call receive_text(Jean, "I'll be right there <3") from _call_receive_text_71

    return

label Jean_summon_in_relationship:
    if Jean.History.check("seen_Player", tracker = "recent"):
        $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            call receive_text(Jean, "Sure, I'll come meet you!") from _call_receive_text_435
        elif dice_roll == 2:
            call receive_text(Jean, "Luring me somewhere, hmm?") from _call_receive_text_825
            call receive_text(Jean, "Omw ;)") from _call_receive_text_826
        elif dice_roll == 3:
            call receive_text(Jean, "Want me to follow ya? Okay!") from _call_receive_text_827
    elif Jean.History.check("seen_Player", tracker = "last"):
        $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            call receive_text(Jean, "No problem, I'll be right there!") from _call_receive_text_828
        elif dice_roll == 2:
            call receive_text(Jean, "Don't like being apart for long, huh?") from _call_receive_text_829
            call receive_text(Jean, "I'm on my way :)") from _call_receive_text_830
        elif dice_roll == 3:
            call receive_text(Jean, "You must really like me haha") from _call_receive_text_831
            call receive_text(Jean, "Okay, coming!") from _call_receive_text_832
    else:
        $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            call receive_text(Jean, "Coming!") from _call_receive_text_833
        elif dice_roll == 2:
            call receive_text(Jean, "Ya! I'm on my way") from _call_receive_text_834
        elif dice_roll == 3:
            call receive_text(Jean, "Duh I wanna hang out") from _call_receive_text_75
            call receive_text(Jean, "Omw") from _call_receive_text_76

    return

label Jean_summon_love_and_trust:
    if Jean.History.check("seen_Player", tracker = "recent"):
        $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            call receive_text(Jean, "Sure, I'll come meet you!") from _call_receive_text_835
        elif dice_roll == 2:
            call receive_text(Jean, "Haha, are we playing hide and go seek???") from _call_receive_text_836
        elif dice_roll == 3:
            call receive_text(Jean, "Haha, sure, I'm on my way") from _call_receive_text_837
    elif Jean.History.check("seen_Player", tracker = "last"):
        $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            call receive_text(Jean, "No problem, I'll be right there!") from _call_receive_text_838
        elif dice_roll == 2:
            call receive_text(Jean, "I'm on my way :)") from _call_receive_text_839
        elif dice_roll == 3:
            call receive_text(Jean, "Okay, coming!") from _call_receive_text_840
    else:
        $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            call receive_text(Jean, "Coming!") from _call_receive_text_841
        elif dice_roll == 2:
            call receive_text(Jean, "Ya! I'm on my way") from _call_receive_text_842
        elif dice_roll == 3:
            call receive_text(Jean, "Okayyy") from _call_receive_text_77
            call receive_text(Jean, "Wasnt doing much anyway") from _call_receive_text_78

    return

label Jean_summon_love:
    if Jean.History.check("seen_Player", tracker = "recent"):
        $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            call receive_text(Jean, "Sure, I'll come meet you!") from _call_receive_text_843
        elif dice_roll == 2:
            call receive_text(Jean, "Haha, are we playing hide and go seek???") from _call_receive_text_844
        elif dice_roll == 3:
            call receive_text(Jean, "Haha, sure, I'm on my way") from _call_receive_text_845
    elif Jean.History.check("seen_Player", tracker = "last"):
        $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            call receive_text(Jean, "No problem, I'll be right there!") from _call_receive_text_846
        elif dice_roll == 2:
            call receive_text(Jean, "I'm on my way :)") from _call_receive_text_847
        elif dice_roll == 3:
            call receive_text(Jean, "Okay, coming!") from _call_receive_text_848
    else:
        $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            call receive_text(Jean, "Coming!") from _call_receive_text_849
        elif dice_roll == 2:
            call receive_text(Jean, "Ya! I'm on my way") from _call_receive_text_850
        elif dice_roll == 3:
            call receive_text(Jean, "Want to hang with me?") from _call_receive_text_79
            call receive_text(Jean, "I guess I can head over <3") from _call_receive_text_80

    return

label Jean_summon_trust:
    if Jean.History.check("seen_Player", tracker = "recent"):
        $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            call receive_text(Jean, "Sure, I'll come meet you!") from _call_receive_text_851
        elif dice_roll == 2:
            call receive_text(Jean, "Haha, are we playing hide and go seek???") from _call_receive_text_852
        elif dice_roll == 3:
            call receive_text(Jean, "Haha, sure, I'm on my way") from _call_receive_text_853
    elif Jean.History.check("seen_Player", tracker = "last"):
        $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            call receive_text(Jean, "No problem, I'll be right there!") from _call_receive_text_854
        elif dice_roll == 2:
            call receive_text(Jean, "I'm on my way :)") from _call_receive_text_855
        elif dice_roll == 3:
            call receive_text(Jean, "Okay, coming!") from _call_receive_text_856
    else:
        $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            call receive_text(Jean, "Coming!") from _call_receive_text_857
        elif dice_roll == 2:
            call receive_text(Jean, "Ya! I'm on my way") from _call_receive_text_858
        elif dice_roll == 3:
            call receive_text(Jean, "Well maybeee") from _call_receive_text_81
            call receive_text(Jean, "Fine, don't go anywhere") from _call_receive_text_82

    return

label Jean_summon_temporary:
    if Jean.History.check("seen_Player", tracker = "recent"):
        $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            call receive_text(Jean, "Hmm? You were just here") from _call_receive_text_859
            call receive_text(Jean, "Okay, I'll find you") from _call_receive_text_860
        elif dice_roll == 2:
            call receive_text(Jean, "Are you messing with me?") from _call_receive_text_861
            call receive_text(Jean, "I guess I can come find you. . .") from _call_receive_text_862
        elif dice_roll == 3:
            call receive_text(Jean, "Hmm. . .") from _call_receive_text_863
            call receive_text(Jean, "Okay. . .") from _call_receive_text_864
    elif Jean.History.check("seen_Player", tracker = "last"):
        $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            call receive_text(Jean, "Again?") from _call_receive_text_865
            call receive_text(Jean, "Okay, real quick") from _call_receive_text_866
        elif dice_roll == 2:
            call receive_text(Jean, "I just saw you though") from _call_receive_text_867
            call receive_text(Jean, "Okay, I'll come by") from _call_receive_text_868
        elif dice_roll == 3:
            call receive_text(Jean, "Mmm, okay I'll swing by") from _call_receive_text_869
    else:
        $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            call receive_text(Jean, "I can swing by for a few minutes, sure") from _call_receive_text_870
        elif dice_roll == 2:
            call receive_text(Jean, "Okay, just for a bit though!") from _call_receive_text_871
        elif dice_roll == 3:
            call receive_text(Jean, "For a little") from _call_receive_text_83
            call receive_text(Jean, "Got too much studying to do later") from _call_receive_text_84

    return

label Jean_summon_busy:
    if Jean.behavior == "studying":
        $ dice_roll = renpy.random.randint(1, 3)
    else:
        $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        call receive_text(Jean, "Too much stuff to do today") from _call_receive_text_87
        call receive_text(Jean, "Sorry </3") from _call_receive_text_88
    elif dice_roll == 2:
        call receive_text(Jean, "I wish, too busy though!") from _call_receive_text_872
        call receive_text(Jean, "Later?") from _call_receive_text_873
    elif dice_roll == 3:
        call receive_text(Jean, "Studying") from _call_receive_text_85
        call receive_text(Jean, "Can't </3") from _call_receive_text_86

    return

label Jean_summon_busy_late:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        call receive_text(Jean, "It's bedtime!") from _call_receive_text_874
    elif dice_roll == 2:
        call receive_text(Jean, f"I'm going to go to bed soon, {Player.first_name}") from _call_receive_text_875
    elif dice_roll == 3:
        call receive_text(Jean, "Mmm, it's a bit late?") from _call_receive_text_89

    return

label Jean_summon_reject:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        call receive_text(Jean, "Not right now") from _call_receive_text_90
        call receive_text(Jean, "Sorryyy </3") from _call_receive_text_91
    elif dice_roll == 2:
        call receive_text(Jean, "Maybe after I study a bit more") from _call_receive_text_92
    elif dice_roll == 3:
        call receive_text(Jean, "If only") from _call_receive_text_93
        call receive_text(Jean, "Too much to do") from _call_receive_text_94

    return

label Jean_summon_reject_asked_once:
    call receive_text(Jean, "Read up, dummy") from _call_receive_text_95

    return

label Jean_summon_reject_asked_twice:
    call receive_text(Jean, "Okay now you're doing it on purpose") from _call_receive_text_96
    call receive_text(Jean, "Stop") from _call_receive_text_97

    return

label Jean_summon_reject_mad:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        call receive_text(Jean, "As if???") from _call_receive_text_876
    elif dice_roll == 2:
        call receive_text(Jean, "Leave me alone!") from _call_receive_text_877
    elif dice_roll == 3:
        call receive_text(Jean, "NO") from _call_receive_text_98
        call receive_text(Jean, ">:((((") from _call_receive_text_99

    return
    
label Jean_dismiss_accept:
    menu:
        "Hey, you can leave if you want.":
            $ Jean.change_face("confused1")

            ch_Jean "I know. . ."

            $ Jean.change_face("neutral")

            ch_Jean "I'm gonna head out for unrelated reasons. . ."
        "I think you should leave.":
            call change_Character_stat(Jean, "love", -tiny_stat) from _call_change_Character_stat_251

            $ Jean.change_face("confused1")

            ch_Jean "Rude. . ."

            $ Jean.change_face("neutral")

            ch_Jean "Whatever, bye." 
        "Leave, give us some privacy." if len(Present) > 1:
            call change_Character_stat(Jean, "love", -tiny_stat) from _call_change_Character_stat_252

            $ Jean.change_face("worried1") 

            ch_Jean "Don't have to be such an ass about it. . ." 
        "Back":
            return False

    return True

label Jean_dismiss_reject:
    menu:
        "Hey, you can leave if you want.":
            $ Jean.change_face("confused1") 

            ch_Jean "Why are you telling me that?" 

            $ Jean.change_face("neutral")

            ch_Jean "I still have stuff to do here."
        "I think you should leave.":
            call change_Character_stat(Jean, "love", -tiny_stat) from _call_change_Character_stat_253

            $ Jean.change_face("confused1")

            ch_Jean "I think you should be nicer." 
        "Leave, give us some privacy." if len(Present) > 1:
            call change_Character_stat(Jean, "love", -tiny_stat) from _call_change_Character_stat_254

            $ Jean.change_face("angry1") 

            ch_Jean "Really thought being rude would work?"
        "Back":
            return False

    return True

label Jean_dismiss_reject_asked_once:
    $ Jean.change_face("angry1") 

    ch_Jean "Don't ignore me."

    return

label Jean_dismiss_reject_asked_twice:
    $ Jean.change_face("appalled2")

    ch_Jean "I already said no!"
    
    if Player.location == Jean.home:
        ch_Jean "{i}You{/i} get out!"
        
        call getting_kicked_out(Jean) from _call_getting_kicked_out_18

    return

label Jean_dismiss_reject_mad:
    $ dice_roll = renpy.random.randint(1, 3)

    return