init python:

    def Rogue_chatting_study():
        label = "Rogue_chatting_study"

        conditions = [
            "renpy.random.random() > 0.75",
            
            "not Rogue.History.check('said_no_to_study', tracker = 'recent')",
            
            "not Player.History.check('received_invite', tracker = 'daily')",

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

    $ Player.History.update("received_invite")

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
            call change_Character_stat(Rogue, "love", -tiny_stat) from _call_change_Character_stat_596

            $ Rogue.change_face("apalled1")

            ch_Rogue "Ah just. . ."
            ch_Rogue "Never mind. . ."

            $ Rogue.History.update("Player_rejected_studying")

    return

init python:

    def Rogue_chatting_training():
        label = "Rogue_chatting_training"

        conditions = [
            "renpy.random.random() > 0.75",

            "not Rogue.History.check('said_no_to_training', tracker = 'recent')",
            
            "not Player.History.check('received_invite', tracker = 'daily')",

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

    $ Player.History.update("received_invite")

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
            call change_Character_stat(Rogue, "love", -tiny_stat) from _call_change_Character_stat_597

            $ Rogue.change_face("worried3")

            ch_Rogue "Wh- Oh. . ."
            ch_Rogue "Sorry. . ."

            $ Rogue.History.update("Player_rejected_training")

    return

init python:

    def Rogue_chatting_date():
        label = "Rogue_chatting_date"

        conditions = [
            "renpy.random.random() > 0.75"
            
            "2 not in Rogue.schedule.keys() and 3 not in Rogue.schedule.keys()",
            "2 not in Player.schedule.keys() and 3 not in Player.schedule.keys()",

            "not Player.date_planned",

            "not Rogue.History.check('said_no_to_date', tracker = 'recent')",
            
            "not Player.History.check('received_invite', tracker = 'daily')",

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
    elif Rogue.check_traits("quirk") and renpy.random.random() > 0.5:
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

    $ Player.History.update("received_invite")

    menu:
        extend ""
        "Count me in.":
            $ Player.date_planned[Rogue] = "Character_initiated_primary"

            if time_index == 2:
                $ EventScheduler.Events["Rogue_date"].start()
        "Not tonight. . . sorry.":
            $ Rogue.change_face("worried1")

            $ Rogue.History.update("Player_rejected_date")

    return