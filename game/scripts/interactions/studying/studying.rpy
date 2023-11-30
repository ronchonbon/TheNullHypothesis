label study_session:
    $ Character_picker_disabled = True
    $ belt_disabled = True

    $ Player.behavior = "studying"

    $ studying_Character = None

    menu:
        "Study on your own":
            $ _return = True
        "Study with [Rogue.name]" if not Rogue.History.check("studied_with_Player", tracker = "daily") and Rogue in Present and not Rogue.History.check("said_no_to_studying", tracker = "recent") > 2:
            call ask_to_study(Rogue) from _call_ask_to_study

            if _return:
                $ studying_Character = Rogue
        "Invite [Rogue.name] to study" if not Rogue.History.check("studied_with_Player", tracker = "daily") and Rogue in Contacts and Rogue in active_Companions and Rogue not in Present and Rogue.location != "hold" and Player.location not in [Laura.home, Jean.home] and not Rogue.History.check("said_no_to_studying", tracker = "recent") > 2 and not Rogue.History.check("said_goodnight", tracker = "recent"):
            call ask_to_study(Rogue) from _call_ask_to_study_1

            if _return:
                $ studying_Character = Rogue
        "Study with [Laura.name]" if not Laura.History.check("studied_with_Player", tracker = "daily") and Laura in Present and not Laura.History.check("said_no_to_studying", tracker = "recent") > 2:
            call ask_to_study(Laura) from _call_ask_to_study_2

            if _return:
                $ studying_Character = Laura
        "Invite [Laura.name] to study" if not Laura.History.check("studied_with_Player", tracker = "daily") and Laura in Contacts and Laura in active_Companions and Laura not in Present and Laura.location != "hold" and Player.location not in [Rogue.home, Jean.home] and not Laura.History.check("said_no_to_studying", tracker = "recent") > 2 and not Laura.History.check("said_goodnight", tracker = "recent"):
            call ask_to_study(Laura) from _call_ask_to_study_3

            if _return:
                $ studying_Character = Laura
        "Study with [Jean.name]" if not Jean.History.check("studied_with_Player", tracker = "daily") and Jean in Present and not Jean.History.check("said_no_to_studying", tracker = "recent") > 2:
            call ask_to_study(Jean) from _call_ask_to_study_4

            if _return:
                $ studying_Character = Jean
        "Invite [Jean.name] to study" if not Jean.History.check("studied_with_Player", tracker = "daily") and Jean in Contacts and Jean in active_Companions and Jean not in Present and Jean.location != "hold" and Player.location not in [Rogue.home, Laura.home] and not Jean.History.check("said_no_to_studying", tracker = "recent") > 2 and not Jean.History.check("said_goodnight", tracker = "recent"):
            call ask_to_study(Jean) from _call_ask_to_study_5

            if _return:
                $ studying_Character = Jean
        "Back":
            $ Character_picker_disabled = False
            $ belt_disabled = False
            
            return

    if _return:
        if Player.behavior == "training":
            call actually_train(studying_Character) from _call_actually_train_9
        elif Player.behavior == "studying":
            call actually_study(studying_Character) from _call_actually_study_12
    else:
        $ reset_behavior(Player)

    if not renpy.get_screen("phone_screen"):
        $ Character_picker_disabled = False
        $ belt_disabled = False

    return

