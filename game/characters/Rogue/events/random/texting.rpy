init python:

    def Rogue_texting_study():
        label = "Rogue_texting_study"

        conditions = [
            "renpy.random.random() > 0.9",
            
            "Rogue.behavior == 'studying'",

            "not Rogue.timed_text_options",

            "not Rogue.History.check('said_no_to_study', tracker = 'recent')",
            
            "not Rogue.History.check('Player_rejected_studying', tracker = 'daily') and not Rogue.History.check('Player_rejected_training', tracker = 'daily')",
            
            "not EventScheduler.Events['Rogue_chatting_study'].completed or day - EventScheduler.Events['Rogue_chatting_study'].completed_when >= 5",
            "not EventScheduler.Events['Rogue_texting_study'].completed or day - EventScheduler.Events['Rogue_texting_study'].completed_when >= 5",
                 
            "Player.location not in ['hold', Rogue.location, Rogue.destination]",
            "Player.destination not in [Rogue.location, Rogue.destination]",
                   
            "Rogue.History.check('studied_with_Player') and not Rogue.History.check('studied_with_Player', tracker = 'weekly')",

            "time_index < 3 or approval_check(Rogue, threshold = 'talk_late')",
            
            "Rogue.is_in_normal_mood()",
            "approval_check(Rogue, threshold = 'friendship')"]

        repeatable = True
        automatic = True

        return EventClass(label, conditions, repeatable = repeatable, automatic = automatic)

label Rogue_texting_study:
    call receive_text(Rogue, "Heyy", buzz = False) from _call_receive_text_455
    call receive_text(Rogue, "Was bout to study", buzz = False) from _call_receive_text_456
    call receive_text(Rogue, "Wonderin if you might wanna come over and join me?", buzz = False) from _call_receive_text_457

    $ Rogue.timed_text_options.update({"Rogue_texting_study": ["sorry, not right now", "sure, I'll be right over", "why the hell would I want to study?"]})

    return

label Rogue_texting_study_response:
    $ temp = Rogue.timed_text_options["Rogue_texting_study"][:]

    $ del Rogue.timed_text_options["Rogue_texting_study"]

    if Rogue.text_history[-1][1] == temp[0]:
        call receive_text(Rogue, "Don't worry none") from _call_receive_text_458

        $ Rogue.History.update("Player_rejected_studying")
    elif Rogue.text_history[-1][1] == temp[1]:
        call receive_text(Rogue, "Great :)))") from _call_receive_text_459
        call receive_text(Rogue, "Ill be waitin for ya") from _call_receive_text_460
        
        hide screen phone_screen

        call send_Characters(Rogue, Rogue.home, behavior = "studying") from _call_send_Characters_159
        call set_the_scene(location = Rogue.location) from _call_set_the_scene_197

        call actually_study(Rogue) from _call_actually_study_10
    elif Rogue.text_history[-1][1] == temp[2]:
        call receive_text(Rogue, "I just thought") from _call_receive_text_461
        call receive_text(Rogue, "Sorry") from _call_receive_text_462
        
        call change_Girl_stat(Rogue, "love", 0) from _call_change_Girl_stat_604

        $ Rogue.History.update("Player_rejected_studying")

    return

init python:

    def Rogue_texting_training():
        label = "Rogue_texting_training"

        conditions = [
            "renpy.random.random() > 0.9",
            
            "Rogue.behavior == 'training'",

            "not Rogue.timed_text_options",

            "not Rogue.History.check('said_no_to_training', tracker = 'recent')",
            
            "not Rogue.History.check('Player_rejected_studying', tracker = 'daily') and not Rogue.History.check('Player_rejected_training', tracker = 'daily')",
            
            "not EventScheduler.Events['Rogue_chatting_training'].completed or day - EventScheduler.Events['Rogue_chatting_training'].completed_when >= 5",
            "not EventScheduler.Events['Rogue_texting_training'].completed or day - EventScheduler.Events['Rogue_texting_training'].completed_when >= 5",
            
            "Player.location not in ['hold', Rogue.location, Rogue.destination]",
            "Player.destination not in [Rogue.location, Rogue.destination]",
            
            "Rogue.History.check('trained_with_Player') and not Rogue.History.check('trained_with_Player', tracker = 'weekly')",
            
            "time_index < 3",

            "Rogue.is_in_normal_mood()",
            "approval_check(Rogue, threshold = 'friendship')"]

        repeatable = True
        automatic = True

        return EventClass(label, conditions, repeatable = repeatable, automatic = automatic)

