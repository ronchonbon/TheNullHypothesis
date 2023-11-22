init -1:
    
    default phone_interactable = False
    default phone_disabled = False
    
    default booting = False
    default loading = False

    default humhum_available = False
    default humhum_hidden = False
    default humhum_index = -1

    default unread_messages = {}
    
    default humhum_yadjustment = ui.adjustment()
    default text_screen_yadjustment = ui.adjustment()

    default current_phone_screen = "home"
    
    default current_phone_Character = None

    default available_songs = []
    default available_ringtones = []
    default repeating = True

    default emergency_broadcast = False

    default input_cheats = False

transform message_appear(direction):
    xoffset 50*direction alpha 0.0

    parallel:
        ease 0.5 alpha 1.0
    parallel:
        easein_back 0.5 xoffset 0

transform message_appear_icon:
    zoom 0.0
    easein_back 0.5 zoom 1.0

image humhum_animation1 = Composite(
    (500, 854),
    (0, 0), "images/interface/phone/humhum_animated_background.webp",
    (78, 250), "images/interface/phone/humhum_animated_open.webp")

image humhum_animation2 = Composite(
    (500, 854),
    (0, 0), "images/interface/phone/humhum_animated_background.webp",
    (78, 250), "images/interface/phone/humhum_animated_closed.webp",
    (71, 582), "images/interface/phone/humhum_animated_hum.webp")

image humhum_animation3 = Composite(
    (500, 854),
    (0, 0), "images/interface/phone/humhum_animated_background.webp",
    (78, 250), "images/interface/phone/humhum_animated_open.webp",
    (71, 582), "images/interface/phone/humhum_animated_humhum.webp")

image humhum_animation:
    "humhum_animation1"
    pause 0.15
    "humhum_animation2"
    pause 0.15
    "humhum_animation3"
    pause 0.15
    repeat

style phone is default

style phone_button:
    activate_sound "sounds/interface/phone.ogg"

style phone_image_button:
    activate_sound "sounds/interface/phone.ogg"

screen phone_screen():
    layer "interface"

    style_prefix "phone"
    
    on "show" action [
        Hide("map_screen"),
        SetVariable("choice_disabled", True),
        SetVariable("say_obscured", True),
        SetVariable("Character_picker_disabled", True),
        SetVariable("current_input", ""),
        SetVariable("humhum_index", -1)]

    if current_phone_Character:
        on "hide" action [
            SetVariable(current_phone_screen, "home"),
            SetField(current_phone_Character, "electronic", False),
            SetVariable("phone_interactable", True),
            SetVariable("input_cheats", False),
            SetVariable("choice_disabled", False),
            SetVariable("say_obscured", False),
            SetVariable("Character_picker_disabled", False),
            Function(renpy.call_in_new_context, "read_texts", current_phone_Character, override = True)]
    else:
        on "hide" action [
            SetVariable(current_phone_screen, "home"),
            SetVariable("phone_interactable", True),
            SetVariable("input_cheats", False),
            SetVariable("choice_disabled", False),
            SetVariable("say_obscured", False),
            SetVariable("Character_picker_disabled", False)]

    timer 0.5 action SetVariable("booting", False)
    
    if not black_screen:
        fixed align (0.5, 0.5) xysize (500, 965):
            if booting:
                add "images/interface/phone/wallpaper_1.webp" align (0.5, 0.5)
                add "images/interface/phone/intro.webp" align (0.5, 0.5)
            else:
                add f"images/interface/phone/wallpaper_{Player.phone_wallpaper + 1}.webp" align (0.5, 0.5)

                fixed anchor (0.5, 0.0) pos (0.5, 0.0) xysize (504, 42):
                    add "images/interface/phone/status.webp" align (0.5, 0.5)

                    if unread_messages:
                        add "images/interface/phone/message.webp" anchor (0.5, 0.5) pos (0.08, 0.5)

                    add "images/interface/phone/signal.webp" anchor (0.5, 0.5) pos (0.87, 0.5)

                    if time_index == 0:
                        add "images/interface/phone/battery_100.webp" anchor (0.5, 0.5) pos (0.92, 0.5)
                    elif time_index == 1:
                        add "images/interface/phone/battery_75.webp" anchor (0.5, 0.5) pos (0.92, 0.5)
                    elif time_index == 2:
                        add "images/interface/phone/battery_50.webp" anchor (0.5, 0.5) pos (0.92, 0.5)
                    elif time_index >= 3:
                        add "images/interface/phone/battery_25.webp" anchor (0.5, 0.5) pos (0.92, 0.5)

                if current_phone_screen == "home":
                    use home_screen
                elif current_phone_screen == "apps":
                    use app_screen
                elif current_phone_screen == "call_choice":
                    use call_choice_screen
                elif current_phone_screen == "call":
                    use call_screen
                elif current_phone_screen == "text_choice":
                    use text_choice_screen
                elif current_phone_screen == "text":
                    use text_screen
                elif current_phone_screen == "profile":
                    use profile_screen
                elif current_phone_screen == "music":
                    use music_screen
                # # elif current_phone_screen == "achievements":
                # #     use achievements_screen
                elif current_phone_screen == "humhum_home":
                    use humhum_home_screen
                # # elif current_phone_screen == "humhum_gallery":
                # #     use humhum_gallery_screen
                elif current_phone_screen == "humhum_choice":
                    use humhum_choice_screen
                elif current_phone_screen == "humhum":
                    use humhum_screen
                elif current_phone_screen == "config":
                    use config_screen

                if emergency_broadcast:
                    add "images/interface/phone/alert.webp" anchor (0.5, 0.5) pos (0.5, 0.5)

                fixed anchor (0.5, 1.0) pos (0.5, 1.0) xysize (500, 74):
                    add "images/interface/phone/bottom.webp"

                    hbox anchor (0.5, 0.5) pos (0.5, 0.5):
                        spacing 50

                        imagebutton:
                            if Player.phone_wallpaper in [0, 5]:
                                idle "images/interface/phone/back_idle.webp" hover "images/interface/phone/back_orange.webp"
                            elif Player.phone_wallpaper in [1]:
                                idle "images/interface/phone/back_idle.webp" hover "images/interface/phone/back_blue.webp"
                            elif Player.phone_wallpaper in [2, 3, 6]:
                                idle "images/interface/phone/back_idle.webp" hover "images/interface/phone/back_red.webp"
                            elif Player.phone_wallpaper in [4]:
                                idle "images/interface/phone/back_idle.webp" hover "images/interface/phone/back_green.webp"

                            if phone_interactable and not phone_disabled and (not current_phone_Character or not current_phone_Character.mandatory_text_options):
                                if current_phone_screen in ["call", "humhum"]:
                                    action SetVariable("current_phone_screen", current_phone_screen + "_choice")
                                elif current_phone_screen == "text":
                                    action [
                                        Function(renpy.call_in_new_context, "read_texts", current_phone_Character, override = True),
                                        SetVariable("current_phone_screen", current_phone_screen + "_choice")]
                                else:
                                    action SetVariable("current_phone_screen", "home")
                            else:
                                action None

                        imagebutton:
                            if Player.phone_wallpaper in [0, 5]:
                                idle "images/interface/phone/home_idle.webp" hover "images/interface/phone/home_orange.webp"
                            elif Player.phone_wallpaper in [1]:
                                idle "images/interface/phone/home_idle.webp" hover "images/interface/phone/home_blue.webp"
                            elif Player.phone_wallpaper in [2, 6]:
                                idle "images/interface/phone/home_idle.webp" hover "images/interface/phone/home_red.webp"
                            elif Player.phone_wallpaper in [3, 4]:
                                idle "images/interface/phone/home_idle.webp" hover "images/interface/phone/home_green.webp"

                            if phone_interactable and not phone_disabled and (not current_phone_Character or not current_phone_Character.mandatory_text_options):
                                if current_phone_screen == "home":
                                    action [
                                        Hide("phone_screen"),
                                        Call("move_location", Player.location, from_current = True)]
                                elif current_phone_screen == "text":
                                    action [
                                        Function(renpy.call_in_new_context, "read_texts", current_phone_Character, override = True),
                                        SetVariable("current_phone_screen", "home")]
                                else:
                                    action SetVariable("current_phone_screen", "home")
                            else:
                                action None

                        imagebutton:
                            if Player.phone_wallpaper in [0, 5]:
                                idle "images/interface/phone/apps_idle.webp" hover "images/interface/phone/apps_orange.webp"
                            elif Player.phone_wallpaper in [1, 3]:
                                idle "images/interface/phone/apps_idle.webp" hover "images/interface/phone/apps_blue.webp"
                            elif Player.phone_wallpaper in [2, 6]:
                                idle "images/interface/phone/apps_idle.webp" hover "images/interface/phone/apps_red.webp"
                            elif Player.phone_wallpaper in [4]:
                                idle "images/interface/phone/apps_idle.webp" hover "images/interface/phone/apps_green.webp"

                            if phone_interactable and not phone_disabled and (not current_phone_Character or not current_phone_Character.mandatory_text_options):
                                if current_phone_screen == "text":
                                    action [
                                        Function(renpy.call_in_new_context, "read_texts", current_phone_Character, override = True),
                                        SetVariable("current_phone_screen", "apps")]
                                else:                                
                                    action SetVariable("current_phone_screen", "apps")
                            else:
                                action None

            if Player.phone_cracked:
                add "images/interface/phone/cracked.webp" align (0.5, 0.5) alpha 0.2

        fixed anchor (0.5, 0.5) pos (0.498675, 0.499) xysize (577, 1080):
            add f"images/interface/phone/frame_{Player.phone_frame + 1}.webp"

    use quick_menu

