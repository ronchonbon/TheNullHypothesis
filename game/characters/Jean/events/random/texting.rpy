init python:

    def Jean_texting_study():
        label = "Jean_texting_study"

        conditions = [
            "renpy.random.random() > 0.9",
            
            "Jean.behavior == 'studying'",

            "not Jean.timed_text_options",

            "not Jean.History.check('said_no_to_study', tracker = 'recent')",
            
            "not Jean.History.check('Player_rejected_studying', tracker = 'daily') and not Jean.History.check('Player_rejected_training', tracker = 'daily')",
            
            "not EventScheduler.Events['Jean_chatting_study'].completed or day - EventScheduler.Events['Jean_chatting_study'].completed_when >= 5",
            "not EventScheduler.Events['Jean_texting_study'].completed or day - EventScheduler.Events['Jean_texting_study'].completed_when >= 5",
                 
            "Player.location not in ['hold', Jean.location, Jean.destination]",
            "Player.destination not in [Jean.location, Jean.destination]",
                   
            "Jean.History.check('studied_with_Player') and not Jean.History.check('studied_with_Player', tracker = 'weekly')",

            "time_index < 3 or approval_check(Jean, threshold = 'talk_late')",
            
            "Jean.is_in_normal_mood()",
            "approval_check(Jean, threshold = 'friendship')"]

        repeatable = True
        automatic = True

        return EventClass(label, conditions, repeatable = repeatable, automatic = automatic)

label Jean_texting_study:
    call receive_text(Jean, "You busy right now?", buzz = False) from _call_receive_text_2
    call receive_text(Jean, "Gonna be studying in my room", buzz = False) from _call_receive_text_3
    call receive_text(Jean, "You should come over and join me <3", buzz = False) from _call_receive_text_4

    $ Jean.timed_text_options.update({"Jean_texting_study": ["sorry, not right now", "count me in", "yeah, I'm good. studying sucks"]})

    return

label Jean_texting_study_response:
    $ temp = Jean.timed_text_options["Jean_texting_study"][:]

    $ del Jean.timed_text_options["Jean_texting_study"]

    if Jean.text_history[-1][1] == temp[0]:
        call receive_text(Jean, "Ugh, fine") from _call_receive_text_5

        $ Jean.History.update("Player_rejected_studying")
    elif Jean.text_history[-1][1] == temp[1]:
        call send_text(Jean, "be right over") from _call_send_text_1
        call receive_text(Jean, "Awesome") from _call_receive_text_6
        call receive_text(Jean, "Just don't make me wait too long <3") from _call_receive_text_7
        
        hide screen phone_screen

        call send_Characters(Jean, Jean.home, behavior = "studying") from _call_send_Characters_45
        call set_the_scene(location = Jean.location) from _call_set_the_scene_39

        call actually_study(Jean) from _call_actually_study_1
    elif Jean.text_history[-1][1] == temp[2]:
        call receive_text(Jean, "It does not") from _call_receive_text_8
        call receive_text(Jean, "Whatever, your loss") from _call_receive_text_9
        
        call change_Character_stat(Jean, "love", 0) from _call_change_Character_stat_71

        $ Jean.History.update("Player_rejected_studying")

    return

init python:

    def Jean_texting_training():
        label = "Jean_texting_training"

        conditions = [
            "renpy.random.random() > 0.9",
            
            "Jean.behavior == 'training'",

            "not Jean.timed_text_options",

            "not Jean.History.check('said_no_to_training', tracker = 'recent')",
            
            "not Jean.History.check('Player_rejected_studying', tracker = 'daily') and not Jean.History.check('Player_rejected_training', tracker = 'daily')",
            
            "not EventScheduler.Events['Jean_chatting_training'].completed or day - EventScheduler.Events['Jean_chatting_training'].completed_when >= 5",
            "not EventScheduler.Events['Jean_texting_training'].completed or day - EventScheduler.Events['Jean_texting_training'].completed_when >= 5",
            
            "Player.location not in ['hold', Jean.location, Jean.destination]",
            "Player.destination not in [Jean.location, Jean.destination]",
            
            "Jean.History.check('trained_with_Player') and not Jean.History.check('trained_with_Player', tracker = 'weekly')",
            
            "time_index < 3",

            "Jean.is_in_normal_mood()",
            "approval_check(Jean, threshold = 'friendship')"]

        repeatable = True
        automatic = True

        return EventClass(label, conditions, repeatable = repeatable, automatic = automatic)

