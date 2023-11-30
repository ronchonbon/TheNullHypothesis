default volume_muted = False

screen hotkeys_screen():
    if not input_cheats:
        if not black_screen and not belt_hidden and sandbox and not ongoing_Event and (not current_phone_Character or not current_phone_Character.mandatory_text_options):
            key "m" action [
                        SetVariable("current_Player_menu_page", "map"),
                        ToggleScreen("Player_menu")]
                        
            key "i" action [
                        SetVariable("current_Player_menu_page", "inventory"),
                        ToggleScreen("Player_menu")]
                        
            key "j" action [
                        SetVariable("current_Player_menu_page", "journal"),
                        ToggleScreen("Player_menu")]
                        
            key "p" action ToggleScreen("phone_screen")

            if Player.location != Player.home:
                key "r" action Call("travel", Player.home)

            if Player.location != "bg_classroom":
                key "c" action Call("travel", "bg_classroom")

            if Player.location != "bg_danger":
                key "g" action Call("travel", "bg_danger")

            if Player.schedule or Player.date_planned or (day - EventScheduler.Events["Rogue_confession_text"].completed_when == 1 and not EventScheduler.Events["Rogue_confession"].completed):
                key "q" action Show("say", who = None, what = "Maybe don't skip today.", hide_after = 5.0)
            else:
                key "q" action Call("go_to_sleep", automatic = True, from_current = True)

        if volume_muted:
            key "-" action [
                SetVariable("volume_muted", False),
                SetMute(["sound", "music"], False)]
        else:
            key "-" action [
                SetVariable("volume_muted", True),
                SetMute(["sound", "music"], True)]