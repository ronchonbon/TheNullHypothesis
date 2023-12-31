label get_ready_for_bed:
    $ Character_picker_active = False
    $ belt_disabled = True

    if not Present:
        "You should probably get some sleep."
    else:
        "It's getting late."

    $ Party = []

    $ Player.getting_ready_for_bed = True

    $ selected_Event = EventScheduler.choose_Event(getting_ready_for_bed = True)

    if selected_Event:
        call start_Event(selected_Event) from _call_start_Event_10
    else:
        $ Present = get_Present(location = Player.location)

        if Present:
            call sleepover(Present) from _call_sleepover

    jump go_to_sleep

label go_to_sleep(automatic = False):
    $ Character_picker_disabled = True
    $ belt_disabled = True
        
    if automatic:
        hide screen Action_screen
        hide screen interactions_screen
        hide screen phone_screen
        hide screen Player_menu
        hide screen shop_screen
        hide screen Wardrobe_screen

        call closing_Action_interface from _call_closing_Action_interface_5

        call remove_Characters(location = Player.location) from _call_remove_Characters_234
        
        $ Player.destination = Player.home
        $ Player.location = Player.home

        $ time_index = 3
        
        $ lighting = "night"
        
    $ reset_behavior()
    
    $ temp_sleepover_Characters = []

    python:
        for C in Present:
            if C in all_Girls:
                temp_sleepover_Characters.append(C)

    while temp_sleepover_Characters:
        $ thresholds = eval(f"{temp_sleepover_Characters[0].tag}_thresholds")

        call change_Girl_stat(temp_sleepover_Characters[0], "love", int(0.04*thresholds["sleepover"][0])) from _call_change_Girl_stat_1602
        call change_Girl_stat(temp_sleepover_Characters[0], "trust", int(0.04*thresholds["sleepover"][1])) from _call_change_Girl_stat_1603

        $ temp_sleepover_Characters[0].History.update("sleepover")

        $ temp_sleepover_Characters[0].getting_ready_for_bed = True

        $ temp_sleepover_Characters.remove(temp_sleepover_Characters[0])

    call set_Character_Outfits(instant = False) from _call_set_Character_Outfits_13

    if Present:
        pause 2.0

    $ Player.getting_ready_for_bed = False

    if not automatic:
        $ lights_on = False

        $ lighting = "moonlight"

        call set_the_scene(fade = False, fade_Characters = False) from _call_set_the_scene_302

    $ Character_picker_disabled = True
    $ belt_disabled = True
    
    pause 2.0

    $ fade_to_black(0.4)

    python:
        for C in all_Characters:
            C.sleeping = True

    $ Player.sleeping = True

    call check_for_Events(sleeping = True) from _call_check_for_Events_1

    python:
        for C in all_Characters:
            C.sleeping = False

    $ Player.sleeping = False

    $ lights_on = True

    if time_index >= 3:
        python:
            for C in all_Characters:
                C.waking_up = True

        $ Player.waking_up = True
        
        call wait_around(fade = False) from _call_wait_around_2

        python:
            for C in all_Characters:
                C.waking_up = False

        $ Player.waking_up = False

    if black_screen:
        $ fade_in_from_black(0.4)
                
    $ Character_picker_active = True
    $ belt_disabled = False

    $ renpy.force_autosave()

    call move_location(Player.location) from _call_move_location_45

    return

