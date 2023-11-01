label progress_story:
    call reset_all_interfaces from _call_reset_all_interfaces_1

    $ Party = []

    $ fade_to_black(0.4)

    $ renpy.pause(1.0, hard = True)

    $ Player.location = Player.home

    $ Present = get_Present()

    call displace_Characters(Present[:]) from _call_displace_Characters_2

    $ temp_hiding_Characters = Present[:]

    while temp_hiding_Characters:
        call hide_Character(temp_hiding_Characters[0]) from _call_hide_Character_32

        $ temp_hiding_Characters.remove(temp_hiding_Characters[0])

    $ fade_in_from_black(0.4)

    if chapter == 1:
        if season == 1:
            $ weekday = 4

            call go_to_sleep(automatic = True) from _call_go_to_sleep
        elif season == 2:
            $ weekday = 5

            call go_to_sleep(automatic = True) from _call_go_to_sleep_1
        elif season == 3:
            $ time_index = 2
            
            $ lighting = "evening"

            if not EventScheduler.Events["ch1_season_three_progress"].completed:
                $ EventScheduler.Events["ch1_season_three_progress"].start()
            else:
                call open_texts(Kurt) from _call_open_texts_39

                pause
                
                call send_text(Kurt, "hey, about that comic book store in town") from _call_send_text_108

    return