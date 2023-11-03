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
        add "images/interface/belt/belt.webp" align (0.5, 0.5)

        if weather:
            if time_index <= 3:
                add f"images/interface/belt/{time_index}_{weather}.webp" align (0.5, 0.5)
            else:
                add f"images/interface/belt/3_{weather}.webp" align (0.5, 0.5)
        else:
            if time_index <= 3:
                add f"images/interface/belt/{time_index}.webp" align (0.5, 0.5)
            else:
                add "images/interface/belt/3.webp" align (0.5, 0.5)

        vbox anchor (0.5, 0.5) pos (0.932, 0.065) xysize (25, 100):
            for s in range(1, Player.max_stamina + 1):
                if s <= Player.max_stamina - clock:
                    imagebutton align (0.5, 0.5):
                        idle "images/interface/belt/stamina_empty.webp" hover "images/interface/belt/stamina_empty.webp"

                        action NullAction()

                        tooltip "Stamina"
                else:
                    imagebutton align (0.5, 0.5):
                        idle "images/interface/belt/stamina.webp" hover "images/interface/belt/stamina.webp"

                        action NullAction()

                        tooltip "Stamina"

        text f"{temperature[time_index]} " + u"\u00b0C" anchor (1.0, 0.5) pos (0.780, 0.044):
            color "#ffffff"
            
            size 25
        
        text f"{week[weekday][0:3]}" anchor (0.5, 0.5) pos (0.965, 0.05):
            color "#ffffff"

            bold True
            
            size 45
        
        text f"{time_options[time_index].capitalize()}" anchor (0.5, 0.5) pos (0.966, 0.087):
            color "#ffffff"

            size 30
            
        if renpy.get_screen("say"):
            add "images/interface/belt/journal_idle.webp" align (0.5, 0.5)
        elif not belt_disabled and (not current_phone_Character or not current_phone_Character.mandatory_text_options):
            imagebutton align (0.5, 0.5):
                idle "images/interface/belt/journal_idle.webp" hover "images/interface/belt/journal.webp"

                action [
                    SetVariable("current_Player_menu_page", "journal"),
                    Show("Player_menu"),
                    SetVariable("journal_alert", False)]

                focus_mask True

                tooltip "Open Journal"
        else:
            add "images/interface/belt/journal_lock.webp" align (0.5, 0.5)

        if renpy.get_screen("say"):
            add "images/interface/belt/inventory_idle.webp" align (0.5, 0.5)
        elif not belt_disabled and (not current_phone_Character or not current_phone_Character.mandatory_text_options):
            imagebutton align (0.5, 0.5):
                idle "images/interface/belt/inventory_idle.webp" hover "images/interface/belt/inventory.webp"

                action [
                    SetVariable("current_Player_menu_page", "inventory"),
                    Show("Player_menu"),
                    SetVariable("inventory_alert", False)]

                focus_mask True

                tooltip "Open Inventory"
        else:
            add "images/interface/belt/inventory_lock.webp" align (0.5, 0.5)
            
        if renpy.get_screen("say"):
            add "images/interface/belt/map_idle.webp" align (0.5, 0.5)
        elif not belt_disabled and (not current_phone_Character or not current_phone_Character.mandatory_text_options):
            imagebutton align (0.5, 0.5):
                idle "images/interface/belt/map_idle.webp" hover "images/interface/belt/map.webp"
                
                action [
                    SetVariable("current_Player_menu_page", "map"),
                    Show("Player_menu")]

                focus_mask True

                tooltip "Open Map"
        else:
            add "images/interface/belt/map_lock.webp" align (0.5, 0.5)
            
        if sandbox and quick_location_1 and renpy.get_screen("say"):
            add "images/interface/belt/quick1_idle.webp" align (0.5, 0.5)
        elif sandbox and quick_location_1 and not belt_disabled and (not current_phone_Character or not current_phone_Character.mandatory_text_options):
            imagebutton align (0.5, 0.5):
                idle "images/interface/belt/quick1_idle.webp" hover "images/interface/belt/quick1.webp"
                
                action Function(exec, quick_location_1)

                focus_mask True

                tooltip "Move to QuickLoc1"
        else:
            add "images/interface/belt/quick1_lock.webp" align (0.5, 0.5)
            
        if sandbox and quick_location_2 and renpy.get_screen("say"):
            add "images/interface/belt/quick2_idle.webp" align (0.5, 0.5)
        elif sandbox and quick_location_2 and not belt_disabled and (not current_phone_Character or not current_phone_Character.mandatory_text_options):
            imagebutton align (0.5, 0.5):
                idle "images/interface/belt/quick2_idle.webp" hover "images/interface/belt/quick2.webp"
                
                action Function(exec, quick_location_2)

                focus_mask True

                tooltip "Move to QuickLoc2"
        else:
            add "images/interface/belt/quick2_lock.webp" align (0.5, 0.5)
            
        if sandbox and quick_location_3 and renpy.get_screen("say"):
            add "images/interface/belt/quick3_idle.webp" align (0.5, 0.5)
        elif sandbox and quick_location_3 and not belt_disabled and (not current_phone_Character or not current_phone_Character.mandatory_text_options):
            imagebutton align (0.5, 0.5):
                idle "images/interface/belt/quick3_idle.webp" hover "images/interface/belt/quick3.webp"
                
                action Function(exec, quick_location_3)

                focus_mask True

                tooltip "Move to QuickLoc3"
        else:
            add "images/interface/belt/quick3_lock.webp" align (0.5, 0.5)

        if renpy.get_screen("say"):
            add "images/interface/belt/phone_idle.webp" align (0.5, 0.5)
        elif not belt_disabled and (not current_phone_Character or not current_phone_Character.mandatory_text_options):
            imagebutton align (0.5, 0.5):
                idle "images/interface/belt/phone_idle.webp" hover "images/interface/belt/phone.webp"
                
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
            add "images/interface/belt/phone_lock.webp" align (0.5, 0.5)

        if journal_alert:
            add "images/interface/belt/journal_alert.webp" align (0.5, 0.5)

        if inventory_alert:
            add "images/interface/belt/inventory_alert.webp" align (0.5, 0.5)

        if phone_alert or unread_messages:
            add "images/interface/belt/phone_alert.webp" align (0.5, 0.5)

        if Player.sweat >= Player.sweaty_threshold:
            imagebutton align (0.5, 0.5):
                idle "images/interface/belt/sweaty.webp" hover "images/interface/belt/sweaty.webp"

                action NullAction()

                focus_mask True

                tooltip "Sweaty"

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
            if belt_hidden or ongoing_Event or not sandbox:
                frame anchor (1.0, 0.5) pos (0.98, 0.166):
                    background Frame("images/interface/belt/update.webp", 12, 12)

                    padding (25, 15, 15, 15)

                    text update_message align (0.5, 0.5):
                        color "#ffffff"

                        size 32

                    at transform:
                        fade_in(0.4)
                        pause 2.5
                        fade_out(0.4)
            else:
                frame anchor (1.0, 0.5) pos (0.935, 0.166):
                    background Frame("images/interface/belt/update.webp", 12, 12)

                    padding (25, 15, 15, 15)

                    text update_message align (0.5, 0.5):
                        color "#ffffff"

                        size 32

                    at transform:
                        fade_in(0.4)
                        pause 2.5
                        fade_out(0.4)

            timer 3.3 action SetVariable("update_message", None)