screen home_screen():
    style_prefix "phone"

    $ time_of_day = time_options[time_index]
    $ day_of_week = week[weekday]

    fixed anchor (0.5, 0.5) pos (0.5, 0.4815) xysize (500, 854):
        fixed anchor (0.5, 0.5) pos (0.5, 0.08) xysize (488, 101):
            if weather:
                add f"images/interface/phone/clock_{time_index}_{weather}.webp" align (0.5, 0.5)
            else:
                add f"images/interface/phone/clock_{time_index}.webp" align (0.5, 0.5)

            text f"{temperature[time_index]} " + u"\u00b0C" anchor (0.5, 0.5) pos (0.0775, 0.28):
                color "#ffffff"
                
                size 25
            
            text f"{week[weekday][0:3]}" anchor (0.5, 0.5) pos (0.895, 0.32):
                color "#ffffff"
                
                size 45
            
            text f"{time_options[time_index].capitalize()}" anchor (0.5, 0.5) pos (0.898, 0.77):
                color "#ffffff"

                size 30

        fixed anchor (0.5, 0.5) pos (0.5, 0.195) xysize (489, 65):
            if phone_interactable and not phone_disabled:
                imagebutton align (0.5, 0.5):
                    idle "images/interface/phone/search_bar_idle.webp" hover "images/interface/phone/search_bar.webp" selected_idle "images/interface/phone/search_bar.webp"

                    selected input_cheats

                    action ToggleVariable("input_cheats")

                if input_cheats:
                    input id "input" value VariableInputValue("current_input", default = True) anchor (0.0, 0.5) pos (0.13, 0.58):
                        size 30
                        color "#000000"

                        length 25

                    key "K_RETURN" action [
                        SetVariable("input_cheats", False),
                        Call("enter_cheat_code", current_input, from_current = True)]
            else:
                add "images/interface/phone/search_bar_idle.webp" anchor (1.0, 0.5) pos (1.0, 0.5)

        if humhum_available and not humhum_hidden:
            $ humhumthread_to_display = HumHumPool.HumHumThreads[list(HumHumPool.HumHumThreads.keys())[humhum_index]]

            fixed anchor (0.5, 0.5) pos (0.5, 0.385) xysize (489, 220):
                fixed anchor (0.5, 0.0) pos (0.5, 0.0) xysize (489, 38):
                    add "images/interface/phone/home_humhum_bar.webp" align (0.5, 0.5)

                    text "#LatestHums" anchor (0.0, 0.5) pos (0.01, 0.5):
                        size 30

                        color "#d56cc4"

                    imagebutton anchor (0.5, 0.5) pos (0.82, 0.57):
                        idle "images/interface/phone/home_humhum_left_idle.webp" hover "images/interface/phone/home_humhum_left.webp"

                        if phone_interactable and not phone_disabled:
                            action [
                                SetVariable("humhum_index", (humhum_index - 1) % len(list(HumHumPool.HumHumThreads.keys()))),
                                SetVariable("humhum_yadjustment.value", 0)]
                        else:
                            action None

                    imagebutton anchor (0.5, 0.5) pos (0.94, 0.57):
                        idle "images/interface/phone/home_humhum_right_idle.webp" hover "images/interface/phone/home_humhum_right.webp"

                        if phone_interactable and not phone_disabled:
                            action [
                                SetVariable("humhum_index", (humhum_index + 1) % len(list(HumHumPool.HumHumThreads.keys()))),
                                SetVariable("humhum_yadjustment.value", 0)]
                        else:
                            action None

                fixed anchor (0.0, 1.0) pos (0.0, 1.0) xysize (453, 177):
                    add "images/interface/phone/home_humhum_box.webp"

                    if humhumthread_to_display.HumHums[0].Owner != Player:
                        add At(f"images/interface/phone/icons/{humhumthread_to_display.HumHums[0].Owner.tag}.webp", humhum_icon) anchor (0.5, 0.5) pos (0.055, 0.122)

                        text humhumthread_to_display.HumHums[0].Owner.call_sign anchor (0.0, 0.5) pos (0.125, 0.122) size 32
                    else:
                        add At(f"images/interface/phone/icons/Player_{Player.background_color}.webp", humhum_icon) anchor (0.5, 0.5) pos (0.055, 0.122)

                        text humhumthread_to_display.HumHums[0].Owner.call_sign anchor (0.0, 0.5) pos (0.125, 0.122) size 32

                    viewport id "home_humhum_viewport" yadjustment humhum_yadjustment anchor (0.0, 0.0) pos (0.0, 0.3) xysize (453, 120):
                        draggable True
                        mousewheel True

                        vbox xalign 0.5 xsize 453:
                            fixed xalign 0.5 xysize (435, 115):
                                text humhumthread_to_display.HumHums[0].body anchor (0.0, 0.0) pos (0.01, 0.015):
                                    if len(humhumthread_to_display.HumHums[0].body) > 125:
                                        size 24
                                    elif len(humhumthread_to_display.HumHums[0].body) > 100:
                                        size 26
                                    elif len(humhumthread_to_display.HumHums[0].body) > 75:
                                        size 30
                                    elif len(humhumthread_to_display.HumHums[0].body) > 50:
                                        size 34 
                                    else:
                                        size 38
                                    
                                    text_align 0.0

                            if len(humhumthread_to_display.HumHums) > 1:
                                frame xalign 0.5 xsize 453:
                                    background Frame("images/interface/phone/home_humhum_reply_box.webp", 0, 15, 0, 15)

                                    vbox xalign 0.5 xsize 453:
                                        null height 15

                                        for h in range(1, len(humhumthread_to_display.HumHums)):
                                            hbox xalign 0.5 xsize 425:
                                                if humhumthread_to_display.HumHums[h].Owner != Player:
                                                    add At(f"images/interface/phone/icons/{humhumthread_to_display.HumHums[h].Owner.tag}.webp", humhum_icon) yalign 0.0
                                                else:
                                                    add At(f"images/interface/phone/icons/Player_{Player.background_color}.webp", humhum_icon) yalign 0.0

                                                null width 8

                                                fixed yalign 0.0 xysize (375, 50):
                                                    if len(humhumthread_to_display.HumHums[h].body) > 75:
                                                        text humhumthread_to_display.HumHums[h].body align (0.0, 0.0):
                                                            size 16
                                                            
                                                            text_align 0.0
                                                    elif len(humhumthread_to_display.HumHums[h].body) > 50:
                                                        text humhumthread_to_display.HumHums[h].body align (0.0, 0.0):
                                                            size 18 
                                                            
                                                            text_align 0.0
                                                    else:
                                                        text humhumthread_to_display.HumHums[h].body align (0.0, 0.0):
                                                            size 24
                                                            
                                                            text_align 0.0
                                                            
                                            null height 4

                fixed anchor (1.0, 1.0) pos (1.0, 1.0) xysize (33, 180):
                    add "images/interface/phone/home_humhum_scrollbar_background.webp" align (0.5, 0.5)

                    vbar value YScrollValue("home_humhum_viewport") anchor (0.5, 0.5) pos (0.5, 0.5) xysize (13, 159):
                        base_bar Frame("images/interface/phone/home_humhum_scrollbar.webp")

                        thumb "images/interface/phone/home_humhum_scrollbar_thumb.webp"
                        thumb_offset 8

                        unscrollable "hide"

        imagebutton anchor (0.5, 0.5) pos (0.2, 0.85):
            idle At("images/interface/phone/icons/call_idle.webp", phone_icon) hover At("images/interface/phone/icons/call.webp", phone_icon)
            
            if phone_interactable and not phone_disabled:
                action [
                    SetVariable("loading", True),
                    SetVariable("current_phone_screen", "call_choice")]
            else:
                action None

        imagebutton anchor (0.5, 0.5) pos (0.5, 0.85):
            idle At("images/interface/phone/icons/blah_idle.webp", phone_icon) hover At("images/interface/phone/icons/blah.webp", phone_icon)
            
            if phone_interactable and not phone_disabled:
                action [
                    SetVariable("loading", True),
                    SetVariable("current_phone_screen", "text_choice")]
            else:
                action None

        imagebutton anchor (0.5, 0.5) pos (0.8, 0.85):
            idle At("images/interface/phone/icons/profile_idle.webp", phone_icon) hover At("images/interface/phone/icons/profile.webp", phone_icon)
            
            if phone_interactable and not phone_disabled:
                action [
                    SetVariable("loading", True),
                    SetVariable("current_phone_screen", "profile")]
            else:
                action None

