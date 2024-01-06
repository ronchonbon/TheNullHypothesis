label Laura_texting(message):
    python:
        for E in Laura.timed_text_options.keys():
            for text in Laura.timed_text_options[E]:
                if message == text:
                    renpy.call(f"{E}_response")

    if Laura.timed_text_options:
        call Laura_text_ignored from _call_Laura_text_ignored

        $ Laura.timed_text_options = {}

    if message == "how are you?":
        $ selected_Event = EventScheduler.choose_Event(texting = True)

        if selected_Event:
            call start_Event(selected_Event) from _call_start_Event_3
        else:
            if time_index == 3:
                if approval_check(Laura, threshold = "talk_late"):
                    call Laura_text_how_are_you_late_accept from _call_Laura_text_how_are_you_late_accept
                else:
                    if approval_check(Laura, threshold = "friendship"):
                        call Laura_text_how_are_you_late_reject from _call_Laura_text_how_are_you_late_reject
                    else:
                        if Laura.History.check("said_too_late_to_text", tracker = "recent") == 1:
                            call Laura_text_how_are_you_late_reject_asked_once from _call_Laura_text_how_are_you_late_reject_asked_once
                        elif Laura.History.check("said_too_late_to_text", tracker = "recent") > 1:
                            call Laura_text_how_are_you_late_reject_asked_twice from _call_Laura_text_how_are_you_late_reject_asked_twice
                        else:
                            call Laura_text_how_are_you_late_reject from _call_Laura_text_how_are_you_late_reject_1

                    $ Laura.History.update("said_too_late_to_text")
            else:
                $ status = Laura.get_status()

                if status not in ["heartbroken", "mad"]:
                    call change_Character_stat(Laura, "love", tiny_stat) from _call_change_Character_stat_39

                if status:
                    call expression f"Laura_text_how_are_you_{status}" from _call_expression_21
                elif approval_check(Laura, threshold = "love"):
                    call Laura_text_how_are_you_love from _call_Laura_text_how_are_you_love
                elif Laura in Partners:
                    call Laura_text_how_are_you_relationship from _call_Laura_text_how_are_you_relationship
                else:
                    call Laura_text_how_are_you from _call_Laura_text_how_are_you

        $ Laura.History.update("sent_how_are_you_text")

    if "good morning" in message:
        $ status = Laura.get_status()

        if status not in ["heartbroken", "mad"]:
            call change_Character_stat(Laura, "love", tiny_stat) from _call_change_Character_stat_40

        if status:
            call expression f"Laura_text_good_morning_{status}" from _call_expression_22
        elif approval_check(Laura, threshold = "love"):
            call Laura_text_good_morning_love from _call_Laura_text_good_morning_love
        elif Laura in Partners:
            call Laura_text_good_morning_relationship from _call_Laura_text_good_morning_relationship
        else:
            call Laura_text_good_morning from _call_Laura_text_good_morning

        $ Laura.History.update("sent_good_morning_text")

    if "goodnight" in message:
        $ status = Laura.get_status()

        if status not in ["heartbroken", "mad"]:
            call change_Character_stat(Laura, "love", tiny_stat) from _call_change_Character_stat_41

        if status:
            call expression f"Laura_text_goodnight_{status}" from _call_expression_23
        elif approval_check(Laura, threshold = "love"):
            call Laura_text_goodnight_love from _call_Laura_text_goodnight_love
        elif Laura in Partners:
            call Laura_text_goodnight_relationship from _call_Laura_text_goodnight_relationship
        else:
            call Laura_text_goodnight from _call_Laura_text_goodnight

        $ Laura.History.update("said_goodnight")

    if message == "wanna come over?":
        call summon(Laura) from _call_summon_1

    if message in ["want to go on a date tonight?", "ready for that date?"]:
        call Laura_text_ask_on_date from _call_Laura_text_ask_on_date

    return

