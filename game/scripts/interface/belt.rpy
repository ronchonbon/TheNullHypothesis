init -1:
    
    default belt_hidden = False
    default belt_disabled = True

    default inventory_alert = False
    default journal_alert = False
    default phone_alert = False

    default update_messages = []
    default update_message = None

style belt is default

style belt_button:
    # hover_sound "sounds/interface/hover.ogg"
    activate_sound "sounds/interface/press.ogg"

style belt_image_button:
    # hover_sound "sounds/interface/hover.ogg"
    activate_sound "sounds/interface/press.ogg"

screen belt_screen():
    layer "interface"

    style_prefix "belt"

    if not black_screen and not belt_hidden and sandbox and not ongoing_Event:
        add "images/interface/belt/background.webp" zoom interface_new_adjustment

        hbox anchor (0.5, 0.5) pos (0.891, 0.036) xysize (int(55*background_sampling), int(260*background_sampling)):
            for s in range(Player.max_stamina):
                if s >= clock:
                    imagebutton align (0.5, 0.5):
                        idle At("images/interface/belt/stamina_empty.webp", interface) hover At("images/interface/belt/stamina_empty.webp", interface)

                        action NullAction()

                        tooltip "Stamina (Empty)"
                else:
                    imagebutton align (0.5, 0.5):
                        idle At("images/interface/belt/stamina.webp", interface) hover At("images/interface/belt/stamina.webp", interface)

                        action NullAction()

                        tooltip "Stamina"

            for s in range(Player.max_stamina, 4):
                imagebutton align (0.5, 0.5):
                    idle At("images/interface/belt/stamina_lock.webp", interface) hover At("images/interface/belt/stamina_lock.webp", interface)

                    action NullAction()

                    tooltip "Stamina (Locked)"

        text f"{temperature[time_index]} " + u"\u00b0C" anchor (0.5, 0.5) pos (0.903, 0.082):
            font "agency_fb_bold.ttf"

            color "#ffffff"
            
            size 25
        
        text f"{week[weekday][0:2]}" anchor (0.5, 0.5) pos (0.963, 0.05):
            font "magneto_bold.ttf"
            
            color "#ffffff"
            
            size 45
        
        text f"{time_options[time_index].capitalize()}" anchor (0.5, 0.5) pos (0.963, 0.09):
            color "#ffffff"

            size 35
            
        if renpy.get_screen("say"):
            add "images/interface/belt/journal_idle.webp" zoom interface_new_adjustment
        elif not belt_disabled and (not current_phone_Character or not current_phone_Character.mandatory_text_options):
            imagebutton align (0.5, 0.5):
                idle At("images/interface/belt/journal_idle.webp", interface) hover At("images/interface/belt/journal.webp", interface)

                action [
                    SetVariable("current_Player_menu_page", "journal"),
                    Show("Player_menu"),
                    SetVariable("journal_alert", False)]

                focus_mask True

                tooltip "Open Journal"
        else:
            add "images/interface/belt/journal_lock.webp" zoom interface_new_adjustment

        if renpy.get_screen("say"):
            add "images/interface/belt/inventory_idle.webp" zoom interface_new_adjustment
        elif not belt_disabled and (not current_phone_Character or not current_phone_Character.mandatory_text_options):
            imagebutton align (0.5, 0.5):
                idle At("images/interface/belt/inventory_idle.webp", interface) hover At("images/interface/belt/inventory.webp", interface)

                action [
                    SetVariable("current_Player_menu_page", "inventory"),
                    Show("Player_menu"),
                    SetVariable("inventory_alert", False)]

                focus_mask True

                tooltip "Open Inventory"
        else:
            add "images/interface/belt/inventory_lock.webp" zoom interface_new_adjustment
            
        if renpy.get_screen("say"):
            add "images/interface/belt/map_idle.webp" zoom interface_new_adjustment
        elif not belt_disabled and (not current_phone_Character or not current_phone_Character.mandatory_text_options):
            imagebutton align (0.5, 0.5):
                idle At("images/interface/belt/map_idle.webp", interface) hover At("images/interface/belt/map.webp", interface)
                
                action [
                    SetVariable("current_Player_menu_page", "map"),
                    Show("Player_menu")]

                focus_mask True

                tooltip "Open Map"
        else:
            add "images/interface/belt/map_lock.webp" zoom interface_new_adjustment
            
        if sandbox and quick_location_1 and renpy.get_screen("say"):
            add "images/interface/belt/quick1_idle.webp" zoom interface_new_adjustment
        elif sandbox and quick_location_1 and not belt_disabled and (not current_phone_Character or not current_phone_Character.mandatory_text_options):
            imagebutton align (0.5, 0.5):
                idle At("images/interface/belt/quick1_idle.webp", interface) hover At("images/interface/belt/quick1.webp", interface)
                
                action Function(exec, quick_location_1)

                focus_mask True

                tooltip "Move to QuickLoc1"
        else:
            add "images/interface/belt/quick1_lock.webp" zoom interface_new_adjustment
            
        if sandbox and quick_location_2 and renpy.get_screen("say"):
            add "images/interface/belt/quick2_idle.webp" zoom interface_new_adjustment
        elif sandbox and quick_location_2 and not belt_disabled and (not current_phone_Character or not current_phone_Character.mandatory_text_options):
            imagebutton align (0.5, 0.5):
                idle At("images/interface/belt/quick2_idle.webp", interface) hover At("images/interface/belt/quick2.webp", interface)
                
                action Function(exec, quick_location_2)

                focus_mask True

                tooltip "Move to QuickLoc2"
        else:
            add "images/interface/belt/quick2_lock.webp" zoom interface_new_adjustment
            
        if sandbox and quick_location_3 and renpy.get_screen("say"):
            add "images/interface/belt/quick3_idle.webp" zoom interface_new_adjustment
        elif sandbox and quick_location_3 and not belt_disabled and (not current_phone_Character or not current_phone_Character.mandatory_text_options):
            imagebutton align (0.5, 0.5):
                idle At("images/interface/belt/quick3_idle.webp", interface) hover At("images/interface/belt/quick3.webp", interface)
                
                action Function(exec, quick_location_3)

                focus_mask True

                tooltip "Move to QuickLoc3"
        else:
            add "images/interface/belt/quick3_lock.webp" zoom interface_new_adjustment

        if renpy.get_screen("say"):
            add "images/interface/belt/phone_idle.webp" zoom interface_new_adjustment
        elif not belt_disabled and (not current_phone_Character or not current_phone_Character.mandatory_text_options):
            imagebutton align (0.5, 0.5):
                idle At("images/interface/belt/phone_idle.webp", interface) hover At("images/interface/belt/phone.webp", interface)
                
                if not renpy.get_screen("phone_screen"):
                    action [
                        SetVariable("booting", True),
                        Show("phone_screen"),
                        SetVariable("phone_alert", False)]
                else:
                    action [
                        Hide("phone_screen"),
                        Call("move_location", Player.location, from_current = True)]

                focus_mask True

                tooltip "Open Phone"
        else:
            add "images/interface/belt/phone_lock.webp" zoom interface_new_adjustment

        if journal_alert:
            add "images/interface/belt/journal_alert.webp" zoom interface_new_adjustment

        if inventory_alert:
            add "images/interface/belt/inventory_alert.webp" zoom interface_new_adjustment

        if phone_alert or unread_messages:
            add "images/interface/belt/phone_alert.webp" zoom interface_new_adjustment

        if Player.sweat >= Player.sweaty_threshold:
            imagebutton align (0.5, 0.5):
                idle At("images/interface/belt/sweaty.webp", interface) hover At("images/interface/belt/sweaty.webp", interface)

                action NullAction()

                focus_mask True

                tooltip "Sweaty"

        if Player.History.check("attended_class", tracker = "weekly") >= 3:
            imagebutton align (0.5, 0.5):
                idle At("images/interface/belt/attendance.webp", interface) hover At("images/interface/belt/attendance.webp", interface)

                action NullAction()

                focus_mask True

                tooltip "Attendance Bonus"

    if tooltips_enabled:
        use tooltips