label Rogue_texting_training:
    $ temp = Rogue.Player_petname.capitalize()

    call receive_text(Rogue, f"{temp}, ya free?", buzz = False) from _call_receive_text_463
    call receive_text(Rogue, "Im in the Danger Room rn", buzz = False) from _call_receive_text_464
    call receive_text(Rogue, "Thought you might wanna come train with me. . .", buzz = False) from _call_receive_text_465

    $ Rogue.timed_text_options.update({"Rogue_texting_training": ["maybe some other time, sorry", "count me in", "train? with you? nah"]})

    return

label Rogue_texting_training_response:
    $ temp = Rogue.timed_text_options["Rogue_texting_training"][:]

    $ del Rogue.timed_text_options["Rogue_texting_training"]

    if Rogue.text_history[-1][1] == temp[0]:
        call receive_text(Rogue, "Aint no thing, sugar") from _call_receive_text_466

        $ Rogue.History.update("Player_rejected_training")
    elif Rogue.text_history[-1][1] == temp[1]:
        if time_index > 2:
            call receive_text(Rogue, "Too late. . .") from _call_receive_text_824
            
            call change_Girl_stat(Rogue, "love", 0) from _call_change_Girl_stat_1606
        else:
            call send_text(Rogue, "I'll be right there") from _call_send_text_34
            call receive_text(Rogue, "Sweet") from _call_receive_text_467
            call receive_text(Rogue, "I'll wait for ya to show before stretchin :)))") from _call_receive_text_468
            
            hide screen phone_screen

            call send_Characters(Rogue, "bg_danger", behavior = "training") from _call_send_Characters_160
            call set_the_scene(location = "bg_danger") from _call_set_the_scene_198

            call actually_train(Rogue) from _call_actually_train_7
    elif Rogue.text_history[-1][1] == temp[2]:
        call receive_text(Rogue, "Oh") from _call_receive_text_469
        call receive_text(Rogue, "Okay") from _call_receive_text_470
        call receive_text(Rogue, "Sorry") from _call_receive_text_471
        
        call change_Girl_stat(Rogue, "love", 0) from _call_change_Girl_stat_605

        $ Rogue.History.update("Player_rejected_training")

    return

init python:

    def Rogue_texting_date():
        label = "Rogue_texting_date"

        conditions = [
            "renpy.random.random() > 0.9",
            
            "not Player.date_planned",
            "2 not in Rogue.schedule.keys() and 3 not in Rogue.schedule.keys()",
            "2 not in Player.schedule.keys() and 3 not in Player.schedule.keys()",
            
            "not Rogue.timed_text_options",
            
            "not Rogue.History.check('said_no_to_date', tracker = 'recent')",
            
            "not Rogue.History.check('Player_rejected_studying', tracker = 'daily') and not Rogue.History.check('Player_rejected_training', tracker = 'daily') and not Rogue.History.check('Player_rejected_date', tracker = 'weekly')",
            
            "not EventScheduler.Events['Rogue_chatting_date'].completed or day - EventScheduler.Events['Rogue_chatting_date'].completed_when >= 5",
            "not EventScheduler.Events['Rogue_texting_date'].completed or day - EventScheduler.Events['Rogue_texting_date'].completed_when >= 5",
            
            "Player.location not in ['hold', Rogue.location, Rogue.destination]",
            "Player.destination not in [Rogue.location, Rogue.destination]",
            
            "day - EventScheduler.Events['Rogue_first_date'].completed_when >= 5",
            "not EventScheduler.Events['Rogue_date'].completed or day - EventScheduler.Events['Rogue_date'].completed_when >= 5",
            
            "time_index < 2",

            "Rogue.is_in_normal_mood()",
            "approval_check(Rogue, threshold = 'dating')"]

        repeatable = True
        automatic = True

        return EventClass(label, conditions, repeatable = repeatable, automatic = automatic)

label Rogue_texting_date:
    call receive_text(Rogue, "Hey! :)))", buzz = False) from _call_receive_text_472
    call receive_text(Rogue, "Im free tonight and was wonderin", buzz = False) from _call_receive_text_473
    call receive_text(Rogue, "Maybe you wanna go on a date?", buzz = False) from _call_receive_text_474

    $ Rogue.timed_text_options.update({"Rogue_texting_date": ["sorry, not tonight", "I'd like that! I'll see you tonight", "yeah, no. I'm good"]})

    return

