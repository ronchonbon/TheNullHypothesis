label getting_kicked_out(Girl):
    $ Character_picker_disabled = True

    if not Girl.status["miffed"] and not Girl.status["mad"]:
        $ Girl.give_status("miffed")

    call reset_all_interfaces from _call_reset_all_interfaces_2

    pause 1.0

    if Player.location == Girl.home:
        $ Girl.wants_alone_time = 1

        $ Character_picker_disabled = False

        call move_location("bg_girls_hallway") from _call_move_location_40
    else:
        call remove_Characters(Girl) from _call_remove_Characters_233

        $ Character_picker_disabled = False
        
        call move_location(Player.location) from _call_move_location_31

    return