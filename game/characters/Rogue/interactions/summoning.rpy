label Rogue_summon_in_love:
    if Rogue.History.check("seen_Player", tracker = "recent") > 1:
        $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            call receive_text(Rogue, "I'm comin!") from _call_receive_text_935
        elif dice_roll == 2:
            call receive_text(Rogue, "Was wonderin where you were goin") from _call_receive_text_936
            call receive_text(Rogue, "Be right there!") from _call_receive_text_937
        elif dice_roll == 3:
            call receive_text(Rogue, "I'm glad you asked!") from _call_receive_text_938
            call receive_text(Rogue, "I didn't want to say bye so soon") from _call_receive_text_939
    elif Rogue.History.check("seen_Player", tracker = "last"):
        $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            call receive_text(Rogue, "You know it!") from _call_receive_text_940
            call receive_text(Rogue, "Gimme one sec") from _call_receive_text_941
        elif dice_roll == 2:
            call receive_text(Rogue, "I was hopin you'd ask") from _call_receive_text_942
            call receive_text(Rogue, "Be right there") from _call_receive_text_943
        elif dice_roll == 3:
            call receive_text(Rogue, "I always want more time with you!") from _call_receive_text_944
            call receive_text(Rogue, "Comin!") from _call_receive_text_945
    else:
        if Rogue.check_traits("quirk"):
            $ dice_roll = renpy.random.randint(1, 4)
        else:
            $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            call receive_text(Rogue, "Sure!") from _call_receive_text_505
            call receive_text(Rogue, "Be there in a jiff") from _call_receive_text_506
        elif dice_roll == 2:
            call receive_text(Rogue, "I'm on my way!") from _call_receive_text_946
        elif dice_roll == 3:
            call receive_text(Rogue, "You bet I do!") from _call_receive_text_947
            call receive_text(Rogue, "Don't go anywhere!") from _call_receive_text_948
        elif dice_roll == 4:
            call receive_text(Rogue, "Yes!") from _call_receive_text_502
            call receive_text(Rogue, "I mean, of course I wanna") from _call_receive_text_503
            call receive_text(Rogue, "Be there as fast as I can") from _call_receive_text_504

    return

label Rogue_summon_in_relationship:
    if Rogue.History.check("seen_Player", tracker = "recent") > 1:
        $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            call receive_text(Rogue, "I'm comin!") from _call_receive_text_949
        elif dice_roll == 2:
            call receive_text(Rogue, "Was wonderin where you were goin") from _call_receive_text_950
            call receive_text(Rogue, "Be right there!") from _call_receive_text_951
        elif dice_roll == 3:
            call receive_text(Rogue, "I'm glad you asked!") from _call_receive_text_952
            call receive_text(Rogue, "I didn't want to say bye so soon") from _call_receive_text_953
    elif Rogue.History.check("seen_Player", tracker = "last"):
        $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            call receive_text(Rogue, "You know it!") from _call_receive_text_954
            call receive_text(Rogue, "Gimme one sec") from _call_receive_text_955
        elif dice_roll == 2:
            call receive_text(Rogue, "I was hopin you'd ask") from _call_receive_text_956
            call receive_text(Rogue, "Be right there") from _call_receive_text_957
        elif dice_roll == 3:
            call receive_text(Rogue, "I always want more time with you!") from _call_receive_text_958
            call receive_text(Rogue, "Comin!") from _call_receive_text_959
    else:
        $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            call receive_text(Rogue, "I'm on my way!") from _call_receive_text_960
        elif dice_roll == 2:
            call receive_text(Rogue, "You bet I do!") from _call_receive_text_961
            call receive_text(Rogue, "Don't go anywhere!") from _call_receive_text_962
        elif dice_roll == 3:
            call receive_text(Rogue, "Always down to hang with you") from _call_receive_text_507
            call receive_text(Rogue, "Be right there") from _call_receive_text_508

    return

