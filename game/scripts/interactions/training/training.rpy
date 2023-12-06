label train:
    $ Character_picker_disabled = True
    $ belt_disabled = True

    $ Player.behavior = "training"

    $ training_Character = None

    menu:
        "Train on your own":
            $ renpy.dynamic(temp_Characters = Present[:])

            while temp_Characters:
                call remove_Characters(temp_Characters[0]) from _call_remove_Characters_237

                $ temp_Characters.remove(temp_Characters[0])

            $ _return = True
        "Train with [Rogue.name]" if not Rogue.History.check("trained_with_Player", tracker = "daily") and Rogue in Present and not Rogue.History.check("said_no_to_training", tracker = "recent") > 2:
            call ask_to_train(Rogue) from _call_ask_to_train

            if _return:
                $ training_Character = Rogue
        "Invite [Rogue.name] to train" if not Rogue.History.check("trained_with_Player", tracker = "daily") and Rogue in Contacts and Rogue in active_Companions and Rogue not in Present and Rogue.location != "hold" and not Rogue.History.check("said_no_to_training", tracker = "recent") > 2 and not Rogue.History.check("said_goodnight", tracker = "recent"):
            call ask_to_train(Rogue) from _call_ask_to_train_1

            if _return:
                $ training_Character = Rogue
        "Train with [Laura.name]" if not Laura.History.check("trained_with_Player", tracker = "daily") and Laura in Present and not Laura.History.check("said_no_to_training", tracker = "recent") > 2:
            call ask_to_train(Laura) from _call_ask_to_train_2

            if _return:
                $ training_Character = Laura
        "Invite [Laura.name] to train" if not Laura.History.check("trained_with_Player", tracker = "daily") and Laura in Contacts and Laura in active_Companions and Laura not in Present and Laura.location != "hold" and not Laura.History.check("said_no_to_training", tracker = "recent") > 2 and not Laura.History.check("said_goodnight", tracker = "recent"):
            call ask_to_train(Laura) from _call_ask_to_train_3

            if _return:
                $ training_Character = Laura
        "Train with [Jean.name]" if not Jean.History.check("trained_with_Player", tracker = "daily") and Jean in Present and not Jean.History.check("said_no_to_training", tracker = "recent") > 2:
            call ask_to_train(Jean) from _call_ask_to_train_4

            if _return:
                $ training_Character = Jean
        "Invite [Jean.name] to train" if not Jean.History.check("trained_with_Player", tracker = "daily") and Jean in Contacts and Jean in active_Companions and Jean not in Present and Jean.location != "hold" and not Jean.History.check("said_no_to_training", tracker = "recent") > 2 and not Jean.History.check("said_goodnight", tracker = "recent"):
            call ask_to_train(Jean) from _call_ask_to_train_5

            if _return:
                $ training_Character = Jean
        "Back":
            $ Character_picker_disabled = False
            $ belt_disabled = False

            return

    if _return:
        if Player.behavior == "studying":
            call actually_study(training_Character) from _call_actually_study_13
        elif Player.behavior == "training":
            call actually_train(training_Character) from _call_actually_train_10
    else:
        $ reset_behavior(Player)

    if not renpy.get_screen("phone_screen"):
        $ Character_picker_disabled = False
        $ belt_disabled = False

    return

