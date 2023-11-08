label refresh_season_content:
    $ register_Characters()
    $ register_Events()
    $ register_Quests()
    $ register_Items()

    $ EventScheduler.update_conditions()

    show screen updates_screen()
    show screen belt_screen()
    show screen Character_picker()
    show screen hotkeys_screen()

    show filter onlayer filters:
        alpha 0.5

    $ available_songs = []

    $ available_ringtones = []

    $ updated_database_Characters = unlocked_Characters[:]

    while updated_database_Characters:
        $ updated_database_Characters[0].database = {}

        call expression f"update_{updated_database_Characters[0].tag}_database" from _call_expression_115

        if updated_database_Characters:
            $ updated_database_Characters.remove(updated_database_Characters[0])

    if chapter >= 1 and season >= 1:
        show background zorder 0
        show midground zorder 2
        show foreground zorder 4
        show cover1 zorder 97
        show cover2 zorder 98
        show bottom_bar zorder 99

        call start_chapter_one_season_one from _call_start_chapter_one_season_one

    if chapter >= 1 and season >= 2:
        call start_chapter_one_season_two from _call_start_chapter_one_season_two

    if chapter >= 1 and season >= 3:
        call start_chapter_one_season_three from _call_start_chapter_one_season_three

        $ mall_damage = True

    if chapter >= 1 and season >= 4:
        call start_chapter_one_season_four from _call_start_chapter_one_season_four

        $ mall_damage = False

    python:
        for C in all_Girls:
            C.possible_Actions = []

            for Action_type in all_Action_types:
                if eval(f"{C.tag}_thresholds['{Action_type}'][0]") <= max_stats[season - 1] and eval(f"{C.tag}_thresholds['{Action_type}'][1]") <= max_stats[season - 1]:
                    C.possible_Actions.append(Action_type)
                
            C.possible_poses = []

            for pose in pose_names.keys():
                if eval(f"{C.tag}_thresholds['{pose}'][0]") <= max_stats[season - 1] and eval(f"{C.tag}_thresholds['{pose}'][1]") <= max_stats[season - 1]:
                    C.possible_poses.append(pose)

    if not game_started:
        call set_Character_Outfits from _call_set_Character_Outfits_10
    else:
        $ temp_resetting_Outfits_Girls = all_Girls[:]

        while temp_resetting_Outfits_Girls:
            if temp_resetting_Outfits_Girls[0].location != Player.location:
                call set_Character_Outfits(temp_resetting_Outfits_Girls[0]) from _call_set_Character_Outfits_22

            $ temp_resetting_Outfits_Girls.remove(temp_resetting_Outfits_Girls[0])

    $ temp_refreshing_Characters = all_Girls[:]

    while temp_refreshing_Characters:
        $ temp_all_Outfits = list(temp_refreshing_Characters[0].Wardrobe.Outfits.values())[:]

        while temp_all_Outfits:
            call set_Outfit_flags(temp_refreshing_Characters[0], temp_all_Outfits[0], hypothetical = True) from _call_set_Outfit_flags_23

            if temp_all_Outfits:
                $ temp_all_Outfits.remove(temp_all_Outfits[0])

        if temp_refreshing_Characters:
            $ temp_refreshing_Characters.remove(temp_refreshing_Characters[0])

    return