label Rogue_summon_love_and_trust:
    if Rogue.History.check("seen_Player", tracker = "recent") > 1:
        $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            call receive_text(Rogue, "Heh, didn't get enough?") from _call_receive_text_963
            call receive_text(Rogue, "On my way") from _call_receive_text_964
        elif dice_roll == 2:
            call receive_text(Rogue, "Sure, we can hang out some more!") from _call_receive_text_965
        elif dice_roll == 3:
            call receive_text(Rogue, "Yeah, I wouldn't mind hangin out more!") from _call_receive_text_966
    elif Rogue.History.check("seen_Player", tracker = "last"):
        $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            call receive_text(Rogue, "Heh, didn't get enough?") from _call_receive_text_967
            call receive_text(Rogue, "On my way") from _call_receive_text_968
        elif dice_roll == 2:
            call receive_text(Rogue, "Sure, we can hang out some more!") from _call_receive_text_969
        elif dice_roll == 3:
            call receive_text(Rogue, "Yeah, I wouldn't mind hangin out more!") from _call_receive_text_970
    else:
        $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            call receive_text(Rogue, "Sounds good to me") from _call_receive_text_971
        elif dice_roll == 2:
            call receive_text(Rogue, "Sure!") from _call_receive_text_972
        elif dice_roll == 3:
            call receive_text(Rogue, "Oh alright") from _call_receive_text_509
            call receive_text(Rogue, "Guess I can head over") from _call_receive_text_510

    return

label Rogue_summon_love:
    if Rogue.History.check("seen_Player", tracker = "recent") > 1:
        $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            call receive_text(Rogue, "Heh, didn't get enough?") from _call_receive_text_973
            call receive_text(Rogue, "On my way") from _call_receive_text_974
        elif dice_roll == 2:
            call receive_text(Rogue, "Sure, we can hang out some more!") from _call_receive_text_975
        elif dice_roll == 3:
            call receive_text(Rogue, "Yeah, I wouldn't mind hangin out more!") from _call_receive_text_976
    elif Rogue.History.check("seen_Player", tracker = "last"):
        $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            call receive_text(Rogue, "Heh, didn't get enough?") from _call_receive_text_977
            call receive_text(Rogue, "On my way") from _call_receive_text_978
        elif dice_roll == 2:
            call receive_text(Rogue, "Sure, we can hang out some more!") from _call_receive_text_979
        elif dice_roll == 3:
            call receive_text(Rogue, "Yeah, I wouldn't mind hangin out more!") from _call_receive_text_980
    else:
        $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            call receive_text(Rogue, "Sounds good to me") from _call_receive_text_981
        elif dice_roll == 2:
            call receive_text(Rogue, "Sure!") from _call_receive_text_982
        elif dice_roll == 3:
            call receive_text(Rogue, "Well") from _call_receive_text_511
            call receive_text(Rogue, "Alright, I did wanna hang with ya") from _call_receive_text_512

    return

label Rogue_summon_trust:
    if Rogue.History.check("seen_Player", tracker = "recent") > 1:
        $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            call receive_text(Rogue, "Heh, I suppose") from _call_receive_text_983
            call receive_text(Rogue, "On my way") from _call_receive_text_984
        elif dice_roll == 2:
            call receive_text(Rogue, "Sure, we can hang out some more!") from _call_receive_text_985
        elif dice_roll == 3:
            call receive_text(Rogue, "Yeah, I wouldn't mind hangin out more!") from _call_receive_text_986
    elif Rogue.History.check("seen_Player", tracker = "last"):
        $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            call receive_text(Rogue, "Heh, I suppose") from _call_receive_text_987
            call receive_text(Rogue, "On my way") from _call_receive_text_988
        elif dice_roll == 2:
            call receive_text(Rogue, "Sure, we can hang out some more!") from _call_receive_text_989
        elif dice_roll == 3:
            call receive_text(Rogue, "Yeah, I wouldn't mind hangin out more!") from _call_receive_text_990
    else:
        $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            call receive_text(Rogue, "Sounds good to me") from _call_receive_text_991
        elif dice_roll == 2:
            call receive_text(Rogue, "Sure!") from _call_receive_text_992
        elif dice_roll == 3:
            call receive_text(Rogue, "Sure") from _call_receive_text_513
            call receive_text(Rogue, "Headin over right now") from _call_receive_text_514

    return

