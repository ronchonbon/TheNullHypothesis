init python:

    def Laura_I_love_you():
        label = "Laura_I_love_you"

        conditions = [
            "Laura in Partners",

            "approval_check(Laura, threshold = Laura_thresholds['love'])",

            "day - EventScheduler.Events['Laura_penultimate_quirk'].completed_when >= 3",
            
            "Player.location == Player.home and not Present",

            "Laura.is_in_normal_mood()"]

        waking = True

        priority = 99

        return EventClass(label, conditions, waking = waking, priority = priority)

label Laura_I_love_you:
    $ ongoing_Event = True

    call receive_text(Rogue, f"Gmornin {Rogue.Player_petname} :)") from _call_receive_text_709
    call receive_text(Rogue, "Hope ya slept well") from _call_receive_text_710

    "As you wake up, your phone buzzes with several new texts."

    call open_texts(Rogue) from _call_open_texts_25
    call send_text(Rogue, "good morning!") from _call_send_text_90

    $ Rogue.mandatory_text_options = ["I slept well, hope you did too", "could be worse, could be better", "I didn't, but whatever"]
    $ temp = Rogue.mandatory_text_options[:]

    while Rogue.mandatory_text_options:
        pause

    if Rogue.text_history[-1][1] == temp[0]:
        call receive_text(Rogue, "Aint you sweet :)") from _call_receive_text_711

        call change_Girl_stat(Rogue, "love", 0) from _call_change_Girl_stat_1040
    elif Rogue.text_history[-1][1] == temp[1]:
        call receive_text(Rogue, "Glad it wasnt too bad") from _call_receive_text_712
    elif Rogue.text_history[-1][1] == temp[2]:
        call receive_text(Rogue, "Real sorry to hear that :(") from _call_receive_text_713

    call receive_text(Rogue, "Just textin ya cuz I thought you should know") from _call_receive_text_714
    call receive_text(Rogue, "X23 was actin a bit weird this mornin") from _call_receive_text_715
    call receive_text(Rogue, "Well past few days actually") from _call_receive_text_716
    call send_text(Rogue, "she has?") from _call_send_text_91
    call send_text(Rogue, "did something happen?") from _call_send_text_92
    call receive_text(Rogue, "Nothin bad") from _call_receive_text_717
    call receive_text(Rogue, "Can I come over?") from _call_receive_text_718
    call receive_text(Rogue, "So I can tell ya bout it") from _call_receive_text_719
    call send_text(Rogue, "sure") from _call_send_text_93
    call receive_text(Rogue, "On my way") from _call_receive_text_720

    pause 2.0

    hide screen phone_screen

    "You quickly brush your teeth and get dressed."
    "As you're pulling your pants on. . ."

    call knock_on_door(times = 2) from _call_knock_on_door_41

    $ temp = Rogue.Player_petname.capitalize()

    ch_Rogue "[temp], it's me!"
    "You finish dressing and open the door."

    call send_Characters(Rogue, Player.home, behavior = False) from _call_send_Characters_112

    $ Rogue.change_face("worried1", mouth = "smirk")

    ch_Rogue "Thanks for lettin' me over."
    ch_Player "Of course."
    ch_Player "Is everything really okay?"

    $ Rogue.change_face("smirk2")

    ch_Rogue "Don't worry, ain't nothin' bad."

    $ Rogue.change_face("worried1", mouth = "lipbite", eyes = "right")

    ch_Rogue "It's about yer relationship with [Laura.name]."
    ch_Player "What about it. . . ?"

    $ Rogue.change_face("worried1", mouth = "smirk")

    ch_Rogue "Ah figured you should know. . . why ah think she's been actin' real odd lately."

    $ Rogue.change_face("confused1", mouth = "smirk")

    ch_Rogue "It's yer fault ah'm friends with her, not that ah mind."

    $ Rogue.change_face("smirk2")

    ch_Rogue "And, she usually asks me a ton of questions 'bout you. . ."

    $ Rogue.change_face("worried1", mouth = "smirk", blush = 1)

    ch_Rogue "About romance 'n stuff."

    $ Rogue.change_face("worried1", mouth = "lipbite", eyes = "right", blush = 1)

    ch_Rogue "The past couple days. . . it's gotten a lot worse."

    $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

    ch_Rogue "She can't stop talkin' about ya, says she can't stop thinkin' about ya. . ."

    $ Rogue.change_face("worried1", mouth = "lipbite", blush = 2)

    ch_Rogue "Wants to spend every moment with ya. . ."
    ch_Rogue "It's really frustratin' her, and she's been hidin' it all from you."

    $ Rogue.change_face("worried1", mouth = "smirk", blush = 1)

    ch_Rogue "[Player.first_name], ah think. . ."
    ch_Rogue "Ah think she's in love with you."

    menu:
        extend ""
        "You think she's. . . actually in love with me?":
            pass
        "I. . . wait a minute, like {i}in love{/i}?":
            pass
        "[Rogue.name], what are you talking about? Be serious.":
            pass

    $ Rogue.change_face("worried2")

    ch_Rogue "Ah ain't jokin' around, [Rogue.Player_petname]."
    ch_Rogue "Ah'm tellin ya', because we both know [Laura.name] better than anyone."

    $ Rogue.change_face("worried1")

    ch_Rogue "You can imagine how hard she's lyin' to herself 'bout what's goin' on."
    ch_Rogue "Ah reckon she'd never even say anythin' to ya on her own."

    $ Rogue.change_face("worried1", eyes = "right", blush = 1)

    ch_Rogue "Maybe it ain't my place, but ah think you should have a talk with 'er."
    ch_Rogue "Otherwise, she'll just bottle everythin' up and might end up explodin'."

    $ Rogue.change_face("worried1", blush = 1)

    menu:
        extend ""
        "No, thank you for letting me know. I know what you mean, and this is important, to all of us.":
            $ Rogue.change_face("worried1", mouth = "smirk")

            ch_Rogue "Thanks, ah also think it's important." 
            ch_Rogue "Ah reckon this was inevitable with her." 
            
            call change_Girl_stat(Rogue, "love", 0) from _call_change_Girl_stat_1041 
            call change_Girl_stat(Rogue, "trust", 0) from _call_change_Girl_stat_1042
        "I. . . just never expected. . . No, thank you for letting me know, this is important.":
            $ Rogue.change_face("confused1", mouth = "smirk")

            ch_Rogue "Ah'm sorry, [Rogue.Player_petname], but how could ya not expect this?" 
            ch_Rogue "Ah reckon this was inevitable with her." 
            
            call change_Girl_stat(Rogue, "love", 0) from _call_change_Girl_stat_1043
        "No, it really isn't your place to be giving me advice about my relationship, but regardless, thanks for letting me know.":
            $ Rogue.change_face("worried1", eyes = "down")

            ch_Rogue "Ah'm sorry, [Rogue.Player_petname], ah won't do it again. . ." 
            
            $ Rogue.change_face("worried1") 
            
            ch_Rogue "But, ah reckon this was inevitable with her." 
            
            call change_Girl_stat(Rogue, "love", 0) from _call_change_Girl_stat_1044

    $ Rogue.change_face("worried1", mouth = "smirk")

    ch_Player "Yeah, you're probably right. . ."
    ch_Player "I should go talk to her right now."

    $ Rogue.change_face("smirk2")

    ch_Rogue "Alright, ah'll see ya later then."
    ch_Rogue "Good luck, ah'm rootin' for the two of ya."

    call remove_Characters(Rogue) from _call_remove_Characters_253

    if Laura.History.check("quirk_encouraged") >= Laura.History.check("quirk_discouraged"):
        call Laura_I_love_you_1A from _call_Laura_I_love_you_1A
    else:
        call Laura_I_love_you_1B from _call_Laura_I_love_you_1B

    $ Laura.change_face("angry1", eyes = "right")

    menu:
        extend ""
        "I know you're struggling with parts of yourself, but I want you to feel like you can let me share some of that burden.":
            call change_Girl_stat(Laura, "love", 0) from _call_change_Girl_stat_1045 
            call change_Girl_stat(Laura, "trust", 0) from _call_change_Girl_stat_1046
        "[Laura.name], I know you've been talking to [Rogue.name] about what you're struggling with, but I'm your boyfriend. You can come to me for support too. . .":
            call change_Girl_stat(Laura, "love", 0) from _call_change_Girl_stat_1047
        "Seriously, [Laura.name], I am your boyfriend. I know you've been leaning on [Rogue.name], but you need to start coming to me for support.":
            call change_Girl_stat(Laura, "love", 0) from _call_change_Girl_stat_1048 
            call change_Girl_stat(Laura, "trust", 0) from _call_change_Girl_stat_1049

    $ Laura.change_face("furious", blush = 1)

    ch_Laura "You. Are. The. Problem."
    ch_Laura "You're constantly in my thoughts, and I find it increasingly difficult to resist the desire to be near you."

    $ Laura.change_face("angry1", eyes = "right", blush = 1)

    ch_Laura "It's. . . not a bad thing. . ."

    $ Laura.change_face("worried1", eyes = "right", blush = 1)

    ch_Laura "I want this to be the case. . ."
    ch_Laura "But processing these 'emotions' was never something I was prepared for."

    $ Laura.change_face("worried2", blush = 1)

    ch_Laura "[Rogue.name] tried to explain the phenomenon early on."

    $ Laura.change_face("worried1", eyes = "right", blush = 1)

    ch_Laura "I did not think I'd be capable of it. . . even with you. . ."

    $ Laura.change_face("neutral", blush = 2)

    ch_Laura "But, it seems like I was mistaken. . ."

    menu:
        extend ""
        "Let her keep going.":
            call Laura_I_love_you_2A from _call_Laura_I_love_you_2A
        "[Laura.name], if it makes it easier. . . I love you.":
            call change_Girl_stat(Laura, "love", 0) from _call_change_Girl_stat_1050
            
            call Laura_I_love_you_2B from _call_Laura_I_love_you_2B

    $ Laura.change_face("sly", blush = 1)

    if Laura.quirk:
        ch_Laura "So, we are 'in love' now. . ."

        $ Laura.change_face("sly", mouth = "lipbite", blush = 1)

        ch_Laura "Come here."

        $ Laura.change_face("kiss2", blush = 1)

        "Without another word, [Laura.name] grabs you by the collar, pulling you into a deep kiss."

        $ Laura.change_face("sly", blush = 1)
    else:
        $ Laura.change_face("worried1", mouth = "lipbite", blush = 1)

        ch_Laura "So, we are 'in love' now?"
        ch_Player "I'd say so. . ."

        $ Laura.change_face("sly", blush = 1)

        ch_Laura "Then I will need to kiss you. . ."
        ch_Player "Go right ahead."

        $ Laura.change_face("sly", mouth = "lipbite", blush = 1)

        pause 1.0

        $ Laura.change_face("kiss2", blush = 1)

        "Without another word, [Laura.name] grabs you by the collar, pulling you into a deep kiss."

        $ Laura.change_face("sly", blush = 1)

    $ Laura.History.update("kiss")

    $ Laura.change_face("smirk2", mouth = "lipbite", blush = 1)

    pause 1.0

    $ Laura.change_face("worried1", mouth = "lipbite", blush = 1)

    if Laura.quirk:
        ch_Laura "I'm. . . very glad I made you my boyfriend. . ."
    else:
        ch_Laura "I'm. . . very glad you're my boyfriend. . ."

    $ Laura.change_face("smirk2", blush = 1)

    ch_Laura "I have much to be thankful for."

    $ Laura.change_face("worried1", blush = 1)

    ch_Laura "You have been essential in my life since I was freed. . ."

    $ Laura.change_face("worried1", eyes = "right", blush = 1)

    ch_Laura "[Rogue.name] as well."

    $ Laura.change_face("angry1", blush = 1)

    ch_Laura "I might not show my emotions very effectively, but don't think I'm not appreciative."

    $ Laura.change_face("sly", blush = 1)

    ch_Laura "I believe I'm finally starting to understand why people like this 'romance' thing. . ."

    if Laura.quirk:
        $ Laura.change_face("sly", mouth = "lipbite", blush = 1)

        ch_Laura "I am also looking forward to exploring our physical connection."
        ch_Laura "You are constantly in my thoughts and satisfy me emotionally. . ."

        $ Laura.change_face("angry1", mouth = "lipbite", blush = 1)

        ch_Laura "But you also arouse me to no end."
        ch_Laura "I am infinitely frustrated, and now that you are truly mine, I will use you to remedy that."

        $ Laura.change_face("angry1", eyes = "squint", mouth = "lipbite", blush = 2)

        ch_Laura "Wherever and whenever I want."

        menu:
            extend ""
            "I was hoping you'd say that. . . use me to your heart's content.":
                call change_Girl_stat(Laura, "love", 0) from _call_change_Girl_stat_1051
            "I'm sorry I frustrate you so much. . . don't hesitate to make me pay for it.":
                call change_Girl_stat(Laura, "love", 0) from _call_change_Girl_stat_1052 
                call change_Girl_stat(Laura, "trust", 0) from _call_change_Girl_stat_1053
            "It's not my fault you're so horny all the time, but fine, you know I'll be available.":
                call change_Girl_stat(Laura, "love", 0) from _call_change_Girl_stat_1054

        $ Laura.change_face("furious", blush = 2)

        ch_Laura "Expect to be accosted any time of the day."

        $ Laura.change_face("furious", eyes = "squint", blush = 1)

        ch_Laura "I need to go train, but I will come find you soon enough."

        $ Laura.change_face("sly", mouth = "lipbite", blush = 1)

        ch_Player "I'm sure you'll be able to find me. . ."
        ch_Laura "You would be correct."
    else:
        $ Laura.change_face("sly", mouth = "lipbite", blush = 1)

        ch_Laura "I am also looking forward to exploring our physical connection."
        ch_Laura "You are constantly in my thoughts and satisfy me emotionally. . ."

        $ Laura.change_face("worried1", eyes = "right", mouth = "lipbite", blush = 1)

        ch_Laura "But you also arouse me to no end."

        $ Laura.change_face("angry1", mouth = "lipbite", blush = 1)

        ch_Laura "I hope. . . we can explore ways to remedy that. . ."

        $ Laura.change_face("angry1", eyes = "squint", mouth = "lipbite", blush = 1)

        ch_Laura "Together. . ."

        menu:
            extend ""
            "I'm also looking forward to it, and I will do my best to alleviate your frustrations.":
                call change_Girl_stat(Laura, "love", 0) from _call_change_Girl_stat_1055
            "I'm sorry I frustrate you so much. . . but don't worry, I'll help alleviate your frustrations the best I can.":
                call change_Girl_stat(Laura, "love", 0) from _call_change_Girl_stat_1056 
                call change_Girl_stat(Laura, "trust", 0) from _call_change_Girl_stat_1057
            "It's not my fault you're so horny all the time, but yeah, we'll figure it out.":
                call change_Girl_stat(Laura, "love", 0) from _call_change_Girl_stat_1058

        $ Laura.change_face("worried1", eyes = "right", mouth = "lipbite", blush = 1)

        ch_Laura "I will. . . let you know whenever I need you. . ."

        $ Laura.change_face("sexy", blush = 1)

        ch_Laura "Unfortunately, I need to go train."
        ch_Laura "Hopefully we can spend time together soon enough."
        ch_Player "I'll be looking forward to it."

    call remove_Characters(Laura) from _call_remove_Characters_254

    $ ongoing_Event = False

    return