label Laura_text_how_are_you:
    $ dice_roll = renpy.random.randint(1, 3)
    
    if dice_roll == 1:
        call receive_text(Laura, "I'm fine") from _call_receive_text_319
        call receive_text(Laura, "Thanks") from _call_receive_text_320
    elif dice_roll == 2:
        call receive_text(Laura, "Good. . .") from _call_receive_text_1073
    elif dice_roll == 2:
        call receive_text(Laura, "Everything is fine") from _call_receive_text_1074
        call receive_text(Laura, "Why?") from _call_receive_text_1075

    return

label Laura_text_how_are_you_late_accept:
    $ dice_roll = renpy.random.randint(1, 3)
    
    if dice_roll == 1:
        call receive_text(Laura, "I'm") from _call_receive_text_321
        call receive_text(Laura, "Okay") from _call_receive_text_322
        call receive_text(Laura, "Done training for the night, so") from _call_receive_text_323
        call receive_text(Laura, "I don't have to go to bed yet") from _call_receive_text_324
        call receive_text(Laura, "If you wanted to hang out") from _call_receive_text_325
    elif dice_roll == 2:
        call receive_text(Laura, "Fine, can't sleep") from _call_receive_text_1076
        call receive_text(Laura, "We can talk if you want") from _call_receive_text_1077
    elif dice_roll == 3:
        call receive_text(Laura, "Tired") from _call_receive_text_1078
        call receive_text(Laura, "But") from _call_receive_text_1079
        call receive_text(Laura, "Wouldn't mind talking some more") from _call_receive_text_1080

    return

label Laura_text_how_are_you_late_reject:
    $ dice_roll = renpy.random.randint(1, 3)
    
    if dice_roll == 1:
        call receive_text(Laura, "Fine") from _call_receive_text_326
        call receive_text(Laura, "Done training") from _call_receive_text_327
        call receive_text(Laura, "Going to bed") from _call_receive_text_328
    elif dice_roll == 2:
        call receive_text(Laura, "Sleeping") from _call_receive_text_1081
    elif dice_roll == 2:
        call receive_text(Laura, "It's late") from _call_receive_text_1082

    return

label Laura_text_how_are_you_late_reject_asked_once:
    call Laura_asked_once_text("late") from _call_Laura_asked_once_text_2

    return

label Laura_text_how_are_you_late_reject_asked_twice:
    call Laura_asked_once_text("late") from _call_Laura_asked_once_text_3
    
    return

label Laura_text_how_are_you_relationship:
    $ dice_roll = renpy.random.randint(1, 3)
    
    if dice_roll == 1:
        call receive_text(Laura, "I'm fine") from _call_receive_text_333
        call receive_text(Laura, "Bored") from _call_receive_text_334
        call receive_text(Laura, "Want to hang out with you") from _call_receive_text_335
    elif dice_roll == 2:
        call receive_text(Laura, "Fine") from _call_receive_text_1083
        call receive_text(Laura, "When are we spending more time together?") from _call_receive_text_1084
    elif dice_roll == 3:
        call receive_text(Laura, "Meh") from _call_receive_text_1085
        call receive_text(Laura, "Fine") from _call_receive_text_1086
        call receive_text(Laura, "Better if you were here") from _call_receive_text_1087

    return

