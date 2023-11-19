init python:

    def Rogue_chatting_study():
        label = "Rogue_chatting_study"

        conditions = [
            "renpy.random.random() > 0.75",
            
            "not Rogue.History.check('said_no_to_study', tracker = 'recent')",
            
            "not Rogue.History.check('Player_rejected_studying', tracker = 'daily') and not Rogue.History.check('Player_rejected_training', tracker = 'daily')",
            
            "not EventScheduler.Events['Rogue_chatting_study'].completed or day - EventScheduler.Events['Rogue_chatting_study'].completed_when >= 3",
            "not EventScheduler.Events['Rogue_texting_study'].completed or day - EventScheduler.Events['Rogue_texting_study'].completed_when >= 3",

            "Player.location == Rogue.location and Player.location in [Player.home, Rogue.home]",

            "Rogue.History.check('studied_with_Player') and not Rogue.History.check('studied_with_Player', tracker = 'weekly')",

            "time_index < 3 or approval_check(Rogue, threshold = 'talk_late')",

            "Rogue.is_in_normal_mood()",
            "approval_check(Rogue, threshold = 'friendship')"]

        waiting = True

        repeatable = True

        return EventClass(label, conditions, waiting = waiting, repeatable = repeatable)

label Rogue_chatting_study:
    $ Rogue.change_face("pleased1")

    ch_Rogue "Hey, [Rogue.Player_petname], think we should study?"

    menu:
        extend ""
        "Sorry, little busy!":
            $ Rogue.change_face("surprised1")

            ch_Rogue "No worries!"

            $ Rogue.History.update("Player_rejected_studying")
        "Yeah, definitely!":
            $ Rogue.change_face("happy")

            ch_Rogue "Great!"

            call actually_study(Rogue) from _call_actually_study_9
        "Why would I ever want to do that?":
            $ Rogue.change_face("apalled1")

            ch_Rogue "Ah just. . ."
            ch_Rogue "Never mind. . ."

            call change_Girl_stat(Rogue, "love", 0) from _call_change_Girl_stat_596

            $ Rogue.History.update("Player_rejected_studying")

    return

init python:

    def Rogue_chatting_training():
        label = "Rogue_chatting_training"

        conditions = [
            "renpy.random.random() > 0.9",

            "not Rogue.History.check('said_no_to_training', tracker = 'recent')",
            
            "not Rogue.History.check('Player_rejected_studying', tracker = 'daily') and not Rogue.History.check('Player_rejected_training', tracker = 'daily')",
            
            "not EventScheduler.Events['Rogue_chatting_training'].completed or day - EventScheduler.Events['Rogue_chatting_training'].completed_when >= 5",
            "not EventScheduler.Events['Rogue_texting_training'].completed or day - EventScheduler.Events['Rogue_texting_training'].completed_when >= 5",
            
            "Player.location == Rogue.location and Player.location == 'bg_danger'",

            "Rogue.History.check('trained_with_Player') and not Rogue.History.check('trained_with_Player', tracker = 'weekly')",

            "time_index < 3",

            "Rogue.is_in_normal_mood()",
            "approval_check(Rogue, threshold = 'friendship')"]

        waiting = True

        repeatable = True

        return EventClass(label, conditions, waiting = waiting, repeatable = repeatable)

label Rogue_chatting_training:
    $ Rogue.change_face("smirk2")

    ch_Rogue "Should we train, [Rogue.Player_petname]?"

    menu:
        extend ""
        "Maybe some other time?":
            $ Rogue.change_face("surprised1")

            ch_Rogue "Yeah, anytime!"

            $ Rogue.History.update("Player_rejected_training")
        "For sure!":
            $ Rogue.change_face("happy")

            ch_Rogue "Awesome!"

            call actually_train(Rogue) from _call_actually_train_6
        "With you? Nah.":
            $ Rogue.change_face("worried3")

            ch_Rogue "Wh- Oh. . ."
            ch_Rogue "Sorry. . ."

            call change_Girl_stat(Rogue, "love", 0) from _call_change_Girl_stat_597

            $ Rogue.History.update("Player_rejected_training")

    return

init python:

    def Rogue_chatting_date():
        label = "Rogue_chatting_date"

        conditions = [
            "renpy.random.random() > 0.9"
            
            "2 not in Rogue.schedule.keys() and 3 not in Rogue.schedule.keys()",
            "2 not in Player.schedule.keys() and 3 not in Player.schedule.keys()",

            "not Player.date_planned",

            "not Rogue.History.check('said_no_to_date', tracker = 'recent')",
            
            "not Rogue.History.check('Player_rejected_studying', tracker = 'daily') and not Rogue.History.check('Player_rejected_training', tracker = 'daily') and not Rogue.History.check('Player_rejected_date', tracker = 'weekly')",
            
            "not EventScheduler.Events['Rogue_chatting_date'].completed or day - EventScheduler.Events['Rogue_chatting_date'].completed_when >= 5",
            "not EventScheduler.Events['Rogue_texting_date'].completed or day - EventScheduler.Events['Rogue_texting_date'].completed_when >= 5",
            
            "Player.location == Rogue.location",

            "day - EventScheduler.Events['Rogue_first_date'].completed_when >= 5",
            "not EventScheduler.Events['Rogue_date'].completed or day - EventScheduler.Events['Rogue_date'].completed_when >= 5",

            "time_index < 2",

            "Rogue.is_in_normal_mood()",
            "approval_check(Rogue, threshold = 'dating')"]

        waiting = True

        repeatable = True

        return EventClass(label, conditions, waiting = waiting, repeatable = repeatable)

label Rogue_chatting_date:
    if Rogue.status["horny"] or Rogue.status["nympho"]:
        $ Rogue.change_face("sexy", eyes = "down", blush = 1)

        pause 1.0

        $ Rogue.change_face("sexy", blush = 1)
        
        $ temp = Rogue.Player_petname.capitalize()

        ch_Rogue "[temp], are ya free tonight?"

        $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

        ch_Rogue "Maybe we could go on a date?"

        $ Rogue.change_face("sexy", blush = 2)

        ch_Rogue "And spend some {i}quality{/i} time together. . ."
    elif Rogue.quirk and renpy.random.random() > 0.5:
        $ Rogue.change_face("worried1", mouth = "smirk")

        pause 1.0

        $ Rogue.change_face("worried1", mouth = "lipbite")
        
        $ temp = Rogue.Player_petname.capitalize()

        ch_Rogue "[temp]. . ."
        ch_Rogue "Can we go on a date tonight, please?"
    else:
        $ Rogue.change_face("worried1")

        ch_Rogue "So, [Rogue.Player_petname]."

        $ Rogue.change_face("worried1", mouth = "smirk")

        ch_Rogue "Ah'm free tonight."
        ch_Rogue "Would you wanna go on a date?"

    menu:
        extend ""
        "Count me in.":
            $ Player.date_planned[Rogue] = "Girl_initiated_primary"

            if time_index == 2:
                $ EventScheduler.Events["Rogue_date"].start()
        "Not tonight. . . sorry.":
            $ Rogue.change_face("worried1")

            $ Rogue.History.update("Player_rejected_date")

    return