screen app_screen():
    style_prefix "phone"

    fixed anchor (0.5, 0.5) pos (0.5, 0.4815) xysize (500, 854):
        add "images/interface/phone/app_list.webp" align (0.5, 0.5)

        text "APPS" anchor (0.0, 0.5) pos (0.02, 0.034):
            size 50

            color "#ffffff"

        imagebutton anchor (0.5, 0.5) pos (0.2, 0.2):
            idle At("images/interface/phone/icons/call_idle.webp", phone_icon) hover At("images/interface/phone/icons/call.webp", phone_icon)
            
            if phone_interactable and not phone_disabled:
                action [
                    SetVariable("loading", True),
                    SetVariable("current_phone_screen", "call_choice")]
            else:
                action None

        imagebutton anchor (0.5, 0.5) pos (0.5, 0.2):
            idle At("images/interface/phone/icons/blah_idle.webp", phone_icon) hover At("images/interface/phone/icons/blah.webp", phone_icon)
            
            if phone_interactable and not phone_disabled:
                action [
                    SetVariable("loading", True),
                    SetVariable("current_phone_screen", "text_choice")]
            else:
                action None

        imagebutton anchor (0.5, 0.5) pos (0.8, 0.2):
            idle At("images/interface/phone/icons/profile_idle.webp", phone_icon) hover At("images/interface/phone/icons/profile.webp", phone_icon)
            
            if phone_interactable and not phone_disabled:
                action [
                    SetVariable("loading", True),
                    SetVariable("current_phone_screen", "profile")]
            else:
                action None

        imagebutton anchor (0.5, 0.5) pos (0.2, 0.4):
            idle At("images/interface/phone/icons/music_idle.webp", phone_icon) hover At("images/interface/phone/icons/music.webp", phone_icon)
            
            if phone_interactable and not phone_disabled:
                action [
                    SetVariable("loading", True),
                    SetVariable("current_phone_screen", "music")]
            else:
                action None

        # imagebutton anchor (0.5, 0.5) pos (0.5, 0.4):
        #     idle At("images/interface/phone/icons/achievements_idle.webp", phone_icon) hover At("images/interface/phone/icons/achievements.webp", phone_icon)
            
        #     if phone_interactable and not phone_disabled:
        #         action SetVariable("current_phone_screen", "achievements")
        #     else:
        #         action None

        if humhum_available:
            imagebutton anchor (0.5, 0.5) pos (0.8, 0.4):
                idle At("images/interface/phone/icons/humhum_idle.webp", phone_icon) hover At("images/interface/phone/icons/humhum.webp", phone_icon)
                
                if phone_interactable and not phone_disabled:
                    action [
                        SetVariable("loading", True),
                        SetVariable("current_phone_screen", "humhum_home")]
                else:
                    action None

        imagebutton anchor (0.5, 0.5) pos (0.2, 0.85):
            idle At("images/interface/phone/icons/save_idle.webp", phone_icon) hover At("images/interface/phone/icons/save.webp", phone_icon)
            
            if phone_interactable and not phone_disabled:
                action ShowMenu("save")
            else:
                action None

        imagebutton anchor (0.5, 0.5) pos (0.5, 0.85):
            idle At("images/interface/phone/icons/load_idle.webp", phone_icon) hover At("images/interface/phone/icons/load.webp", phone_icon)
            
            if phone_interactable and not phone_disabled:
                action ShowMenu("load")
            else:
                action None

        imagebutton anchor (0.5, 0.5) pos (0.8, 0.85):
            idle At("images/interface/phone/icons/config_idle.webp", phone_icon) hover At("images/interface/phone/icons/config.webp", phone_icon)
            
            if phone_interactable and not phone_disabled:
                action [
                    SetVariable("loading", True),
                    SetVariable("current_phone_screen", "config")]
            else:
                action None