label Laura_text_how_are_you_love:
    $ dice_roll = renpy.random.randint(1, 3)
    
    if dice_roll == 1:
        call receive_text(Laura, "I am good") from _call_receive_text_1088
        call receive_text(Laura, "I can't stop thinking about you") from _call_receive_text_1089
        call receive_text(Laura, "But I am good") from _call_receive_text_1090
    elif dice_roll == 2:
        call receive_text(Laura, "I'm fine") from _call_receive_text_1091
        call receive_text(Laura, f"I hope you are doing well {Laura.Player_petname}") from _call_receive_text_1092
    elif dice_roll == 3:
        call receive_text(Laura, "I'm fine") from _call_receive_text_336
        call receive_text(Laura, "I love you and") from _call_receive_text_337
        call receive_text(Laura, "I think") from _call_receive_text_338
        call receive_text(Laura, "I miss you") from _call_receive_text_339

        $ Laura.mandatory_text_options = ["you just saw me earlier, but I miss you too", "I know it's not easy for you. I love and miss you too", "you need to chill, we literally just saw each other"]
        $ temp = Laura.mandatory_text_options[:]

        while Laura.mandatory_text_options:
            pause

        if Laura.text_history[-1][1] == temp[0]:
            call receive_text(Laura, "It's hard") from _call_receive_text_340
            call receive_text(Laura, "Whenever I don't have my eyes on you") from _call_receive_text_341
        elif Laura.text_history[-1][1] == temp[1]:
            call change_Character_stat(Laura, "love", tiny_stat) from _call_change_Character_stat_506

            call receive_text(Laura, "Thank you") from _call_receive_text_342
            call receive_text(Laura, "But stop making me worry so much") from _call_receive_text_343
        elif Laura.text_history[-1][1] == temp[2]:
            call change_Character_stat(Laura, "love", -tiny_stat) from _call_change_Character_stat_507

            call receive_text(Laura, "Asshole") from _call_receive_text_344

    return

label Laura_text_how_are_you_mad:
    $ dice_roll = renpy.random.randint(1, 3)
    
    if dice_roll == 1:
        call receive_text(Laura, "I'm pissed") from _call_receive_text_345
        call receive_text(Laura, "I need to cut something") from _call_receive_text_346
    elif dice_roll == 2:
        call receive_text(Laura, "How do you think") from _call_receive_text_1093
    elif dice_roll == 3:
        call receive_text(Laura, "I am bad") from _call_receive_text_1094

    return

label Laura_text_how_are_you_hearbroken:
    $ dice_roll = renpy.random.randint(1, 3)
    
    if dice_roll == 1:
        call receive_text(Laura, "Not okay") from _call_receive_text_347
        call receive_text(Laura, "I don't know why I feel like this") from _call_receive_text_348
    elif dice_roll == 2:
        pass
    elif dice_roll == 3:
        call receive_text(Laura, "I don't want to talk about it") from _call_receive_text_1095

    return

label Laura_text_how_are_you_horny:
    $ dice_roll = renpy.random.randint(1, 3)
    
    if dice_roll == 1:
        call receive_text(Laura, "I'm fine") from _call_receive_text_349

        if approval_check(Laura, threshold = "hookup"):
            call receive_text(Laura, "Woudl be better if I could see you") from _call_receive_text_350
    elif dice_roll == 2:
        call receive_text(Laura, "Good") from _call_receive_text_1096
        call receive_text(Laura, "Are we seeing each other today?") from _call_receive_text_1097
    elif dice_roll == 3:
        call receive_text(Laura, "Good") from _call_receive_text_1098
        call receive_text(Laura, "I feel very warm") from _call_receive_text_1099

    return

label Laura_text_how_are_you_nympho:
    if approval_check(Laura, threshold = "hookup"):
        $ dice_roll = renpy.random.randint(1, 3)
    else:
        $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        call receive_text(Laura, "I don't know") from _call_receive_text_1100
        call receive_text(Laura, "I feel. . . strange") from _call_receive_text_1101
    elif dice_roll == 2:
        call receive_text(Laura, "I'm. . . fine") from _call_receive_text_1102
        call receive_text(Laura, "It is very hot in the mansion today") from _call_receive_text_1103
    elif dice_roll == 3:
        call receive_text(Laura, "Unsatisfied") from _call_receive_text_351
        call receive_text(Laura, "You are coming over some time soon") from _call_receive_text_352
        call receive_text(Laura, "Very soon") from _call_receive_text_353

    return

label Laura_text_good_morning:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        call receive_text(Laura, "Is it?") from _call_receive_text_354
        call receive_text(Laura, "Why do you say that?") from _call_receive_text_355
        call send_text(Laura, "just trying to be nice. . .") from _call_send_text_26
    elif dice_roll == 2:
        call receive_text(Laura, "Good morning") from _call_receive_text_356
    elif dice_roll == 3:
        call receive_text(Laura, "We'll see") from _call_receive_text_357
        call receive_text(Laura, "I've had worse nights of sleep") from _call_receive_text_358

    return

