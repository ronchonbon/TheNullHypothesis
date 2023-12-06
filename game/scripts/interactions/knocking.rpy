label Player_knocks(host):
    $ Character_picker_active = False
    $ belt_disabled = True

    if Player.location != "bg_girls_hallway":
        call set_the_scene(location = "bg_girls_hallway") from _call_set_the_scene_300

    call knock_on_door(times = 2) from _call_knock_on_door_33

    $ Present = get_Present(location = host.home)[0]

    if host not in Present:
        "There doesn't seem to be anyone home."

        if host in Keys:
            "You let yourself in."

            call move_location(host.home) from _call_move_location_56
        else:
            call move_location("bg_girls_hallway") from _call_move_location_42
        
    $ sorted_Characters = sort_Characters_by_approval(Present[:])[:]

    if host in sorted_Characters:
        $ sorted_Characters.remove(host)
        $ sorted_Characters.insert(0, host)
        
    $ Present = get_Present(location = Player.location)[0]

    if time_index == 3 and not approval_check(sorted_Characters[0], threshold = "talk_late"):
        if sorted_Characters[0].History.check("said_too_late_to_talk", tracker = "recent") >= 2:
            call change_Character_stat(sorted_Characters[0], "love", -5) from _call_change_Character_stat_982
            call change_Character_stat(sorted_Characters[0], "trust", -5) from _call_change_Character_stat_983

            call expression f"{sorted_Characters[0].tag}_greets_Player_knocking_late_asked_twice" from _call_expression_250
        elif sorted_Characters[0].History.check("said_too_late_to_talk", tracker = "recent") == 1:
            call change_Character_stat(sorted_Characters[0], "love", -2) from _call_change_Character_stat_984

            call expression f"{sorted_Characters[0].tag}_greets_Player_knocking_late_asked_once" from _call_expression_251
        else:
            call expression f"{sorted_Characters[0].tag}_greets_Player_knocking_late" from _call_expression_252

        $ sorted_Characters[0].History.update("said_too_late_to_talk")
                
        call move_location("bg_girls_hallway") from _call_move_location_43
    else:
        $ status = sorted_Characters[0].get_status()
        
        if status:
            call expression f"{sorted_Characters[0].tag}_greets_Player_knocking_{status}" pass (welcoming_Characters = sorted_Characters) from _call_expression_253
        elif approval_check(sorted_Characters[0], threshold = "love"):
            call expression f"{sorted_Characters[0].tag}_greets_Player_knocking_love" pass (welcoming_Characters = sorted_Characters) from _call_expression_254
        elif sorted_Characters[0] in Partners:
            call expression f"{sorted_Characters[0].tag}_greets_Player_knocking_relationship" pass (welcoming_Characters = sorted_Characters) from _call_expression_255
        else:
            if sorted_Characters[0].History.check("rejected_knock_on_door", tracker = "recent") > 2:
                call change_Character_stat(sorted_Characters[0], "love", -5) from _call_change_Character_stat_985
                call change_Character_stat(sorted_Characters[0], "trust", -5) from _call_change_Character_stat_986

                if renpy.random.random() > 0.25:
                    call expression f"{sorted_Characters[0].tag}_greets_Player_knocking_reject_asked_twice" from _call_expression_257
                else:
                    "You are being ignored."
            elif sorted_Characters[0].History.check("rejected_knock_on_door", tracker = "recent") == 2:
                call change_Character_stat(sorted_Characters[0], "love", -5) from _call_change_Character_stat_987
                call change_Character_stat(sorted_Characters[0], "trust", -5) from _call_change_Character_stat_988

                call expression f"{sorted_Characters[0].tag}_greets_Player_knocking_reject_asked_twice" from _call_expression_258
            elif sorted_Characters[0].History.check("rejected_knock_on_door", tracker = "recent") == 1:
                call change_Character_stat(sorted_Characters[0], "love", -2) from _call_change_Character_stat_989

                call expression f"{sorted_Characters[0].tag}_greets_Player_knocking_reject_asked_once" from _call_expression_259
            else:
                call expression f"{sorted_Characters[0].tag}_greets_Player_knocking_reject" pass (welcoming_Characters = sorted_Characters) from _call_expression_260

            $ sorted_Characters[0].History.update("rejected_knock_on_door")
            
            call move_location("bg_girls_hallway") from _call_move_location_44

    if Player.location != host.home:
        call set_the_scene(location = host.home) from _call_set_the_scene_301

    $ Character_picker_active = True
    $ belt_disabled = False

    return