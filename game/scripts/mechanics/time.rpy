init python:

    def reset_Characters_at_end_of_period(Characters = None):
        Characters = all_Characters[:] if not Characters else Characters

        for C in Characters:
            if C in all_Companions:
                if C.behavior in ["studying", "in_class", "teaching", "training"]:
                    if C.location != Player.location:
                        if C.behavior == "studying":
                            C.XP += 10*C.stat_modifier

                            C.History.update("studied")
                        elif C.behavior == "in_class":
                            C.XP += 20*C.stat_modifier*C.max_stamina

                            C.History.update("attended_class")
                        elif C.behavior == "teaching":
                            C.XP += 20*C.stat_modifier*C.max_stamina

                            C.History.update("taught_class")
                        elif C.behavior == "training":
                            C.XP += 10*C.stat_modifier

                            C.History.update("trained")

                    for other_C in all_Companions:
                        if other_C != C:
                            if other_C not in C.likes.keys():
                                C.likes[other_C] = 0
                            
                            if C not in other_C.likes.keys():
                                other_C.likes[C] = 0
                                
                            if other_C.location == C.location and other_C.behavior in ["studying", "in_class", "teaching", "training"]:
                                C.likes[other_C] += 5
                                other_C.likes[C] += 5

                C.remove_trait("wet")
                
                C.desire -= 25 if C.desire >= 25 else C.desire
                C.stamina += 1 if C.stamina < C.max_stamina else 0

                C.wants_alone_time -= 1 if C.wants_alone_time > 0 else 0

            if C in Sprites:
                C.change_face()
                C.change_arms()

        return

    def reset_Characters_at_end_of_day(Characters = None):
        Characters = all_Characters[:] if not Characters else Characters

        for C in Characters:
            if C in all_Companions:
                for status in ["miffed", "mad", "heartbroken", "horny", "nympho"]:
                    C.status[status] -= 1 if C.status[status] > 0 else 0

                for location in C.spunk.keys():
                    C.spunk[location] = 0
                    C.persistent_spunk[location] = 0

                for location in C.creampie.keys():
                    C.creampie[location] = 0

                for I in C.Wardrobe.Clothes.values():
                    I.soiled = False

                for O in C.Wardrobe.Outfits.keys():
                    for I in C.Wardrobe.Outfits[O].Clothes.values():
                        I.soiled = False

                C.desire = 0
                C.stamina = C.max_stamina

                C.choose_Outfits()

            if C in all_NPCs:
                if C.check_traits("gives_work"):
                    C.give_trait("has_jobs")
                
        return

label wait_around(fade = True, silent = False, Events = True):
    hide screen phone_screen

    $ Character_picker_disabled = True
    $ belt_disabled = True

    $ check_predicted_images()

    if fade and not silent:
        $ fade_to_black(0.4)

    $ reset_Characters_at_end_of_period()
    
    call level_up from _call_level_up

    if time_index < 3:
        $ time_index += 1

        $ renpy.dynamic(temp_weather = weather)

        $ set_weather()

        if time_index in [0, 1]:
            $ lighting = "day"
        elif time_index == 2:
            $ lighting = "evening"
        elif time_index > 3 or not lights_on:
            if Player.location == Rogue.home and "candle" in Rogue.inventory.keys() and "mirror" in Rogue.inventory.keys() and "camera" in Rogue.inventory.keys():
                $ lighting = "candlelit"
            else:
                $ lighting = "moonlight"
        elif time_index == 3:
            $ lighting = "night"

        $ Player.desire -= 25 if Player.desire >= 25 else Player.desire
        $ Player.stamina += 1 if Player.stamina < Player.max_stamina else 0

        python:
            for C in all_Companions:
                C.remove_trait("messy_bed")
                
        $ Player.remove_trait("messy_bed")

        python:
            for C in all_Characters:
                C.History.increment()

        $ Player.History.increment()
    else:
        call start_new_day from _call_start_new_day_7

    $ clock = Player.max_stamina

    call set_music from _call_set_music_15

    if not silent:
        call set_the_scene(fade = False, fade_Characters = False) from _call_set_the_scene_327

        if black_screen:
            $ fade_in_from_black(0.4)

        if Player.behavior == "waking_up":
            call check_for_Events(waking = True) from _call_check_for_Events_2
        
        $ leaving_Characters, arriving_Characters = set_Character_locations()

        $ was_teaching = None

        python:
            for C in Professors:
                if C.behavior == "teaching":
                    was_teaching = C

    $ set_Character_behavior()

    if Player.location in ["bg_campus", "bg_pool"] and weather and temp_weather != weather:
        $ EventScheduler.Events["inclement_weather"].start()

    if not silent:
        if was_teaching and was_teaching.behavior != "teaching" and was_teaching.location == Player.location:
            $ renpy.dynamic(temp_destination = was_teaching.destination)
            $ renpy.dynamic(temp_location = was_teaching.location)

            call add_Characters(was_teaching) from _call_add_Characters_2

            $ was_teaching.destination = temp_destination
            $ was_teaching.location = temp_location

        if leaving_Characters:
            call Characters_leave(leaving_Characters) from _call_Characters_leave_7

    call set_Character_Outfits from _call_set_Character_Outfits_27

    if not silent:
        if arriving_Characters:
            call Characters_arrive(arriving_Characters) from _call_Characters_arrive_4

        if Events:
            call check_for_Events(waiting = True) from _call_check_for_Events_15

    python:
        for C in all_Characters:
            C.location = C.destination

    $ Character_picker_disabled = False
    $ belt_disabled = False

    return

label start_new_day(fast = False):
    if not fast:
        call refresh_season_content from _call_refresh_season_content_8

    $ day += 1
    $ season_day += 1

    if weekday < 6:
        $ weekday += 1
    else:
        $ weekday = 0

    $ time_index = 0

    $ rain_probability += 0.05 if rain_probability < 1.0 else 0.0
    $ snow_left -= 1 if snow_left > 0 else 0

    if day > 3:
        $ set_weather()
    
    if not fast:
        $ reset_Characters_at_end_of_day()

    $ lights_on = True

    $ lighting = "day"

    if weekday == 0 and time_index == 0:
        if Player.History.check("attended_class", tracker = "weekly") >= 3:
            $ check_attendance = True
        else:
            $ check_attendance = False
    else:
        $ check_attendance = None

    $ Player.cash += Player.income
    $ Player.total_cash += Player.income

    $ Player.desire = 0
    $ Player.stamina = Player.max_stamina

    python:
        for C in all_Companions:
            C.give_trait("messy_bed")
            
    $ Player.give_trait("messy_bed")

    $ shower_steam = False

    $ update_messages = []

    $ renpy.dynamic(temp_Characters = all_Companions[:])

    while temp_Characters:
        if temp_Characters[0].timed_text_options:
            $ temp_Characters[0].timed_text_options = {}

            call change_Character_stat(temp_Characters[0], "love", -tiny_stat) from _call_change_Character_stat_1038

        $ temp_Characters.remove(temp_Characters[0])

    $ clock = Player.max_stamina
    
    python:
        for C in all_Characters:
            C.schedule = {}
            C.History.increment()

    $ Player.schedule = {}
    $ Player.date_planned = {}
    $ Player.History.increment()

    if check_attendance is not None:
        if check_attendance:
            $ Player.give_trait("attendance_bonus")
                
            $ Player.stat_modifier = 1.2
        else:
            $ Player.remove_trait("attendance_bonus")

            $ Player.stat_modifier = 1.0

    return