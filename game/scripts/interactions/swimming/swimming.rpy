label swim:
    $ Character_picker_disabled = True
    $ belt_disabled = True

    $ Player.behavior = "swimming"
    
    $ renpy.dynamic(temp_Characters = Present[:])

    python:
        for C in all_NPCs:
            if C in temp_Characters:
                temp_Characters.remove(C)

    if temp_Characters:
        if len(temp_Characters) > 1:
            ch_Player "Do you all want to go for a swim?"
        else:
            ch_Player "Want to go for a swim, [temp_Characters[0].name]?"

    $ stable_swimming_Characters = temp_Characters[:]

    while temp_Characters:
        call ask_to_swim(temp_Characters[0]) from _call_ask_to_swim

        if not _return:
            $ stable_swimming_Characters.remove(temp_Characters[0])

        $ temp_Characters.remove(temp_Characters[0])

    call actually_swim(stable_swimming_Characters) from _call_actually_swim
        
    $ Character_picker_disabled = False
    $ belt_disabled = False

    return

label ask_to_swim(Girl):   
    $ status = Girl.get_status()

    if Girl.swimming_Outfit.name != Girl.indoor_Outfit.name and Girl.is_in_normal_mood() and approval_check(Girl, threshold = "friendship") and (not time_index >= 3 or approval_check(Girl, threshold = "talk_late")):
        call expression f"{Girl.tag}_accept_swim" from _call_expression_330
    else:
        if Girl.History.check("said_no_to_swimming", tracker = "recent") >= 2:
            call change_Girl_stat(Girl, "love", -5) from _call_change_Girl_stat_1018
            call change_Girl_stat(Girl, "trust", -5) from _call_change_Girl_stat_1019

            call expression f"{Girl.tag}_reject_swim_asked_twice" from _call_expression_331
        elif Girl.History.check("said_no_to_swimming", tracker = "recent") == 1:
            call change_Girl_stat(Girl, "love", -2) from _call_change_Girl_stat_1020

            call expression f"{Girl.tag}_reject_swim_asked_once" from _call_expression_332
        else:
            call expression f"{Girl.tag}_reject_swim" from _call_expression_333

        $ Girl.History.update("said_no_to_swimming")

        return False

    return True

label actually_swim(swimming_Characters):
    if swimming_Characters:
        python:
            for C in swimming_Characters:
                C.behavior = "swimming"

        call set_Character_Outfits(swimming_Characters, instant = False) from _call_set_Character_Outfits_18

    $ renpy.dynamic(temp_Characters = swimming_Characters[:])

    while temp_Characters:
        if temp_Characters[0].desire <= 50:
            call change_Girl_stat(temp_Characters[0], "desire", 5) from _call_change_Girl_stat_1021
        else:
            call change_Girl_stat(temp_Characters[0], "desire", 60 - temp_Characters[0].desire) from _call_change_Girl_stat_1022

        $ temp_Characters.remove(temp_Characters[0])

    if black_screen:
        $ fade_in_from_black(0.4)

    $ clock -= 1

    if swimming_Characters:
        pause 2.0

        python:
            for C in swimming_Characters:
                C.wet = True

        pause 2.0

    $ selected_Event = EventScheduler.choose_Event()

    if selected_Event:
        call start_Event(selected_Event) from _call_start_Event_13
    else:
        $ fade_to_black(0.4)
        
        call expression f"chapter_{chapter}_swimming_narrations" pass (swimming_Characters = swimming_Characters) from _call_expression_334

        pause 2.0

        if clock > 0 or time_index == 3:
            $ fade_in_from_black(0.4)

    call after_swimming from _call_after_swimming
    call check_for_Events(only_automatic = True) from _call_check_for_Events_20
    call move_location(Player.location) from _call_move_location_51

    return

label after_swimming:
    if swimming_Characters:
        python:
            for C in swimming_Characters:
                C.History.update("swam_with_Player")
                C.behavior = None

                for other_C in swimming_Characters:
                    if other_C != C:
                        if other_C not in C.likes.keys():
                            C.likes[other_C] = 0
                        
                        if C not in other_C.likes.keys():
                            other_C.likes[C] = 0

                        C.likes[other_C] += 10
                        other_C.likes[C] += 10

    $ Player.History.update("swam")
    $ Player.behavior = None
    $ Player.chlorine += 1

    return