screen call_choice_screen():
    style_prefix "phone"

    fixed anchor (0.5, 0.5) pos (0.5, 0.4815) xysize (500, 854):
        add "images/interface/phone/call_contacts.webp" align (0.5, 0.5)

        add "images/interface/phone/call_top.webp" anchor (0.5, 0.0) pos (0.5, 0.0)

        text "CALL" anchor (0.0, 0.5) pos (0.15, 0.034):
            size 50

            color "#ffffff"

        text "Contact List" anchor (0.0, 0.5) pos (0.02, 0.11):
            size 40

            color "#ffffff"

        vpgrid id "call_choice_screen_viewport" anchor (0.5, 0.0) pos (0.52, 0.17) xysize (500, 698):
            cols 1

            spacing 15

            draggable True
            mousewheel True

            for C in Contacts:
                button align (0.5, 0.5) xysize (460, 100):
                    idle_background "images/interface/phone/call_contact_idle.webp" hover_background "images/interface/phone/call_contact.webp"

                    add At(f"images/interface/phone/icons/{C.tag}.webp", call_icon) anchor (0.5, 0.5) pos (0.1, 0.5)

                    text f"{C.name}" anchor (0.0, 0.5) pos (0.215, 0.5):
                        size 40

                        color "#000000"
                    
                    if phone_interactable and not phone_disabled:
                        if C.History.check("said_goodnight", tracker = "daily"):
                            action Show("say", who = None, what = "You already said goodnight.", hide_after = 5.0)
                        elif C.History.check("said_too_late_to_talk", tracker = "recent") >= 2:
                            action Show("say", who = None, what = "Maybe give it a rest.", hide_after = 5.0)
                        else:
                            if C.location != Player.location:
                                action [
                                    SetField(C, "electronic", True),
                                    SetVariable("current_phone_Character", C),
                                    SetVariable("current_phone_screen", "call"),
                                    Call("chat", C, from_current = True)]
                            else:
                                action [
                                    Hide("phone_screen"),
                                    Call("chat", C, from_current = True)]
                    else:
                        action NullAction()

        vbar value YScrollValue("call_choice_screen_viewport") anchor (0.0, 0.0) pos (0.955, 0.15) xysize (15, 698):
            base_bar Frame("images/interface/phone/call_scrollbar.webp")

            thumb "images/interface/phone/call_scrollbar_thumb.webp"
            thumb_offset 12

            unscrollable "hide"

screen call_screen():
    style_prefix "phone"

    fixed anchor (0.5, 0.5) pos (0.5, 0.4815) xysize (500, 854):
        add "images/interface/phone/call_calling.webp" align (0.5, 0.5)

        add "images/interface/phone/call_top.webp" anchor (0.5, 0.0) pos (0.5, 0.0)

        text "CALL" anchor (0.0, 0.5) pos (0.15, 0.034):
            size 50

            color "#ffffff"

        add At(f"images/interface/phone/photos/{current_phone_Character.tag}.webp", call_photo) anchor (0.5, 0.5) pos (0.5, 0.31)

        text f"Calling {current_phone_Character.name}. . ." anchor (0.0, 0.5) pos (0.15, 0.62):
            size 48

            color "#ffffff"

screen text_choice_screen():
    style_prefix "phone"

    timer 0.5 action SetVariable("loading", False)

    fixed anchor (0.5, 0.5) pos (0.5, 0.4815) xysize (500, 854):
        if loading:
            add "images/interface/phone/blah_intro.webp" align (0.5, 0.5)
        else:
            add "images/interface/phone/blah_contacts.webp" align (0.5, 0.5)

            add "images/interface/phone/blah_top.webp" anchor (0.5, 0.0) pos (0.5, 0.0)

            text "BLAH!" anchor (0.0, 0.5) pos (0.15, 0.034):
                size 50

                color "#ffffff"

            text "Contact List" anchor (0.0, 0.5) pos (0.02, 0.11):
                size 40

                color "#ffffff"

            vpgrid id "text_choice_screen_viewport" anchor (0.5, 0.0) pos (0.52, 0.17) xysize (500, 698):
                cols 1

                spacing 15

                draggable True
                mousewheel True

                for C in Contacts:
                    button align (0.5, 0.5) xysize (460, 100):
                        idle_background "images/interface/phone/blah_contact_idle.webp" hover_background "images/interface/phone/blah_contact.webp" selected_idle_background "images/interface/phone/blah_contact.webp"

                        selected C in unread_messages.keys()

                        add At(f"images/interface/phone/icons/{C.tag}.webp", call_icon) anchor (0.5, 0.5) pos (0.1, 0.5)

                        text f"{C.name}" anchor (0.0, 0.5) pos (0.215, 0.5):
                            size 40

                            color "#000000"
                        
                        if phone_interactable and not phone_disabled:
                            action [
                                SetVariable("current_phone_Character", C),
                                SetVariable("current_phone_screen", "text")]
                        else:
                            action NullAction()

            vbar value YScrollValue("text_choice_screen_viewport") anchor (0.0, 0.0) pos (0.955, 0.15) xysize (15, 698):
                base_bar Frame("images/interface/phone/blah_scrollbar.webp")

                thumb "images/interface/phone/blah_scrollbar_thumb.webp"
                thumb_offset 12

                unscrollable "hide"