label sleepover(Characters):
    if Characters in all_Characters:
        $ Characters = [Characters]

    $ Characters = sort_Characters_by_approval(Characters[:])[:]

    $ temp_sleeping_Characters = Characters[:]

    python:
        for C in temp_sleeping_Characters:
            if Player.location == C.home:
                temp_sleeping_Characters.remove(C)
                temp_sleeping_Characters.insert(0, C)

    $ sleeping_Characters = []

    $ also_leaving = False

    while temp_sleeping_Characters:
        if temp_sleeping_Characters[0] in all_Girls:    
            $ status = temp_sleeping_Characters[0].get_status()

            if status:
                call expression f"{temp_sleeping_Characters[0].tag}_getting_late_{status}" from _call_expression_270
            elif approval_check(temp_sleeping_Characters[0], threshold = "love"):
                call expression f"{temp_sleeping_Characters[0].tag}_getting_late_love" from _call_expression_271
            elif temp_sleeping_Characters[0] in Partners:
                call expression f"{temp_sleeping_Characters[0].tag}_getting_late_relationship" from _call_expression_272
            else:
                call expression f"{temp_sleeping_Characters[0].tag}_getting_late" from _call_expression_273

            $ option = None

            menu:
                extend ""
                "Do you want to sleep over tonight?" if temp_sleeping_Characters[0] in Partners and Player.location == Player.home and not sleeping_Characters:
                    $ option = "sleepover"
                "Can I sleep over tonight?" if temp_sleeping_Characters[0] in Partners and Player.location == temp_sleeping_Characters[0].home:
                    $ option = "sleepover"
                "Did you also want to sleep over, [temp_sleeping_Characters[0].name]?" if temp_sleeping_Characters[0] in Partners and sleeping_Characters:
                    $ option = "sleepover"
                "Goodnight, [temp_sleeping_Characters[0].name].":
                    $ option = "goodnight"

            if option == "sleepover":
                $ status = temp_sleeping_Characters[0].get_status()

                if status:
                    call expression f"{temp_sleeping_Characters[0].tag}_asked_to_sleepover_{status}" pass (sleeping_Characters = sleeping_Characters) from _call_expression_274
                elif approval_check(temp_sleeping_Characters[0], threshold = "love"):
                    call expression f"{temp_sleeping_Characters[0].tag}_asked_to_sleepover_love" pass (sleeping_Characters = sleeping_Characters) from _call_expression_275
                elif temp_sleeping_Characters[0] in Partners:
                    call expression f"{temp_sleeping_Characters[0].tag}_asked_to_sleepover_relationship" pass (sleeping_Characters = sleeping_Characters) from _call_expression_276
                else:
                    call expression f"{temp_sleeping_Characters[0].tag}_asked_to_sleepover" pass (sleeping_Characters = sleeping_Characters) from _call_expression_277

                if not _return:
                    $ option = "rejected"
            elif option == "goodnight":
                $ temp_friend_Characters = sleeping_Characters[:]
                $ temp_friend_Characters.append(temp_sleeping_Characters[0])

                $ status = temp_sleeping_Characters[0].get_status()

                if are_Characters_in_Partners(temp_sleeping_Characters) and approval_check(temp_sleeping_Characters[0], threshold = "sleepover") and (are_Characters_friends(temp_friend_Characters) or renpy.random.random() > 0.5):
                    if status:
                        call expression f"{temp_sleeping_Characters[0].tag}_request_sleepover_{status}" pass (sleeping_Characters = sleeping_Characters) from _call_expression_278
                    elif approval_check(temp_sleeping_Characters[0], threshold = "love"):
                        call expression f"{temp_sleeping_Characters[0].tag}_request_sleepover_love" pass (sleeping_Characters = sleeping_Characters) from _call_expression_279
                    elif temp_sleeping_Characters[0] in Partners:
                        call expression f"{temp_sleeping_Characters[0].tag}_request_sleepover_relationship" pass (sleeping_Characters = sleeping_Characters) from _call_expression_280
                    else:
                        call expression f"{temp_sleeping_Characters[0].tag}_request_sleepover" pass (sleeping_Characters = sleeping_Characters) from _call_expression_281

                    if not _return:
                        $ option = "rejected"
                    else:
                        $ option = "sleepover"
                else:
                    if status:
                        call expression f"{temp_sleeping_Characters[0].tag}_goodnight_{status}" pass (sleeping_Characters = sleeping_Characters, also_leaving = also_leaving) from _call_expression_282
                    elif approval_check(temp_sleeping_Characters[0], threshold = "love"):
                        call expression f"{temp_sleeping_Characters[0].tag}_goodnight_love" pass (sleeping_Characters = sleeping_Characters, also_leaving = also_leaving) from _call_expression_283
                    elif temp_sleeping_Characters[0] in Partners:
                        call expression f"{temp_sleeping_Characters[0].tag}_goodnight_relationship" pass (sleeping_Characters = sleeping_Characters, also_leaving = also_leaving) from _call_expression_284
                    else:
                        call expression f"{temp_sleeping_Characters[0].tag}_goodnight" pass (sleeping_Characters = sleeping_Characters, also_leaving = also_leaving) from _call_expression_285
        else:
            call expression f"{temp_sleeping_Characters[0].tag}_leaves" from _call_expression_286

        if option in ["goodnight", "rejected"] and Player.location == temp_sleeping_Characters[0].home:
            call move_location(Player.home) from _call_move_location_46
        elif option in ["goodnight", "rejected"]:
            call send_Characters(temp_sleeping_Characters[0], temp_sleeping_Characters[0].home) from _call_send_Characters_228

            $ also_leaving = True
                
        $ temp_sleeping_Characters.remove(temp_sleeping_Characters[0])

    return