label Laura_text_good_morning_relationship:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        call receive_text(Laura, f"Good morning {Laura.Player_petname}") from _call_receive_text_359
        call receive_text(Laura, "I") from _call_receive_text_360
        call receive_text(Laura, "Hope you slept well") from _call_receive_text_361
    elif dice_roll == 2:
        call receive_text(Laura, f"Hello {Laura.Player_petname}") from _call_receive_text_1104
    elif dice_roll == 3:
        call receive_text(Laura, "I suppose it is a good morning") from _call_receive_text_1105

    return

label Laura_text_good_morning_love:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        call receive_text(Laura, "Hey") from _call_receive_text_362
        call receive_text(Laura, "I") from _call_receive_text_363
        call receive_text(Laura, "You were in my dreams last night") from _call_receive_text_364
        call receive_text(Laura, "It was nice for once") from _call_receive_text_365
    elif dice_roll == 2:
        call receive_text(Laura, "Hey") from _call_receive_text_1106
        call receive_text(Laura, "I'm glad you are awake") from _call_receive_text_1107
        call receive_text(Laura, "I missed you") from _call_receive_text_1108
    elif dice_roll == 3:
        call receive_text(Laura, "Morning") from _call_receive_text_366
        call receive_text(Laura, "How did you sleep?") from _call_receive_text_367
        call receive_text(Laura, "Did you have any dreams?") from _call_receive_text_368
        call receive_text(Laura, "Are you feeling okay?") from _call_receive_text_369

        $ Laura.mandatory_text_options = ["I slept well, no dreams. I'm feeling fine", "I'm glad you care so much. everything's great", "chill"]
        $ temp = Laura.mandatory_text_options[:]

        while Laura.mandatory_text_options:
            pause

        if Laura.text_history[-1][1] == temp[0]:
            call receive_text(Laura, "Good") from _call_receive_text_370
        elif Laura.text_history[-1][1] == temp[1]:
            call change_Character_stat(Laura, "love", tiny_stat) from _call_change_Character_stat_513

            call send_text(Laura, "don't worry :)") from _call_send_text_27
            call receive_text(Laura, "Good") from _call_receive_text_371
            call receive_text(Laura, "I'll stop worrying when you stop giving me reasons to") from _call_receive_text_372
        elif Laura.text_history[-1][1] == temp[2]:
            call receive_text(Laura, "So you're fine then?") from _call_receive_text_373

    return

label Laura_text_good_morning_mad:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        call receive_text(Laura, "Not in the mood.") from _call_receive_text_374
    elif dice_roll == 2:
        call receive_text(Laura, "Leave me alone.") from _call_receive_text_1109
    elif dice_roll == 3:
        call receive_text(Laura, "Sure") from _call_receive_text_1110

    return

label Laura_text_good_morning_hearbroken:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        call receive_text(Laura, "No, it's not") from _call_receive_text_375
    elif dice_roll == 2:
        pass
    elif dice_roll == 3:
        call receive_text(Laura, ". . .") from _call_receive_text_1111

    return

label Laura_text_good_morning_horny:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        call receive_text(Laura, "Hello") from _call_receive_text_1112
        call receive_text(Laura, "We should spend time together today") from _call_receive_text_1113
    elif dice_roll == 2:
        call receive_text(Laura, "Good morning") from _call_receive_text_1114
        call receive_text(Laura, "Let's spend time together today") from _call_receive_text_1115
    elif dice_roll == 3:
        call receive_text(Laura, "Good morning") from _call_receive_text_376
        
        if approval_check(Laura, threshold = "hookup"):
            call receive_text(Laura, "I can't get you out of my head") from _call_receive_text_377
            call receive_text(Laura, "Stop being so. . .") from _call_receive_text_378
            call receive_text(Laura, "Never mind") from _call_receive_text_379

    return