screen text_screen():
    style_prefix "phone"

    fixed anchor (0.5, 0.5) pos (0.5, 0.4815) xysize (500, 854):
        add "images/interface/phone/blah_message.webp" anchor (0.5, 0.5) pos (0.5, 0.508)

        add "images/interface/phone/blah_top.webp" anchor (0.5, 0.0) pos (0.5, 0.0)

        text "BLAH!" anchor (0.0, 0.5) pos (0.15, 0.034):
            size 50

            color "#ffffff"

        if current_phone_Character in Contacts:
            text f"Chatting with {current_phone_Character.name}" anchor (0.0, 0.5) pos (0.02, 0.11):
                size 40

                color "#ffffff"
        else:
            text f"Chatting with Unknown Number" anchor (0.0, 0.5) pos (0.02, 0.11):
                size 40

                color "#ffffff"

        use text_history(current_phone_Character)

    if current_phone_Character.mandatory_text_options or (phone_interactable and not phone_disabled and current_phone_Character not in Present and (not "bg_shower" in Player.location or current_phone_Character.location != Player.location.replace("_shower", ""))):
        $ text_options = []
        
        if current_phone_Character.mandatory_text_options:
            $ text_options = current_phone_Character.mandatory_text_options[:]
        elif not current_phone_Character.History.check("said_too_late_to_text", tracker = "recent") > 2:
            if not current_phone_Character.History.check("said_goodnight", tracker = "recent"):
                python:
                    for text in reversed(current_phone_Character.text_options):
                        if "date" in text and (current_phone_Character.History.check("said_no_to_date", tracker = "recent") or current_phone_Character in Player.date_planned.keys()):
                            pass
                        else:
                            text_options.insert(0, text)

                if current_phone_Character in all_Companions and time_index < 2 and current_phone_Character not in Player.date_planned.keys() and not current_phone_Character.History.check("said_no_to_date", tracker = "recent") and current_phone_Character.History.check("went_on_date_with_Player"):
                    $ text_options.insert(0, "want to go on a date tonight?")

                if current_phone_Character in all_Companions and current_phone_Character.History.check("said_no_to_summon", tracker = "recent") < 3 and not current_phone_Character.History.check("said_no_to_studying", tracker = "recent") and not current_phone_Character.History.check("said_no_to_training", tracker = "recent") and not current_phone_Character.History.check('rejected_knock_on_door', tracker = 'recent'):
                    $ text_options.insert(0, "wanna come over?")

                if not current_phone_Character.History.check("sent_how_are_you_text", tracker = "daily"):
                    if current_phone_Character in all_Companions:
                        $ text_options.insert(0, "how are you?")
                    elif current_phone_Character in [Kurt]:
                        $ text_options.insert(0, "how's it going?")

                if current_phone_Character in all_Companions:
                    if time_index == 0:
                        if not current_phone_Character.History.check("talked_with_Player", tracker = "daily") and not current_phone_Character.History.check("texted_with_Player", tracker = "daily"):
                            $ text_options.insert(0, "good morning!")
                    elif time_index == 3:
                        $ text_options.insert(0, "goodnight!")
                        
            if current_phone_Character.timed_text_options:
                python:
                    for E in current_phone_Character.timed_text_options.keys():
                        for text in reversed(current_phone_Character.timed_text_options[E]):
                            text_options.insert(0, text)

        viewport anchor (0.0, 0.5) pos (1.15, 0.5) xysize (480, 600):
            draggable True
            mousewheel True
            xfill True
            yfill True

            yinitial 0.0
            
            vbox align (0.0, 0.0):
                xfill True

                if current_phone_Character.location != "hold": 
                    for message in text_options:
                        button xalign 0.0:
                            idle_background Frame("images/interface/phone/text_frame_Player_idle.webp", 30, 30)
                            hover_background Frame("images/interface/phone/text_frame_Player.webp", 30, 30)

                            activate_sound None

                            padding (15, 15, 15, 15)
                            minimum (100, 0)
                            xmaximum 300

                            text message align (0.5, 0.5):
                                size 32

                            if current_phone_Character.mandatory_text_options:
                                action Call("send_text", current_phone_Character, message)
                            else:
                                action Call("send_text", current_phone_Character, message, from_current = True)

screen text_history(Character):
    style_prefix "phone"

    python:
        text_screen_yadjustment.value = float("inf")

    $ previous_Owner = None

    $ last_status = None

    viewport yadjustment text_screen_yadjustment anchor (0.5, 0.0) pos (0.5, 0.17) xysize (440, 610):
        draggable True
        mousewheel True

        yinitial 1.0
    
        vbox align (0.0, 0.0) xsize 440:
            spacing 5

            for Owner, content, status in Character.text_history:
                if last_status == "read" and status in ["unread", "current", "recently_read"]:
                    add "images/interface/phone/texts_end.webp" xalign 0.5

                if Owner != Player:
                    hbox align (0.0, 0.0):
                        spacing 5

                        if previous_Owner != Owner.tag:
                            add At(f"images/interface/phone/icons/{Owner.tag}.webp", humhum_icon):
                                if status == "current":
                                    at message_appear_icon()
                        else:
                            null width 45

                        vbox align (0.0, 0.5):
                            if previous_Owner != Owner.tag and Owner in Contacts:
                                text Owner.name:
                                    size 30

                            frame:
                                background Frame("images/interface/phone/text_frame.webp", 30, 30)

                                padding (15, 15, 15, 15)
                                minimum (50, 0)
                                xmaximum 375

                                if status == "current":
                                    at message_appear(-1)

                                text content:
                                    text_align 0.0

                                    size 30

                                    if Owner.tag in Cast:
                                        color eval(f"{Owner.tag}_color")
                                    else:
                                        color "#000000"
                else:
                    hbox align (1.0, 0.0):
                        spacing 5

                        box_reverse True

                        if previous_Owner != Owner.tag:
                            add At(f"images/interface/phone/icons/Player_{Player.background_color}.webp", humhum_icon):
                                if status == "current":
                                    at message_appear_icon()
                        else:
                            null width 45

                        vbox align (1.0, 0.5):
                            frame:
                                background Frame("images/interface/phone/text_frame_Player.webp", 30, 30)

                                padding (15, 15, 15, 15)
                                minimum (50, 0)
                                xmaximum 375

                                if status == "current":
                                    at message_appear(1)

                                text content:
                                    text_align 1.0

                                    size 30
                                
                $ previous_Owner = Owner.tag

                $ last_status = status

screen profile_screen():
    style_prefix "phone"

    fixed anchor (0.5, 0.5) pos (0.5, 0.4815) xysize (500, 854):
        add "images/interface/phone/profile_background.webp" align (0.5, 0.5)

        text "PROFILE" anchor (0.0, 0.5) pos (0.15, 0.034):
            size 50

            color "#ffffff"

        add At("Player_portrait", humhum_photo) pos (0.275, 0.285) zoom 0.7

        text "Name" anchor (0.0, 0.5) pos (0.52, 0.21) size 32

        text f"{Player.first_name} {Player.last_name[0]}." anchor (1.0, 0.5) pos (0.92, 0.21) size 32
        
        text "XP" anchor (0.0, 0.5) pos (0.075, 0.562) size 32

        bar value Player.XP - int(Player.XP_goal/1.75) range Player.XP_goal - int(Player.XP_goal/1.75) anchor (0.0, 0.5) pos (0.175, 0.5625) xysize (372, 26):
            left_bar Frame("images/interface/phone/profile_xp.webp")
            right_bar Frame("images/interface/phone/profile_xp_empty.webp")

            thumb None
                
        text "Mutation Level" anchor (0.0, 0.5) pos (0.074, 0.635) size 32

        text f"{Player.level}" anchor (1.0, 0.5) pos (0.915, 0.635) size 32

        text "Stamina" anchor (0.0, 0.5) pos (0.074, 0.702) size 32

        hbox anchor (0.0, 0.5) pos (0.28, 0.707):
            for i in range(Player.stamina):
                add "images/interface/phone/profile_stamina.webp"

            for i in range(Player.max_stamina - Player.stamina):
                add "images/interface/phone/profile_stamina_empty.webp"

