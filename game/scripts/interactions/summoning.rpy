label summon(Character):
    if Player.location in bedrooms or "bg_shower" in Player.location:
        if Player.location in [Character.home, f"bg_shower_{Character.tag}"]:
            $ location = "your room"
        else:
            $ location = location_conversational_names[Player.location]
    else:
        $ location = location_conversational_names[Player.location]

    call send_text(Character, f"I'm in {location}") from _call_send_text_80

    if Character.wants_alone_time:
        call expression f"{Character.tag}_summon_busy" from _call_expression_301

        $ Character.History.update("said_no_to_summon")

        return

    if time_index == 3 and not approval_check(Character, threshold = "talk_late"):
        if Character.History.check("said_too_late_to_text", tracker = "recent") >= 2:
            call change_Character_stat(Character, "love", -small_stat) from _call_change_Character_stat_1004
            call change_Character_stat(Character, "trust", -small_stat) from _call_change_Character_stat_1005

            call expression f"{Character.tag}_summon_reject_asked_twice" from _call_expression_303
        elif Character.History.check("said_too_late_to_text", tracker = "recent") == 1:
            call change_Character_stat(Character, "love", -tiny_stat) from _call_change_Character_stat_1006

            call expression f"{Character.tag}_summon_reject_asked_once" from _call_expression_304
        else:
            call expression f"{Character.tag}_summon_busy_late" from _call_expression_305

        $ Character.History.update("said_too_late_to_text")

        return
    else:
        $ status = Character.get_status()

        if status == "mad":
            call expression f"{Character.tag}_summon_reject_mad" from _call_expression_306

            $ Character.History.update("said_no_to_summon")

            return
        # elif status:
        #     call expression f"{Character.tag}_summon_{status}" from _call_expression_307
        elif time_index not in Character.schedule.keys() or (approval_check(Character, threshold = "shirk_responsibilities")):
            if approval_check(Character, threshold = "love"):
                call expression f"{Character.tag}_summon_in_love" from _call_expression_308
            elif Character in Partners:
                call expression f"{Character.tag}_summon_in_relationship" from _call_expression_309
            elif approval_check(Character, threshold = "follow"):
                call expression f"{Character.tag}_summon_love_and_trust" from _call_expression_310
            elif approval_check(Character, "love", threshold = eval(f"{Character.tag}_thresholds['follow'][0]")):
                call expression f"{Character.tag}_summon_love" from _call_expression_311
            elif approval_check(Character, "trust", threshold = eval(f"{Character.tag}_thresholds['follow'][1]")):
                call expression f"{Character.tag}_summon_trust" from _call_expression_312
            elif approval_check(Character, threshold = "temporary_follow") and renpy.random.random() > 0.5:
                call expression f"{Character.tag}_summon_temporary" from _call_expression_313
            else:
                if Character.History.check("said_no_to_summon", tracker = "recent") >= 2:
                    call change_Character_stat(Character, "love", -small_stat) from _call_change_Character_stat_1007
                    call change_Character_stat(Character, "trust", -small_stat) from _call_change_Character_stat_1008

                    call expression f"{Character.tag}_summon_reject_asked_twice" from _call_expression_315
                elif Character.History.check("said_no_to_summon", tracker = "recent") == 1:
                    call change_Character_stat(Character, "love", -tiny_stat) from _call_change_Character_stat_1009

                    call expression f"{Character.tag}_summon_reject_asked_once" from _call_expression_316
                else:
                    call expression f"{Character.tag}_summon_reject" from _call_expression_317

                $ Character.History.update("said_no_to_summon")

                return
        else:
            call expression f"{Character.tag}_summon_busy" from _call_expression_318

            $ Character.History.update("said_no_to_summon")

            return

    hide screen phone_screen

    $ Character.original_location = Character.location
    $ Character.destination = Player.location

    $ reset_behavior(Character)
    
    call set_Character_Outfits(Character) from _call_set_Character_Outfits_16
    call Characters_arrive(Character, invited = True) from _call_Characters_arrive_1
    call move_location(Player.location) from _call_move_location_32

    return

label dismiss(Character):
    if Character in all_Companions:
        if approval_check(Character, threshold = "follow") and Player.location != Character.home:
            call expression f"{Character.tag}_dismiss_accept" from _call_expression_319

            if _return:
                call remove_Characters(Character) from _call_remove_Characters_235
        else:
            if Character.History.check("said_no_to_dismiss", tracker = "recent") >= 2:
                call change_Character_stat(Character, "love", -small_stat) from _call_change_Character_stat_1010
                call change_Character_stat(Character, "trust", -small_stat) from _call_change_Character_stat_1011

                call expression f"{Character.tag}_dismiss_reject_asked_twice" from _call_expression_321
            elif Character.History.check("said_no_to_dismiss", tracker = "recent") == 1:
                call change_Character_stat(Character, "love", -tiny_stat) from _call_change_Character_stat_1012

                call expression f"{Character.tag}_dismiss_reject_asked_once" from _call_expression_322
            else:
                call expression f"{Character.tag}_dismiss_reject" from _call_expression_323

            if _return:
                $ Character.History.update("said_no_to_dismiss")
    else:
        call expression f"{Character.tag}_dismiss" from _call_expression_324

        if _return:
            call remove_Characters(Character) from _call_remove_Characters_236

    if Character.location != Player.location:
        call move_location(Player.location) from _call_move_location_33
        
    return