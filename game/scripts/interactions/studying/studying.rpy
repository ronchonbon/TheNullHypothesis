label study_session:
    $ Character_picker_disabled = True
    $ belt_disabled = True

    $ Player.studying = True
    $ Player.training = False

    $ studying_Girl = None

    menu:
        "Study on your own":
            python:
                for C in Present:
                    C.studying = False
                    
            $ _return = True
        "Study with [Rogue.name]" if not Rogue.History.check("studied_with_Player", tracker = "daily") and Rogue in Present and not Rogue.History.check("said_no_to_studying", tracker = "recent") > 2:
            call ask_to_study(Rogue) from _call_ask_to_study

            if _return:
                $ studying_Girl = Rogue
        "Invite [Rogue.name] to study" if not Rogue.History.check("studied_with_Player", tracker = "daily") and Rogue in Contacts and Rogue in active_Girls and Rogue not in Present and Rogue.location != "hold" and Player.location not in [Laura.home, Jean.home] and not Rogue.History.check("said_no_to_studying", tracker = "recent") > 2 and not Rogue.History.check("said_goodnight", tracker = "recent"):
            call ask_to_study(Rogue) from _call_ask_to_study_1

            if _return:
                $ studying_Girl = Rogue
        "Study with [Laura.name]" if not Laura.History.check("studied_with_Player", tracker = "daily") and Laura in Present and not Laura.History.check("said_no_to_studying", tracker = "recent") > 2:
            call ask_to_study(Laura) from _call_ask_to_study_2

            if _return:
                $ studying_Girl = Laura
        "Invite [Laura.name] to study" if not Laura.History.check("studied_with_Player", tracker = "daily") and Laura in Contacts and Laura in active_Girls and Laura not in Present and Laura.location != "hold" and Player.location not in [Rogue.home, Jean.home] and not Laura.History.check("said_no_to_studying", tracker = "recent") > 2 and not Laura.History.check("said_goodnight", tracker = "recent"):
            call ask_to_study(Laura) from _call_ask_to_study_3

            if _return:
                $ studying_Girl = Laura
        "Study with [Jean.name]" if not Jean.History.check("studied_with_Player", tracker = "daily") and Jean in Present and not Jean.History.check("said_no_to_studying", tracker = "recent") > 2:
            call ask_to_study(Jean) from _call_ask_to_study_4

            if _return:
                $ studying_Girl = Jean
        "Invite [Jean.name] to study" if not Jean.History.check("studied_with_Player", tracker = "daily") and Jean in Contacts and Jean in active_Girls and Jean not in Present and Jean.location != "hold" and Player.location not in [Rogue.home, Laura.home] and not Jean.History.check("said_no_to_studying", tracker = "recent") > 2 and not Jean.History.check("said_goodnight", tracker = "recent"):
            call ask_to_study(Jean) from _call_ask_to_study_5

            if _return:
                $ studying_Girl = Jean
        "Back":
            $ Character_picker_disabled = False
            $ belt_disabled = False
            
            return

    if _return:
        if Player.training:
            call actually_train(studying_Girl) from _call_actually_train_9
        elif Player.studying:
            call actually_study(studying_Girl) from _call_actually_study_12
    else:
        $ Player.studying = False
        $ Player.training = False

    if not renpy.get_screen("phone_screen"):
        $ Character_picker_disabled = False
        $ belt_disabled = False

    return