label Laura_I_love_you_1A:
    $ Laura.quirk = True

    ch_Rogue "*gasp*"
    "As [Rogue.name] leaves, and you're about to close the door, you hear a gasp."
    ch_Rogue "Lord, are ya fixin' to give me a heart attack?"
    ch_Laura "Sorry. . ."
    "Before you can peek outside to see what's going on. . ."

    call send_Characters(Laura, Player.home, behavior = False) from _call_send_Characters_113

    $ Laura.change_face("suspicious2")

    "[Laura.name] shoves her way into your room, locking the door behind her."
    ch_Player "Oh, hey, I was actually just about to-"

    $ Laura.change_face("angry1")

    ch_Laura "I know."
    ch_Laura "I heard your conversation."

    $ Laura.change_face("confused1")

    ch_Player "Wha. . . you heard everything I just talked about with [Rogue.name]?"
    ch_Laura "Yes. . . you know how good my senses are. . ."

    $ Laura.change_face("neutral")

    ch_Laura "After talking with [Rogue.name] earlier, I followed her."

    $ Laura.change_face("suspicious1")

    ch_Laura "Her reaction to the discussion led me to believe she'd seek you out."
    ch_Laura "When she came here, I made sure to stay close by."

    menu:
        extend ""
        "And then you eavesdropped on our conversation. . . guess I shouldn't be surprised.":
            $ Laura.change_face("confused1")

            ch_Laura "Of course, and you shouldn't be." 
            
            $ Laura.change_face("neutral") 
            
            ch_Laura "Although, this is the first time I have actually eavesdropped when you were with another girl."
        "And you just decided to listen to everything we talked about?!":
            $ Laura.change_face("confused2")

            ch_Laura "Of course." 
            
            $ Laura.change_face("confused1") 
            
            ch_Laura "Why are you surprised?" 
            
            $ Laura.change_face("neutral") 
            
            ch_Laura "Although, this is the first time I have actually eavesdropped when you were with another girl."
        "What the fuck. . . this isn't the first time, is it?":
            $ Laura.change_face("neutral", eyes = "squint")

            ch_Laura "No, it is the first time." 
            
            $ Laura.change_face("neutral") 
            
            ch_Laura "Previously, if you were in private with another girl, I would not eavesdrop." 
            ch_Laura "Of course, I'd still be nearby just in case."

    $ Laura.change_face("neutral")

    ch_Laura "You have routinely encouraged this behavior."

    if Laura.History.check("started_penultimate_quirk_encouraged"):
        $ Laura.change_face("suspicious1") 
        
        ch_Laura "The last time we discussed our relationship, I made it clear I would not stop any behavior you have been encouraging."

    $ Laura.change_face("confused1")

    ch_Player "Well, this was going to happen one way or another."

    $ Laura.change_face("angry1", eyes = "right")

    ch_Player "If you heard what she said, you know why I was about to ask you to talk."
    ch_Laura "I do. . ."

    $ Laura.change_face("furious")

    return

