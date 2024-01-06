label take_a_shower:
    $ Character_picker_disabled = True
    $ belt_disabled = True

    python:
        showering_Characters = []
        not_showering_Characters = []

        for G in active_Companions:
            if G.location == Player.location:
                if Player.location == "bg_lockers" and time_index in G.schedule and (G.schedule[time_index] == ["bg_lockers", "showering"] or G.schedule[time_index] == ["bg_lockers", "changing"]):
                    showering_Characters.append(G)
                elif G.behavior == "showering" and Player.location == "bg_lockers" and approval_check(G, threshold = "friendship"):
                    showering_Characters.append(G)
                elif "bg_shower" in Player.location and approval_check(G, threshold = "see_pussy"):
                    showering_Characters.append(G)
                else:
                    not_showering_Characters.append(G)

                # if G in showering_Characters and not are_Characters_friends(showering_Characters + G):
                #     showering_Characters.remove(G)
                #     not_showering_Characters.append(G)

    if not_showering_Characters:
        python:
            for C in not_showering_Characters:
                if C in Party:
                    Party.remove(C)

        $ set_Character_locations(not_showering_Characters)
        $ set_Character_behavior(not_showering_Characters)

        call Characters_leave(not_showering_Characters[:]) from _call_Characters_leave_5
        call set_Character_Outfits(not_showering_Characters) from _call_set_Character_Outfits_11

    if showering_Characters:
        $ renpy.random.shuffle(showering_Characters)

        python:
            for C in showering_Characters:
                C.behavior = "showering"

        if Player.location == "bg_lockers":
            call set_Character_Outfits(showering_Characters, instant = False) from _call_set_Character_Outfits_12
        elif "bg_shower" in Player.location:
            $ renpy.dynamic(temp_Characters = showering_Characters[:])

            while temp_Characters:
                call change_Outfit(temp_Characters[0], temp_Characters[0].Wardrobe.Outfits["Nude"]) from _call_change_Outfit_42
                
                $ temp_Characters.remove(temp_Characters[0])

        if black_screen:
            $ fade_in_from_black(0.4)
            
        pause 2.0

    if "bg_shower" in Player.location:
        $ Player.give_trait("naked")
        $ Player.give_trait("cock_out")

        if showering_Characters:
            $ renpy.dynamic(temp_Characters = showering_Characters[:])

            while temp_Characters:
                call expression f"{temp_Characters[0].tag}_seeing_penis" from _call_expression_89
                    
                $ temp_Characters[0].History.update("seen_Player_naked")

                $ temp_Characters.remove(temp_Characters[0])

        $ shower_open = False

        pause 1.0

    $ Player.behavior = "showering"
    $ shower_steam = True

    $ Player.sweat = 0
    $ Player.chlorine = 0
    $ Player.remove_trait("spunk")
    $ Player.remove_trait("saliva")
    $ Player.remove_trait("grool")
    $ Player.remove_trait("dirty_cock")
    
    if showering_Characters:
        python:
            for G in showering_Characters:
                G.give_trait("wet")

                for location in G.spunk.keys():
                    G.spunk[location] = 0

    $ renpy.dynamic(temp_Characters = showering_Characters[:])

    while temp_Characters:
        if not temp_Characters[0].History.check("showered_with_Player", tracker = "recent"):
            $ temp_Characters[0].History.update("showered_with_Player")

        $ temp_Characters.remove(temp_Characters[0])
            
    pause 5.0

    $ selected_Event = EventScheduler.choose_Event()

    if selected_Event:
        call start_Event(selected_Event) from _call_start_Event_9

        $ Player.behavior = None
    else:
        $ fade_to_black(0.4)

        pause 2.0

        $ Player.behavior = None

        $ fade_in_from_black(0.4)

    pause 1.0

    if "bg_shower" in Player.location:
        $ shower_open = True

        pause 1.0

    if showering_Characters:
        $ renpy.dynamic(temp_Characters = showering_Characters[:])

        while temp_Characters:
            # call try_on(temp_Characters[0], temp_Characters[0].Wardrobe.Clothes["towel"]) from _call_try_on_14

            $ temp_Characters[0].behavior = None

            if time_index in temp_Characters[0].schedule.keys() and temp_Characters[0].schedule[time_index][1] == "showering":
                $ del temp_Characters[0].schedule[time_index]

            $ temp_Characters.remove(temp_Characters[0])

        pause 1.0

    $ Player.History.update("showered")
    $ Player.remove_trait("naked")
    $ Player.remove_trait("cock_out")

    if time_index not in [0, 3] or Player.History.check("showered", tracker = "recent") > 1:
        $ clock -= 1

    if clock == 0:
        call check_for_Events(only_automatic = True) from _call_check_for_Events_17
        
    call move_location(Player.location) from _call_move_location_49

    return