label Laura_text_good_morning_nympho:
    if approval_check(Laura, threshold = "hookup"):
        $ dice_roll = renpy.random.randint(1, 3)
    else:
        $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        call receive_text(Laura, "You're just waking up?") from _call_receive_text_1116
        call send_text(Laura, "uh. . . yeah?") from _call_send_text_7
        call receive_text(Laura, "I've been awake for hours") from _call_receive_text_1117
        call receive_text(Laura, "Can't stop thinking about") from _call_receive_text_1118
        call receive_text(Laura, "Stuff") from _call_receive_text_1119
    elif dice_roll == 2:
        call receive_text(Laura, "I hope so") from _call_receive_text_1120
        call receive_text(Laura, "Will I see you today?") from _call_receive_text_1121
    elif dice_roll == 3:
        call receive_text(Laura, "Could tell me that in person") from _call_receive_text_380
        call receive_text(Laura, "Why aren't you in my bed") from _call_receive_text_381
        call receive_text(Laura, "Now I need to do it on my own. . .") from _call_receive_text_382

        $ Laura.behavior = "masturbating"

    return

label Laura_text_goodnight:
    if Laura.behavior == "training":
        $ dice_roll = renpy.random.randint(1, 4)
    else:
        $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        call receive_text(Laura, "I don't understand") from _call_receive_text_383
        call receive_text(Laura, "But") from _call_receive_text_384
        call receive_text(Laura, "Goodnight") from _call_receive_text_385
    elif dice_roll == 2:
        call receive_text(Laura, "Okay") from _call_receive_text_386
        call receive_text(Laura, "Goodnight") from _call_receive_text_387
    elif dice_roll == 3:
        call receive_text(Laura, "Yep") from _call_receive_text_1122
    elif dice_roll == 4:
        call receive_text(Laura, "You're going to sleep or something?") from _call_receive_text_388
        call receive_text(Laura, "I'm not done training yet") from _call_receive_text_389

    return

label Laura_text_goodnight_relationship:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        call receive_text(Laura, "Goodnight") from _call_receive_text_390
        call receive_text(Laura, "Sleep well") from _call_receive_text_391
        call receive_text(Laura, "Or else") from _call_receive_text_392
    elif dice_roll == 2:
        call receive_text(Laura, "Goodnight") from _call_receive_text_1123
        call receive_text(Laura, "See you tomorrow") from _call_receive_text_1124
    elif dice_roll == 3:
        call receive_text(Laura, "Talk to you tomorrow") from _call_receive_text_1125

    return

label Laura_text_goodnight_love:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        call receive_text(Laura, f"Goodnight {Laura.Player_petname}") from _call_receive_text_393
        call receive_text(Laura, "I") from _call_receive_text_394
        call receive_text(Laura, "Love you") from _call_receive_text_395
    elif dice_roll == 2:
        call receive_text(Laura, "Goodnight") from _call_receive_text_1126
        call receive_text(Laura, f"{Laura.Player_petname}") from _call_receive_text_1127
    elif dice_roll == 3:
        call receive_text(Laura, "Sleep already?") from _call_receive_text_396
        call receive_text(Laura, "Why aren't you in my bed?") from _call_receive_text_397

        $ Laura.mandatory_text_options = ["maybe some other night", "I'm sorry. maybe I could stay over tomorrow?", "because you toss and turn constantly. why can't you just relax?"]
        $ temp = Laura.mandatory_text_options[:]

        while Laura.mandatory_text_options:
            pause
        
        if Laura.text_history[-1][1] == temp[0]:
            pass
        elif Laura.text_history[-1][1] == temp[1]:
            call change_Character_stat(Laura, "love", tiny_stat) from _call_change_Character_stat_519

            call receive_text(Laura, "If I had it my way") from _call_receive_text_398
            call receive_text(Laura, "It would be every night") from _call_receive_text_399
        elif Laura.text_history[-1][1] == temp[2]:
            call change_Character_stat(Laura, "love", -tiny_stat) from _call_change_Character_stat_520

            call receive_text(Laura, "I can't help it") from _call_receive_text_400
            call receive_text(Laura, "Nightmares") from _call_receive_text_401

    return