label Rogue_summon_temporary:
    if Rogue.History.check("seen_Player", tracker = "recent") > 1:
        $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            call receive_text(Rogue, "Okay, for a few more minutes") from _call_receive_text_993
        elif dice_roll == 2:
            call receive_text(Rogue, "Okay, I have time for a little more") from _call_receive_text_994
        elif dice_roll == 3:
            call receive_text(Rogue, "Just for a bit longer") from _call_receive_text_995
    elif Rogue.History.check("seen_Player", tracker = "last"):
        $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            call receive_text(Rogue, "Okay, then I really have to go") from _call_receive_text_996
        elif dice_roll == 2:
            call receive_text(Rogue, "I suppose I can make more time") from _call_receive_text_997
        elif dice_roll == 3:
            call receive_text(Rogue, "Okay, but just for a bit") from _call_receive_text_998
    else:
        $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            call receive_text(Rogue, "Okay, just for a bit!") from _call_receive_text_999
        elif dice_roll == 2:
            call receive_text(Rogue, "I have a few!") from _call_receive_text_1000
        elif dice_roll == 3:
            call receive_text(Rogue, "Guess I can") from _call_receive_text_515
            call receive_text(Rogue, "But not for long") from _call_receive_text_516

    return

label Rogue_summon_busy:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        call receive_text(Rogue, "Sorry [Rogue.Player_petname]") from _call_receive_text_517
        call receive_text(Rogue, "Bit busy right now") from _call_receive_text_518
    elif dice_roll == 2:
        call receive_text(Rogue, "Wish I could [Rogue.Player_petname]") from _call_receive_text_519
        call receive_text(Rogue, "Too busy") from _call_receive_text_520
    elif dice_roll == 3:
        call receive_text(Rogue, "Bad timing :(") from _call_receive_text_1001
        call receive_text(Rogue, "Maybe later?") from _call_receive_text_1002

    return

label Rogue_summon_busy_late:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        call receive_text(Rogue, "Bit late [Rogue.Player_petname]") from _call_receive_text_521
    elif dice_roll == 2:
        call receive_text(Rogue, "I should really head to bed. . .") from _call_receive_text_1003
    elif dice_roll == 3:
        call receive_text(Rogue, "Maybe in the mornin?") from _call_receive_text_1004

    return

label Rogue_summon_reject:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        call receive_text(Rogue, "Sorry") from _call_receive_text_522
        call receive_text(Rogue, "Not right now") from _call_receive_text_523
    elif dice_roll == 2:
        call receive_text(Rogue, "Maybe later?") from _call_receive_text_524
    elif dice_roll == 3:
        call receive_text(Rogue, "I wish") from _call_receive_text_525
        call receive_text(Rogue, "Sorry") from _call_receive_text_526

    return

label Rogue_summon_reject_asked_once:
    call Rogue_asked_once_text("busy") from _call_Rogue_asked_once_text_1

    return

label Rogue_summon_reject_asked_twice:
    call Rogue_asked_twice_text("busy") from _call_Rogue_asked_twice_text_1

    return

label Rogue_summon_reject_mad:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        call receive_text(Rogue, "Ain't goin fuckin nowhere") from _call_receive_text_530
    elif dice_roll == 2:
        call receive_text(Rogue, "No way in hell")
    elif dice_roll == 3:
        call receive_text(Rogue, "What the hell are you thinkin?")

    return
    