screen music_screen():
    style_prefix "phone"

    $ file_list = renpy.list_files()
    $ song_list = []
    $ current_song = 0
    
    for file in file_list:
        if len(file.split("/")) > 1 and file.split("/")[-2] == "music":
            if file.split("/")[-1].split(".")[0] in available_songs:
                $ song_list.append(file)

    for f, file in enumerate(song_list):
        if file == renpy.music.get_playing():
            $ current_song = f

    fixed anchor (0.5, 0.5) pos (0.5, 0.4815) xysize (500, 854):
        add "images/interface/phone/music_background.webp" align (0.5, 0.5)

        text "MUSIC PLAYER" anchor (0.0, 0.5) pos (0.15, 0.034):
            size 50

            color "#ffffff"

        if renpy.music.get_playing():
            text renpy.music.get_playing().split("/")[-1].split(".")[0] anchor (0.0, 0.5) pos (0.32, 0.125):
                size 45

            bar value AudioPositionValue(channel = 'music') anchor (0.0, 0.5) pos (0.32, 0.175) xysize (288, 8):
                left_bar "images/interface/phone/music_bar.webp"
                right_bar "images/interface/phone/music_bar_empty.webp"

                thumb None
                thumb_offset 0

        hbox anchor (0.5, 0.5) pos (0.5, 0.2715) xysize (425, 75):
            spacing 5

            imagebutton:
                idle "images/interface/phone/music_shuffle_idle.webp" hover "images/interface/phone/music_shuffle.webp"

                if phone_interactable and not phone_disabled:
                    action Play("music", song_list[(renpy.random.randint(0, len(song_list))) % len(song_list)], loop = repeating)
                else:
                    action None

            imagebutton:
                idle "images/interface/phone/music_left_idle.webp" hover "images/interface/phone/music_left.webp"
                
                if phone_interactable and not phone_disabled:
                    action Play("music", song_list[(current_song - 1) % len(song_list)], loop = repeating)
                else:
                    action None

            if renpy.music.get_pause():
                imagebutton:
                    idle "images/interface/phone/music_play.webp" hover "images/interface/phone/music_pause.webp"
                    
                    if phone_interactable and not phone_disabled:
                        action PauseAudio("music", value = False)
                    else:
                        action None
            else:
                imagebutton:
                    idle "images/interface/phone/music_pause.webp" hover "images/interface/phone/music_play.webp"
                    
                    if phone_interactable and not phone_disabled:
                        action PauseAudio("music", value = True)
                    else:
                        action None

            imagebutton:
                idle "images/interface/phone/music_right_idle.webp" hover "images/interface/phone/music_right.webp"
                
                if phone_interactable and not phone_disabled:
                    action Play("music", song_list[(current_song + 1) % len(song_list)], loop = repeating)
                else:
                    action None

            imagebutton:
                idle "images/interface/phone/music_repeat_idle.webp" hover "images/interface/phone/music_repeat.webp" selected_idle "images/interface/phone/music_repeat.webp"
                
                selected repeating

                if phone_interactable and not phone_disabled:
                    if repeating:
                        action [
                            Play("music", song_list[current_song], loop = False),
                            SetVariable("repeating", False)]
                    else:
                        action [
                            Play("music", song_list[current_song], loop = True),
                            SetVariable("repeating", True)]
                else:
                    action None

        viewport id "music_screen_viewport" anchor (0.5, 0.0) pos (0.54, 0.375) xysize (500, 500):
            draggable True
            mousewheel True

            vbox:
                spacing 10

                for file in song_list:
                    button xalign 0.0 xysize (424, 70):
                        idle_background "images/interface/phone/music_song_idle.webp" hover_background "images/interface/phone/music_song.webp" selected_idle_background "images/interface/phone/music_song.webp"

                        selected file == renpy.music.get_playing()

                        text file.split("/")[-1].split(".")[0] anchor (0.0, 0.5) pos (0.1, 0.5):
                            size 32

                        if phone_interactable and not phone_disabled:
                            action Play("music", file, loop = repeating)
                        else:
                            action None

        vbar value YScrollValue("music_screen_viewport") anchor (0.0, 0.0) pos (0.92, 0.375) xysize (15, 500):
            base_bar Frame("images/interface/phone/music_scrollbar.webp")

            thumb "images/interface/phone/music_scrollbar_thumb.webp"
            thumb_offset 12

            unscrollable "hide"

