init python:

    def Rogue_chapter_one_season_two_training_sessions():
        label = "Rogue_chapter_one_season_two_training_sessions"

        conditions = [
            "season == 2",
            "Rogue.History.check('trained_with_Player', tracker = 'season') >= 1",
            "Player.training == Rogue and Rogue.training"]

        priority = 99
        repeatable = True

        return EventClass(label, conditions, priority = priority, repeatable = repeatable)

label Rogue_chapter_one_season_two_training_sessions:
    $ ongoing_Event = True

    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        $ Rogue.change_face("worried1", mouth = "smirk")
            
        ch_Rogue "Ya doin' alright?"
        ch_Player "Yeah, I'm fine."
        ch_Player "Are you okay?" 

        $ Rogue.change_face("worried1", eyes = "right", mouth = "smirk")

        ch_Rogue "Yeah."

        $ Rogue.change_face("worried1")

        ch_Rogue "Just glad ya wanted to train with me again. . ."
        ch_Player "Of course I do."
        ch_Player "It's way more fun, not to mention less painful, when doing it with you."

        $ Rogue.change_face("worried1", mouth = "smirk")

        ch_Rogue "It is fun. . ."
        ch_Rogue "Let's get started."

        $ Rogue.change_face("smirk2")

        "You go through a quick warmup, and [Rogue.name] mentions how much your physique has changed recently."

        $ Rogue.change_face("smirk2", mouth = "lipbite")

        "She has a hard time focusing on the workouts."
        "But once you get into the training, she's all business."

        $ Rogue.change_face("angry1")

        "You both spend a few hours practicing various techniques and also having a good bit of fun." 
        "[Rogue.name] seems to thoroughly enjoy the company."
        "She's also more competitive than you would've thought, trying to push herself to keep up with you, to no avail."

        $ Rogue.change_face("angry1", mouth = "smirk")

        "Your advantages in strength and speed give an edge."
        "As usual, the session was productive, but also fun and relaxing in a way."

        $ Rogue.change_face("happy")

        ch_Rogue "Thanks, [Rogue.Player_petname]." 

        $ Rogue.change_face("worried1", mouth = "smirk")

        ch_Rogue "Ah really like trainin' with ya. . ."
        ch_Player "I really like it too."

        $ Rogue.change_face("smirk2")

        ch_Rogue "Ah'll see ya later."
    elif dice_roll == 2:
        $ Rogue.change_face("smirk2")

        ch_Player "Ready to go, [Rogue.petname]?" 
        ch_Rogue "Yep!"
        ch_Rogue "Thanks for trainin' with me today. . ."

        $ Rogue.change_face("smirk2", mouth = "lipbite")

        ch_Player "You don't have to thank me every time."

        $ Rogue.change_face("smirk2", eyes = "down", blush = 1)

        ch_Rogue "Ah know."
        ch_Rogue "But still. . ."

        $ Rogue.change_face("smirk2", mouth = "lipbite")

        ch_Player "C'mon, let's get started."
        "You both go through a quick warmup, with [Rogue.name] doing her best to keep up with you during all the exercises."
        "Her fitness is fantastic compared to a normal person, but your new situation keeps you improving at a normally unattainable rate."
        "She doesn't seem to mind and just enjoys the company."

        $ Rogue.change_face("smirk2")

        "After transitioning to technique and sparring practice, something else becomes clear."

        if Laura.History.check("trained_with_Player", tracker = "season") >= 2:
            "It's as if your progress is as fast as ever." 
            
            $ Rogue.change_face("surprised1") 
            
            "All that training with [Laura.name] has really sunk in." 
            "You're stronger and faster now, sure. . ." 
            "But in terms of learning proper technique - and implementing it practically - you outclass [Rogue.name] by a mile."
        else:
            "Even though you haven't been training combat techniques as much as you should lately." 
            "Your progress is still substantially faster than [Rogue.name]'s." 
            
            $ Rogue.change_face("surprised1") 
            
            "Who knows where you'd be right now if you trained with [Laura.name] more."

        "Despite her competitive side pushing her to try and keep up, [Rogue.name] just seems happy that you're getting so much better."

        $ Rogue.change_face("confused1", mouth = "smirk")

        ch_Rogue "Yer makin' some real impressive progress." 

        $ Rogue.change_face("smirk2")

        ch_Rogue "Wish ah got better that fast." 
        ch_Player "Thanks, [Rogue.petname]."
        ch_Player "Don't worry, just because I'm that much better, doesn't mean I'll stop training with you."

        $ Rogue.change_face("sly", blush = 1)

        ch_Rogue "Yer a real joker, ain't ya."
        ch_Rogue "You better keep trainin' with me, so ah have an excuse to hit ya."
        ch_Player "You can try."

        $ Rogue.change_face("sly")

        ch_Rogue "Ah'll be seein' you later."
    elif dice_roll == 3:
        $ Rogue.change_face("happy")

        ch_Rogue "Ya ready to start?" 

        $ Rogue.change_face("smirk2")

        ch_Player "Sure am."
        ch_Player "C'mon."
        "You spend just as much time chatting as you do warming up."
        "It's nice, not having to push yourself to the breaking point for once."

        $ Rogue.change_face("angry1", mouth = "smirk")

        "Once you start the actual training, [Rogue.name]'s game face returns."
        "She knows she can't keep up with you physically anymore, so she does her best to one up you with better technique."
        "It's clear she's spent a lot of time training, and your physique doesn't give you as much of an edge as it should."
        "The session ends up being a great workout for both of you and good fun."

        $ Rogue.change_face("happy")

        ch_Rogue "Thanks again for the trainin'."

        $ Rogue.change_face("smirk2", mouth = "lipbite")

        ch_Rogue "It's always a great time. . ."
        ch_Player "Of course, [Rogue.petname]." 
        ch_Player "We'll just have to do it more often."

        $ Rogue.change_face("smirk2", mouth = "lipbite", blush = 1)

        ch_Rogue "Ah sure hope so. . ."
        ch_Rogue "See ya later, [Rogue.Player_petname]."

    call remove_Characters(Rogue) from _call_remove_Characters_206

    $ ongoing_Event = False

    return