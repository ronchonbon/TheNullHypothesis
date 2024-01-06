screen climax_screen():
    if not black_screen and not belt_hidden and sandbox and not ongoing_Event and (not current_phone_Character or not current_phone_Character.mandatory_text_options):
        if not renpy.get_screen("say") and not renpy.get_screen("Player_customization_screen") and not renpy.get_screen("Player_menu") and not renpy.get_screen("shop_screen") and not renpy.get_screen("Wardrobe_screen"):
            timer 15.0 action Function(renpy.call_in_new_context, "climax_screen_result") repeat True

label climax_screen_result:
    $ renpy.dynamic(temp_Characters = all_Companions[:])

    while temp_Characters:
        if temp_Characters[0].location != "hold":
            if temp_Characters[0].remote_vibrator is not None and temp_Characters[0].remote_vibrator > 0.0:
                if temp_Characters[0].stamina:
                    call change_Character_stat(temp_Characters[0], "desire", int(5.0*temp_Characters[0].remote_vibrator)) from _call_change_Character_stat_24

                    if temp_Characters[0].desire >= 100:
                        call expression f"{temp_Characters[0].tag}_remote_vibrator_orgasm"
                    elif temp_Characters[0].desire >= 75:
                        call expression f"{temp_Characters[0].tag}_remote_vibrator_75"
                    elif temp_Characters[0].desire >= 50:
                        call expression f"{temp_Characters[0].tag}_remote_vibrator_50"
                    elif temp_Characters[0].desire >= 25:
                        call expression f"{temp_Characters[0].tag}_remote_vibrator_25"
                else:
                    call expression f"{temp_Characters[0].tag}_remote_vibrator_out_of_stamina"
            
            if temp_Characters[0].behavior == "masturbating":
                if temp_Characters[0].stamina and (not temp_Characters[0].History.check("orgasmed", tracker = "recent") or temp_Characters[0].status["nympho"]):
                    if temp_Characters[0].location == Player.location:
                        call change_Character_stat(temp_Characters[0], "desire", 5) from _call_change_Character_stat_25

                    if temp_Characters[0].desire >= 100:
                        call expression f"{temp_Characters[0].tag}_masturbating_orgasm"
                    elif temp_Characters[0].desire >= 75:
                        call expression f"{temp_Characters[0].tag}_masturbating_75"
                    elif temp_Characters[0].desire >= 50:
                        call expression f"{temp_Characters[0].tag}_masturbating_50"
                    elif temp_Characters[0].desire >= 25:
                        call expression f"{temp_Characters[0].tag}_masturbating_25"
                else:
                    $ temp_Characters[0].behavior = None

        $ temp_Characters.remove(temp_Characters[0])