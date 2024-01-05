label Rogue_texting(message):
    python:
        for E in Rogue.timed_text_options.keys():
            for text in Rogue.timed_text_options[E]:
                if message == text:
                    renpy.call(f"{E}_response")

    if Rogue.timed_text_options:
        call Rogue_text_ignored from _call_Rogue_text_ignored

        $ Rogue.timed_text_options = {}

    if message == "how are you?":
        $ selected_Event = EventScheduler.choose_Event(texting = True)

        if selected_Event:
            call start_Event(selected_Event) from _call_start_Event_5
        else:
            if time_index == 3:
                if approval_check(Rogue, threshold = "talk_late"):
                    call Rogue_text_how_are_you_late_accept from _call_Rogue_text_how_are_you_late_accept
                else:
                    if approval_check(Rogue, threshold = "friendship"):
                        call Rogue_text_how_are_you_late_reject from _call_Rogue_text_how_are_you_late_reject
                    else:
                        if Rogue.History.check("said_too_late_to_text", tracker = "recent") == 1:
                            call Rogue_text_how_are_you_late_reject_asked_once from _call_Rogue_text_how_are_you_late_reject_asked_once
                        elif Rogue.History.check("said_too_late_to_text", tracker = "recent") > 1:
                            call Rogue_text_how_are_you_late_reject_asked_twice from _call_Rogue_text_how_are_you_late_reject_asked_twice
                        else:
                            call Rogue_text_how_are_you_late_reject from _call_Rogue_text_how_are_you_late_reject_1

                    $ Rogue.History.update("said_too_late_to_text")
            else:
                $ status = Rogue.get_status()

                if status not in ["heartbroken", "mad"]:
                    call change_Character_stat(Rogue, "love", tiny_stat) from _call_change_Character_stat_480

                if status:
                    call expression f"Rogue_text_how_are_you_{status}" from _call_expression_36
                elif approval_check(Rogue, threshold = "love"):
                    call Rogue_text_how_are_you_love from _call_Rogue_text_how_are_you_love
                elif Rogue in Partners:
                    call Rogue_text_how_are_you_relationship from _call_Rogue_text_how_are_you_relationship
                else:
                    call Rogue_text_how_are_you from _call_Rogue_text_how_are_you

        $ Rogue.History.update("sent_how_are_you_text")

    if "good morning" in message:
        $ status = Rogue.get_status()

        if status not in ["heartbroken", "mad"]:
            call change_Character_stat(Rogue, "love", tiny_stat) from _call_change_Character_stat_481

        if status:
            call expression f"Rogue_text_good_morning_{status}" from _call_expression_37
        elif approval_check(Rogue, threshold = "love"):
            call Rogue_text_good_morning_love from _call_Rogue_text_good_morning_love
        elif Rogue in Partners:
            call Rogue_text_good_morning_relationship from _call_Rogue_text_good_morning_relationship
        else:
            call Rogue_text_good_morning from _call_Rogue_text_good_morning

        $ Rogue.History.update("sent_good_morning_text")

    if "goodnight" in message:
        $ status = Rogue.get_status()

        if status not in ["heartbroken", "mad"]:
            call change_Character_stat(Rogue, "love", tiny_stat) from _call_change_Character_stat_482

        if status:
            call expression f"Rogue_text_goodnight_{status}" from _call_expression_38
        elif approval_check(Rogue, threshold = "love"):
            call Rogue_text_goodnight_love from _call_Rogue_text_goodnight_love
        elif Rogue in Partners:
            call Rogue_text_goodnight_relationship from _call_Rogue_text_goodnight_relationship
        else:
            call Rogue_text_goodnight from _call_Rogue_text_goodnight

        $ Rogue.History.update("said_goodnight")

    if message == "wanna come over?":
        call summon(Rogue) from _call_summon_3

    if message in ["want to go on a date tonight?", "want to go on that date tonight?"]:
        call Rogue_text_ask_on_date from _call_Rogue_text_ask_on_date

    return

