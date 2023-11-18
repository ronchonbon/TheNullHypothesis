init python:

    def Jean_chapter_one_season_three_study_sessions():
        label = "Jean_chapter_one_season_three_study_sessions"

        conditions = [
            "chapter == 1 and season == 3",
            
            "Player.studying == Jean and Jean.studying"]

        priority = 99
        repeatable = True

        return EventClass(label, conditions, priority = priority, repeatable = repeatable)

label Jean_chapter_one_season_three_study_sessions:
    $ ongoing_Event = True

    $ dice_roll = renpy.random.randint(1, 3)

    if not Jean.History.check("studied_with_Player", tracker = "season") or dice_roll == 1:
        $ Jean.change_face("happy")

        ch_Jean "Ready?" 
        
        if Player.History.check("studied") >= 12:
            $ Jean.change_face("smirk2") 
            
            ch_Jean "Your grades have been pretty stellar lately." 
            
            if Jean in Partners:
                ch_Jean "It's fitting that my boyfriend is also top of his class. . ."
        else:
            $ Jean.change_face("worried1", mouth = "smirk") 
            
            ch_Jean "I think we need to study together a bit more often. . ."

        $ Jean.change_face("sly")

        ch_Jean "Today's gonna be fun, don't you worry."
        ch_Player "Fun. . ."

        $ Jean.change_face("confused1", mouth = "smirk")

        ch_Jean "Oh shush, you."
        ch_Jean "Help me get this stuff set up." 

        $ Jean.change_face("smirk2")

        "As she helps set everything up, you notice her mood start to darken a bit."

        $ Jean.change_face("worried1", eyes = "down")

        "Once she takes her usual spot on the bed right next to you, she seems to perk up a bit."

        $ Jean.change_face("worried1", mouth = "smirk", eyes = "down", blush = 1)

        "[Jean.name] doesn't seem to want to take charge today, so you guide the session towards topics you've been having trouble with."

        $ Jean.change_face("confused1", mouth = "smirk")

        "Despite her odd mood, you can tell she tries just as hard to help you as usual."
        "Although, she seems to spend more time chatting with you and enjoying your presence than actually focusing on studying."

        $ Jean.change_face("smirk2")

        ch_Player "Hey, this question was giving me trouble earlier."
        "You point to one of the more difficult practice questions."

        $ Jean.change_face("confused1", mouth = "smirk")

        pause 1.0

        if Jean in Partners:
            $ Jean.change_face("sly") 
            
            ch_Jean "Give me a kiss and I'll tell you."

            $ Jean.change_face("kiss2") 
            
            "You oblige her, and your lips briefly connect." 

            $ Jean.History.update("kiss")
        else:
            ch_Jean "Oh, that one?"

        $ Jean.change_face("smirk2")

        ch_Jean "Okay, it's choice B." 
        "She gets off track a few times throughout the rest of the session, but it's still relatively productive."

        $ Jean.change_face("worried1", mouth = "smirk")

        ch_Jean "Can we call it there?"
        ch_Player "Sure, is something wrong?"
        ch_Jean "No. . ."

        $ Jean.change_face("worried1", eyes = "right")

        ch_Jean "It's just. . ."

        $ Jean.change_face("worried1", mouth = "smirk")

        ch_Jean "Thanks for spending time with me, [Jean.Player_petname]."
    elif dice_roll == 2:
        $ Jean.change_face("happy")

        ch_Jean "Feeling good today, [Jean.Player_petname]?" 
        ch_Player "Pretty good, and you?"

        $ Jean.change_face("smirk2", eyes = "right")

        ch_Jean "Better with you around. . ." 

        $ Jean.change_face("smirk2")

        ch_Jean "C'mon, help me set this stuff up."
        "After just a few minutes, she seems satisfied with the current arrangement."

        $ Jean.change_face("smirk2", eyes = "down", blush = 1)

        "You plop down on the bed next to each other, and she gives you a little nudge."
        "Today, [Jean.name] seems much more focused on the studying part and runs you through a bunch of practice."
        "Whenever you have a question or make a mistake, she knows exactly how to clear up any confusion."

        $ Jean.change_face("confused1", mouth = "smirk")

        "After all the time you've spent studying together, she's intimately aware of how to make things easy for you to understand." 

        $ Jean.change_face("smirk2")

        ch_Jean "Okay, [Jean.Player_petname], why don't you try this one?" 
        "She points to a particular question."

        ch_Player "Hmm. . ." 

        $ Jean.change_face("confused1", mouth = "smirk") 

        ch_Player "Okay, I'm pretty sure it's choice D." 

        $ Jean.change_face("happy")

        ch_Jean "Good job!"

        $ Jean.change_face("smirk2")

        ch_Jean "You're doing great today."
        "After that, the study session devolves into more of a hangout session than anything else."
    elif dice_roll == 3:
        $ Jean.change_face("sly")

        ch_Jean "Want some help setting up?" 

        $ Jean.change_face("confused1", mouth = "smirk")

        ch_Player "Yes please."
        ch_Jean "You know me too well, [Jean.Player_petname]."
        "Setup takes longer than usual today, as you both spend a lot of time just chatting."
        "After plenty of procrastination, everything's finally organized."

        $ Jean.change_face("smirk2", eyes = "down", blush = 1)

        "She hops onto the bed right next to you, leaning into your shoulder."
        "[Jean.name] takes the lead at the start and seems to be in a bit of a rush, as she runs you through a bunch of practice questions."

        $ Jean.change_face("confused1", mouth = "smirk", eyes = "down") 

        "She also gets sidetracked several times and finds plenty of excuses to chat." 

        $ Jean.change_face("smirk2")

        ch_Jean "Okay, okay, back on topic. . ."
        ch_Jean "Why don't you try this one." 
        "She points to a particular question." 

        $ Jean.change_face("worried1", mouth = "smirk")

        ch_Player "Hmm. . ." 
        ch_Player "Isn't it. . ." 

        $ Jean.change_face("happy")

        ch_Jean "I knew you'd get it."

        $ Jean.change_face("sly")

        "She seems to be satisfied with your performance and uses that as another excuse to spend the rest of your time together just hanging out and chatting about random stuff."

        $ Jean.change_face("worried1", mouth = "smirk")

        ch_Jean "That was fun. . ."

        if Player.location != Jean.home:
            ch_Jean "I can't stick around, but, thanks [Jean.Player_petname]."

            call remove_Characters(Jean) from _call_remove_Characters_49

    if Player.location == Jean.home and Player.location != Jean.location and Jean not in Keys:
        call set_the_scene(location = "bg_girls_hallway") from _call_set_the_scene_132
    
    $ ongoing_Event = False

    return