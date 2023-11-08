init python:

    def Jean_chatting_study():
        label = "Jean_chatting_study"

        conditions = [
            "Jean.History.check('studied_with_Player')",
            "not Jean.History.check('studied_with_Player', tracker = 'weekly')",
            "time_index < 3 or approval_check(Jean, threshold = 'talk_late')",
            "Player.location == Jean.location and Player.location in [Player.home, Jean.home]",
            "not Jean.History.check('said_no_to_study', tracker = 'recent')",
            "not Jean.History.check('Player_rejected_studying', tracker = 'daily') and not Jean.History.check('Player_rejected_training', tracker = 'daily')",
            "not EventScheduler.Events['Jean_chatting_study'].completed or day - EventScheduler.Events['Jean_chatting_study'].completed >= 3",
            "not EventScheduler.Events['Jean_texting_study'].completed or day - EventScheduler.Events['Jean_texting_study'].completed >= 3",
            "not Jean.status['miffed'] and not Jean.status['mad'] and not Jean.status['heartbroken'] and not Jean.wants_alone_time",
            "approval_check(Jean, threshold = 'friendship')",
            "renpy.random.random() > 0.75"]

        waiting = True

        repeatable = True

        return EventClass(label, conditions, waiting = waiting, repeatable = repeatable)

label Jean_chatting_study:
    $ Jean.change_face("smirk2")

    ch_Jean "What do you think, should we squeeze in some study time?"

    menu:
        extend ""
        "Sorry, little busy right now.":
            $ Jean.change_face("confused1")

            ch_Jean "Ugh, fine."

            $ Jean.History.update("Player_rejected_studying")
        "Yeah, sure!":
            $ Jean.change_face("happy")

            ch_Jean "Awesome!"

            call actually_study(Jean) from _call_actually_study
        "I'm good. . .":
            $ Jean.change_face("worried1")

            ch_Player "Studying sucks."
            ch_Jean "Aw. . ."
            ch_Jean "Fine, your loss."

            call change_Girl_stat(Jean, "love", 0) from _call_change_Girl_stat_63

            $ Jean.History.update("Player_rejected_studying")

    return

init python:

    def Jean_chatting_training():
        label = "Jean_chatting_training"

        conditions = [
            "Jean.History.check('trained_with_Player')",
            "not Jean.History.check('trained_with_Player', tracker = 'weekly')",
            "time_index < 3",
            "Player.location == Jean.location and Player.location == 'bg_danger'",
            "not Jean.History.check('said_no_to_training', tracker = 'recent')",
            "not Jean.History.check('Player_rejected_studying', tracker = 'daily') and not Jean.History.check('Player_rejected_training', tracker = 'daily')",
            "not EventScheduler.Events['Jean_chatting_training'].completed or day - EventScheduler.Events['Jean_chatting_training'].completed >= 5",
            "not EventScheduler.Events['Jean_texting_training'].completed or day - EventScheduler.Events['Jean_texting_training'].completed >= 5",
            "not Jean.status['miffed'] and not Jean.status['mad'] and not Jean.status['heartbroken'] and not Jean.wants_alone_time",
            "approval_check(Jean, threshold = 'friendship')",
            "renpy.random.random() > 0.9"]

        waiting = True

        repeatable = True

        return EventClass(label, conditions, waiting = waiting, repeatable = repeatable)

label Jean_chatting_training:
    ch_Jean "We should probably train, right?"

    menu:
        extend ""
        "Not right now, sorry.":
            $ Jean.change_face("confused1")

            ch_Jean "Okay, I guess I can practice something else."

            $ Jean.History.update("Player_rejected_training")
        "Yeah, sounds good.":
            $ Jean.change_face("pleased2")

            ch_Jean "Cool!"

            call actually_train(Jean) from _call_actually_train
        "Trying to show off again? No thanks.":
            $ Jean.change_face("angry1")

            ch_Jean "What the hell?"
            ch_Jean "Ass. . ."

            call change_Girl_stat(Jean, "love", 0) from _call_change_Girl_stat_64

            $ Jean.History.update("Player_rejected_training")

    return

init python:

    def Jean_chatting_date():
        label = "Jean_chatting_date"

        conditions = [
            "Jean.location == Player.location",
            "not Player.date_planned",
            "2 not in Jean.schedule.keys() and 3 not in Jean.schedule.keys()",
            "2 not in Player.schedule.keys() and 3 not in Player.schedule.keys()",
            "time_index < 2",
            "not Jean.History.check('said_no_to_date', tracker = 'recent')",
            "not Jean.History.check('Player_rejected_studying', tracker = 'daily') and not Jean.History.check('Player_rejected_training', tracker = 'daily') and not Jean.History.check('Player_rejected_date', tracker = 'weekly')",
            "EventScheduler.Events['Jean_first_date'].completed and day - EventScheduler.Events['Jean_first_date'].completed >= 5",
            "not EventScheduler.Events['Jean_date'].completed or day - EventScheduler.Events['Jean_date'].completed >= 5",
            "not EventScheduler.Events['Jean_chatting_date'].completed or day - EventScheduler.Events['Jean_chatting_date'].completed >= 5",
            "not EventScheduler.Events['Jean_texting_date'].completed or day - EventScheduler.Events['Jean_texting_date'].completed >= 5",
            "not Jean.status['miffed'] and not Jean.status['mad'] and not Jean.status['heartbroken'] and not Jean.wants_alone_time",
            "approval_check(Jean, threshold = 'dating')",
            "renpy.random.random() > 0.9"]

        waiting = True

        repeatable = True

        return EventClass(label, conditions, waiting = waiting, repeatable = repeatable)

label Jean_chatting_date:
    if Jean.status["horny"] or Jean.status["nympho"]:
        $ Jean.change_face("sexy", eyes = "down", blush = 1)

        pause 1.0

        $ Jean.change_face("sexy", blush = 1)

        ch_Jean "I could {i}really{/i} use some time with you tonight. . ."

        $ Jean.change_face("sly", mouth = "lipbite", blush = 1)

        ch_Jean "Let's make a date out of it."
    elif Jean.quirk and renpy.random.random() > 0.5:
        $ Jean.change_face("sexy")

        pause 1.0

        $ Jean.change_face("sly")

        ch_Jean "So, [Jean.Player_petname]. . ."
        ch_Jean "Free up your schedule tonight, we're going on a date."
    else:
        $ Jean.change_face("happy")

        ch_Jean "Hey!"

        $ Jean.change_face("smirk2")

        ch_Jean "I'll be free later."
        ch_Jean "We should totally go on a date tonight."

    menu:
        extend ""
        "Count me in.":
            $ Player.date_planned[Jean] = "Girl_initiated_primary"

            if time_index == 2:
                $ EventScheduler.Events["Jean_date"].start()
        "Not tonight. . . sorry.":
            $ Jean.change_face("confused1", eyes = "squint")

            $ Jean.History.update("Player_rejected_date")

    return