label Laura_I_love_you_1B:
    $ Laura.quirk = False

    call open_texts(Laura) from _call_open_texts_26

    pause

    call send_text(Laura, "hey, you busy right now?") from _call_send_text_94
    call receive_text(Laura, "What's wrong, are you okay?") from _call_receive_text_721
    call receive_text(Laura, "Did something happen?") from _call_receive_text_722
    call receive_text(Laura, "Do you need my help?") from _call_receive_text_723
    call send_text(Laura, "don't worry, everything's fine") from _call_send_text_95
    call send_text(Laura, "it's just. . .") from _call_send_text_96

    $ Laura.mandatory_text_options = [f"to be honest, I just had a talk with {Rogue.name}, and I think we should have a talk as well", "could you come over? we should really have a talk", "you really need to chill out. come over, we need to talk"]
    $ temp = Laura.mandatory_text_options[:]

    while Laura.mandatory_text_options:
        pause

    if Laura.text_history[-1][1] == temp[0]:
        call change_Girl_stat(Laura, "trust", 0) from _call_change_Girl_stat_1059
    elif Laura.text_history[-1][1] == temp[2]:
        call change_Girl_stat(Laura, "love", 0) from _call_change_Girl_stat_1060

    call receive_text(Laura, "I'm coming") from _call_receive_text_724

    pause 2.0

    hide screen phone_screen

    "After waiting for a few minutes, you hear someone knock on your door."

    call knock_on_door(times = 2) from _call_knock_on_door_42

    "You open it, and [Laura.name] walks in."

    $ reset_behavior(Laura)

    call change_Outfit(Laura, Laura.Wardrobe.superhero_Outfit, instant = True) from _call_change_Outfit_47
    call add_Characters(Laura) from _call_add_Characters_90

    $ Laura.change_face("neutral")

    ch_Laura "I know what you want to talk about."

    $ Laura.change_face("angry1", eyes = "right")

    ch_Laura "I had a discussion with [Rogue.name] earlier. . ."

    $ Laura.change_face("angry1")

    ch_Laura "I had intended on training, to distract myself from the situation."

    $ Laura.change_face("furious")

    ch_Laura "But clearly, this is not something I can avoid."
    ch_Laura "As you now seem to be aware of everything. . ."

    return

