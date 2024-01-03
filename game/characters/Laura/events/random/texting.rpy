init python:

    def Laura_texting_study():
        label = "Laura_texting_study"

        conditions = [
            "renpy.random.random() > 0.9",
            
            "Laura.behavior == 'studying'",

            "not Laura.timed_text_options",

            "not Laura.History.check('said_no_to_study', tracker = 'recent')",
            
            "not Player.History.check('received_invite', tracker = 'daily')",

            "Player.location not in ['hold', Laura.location, Laura.destination]",
            "Player.destination not in [Laura.location, Laura.destination]",
                   
            "Laura.History.check('studied_with_Player') and not Laura.History.check('studied_with_Player', tracker = 'weekly')",

            "time_index < 3 or approval_check(Laura, threshold = 'talk_late')",
            
            "Laura.is_in_normal_mood()",
            "approval_check(Laura, threshold = 'friendship')"]

        repeatable = True
        automatic = True

        return EventClass(label, conditions, repeatable = repeatable, automatic = automatic)

label Laura_texting_study:
    call receive_text(Laura, "[Player.first_name]", buzz = False) from _call_receive_text_267
    call receive_text(Laura, "I'm trying to study", buzz = False) from _call_receive_text_268
    call receive_text(Laura, "It's not working", buzz = False) from _call_receive_text_269
    call receive_text(Laura, "Come over and help", buzz = False) from _call_receive_text_270

    $ Laura.timed_text_options.update({"Laura_texting_study": ["sorry, not right now", "sure, I'll be right over", "I'm not in the mood to just teach you everything right now"]})

    $ Player.History.update("received_invite")

    return

label Laura_texting_study_response:
    $ temp = Laura.timed_text_options["Laura_texting_study"][:]

    $ del Laura.timed_text_options["Laura_texting_study"]

    if Laura.text_history[-1][1] == temp[0]:
        call receive_text(Laura, "Shit") from _call_receive_text_271
        call receive_text(Laura, "Fine") from _call_receive_text_272

        $ Laura.History.update("Player_rejected_studying")
    elif Laura.text_history[-1][1] == temp[1]:
        call receive_text(Laura, "Good") from _call_receive_text_273
        call receive_text(Laura, "I'll be waiting") from _call_receive_text_274
        
        hide screen phone_screen

        call send_Characters(Laura, Laura.home, behavior = "studying") from _call_send_Characters_103
        call set_the_scene(location = Laura.home) from _call_set_the_scene_120

        call actually_study(Laura) from _call_actually_study_7
    elif Laura.text_history[-1][1] == temp[2]:
        call change_Character_stat(Laura, "love", -tiny_stat) from _call_change_Character_stat_351

        call receive_text(Laura, "Goddamnit") from _call_receive_text_275
        call receive_text(Laura, "Now I have to find the redhead") from _call_receive_text_276
        
        $ Laura.History.update("Player_rejected_studying")

    return

init python:

    def Laura_texting_training():
        label = "Laura_texting_training"

        conditions = [
            "renpy.random.random() > 0.9",
            
            "Laura.behavior == 'training'",

            "not Laura.timed_text_options",

            "not Laura.History.check('said_no_to_training', tracker = 'recent')",
            
            "not Player.History.check('received_invite', tracker = 'daily')",

            "Player.location not in ['hold', Laura.location, Laura.destination]",
            "Player.destination not in [Laura.location, Laura.destination]",
            
            "Laura.History.check('trained_with_Player') and not Laura.History.check('trained_with_Player', tracker = 'weekly')",
            
            "time_index < 3",

            "Laura.is_in_normal_mood()",
            "approval_check(Laura, threshold = 'friendship')"]

        repeatable = True
        automatic = True

        return EventClass(label, conditions, repeatable = repeatable, automatic = automatic)

label Laura_texting_training:
    call receive_text(Laura, "Come to the Danger Room", buzz = False) from _call_receive_text_278
    call receive_text(Laura, "You're still weak", buzz = False) from _call_receive_text_279
    call receive_text(Laura, "You need to train with me", buzz = False) from _call_receive_text_280

    $ Laura.timed_text_options.update({"Laura_texting_training": ["maybe some other time, sorry", "you're not wrong. . . I'll be right there", "I'd rather be weak than have you beat the shit out of me"]})

    $ Player.History.update("received_invite")

    return