screen humhum_home_screen():
    style_prefix "phone"

    timer 0.5 action SetVariable("loading", False)

    fixed anchor (0.5, 0.5) pos (0.5, 0.4815) xysize (500, 854):
        if loading:
            add "humhum_animation" align (0.5, 0.5)
        else:
            add "images/interface/phone/humhum_background.webp" align (0.5, 0.5)

            text "HUMHUM" anchor (0.0, 0.5) pos (0.15, 0.034):
                size 50

                color "#ffffff"

            viewport id "humhum_home_screen_viewport" anchor (0.5, 0.0) pos (0.5, 0.11) xysize (475, 625):
                draggable True
                mousewheel True
            
                vbox xalign 0.5 xsize 453:
                    for H in HumHumPool.HumHumThreads.values():
                        fixed xalign 0.5 xsize 453:
                            yfit True
                            
                            add "images/interface/phone/home_humhum_box.webp"

                            if H.HumHums[0].Owner != Player:
                                add At(f"images/interface/phone/icons/{H.HumHums[0].Owner.tag}.webp", humhum_icon) anchor (0.5, 0.5) pos (0.055, 22)

                                text H.HumHums[0].Owner.call_sign anchor (0.0, 0.5) pos (0.125, 22) size 32
                            else:
                                add At(f"images/interface/phone/icons/Player_{Player.background_color}.webp", humhum_icon) anchor (0.5, 0.5) pos (0.055, 22)

                                text H.HumHums[0].Owner.call_sign anchor (0.0, 0.5) pos (0.125, 22) size 32

                            fixed anchor (0.5, 0.0) pos (0.5, 53) xysize (435, 115):
                                text H.HumHums[0].body anchor (0.0, 0.0) pos (0.01, 0.015): 
                                    if len(H.HumHums[0].body) > 125:
                                        size 24
                                    elif len(H.HumHums[0].body) > 100:
                                        size 26
                                    elif len(H.HumHums[0].body) > 75:
                                        size 30
                                    elif len(H.HumHums[0].body) > 50:
                                        size 34 
                                    else:
                                        size 38
                                    
                                    text_align 0.0

                            if len(H.HumHums) > 1:
                                frame anchor (0.5, 0.0) pos (0.5, 170) xsize 453:
                                    background Frame("images/interface/phone/home_humhum_reply_box.webp", 0, 15, 0, 15)

                                    vbox xalign 0.5 xsize 453:
                                        null height 15

                                        for h in range(1, len(H.HumHums)):
                                            hbox xalign 0.5 xsize 425:
                                                if H.HumHums[h].Owner != Player:
                                                    add At(f"images/interface/phone/icons/{H.HumHums[h].Owner.tag}.webp", humhum_icon) yalign 0.0
                                                else:
                                                    add At(f"images/interface/phone/icons/Player_{Player.background_color}.webp", humhum_icon) yalign 0.0

                                                null width 8

                                                fixed yalign 0.0 xysize (375, 50):
                                                    if len(H.HumHums[h].body) > 75:
                                                        text H.HumHums[h].body align (0.0, 0.0):
                                                            size 16
                                                            
                                                            text_align 0.0
                                                    elif len(H.HumHums[h].body) > 50:
                                                        text H.HumHums[h].body align (0.0, 0.0):
                                                            size 18 
                                                            
                                                            text_align 0.0
                                                    else:
                                                        text H.HumHums[h].body align (0.0, 0.0):
                                                            size 24
                                                            
                                                            text_align 0.0
                                                            
                                            null height 4

                        null height 15

            vbar value YScrollValue("humhum_home_screen_viewport") anchor (0.0, 0.0) pos (0.95, 0.11) xysize (13, 625):
                base_bar Frame("images/interface/phone/humhum_scrollbar.webp")

                thumb "images/interface/phone/humhum_scrollbar_thumb.webp"
                thumb_offset 12

                unscrollable "hide"

            fixed anchor (0.5, 1.0) pos (0.5, 1.0) xysize (500, 103):
                add "images/interface/phone/humhum_bar.webp" align (0.5, 0.5)

                hbox anchor (0.5, 0.5) pos (0.5, 0.5):
                    spacing 50

                    imagebutton:
                        idle "images/interface/phone/humhum_home.webp" hover "images/interface/phone/humhum_home.webp"

                        if phone_interactable and not phone_disabled:
                            action SetVariable("current_phone_screen", "humhum_home")
                        else:
                            action None

                    # imagebutton:
                    #     idle "images/interface/phone/humhum_gallery_idle.webp" hover "images/interface/phone/humhum_gallery.webp"

                    #     if phone_interactable and not phone_disabled:
                    #         action SetVariable("current_phone_screen", "humhum_gallery")
                    #     else:
                    #         action None

                    null width 44

                    imagebutton:
                        idle "images/interface/phone/humhum_friends_idle.webp" hover "images/interface/phone/humhum_friends.webp"

                        if phone_interactable and not phone_disabled:
                            action SetVariable("current_phone_screen", "humhum_choice")
                        else:
                            action None

screen humhum_choice_screen():
    style_prefix "phone"

    fixed anchor (0.5, 0.5) pos (0.5, 0.4815) xysize (500, 854):
        add "images/interface/phone/humhum_background.webp" align (0.5, 0.5)

        text "HUMHUM" anchor (0.0, 0.5) pos (0.15, 0.034):
            size 50

            color "#ffffff"

        vpgrid id "humhum_choice_screen_viewport" anchor (0.5, 0.0) pos (0.5, 0.1) xysize (450, 625):
            cols 3

            spacing 0

            xfill True

            draggable True
            mousewheel True

            for G in active_Companions:
                imagebutton align (0.5, 0.5):
                    idle At(f"images/interface/phone/icons/{G.tag}_idle.webp", phone_icon) hover At(f"images/interface/phone/icons/{G.tag}.webp", phone_icon)
                    
                    if phone_interactable and not phone_disabled:
                        action [
                            SetVariable("current_phone_Character", G),
                            SetVariable("current_phone_screen", "humhum")]
                    else:
                        action None

        vbar value YScrollValue("humhum_choice_screen_viewport") anchor (0.0, 0.0) pos (0.945, 0.1) xysize (13, 625):
            base_bar Frame("images/interface/phone/humhum_scrollbar.webp")

            thumb "images/interface/phone/humhum_scrollbar_thumb.webp"
            thumb_offset 12

            unscrollable "hide"

        fixed anchor (0.5, 1.0) pos (0.5, 1.0) xysize (500, 103):
            add "images/interface/phone/humhum_bar.webp" align (0.5, 0.5)

            hbox anchor (0.5, 0.5) pos (0.5, 0.5):
                spacing 50

                imagebutton:
                    idle "images/interface/phone/humhum_home_idle.webp" hover "images/interface/phone/humhum_home.webp"

                    if phone_interactable and not phone_disabled:
                        action SetVariable("current_phone_screen", "humhum_home")
                    else:
                        action None

                # imagebutton:
                #     idle "images/interface/phone/humhum_gallery_idle.webp" hover "images/interface/phone/humhum_gallery.webp"

                #     if phone_interactable and not phone_disabled:
                #         action SetVariable("current_phone_screen", "humhum_gallery")
                #     else:
                #         action None

                null width 44

                imagebutton:
                    idle "images/interface/phone/humhum_friends.webp" hover "images/interface/phone/humhum_friends.webp"

                    if phone_interactable and not phone_disabled:
                        action SetVariable("current_phone_screen", "humhum_choice")
                    else:
                        action None