label Jean_texting_training:
    $ temp = Jean.Player_petname.capitalize()

    call receive_text(Jean, f"{temp}, I wanna train with my powers", buzz = False) from _call_receive_text_10
    call receive_text(Jean, "You know I can't do it without you <3", buzz = False) from _call_receive_text_11
    call receive_text(Jean, "Come on over", buzz = False) from _call_receive_text_12

    $ Jean.timed_text_options.update({"Jean_texting_training": ["I'm a bit busy, sorry", "sure, I'll be right there", "you just want an excuse to show off. I'm good"]})

    return

label Jean_texting_training_response:
    $ temp = Jean.timed_text_options["Jean_texting_training"][:]

    $ del Jean.timed_text_options["Jean_texting_training"]

    if Jean.text_history[-1][1] == temp[0]:
        call receive_text(Jean, "Ugh") from _call_receive_text_13
        call receive_text(Jean, "I guess I can practice other stuff. . . </3") from _call_receive_text_14

        $ Jean.History.update("Player_rejected_training")
    elif Jean.text_history[-1][1] == temp[1]:
        if time_index > 2:
            call receive_text(Jean, "Too late!") from _call_receive_text_822

            call change_Character_stat(Jean, "love", 0) from _call_change_Character_stat_1604
        else:
            call receive_text(Jean, "Awesome") from _call_receive_text_15
            call receive_text(Jean, "I'll wait for you before warming up <3") from _call_receive_text_16
            
            hide screen phone_screen

            call send_Characters(Jean, "bg_danger", behavior = "training") from _call_send_Characters_46
            call set_the_scene(location = "bg_danger") from _call_set_the_scene_40

            call actually_train(Jean) from _call_actually_train_1
    elif Jean.text_history[-1][1] == temp[2]:
        call receive_text(Jean, "The hell?") from _call_receive_text_17
        call receive_text(Jean, "Why are you such an ass today?") from _call_receive_text_18
        call receive_text(Jean, "Whatever, I'll just practice something else") from _call_receive_text_19
        
        call change_Character_stat(Jean, "love", 0) from _call_change_Character_stat_72

        $ Jean.History.update("Player_rejected_training")

    return

init python:

    def Jean_texting_date():
        label = "Jean_texting_date"

        conditions = [
            "renpy.random.random() > 0.9",
            
            "not Player.date_planned",
            "2 not in Jean.schedule.keys() and 3 not in Jean.schedule.keys()",
            "2 not in Player.schedule.keys() and 3 not in Player.schedule.keys()",
            
            "not Jean.timed_text_options",
            
            "not Jean.History.check('said_no_to_date', tracker = 'recent')",
            
            "not Jean.History.check('Player_rejected_studying', tracker = 'daily') and not Jean.History.check('Player_rejected_training', tracker = 'daily') and not Jean.History.check('Player_rejected_date', tracker = 'weekly')",
            
            "not EventScheduler.Events['Jean_chatting_date'].completed or day - EventScheduler.Events['Jean_chatting_date'].completed_when >= 5",
            "not EventScheduler.Events['Jean_texting_date'].completed or day - EventScheduler.Events['Jean_texting_date'].completed_when >= 5",
            
            "Player.location not in ['hold', Jean.location, Jean.destination]",
            "Player.destination not in [Jean.location, Jean.destination]",
            
            "day - EventScheduler.Events['Jean_first_date'].completed_when >= 5",
            "not EventScheduler.Events['Jean_date'].completed or day - EventScheduler.Events['Jean_date'].completed_when >= 5",
            
            "time_index < 2",

            "Jean.is_in_normal_mood()",
            "approval_check(Jean, threshold = 'dating')"]

        repeatable = True
        automatic = True

        return EventClass(label, conditions, repeatable = repeatable, automatic = automatic)

label Jean_texting_date:
    $ temp = Jean.Player_petname.capitalize()

    call receive_text(Jean, f"{temp}!", buzz = False) from _call_receive_text_20
    call receive_text(Jean, "I finally have some free time tonight", buzz = False) from _call_receive_text_21
    call receive_text(Jean, "I wanna take you out on a date <3", buzz = False) from _call_receive_text_22

    $ Jean.timed_text_options.update({"Jean_texting_date": ["sorry, I'm busy tonight", "sounds great! see you tonight", "I'd rather not"]})

    return