label Rogue_text_how_are_you:
    $ dice_roll = renpy.random.randint(1, 3)
    
    if dice_roll == 1:
        call receive_text(Rogue, "Not too bad") from _call_receive_text_531
        call receive_text(Rogue, "Thanks for askin :))") from _call_receive_text_532
    elif dice_roll == 2:
        call receive_text(Rogue, "Good! Havin a pretty good day actually")
    elif dice_roll == 3:
        call receive_text(Rogue, "Meh, its a day. How are you?")

        $ Rogue.mandatory_text_options = ["anything I can do?", "same", "jeez with the negativity"]
        $ temp = Rogue.mandatory_text_options[:]

        while Rogue.mandatory_text_options:
            pause

        if Rogue.text_history[-1][1] == temp[0]:
            call change_Character_stat(Rogue, "love", tiny_stat)

            call receive_text(Rogue, "Nah Im okay :)")
            call receive_text(Rogue, "Youre sweet though")
        elif Rogue.text_history[-1][1] == temp[1]:
            call receive_text(Rogue, "we can do it, I believe in us")
        elif Rogue.text_history[-1][1] == temp[2]:
            call change_Character_stat(Rogue, "love", -tiny_stat)

            call receive_text(Rogue, "I am not negative! So rude")
    
    return

label Rogue_text_how_are_you_late_accept:
    $ dice_roll = renpy.random.randint(1, 3)
    
    if dice_roll == 1:
        call receive_text(Rogue, "Im alright") from _call_receive_text_533
        call receive_text(Rogue, "Was bout to go to sleep") from _call_receive_text_534
        call receive_text(Rogue, "But I could. . .") from _call_receive_text_535
        call receive_text(Rogue, "Stay up a bit longer if ya wanted to chat") from _call_receive_text_536
    elif dice_roll == 2:
        call receive_text(Rogue, "Good, just gettin ready for bed :)")
        call receive_text(Rogue, "Might stay up for a bit longer though")
    elif dice_roll == 3:
        call receive_text(Rogue, "Just hangin out a bit before going to sleep!")

    return

label Rogue_text_how_are_you_late_reject:
    $ dice_roll = renpy.random.randint(1, 3)
    
    if dice_roll == 1:
        call receive_text(Rogue, "Good") from _call_receive_text_537
        call receive_text(Rogue, "Real tired tho") from _call_receive_text_538
        call receive_text(Rogue, "Bout to hit the hay, can't really chat") from _call_receive_text_539
        call receive_text(Rogue, "Sorry hon") from _call_receive_text_540
    elif dice_roll == 2:
        call receive_text(Rogue, "Sleepy! Night!")
    elif dice_roll == 3:
        call receive_text(Rogue, "Just gettin ready for bed, talk to ya tomorrow!")

    return

label Rogue_text_how_are_you_late_reject_asked_once:
    call Rogue_asked_once_text("late") from _call_Rogue_asked_once_text_2

    return

label Rogue_text_how_are_you_late_reject_asked_twice:
    call Rogue_asked_twice_text("late") from _call_Rogue_asked_twice_text_2
    
    return

label Rogue_text_how_are_you_relationship:
    $ dice_roll = renpy.random.randint(1, 3)
    
    if dice_roll == 1:
        call receive_text(Rogue, "Pretty good") from _call_receive_text_545
        call receive_text(Rogue, "Could be better if we were hangin") from _call_receive_text_546
    elif dice_roll == 2:
        call receive_text(Rogue, "Good! Hope I get to see you later!")
    elif dice_roll == 3:
        call receive_text(Rogue, f"Heh, Im doing alright {Rogue.Player_petname} :)")

    return

label Rogue_text_how_are_you_love:
    $ dice_roll = renpy.random.randint(1, 3)
    
    if dice_roll == 1:
        call receive_text(Rogue, "Good, just thinkin bout ya :)")
    elif dice_roll == 2:
        call receive_text(Rogue, "Good :):)")
        call receive_text(Rogue, "Youre so sweet always checkin on me")
    elif dice_roll == 3:
        call receive_text(Rogue, "Im good") from _call_receive_text_547
        call receive_text(Rogue, "But I miss ya lots") from _call_receive_text_548
        call receive_text(Rogue, "I really love you") from _call_receive_text_549

        $ Rogue.mandatory_text_options = ["we just saw each other, but I love you too", "I always miss you too, love you", "we literally just saw each other, chill"]
        $ temp = Rogue.mandatory_text_options[:]

        while Rogue.mandatory_text_options:
            pause

        if Rogue.text_history[-1][1] == temp[0]:
            call receive_text(Rogue, "Sorry, just can't help it") from _call_receive_text_550
        elif Rogue.text_history[-1][1] == temp[1]:
            call change_Character_stat(Rogue, "love", tiny_stat) from _call_change_Character_stat_786

            call receive_text(Rogue, "Really hope you come by later :)))") from _call_receive_text_551
        elif Rogue.text_history[-1][1] == temp[2]:
            call change_Character_stat(Rogue, "love", -tiny_stat) from _call_change_Character_stat_787

            call receive_text(Rogue, "Sorry") from _call_receive_text_552

    return