label ask_to_study(Companion):
    $ status = Companion.get_status()

    if Companion in Present:
        ch_Player "Wanna study together?"

        if Companion.is_in_normal_mood() and not Companion.History.check("studied_with_Player", tracker = "daily"):
            call expression f"{Companion.tag}_accept_study" from _call_expression_287
        else:
            if Companion.History.check("said_no_to_studying", tracker = "recent") >= 2:
                call change_Companion_stat(Companion, "love", -5) from _call_change_Companion_stat_995
                call change_Companion_stat(Companion, "trust", -5) from _call_change_Companion_stat_996
                
                call expression f"{Companion.tag}_reject_study_asked_twice" from _call_expression_288
            elif Companion.History.check("said_no_to_studying", tracker = "recent") == 1:
                call change_Companion_stat(Companion, "love", -2) from _call_change_Companion_stat_997

                call expression f"{Companion.tag}_reject_study_asked_once" from _call_expression_289
            else:
                call expression f"{Companion.tag}_reject_study" from _call_expression_290

            $ Companion.History.update("said_no_to_studying")

            return False
    else:
        call open_texts(Companion) from _call_open_texts_20
        call send_text(Companion, "hey, wanna study?") from _call_send_text_79

        if time_index == 3:
            if time_index not in Companion.schedule.keys() and approval_check(Companion, threshold = "talk_late") and not Companion.History.check("studied_with_Player", tracker = "daily"):
                call expression f"{Companion.tag}_accept_study_text" from _call_expression_291
            else:
                if Companion.History.check("said_too_late_to_text", tracker = "recent") >= 2:
                    call change_Companion_stat(Companion, "love", -5) from _call_change_Companion_stat_998
                    call change_Companion_stat(Companion, "trust", -5) from _call_change_Companion_stat_999

                    call expression f"{Companion.tag}_summon_reject_asked_twice" from _call_expression_293
                elif Companion.History.check("said_too_late_to_text", tracker = "recent") == 1:
                    call change_Companion_stat(Companion, "love", -2) from _call_change_Companion_stat_1000

                    call expression f"{Companion.tag}_summon_reject_asked_once" from _call_expression_294
                else:
                    call expression f"{Companion.tag}_summon_busy_late" from _call_expression_295

                $ Companion.History.update("said_too_late_to_text")

                $ phone_interactable = True 

                return False
        else:
            if time_index not in Companion.schedule.keys() and Companion.is_in_normal_mood() and not Companion.History.check("studied_with_Player", tracker = "daily"):
                call expression f"{Companion.tag}_accept_study_text" from _call_expression_296
            else:
                if Companion.History.check("said_no_to_studying", tracker = "recent") >= 2:
                    call change_Companion_stat(Companion, "love", -5) from _call_change_Companion_stat_1002
                    call change_Companion_stat(Companion, "trust", -5) from _call_change_Companion_stat_1003

                    call expression f"{Companion.tag}_reject_study_asked_twice_text" from _call_expression_298
                elif Companion.History.check("said_no_to_studying", tracker = "recent") == 1:
                    call change_Companion_stat(Companion, "love", -2) from _call_change_Companion_stat_1001
                    
                    call expression f"{Companion.tag}_reject_study_asked_once_text" from _call_expression_297
                else:
                    call expression f"{Companion.tag}_reject_study_text" from _call_expression_299

                $ Companion.History.update("said_no_to_studying")

                $ phone_interactable = True 

                return False

        pause

        hide screen phone_screen

    return True

label actually_study(Companion):        
    hide screen phone_screen

    if Companion:
        $ Player.behavior = "studying" 
        $ Player.behavior_Partners = [Companion]

        $ Companion.behavior = "studying"

    if black_screen:
        $ fade_in_from_black(0.4)

    $ clock -= 1

    $ selected_Event = EventScheduler.choose_Event()

    if selected_Event:
        if Companion:
            if Companion not in Present:
                $ Companion.destination = Player.location

                if Companion.Outfit.name != Companion.Wardrobe.indoor_Outfit.name:
                    call set_Character_Outfits(Companion, instant = True) from _call_set_Character_Outfits_15    

                call Characters_arrive(Companion, invited = True) from _call_Characters_arrive

                $ Companion.location = Companion.destination
            else:
                if Companion.Outfit.name != Companion.Wardrobe.indoor_Outfit.name:
                    call set_Character_Outfits(Companion, instant = False) from _call_set_Character_Outfits_14

            call remove_everyone_but(Companion) from _call_remove_everyone_but_7
            
        call start_Event(selected_Event) from _call_start_Event_11
    else:
        $ fade_to_black(0.4)
        
        call expression f"chapter_{chapter}_season_{season}_studying_narrations" from _call_expression_300

        pause 2.0

        if clock > 0 or time_index == 3:
            $ fade_in_from_black(0.4)

    call after_studying from _call_after_studying
    call check_for_Events(only_automatic = True) from _call_check_for_Events_18
    call move_location(Player.location) from _call_move_location_47

    return

label after_studying:
    if Player.behavior_Partners:
        python:
            for C in Player.behavior_Partners:
                C.History.update("studied_with_Player")
                C.behavior = None

                gained_XP = int(10*C.stat_modifier)
                C.XP += gained_XP

                if time_index in C.schedule.keys() and C.schedule[time_index][1] == "studying":
                    del C.schedule[time_index]
                
                update_messages.append("{color=%s}%s{/color} gained {color=%s}%s XP{/color} from {color=%s}Studying{/color}" % (eval(f"{C.tag}_color"), C.name, "#feba00", gained_XP, "#feba00"))

    $ Player.History.update("studied")
    $ Player.behavior = None

    $ gained_XP = int(10*Player.stat_modifier)
    $ Player.XP += gained_XP

    $ update_messages.append("{color=%s}%s{/color} gained {color=%s}%s XP{/color} from {color=%s}Studying{/color}" % ("#feba00", Player.first_name, "#feba00", gained_XP, "#feba00"))

    return