label Laura_text_goodnight_mad:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        call receive_text(Laura, "No") from _call_receive_text_402
        call receive_text(Laura, "It hasn't been") from _call_receive_text_403
    elif dice_roll == 2:
        call receive_text(Laura, "Mhm") from _call_receive_text_1128
    elif dice_roll == 3:
        call receive_text(Laura, "Sure") from _call_receive_text_1129

    return

label Laura_text_goodnight_hearbroken:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        call receive_text(Laura, "Oh") from _call_receive_text_404
        call receive_text(Laura, "Okay") from _call_receive_text_405
    elif dice_roll == 2:
        pass
    elif dice_roll == 3:
        call receive_text(Laura, "Fine") from _call_receive_text_1130

    return

label Laura_text_goodnight_horny:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        call receive_text(Laura, "So early?") from _call_receive_text_406

        if approval_check(Laura, threshold = "hookup"):
            call receive_text(Laura, "But you didn't") from _call_receive_text_407
            call receive_text(Laura, "Never mind, I'll do it myself") from _call_receive_text_408

            $ Laura.behavior = "masturbating"
    elif dice_roll == 2:
        call receive_text(Laura, "Goodnight") from _call_receive_text_1131

        if approval_check(Laura, threshold = "hookup"):
            call receive_text(Laura, "I will be thinking of you tonight") from _call_receive_text_1132
    elif dice_roll == 3:
        call receive_text(Laura, "Fine, goodnight") from _call_receive_text_1133

    return

label Laura_text_goodnight_nympho:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        call receive_text(Laura, "Really?") from _call_receive_text_409
        call receive_text(Laura, "So early, again?") from _call_receive_text_410

        if approval_check(Laura, threshold = "hookup"):
            call receive_text(Laura, "One of these nights I'm going to have to make you give me some. . .") from _call_receive_text_411
            call receive_text(Laura, "Attention") from _call_receive_text_412
            call receive_text(Laura, "You better at least find me tomorrow") from _call_receive_text_413
    elif dice_roll == 2:
        call receive_text(Laura, "Don't go to sleep yet") from _call_receive_text_1134
        call receive_text(Laura, ". . .") from _call_receive_text_1135
        call receive_text(Laura, "Fine, tomorrow") from _call_receive_text_1136
    elif dice_roll == 3:
        call receive_text(Laura, "Why do you go to bed so early") from _call_receive_text_1137
        
        if approval_check(Laura, threshold = "hookup"):
            call receive_text(Laura, "I need your attention") from _call_receive_text_1138

    return

label Laura_text_ignored:
    call change_Character_stat(Laura, "love", -tiny_stat) from _call_change_Character_stat_523

    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        call receive_text(Laura, "Don't ignore me") from _call_receive_text_414
    elif dice_roll == 2:
        call receive_text(Laura, "Is your phone working properly?") from _call_receive_text_1139
    elif dice_roll == 3:
        call receive_text(Laura, "You better not be ignoring me") from _call_receive_text_1140

    $ Laura.give_status("miffed")

    return

