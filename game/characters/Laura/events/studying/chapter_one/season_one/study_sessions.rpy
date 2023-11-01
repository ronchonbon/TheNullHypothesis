init python:

    def Laura_chapter_one_season_one_study_sessions():
        label = "Laura_chapter_one_season_one_study_sessions"

        conditions = [
            "season == 1",
            "Laura.History.check('studied_with_Player', tracker = 'season') >= 1",
            "Player.studying == Laura and Laura.studying"]

        priority = 99
        repeatable = True

        return EventClass(label, conditions, priority = priority, repeatable = repeatable)

label Laura_chapter_one_season_one_study_sessions:
    $ ongoing_Event = True

    $ dice_roll = renpy.random.randint(1, 4)

    if dice_roll == 1:
        $ Laura.change_face("neutral")

        ch_Player "Don't just throw everything on the bed."

        $ Laura.change_face("confused1")

        ch_Player "It'll make things easier if we just organize everything."

        $ Laura.change_face("neutral")

        ch_Laura "Fine."

        $ Laura.change_face("angry1", eyes = "down")

        "She actually helps you organize things this time."
        "While you're setting things up, her hand accidentally brushes against yours. . ." 

        $ Laura.change_face("surprised2")

        ". . . and she jerks it away out of reflex." 

        $ Laura.change_face("angry1", eyes = "right", blush = 1)

        "You spend the next couple hours guiding [Laura.name] through the course materials."

        $ Laura.change_face("angry1", eyes = "down", blush = 1)

        "You notice her nostrils flare, and she scoots a bit further away from you."
        ch_Player "Okay, this one is definitely gonna be on the quiz this week." 
        "You show her a question from class." 

        $ Laura.change_face("confused1")

        ch_Laura "Is it. . ." 
        ch_Player "Uhh, no. . . It's . . ." 

        $ Laura.change_face("angry1", blush = 1)

        "You spend a while longer, correcting some misconceptions she apparently had. . ." 

        $ Laura.change_face("neutral")

        ch_Laura "That's enough."

        $ Laura.change_face("angry1")

        ch_Laura "I need to catch up on training." 
        ch_Player "Have fun." 

        $ Laura.change_face("confused1")
    elif dice_roll == 2:
        $ Laura.change_face("neutral")

        ch_Player "Here, just let me organize things first."
        ch_Laura "I will help. . ."

        $ Laura.change_face("neutral", eyes = "down")

        "It only takes a few minutes to set things up with her help."
        "You do notice any time she gets close to you, her nostrils flare slightly, and she shifts away a bit."

        $ Laura.change_face("surprised2")

        ch_Player "Do I really smell that good?"

        $ Laura.change_face("appalled1")

        ". . ."
        "She just glares at you."
        ch_Player "Never mind. . ."

        $ Laura.change_face("angry1", eyes = "down")

        "You start the lesson by going over what you've learned in class so far."
        "You start with one of your better subjects, so it's fairly easy to get [Laura.name] up to speed."

        $ Laura.change_face("neutral", eyes = "down")

        "She goes through some practice tests, and you periodically correct her or answer any questions she may have."

        $ Laura.change_face("confused1")

        ch_Laura "Is this one right?" 
        "You look it over and can see where she went wrong."
        ch_Player "No, it's actually. . . because. . ." 

        $ Laura.change_face("angry1")

        ch_Laura "Fuck." 

        $ Laura.change_face("neutral")

        "The rest of the session goes by quickly, as you slowly but surely get [Laura.name] to understand the material."

        $ Laura.change_face("surprised2")

        ch_Player "Not bad, you're making pretty good progress." 

        $ Laura.change_face("angry1", eyes = "right")

        ch_Laura "Thanks. . ."

        $ Laura.change_face("neutral")

        ch_Player "That's all for today, you gonna go train now?" 
        ch_Laura "Yes."
    elif dice_roll == 3:
        "[Laura.name] carelessly tosses all her notes and study materials onto the bed."
        ch_Player "Next time, just let me set things up. . ." 

        $ Laura.change_face("confused1")

        ch_Laura "Fine. . ." 

        $ Laura.change_face("neutral")

        "You take a moment to reorganize everything."

        $ Laura.change_face("suspicious1")

        "[Laura.name] just sits there, watching you intently." 

        $ Laura.change_face("neutral")

        ch_Player "{i}Ahem{/i}. . . so, which class do you want to work on today?"
        ch_Laura "This one. . ."

        $ Laura.change_face("angry1")

        ch_Player "Do you remember anything at all from the lectures?"
        ch_Laura ". . ." 

        $ Laura.change_face("neutral")

        ch_Player "From the top then. . ."

        $ Laura.change_face("angry1", eyes = "down")

        "While going over what [Laura.name] missed during class, you notice she's getting a bit frustrated."
        "It takes longer than usual, but you take your time and make sure she understands the concepts."

        $ Laura.change_face("neutral")

        "You finish the lesson by giving her practice questions."
        "She only has trouble with one of them."

        $ Laura.change_face("confused1")

        ch_Laura "I don't know this one, tell me the answer." 

        $ Laura.change_face("angry1")

        "She points to a particular question."
        ch_Player "I'm pretty sure it's. . ."

        $ Laura.change_face("neutral")

        ch_Laura "I've had enough, I'm going to train now." 
        ch_Player "Bye. . ."
    elif dice_roll == 4:
        $ Laura.change_face("neutral")

        "You start setting things up for the session before [Laura.name] can mess anything up."

        $ Laura.change_face("confused1")

        "At least she tries to help after a minute."

        $ Laura.change_face("neutral")

        ch_Player "I was thinking about starting with this class today, sound good?"
        ch_Laura "Fine."
        "You mainly focus on topics from the study guide and have [Laura.name] try practice questions."
        "She actually seems pretty good with the course material."
        "It appears your tutoring sessions have been somewhat effective."

        $ Laura.change_face("confused1")

        ch_Laura "This one. . ."
        "She points to a particular question."
        ch_Laura "This is the answer, right?"

        $ Laura.change_face("smirk2")

        ch_Player "Yep, that's right."
        "Since she did so well, things went faster than expected."
        "You just spend the last bit of time doing some review."

        $ Laura.change_face("neutral", eyes = "right")

        "Out of the corner of your eye, you notice [Laura.name] scoot a bit away from you, as her nostrils flare slightly."

        $ Laura.change_face("angry1", blush= 1)

        ch_Player "Alright, that should be everything for now." 

        $ Laura.change_face("angry1")

        ch_Laura "Good, I need to go train."
        
    call remove_Characters(Laura) from _call_remove_Characters_122

    if Player.location == Laura.home and Laura not in Keys:
        call set_the_scene(location = "bg_girls_hallway") from _call_set_the_scene_350

    call change_Girl_stat(Laura, "love", 5) from _call_change_Girl_stat_395
    
    $ ongoing_Event = False

    return