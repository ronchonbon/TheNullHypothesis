label getting_kicked_out(Character):
    $ Character_picker_disabled = True

    if not Character.status["miffed"] and not Character.status["mad"]:
        $ Character.give_status("miffed")

    call reset_all_interfaces from _call_reset_all_interfaces_2

    # pause 1.0

    if Player.location == Character.home:
        $ Character.wants_alone_time = 1

        $ Character_picker_disabled = False

        call move_location("bg_girls_hallway") from _call_move_location_40
    else:
        call remove_Characters(Character) from _call_remove_Characters_233

        $ Character_picker_disabled = False
        
        call move_location(Player.location) from _call_move_location_31

    return