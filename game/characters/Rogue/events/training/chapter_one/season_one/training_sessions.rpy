init python:

    def Rogue_chapter_one_season_one_training_sessions():
        label = "Rogue_chapter_one_season_one_training_sessions"

        conditions = [
            "chapter == 1 and season == 1",
            "Rogue.History.check('trained_with_Player', tracker = 'season') >= 1",
            "Player.training == Rogue and Rogue.training"]

        priority = 99
        repeatable = True

        return EventClass(label, conditions, priority = priority, repeatable = repeatable)

label Rogue_chapter_one_season_one_training_sessions:
    $ ongoing_Event = True

    $ dice_roll = renpy.random.randint(1, 4)

    if dice_roll == 1:
        $ Rogue.change_face("pleased1")

        ch_Player "Ready to start?" 

        $ Rogue.change_face("smirk2")

        ch_Rogue "Yep."

        "You help each other limber up, and [Rogue.name] seems to enjoy the brief contact."

        $ Rogue.change_face("smirk2", mouth = "lipbite")

        "You were taught how to train techniques on your own, and you attempt to pass some of the knowledge on to [Rogue.name]." 

        $ Rogue.change_face("smirk2")

        "You barely know what you're doing, and [Rogue.name] ends up doing most of the teaching."
        "It was a productive session nonetheless."
        "You both finish up the session with some basic exercises."
        "She's in great shape too. . ."

        $ Rogue.change_face("happy")

        ch_Rogue "Thanks for the session, [Rogue.Player_petname]." 

        $ Rogue.change_face("worried1", mouth = "smirk")

        ch_Rogue "You don't know how nice it is. . . makes me feel a bit normal. . ."

        $ Rogue.change_face("smirk2")

        ch_Rogue "Ah'll see ya later."
    elif dice_roll == 2:
        $ Rogue.change_face("smirk2")

        ch_Player "Today's gonna be good, I can tell."

        $ Rogue.change_face("smirk2", eyes = "down", blush = 1)

        ch_Rogue "Already is now that yer here. . ."

        $ Rogue.change_face("smirk2", mouth = "lipbite")

        "You both go through a standard warm up and feel more energetic than usual."
        "[Rogue.name] seems to particularly enjoy helping you stretch."

        $ Rogue.change_face("smirk2")

        "Afterwards, she leads you through a few drills, trying to teach you everything she's picked up so far."
        "She couldn't spar with anyone, but she's a good student and was still able to learn a lot just by observing other people."
        "You already know [Rogue.name] is a great teacher from the tutoring sessions, and she makes it easy to absorb the lesson."

        $ Rogue.change_face("happy")

        ch_Rogue "Great job today, [Rogue.Player_petname]!" 

        $ Rogue.change_face("smirk2")

        ch_Rogue "Yer a real quick learner." 
        ch_Player "Thanks, and you're a great teacher." 

        $ Rogue.change_face("smirk2", blush = 1)

        ch_Rogue "Thanks. . . ah'll see ya later, [Rogue.Player_petname]."
    elif dice_roll == 3:
        $ Rogue.change_face("happy")

        $ Rogue.change_face("smirk2")

        ch_Rogue "Ready to go?"
        ch_Player "Yep! Let's start."
        "After a brief warm up, you spend the next couple hours practicing some fairly basic techniques together."
        "Despite being a grade above you, the practice helps [Rogue.name] almost as much as it helps you."
        "Knowledge can't make up for lacking practical experience."

        $ Rogue.change_face("smirk2", mouth = "lipbite")

        "The both of you make good progress, and she seems to be thoroughly enjoying the contact."
        "You finish the session with a workout and feel great afterwards."

        $ Rogue.change_face("happy")

        ch_Rogue "Ah really wish ah'd known ya sooner."

        $ Rogue.change_face("smirk2", mouth = "lipbite")

        ch_Rogue "Feels great finally bein' able to train with someone. . ."
        ch_Player "You are a great training partner." 

        $ Rogue.change_face("smirk2", mouth = "lipbite", blush = 1)

        ch_Rogue "Thanks."
        ch_Rogue "Ah'll be seein' you later."
        ch_Rogue "Bye, [Rogue.Player_petname]."
    elif dice_roll == 4:
        $ Rogue.change_face("worried1")

        ch_Player "Hey, is everything alright?" 
        ch_Rogue "Yeah. . . ah'm just worried 'bout how little progress ah've made with my power."

        $ Rogue.change_face("worried1", mouth = "smirk")

        ch_Rogue "Don't wanna drag you into it. . . let's just get to trainin'."
        ch_Rogue "That'll help distract me."
        ch_Player "Sure, let's start." 

        $ Rogue.change_face("smirk1")

        ch_Rogue "Thanks, [Rogue.Player_petname]."
        "[Rogue.name] dives head first into the warm up, making it a bit more intense than usual."

        $ Rogue.change_face("angry1")

        "She seems distracted during the session, and you wonder if you should say something."

        $ Rogue.change_face("furious")

        "During sparring, she almost seems to be taking her frustrations out on you, pushing you to your limit."

        $ Rogue.change_face("worried1")

        "Although, after seeing you start to struggle, she seems to snap out of it."

        $ Rogue.change_face("worried1", eyes = "right")

        "The session finishes up as normal and, in the end, it was productive."

        $ Rogue.change_face("worried1")

        ch_Rogue "Ah'm sorry, [Rogue.Player_petname]." 
        ch_Rogue "Didn't mean to take it out on you. . ."
        ch_Rogue "Just had a lot on my mind."
        ch_Player "Don't worry about it."
        ch_Player "It's not good to keep things bottled up."

        $ Rogue.change_face("worried1", eyes = "right")

        ch_Rogue "Ah know. . ."
        ch_Player "Remember, if you want to vent to someone, just let me know."
        ch_Player "I'm always available."

        $ Rogue.change_face("worried1", mouth = "smirk")

        ch_Rogue "Ah appreciate it, [Rogue.Player_petname]."
        ch_Rogue "Might take ya up on that. . ."
        ch_Rogue "See ya later."

    call remove_Characters(Rogue) from _call_remove_Characters_201

    $ ongoing_Event = False

    return