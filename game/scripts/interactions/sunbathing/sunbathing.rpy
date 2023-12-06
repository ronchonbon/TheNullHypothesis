label sunbathe:
    $ Character_picker_disabled = True
    $ belt_disabled = True

    $ Player.behavior = "sunbathing"
    
    $ renpy.dynamic(temp_Characters = Present[:])

    python:
        for C in all_NPCs:
            if C in temp_Characters:
                temp_Characters.remove(C)

    if temp_Characters:
        if len(temp_Characters) > 1:
            ch_Player "Do you all want to sunbathe?"
        else:
            ch_Player "Want to sunbathe, [temp_Characters[0].name]?"

    $ stable_sunbathing_Characters = temp_Characters[:]

    while temp_Characters:
        call ask_to_sunbathe(temp_Characters[0]) from _call_ask_to_sunbathe

        if not _return:
            $ stable_sunbathing_Characters.remove(temp_Characters[0])

        $ temp_Characters.remove(temp_Characters[0])

    call actually_sunbathe(stable_sunbathing_Characters) from _call_actually_sunbathe
        
    $ Character_picker_disabled = False
    $ belt_disabled = False

    return

label ask_to_sunbathe(Character):   
    $ status = Character.get_status()

    if Character.is_in_normal_mood() and approval_check(Character, threshold = "dating"):
        call expression f"{Character.tag}_accept_sunbathe" from _call_expression_325
    else:
        if Character.History.check("said_no_to_sunbathing", tracker = "recent") >= 2:
            call change_Character_stat(Character, "love", -5) from _call_change_Character_stat_1013
            call change_Character_stat(Character, "trust", -5) from _call_change_Character_stat_1014

            call expression f"{Character.tag}_reject_sunbathe_asked_twice" from _call_expression_326
        elif Character.History.check("said_no_to_sunbathing", tracker = "recent") == 1:
            call change_Character_stat(Character, "love", -2) from _call_change_Character_stat_1015

            call expression f"{Character.tag}_reject_sunbathe_asked_once" from _call_expression_327
        else:
            call expression f"{Character.tag}_reject_sunbathe" from _call_expression_328

        $ Character.History.update("said_no_to_sunbathing")

        return False

    return True

label actually_sunbathe(sunbathing_Characters):
    if sunbathing_Characters:
        pause 1.0

        python:
            for C in sunbathing_Characters:
                C.behavior = "sunbathing"

        call set_Character_Outfits(sunbathing_Characters, instant = False) from _call_set_Character_Outfits_17

        pause 1.0

    if black_screen:
        $ fade_in_from_black(0.4)

    $ clock -= 1

    $ selected_Event = EventScheduler.choose_Event()

    if selected_Event:
        call start_Event(selected_Event) from _call_start_Event_12
    else:
        $ fade_to_black(0.4)
        
        call expression f"chapter_{chapter}_sunbathing_narrations" pass (sunbathing_Characters = sunbathing_Characters) from _call_expression_329

        pause 2.0

        if clock > 0 or time_index == 3:
            $ fade_in_from_black(0.4)

    call after_sunbathing from _call_after_sunbathing
    call check_for_Events(only_automatic = True) from _call_check_for_Events_19
    call move_location(Player.location) from _call_move_location_50

    return

label after_sunbathing:
    if sunbathing_Characters:
        python:
            for C in sunbathing_Characters:
                if C.Clothes["bodysuit"].string and "swimsuit" in C.Clothes["bodysuit"].string:
                    C.tan_lines["full"] = C.Clothes["bodysuit"].string
                    C.History.update("tan_lines_full")

                if C.Clothes["bra"].string and "bikini" in C.Clothes["bra"].string:
                    C.tan_lines["top"] = C.Clothes["bra"].string
                    C.History.update("tan_lines_top")

                if C.Clothes["underwear"].string and "bikini" in C.Clothes["underwear"].string:
                    C.tan_lines["bottom"] = C.Clothes["underwear"].string
                    C.History.update("tan_lines_bottom")

                C.History.update("tanned_with_Player")
                C.behavior = None

                for other_C in sunbathing_Characters:
                    if other_C != C:
                        if other_C not in C.likes.keys():
                            C.likes[other_C] = 0
                        
                        if C not in other_C.likes.keys():
                            other_C.likes[C] = 0

                        C.likes[other_C] += 10
                        other_C.likes[C] += 10

    $ Player.History.update("sunbathed")
    $ Player.behavior = None

    return