label take_a_shower:
    $ Character_picker_disabled = True
    $ belt_disabled = True

    python:
        showering_Companions = []
        not_showering_Companions = []

        for G in active_Companions:
            if G.location == Player.location:
                if Player.location == "bg_lockers" and time_index in G.schedule and (G.schedule[time_index] == ["bg_lockers", "showering"] or G.schedule[time_index] == ["bg_lockers", "changing"]):
                    showering_Companions.append(G)
                elif G.behavior == "showering" and Player.location == "bg_lockers" and approval_check(G, threshold = "friendship"):
                    showering_Companions.append(G)
                elif "bg_shower" in Player.location and approval_check(G, threshold = "see_pussy"):
                    showering_Companions.append(G)
                else:
                    not_showering_Companions.append(G)

                # if G in showering_Companions and not are_Characters_friends(showering_Companions + G):
                #     showering_Companions.remove(G)
                #     not_showering_Companions.append(G)

    if not_showering_Companions:
        python:
            for C in not_showering_Companions:
                if C in Party:
                    Party.remove(C)

        $ set_Character_locations(not_showering_Companions)
        $ set_Character_behavior(not_showering_Companions)

        call Characters_leave(not_showering_Companions[:]) from _call_Characters_leave_5
        call set_Character_Outfits(not_showering_Companions) from _call_set_Character_Outfits_11

    if showering_Companions:
        $ renpy.random.shuffle(showering_Companions)

        python:
            for C in showering_Companions:
                C.behavior = "showering"

        if Player.location == "bg_lockers":
            call set_Character_Outfits(showering_Companions, instant = False) from _call_set_Character_Outfits_12
        elif "bg_shower" in Player.location:
            $ temp_showering_Companions = showering_Companions[:]

            while temp_showering_Companions:
                call change_Outfit(temp_showering_Companions[0], temp_showering_Companions[0].Wardrobe.Outfits["Nude"]) from _call_change_Outfit_42
                
                $ temp_showering_Companions.remove(temp_showering_Companions[0])

        if black_screen:
            $ fade_in_from_black(0.4)
            
        pause 2.0

    if "bg_shower" in Player.location:
        $ Player.naked = True
        $ Player.cock_out = True

        if showering_Companions:
            $ temp_showering_Companions = showering_Companions[:]

            while temp_showering_Companions:
                if not temp_showering_Companions[0].History.check("seen_Player_naked"):
                    $ EventScheduler.Events[f"{temp_showering_Companions[0].tag}_seeing_penis"].start()

                $ temp_showering_Companions[0].History.update("seen_Player_naked")

                $ temp_showering_Companions.remove(temp_showering_Companions[0])

        $ shower_open = False

        pause 1.0

    $ Player.behavior = "showering"
    $ shower_steam = True

    $ Player.sweat = 0
    $ Player.chlorine = 0
    $ Player.spunk = False
    $ Player.saliva = False
    $ Player.grool = False
    $ Player.dirty_cock = False

    if showering_Companions:
        python:
            for G in showering_Companions:
                G.wet = True

                for location in G.spunk.keys():
                    G.spunk[location] = False

    $ temp_showering_Companions = showering_Companions[:]

    while temp_showering_Companions:
        if not temp_showering_Companions[0].History.check("showered_with_Player", tracker = "recent"):
            $ temp_showering_Companions[0].History.update("showered_with_Player")

        $ temp_showering_Companions.remove(temp_showering_Companions[0])
            
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

    if showering_Companions:
        $ temp_showering_Companions = showering_Companions[:]

        while temp_showering_Companions:
            # call try_on(temp_showering_Companions[0], temp_showering_Companions[0].Wardrobe.Clothes["towel"]) from _call_try_on_14

            $ temp_showering_Companions[0].behavior = None

            if time_index in temp_showering_Companions[0].schedule.keys() and temp_showering_Companions[0].schedule[time_index][1] == "showering":
                $ del temp_showering_Companions[0].schedule[time_index]

            $ temp_showering_Companions.remove(temp_showering_Companions[0])

        pause 1.0

    $ Player.History.update("showered")
    $ Player.naked = False
    $ Player.cock_out = False

    if time_index not in [0, 3] or Player.History.check("showered", tracker = "recent") > 1:
        $ clock -= 1

    if clock == 0:
        call check_for_Events(only_automatic = True) from _call_check_for_Events_17
        
    call move_location(Player.location) from _call_move_location_49

    return