label Jean_texting_date_response:
    $ temp = Jean.timed_text_options["Jean_texting_date"][:]

    $ del Jean.timed_text_options["Jean_texting_date"]

    if Jean.text_history[-1][1] == temp[0]:
        call receive_text(Jean, "Ugh") from _call_receive_text_23
        call receive_text(Jean, "Fine") from _call_receive_text_24
        call receive_text(Jean, "Some other night") from _call_receive_text_25

        $ Jean.History.update("Player_rejected_date")
    elif Jean.text_history[-1][1] == temp[1]:
        if time_index > 2:
            call receive_text(Jean, "Well, it's too late now. . .") from _call_receive_text_329

            call change_Character_stat(Jean, "love", 0) from _call_change_Character_stat_1599
        else:
            call receive_text(Jean, "Perfect") from _call_receive_text_26
            call receive_text(Jean, "See you later! <3") from _call_receive_text_27

            call change_Character_stat(Jean, "love", 0) from _call_change_Character_stat_73

            $ Player.date_planned[Jean] = "Character_initiated_primary"

            if time_index == 2:
                $ EventScheduler.Events["Jean_date"].start()
    elif Jean.text_history[-1][1] == temp[2]:
        call receive_text(Jean, "What? Why???") from _call_receive_text_28
        call receive_text(Jean, "Whatever, some other night") from _call_receive_text_29
        
        call change_Character_stat(Jean, "love", 0) from _call_change_Character_stat_74

        $ Jean.History.update("Player_rejected_date")

    return

init python:

    def Jean_texting_summon_horny():
        label = "Jean_texting_summon_horny"

        conditions = [
            "renpy.random.random() > 0.9",

            "Jean.check_traits('quirk')",

            "not Jean.timed_text_options",
            
            "not Jean.History.check('rejected_knock_on_door', tracker = 'recent')",
            
            "Jean.location in [Jean.home, Player.home]",

            "Player.location not in ['hold', Jean.location, Jean.destination]",
            "Player.destination not in [Jean.location, Jean.destination]",

            "Jean.History.check('hookup')",
            
            "Jean.is_in_normal_mood()",           
            "Jean.status['horny'] or Jean.status['nympho']"]

        repeatable = True
        automatic = True

        return EventClass(label, conditions, repeatable = repeatable, automatic = automatic)

label Jean_texting_summon_horny:
    $ temp = Jean.Player_petname.capitalize()

    call receive_text(Jean, f"{temp}", buzz = False) from _call_receive_text_30    
    call receive_text(Jean, "Your big sister needs you", buzz = False) from _call_receive_text_31
    call receive_text(Jean, "Im bored", buzz = False) from _call_receive_text_32
    call receive_text(Jean, "And. . . wet", buzz = False) from _call_receive_text_33
    call receive_text(Jean, "I wanna play with you", buzz = False) from _call_receive_text_34
    call receive_text(Jean, "Come over <3", buzz = False) from _call_receive_text_35

    $ Jean.timed_text_options.update({"Jean_texting_summon_horny": ["I'm sorry, I can't. too busy right now", "I'll be there as fast as I can", "you can't just deal with that yourself? I'm busy"]})

    return

label Jean_texting_summon_horny_response:
    $ temp = Jean.timed_text_options["Jean_texting_summon_horny"][:]

    $ del Jean.timed_text_options["Jean_texting_summon_horny"]
    
    if Jean.text_history[-1][1] == temp[0]:
        call receive_text(Jean, "Ugh, no fun") from _call_receive_text_36
        call receive_text(Jean, "Fine, then I'll just play with myself") from _call_receive_text_37
        call receive_text(Jean, "And you're not allowed to watch ;P") from _call_receive_text_38

        call change_Character_stat(Jean, "desire", 0) from _call_change_Character_stat_75
    elif Jean.text_history[-1][1] == temp[1]:
        call receive_text(Jean, "Good") from _call_receive_text_39
        call receive_text(Jean, "I can't wait <3") from _call_receive_text_40
        
        call change_Character_stat(Jean, "love", 0) from _call_change_Character_stat_76
        
        hide screen phone_screen

        call remove_everyone_but(Jean, location = Jean.location, fade = False) from _call_remove_everyone_but_9
        call set_the_scene(location = Jean.location) from _call_set_the_scene_41

        $ Jean.change_face("sexy", blush = 2)
        
        $ choice_disabled = False
    elif Jean.text_history[-1][1] == temp[2]:
        call receive_text(Jean, "Ugh, don't have to be an ass about it") from _call_receive_text_41
        call receive_text(Jean, "Whatever, fine") from _call_receive_text_42

        call change_Character_stat(Jean, "love", 0) from _call_change_Character_stat_77

    return