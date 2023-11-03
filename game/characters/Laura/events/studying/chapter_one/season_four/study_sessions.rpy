init python:

    def Laura_chapter_one_season_four_study_sessions():
        label = "Laura_chapter_one_season_four_study_sessions"

        conditions = [
            "season == 4",
            "Player.studying == Laura and Laura.studying"]

        priority = 99
        repeatable = True

        return EventClass(label, conditions, priority = priority, repeatable = repeatable)

label Laura_chapter_one_season_four_study_sessions:
    $ ongoing_Event = True

    $ dice_roll = renpy.random.randint(1, 3)

    if not Laura.History.check("studied_with_Player", tracker = "season") or dice_roll == 1:
        $ Laura.change_face("neutral")

        ch_Laura "I will help. . ."
        ch_Player "How sweet."

        $ Laura.change_face("suspicious1")

        ch_Laura "On second thought. . ."
        ch_Player "I'm just messing with you."

        $ Laura.change_face("neutral", eyes = "squint")

        ch_Player "You're still gonna help, right?"
        ch_Laura "Fine."

        $ Laura.change_face("neutral")

        "Maybe you are a bit picky about how things are organized, but by now, she knows where you like things to go."
        "Set up only takes a few minutes."

        $ Laura.change_face("neutral", eyes = "down", blush = 1)

        "You get on the bed, with [Laura.name] taking her spot next to you. . ."

        $ Laura.change_face("angry1", eyes = "down", blush = 1)

        "Although, she leans into you a bit more firmly than usual."
        "As time goes on, you realize it's become much less of a tutoring session and more of a mutually beneficial study session."

        $ Laura.change_face("neutral", mouth = "smirk", eyes = "down", blush = 1)

        "[Laura.name] seems to enjoy one-upping you quite a bit, as she shows off her knowledge of things you weren't aware of."

        $ Laura.change_face("sly", blush = 1)

        "She points out one specific question." 

        ch_Player "You're quizzing me?" 

        $ Laura.change_face("confused1", mouth = "smirk", blush = 1)

        "She just taps on the question and waits."
        ch_Player "Okay. . ." 
        ch_Player "Is it. . . ?" 

        $ Laura.change_face("sly")

        ch_Player "No?"
        "She points to the correct answer."
        ch_Player "Shit. . ."

        $ Laura.change_face("smirk2")

        ch_Player "Could you. . . explain why?"

        $ Laura.change_face("neutral", eyes = "squint")

        ch_Player "You don't want to talk?"

        $ Laura.change_face("suspicious1")

        ch_Player "Or am I just missing something obvious?" 

        $ Laura.change_face("confused1", mouth = "smirk")

        "After finally figuring out what you were doing wrong, you feel pretty dumb."

        $ Laura.change_face("sly")

        if Player.location != Laura.home:
            "[Laura.name] just gives you a condescending pat on the shoulder, before getting up to leave."

            $ Laura.change_face("smirk2")

            ch_Player "Thanks for the help. . ."

            call remove_Characters(Laura) from _call_remove_Characters_120
        else:
            "[Laura.name] just gives you a condescending pat on the shoulder, before indicating you should leave."

            $ Laura.change_face("smirk2")

            ch_Player "Thanks for the help. . ."

            call set_the_scene(location = "bg_girls_hallway") from _call_set_the_scene_135
    elif dice_roll == 2:
        $ Laura.change_face("neutral", eyes = "squint")

        "[Laura.name] just stands there, not moving to help you set things up."

        ch_Player "Just gonna watch?"

        $ Laura.change_face("neutral", eyes = "right")

        pause 1.0

        $ Laura.change_face("neutral", eyes = "left")

        "After taking a moment to look around, out the windows, under the door, she responds."

        $ Laura.change_face("neutral", eyes = "squint")

        ch_Laura "Fine, here."
        "After a few minutes, everything's all set up."

        $ Laura.change_face("neutral", eyes = "down", blush = 1)

        "She 'gently' pushes you onto the bed, positioning herself between you and the door."

        $ Laura.change_face("angry1", eyes = "down", blush = 1)

        ch_Player "You could just ask me instead of pushing. . ." 

        $ Laura.change_face("neutral", mouth = "smirk", eyes = "down", blush = 1)

        ch_Laura "Let's start with this. . ."
        
        "She just ignores you, forcefully bumping into your shoulder, urging you to start the session."

        $ Laura.change_face("neutral", eyes = "down", blush = 1)

        "As an hour goes by, [Laura.name] surprises you with her knowledge, and it ends up being more of a review session for the both of you."
        "Although, you suspect she only studies so hard to try and one-up you, knowing how competitive she can be at times."

        $ Laura.change_face("neutral")

        ch_Laura "This one."
        "She points at a question."
        ch_Laura "Answer it."

        $ Laura.change_face("sly")

        ch_Player "That one?"
        ch_Player "It's choice A, right?"
        
        $ Laura.change_face("angry1")

        pause 1.0

        $ Laura.change_face("suspicious1")

        ch_Laura "Yes. . ." 
        "Seems like she didn't expect you to know the answer." 

        $ Laura.change_face("angry1", eyes = "down")

        "You finish up the session by going back and forth, quizzing each other, trying to gain the upper hand."

        $ Laura.change_face("suspicious1", eyes = "down")

        "Neither of you seems to be able to beat the other."

        $ Laura.change_face("angry1")

        ch_Laura "Enough, my head hurts." 
        ch_Player "Sure, let's call it there."

        if Player.location != Laura.home and renpy.random.random() > 0.5:
            call Characters_leave(Laura) from _call_Characters_leave_1
    elif dice_roll == 3:
        $ Laura.change_face("neutral", eyes = "right")

        pause 1.0

        $ Laura.change_face("neutral", eyes = "left")

        "After taking a second to look around, [Laura.name] moves to help you set things up."

        $ Laura.change_face("surprised1")

        ch_Player "Thanks for the help." 

        $ Laura.change_face("angry1", eyes = "right", blush = 1)

        ch_Laura "Sure. . ." 
        "This time, you jump onto the bed before she can push you."

        $ Laura.change_face("confused1", mouth = "smirk")

        "She plops down right next to you, making sure to bump into your shoulder on the way down."
        "Still positioning herself between you and the door."

        $ Laura.change_face("smirk2", eyes = "down", blush = 1)

        ch_Player "So. . . where did you want to start?"
        ch_Laura "You pick this time."

        $ Laura.change_face("neutral", eyes = "right", blush = 1)

        ch_Player "Sure."

        $ Laura.change_face("neutral", eyes = "down", blush = 1)

        ch_Player "Why don't we start with. . ."
        "You spend the next few hours going over one of [Laura.name]'s least favorite subjects."

        $ Laura.change_face("angry1", eyes = "down", blush = 1)

        "She realizes her mistake, letting you choose the topic for today's session and makes you pay for it. . ."

        $ Laura.change_face("suspicious1", blush = 1)

        ch_Laura "Why don't we move on to this. . ."

        $ Laura.change_face("angry1", eyes = "down", blush = 1)

        ch_Player "Wait, but. . ."

        $ Laura.change_face("angry1", mouth = "smirk", eyes = "down", blush = 1)

        "She forces a change in subject to one of your least favorites and seems to enjoy your suffering."

        $ Laura.change_face("neutral", eyes = "down", blush = 1)

        ch_Player "Do you know how to do this one?"
        "You point to a particular question."

        $ Laura.change_face("confused1", eyes = "down", blush = 1)

        ch_Laura "Isn't it. . . ?"
        "You check the answer key, and she explains how she got that answer."
        ch_Player "Nice, thanks."

        $ Laura.change_face("smirk2")

        ch_Player "I think we can call it there. . ." 

        $ Laura.change_face("confused1", mouth = "smirk", eyes = "squint")

        ch_Player "I've had enough of this subject."
        ch_Laura "Fine."
        ch_Laura "I'll stick around for a while."

    if Player.location == Laura.home and Player.location != Laura.location and Laura not in Keys:
        call set_the_scene(location = "bg_girls_hallway") from _call_set_the_scene_348
    
    $ ongoing_Event = False

    return