label Rogue_text_how_are_you_mad:
    $ dice_roll = renpy.random.randint(1, 3)
    
    if dice_roll == 1:
        call receive_text(Rogue, "Madder than a cat in a rainstorm") from _call_receive_text_553
        call receive_text(Rogue, "You best not come near anytime soon") from _call_receive_text_554
    elif dice_roll == 2:
        call receive_text(Rogue, "Youre really gonna ask me that?")
    elif dice_roll == 3:
        call receive_text(Rogue, "You know damn well how Im doin")

    return

label Rogue_text_how_are_you_hearbroken:
    $ dice_roll = renpy.random.randint(1, 3)
    
    if dice_roll == 1:
        call receive_text(Rogue, "Im") from _call_receive_text_555
        call receive_text(Rogue, "Well") from _call_receive_text_556
        call receive_text(Rogue, "I reckon im just") from _call_receive_text_557
        call receive_text(Rogue, "Sad as a willow") from _call_receive_text_558
    elif dice_roll == 2:
        call receive_text(Rogue, "Oh")
        call receive_text(Rogue, "Im okay I guess")
    elif dice_roll == 3:
        call receive_text(Rogue, "Ive been better. . .")

    return

label Rogue_text_how_are_you_horny:
    if Rogue.location == Rogue.home:
        $ dice_roll = renpy.random.randint(1, 3)
    else:
        $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        call receive_text(Rogue, "Im alright") from _call_receive_text_559

        if approval_check(Rogue, threshold = "hookup"):
            call receive_text(Rogue, "Would be a might better if I could lay my eyes on you. . .") from _call_receive_text_560
        else:
            call receive_text(Rogue, "Wouldnt mind hangin out later though :)")
    elif dice_roll == 2:
        call receive_text(Rogue, "Good :)")
        call receive_text(Rogue, "Was just thinkin bout you, actually")
    elif dice_roll == 3:
        call receive_text(Rogue, "I was just bout to text ya")
        call receive_text(Rogue, "Wanna hang out or somethin? :)")

        $ Rogue.mandatory_text_options = ["yeah of course!", "I wish, I'm pretty busy though. . .", "not really"]
        $ temp = Rogue.mandatory_text_options[:]

        while Rogue.mandatory_text_options:
            pause

        if Rogue.text_history[-1][1] == temp[0]:
            call receive_text(Rogue, "Yay! My room?")
            call send_text(Rogue, "be right there!")

            call move_location(Rogue.home)
        elif Rogue.text_history[-1][1] == temp[1]:
            call receive_text(Rogue, "Well")
            call receive_text(Rogue, "Maybe later")
            call receive_text(Rogue, "Could be fun :)")
        elif Rogue.text_history[-1][1] == temp[2]:
            call change_Character_stat(Rogue, "love", -tiny_stat)

            call receive_text(Rogue, "Rude")
    
    return

label Rogue_text_how_are_you_nympho:
    if approval_check(Rogue, threshold = "hookup"):
        $ dice_roll = renpy.random.randint(1, 3)
    else:
        $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        call receive_text(Rogue, "Im okay but")
        call receive_text(Rogue, "We should hang out later")
    elif dice_roll == 2:
        call receive_text(Rogue, "Good!")
        call receive_text(Rogue, "Is it just me or is it really warm today, though?")
    elif dice_roll == 3:
        call receive_text(Rogue, "All hot and bothered") from _call_receive_text_561
        call receive_text(Rogue, "Only a good dose of you could cool me off. . .") from _call_receive_text_562

    return