screen updates_screen():
    layer "screens"

    if not renpy.get_screen("Player_menu"):
        if update_messages and not update_message:
            timer 0.2 action [
                SetVariable("update_message", update_messages[0]), 
                RemoveFromSet(update_messages, update_messages[0])]

        if update_message:
            if Action_screen_showing:
                frame anchor (1.0, 0.5) pos (0.85, 0.05):
                    background Frame("images/interface/belt/update.webp", 2, 2)

                    padding (15, 15, 15, 15)

                    text update_message align (0.5, 0.5):
                        color "#ffffff"

                        size 32

                    at transform:
                        fade_in(0.4)
                        pause 2.5
                        fade_out(0.4)
            elif belt_hidden or ongoing_Event or not sandbox:
                frame anchor (1.0, 0.5) pos (0.98, 0.05):
                    background Frame("images/interface/belt/update.webp", 2, 2)

                    padding (15, 15, 15, 15)

                    text update_message align (0.5, 0.5):
                        color "#ffffff"

                        size 32

                    at transform:
                        fade_in(0.4)
                        pause 2.5
                        fade_out(0.4)
            else:
                frame anchor (1.0, 0.5) pos (0.925, 0.18):
                    background Frame("images/interface/belt/update.webp", 2, 2)

                    padding (15, 15, 15, 15)

                    text update_message align (0.5, 0.5):
                        color "#ffffff"

                        size 32

                    at transform:
                        fade_in(0.4)
                        pause 2.5
                        fade_out(0.4)

            timer 3.3 action SetVariable("update_message", None)