label Rogue_texting_date_response:
    $ temp = Rogue.timed_text_options["Rogue_texting_date"][:]

    $ del Rogue.timed_text_options["Rogue_texting_date"]

    if Rogue.text_history[-1][1] == temp[0]:
        call receive_text(Rogue, "Its alright, maybe some other time") from _call_receive_text_475
    elif Rogue.text_history[-1][1] == temp[1]:
        if time_index > 2:
            call receive_text(Rogue, "It's a little too late for that. . .") from _call_receive_text_821
            
            call change_Girl_stat(Rogue, "love", 0) from _call_change_Girl_stat_1601
        else:
            call receive_text(Rogue, "Can't wait :)))") from _call_receive_text_476

            call change_Girl_stat(Rogue, "love", 0) from _call_change_Girl_stat_606

            $ Player.date_planned[Rogue] = "Girl_initiated_primary"

            if time_index == 2:
                $ EventScheduler.Events["Rogue_date"].start()
    elif Rogue.text_history[-1][1] == temp[2]:
        call receive_text(Rogue, "Sorry. . .") from _call_receive_text_477
        
        call change_Girl_stat(Rogue, "love", 0) from _call_change_Girl_stat_607

    return

init python:

    def Rogue_texting_ask_to_masturbate():
        label = "Rogue_texting_ask_to_masturbate"

        conditions = [
            "renpy.random.random() > 0.9",

            "Rogue.quirk",

            "Rogue.behavior == 'masturbating'",

            "not Rogue.timed_text_options",

            "Player.location not in ['hold', Rogue.location, Rogue.destination]",
            "Player.destination not in [Rogue.location, Rogue.destination]",
                        
            "Rogue.History.check('self_touch_pussy')",

            "Rogue.is_in_normal_mood()",   
            "Rogue.status['horny'] or Rogue.status['nympho']"]

        repeatable = True
        automatic = True

        return EventClass(label, conditions, repeatable = repeatable, automatic = automatic)

label Rogue_texting_ask_to_masturbate:
    $ temp = Rogue.Player_petname.capitalize()

    call receive_text(Rogue, f"{temp}", buzz = False) from _call_receive_text_478
    call receive_text(Rogue, "Im. . .", buzz = False) from _call_receive_text_479
    call receive_text(Rogue, "All pent up", buzz = False) from _call_receive_text_480
    call receive_text(Rogue, "Am I allowed to", buzz = False) from _call_receive_text_481
    call receive_text(Rogue, "Touch myself?", buzz = False) from _call_receive_text_482

    $ Rogue.timed_text_options.update({"Rogue_texting_ask_to_masturbate": ["not allowed. maybe I'll come take care of you later", "yes, you're allowed. but only if you say please", "you're not allowed, because I'm about to head over and take care of you myself"]})

    $ Rogue.behavior = None

    return

label Rogue_texting_ask_to_masturbate_response:
    $ temp = Rogue.timed_text_options["Rogue_texting_ask_to_masturbate"][:]

    $ del Rogue.timed_text_options["Rogue_texting_ask_to_masturbate"]

    if Rogue.text_history[-1][1] == temp[0]:
        call receive_text(Rogue, "Alright, [Rogue.Player_petname]") from _call_receive_text_483
        call receive_text(Rogue, "Please don't make me wait too long") from _call_receive_text_484

        call change_Girl_stat(Rogue, "desire", 0) from _call_change_Girl_stat_608
    elif Rogue.text_history[-1][1] == temp[1]:
        call receive_text(Rogue, "Please, [Rogue.Player_petname]") from _call_receive_text_485
        call send_text(Rogue, "good, go ahead") from _call_send_text_35
        
        call change_Girl_stat(Rogue, "love", 0) from _call_change_Girl_stat_609
            
        if Rogue.location in [Rogue.home, Player.home]:
            $ Rogue.behavior = "masturbating"
    elif Rogue.text_history[-1][1] == temp[2]:
        call receive_text(Rogue, "Lord, please do") from _call_receive_text_486
        
        hide screen phone_screen

        call remove_everyone_but(Rogue, location = Rogue.location, fade = False) from _call_remove_everyone_but_12
        call set_the_scene(location = Rogue.location) from _call_set_the_scene_199

        $ Rogue.change_face("manic", blush = 2)

        call change_Girl_stat(Rogue, "desire", 0) from _call_change_Girl_stat_610

        $ Rogue.History.update("hookup")
            
        call screen Action_screen(automatic = True)
        
        $ choice_disabled = False
        
    return