label Rogue_text_good_morning:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        call receive_text(Rogue, "Mornin!") from _call_receive_text_563
    elif dice_roll == 2:
        call receive_text(Rogue, "Gmornin darlin :)") from _call_receive_text_564
    elif dice_roll == 3:
        call receive_text(Rogue, "Howdy!") from _call_receive_text_565
        call receive_text(Rogue, "Hope ya slept well") from _call_receive_text_566

    return

label Rogue_text_good_morning_relationship:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        call receive_text(Rogue, f"Mornin {Rogue.Player_petname} :)))") from _call_receive_text_567
    elif dice_roll == 2:
        call receive_text(Rogue, "Hey! Miss me last night? :)")
    elif dice_roll == 3:
        call receive_text(Rogue, f"Hey {Rogue.Player_petname} <33")

    return

label Rogue_text_good_morning_love:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        call receive_text(Rogue, "Mornin lover") from _call_receive_text_568
        call receive_text(Rogue, "Had a dream bout ya last night") from _call_receive_text_569
    elif dice_roll == 2:
        call receive_text(Rogue, "Good mornin!!! Cant wait to see you today :)")
    elif dice_roll == 3:
        call receive_text(Rogue, "Mornin darlin") from _call_receive_text_570
        call receive_text(Rogue, "Sleep well") from _call_receive_text_571

        $ Rogue.mandatory_text_options = ["pretty well", "would've been better with you here", "tbh, no"]
        $ temp = Rogue.mandatory_text_options[:]

        while Rogue.mandatory_text_options:
            pause

        if Rogue.text_history[-1][1] == temp[0]:
            call receive_text(Rogue, "Good!") from _call_receive_text_572
        elif Rogue.text_history[-1][1] == temp[1]:
            call change_Character_stat(Rogue, "love", tiny_stat) from _call_change_Character_stat_793

            call receive_text(Rogue, "Well") from _call_receive_text_573
            call receive_text(Rogue, "You know I always wanna :)))") from _call_receive_text_574
        elif Rogue.text_history[-1][1] == temp[2]:
            call receive_text(Rogue, "Oh no! Im sorry hon") from _call_receive_text_575

    return

label Rogue_text_good_morning_mad:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        call receive_text(Rogue, "No") from _call_receive_text_576
        call receive_text(Rogue, "It aint been") from _call_receive_text_577
    elif dice_roll == 2:
        call receive_text(Rogue, "Is it?")
    elif dice_roll == 2:
        call receive_text(Rogue, "Mhm")

    return

label Rogue_text_good_morning_hearbroken:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        call receive_text(Rogue, "My mornins not been so good. . .") from _call_receive_text_578
    elif dice_roll == 2:
        call receive_text(Rogue, "Mornin. . .")
        call receive_text(Rogue, "Kinda wish Id stayed in bed. . .")
    elif dice_roll == 2:
        call receive_text(Rogue, "I guess. . .")

    return

label Rogue_text_good_morning_horny:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        call receive_text(Rogue, "Good mornin handsome!")
    elif dice_roll == 2:
        call receive_text(Rogue, "Good mornin :)")
        call receive_text(Rogue, "Any chance you want to hang out later?")
    elif dice_roll == 3:
        call receive_text(Rogue, f"Good mornin {Rogue.Player_petname}") from _call_receive_text_579

        if approval_check(Rogue, threshold = "hookup"):
            call receive_text(Rogue, "Was just thinkin bout you") from _call_receive_text_580

    return

label Rogue_text_good_morning_nympho:
    if approval_check(Rogue, threshold = "hookup"):
        $ dice_roll = renpy.random.randint(1, 3)
    else:
        $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        call receive_text(Rogue, "Yeah it is ;)")
    elif dice_roll == 2:
        call receive_text(Rogue, "Mmm good mornin to you too!")
    elif dice_roll == 3:
        call receive_text(Rogue, "Wish you could tell me in person") from _call_receive_text_581
        call receive_text(Rogue, "Wouldnt mind you bein in bed with me. . .") from _call_receive_text_582

    return

label Rogue_text_goodnight:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        call receive_text(Rogue, f"Gnight {Rogue.Player_petname}!") from _call_receive_text_583
    elif dice_roll == 2:
        call receive_text(Rogue, "Sweet dreams darlin") from _call_receive_text_584
    elif dice_roll == 3:
        call receive_text(Rogue, "Gnight") from _call_receive_text_585
        call receive_text(Rogue, "See ya tomorrow :)") from _call_receive_text_586
    
    return

