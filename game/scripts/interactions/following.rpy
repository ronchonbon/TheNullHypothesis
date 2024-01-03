label start_following(Character):
    ch_Player "Hey, mind following me around for a bit?"

    $ status = Character.get_status()

    if status == "mad":
        call expression f"{Character.tag}_follow_reject_mad" from _call_expression_214

        $ Character.History.update("said_no_to_following")

        return
    elif time_index == 3 and not approval_check(Character, threshold = "talk_late"):
        if Character.History.check("said_no_to_following", tracker = "recent") >= 2:
            call change_Character_stat(Character, "love", -small_stat) from _call_change_Character_stat_970
            call change_Character_stat(Character, "trust", -small_stat) from _call_change_Character_stat_971

            call expression f"{Character.tag}_follow_reject_asked_twice" from _call_expression_216
        elif Character.History.check("said_no_to_following", tracker = "recent") == 1:
            call change_Character_stat(Character, "love", -tiny_stat) from _call_change_Character_stat_972

            call expression f"{Character.tag}_follow_reject_asked_once" from _call_expression_217
        else:
            call expression f"{Character.tag}_busy_late" from _call_expression_218

        $ Character.History.update("said_no_to_following")

        return
    elif time_index not in Character.schedule.keys() or (approval_check(Character, threshold = "shirk_responsibilities")):
        if approval_check(Character, threshold = "love"):
            call expression f"{Character.tag}_follow_in_love" from _call_expression_219
        elif Character in Partners:
            call expression f"{Character.tag}_follow_in_relationship" from _call_expression_220
        elif approval_check(Character, threshold = "talk_late"):
            call expression f"{Character.tag}_follow_love_and_trust" from _call_expression_221
        elif approval_check(Character, "love", threshold = eval(f"{Character.tag}_thresholds['follow'][0]")) and approval_check(Character, threshold = "talk_late"):
            call expression f"{Character.tag}_follow_love" from _call_expression_222
        elif approval_check(Character, "trust", threshold = eval(f"{Character.tag}_thresholds['follow'][1]")) and approval_check(Character, threshold = "talk_late"):
            call expression f"{Character.tag}_follow_trust" from _call_expression_223
        elif approval_check(Character, threshold = "talk_late") and renpy.random.random() > 0.5:
            call expression f"{Character.tag}_follow_temporary" from _call_expression_224
        else:
            if Character.History.check("said_no_to_following", tracker = "recent") >= 2:
                call change_Character_stat(Character, "love", -small_stat) from _call_change_Character_stat_973
                call change_Character_stat(Character, "trust", -small_stat) from _call_change_Character_stat_974

                call expression f"{Character.tag}_follow_reject_asked_twice" from _call_expression_226
            elif Character.History.check("said_no_to_following", tracker = "recent") == 1:                    
                call change_Character_stat(Character, "love", -tiny_stat) from _call_change_Character_stat_975

                call expression f"{Character.tag}_follow_reject_asked_once" from _call_expression_227
            else:
                call expression f"{Character.tag}_follow_reject" from _call_expression_228

            $ Character.History.update("said_no_to_following")

            return
    else:
        call expression f"{Character.tag}_follow_busy" from _call_expression_229

        $ Character.History.update("said_no_to_following")

        return

    $ reset_behavior(Character)

    $ Character.original_location = Character.location

    $ Party.append(Character)

    return

label stop_following(Character):
    ch_Player "You can stop following me now."

    $ Party.remove(Character)

    $ status = Character.get_status()

    if status:
        call expression f"{Character.tag}_stop_follow_{status}" from _call_expression_230
    elif approval_check(Character, threshold = "love"):
        if renpy.random.random() > 0.5:
            call expression f"{Character.tag}_stop_follow_love" from _call_expression_231
        else:
            call expression f"{Character.tag}_stop_follow_love_stay" from _call_expression_232

            return
    else:
        call expression f"{Character.tag}_stop_follow" from _call_expression_233

    if Character.location != Character.original_location:
        hide screen interactions_screen

        call send_Characters(Character, Character.original_location) from _call_send_Characters_227

        $ belt_hidden = False

    return