label Laura_texting_training_response:
    $ temp = Laura.timed_text_options["Laura_texting_training"][:]

    $ del Laura.timed_text_options["Laura_texting_training"]

    if Laura.text_history[-1][1] == temp[0]:
        call receive_text(Laura, "You're getting weaker by the minute") from _call_receive_text_281

        $ Laura.History.update("Player_rejected_training")
    elif Laura.text_history[-1][1] == temp[1]:
        if time_index > 2:
            call change_Character_stat(Laura, "love", -tiny_stat) from _call_change_Character_stat_1605

            call receive_text(Laura, "Too late.") from _call_receive_text_823
        else:
            call receive_text(Laura, "Good") from _call_receive_text_282
            call receive_text(Laura, "Don't think you'll get out of the warmup by taking your time") from _call_receive_text_283
            
            hide screen phone_screen

            call send_Characters(Laura, "bg_danger", behavior = "training") from _call_send_Characters_104
            call set_the_scene(location = "bg_danger") from _call_set_the_scene_121

            call actually_train(Laura) from _call_actually_train_4
    elif Laura.text_history[-1][1] == temp[2]:
        call change_Character_stat(Laura, "love", -tiny_stat) from _call_change_Character_stat_352

        call receive_text(Laura, "Stop being such a goddamn wimp") from _call_receive_text_284
        
        $ Laura.History.update("Player_rejected_training")

    return

init python:

    def Laura_texting_date():
        label = "Laura_texting_date"

        conditions = [
            "renpy.random.random() > 0.9",
            
            "not Player.date_planned",
            "2 not in Laura.schedule.keys() and 3 not in Laura.schedule.keys()",
            "2 not in Player.schedule.keys() and 3 not in Player.schedule.keys()",
            
            "not Laura.timed_text_options",
            
            "not Laura.History.check('said_no_to_date', tracker = 'recent')",
            
            "not Player.History.check('received_invite', tracker = 'daily')",

            "Player.location not in ['hold', Laura.location, Laura.destination]",
            "Player.destination not in [Laura.location, Laura.destination]",
            
            "day - EventScheduler.Events['Laura_first_date'].completed_when >= 5",
            "not EventScheduler.Events['Laura_date'].completed or day - EventScheduler.Events['Laura_date'].completed_when >= 5",
            
            "time_index < 2",

            "Laura.is_in_normal_mood()",
            "approval_check(Laura, threshold = 'dating')"]

        repeatable = True
        automatic = True

        return EventClass(label, conditions, repeatable = repeatable, automatic = automatic)

label Laura_texting_date:
    call receive_text(Laura, "Hey", buzz = False) from _call_receive_text_285
    call receive_text(Laura, "I want to go on another date with you", buzz = False) from _call_receive_text_286
    call receive_text(Laura, "Are you free tonight?", buzz = False) from _call_receive_text_287

    $ Laura.timed_text_options.update({"Laura_texting_date": ["sorry, I have other plans tonight", "I am free, see you tonight", "no, I'm good. . ."]})

    $ Player.History.update("received_invite")

    return

label Laura_texting_date_response:
    $ temp = Laura.timed_text_options["Laura_texting_date"][:]

    $ del Laura.timed_text_options["Laura_texting_date"]

    if Laura.text_history[-1][1] == temp[0]:
        call receive_text(Laura, "Another night") from _call_receive_text_288

        $ Laura.History.update("Player_rejected_date")
    elif Laura.text_history[-1][1] == temp[1]:
        if time_index > 2:            
            call change_Character_stat(Laura, "love", -tiny_stat) from _call_change_Character_stat_1600

            call receive_text(Laura, "Too late.") from _call_receive_text_820
        else:
            call receive_text(Laura, "Good") from _call_receive_text_289

            $ Player.date_planned[Laura] = "Character_initiated_primary"

            if time_index == 2:
                $ EventScheduler.Events["Laura_date"].start()
    elif Laura.text_history[-1][1] == temp[2]:
        call change_Character_stat(Laura, "love", -tiny_stat) from _call_change_Character_stat_354

        call receive_text(Laura, "What?!") from _call_receive_text_290
        
        $ Laura.History.update("Player_rejected_date")

    return