label Rogue_text_goodnight_relationship:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        call receive_text(Rogue, "Night hon") from _call_receive_text_587
        call receive_text(Rogue, "Sleep tight") from _call_receive_text_588
    elif dice_roll == 2:
        call receive_text(Rogue, "Night! Cant wait to see you tomorrow :)")
    elif dice_roll == 3:
        call receive_text(Rogue, f"Sleep well {Rogue.Player_petname}")

    return

label Rogue_text_goodnight_love:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        call receive_text(Rogue, f"Gnight {Rogue.Player_petname}") from _call_receive_text_589
        call receive_text(Rogue, "Love you") from _call_receive_text_590
    elif dice_roll == 2:
        call receive_text(Rogue, "Sleep well for me! <333")
    elif dice_roll == 3:
        call receive_text(Rogue, "Gnight") from _call_receive_text_591
        call receive_text(Rogue, "Wish you were here <3") from _call_receive_text_593

        $ Rogue.mandatory_text_options = ["I do too, we'll see about some other day", "if you're good, I might stay over tomorrow", "maybe I would be if you didn't snore"]
        $ temp = Rogue.mandatory_text_options[:]

        while Rogue.mandatory_text_options:
            pause
        
        if Rogue.text_history[-1][1] == temp[0]:
            pass
        elif Rogue.text_history[-1][1] == temp[1]:
            call receive_text(Rogue, "I will be") from _call_receive_text_594
            call receive_text(Rogue, "I promise") from _call_receive_text_595
        elif Rogue.text_history[-1][1] == temp[2]:
            call change_Character_stat(Rogue, "love", -tiny_stat) from _call_change_Character_stat_800

            call receive_text(Rogue, "Do I really snore?") from _call_receive_text_596
            call receive_text(Rogue, "Sorry. . .") from _call_receive_text_597

    return

label Rogue_text_goodnight_mad:
    $ dice_roll = renpy.random.randint(1, 3)
    
    if dice_roll == 1:
        call receive_text(Rogue, "No") from _call_receive_text_598
        call receive_text(Rogue, "It aint") from _call_receive_text_599
    elif dice_roll == 2:
        call receive_text(Rogue, "K")
    elif dice_roll == 3:
        call receive_text(Rogue, "Whatever")

    return

label Rogue_text_goodnight_hearbroken:
    $ dice_roll = renpy.random.randint(1, 3)
    
    if dice_roll == 1:
        call receive_text(Rogue, "Oh") from _call_receive_text_600
        call receive_text(Rogue, "Okay") from _call_receive_text_601
        call receive_text(Rogue, "Goodnight") from _call_receive_text_602
    elif dice_roll == 2:
        call receive_text(Rogue, "Goodnight. . .")
    elif dice_roll == 3:
        call receive_text(Rogue, "Maybe. . . nevermind, goodnight")

    return

label Rogue_text_goodnight_horny:
    $ dice_roll = renpy.random.randint(1, 3)
    
    if dice_roll == 1:
        call receive_text(Rogue, "Oh, youre goin to bed?") from _call_receive_text_603
        call receive_text(Rogue, "Was wonderin") from _call_receive_text_604
        call receive_text(Rogue, "Never mind, maybe tomorrow") from _call_receive_text_605
        call receive_text(Rogue, "Gnight! :)") from _call_receive_text_606
    elif dice_roll == 2:
        call receive_text(Rogue, "Already going to bed?")

        if approval_check(Rogue, threshold = "hookup"):
            call receive_text(Rogue, "Sure you don't want to. . . you know?")
            call receive_text(Rogue, ". . . I guess I can wait till we're together")
        else:
            call receive_text(Rogue, "Gnight ;)")
    elif dice_roll == 3:
        if approval_check(Rogue, threshold = "hookup"):
            call receive_text(Rogue, "Sleep tight, think of me <3")
        else:
            call receive_text(Rogue, "Sleep tight haha")

    return

