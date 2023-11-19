init python:

    def Laura_chatting_study():
        label = "Laura_chatting_study"

        conditions = [
            "renpy.random.random() > 0.75",
            
            "not Laura.History.check('said_no_to_study', tracker = 'recent')",
            
            "not Laura.History.check('Player_rejected_studying', tracker = 'daily') and not Laura.History.check('Player_rejected_training', tracker = 'daily')",
            
            "not EventScheduler.Events['Laura_chatting_study'].completed or day - EventScheduler.Events['Laura_chatting_study'].completed_when >= 3",
            "not EventScheduler.Events['Laura_texting_study'].completed or day - EventScheduler.Events['Laura_texting_study'].completed_when >= 3",

            "Player.location == Laura.location and Player.location in [Player.home, Laura.home]",

            "Laura.History.check('studied_with_Player') and not Laura.History.check('studied_with_Player', tracker = 'weekly')",

            "time_index < 3 or approval_check(Laura, threshold = 'talk_late')",

            "Laura.is_in_normal_mood()",
            "approval_check(Laura, threshold = 'friendship')"]

        waiting = True

        repeatable = True

        return EventClass(label, conditions, waiting = waiting, repeatable = repeatable)

label Laura_chatting_study:
    $ Laura.change_face("neutral")

    ch_Laura "We should study."

    menu:
        extend ""
        "Sorry, kinda busy.":
            $ Laura.eyes = "right"

            ch_Laura "Yeah, whatever."

            $ Laura.History.update("Player_rejected_studying")
        "Yeah, okay!":
            $ Laura.change_face("smirk1")

            call actually_study(Laura) from _call_actually_study_6
        "Not in the mood, [Laura.name]. . .":
            $ Laura.change_face("angry1")

            if Jean.location != Player.location:
                ch_Laura "{i}Grrrr{/i}, where's the redhead when you need her."
            else:
                ch_Laura "{i}Grrrr{/i}."

            call change_Girl_stat(Laura, "love", 0) from _call_change_Girl_stat_339

            $ Laura.History.update("Player_rejected_studying")

    return

init python:

    def Laura_chatting_training():
        label = "Laura_chatting_training"

        conditions = [
            "renpy.random.random() > 0.9",

            "not Laura.History.check('said_no_to_training', tracker = 'recent')",
            
            "not Laura.History.check('Player_rejected_studying', tracker = 'daily') and not Laura.History.check('Player_rejected_training', tracker = 'daily')",
            
            "not EventScheduler.Events['Laura_chatting_training'].completed or day - EventScheduler.Events['Laura_chatting_training'].completed_when >= 5",
            "not EventScheduler.Events['Laura_texting_training'].completed or day - EventScheduler.Events['Laura_texting_training'].completed_when >= 5",
            
            "Player.location == Laura.location and Player.location == 'bg_danger'",

            "Laura.History.check('trained_with_Player') and not Laura.History.check('trained_with_Player', tracker = 'weekly')",

            "time_index < 3",

            "Laura.is_in_normal_mood()",
            "approval_check(Laura, threshold = 'friendship')"]

        waiting = True

        repeatable = True

        return EventClass(label, conditions, waiting = waiting, repeatable = repeatable)

label Laura_chatting_training:
    $ Laura.change_face("confused1")

    ch_Laura "Why aren't we training already?"

    menu:
        extend ""
        "Maybe some other time?":
            $ Laura.change_face("angry1", eyes = "right")

            ch_Laura "Your problem."

            $ Laura.History.update("Player_rejected_training")
        "Yeah, good point.":
            $ Laura.change_face("smirk1")

            ch_Laura "Good."

            call actually_train(Laura) from _call_actually_train_3
        "Because I like to take breaks between getting the shit kicked out of me?":
            $ Laura.change_face("angry1", eyes = "squint")

            ch_Laura "Wimp. . ."    

            call change_Girl_stat(Laura, "love", 0) from _call_change_Girl_stat_340

            $ Laura.History.update("Player_rejected_training")

    return

init python:

    def Laura_chatting_date():
        label = "Laura_chatting_date"

        conditions = [
            "renpy.random.random() > 0.9"
            
            "2 not in Laura.schedule.keys() and 3 not in Laura.schedule.keys()",
            "2 not in Player.schedule.keys() and 3 not in Player.schedule.keys()",

            "not Player.date_planned",

            "not Laura.History.check('said_no_to_date', tracker = 'recent')",
            
            "not Laura.History.check('Player_rejected_studying', tracker = 'daily') and not Laura.History.check('Player_rejected_training', tracker = 'daily') and not Laura.History.check('Player_rejected_date', tracker = 'weekly')",
            
            "not EventScheduler.Events['Laura_chatting_date'].completed or day - EventScheduler.Events['Laura_chatting_date'].completed_when >= 5",
            "not EventScheduler.Events['Laura_texting_date'].completed or day - EventScheduler.Events['Laura_texting_date'].completed_when >= 5",
            
            "Player.location == Laura.location",

            "day - EventScheduler.Events['Laura_first_date'].completed_when >= 5",
            "not EventScheduler.Events['Laura_date'].completed or day - EventScheduler.Events['Laura_date'].completed_when >= 5",

            "time_index < 2",

            "Laura.is_in_normal_mood()",
            "approval_check(Laura, threshold = 'dating')"]

        waiting = True

        repeatable = True

        return EventClass(label, conditions, waiting = waiting, repeatable = repeatable)

label Laura_chatting_date:
    if Laura.status["horny"] or Laura.status["nympho"]:
        $ Laura.change_face("sly", eyes = "down", blush = 1)

        pause 1.0

        $ Laura.change_face("sexy", blush = 1)

        ch_Laura "I want to go on a date. . . and spend some time with you tonight. . ."
    elif Laura.quirk and renpy.random.random() > 0.5:
        $ Laura.change_face("angry1", eyes = "right")

        pause 1.0

        $ Laura.change_face("angry1")

        ch_Laura "I want to go on a date with you tonight."
    else:
        $ Laura.change_face("sly")

        ch_Laura "We're going on a date tonight."

    menu:
        extend ""
        "Count me in.":
            $ Player.date_planned[Laura] = "Girl_initiated_primary"

            if time_index == 2:
                $ EventScheduler.Events["Laura_date"].start()
        "Not tonight. . . sorry.":
            $ Laura.change_face("neutral", eyes = "squint")

            $ Laura.History.update("Player_rejected_date")

    return