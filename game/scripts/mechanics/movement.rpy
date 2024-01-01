label travel(destination):
    hide screen phone_screen
    hide screen Player_menu
    
    $ Character_picker_disabled = True
    $ belt_disabled = True

    $ Player.destination = destination
    
    if Player.destination in public_locations and Party:
        $ someone_changed = False

        $ renpy.dynamic(temp_Characters = Party[:])

        while temp_Characters:
            if destination in all_Companions:
                $ temp_Characters[0].destination = destination.home
                $ temp_Characters[0].location = destination.home
            else:
                $ temp_Characters[0].destination = destination
                $ temp_Characters[0].location = destination

            if "public" not in temp_Characters[0].Outfit.flags:
                call expression f"{temp_Characters[0].tag}_Party_change_into_public_Outfit" from _call_expression_378

                pause 1.0

                call set_Character_Outfits(temp_Characters, instant = False) from _call_set_Character_Outfits_26

                $ someone_changed = True

            $ locations = list(temp_Characters[0].spunk.keys())

            while locations:
                if temp_Characters[0].spunk[locations[0]]:
                    call clean_cum(temp_Characters[0]) from _call_clean_cum_7

                    $ someone_changed = True

                $ locations.remove(locations[0])

            $ temp_Characters.remove(temp_Characters[0])

        if someone_changed:
            "Looks like everyone's ready to go."

    $ stack_depth = renpy.call_stack_depth()

    while stack_depth > 0:
        $ stack_depth -= 1

        $ renpy.pop_call()

    if clock <= 0 and time_index < 3:
        call wait_around(fade = False, silent = True) from _call_wait_around_29

    call move_location(Player.destination) from _call_move_location_54

    return

label move_location(destination):
    call reset_all_interfaces from _call_reset_all_interfaces

    if destination in bedrooms and destination != Player.home:
        python:
            for C in all_Companions:
                if C.tag in destination:
                    destination = C

                    break

    $ reset_behavior(Player)

    $ Player.destination = destination
    
    if destination == "bg_campus":
        jump campus
    elif destination == "bg_girls_hallway":
        jump girls_hallway
    elif destination == "bg_hallway":
        jump hallway
    elif destination == Player.home:
        jump Player_room
    elif destination in all_Companions:
        $ current_bedroom = destination
        $ Player.destination = current_bedroom.home

        jump Character_room
    elif "bg_shower" in destination:
        jump shower
    elif destination == "bg_classroom":
        jump classroom
    elif destination == "bg_danger":
        jump danger_room
    elif destination == "bg_pool":
        jump pool
    elif destination == "bg_lockers":
        jump lockers
    elif destination == "bg_study":
        jump study
    elif destination == "bg_mall":
        jump mall