label Rogue_text_goodnight_nympho:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        call receive_text(Rogue, "Youre goin to bed?") from _call_receive_text_607
        call receive_text(Rogue, "But") from _call_receive_text_608

        if approval_check(Rogue, threshold = "hookup"):
            call receive_text(Rogue, "I could really use some attention. . .") from _call_receive_text_609
            call receive_text(Rogue, "Or at least have you to press up against. . .") from _call_receive_text_610
        else:
            call receive_text(Rogue, ":(")
    elif dice_roll == 2:
        if approval_check(Rogue, threshold = "hookup"):
            call receive_text(Rogue, f"Come on {Rogue.Player_petname}, you cant go to bed without giving your {Rogue.petname} some attention!")

        call receive_text(Rogue, ":(")
        call receive_text(Rogue, "Fine")
    elif dice_roll == 3:
        call receive_text(Rogue, "Already?")
        call receive_text(Rogue, "But. . .")

        if approval_check(Rogue, threshold = "hookup"):
            call receive_text(Rogue, "I'm dripping for you. . .")

    return

label Rogue_text_ignored:
    call change_Character_stat(Rogue, "love", -tiny_stat) from _call_change_Character_stat_803

    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        call receive_text(Rogue, "Oh") from _call_receive_text_611
        call receive_text(Rogue, "Maybe my texts aren't going through")
    elif dice_roll == 2:
        call receive_text(Rogue, ". . .")
    elif dice_roll == 3:
        call receive_text(Rogue, "?")

    $ Rogue.give_status("miffed")

    return