label Laura_text_ask_on_date:
    if Player.date_planned or 2 in Player.schedule.keys() or 3 in Player.schedule.keys():
        call receive_text(Laura, "Not tonight") from _call_receive_text_731

        "You already have plans this evening."

        return
    
    if time_index > 2:
        call receive_text(Laura, "Little late for that") from _call_receive_text_415

        $ Laura.History.update("said_no_to_date")
        
        return
        
    if not Laura.History.check("went_on_date_with_Player"):
        if Player.cash < 130:
            call receive_text(Laura, "Not tonight") from _call_receive_text_416

            "First dates can be pretty expensive. . . you should probably save up at least $130 just to be sure."

            $ Laura.History.update("said_no_to_date")

            return

        $ Player.date_planned[Laura] = "Player_initiated_primary"

        $ phone_interactable = False

        if Laura.History.check("quirk_encouraged") >= Laura.History.check("quirk_discouraged"):
            if time_index < 2:
                call receive_text(Laura, "Be ready in the evening") from _call_receive_text_417
                call send_text(Laura, "where should we meet?") from _call_send_text_28

                pause 2.0

                call send_text(Laura, "???") from _call_send_text_29

                "She doesn't respond."
        else:
            call receive_text(Laura, "Yes") from _call_receive_text_418
            call send_text(Laura, "where should we meet?") from _call_send_text_30
            call receive_text(Laura, "Outside your room this evening") from _call_receive_text_419
            call send_text(Laura, "got it") from _call_send_text_31
            
        if time_index == 2:
            $ ongoing_Event = True
            
            if Party:
                call Characters_leave(Party) from _call_Characters_leave_3
        
            hide screen phone_screen

            $ phone_interactable = True
                
            $ EventScheduler.Events["Laura_first_date"].start()
    else:
        if Player.cash < 40:
            call receive_text(Laura, "Not tonight") from _call_receive_text_420

            "You sure you have enough money to take her on a date? Try saving up at least $40."

            $ Laura.History.update("said_no_to_date")

            $ phone_interactable = True

            return
    
        if Laura.status["mad"] or Laura.status["heartbroken"]:
            call receive_text(Laura, "Ask me again some other day") from _call_receive_text_421
                
            $ Laura.History.update("said_no_to_date")
        elif Laura.status["horny"] or Laura.status["nympho"]:
            call receive_text(Laura, "Yes") from _call_receive_text_422
            call receive_text(Laura, "But let's hurry back to my room after") from _call_receive_text_423

            $ Player.date_planned[Laura] = "Player_initiated_primary"
        else:
            if renpy.random.random() > 0.5 or Laura.History.check("trained", tracker = "daily"):
                $ dice_roll = renpy.random.randint(1, 2)
            else:
                $ dice_roll = renpy.random.randint(1, 4)

            if dice_roll == 1:
                call receive_text(Laura, "I do") from _call_receive_text_424
                call receive_text(Laura, "Be ready in the evening") from _call_receive_text_425

                $ Player.date_planned[Laura] = "Player_initiated_primary"
            elif dice_roll == 2:
                call receive_text(Laura, "Yes") from _call_receive_text_426
                call receive_text(Laura, "I'll find you this evening") from _call_receive_text_427

                $ Player.date_planned[Laura] = "Player_initiated_primary"
            elif dice_roll == 3:
                $ Laura.schedule[2] = ["bg_danger", "training"]

                call receive_text(Laura, "Not tonight") from _call_receive_text_428
                call receive_text(Laura, "Training") from _call_receive_text_429
                call receive_text(Laura, "Ask me again tomorrow") from _call_receive_text_430
                
                $ Laura.History.update("said_no_to_date")
            elif dice_roll == 4:
                $ Laura.schedule[2] = ["bg_danger", "training"]

                call receive_text(Laura, "Can't") from _call_receive_text_431
                call receive_text(Laura, "We're training tonight") from _call_receive_text_432
                call send_text(Laura, "we are?") from _call_send_text_32
                call receive_text(Laura, ". . .") from _call_receive_text_433

                $ Laura.mandatory_text_options = ["I mean. . . of course we are. . .", "I. . . can't tonight"]
                $ temp = Laura.mandatory_text_options[:]

                while Laura.mandatory_text_options:
                    pause

                if Laura.text_history[-1][1] == temp[0]:
                    $ Player.schedule[2] = [
                        ["Player.location != 'bg_danger'", "renpy.say(None, 'You head to the Danger Room to train with [Laura.name].')"],
                        ["Laura.location != 'bg_danger'", "renpy.call('send_Characters', Laura, 'bg_danger', behavior = 'training')"],
                        ["Player.location != 'bg_danger'", "renpy.call('set_the_scene', location = 'bg_danger')"],
                        ["True", "renpy.call('actually_train', Laura)"]]
                else:
                    call receive_text(Laura, ". . .") from _call_receive_text_434

                    $ Laura.History.update("Player_rejected_training")
                
                $ Laura.History.update("said_no_to_date")

    $ phone_interactable = True

    return