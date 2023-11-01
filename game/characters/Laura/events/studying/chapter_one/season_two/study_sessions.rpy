init python:

    def Laura_chapter_one_season_two_study_sessions():
        label = "Laura_chapter_one_season_two_study_sessions"

        conditions = [
            "season == 2",
            "Laura.History.check('studied_with_Player', tracker = 'season') >= 1",
            "Player.studying == Laura and Laura.studying"]

        priority = 99
        repeatable = True

        return EventClass(label, conditions, priority = priority, repeatable = repeatable)

label Laura_chapter_one_season_two_study_sessions:
    $ ongoing_Event = True

    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        $ Laura.change_face("neutral")

        ch_Player "Can you help me set things up?"

        $ Laura.change_face("confused1")

        ch_Laura "Fine, but tell me where things go in the first place."

        $ Laura.change_face("neutral")

        ch_Player "Right. . ."

        $ Laura.change_face("angry1", eyes = "down")

        "She does help you organize all the materials, and it barely takes a few minutes under your direction."
        "Instead of shying away from close contact, she seems to gravitate closer to you at times. . ." 

        $ Laura.change_face("surprised2")

        ". . . although she still can't help but react to unexpected contact." 

        $ Laura.change_face("angry1", eyes = "right", blush = 1)

        "For the next several hours, you do your best to tutor [Laura.name]."

        $ Laura.change_face("angry1", blush = 1)

        "Again, she inches closer to you as the session goes on."
        "Despite the angry look on her face she seems very attentive and puts in a great deal of effort to learn the material."
        ch_Player "Okay, this one is definitely gonna be on the quiz this week." 
        "You show her a question from class." 

        $ Laura.change_face("confused1")

        ch_Laura "What's the correct answer?" 
        ch_Player "It's. . ." 

        $ Laura.change_face("angry1", blush = 1)

        ch_Laura "{i}Grrrrrr{/i}. . ."
        "Her frustration mounts as she continues to get questions wrong."
        "To the point where the session has become quite unproductive." 

        $ Laura.change_face("furious")

        ch_Player "I think we should stop."

        $ Laura.change_face("angry1")

        ch_Player "You're not making any progress by being angry. . ." 
        ch_Laura "Fine, then I'm going to train to blow off steam." 

        $ Laura.change_face("neutral")
    elif dice_roll == 2:
        $ Laura.change_face("neutral", eyes = "down")

        "Without any prompting, [Laura.name] starts organizing and setting up the study materials."
        "With your help, it only takes a few minutes to get everything set up."

        $ Laura.change_face("neutral")

        ch_Player "You seem eager today."

        $ Laura.change_face("surprised2")

        pause 1.0

        $ Laura.change_face("angry1")

        ch_Laura "I am not. . . eager. . ."

        $ Laura.change_face("angry1", eyes = "right")

        ch_Laura "Let's just get this over with." 
        ch_Player "If you say so. . ."

        $ Laura.change_face("suspicious1")

        ch_Player "Let's get started."
        "Despite claiming otherwise, [Laura.name] does seem more attentive than usual."
        "She actively listens and even asks questions to clarify things she was unsure about."

        $ Laura.change_face("neutral", eyes = "down")

        ch_Player "Here, why don't you try this practice question."

        $ Laura.change_face("confused1")

        ch_Laura "That one?" 
        "You picked this question assuming she wouldn't know the answer, but. . ."

        $ Laura.change_face("neutral")

        ch_Laura "It's choice B." 
        ch_Player "N-"
        ch_Player "Wait, that's actually right." 

        $ Laura.change_face("sly")

        ch_Player "How'd you know?"
        ch_Player "We didn't go over that stuff yet."

        $ Laura.change_face("angry1", eyes = "right")

        ch_Laura "I. . . might've listened to a few things during lecture the other day. . ." 

        $ Laura.change_face("furious", eyes = "right")

        ch_Laura "Didn't want to waste so much of your time."
        ch_Laura "Or whatever. . ."
        ch_Player "Thanks, [Laura.petname]."

        $ Laura.change_face("furious")

        ch_Player "I really do appreciate the thought."

        $ Laura.change_face("angry1")

        ch_Laura "You're welcome." 
        ch_Laura "Bye."
    elif dice_roll == 3:
        $ Laura.change_face("neutral")

        ch_Laura "I will help set things up."
        ch_Player "Thanks, [Laura.petname]." 

        $ Laura.change_face("neutral", eyes = "squint")

        ch_Player "What. . . ?" 
        ch_Laura "You're welcome."
        "With her help, it barely takes a few minutes."

        $ Laura.change_face("smirk1")

        "Seems like she's catching on and knows how you like to organize things, making it go even faster than usual."
        ch_Player "I was thinking about starting with the psychology stuff today."
        ch_Laura "I would rather start with calculus."
        ch_Player "Oh?"

        $ Laura.change_face("angry1")

        ch_Laura "I've been. . ."

        $ Laura.change_face("angry1", eyes = "right")

        ch_Laura ". . . paying more attention in class." 

        $ Laura.change_face("angry1")

        ch_Laura "Psychology is one of the more tolerable subjects."

        $ Laura.change_face("furious")

        ch_Laura "But I hate calculus."
        ch_Player "You and me both. . ."

        $ Laura.change_face("neutral")

        ch_Player "Sure, we can start there."
        "Has math ever been your best subject?"
        "Regardless, ever since you nearly died and got a massive concussion, it comes more naturally to you."
        "While you might not enjoy calculus, brain damage seems to have rewired a few things."

        $ Laura.change_face("confused1")

        "You do your best to go over the important things from class, but [Laura.name] struggles more than usual."

        $ Laura.change_face("furious", eyes = "down")

        ch_Laura "{i}Grrrrrr{/i}"
        ch_Laura "How the hell am I supposed to know this?"

        $ Laura.change_face("angry1")

        "She points to a particular question."

        ch_Player "Oh that one?"
        ch_Player "I'm pretty sure it's. . ."

        $ Laura.change_face("angry1")

        ch_Laura "Math makes me angry." 
        ch_Player "It has that effect on a lot of people."
        ch_Player "Let's call it there before you. . . end up clawing the textbook to death."

        $ Laura.change_face("neutral", eyes = "squint")

        ch_Laura "How'd you know what I was thinking?"

    call remove_Characters(Laura) from _call_remove_Characters_125

    if Player.location == Laura.home and Laura not in Keys:
        call set_the_scene(location = "bg_girls_hallway") from _call_set_the_scene_353

    call change_Girl_stat(Laura, "love", 5) from _call_change_Girl_stat_404
    
    $ ongoing_Event = False

    return