label Rogue_text_ask_on_date:
    if Player.date_planned or 2 in Player.schedule.keys() or 3 in Player.schedule.keys():
        call receive_text(Rogue, "Oh no! I can't tonight. Rain check?") from _call_receive_text_732

        "You already have plans this evening."

        return

    if time_index > 2:
        call receive_text(Rogue, "I don't think there's time today. . .") from _call_receive_text_613

        $ Rogue.History.update("said_no_to_date")
        
        return
        
    if not Rogue.History.check("went_on_date_with_Player"):
        if Player.cash < 130:
            call receive_text(Rogue, "Oh no! I can't tonight. Rain check?") from _call_receive_text_614

            "First dates can be pretty expensive. . . you should probably save up at least $130 just to be sure."

            $ Rogue.History.update("said_no_to_date")

            return

        $ Player.date_planned[Rogue] = "Player_initiated_primary"

        $ phone_interactable = False

        call receive_text(Rogue, "Yes!", delay = 0.25) from _call_receive_text_615

        "She must've already been looking at her phone. . ."

        if time_index == 2:
            call send_text(Rogue, "great!") from _call_send_text_42

            if Player.location == "bg_hallway":
                call send_text(Rogue, "let's meet outside my room") from _call_send_text_43
            else:
                call send_text(Rogue, "I'll be waiting right outside my room") from _call_send_text_44

            call receive_text(Rogue, "Omw! :))") from _call_receive_text_616
            call receive_text(Rogue, "See ya soon") from _call_receive_text_617
        else:
            call receive_text(Rogue, "Where did ya wanna meet?") from _call_receive_text_618
            call send_text(Rogue, "right outside my room") from _call_send_text_45
            call send_text(Rogue, "does that work?") from _call_send_text_46
            call receive_text(Rogue, "Sure does") from _call_receive_text_619
            call receive_text(Rogue, "See ya later :)))") from _call_receive_text_620
            
        if time_index == 2:
            $ ongoing_Event = True
            
            pause 1.0
            
            hide screen phone_screen

            if Party:
                call Characters_leave(Party) from _call_Characters_leave_4

            if Player.location != "bg_hallway":
                call remove_Characters(location = "bg_hallway") from _call_remove_Characters_208
                call send_Characters(Rogue, "bg_hallway", behavior = "on_date") from _call_send_Characters_168
                call set_the_scene(location = "bg_hallway") from _call_set_the_scene_226

                $ Rogue.change_face("pleased1")

                ch_Player "Damn, you beat me."

                $ Rogue.change_face("worried1", mouth = "smirk", eyes = "right", blush = 1)

                ch_Rogue "Heh,  yeah. . . ah was close by. . ."

                $ Rogue.change_face("worried1", mouth = "smirk")
            else:
                "You barely wait a minute before [Rogue.name] arrives."

                call remove_Characters(location = "bg_hallway") from _call_remove_Characters_209
                call send_Characters(Rogue, "bg_hallway", behavior = "on_date") from _call_send_Characters_169

                $ Rogue.change_face("happy")

                ch_Rogue "Hey, [Rogue.Player_petname]!"

                $ Rogue.change_face("worried2", mouth = "lipbite", eyes = "right", blush = 1)

                ch_Player "Damn, that was fast."

                $ Rogue.change_face("worried1", mouth = "smirk", blush = 1)

                ch_Rogue "Heh, yeah. . . ah was close by. . ."

                $ Rogue.change_face("worried1", mouth = "smirk")

            $ phone_interactable = True

            $ EventScheduler.Events["Rogue_first_date"].start()
    else:
        if Player.cash < 40:
            call receive_text(Rogue, "Oh no! I can't tonight. Rain check?") from _call_receive_text_621

            "You sure you have enough money to take her on a date? Try saving up at least $40."

            $ Rogue.History.update("said_no_to_date")

            $ phone_interactable = True

            return
    
        if Rogue.status["mad"] or Rogue.status["heartbroken"]:
            call receive_text(Rogue, "I cant tonight") from _call_receive_text_622
            call receive_text(Rogue, "Maybe some other day. . .") from _call_receive_text_623
                
            $ Rogue.History.update("said_no_to_date")
        elif Rogue.status["horny"] or Rogue.status["nympho"]:
            call receive_text(Rogue, "Yes please. . .") from _call_receive_text_624
            call receive_text(Rogue, "Aint nothin better than a date with you") from _call_receive_text_625
            call receive_text(Rogue, "I just hope you have some special plans for after") from _call_receive_text_626

            $ Player.date_planned[Rogue] = "Player_initiated_primary"
        else:
            if renpy.random.random() > 0.5 or Rogue.History.check("studied", tracker = "daily"):
                $ dice_roll = renpy.random.randint(1, 2)
            else:
                $ dice_roll = renpy.random.randint(1, 4)

            if dice_roll == 1:
                call receive_text(Rogue, "You know I do!") from _call_receive_text_627
                call receive_text(Rogue, "Im lookin forward to it") from _call_receive_text_628

                $ Player.date_planned[Rogue] = "Player_initiated_primary"
            elif dice_roll == 2:
                call receive_text(Rogue, "I was hopin youd ask") from _call_receive_text_629
                call receive_text(Rogue, "See ya tonight :))") from _call_receive_text_630

                $ Player.date_planned[Rogue] = "Player_initiated_primary"
            elif dice_roll == 3:
                $ Rogue.schedule[2] = [Rogue.home, "studying"]
                
                call receive_text(Rogue, f"Im sorry, {Rogue.Player_petname}, I really want to") from _call_receive_text_631
                call receive_text(Rogue, "Tonight just aint good for me") from _call_receive_text_632
                call receive_text(Rogue, "Please ask me again tomorrow") from _call_receive_text_633

                $ Rogue.History.update("said_no_to_date")
            elif dice_roll == 4:
                $ Rogue.schedule[2] = [Rogue.home, "studying"]

                call receive_text(Rogue, "I sure want to") from _call_receive_text_634
                call receive_text(Rogue, "But we got a test comin up") from _call_receive_text_635
                call receive_text(Rogue, "Maybe we could study together instead?") from _call_receive_text_636
                call send_text(Rogue, "we do?") from _call_send_text_47
                call receive_text(Rogue, "Haha, yep") from _call_receive_text_637

                $ Rogue.mandatory_text_options = ["sure, we can study tonight", "sorry, I. . . can't tonight"]
                $ temp = Rogue.mandatory_text_options[:]

                while Rogue.mandatory_text_options:
                    pause

                if Rogue.text_history[-1][1] == temp[0]:
                    $ Player.schedule[2] = [
                        ["Player.location != Rogue.home", "renpy.say(None, 'You rush over to study for that test with [Rogue.name].')"],
                        ["Rogue.location != Rogue.home", "renpy.call('send_Characters', Rogue, Rogue.home, behavior = 'studying')"],
                        ["Player.location != Rogue.home", "renpy.call('set_the_scene', location = Rogue.home)"],
                        ["True", "renpy.call('actually_study', Rogue)"]]
                else:
                    call receive_text(Rogue, "Oh. . . okay") from _call_receive_text_638

                    $ Rogue.History.update("Player_rejected_studying")
                
                $ Rogue.History.update("said_no_to_date")

    $ phone_interactable = True

    return