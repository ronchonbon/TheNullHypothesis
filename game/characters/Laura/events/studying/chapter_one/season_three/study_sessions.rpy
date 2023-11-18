init python:

    def Laura_chapter_one_season_three_study_sessions():
        label = "Laura_chapter_one_season_three_study_sessions"

        conditions = [
            "chapter == 1 and season == 3",
            "Player.studying == Laura and Laura.studying"]

        priority = 99
        repeatable = True

        return EventClass(label, conditions, priority = priority, repeatable = repeatable)

label Laura_chapter_one_season_three_study_sessions:
    $ ongoing_Event = True

    $ dice_roll = renpy.random.randint(1, 3)

    if not Laura.History.check("studied_with_Player", tracker = "season") or dice_roll == 1:
        $ Laura.change_face("neutral")

        "Without any prompting, [Laura.name] starts to help you set everything up."

        $ Laura.change_face("confused1")

        ch_Laura "Why is your face like that?"
        ch_Player "I just wasn't expecting. . ."

        $ Laura.change_face("neutral", eyes = "squint")

        ch_Player "Never mind. . . but thanks for the help."
        ch_Laura "You're welcome."

        $ Laura.change_face("neutral")

        "Once everything's organized, she even takes the initiative, asks questions, and guides you towards topics she's been having trouble with."

        $ Laura.change_face("neutral", eyes = "down", blush = 1)

        "You feel her heart rate speed up as her shoulder occasionally rubs into yours."

        $ Laura.change_face("angry1", eyes = "down", blush = 1)

        "Eventually, she just leans into you for the rest of the session."
        "[Laura.name] has clearly been putting more effort into her studies, as the tutoring session becomes more mutually beneficial."

        $ Laura.change_face("neutral", eyes = "down", blush = 1)

        "You both spend the next couple hours going over tricky subjects and quizzing each other with practice questions."

        $ Laura.change_face("confused1", blush = 1)

        "She points out one specific question." 

        ch_Player "You think this will be on the exam?" 

        $ Laura.change_face("confused1")

        ch_Laura "Of course."

        $ Laura.change_face("neutral")

        ch_Laura "The professor brought it up specifically."
        ch_Laura "The answer is. . ." 

        $ Laura.change_face("sly")

        ch_Player "Huh, I didn't know that one."
        "The satisfaction seems to fuel her, as she spends the rest of the session tutoring you on a few things you didn't know." 

        $ Laura.change_face("smirk2")

        ch_Player "Thanks, [Laura.name]."
        ch_Player "You were a big help today."

        $ Laura.change_face("angry1", mouth = "smirk", eyes = "right", blush = 1)

        ch_Laura "You're welcome. . ." 

        $ Laura.change_face("angry1")

        ch_Laura "Figured I might be able to help you for once." 

        $ Laura.change_face("neutral")

        if renpy.random.random() > 0.5:
            call Characters_leave(Laura) from _call_Characters_leave_2
    elif dice_roll == 2:
        $ Laura.change_face("neutral", eyes = "squint")

        ch_Laura ". . ."
        ch_Laura "Want help?"
        ch_Player "Sure."

        $ Laura.change_face("neutral")

        "[Laura.name] is practiced enough now that you don't even have to tell her where things go anymore."
        "It only takes a couple minutes."

        $ Laura.change_face("neutral", eyes = "down", blush = 1)

        "Without any preamble, [Laura.name] pushes you onto the bed."
        ch_Player "What the. . ."
        "She follows close behind, basically pinning you down as she gets between you and the door."

        $ Laura.change_face("angry1", eyes = "down", blush = 1)

        pause 1.0

        $ Laura.change_face("angry1", blush = 1)

        ch_Player "Wh-." 

        $ Laura.change_face("confused1", mouth = "smirk", blush = 1)

        ch_Laura "I want to start with this. . ."
        "[Laura.name] doesn't let you get a word in edgewise as she takes charge of the session."

        $ Laura.change_face("neutral", eyes = "down", blush = 1)

        "You notice a couple things as time goes on."

        $ Laura.change_face("neutral", eyes = "right", blush = 1)

        "[Laura.name] both seems to lean into you more than usual, while also occasionally glancing at the door or out the windows."
        "Before you can say anything about it. . ."

        $ Laura.change_face("neutral")

        ch_Laura "This question. . . what's the answer?"

        $ Laura.change_face("confused1")

        ch_Player "Wh. . . oh, that one?"
        ch_Player "Isn't it choice D?" 
        
        $ Laura.change_face("sly")

        ch_Laura "No."
        ch_Laura "It's C." 
        ch_Player "Damn, mind explaining it?"
        "After a brief explanation, you realize she must've gone ahead while studying the material"

        $ Laura.change_face("smirk2", eyes = "right")

        ch_Player "You went ah-" 

        $ Laura.change_face("neutral", eyes = "squint")

        "She interrupts you."
        ch_Laura "I'm going to train now."
        ch_Laura "Don't go anywhere dangerous. . ."
        ch_Player "I wasn't planning to. . ."

        $ Laura.change_face("suspicious1")

        ch_Laura "Bye."

        call remove_Characters(Laura) from _call_remove_Characters_123

        ch_Player "What was that about. . ."
    elif dice_roll == 3:
        $ Laura.change_face("neutral", eyes = "right")

        "Instead of immediately helping you organize all the study materials, [Laura.name] seems preoccupied as she glances out the windows."

        $ Laura.change_face("surprised1")

        ch_Player "Are you. . . gonna help?" 

        $ Laura.change_face("angry1", blush = 1)

        ch_Laura "Yes. . ." 
        "After coming to her senses, you both make quick work of setting things up for the study session."

        $ Laura.change_face("neutral", eyes = "right")

        "[Laura.name] plops down onto the bed next to you, making sure to get close and press up against you."

        $ Laura.change_face("angry1", eyes = "down", blush = 1)

        ch_Player "{i}Ahem{/i}. . . so, where did you want to start?"
        ch_Laura "I don't care, you pick."

        $ Laura.change_face("neutral", eyes = "right", blush = 1)

        ch_Player "Sure, let's go with. . ."

        $ Laura.change_face("neutral", eyes = "down", blush = 1)

        "Throughout the session, you again notice [Laura.name] occasionally glancing at the door and out the windows."

        $ Laura.change_face("neutral", eyes = "left", blush = 1)

        ch_Player "Is everything okay?"

        $ Laura.change_face("angry1", blush = 1)

        ch_Laura "Just making sure. . ."

        $ Laura.change_face("angry1", eyes = "down", blush = 1)

        ch_Laura "Now, keep going."
        ch_Laura "I didn't get that last part. . ."
        "You go on with the session, and despite [Laura.name] seemingly keeping constant vigil over you, she still seems to be paying close attention."

        $ Laura.change_face("neutral", eyes = "right", blush = 1)

        ch_Player "Here, try this practice question."
        "You point to a particular question."

        $ Laura.change_face("angry1", eyes = "down", blush = 1)

        ch_Laura "That one is. . ."
        ch_Player "Good job, that's right."

        $ Laura.change_face("neutral")

        ch_Player "I think we can call it there." 

        $ Laura.change_face("neutral", eyes = "squint")

        ch_Laura "I will stay."

    if Player.location == Laura.home and Player.location != Laura.location and Laura not in Keys:
        call set_the_scene(location = "bg_girls_hallway") from _call_set_the_scene_351
    
    $ ongoing_Event = False

    return