screen humhum_screen():
    style_prefix "phone"

    fixed anchor (0.5, 0.5) pos (0.5, 0.4815) xysize (500, 854):
        add "images/interface/phone/humhum_background.webp" align (0.5, 0.5)

        text "HUMHUM" anchor (0.0, 0.5) pos (0.15, 0.034):
            size 50

            color "#ffffff"

        add "images/interface/phone/humhum_profile_background.webp" anchor (0.5, 0.0) pos (0.5, 0.1)

        add At(f"images/interface/phone/photos/{current_phone_Character.tag}.webp", humhum_photo) anchor (0.5, 0.5) pos (0.25, 0.308)

        if current_phone_Character.status["miffed"] or current_phone_Character.status["mad"]:
            add "images/interface/phone/humhum_status_angry.webp" anchor (0.5, 0.5) pos (0.071, 0.548)

        if current_phone_Character.status["horny"] or current_phone_Character.status["nympho"]:
            add "images/interface/phone/humhum_status_nympho.webp" anchor (0.5, 0.5) pos (0.186, 0.548)

        for s, status in enumerate(["heartbroken"]):
            if current_phone_Character.status[status]:
                add f"images/interface/phone/humhum_status_{status}.webp" anchor (0.5, 0.5) pos (0.301 + s*0.115, 0.548)

        text "Name" anchor (0.0, 0.5) pos (0.51, 0.135) size 30

        if len(current_phone_Character.name) < 10:
            text f"{current_phone_Character.name}" anchor (1.0, 0.5) pos (0.95, 0.135) size 30 
        else:
            text f"{current_phone_Character.name}" anchor (1.0, 0.5) pos (0.95, 0.135) size 25 
                
        text "Love" anchor (0.0, 0.5) pos (0.51, 0.215) size 30

        text f"{current_phone_Character.love}" anchor (1.0, 0.5) pos (0.95, 0.215) size 30 
                
        text "Trust" anchor (0.0, 0.5) pos (0.51, 0.297) size 30

        text f"{current_phone_Character.trust}" anchor (1.0, 0.5) pos (0.95, 0.297) size 30

        text "Favorite Gift" anchor (0.0, 0.5) pos (0.51, 0.378) size 30

        text "Relationship Status" anchor (0.0, 0.5) pos (0.04, 0.627) size 28

        if current_phone_Character not in Partners:
            text "Single" anchor (1.0, 0.5) pos (0.95, 0.627) size 30
        elif len(Partners) > 2:
            text "Polyamorous" anchor (1.0, 0.5) pos (0.95, 0.627) size 30
        else:
            text "In a relationship" anchor (1.0, 0.5) pos (0.95, 0.627) size 30

        text "Your Petname" anchor (0.0, 0.5) pos (0.04, 0.707) size 28

        text f"{current_phone_Character.Player_petname}" anchor (1.0, 0.5) pos (0.95, 0.707) size 30

        text "Her Petname" anchor (0.0, 0.5) pos (0.04, 0.787) size 28

        text f"{current_phone_Character.petname}" anchor (1.0, 0.5) pos (0.95, 0.787) size 30

        fixed anchor (0.5, 1.0) pos (0.5, 1.0) xysize (500, 103):
            add "images/interface/phone/humhum_bar.webp" align (0.5, 0.5)

            hbox anchor (0.5, 0.5) pos (0.5, 0.5):
                spacing 50

                imagebutton:
                    idle "images/interface/phone/humhum_home_idle.webp" hover "images/interface/phone/humhum_home.webp"

                    if phone_interactable and not phone_disabled:
                        action SetVariable("current_phone_screen", "humhum_home")
                    else:
                        action None

                # imagebutton:
                #     idle "images/interface/phone/humhum_gallery_idle.webp" hover "images/interface/phone/humhum_gallery.webp"

                #     if phone_interactable and not phone_disabled:
                #         action SetVariable("current_phone_screen", "humhum_gallery")
                #     else:
                #         action None

                null width 44

                imagebutton:
                    idle "images/interface/phone/humhum_friends.webp" hover "images/interface/phone/humhum_friends.webp"

                    if phone_interactable and not phone_disabled:
                        action SetVariable("current_phone_screen", "humhum_choice")
                    else:
                        action None

screen config_screen():
    style_prefix "phone"

    fixed anchor (0.5, 0.5) pos (0.5, 0.4815) xysize (500, 854):
        add "images/interface/phone/config_background.webp" align (0.5, 0.5)

        text "CONFIGURATION" anchor (0.0, 0.5) pos (0.15, 0.034):
            size 50

            color "#ffffff"

        vbox anchor (0.5, 0.0) pos (0.5, 0.15) xysize (494, 650):
            xfill True

            fixed xalign 0.5 xysize (465, 57):
                add "images/interface/phone/config_box.webp" align (0.5, 0.5)

                text "Cellphone Frame" align (0.5, 0.5):
                    size 32

            fixed xalign 0.5 xysize (320, 64):
                imagebutton anchor (0.0, 0.5) pos (0.0, 0.5):
                    idle "images/interface/Player_customization/left_idle.webp" hover "images/interface/Player_customization/left.webp"

                    action SetVariable("Player.phone_frame", (Player.phone_frame - 1) % 7)

                text f"TYPE {Player.phone_frame + 1}" align (0.5, 0.5):
                    size 32

                imagebutton anchor (1.0, 0.5) pos (1.0, 0.5):
                    idle "images/interface/Player_customization/right_idle.webp" hover "images/interface/Player_customization/right.webp"

                    action SetVariable("Player.phone_frame", (Player.phone_frame + 1) % 7)

            fixed xalign 0.5 xysize (465, 57):
                add "images/interface/phone/config_box.webp" align (0.5, 0.5)

                text "Cellphone Wallpaper" align (0.5, 0.5):
                    size 32

            fixed xalign 0.5 xysize (320, 64):
                imagebutton anchor (0.0, 0.5) pos (0.0, 0.5):
                    idle "images/interface/Player_customization/left_idle.webp" hover "images/interface/Player_customization/left.webp"

                    action SetVariable("Player.phone_wallpaper", (Player.phone_wallpaper - 1) % 7)

                $ wallpaper_type = [
                    "Orange",
                    "Blue",
                    "Red",
                    "Galaxy",
                    f"{Rogue.name}",
                    f"{Laura.name}",
                    f"{Jean.name}"]

                text wallpaper_type[Player.phone_wallpaper] align (0.5, 0.5):
                    size 32

                imagebutton anchor (1.0, 0.5) pos (1.0, 0.5):
                    idle "images/interface/Player_customization/right_idle.webp" hover "images/interface/Player_customization/right.webp"

                    action SetVariable("Player.phone_wallpaper", (Player.phone_wallpaper + 1) % 7)

            fixed xalign 0.5 xysize (465, 57):
                add "images/interface/phone/config_box.webp" align (0.5, 0.5)

                text "Hide HumHum Home Widget" align (0.5, 0.5):
                    size 32

            fixed xalign 0.5 xysize (320, 64):
                imagebutton anchor (0.0, 0.5) pos (0.0, 0.5):
                    idle "images/interface/Player_customization/left_idle.webp" hover "images/interface/Player_customization/left.webp"

                    action ToggleVariable("humhum_hidden")

                if humhum_hidden:
                    text "YES" align (0.5, 0.5):
                        size 32
                else:
                    text "NO" align (0.5, 0.5):
                        size 32

                imagebutton anchor (1.0, 0.5) pos (1.0, 0.5):
                    idle "images/interface/Player_customization/right_idle.webp" hover "images/interface/Player_customization/right.webp"

                    action ToggleVariable("humhum_hidden")

            fixed xalign 0.5 xysize (465, 57):
                add "images/interface/phone/config_box.webp" align (0.5, 0.5)

                text "Cellphone Ringtone" align (0.5, 0.5):
                    size 32

            fixed xalign 0.5 xysize (320, 64):
                imagebutton anchor (0.0, 0.5) pos (0.0, 0.5):
                    idle "images/interface/Player_customization/left_idle.webp" hover "images/interface/Player_customization/left.webp"

                    action [
                        Play("sound", f"sounds/ringtones/{(Player.ringtone - 1) % len(available_ringtones)}.ogg"),
                        SetVariable("Player.ringtone", (Player.ringtone - 1) % len(available_ringtones))]

                text f"TYPE {Player.ringtone + 1}" align (0.5, 0.5):
                    size 32

                imagebutton anchor (1.0, 0.5) pos (1.0, 0.5):
                    idle "images/interface/Player_customization/right_idle.webp" hover "images/interface/Player_customization/right.webp"

                    action [
                        Play("sound", f"sounds/ringtones/{(Player.ringtone + 1) % len(available_ringtones)}.ogg"),
                        SetVariable("Player.ringtone", (Player.ringtone + 1) % len(available_ringtones))]