label Laura_I_love_you_2A:
    $ Laura.change_face("worried1", eyes = "right", blush = 1)

    ch_Laura "After everything, I think. . ."

    $ Laura.change_face("worried1", mouth = "smirk", blush = 1)

    ch_Laura "I think I love you."

    menu:
        extend ""
        "You don't know how happy I am to hear that. I love you too.":
            pass
        "I was worried. . . No, I'm glad you were able to realize your feelings. I love you too.":
            pass
        "Took you long enough to get there. And don't worry, I love you too.":
            pass

    $ Laura.change_face("worried4", blush = 2)

    ch_Laura "You. . ."

    $ Laura.change_face("worried1", eyes = "right", blush = 1)

    pause 1.0

    $ Laura.change_face("suspicious1", blush = 1)

    ch_Laura "You are telling me the truth?"
    ch_Player "Yes, of course."

    $ Laura.change_face("worried1", mouth = "smirk", blush = 1)

    ch_Laura "Good."

    return

label Laura_I_love_you_2B:
    $ Laura.change_face("worried4", blush = 2)

    ch_Laura "You. . ."

    $ Laura.change_face("worried1", eyes = "right", blush = 1)

    pause 1.0

    $ Laura.change_face("suspicious1", blush = 1)

    ch_Laura "You are telling me the truth?"
    ch_Player "Yes, of course."
    
    $ Laura.change_face("worried1", eyes = "right", blush = 1)

    ch_Laura "I. . ."

    $ Laura.change_face("worried1", mouth = "smirk", blush = 1)

    ch_Laura "I think I love you too."

    return