label ask_to_study(Girl):
    $ status = Girl.get_status()

    if Girl in Present:
        ch_Player "Wanna study together?"

        if status not in ["miffed", "mad", "heartbroken"] and not Girl.wants_alone_time and not Girl.History.check("studied_with_Player", tracker = "daily"):
            call expression f"{Girl.tag}_accept_study" from _call_expression_287
        else:
            if Girl.History.check("said_no_to_studying", tracker = "recent") >= 2:
                call change_Girl_stat(Girl, "love", -5) from _call_change_Girl_stat_995
                call change_Girl_stat(Girl, "trust", -5) from _call_change_Girl_stat_996
                
                call expression f"{Girl.tag}_reject_study_asked_twice" from _call_expression_288
            elif Girl.History.check("said_no_to_studying", tracker = "recent") == 1:
                call change_Girl_stat(Girl, "love", -2) from _call_change_Girl_stat_997

                call expression f"{Girl.tag}_reject_study_asked_once" from _call_expression_289
            else:
                call expression f"{Girl.tag}_reject_study" from _call_expression_290

            $ Girl.History.update("said_no_to_studying")

            return False
    else:
        call open_texts(Girl) from _call_open_texts_20
        call send_text(Girl, "hey, wanna study?") from _call_send_text_79

        if time_index == 3:
            if time_index not in Girl.schedule.keys() and approval_check(Girl, threshold = "talk_late") and not Girl.History.check("studied_with_Player", tracker = "daily"):
                call expression f"{Girl.tag}_accept_study_text" from _call_expression_291
            else:
                if Girl.History.check("said_too_late_to_text", tracker = "recent") >= 2:
                    call change_Girl_stat(Girl, "love", -5) from _call_change_Girl_stat_998
                    call change_Girl_stat(Girl, "trust", -5) from _call_change_Girl_stat_999

                    call expression f"{Girl.tag}_summon_reject_asked_twice" from _call_expression_293
                elif Girl.History.check("said_too_late_to_text", tracker = "recent") == 1:
                    call change_Girl_stat(Girl, "love", -2) from _call_change_Girl_stat_1000

                    call expression f"{Girl.tag}_summon_reject_asked_once" from _call_expression_294
                else:
                    call expression f"{Girl.tag}_summon_busy_late" from _call_expression_295

                $ Girl.History.update("said_too_late_to_text")

                $ phone_interactable = True 

                return False
        else:
            if time_index not in Girl.schedule.keys() and status not in ["miffed", "mad", "heartbroken"] and not Girl.wants_alone_time and not Girl.History.check("studied_with_Player", tracker = "daily"):
                call expression f"{Girl.tag}_accept_study_text" from _call_expression_296
            else:
                if Girl.History.check("said_no_to_studying", tracker = "recent") == 1:
                    call change_Girl_stat(Girl, "love", -5) from _call_change_Girl_stat_1001
                    
                    call expression f"{Girl.tag}_reject_study_asked_once_text" from _call_expression_297
                elif Girl.History.check("said_no_to_studying", tracker = "recent") > 1:
                    call change_Girl_stat(Girl, "love", -5) from _call_change_Girl_stat_1002
                    call change_Girl_stat(Girl, "trust", -5) from _call_change_Girl_stat_1003

                    call expression f"{Girl.tag}_reject_study_asked_twice_text" from _call_expression_298
                else:
                    call expression f"{Girl.tag}_reject_study_text" from _call_expression_299

                $ Girl.History.update("said_no_to_studying")

                $ phone_interactable = True 

                return False

        pause

        hide screen phone_screen

    return True

label actually_study(Girl):        
    hide screen phone_screen

    if Girl:
        $ Player.studying = Girl

        $ reset_behavior(Girl)

        $ Girl.studying = True

    if black_screen:
        $ fade_in_from_black(0.4)

    $ clock -= 1

    $ selected_Event = EventScheduler.choose_Event()

    if selected_Event:
        if Girl:
            if Girl not in Present:
                $ Girl.destination = Player.location

                if Girl.Outfit.name != Girl.Wardrobe.indoor_Outfit.name:
                    call set_Character_Outfits(Girl, instant = True) from _call_set_Character_Outfits_15    

                call Characters_arrive(Girl, invited = True) from _call_Characters_arrive

                $ Girl.location = Girl.destination
            else:
                if Girl.Outfit.name != Girl.Wardrobe.indoor_Outfit.name:
                    call set_Character_Outfits(Girl, instant = False) from _call_set_Character_Outfits_14

            call remove_everyone_but(Girl) from _call_remove_everyone_but_7
            
        call start_Event(selected_Event) from _call_start_Event_11
    else:
        $ fade_to_black(0.4)
        
        call expression f"chapter_{chapter}_season_{season}_studying_narrations" from _call_expression_300

        pause 2.0

        if clock > 0 or time_index == 3:
            $ fade_in_from_black(0.4)

label after_studying:
    if Player.studying in all_Girls:
        $ Player.studying.History.update("studied_with_Player")
        $ Player.studying.studying = False

        $ gained_XP = int(10*Player.studying.stat_modifier)
        $ Player.studying.XP += gained_XP

        if time_index in Player.studying.schedule.keys() and Player.studying.schedule[time_index][1] == "studying":
            $ del Player.studying.schedule[time_index]
        
        $ update_messages.append("{color=%s}%s{/color} gained {color=%s}%s XP{/color} from {color=%s}Studying{/color}" % (eval(f"{Player.studying.tag}_color"), Player.studying.name, "#feba00", gained_XP, "#feba00"))

    $ Player.History.update("studied")
    $ Player.studying = False

    $ gained_XP = int(10*Player.stat_modifier)
    $ Player.XP += gained_XP

    $ update_messages.append("{color=%s}%s{/color} gained {color=%s}%s XP{/color} from {color=%s}Studying{/color}" % ("#feba00", Player.first_name, "#feba00", gained_XP, "#feba00"))

    call check_for_Events(only_automatic = True) from _call_check_for_Events_18
    call move_location(Player.location) from _call_move_location_47

    return