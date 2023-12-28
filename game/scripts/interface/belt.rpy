init -1:
    
    default belt_hidden = False
    default belt_disabled = True
    default belt_collapsed = False

    default inventory_alert = False
    default journal_alert = False
    default phone_alert = False

    default update_messages = []
    default update_message = None

style belt is default

style updates is default

style updates_frame:
    anchor (1.0, 0.5)

    background Frame(At("images/interface/belt/update.webp", interface), 10, 10)

    padding (15, 15, 15, 15)

style updates_text:
    font "agency_fb.ttf"

    size 32

screen belt_screen():
    layer "interface"

    style_prefix "belt"

    if not black_screen and not belt_hidden and sandbox and not ongoing_Event:
        add At("images/interface/belt/background.webp", interface)

        imagebutton:
            idle At("images/interface/belt/hide_idle.webp", interface) 
            hover At("images/interface/belt/hide.webp", interface)

            action ToggleVariable("belt_collapsed")

            tooltip "Hide Belt"

        text f"{week[weekday][0:2]}" anchor (0.5, 0.5) pos (0.963, 0.05):
            font "magneto_bold.ttf"
            
            size 45
        
        text f"{time_options[time_index].capitalize()}" anchor (0.5, 0.5) pos (0.963, 0.09):
            size 35
        
        hbox anchor (0.5, 0.5) pos (0.891, 0.036) xysize (0.029, 0.241):
            for s in range(Player.max_stamina):
                if s >= clock:
                    imagebutton:
                        idle At("images/interface/belt/stamina_empty.webp", interface) 
                        hover At("images/interface/belt/stamina_empty.webp", interface)

                        action NullAction()

                        tooltip "Stamina (Empty)"
                else:
                    imagebutton:
                        idle At("images/interface/belt/stamina.webp", interface) 
                        hover At("images/interface/belt/stamina.webp", interface)

                        action NullAction()

                        tooltip "Stamina"

            for s in range(Player.max_stamina, 4):
                imagebutton:
                    idle At("images/interface/belt/stamina_lock.webp", interface) 
                    hover At("images/interface/belt/stamina_lock.webp", interface)

                    action NullAction()

                    tooltip "Stamina (Locked)"

        text f"{temperature[time_index]} " + u"\u00b0C" anchor (0.5, 0.5) pos (0.903, 0.082):
            size 25
                
        if not belt_collapsed:
            if renpy.get_screen("say"):
                add At("images/interface/belt/journal_idle.webp", interface)
            elif not belt_disabled and (not current_phone_Character or not current_phone_Character.mandatory_text_options):
                imagebutton:
                    idle At("images/interface/belt/journal_idle.webp", interface) 
                    hover At("images/interface/belt/journal.webp", interface)

                    action [
                        SetVariable("current_Player_menu_page", "journal"),
                        Show("Player_menu"),
                        SetVariable("journal_alert", False)]

                    tooltip "Open Journal"
            else:
                add At("images/interface/belt/journal_lock.webp", interface)

            if renpy.get_screen("say"):
                add At("images/interface/belt/inventory_idle.webp", interface)
            elif not belt_disabled and (not current_phone_Character or not current_phone_Character.mandatory_text_options):
                imagebutton:
                    idle At("images/interface/belt/inventory_idle.webp", interface) 
                    hover At("images/interface/belt/inventory.webp", interface)

                    action [
                        SetVariable("current_Player_menu_page", "inventory"),
                        Show("Player_menu"),
                        SetVariable("inventory_alert", False)]

                    tooltip "Open Inventory"
            else:
                add At("images/interface/belt/inventory_lock.webp", interface)
                
            if renpy.get_screen("say"):
                add At("images/interface/belt/map_idle.webp", interface)
            elif not belt_disabled and (not current_phone_Character or not current_phone_Character.mandatory_text_options):
                imagebutton:
                    idle At("images/interface/belt/map_idle.webp", interface) 
                    hover At("images/interface/belt/map.webp", interface)
                    
                    action [
                        SetVariable("current_Player_menu_page", "map"),
                        Show("Player_menu")]

                    tooltip "Open Map"
            else:
                add At("images/interface/belt/map_lock.webp", interface)
                
            if sandbox and quick_location_1 and renpy.get_screen("say"):
                add At("images/interface/belt/quick1_idle.webp", interface)
            elif sandbox and quick_location_1 and not belt_disabled and (not current_phone_Character or not current_phone_Character.mandatory_text_options):
                imagebutton:
                    idle At("images/interface/belt/quick1_idle.webp", interface) 
                    hover At("images/interface/belt/quick1.webp", interface)
                    
                    action Function(exec, quick_location_1)

                    tooltip "Move to QuickLoc1"
            else:
                add At("images/interface/belt/quick1_lock.webp", interface)
                
            if sandbox and quick_location_2 and renpy.get_screen("say"):
                add At("images/interface/belt/quick2_idle.webp", interface)
            elif sandbox and quick_location_2 and not belt_disabled and (not current_phone_Character or not current_phone_Character.mandatory_text_options):
                imagebutton:
                    idle At("images/interface/belt/quick2_idle.webp", interface) 
                    hover At("images/interface/belt/quick2.webp", interface)
                    
                    action Function(exec, quick_location_2)

                    tooltip "Move to QuickLoc2"
            else:
                add At("images/interface/belt/quick2_lock.webp", interface)
                
            if sandbox and quick_location_3 and renpy.get_screen("say"):
                add At("images/interface/belt/quick3_idle.webp", interface)
            elif sandbox and quick_location_3 and not belt_disabled and (not current_phone_Character or not current_phone_Character.mandatory_text_options):
                imagebutton:
                    idle At("images/interface/belt/quick3_idle.webp", interface) 
                    hover At("images/interface/belt/quick3.webp", interface)
                    
                    action Function(exec, quick_location_3)

                    tooltip "Move to QuickLoc3"
            else:
                add At("images/interface/belt/quick3_lock.webp", interface)

            if renpy.get_screen("say"):
                add At("images/interface/belt/phone_idle.webp", interface)
            elif not belt_disabled and (not current_phone_Character or not current_phone_Character.mandatory_text_options):
                imagebutton:
                    idle At("images/interface/belt/phone_idle.webp", interface) 
                    hover At("images/interface/belt/phone.webp", interface)
                    
                    if not renpy.get_screen("phone_screen"):
                        action [
                            SetVariable("booting", True),
                            Show("phone_screen"),
                            SetVariable("phone_alert", False)]
                    else:
                        action [
                            Hide("phone_screen"),
                            Call("move_location", Player.location, from_current = True)]

                    tooltip "Open Phone"
            else:
                add At("images/interface/belt/phone_lock.webp", interface)

            if journal_alert:
                add At("images/interface/belt/journal_alert.webp", interface)

            if inventory_alert:
                add At("images/interface/belt/inventory_alert.webp", interface)

            if phone_alert or unread_messages:
                add At("images/interface/belt/phone_alert.webp", interface)

            if Player.sweat >= Player.sweaty_threshold:
                imagebutton:
                    idle At("images/interface/belt/sweaty.webp", interface) 
                    hover At("images/interface/belt/sweaty.webp", interface)

                    action NullAction()

                    tooltip "Sweaty"

            if Player.attendance_bonus:
                imagebutton:
                    idle At("images/interface/belt/attendance.webp", interface) 
                    hover At("images/interface/belt/attendance.webp", interface)

                    action NullAction()

                    tooltip "Attendance Bonus"

    if tooltips_enabled:
        use tooltips

screen updates_screen():
    layer "screens"

    style_prefix "updates"

    if not renpy.get_screen("Player_menu"):
        if update_messages and not update_message:
            timer 0.2 action [
                SetVariable("update_message", update_messages[0]), 
                RemoveFromSet(update_messages, update_messages[0])]

        if update_message:
            if Action_screen_showing:
                frame pos (0.85, 0.05):
                    text update_message

                    at transform:
                        fade_in(0.4)
                        pause 2.5
                        fade_out(0.4)
            elif belt_hidden or ongoing_Event or not sandbox:
                frame pos (0.98, 0.05):
                    text update_message

                    at transform:
                        fade_in(0.4)
                        pause 2.5
                        fade_out(0.4)
            else:
                frame pos (0.925, 0.18):
                    text update_message

                    at transform:
                        fade_in(0.4)
                        pause 2.5
                        fade_out(0.4)

            timer 3.3 action SetVariable("update_message", None)