label ask_to_train(Character):
    $ status = Character.get_status()

    if Character in Present:
        ch_Player "Hey, [Character.name], wanna train together?"

        if Character.is_in_normal_mood() and not Character.History.check("trained_with_Player", tracker = "daily") and time_index < 3:
            call expression f"{Character.tag}_accept_train" from _call_expression_346
        else:
            if Character.History.check("said_no_to_training", tracker = "recent") >= 2:
                call change_Character_stat(Character, "love", -5) from _call_change_Character_stat_1029
                call change_Character_stat(Character, "trust", -5) from _call_change_Character_stat_1030

                call expression f"{Character.tag}_reject_train_asked_twice" from _call_expression_347
            elif Character.History.check("said_no_to_training", tracker = "recent") == 1:
                call change_Character_stat(Character, "love", -2) from _call_change_Character_stat_1031
                
                call expression f"{Character.tag}_reject_train_asked_once" from _call_expression_348
            else:
                call expression f"{Character.tag}_reject_train" from _call_expression_349

            $ Character.History.update("said_no_to_training")

            $ phone_interactable = True 

            return False
    else:
        call open_texts(Character) from _call_open_texts_21
        call send_text(Character, "hey, wanna train? I'm in the Danger Room rn") from _call_send_text_81

        if time_index == 3:
            if Character.History.check("said_too_late_to_text", tracker = "recent") >= 2:
                call change_Character_stat(Character, "love", -5) from _call_change_Character_stat_1032
                call change_Character_stat(Character, "trust", -5) from _call_change_Character_stat_1033

                call expression f"{Character.tag}_summon_reject_asked_twice" from _call_expression_351
            elif Character.History.check("said_too_late_to_text", tracker = "recent") == 1:
                call change_Character_stat(Character, "love", -2) from _call_change_Character_stat_1034

                call expression f"{Character.tag}_summon_reject_asked_once" from _call_expression_352
            else:
                call expression f"{Character.tag}_summon_busy_late" from _call_expression_353

            $ Character.History.update("said_too_late_to_text")

            $ phone_interactable = True 

            return False
        else:
            if time_index not in Character.schedule.keys() and Character.is_in_normal_mood() and not Character.History.check("trained_with_Player", tracker = "daily"):
                call expression f"{Character.tag}_accept_train_text" from _call_expression_354
            else:
                if Character.History.check("said_no_to_training", tracker = "recent") >= 2:
                    call change_Character_stat(Character, "love", -5) from _call_change_Character_stat_1035
                    call change_Character_stat(Character, "trust", -5) from _call_change_Character_stat_1036

                    call expression f"{Character.tag}_reject_train_asked_twice_text" from _call_expression_355
                elif Character.History.check("said_no_to_training", tracker = "recent") == 1:
                    call change_Character_stat(Character, "love", -2) from _call_change_Character_stat_1037

                    call expression f"{Character.tag}_reject_train_asked_once_text" from _call_expression_356
                else:
                    call expression f"{Character.tag}_reject_train_text" from _call_expression_357

                $ Character.History.update("said_no_to_training")

                $ phone_interactable = True 

                return False

        pause

        hide screen phone_screen

    return True

label actually_train(Character):            
    hide screen phone_screen

    if Character:
        $ Player.behavior = "training"
        $ Player.behavior_Partners = [Character]

        $ Character.behavior = "training"

    if black_screen:
        $ fade_in_from_black(0.4)

    $ clock -= 1

    $ selected_Event = EventScheduler.choose_Event()

    if selected_Event:
        if Character:
            if Character not in Present:
                $ Character.destination = Player.location

                call set_Character_Outfits(Character, instant = True) from _call_set_Character_Outfits_20  

                call Characters_arrive(Character, invited = True) from _call_Characters_arrive_2

                $ Character.location = Character.destination
            else:
                call set_Character_Outfits(Character, instant = False) from _call_set_Character_Outfits_19

            call remove_everyone_but(Character) from _call_remove_everyone_but_8
            
        call start_Event(selected_Event) from _call_start_Event_14
    else:
        $ fade_to_black(0.4)

        call expression f"chapter_{chapter}_season_{season}_training_narrations" from _call_expression_358

        pause 2.0

        if clock > 0 or time_index == 3:
            $ fade_in_from_black(0.4)

    call after_training from _call_after_training
    call check_for_Events(only_automatic = True) from _call_check_for_Events_21
    call move_location(Player.location) from _call_move_location_52

    return

label after_training:
    if Player.behavior_Partners:
        python:
            for C in Player.behavior_Partners:
                C.History.update("trained_with_Player")
                C.behavior = None

                gained_XP = int(10*C.stat_modifier)
                C.XP += gained_XP

                if time_index in C.schedule.keys() and C.schedule[time_index][1] == "training":
                    del C.schedule[time_index]
                
                update_messages.append("{color=%s}%s{/color} gained {color=%s}%s XP{/color} from {color=%s}Training{/color}" % (eval(f"{C.tag}_color"), C.name, "#feba00", gained_XP, "#feba00"))

    $ Player.History.update("trained")
    $ Player.behavior = None
    $ Player.sweat += 1
    
    $ gained_XP = int(10*Player.stat_modifier)
    $ Player.XP += gained_XP

    $ update_messages.append("{color=%s}%s{/color} gained {color=%s}%s XP{/color} from {color=%s}Training{/color}" % ("#feba00", Player.first_name, "#feba00", gained_XP, "#feba00"))

    return