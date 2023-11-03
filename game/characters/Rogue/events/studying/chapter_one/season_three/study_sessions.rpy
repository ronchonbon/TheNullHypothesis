init python:

    def Rogue_chapter_one_season_three_study_sessions():
        label = "Rogue_chapter_one_season_three_study_sessions"

        conditions = [
            "season == 3",
            "Rogue.History.check('studied_with_Player', tracker = 'season') >= 1",
            "Player.studying == Rogue and Rogue.studying"]

        priority = 99
        repeatable = True

        return EventClass(label, conditions, priority = priority, repeatable = repeatable)

label Rogue_chapter_one_season_three_study_sessions:
    $ ongoing_Event = True

    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Rogue.change_face("happy")

        ch_Rogue "Ah'll help ya set up."

        $ Rogue.change_face("smirk2")

        ch_Player "I appreciate it."
        "By now you know how she likes things organized, so the actual setup doesn't take long at all."

        $ Rogue.change_face("smirk2", eyes = "down", blush = 1)

        "You both take your spots on the bed next to each other, and she leans into your shoulder as usual."

        $ Rogue.change_face("smirk2", eyes = "down", blush = 2)
        
        "This time, you actually help her with some of the material she was having trouble with."
        "You put your hand out for her to touch, as you continue to explain one of the practice questions."

        $ Rogue.change_face("smirk2", blush = 1)

        call take_off(Rogue, "gloves") from _call_take_off_16

        ch_Player "Okay, this one is pretty tricky, but I think you got it."
        "You point to a particularly tricky question."

        $ Rogue.change_face("confused1", mouth = "smirk")

        ch_Rogue "Ah kinda like havin' you as the tutor. . ."
        ch_Player "Think I'm any good at it?" 

        $ Rogue.change_face("smirk2", blush = 1)

        ch_Rogue "'Course ya are."
        ch_Rogue "Yer a surprisingly quick learner."

        $ Rogue.change_face("confused1", mouth = "smirk")

        ch_Rogue "Alright, 'nuff stallin'."
        ch_Rogue "Ah'm pretty sure the answer is choice C."

        $ Rogue.change_face("worried1", mouth = "smirk")

        ch_Player "Great job, you got it right." 

        $ Rogue.change_face("happy", blush = 1)

        pause 1.0

        $ Rogue.change_face("smirk2", eyes = "down", blush = 1)

        "You go over a couple more things, but the session is all but over."

        $ Rogue.change_face("smirk2", blush = 1)

        "You make sure she understands everything, before [Rogue.name] helps you put everything away." 
    elif dice_roll == 2:
        $ Rogue.change_face("worried1", mouth = "smirk")

        ch_Rogue "You been doin' alright?"
        ch_Player "Not the worst, could just really use the distraction right now."

        $ Rogue.change_face("smirk2")

        ch_Rogue "Ah'll be glad to provide that distraction."
        "She starts up some small talk, as you help her set everything up for the session."

        $ Rogue.change_face("smirk2", eyes = "down", blush = 1)

        "You have a nice conversation, before you plop down on the bed next to each other."
        "[Rogue.name] leans into your shoulder, and you automatically put one of your hands out for her to touch"

        $ Rogue.change_face("smirk2", mouth = "lipbite", eyes = "down", blush = 1)

        "The session starts, and she takes the lead, running you through some of your worst subjects." 
        "[Rogue.name] has always been able to make even difficult concepts easy to understand, and today is no different."

        $ Rogue.change_face("confused1", mouth = "smirk", blush = 1)

        ch_Rogue "Alright, [Rogue.Player_petname], ah think ya should be able to get this one right."
        "She points to one of the easier questions." 

        $ Rogue.change_face("confused1", eyes = "squint", mouth = "smirk")

        ch_Player "Oh c'mon, that's too easy."
        ch_Player "The answer is choice D."

        $ Rogue.change_face("sly")

        ch_Rogue "Sorry, darlin', that ain't it."
        ch_Rogue "It's choice C."

        ch_Player "Shit. . ."

        $ Rogue.change_face("confused1", mouth = "smirk")

        "[Rogue.name] makes sure to correct any misunderstandings, and the rest of the session goes by in a flash."
        "Any of the worries that plagued you are long forgotten."

        $ Rogue.change_face("worried1", mouth = "smirk")

        ch_Player "Thanks, [Rogue.petname]."
        ch_Player "This was really helpful, in more ways than one."
        ch_Rogue "'Course, [Rogue.Player_petname], {i}any{/i} time. . ."
        ch_Rogue "You know that, right?"

    $ ongoing_Event = False

    return