label Rogue_dismiss_accept:
    menu:
        "Hey, you can leave if you want.":
            $ dice_roll = renpy.random.randint(1, 3)

            if dice_roll == 1:
                ch_Rogue "Alright, ah'll see you 'round then."
            elif dice_roll == 2:
                $ Rogue.change_face("worried1")

                ch_Rogue "Okay, see you later!"
            elif dice_roll == 3:
                $ Rogue.change_face("smirk2")

                ch_Rogue "That's nice, ah'll probably stick around though."

                $ Rogue.History.update("said_no_to_dismiss")

                return False
        "I think you should leave.":
            if not Rogue.quirk:
                call change_Character_stat(Rogue, "love", -tiny_stat) from _call_change_Character_stat_779
            
            $ dice_roll = renpy.random.randint(1, 3)

            if dice_roll == 1:
                $ Rogue.change_face("worried1")

                ch_Rogue "But. . ."
                ch_Rogue "Okay, ah'll see you 'round. . ."
            elif dice_roll == 2:
                $ Rogue.change_face("sad")

                ch_Rogue "Oh. . . okay. . ."
            elif dice_roll == 3:
                $ Rogue.change_face("angry1")

                ch_Rogue "Fine, I guess. . ."
        "Leave, give us some privacy." if len(Present) > 1:
            if not Rogue.quirk:
                call change_Character_stat(Rogue, "love", -tiny_stat) from _call_change_Character_stat_780

            $ dice_roll = renpy.random.randint(1, 3)

            if dice_roll == 1:
                $ Rogue.change_face("worried1")

                ch_Rogue "Okay. . . sorry."
            elif dice_roll == 2:
                $ Rogue.change_face("sad")

                ch_Rogue "Sorry. . ."
            elif dice_roll == 3:
                $ Rogue.change_face("worried1")

                ch_Rogue "See you later. . ."
        "Back":
            return False

    return True

label Rogue_dismiss_reject:
    menu:
        "Hey, you can leave if you want.":
            $ dice_roll = renpy.random.randint(1, 3)

            if dice_roll == 1:
                $ Rogue.change_face("confused1")

                ch_Rogue "Thanks. . ."

                $ Rogue.change_face("neutral")

                ch_Rogue "But ah think ah'll stick 'round."
            elif dice_roll == 2:
                $ Rogue.change_face("confused1")

                ch_Rogue "Ah know?"
            elif dice_roll == 3:
                $ Rogue.change_face("confused1")

                ch_Rogue "Gee, thanks for tellin' me. . ."
        "I think you should leave.":
            if not Rogue.quirk:
                call change_Character_stat(Rogue, "love", -tiny_stat) from _call_change_Character_stat_781

            $ dice_roll = renpy.random.randint(1, 3)

            if dice_roll == 1:
                $ Rogue.change_face("confused1")

                ch_Rogue "Ah'm good."
            elif dice_roll == 2:
                $ Rogue.change_face("angry1")

                ch_Rogue "So?"
            elif dice_roll == 3:
                $ Rogue.change_face("angry1")

                ch_Rogue "That's great, hon."
        "Leave, give us some privacy." if len(Present) > 1:
            if not Rogue.quirk:
                call change_Character_stat(Rogue, "love", -tiny_stat) from _call_change_Character_stat_782

            $ dice_roll = renpy.random.randint(1, 3)

            if dice_roll == 1:
                $ Rogue.change_face("angry1")

                ch_Rogue "Maybe if you asked polite-like."
            elif dice_roll == 2:
                $ Rogue.change_face("angry1")

                ch_Rogue "No way in hell."
            elif dice_roll == 3:
                $ Rogue.change_face("angry1")

                ch_Rogue "Rude - ain't no way."
        "Back":
            return False

    return True

label Rogue_dismiss_reject_asked_once:
    call Rogue_asked_once("dismissing") from _call_Rogue_asked_once_15

    return

label Rogue_dismiss_reject_asked_twice:
    call Rogue_asked_twice("dismissing") from _call_Rogue_asked_twice_8

    if Player.location == Rogue.home:
        call Rogue_kicking_out from _call_Rogue_kicking_out_11
        call getting_kicked_out(Rogue) from _call_getting_kicked_out_61

    return

label Rogue_dismiss_reject_mad:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        $ Rogue.change_face("appalled2")

        ch_Rogue "Ah'm already pissed off."
        ch_Rogue "Not goin' nowhere."
    elif dice_roll == 2:
        $ Rogue.change_face("furious")

        ch_Rogue "Why do you think you can boss me 'round?"
    elif dice_roll == 3:
        $ Rogue.change_face("furious")

        ch_Rogue "Ah'm really not in the mood for you to tell me what to do."

    return