init -1:
    
    default phone_interactable = False
    default phone_disabled = False
    
    default booting = False
    default loading = False

    default current_phone_screen = "home"
    default current_phone_Character = None

    default wallpaper_index = 0

    default input_cheats = False

    default humhum_available = False
    default humhum_hidden = False
    default humhum_index = -1
    default humhum_yadjustment = ui.adjustment()

    default unread_messages = {}
    default blah_yadjustment = ui.adjustment()

    default daily_bungle_ad = 1
    default daily_bungle_Article = None
    default daily_bungle_yadjustment = ui.adjustment()

    default current_vibrator_index = 0

    default available_songs = []
    default available_ringtones = []
    default music_repeating = True

    default waiting = 0

    default emergency_broadcast = False

transform message_appear(direction):
    xoffset 50*direction alpha 0.0

    parallel:
        ease 0.5 alpha 1.0
    parallel:
        easein_back 0.5 xoffset 0

transform message_appear_icon:
    zoom 0.0
    easein_back 0.5 zoom 1.0

layeredimage humhum_animation1:
    always:
        "images/interface/phone/humhum_animation_background.webp"

    always:
        "images/interface/phone/humhum_animation_open.webp"

layeredimage humhum_animation2:
    always:
        "images/interface/phone/humhum_animation_background.webp"

    always:
        "images/interface/phone/humhum_animation_closed.webp"
    
    always:
        "images/interface/phone/humhum_animation_hum.webp"

layeredimage humhum_animation3:
    always:
        "images/interface/phone/humhum_animation_background.webp"

    always:
        "images/interface/phone/humhum_animation_open.webp"
    
    always:
        "images/interface/phone/humhum_animation_humhum.webp"

image humhum_animation:
    "humhum_animation1"
    pause 0.15
    "humhum_animation2"
    pause 0.15
    "humhum_animation3"
    pause 0.15
    repeat

image achievements_animation:
    "images/interface/phone/achievements_animation_frame1.webp"
    pause 0.5
    "images/interface/phone/achievements_animation_frame2.webp"
    pause 0.5
    # "images/interface/phone/achievements_animation_frame3.webp"
    # pause 0.5
    repeat

style phone is default

style phone_button:
    activate_sound "sounds/interface/phone.ogg"

style phone_image_button:
    activate_sound "sounds/interface/phone.ogg"

style phone_text:
    font "agency_fb.ttf"

    color "#000000"

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
        if booting:
            add At(f"images/interface/phone/wallpaper_{Player.phone_wallpaper}.webp", interface)
            add At("images/interface/phone/intro.webp", interface)
        else:
            add At(f"images/interface/phone/wallpaper_{Player.phone_wallpaper}.webp", interface)

            add At("images/interface/phone/status.webp", interface)

            if unread_messages:
                add At("images/interface/phone/message.webp", interface)

            add At("images/interface/phone/signal.webp", interface)

            if time_index == 0:
                add At("images/interface/phone/battery_100.webp", interface)
            elif time_index == 1:
                add At("images/interface/phone/battery_75.webp", interface)
            elif time_index == 2:
                add At("images/interface/phone/battery_50.webp", interface)
            elif time_index >= 3:
                add At("images/interface/phone/battery_25.webp", interface)

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
            elif current_phone_screen == "humhum_home":
                use humhum_home_screen
            # elif current_phone_screen == "humhum_gallery":
            #     use humhum_gallery_screen
            elif current_phone_screen == "humhum_choice":
                use humhum_choice_screen
            elif current_phone_screen == "humhum":
                use humhum_screen
            elif current_phone_screen == "news":
                use news_screen
            elif current_phone_screen == "remote":
                use remote_screen
            elif current_phone_screen == "achievements_home":
                use achievements_home_screen
            elif current_phone_screen == "achievements_list":
                use achievements_list_screen
            # elif current_phone_screen == "achievements_shop":
            #     use achievements_shop_screen
            elif current_phone_screen == "music":
                use music_screen
            elif current_phone_screen == "config":
                use config_screen

            if emergency_broadcast:
                add "images/interface/phone/alert.webp" align (0.5, 0.5)

            add At("images/interface/phone/bottom.webp", interface)

            imagebutton:
                idle At("images/interface/phone/back_idle.webp" , interface)

                if Player.phone_wallpaper in [1, "Laura"]:
                    hover At("images/interface/phone/back_orange.webp", interface)
                elif Player.phone_wallpaper in [2]:
                    hover At("images/interface/phone/back_blue.webp", interface)
                elif Player.phone_wallpaper in [3, 4, "Jean"]:
                    hover At("images/interface/phone/back_red.webp", interface)
                elif Player.phone_wallpaper in ["Rogue"]:
                    hover At("images/interface/phone/back_green.webp", interface)

                if phone_interactable and not phone_disabled and (not current_phone_Character or not current_phone_Character.mandatory_text_options):
                    if current_phone_screen in ["call", "humhum"]:
                        action [
                            SetVariable("current_phone_screen", current_phone_screen + "_choice"),
                            Call("set_music", from_current = True)]
                    elif current_phone_screen == "text":
                        action [
                            Function(renpy.call_in_new_context, "read_texts", current_phone_Character, override = True),
                            SetVariable("current_phone_screen", current_phone_screen + "_choice"),
                            Call("set_music", from_current = True)]
                    elif current_phone_screen in ["achievements_list", "achievements_shop"]:
                        action SetVariable("current_phone_screen", "achievements_home")
                    else:
                        action [
                            SetVariable("current_phone_screen", "home"),
                            Call("set_music", from_current = True)]
                else:
                    action None

            imagebutton:
                idle At("images/interface/phone/home_idle.webp", interface)

                if Player.phone_wallpaper in [1, "Laura"]:
                    hover At("images/interface/phone/home_orange.webp", interface)
                elif Player.phone_wallpaper in [2]:
                    hover At("images/interface/phone/home_blue.webp", interface)
                elif Player.phone_wallpaper in [3, "Jean"]:
                    hover At("images/interface/phone/home_red.webp", interface)
                elif Player.phone_wallpaper in [4, "Rogue"]:
                    hover At("images/interface/phone/home_green.webp", interface)

                if phone_interactable and not phone_disabled and (not current_phone_Character or not current_phone_Character.mandatory_text_options):
                    if current_phone_screen == "home":
                        action [
                            Hide("phone_screen"),
                            Call("move_location", Player.location, from_current = True)]
                    elif current_phone_screen == "text":
                        action [
                            Function(renpy.call_in_new_context, "read_texts", current_phone_Character, override = True),
                            SetVariable("current_phone_screen", "home"),
                            Call("set_music", from_current = True)]
                    else:
                        action [
                            SetVariable("current_phone_screen", "home"),
                            Call("set_music", from_current = True)]
                else:
                    action None

            imagebutton:
                idle At("images/interface/phone/apps_idle.webp", interface)

                if Player.phone_wallpaper in [1, "Laura"]:
                    hover At("images/interface/phone/apps_orange.webp", interface)
                elif Player.phone_wallpaper in [2, 4]:
                    hover At("images/interface/phone/apps_blue.webp", interface)
                elif Player.phone_wallpaper in [3, "Jean"]:
                    hover At("images/interface/phone/apps_red.webp", interface)
                elif Player.phone_wallpaper in ["Rogue"]:
                    hover At("images/interface/phone/apps_green.webp", interface)

                if phone_interactable and not phone_disabled and (not current_phone_Character or not current_phone_Character.mandatory_text_options):
                    if current_phone_screen == "text":
                        action [
                            Function(renpy.call_in_new_context, "read_texts", current_phone_Character, override = True),
                            SetVariable("current_phone_screen", "apps"),
                            Call("set_music", from_current = True)]
                    else:                                
                        action [
                            SetVariable("current_phone_screen", "apps"),
                            Call("set_music", from_current = True)]
                else:
                    action None

        if Player.phone_cracked:
            add At("images/interface/phone/cracked.webp", interface) alpha 0.2

        add At(f"images/interface/phone/frame_{Player.phone_frame + 1}.webp", interface)

    use quick_menu

screen home_screen():
    style_prefix "phone"

    $ time_of_day = time_options[time_index]
    $ day_of_week = week[weekday]

    if weather:
        add At(f"images/interface/phone/clock_{time_index}_{weather}.webp", interface)
    else:
        add At(f"images/interface/phone/clock_{time_index}.webp", interface)

    text f"{temperature[time_index]} " + u"\u00b0C" anchor (0.5, 0.5) pos (0.3905, 0.1288):
        size 25

        color "#ffffff"
    
    text f"{week[weekday][0:3]}" anchor (0.5, 0.5) pos (0.596, 0.135):
        font "magneto_bold.ttf"

        size 45

        color "#ffffff"
    
    text f"{time_options[time_index].capitalize()}" anchor (0.5, 0.5) pos (0.595, 0.173):
        size 30

        color "#ffffff"

    if phone_interactable and not phone_disabled:
        imagebutton:
            idle At("images/interface/phone/search_bar_idle.webp", interface)
            hover At("images/interface/phone/search_bar.webp", interface)
            selected_idle At("images/interface/phone/search_bar.webp", interface)

            selected input_cheats

            action ToggleVariable("input_cheats")

        if input_cheats:
            input id "cheat_input" value VariableInputValue("current_input", default = True) anchor (0.0, 0.5) pos (0.403, 0.235):
                font "agency_fb.ttf"

                size 30

                color "#000000"

                length 25

            key "K_RETURN" action [
                SetVariable("input_cheats", False),
                Call("enter_cheat_code", current_input, from_current = True)]
    else:
        add At("images/interface/phone/search_bar_idle.webp", interface)

    if not input_cheats:
        text "Search. . ." anchor (0.0, 0.5) pos (0.403, 0.235):
            font "agency_fb.ttf"

            size 30

            color "#bbbbbb"

    if humhum_available and not humhum_hidden:
        $ humhumthread_to_display = HumHumPool.HumHumThreads[list(HumHumPool.HumHumThreads.keys())[humhum_index]]

        add At("images/interface/phone/home_humhum_bar.webp", interface)

        text "#LatestHums" anchor (0.0, 0.5) pos (0.375, 0.29):
            size 30

            color "#d56cc4"

        imagebutton:
            idle At("images/interface/phone/home_humhum_left_idle.webp", interface)
            hover At("images/interface/phone/home_humhum_left.webp", interface)

            if phone_interactable and not phone_disabled:
                action [
                    SetVariable("humhum_index", (humhum_index - 1) % len(list(HumHumPool.HumHumThreads.keys()))),
                    SetVariable("humhum_yadjustment.value", 0)]
            else:
                action None

        imagebutton:
            idle At("images/interface/phone/home_humhum_right_idle.webp", interface)
            hover At("images/interface/phone/home_humhum_right.webp", interface)

            if phone_interactable and not phone_disabled:
                action [
                    SetVariable("humhum_index", (humhum_index + 1) % len(list(HumHumPool.HumHumThreads.keys()))),
                    SetVariable("humhum_yadjustment.value", 0)]
            else:
                action None

        fixed anchor (0.5, 0.5) pos (0.486, 0.392) xysize (int(905*interface_adjustment), int(354*interface_adjustment)):
            add At("images/interface/phone/home_humhum_box.webp", interface)

            if humhumthread_to_display.HumHums[0].Owner != Player:
                add At(f"images/interface/icons/{humhumthread_to_display.HumHums[0].Owner.tag}.webp", humhum_icon) anchor (0.5, 0.5) pos (0.055, 0.122)

                text humhumthread_to_display.HumHums[0].Owner.call_sign anchor (0.0, 0.5) pos (0.125, 0.122) size 32
            else:
                add At(f"images/interface/icons/Player_{Player.background_color}.webp", humhum_icon) anchor (0.5, 0.5) pos (0.055, 0.122)

                text humhumthread_to_display.HumHums[0].Owner.call_sign anchor (0.0, 0.5) pos (0.125, 0.122) size 32

            viewport id "home_humhum_viewport" yadjustment humhum_yadjustment anchor (0.0, 0.0) pos (0.0, 0.3) xysize (int(905*interface_adjustment), int(240*interface_adjustment)):
                draggable True
                mousewheel True

                vbox xsize 1.0:
                    fixed xysize (1.0, 0.9):
                        text humhumthread_to_display.HumHums[0].body anchor (0.0, 0.0) pos (0.02, 0.015):
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
                        frame xsize 1.0:
                            background Frame(At("images/interface/phone/home_humhum_reply_box.webp", interface), 0, 15, 0, 15)

                            vbox xsize 1.0:
                                null height 15

                                for h in range(1, len(humhumthread_to_display.HumHums)):
                                    hbox xsize 425:
                                        if humhumthread_to_display.HumHums[h].Owner != Player:
                                            add At(f"images/interface/icons/{humhumthread_to_display.HumHums[h].Owner.tag}.webp", humhum_icon) yalign 0.0
                                        else:
                                            add At(f"images/interface/icons/Player_{Player.background_color}.webp", humhum_icon) yalign 0.0

                                        null width 8

                                        fixed yalign 0.0 xysize (int(750*interface_adjustment), int(100*interface_adjustment)):
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

        add At("images/interface/phone/home_humhum_scrollbar_background.webp", interface)

        vbar value YScrollValue("home_humhum_viewport") anchor (0.5, 0.5) pos (0.614, 0.392) xysize (int(27*interface_adjustment), int(330*interface_adjustment)):
            base_bar At("images/interface/phone/home_humhum_scrollbar.webp", interface)

            thumb At("images/interface/phone/home_humhum_scrollbar_thumb.webp", interface)
            thumb_offset int(66*interface_adjustment/2/3)

            unscrollable "hide"

    imagebutton anchor (0.5, 0.5) pos (0.416, 0.8):
        idle At("images/interface/icons/call_idle.webp", phone_icon) 
        hover At("images/interface/icons/call.webp", phone_icon)
        
        if phone_interactable and not phone_disabled:
            action [
                SetVariable("loading", True),
                SetVariable("current_phone_screen", "call_choice")]
        else:
            action None

    imagebutton anchor (0.5, 0.5) pos (0.496, 0.8):
        idle At("images/interface/icons/humhum_idle.webp", phone_icon) 
        hover At("images/interface/icons/humhum.webp", phone_icon)
        
        if phone_interactable and not phone_disabled:
            action [
                SetVariable("loading", True),
                SetVariable("current_phone_screen", "humhum_choice")]
        else:
            action None

    imagebutton anchor (0.5, 0.5) pos (0.576, 0.8):
        idle At("images/interface/icons/blah_idle.webp", phone_icon) 
        hover At("images/interface/icons/blah.webp", phone_icon)
        
        if phone_interactable and not phone_disabled:
            action [
                SetVariable("loading", True),
                SetVariable("current_phone_screen", "text_choice")]
        else:
            action None

screen app_screen():
    style_prefix "phone"

    add At("images/interface/phone/app_list.webp", interface)

    text "APPS" anchor (0.0, 0.5) pos (0.37, 0.118):
        size 50

        color "#ffffff"

    imagebutton anchor (0.5, 0.5) pos (0.416, 0.23):
        idle At("images/interface/icons/call_idle.webp", phone_icon) 
        hover At("images/interface/icons/call.webp", phone_icon)
        
        if phone_interactable and not phone_disabled:
            action [
                SetVariable("loading", True),
                SetVariable("current_phone_screen", "call_choice")]
        else:
            action None

    imagebutton anchor (0.5, 0.5) pos (0.576, 0.23):
        idle At("images/interface/icons/blah_idle.webp", phone_icon) 
        hover At("images/interface/icons/blah.webp", phone_icon)
        
        if phone_interactable and not phone_disabled:
            action [
                SetVariable("loading", True),
                SetVariable("current_phone_screen", "text_choice")]
        else:
            action None

    imagebutton anchor (0.5, 0.5) pos (0.416, 0.41333):
        idle At("images/interface/icons/daily_bungle_idle.webp", phone_icon) 
        hover At("images/interface/icons/daily_bungle.webp", phone_icon)
        
        if phone_interactable and not phone_disabled:
            action [
                SetVariable("daily_bungle_ad", renpy.random.choice([1, 2, 3, 4])),
                SetVariable("current_phone_screen", "news")]
        else:
            action None

    if humhum_available:
        imagebutton anchor (0.5, 0.5) pos (0.496, 0.41333):
            idle At("images/interface/icons/humhum_idle.webp", phone_icon) 
            hover At("images/interface/icons/humhum.webp", phone_icon)
            
            if phone_interactable and not phone_disabled:
                action [
                    SetVariable("loading", True),
                    SetVariable("current_phone_screen", "humhum_home")]
            else:
                action None

    imagebutton anchor (0.5, 0.5) pos (0.576, 0.4133):
        idle At("images/interface/icons/hot_control_idle.webp", phone_icon) 
        hover At("images/interface/icons/hot_control.webp", phone_icon)
        
        if phone_interactable and not phone_disabled:
            action SetVariable("current_phone_screen", "remote")
        else:
            action None

    imagebutton anchor (0.5, 0.5) pos (0.416, 0.59666):
        idle At("images/interface/icons/achievements_idle.webp", phone_icon) 
        hover At("images/interface/icons/achievements.webp", phone_icon)
        
        if phone_interactable and not phone_disabled:
            action [
                SetVariable("loading", True),
                SetVariable("current_phone_screen", "achievements_home")]
        else:
            action None

    imagebutton anchor (0.5, 0.5) pos (0.576, 0.59666):
        idle At("images/interface/icons/music_idle.webp", phone_icon) 
        hover At("images/interface/icons/music.webp", phone_icon)
        
        if phone_interactable and not phone_disabled:
            action [
                SetVariable("loading", True),
                SetVariable("current_phone_screen", "music")]
        else:
            action None

    imagebutton anchor (0.5, 0.5) pos (0.416, 0.78):
        idle At("images/interface/icons/save_idle.webp", phone_icon) 
        hover At("images/interface/icons/save.webp", phone_icon)
        
        if phone_interactable and not phone_disabled:
            action ShowMenu("save")
        else:
            action None

    imagebutton anchor (0.5, 0.5) pos (0.496, 0.78):
        idle At("images/interface/icons/load_idle.webp", phone_icon) 
        hover At("images/interface/icons/load.webp", phone_icon)
        
        if phone_interactable and not phone_disabled:
            action ShowMenu("load")
        else:
            action None

    imagebutton anchor (0.5, 0.5) pos (0.576, 0.78):
        idle At("images/interface/icons/config_idle.webp", phone_icon) 
        hover At("images/interface/icons/config.webp", phone_icon)
        
        if phone_interactable and not phone_disabled:
            action [
                SetVariable("loading", True),
                SetVariable("current_phone_screen", "config")]
        else:
            action None

screen call_choice_screen():
    style_prefix "phone"

    add At("images/interface/phone/call_contacts.webp", interface)

    add At("images/interface/phone/call_top.webp", interface)

    text "CALL" anchor (0.0, 0.5) pos (0.402, 0.118):
        size 50

        color "#ffffff"

    text "Contact List" anchor (0.0, 0.5) pos (0.37, 0.173):
        size 40

        color "#ffffff"

    text "Search. . ." anchor (0.0, 0.5) pos (0.55, 0.176):
        size 20

        color "#bbbbbb"

    vpgrid id "call_choice_screen_viewport" anchor (0.5, 0.0) pos (0.49, 0.217) xysize (int(919*interface_adjustment), int(1350*interface_adjustment)):
        cols 1

        spacing 15

        draggable True
        mousewheel True

        for C in Contacts:
            button xysize (int(919*interface_adjustment), int(199*interface_adjustment)):
                idle_background At("images/interface/phone/call_contact_idle.webp", interface)
                hover_background At("images/interface/phone/call_contact.webp", interface)

                add At(f"images/interface/icons/{C.tag}.webp", call_icon) anchor (0.5, 0.5) pos (0.1, 0.5)

                text f"{C.name}" anchor (0.0, 0.5) pos (0.215, 0.5):
                    size 40
                
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

    vbar value YScrollValue("call_choice_screen_viewport") anchor (0.0, 0.0) pos (0.612, 0.217) xysize (int(29*interface_adjustment), int(1350*interface_adjustment)):
        base_bar At("images/interface/phone/call_scrollbar.webp", interface)

        thumb At("images/interface/phone/call_scrollbar_thumb.webp", interface)
        thumb_offset int(79*interface_adjustment/2/3)

        unscrollable "hide"

screen call_screen():
    style_prefix "phone"

    timer 0.5 repeat True action SetVariable("waiting", (waiting + 1) % 4)

    add At("images/interface/phone/call_calling.webp", interface)

    add At("images/interface/phone/call_top.webp", interface)

    text "CALL" anchor (0.0, 0.5) pos (0.402, 0.118):
        size 50

        color "#ffffff"

    add At(f"images/interface/photos/{current_phone_Character.tag}.webp", call_photo) anchor (0.5, 0.5) pos (0.496, 0.33)

    if waiting == 3:
        text f"Calling {current_phone_Character.name}. . ." anchor (0.0, 0.5) pos (0.40, 0.575):
            size 48

            color "#ffffff"
    elif waiting == 2:
        text f"Calling {current_phone_Character.name}. . " + "{alpha=0.0}.{/alpha}" anchor (0.0, 0.5) pos (0.40, 0.575):
            size 48

            color "#ffffff"
    elif waiting == 1:
        text f"Calling {current_phone_Character.name}. " + "{alpha=0.0}. .{/alpha}" anchor (0.0, 0.5) pos (0.40, 0.575):
            size 48

            color "#ffffff"
    elif waiting == 0:
        text f"Calling {current_phone_Character.name}" + "{alpha=0.0}. . .{/alpha}" anchor (0.0, 0.5) pos (0.40, 0.575):
            size 48

            color "#ffffff"

screen text_choice_screen():
    style_prefix "phone"

    timer 0.5 action SetVariable("loading", False)

    if loading:
        add At("images/interface/phone/blah_intro.webp", interface)
    else:
        add At("images/interface/phone/blah_contacts.webp", interface)

        add At("images/interface/phone/blah_top.webp", interface)

        text "BLAH!" anchor (0.0, 0.5) pos (0.402, 0.118):
            size 50

            color "#ffffff"

        text "Contact List" anchor (0.0, 0.5) pos (0.37, 0.173):
            size 40

            color "#ffffff"

        text "Search. . ." anchor (0.0, 0.5) pos (0.55, 0.176):
            size 20

            color "#bbbbbb"

        vpgrid id "text_choice_screen_viewport" anchor (0.5, 0.0) pos (0.49, 0.217) xysize (int(919*interface_adjustment), int(1350*interface_adjustment)):
            cols 1

            spacing 15

            draggable True
            mousewheel True

            for C in Contacts:
                button xysize (int(919*interface_adjustment), int(199*interface_adjustment)):
                    idle_background At("images/interface/phone/blah_contact_idle.webp", interface)
                    hover_background At("images/interface/phone/blah_contact.webp", interface)
                    selected_idle_background At("images/interface/phone/blah_contact.webp", interface)

                    selected C in unread_messages.keys()

                    add At(f"images/interface/icons/{C.tag}.webp", call_icon) anchor (0.5, 0.5) pos (0.1, 0.5)

                    text f"{C.name}" anchor (0.0, 0.5) pos (0.215, 0.5):
                        size 40
                    
                    if phone_interactable and not phone_disabled:
                        action [
                            SetVariable("current_phone_Character", C),
                            SetVariable("current_phone_screen", "text")]
                    else:
                        action NullAction()

        vbar value YScrollValue("text_choice_screen_viewport") anchor (0.0, 0.0) pos (0.612, 0.217) xysize (int(29*interface_adjustment), int(1350*interface_adjustment)):
            base_bar At("images/interface/phone/blah_scrollbar.webp", interface)

            thumb At("images/interface/phone/blah_scrollbar_thumb.webp", interface)
            thumb_offset int(79*interface_adjustment/2/3)

            unscrollable "hide"

screen text_screen():
    style_prefix "phone"

    add At("images/interface/phone/blah_message.webp", interface)

    add At("images/interface/phone/blah_top.webp", interface)

    text "BLAH!" anchor (0.0, 0.5) pos (0.402, 0.118):
        size 50

        color "#ffffff"

    if current_phone_Character in Contacts:
        text f"Chatting with {current_phone_Character.name}" anchor (0.0, 0.5) pos (0.37, 0.173):
            size 40

            color "#ffffff"
    else:
        text "Chatting with Unknown Number" anchor (0.0, 0.5) pos (0.37, 0.173):
            size 40

            color "#ffffff"

    text "Type. . ." anchor (0.0, 0.5) pos (0.49, 0.849):
        size 30

        color "#bbbbbb"

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

        viewport anchor (0.0, 0.5) pos (0.7, 0.5) xysize (0.25, 0.6):
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
                            idle_background Frame(At("images/interface/phone/text_frame_Player_idle.webp", interface), 10, 10)
                            hover_background Frame(At("images/interface/phone/text_frame_Player.webp", interface), 10, 10)

                            activate_sound None

                            padding (15, 15, 15, 15)
                            minimum (int(0.05*config.screen_width), 0)
                            xmaximum int(0.15*config.screen_width)

                            text message:
                                size 32

                            if current_phone_Character.mandatory_text_options:
                                action Call("send_text", current_phone_Character, message)
                            else:
                                action Call("send_text", current_phone_Character, message, from_current = True)

screen text_history(Character):
    style_prefix "phone"

    python:
        blah_yadjustment.value = float("inf")

    $ previous_Owner = None

    $ last_status = None

    viewport yadjustment blah_yadjustment anchor (0.5, 0.0) pos (0.496, 0.218) xysize (0.24, 0.59):
        draggable True
        mousewheel True

        yinitial 1.0
    
        vbox align (0.0, 0.0) xsize 1.0:
            xfill True

            spacing 5

            for Owner, content, status in Character.text_history:
                if last_status == "read" and status in ["unread", "current", "recently_read"]:
                    add "images/interface/phone/texts_end.webp" align (0.5, 0.5) zoom interface_adjustment

                if Owner != Player:
                    hbox align (0.0, 0.0):
                        spacing 5

                        if previous_Owner != Owner.tag:
                            add At(f"images/interface/icons/{Owner.tag}.webp", humhum_icon):
                                if status == "current":
                                    at message_appear_icon()
                        else:
                            null width 45

                        vbox align (0.0, 0.5):
                            if previous_Owner != Owner.tag and Owner in Contacts:
                                text Owner.name anchor (0.0, 0.5) pos (0.0, 0.5):
                                    size 30

                            frame:
                                background Frame(At("images/interface/phone/text_frame.webp", interface), 10, 10)

                                padding (15, 15, 15, 15)
                                minimum (int(0.05*config.screen_width), 0)
                                xmaximum int(0.2*config.screen_width)

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
                            add At(f"images/interface/icons/Player_{Player.background_color}.webp", humhum_icon):
                                if status == "current":
                                    at message_appear_icon()
                        else:
                            null width 45

                        vbox align (1.0, 0.5):
                            frame:
                                background Frame(At("images/interface/phone/text_frame_Player.webp", interface), 10, 10)

                                padding (15, 15, 15, 15)
                                minimum (int(0.05*config.screen_width), 0)
                                xmaximum int(0.2*config.screen_width)

                                if status == "current":
                                    at message_appear(1)

                                text content:
                                    text_align 1.0

                                    size 30
                                
                $ previous_Owner = Owner.tag

                $ last_status = status

screen humhum_home_screen():
    style_prefix "phone"

    timer 0.45 action SetVariable("loading", False)

    if loading:
        add At("humhum_animation", interface)
    else:
        add At("images/interface/phone/humhum_background.webp", interface)

        text "HUMHUM" anchor (0.0, 0.5) pos (0.402, 0.118):
            size 50

            color "#ffffff"

        add At("images/interface/phone/humhum_home_background.webp", interface)

        text "#LatestHums" anchor (0.0, 0.5) pos (0.375, 0.166):
            size 30

            color "#d56cc4"

        viewport id "humhum_home_screen_viewport" anchor (0.5, 0.0) pos (0.488, 0.195) xysize (int(905*interface_adjustment), int(1299*interface_adjustment)):
            draggable True
            mousewheel True
        
            vbox xsize 1.0:
                for H in HumHumPool.HumHumThreads.values():
                    fixed xysize (int(905*interface_adjustment), int(354*interface_adjustment)):
                        yfit True
                        
                        add At("images/interface/phone/home_humhum_box.webp", interface)

                        if H.HumHums[0].Owner != Player:
                            add At(f"images/interface/icons/{H.HumHums[0].Owner.tag}.webp", humhum_icon) anchor (0.5, 0.5) pos (0.055, 22)

                            text H.HumHums[0].Owner.call_sign anchor (0.0, 0.5) pos (0.125, 22):
                                size 32
                        else:
                            add At(f"images/interface/icons/Player_{Player.background_color}.webp", humhum_icon) anchor (0.5, 0.5) pos (0.055, 22)

                            text H.HumHums[0].Owner.call_sign anchor (0.0, 0.5) pos (0.125, 22):
                                size 32

                        fixed anchor (0.5, 0.0) pos (0.5, int(106*interface_adjustment)) xysize (1.0, 115):
                            text H.HumHums[0].body anchor (0.0, 0.0) pos (0.02, 0.015): 
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
                            frame anchor (0.5, 0.0) pos (0.5, int(340*interface_adjustment)) xsize 1.0:
                                background Frame(At("images/interface/phone/home_humhum_reply_box.webp", interface), 0, 15, 0, 15)

                                vbox xsize 1.0:
                                    null height 15

                                    for h in range(1, len(H.HumHums)):
                                        hbox xsize 425:
                                            if H.HumHums[h].Owner != Player:
                                                add At(f"images/interface/icons/{H.HumHums[h].Owner.tag}.webp", humhum_icon) yalign 0.0
                                            else:
                                                add At(f"images/interface/icons/Player_{Player.background_color}.webp", humhum_icon) yalign 0.0

                                            null width 8

                                            fixed yalign 0.0 xysize (int(750*interface_adjustment), int(100*interface_adjustment)):
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

        vbar value YScrollValue("humhum_home_screen_viewport") anchor (0.0, 0.0) pos (0.614, 0.195) xysize (int(27*interface_adjustment), int(1299*interface_adjustment)):
            base_bar At("images/interface/phone/humhum_scrollbar.webp", interface)

            thumb At("images/interface/phone/humhum_scrollbar_thumb.webp", interface)
            thumb_offset int(66*interface_adjustment/2/2)

            unscrollable "hide"

        add At("images/interface/phone/humhum_bar.webp", interface)

        imagebutton:
            idle At("images/interface/phone/humhum_home.webp", interface)
            hover At("images/interface/phone/humhum_home.webp", interface)

            if phone_interactable and not phone_disabled:
                action SetVariable("current_phone_screen", "humhum_home")
            else:
                action None

        # imagebutton:
        #     idle At("images/interface/phone/humhum_gallery_idle.webp", interface)
        #     hover At("images/interface/phone/humhum_gallery.webp", interface)

        #     if phone_interactable and not phone_disabled:
        #         action SetVariable("current_phone_screen", "humhum_gallery")
        #     else:
        #         action None

        imagebutton:
            idle At("images/interface/phone/humhum_friends_idle.webp", interface)
            hover At("images/interface/phone/humhum_friends.webp", interface)

            if phone_interactable and not phone_disabled:
                action SetVariable("current_phone_screen", "humhum_choice")
            else:
                action None

screen humhum_choice_screen():
    style_prefix "phone"

    timer 0.45 action SetVariable("loading", False)

    if loading:
        add At("humhum_animation", interface)
    else:
        add At("images/interface/phone/humhum_background.webp", interface)

        text "HUMHUM" anchor (0.0, 0.5) pos (0.402, 0.118):
            size 50

            color "#ffffff"

        vpgrid id "humhum_choice_screen_viewport" anchor (0.5, 0.0) pos (0.496, 0.175) xysize (int(905*interface_adjustment), int(1299*interface_adjustment)):
            cols 3

            spacing 0

            xfill True

            draggable True
            mousewheel True

            for G in active_Companions:
                imagebutton:
                    idle At(f"images/interface/icons/{G.tag}_idle.webp", phone_icon) 
                    hover At(f"images/interface/icons/{G.tag}.webp", phone_icon)
                    
                    if phone_interactable and not phone_disabled:
                        action [
                            SetVariable("current_phone_Character", G),
                            SetVariable("current_phone_screen", "humhum")]
                    else:
                        action None

        vbar value YScrollValue("humhum_choice_screen_viewport") anchor (0.0, 0.0) pos (0.614, 0.175) xysize (int(27*interface_adjustment), int(1299*interface_adjustment)):
            base_bar At("images/interface/phone/humhum_scrollbar.webp", interface)

            thumb At("images/interface/phone/humhum_scrollbar_thumb.webp", interface)
            thumb_offset int(66*interface_adjustment/2/2)

            unscrollable "hide"

        add At("images/interface/phone/humhum_bar.webp", interface)

        imagebutton:
            idle At("images/interface/phone/humhum_home_idle.webp", interface)
            hover At("images/interface/phone/humhum_home.webp", interface)

            if phone_interactable and not phone_disabled:
                action SetVariable("current_phone_screen", "humhum_home")
            else:
                action None

        # imagebutton:
        #     idle At("images/interface/phone/humhum_gallery_idle.webp", interface)
        #     hover At("images/interface/phone/humhum_gallery.webp", interface)

        #     if phone_interactable and not phone_disabled:
        #         action SetVariable("current_phone_screen", "humhum_gallery")
        #     else:
        #         action None

        imagebutton:
            idle At("images/interface/phone/humhum_friends.webp", interface)
            hover At("images/interface/phone/humhum_friends.webp", interface)

            if phone_interactable and not phone_disabled:
                action SetVariable("current_phone_screen", "humhum_choice")
            else:
                action None

screen humhum_screen():
    style_prefix "phone"

    add At("images/interface/phone/humhum_background.webp", interface)

    text "HUMHUM" anchor (0.0, 0.5) pos (0.402, 0.118):
        size 50

        color "#ffffff"

    add At("images/interface/phone/humhum_profile_background.webp", interface)

    add At(f"images/interface/photos/{current_phone_Character.tag}.webp", humhum_photo) anchor (0.5, 0.5) pos (0.426, 0.311)

    if current_phone_Character.status["miffed"] or current_phone_Character.status["mad"]:
        add At("images/interface/phone/humhum_status_angry.webp", interface)

    if current_phone_Character.status["horny"] or current_phone_Character.status["nympho"]:
        add At("images/interface/phone/humhum_status_nympho.webp", interface)

    for s, status in enumerate(["heartbroken"]):
        if current_phone_Character.status[status]:
            add At(f"images/interface/phone/humhum_status_{status}.webp", interface)

    text "Name" anchor (0.0, 0.5) pos (0.496, 0.179):
        size 30

    if len(current_phone_Character.name) < 10:
        text f"{current_phone_Character.name}" anchor (1.0, 0.5) pos (0.95, 0.179):
            size 30 
    else:
        text f"{current_phone_Character.name}" anchor (1.0, 0.5) pos (0.613, 0.179):
            size 25 
            
    text "Love" anchor (0.0, 0.5) pos (0.496, 0.243):
        size 30

    text f"{current_phone_Character.love}" anchor (1.0, 0.5) pos (0.613, 0.243):
        size 30 
            
    text "Trust" anchor (0.0, 0.5) pos (0.496, 0.308):
        size 30

    text f"{current_phone_Character.trust}" anchor (1.0, 0.5) pos (0.613, 0.308):
        size 30

    text "Favorite Gift" anchor (0.0, 0.5) pos (0.498, 0.373):
        size 30

    text "Relationship Status" anchor (0.0, 0.5) pos (0.372, 0.567):
        size 28

    if current_phone_Character not in Partners:
        text "Single" anchor (1.0, 0.5) pos (0.613, 0.567):
            size 30
    elif len(Partners) > 2:
        text "Polyamorous" anchor (1.0, 0.5) pos (0.613, 0.567):
            size 30
    else:
        text "In a relationship" anchor (1.0, 0.5) pos (0.613, 0.567):
            size 30

    text "Your Petname" anchor (0.0, 0.5) pos (0.372, 0.632):
        size 28

    text f"{current_phone_Character.Player_petname}" anchor (1.0, 0.5) pos (0.613, 0.632):
        size 30

    text "Her Petname" anchor (0.0, 0.5) pos (0.372, 0.697):
        size 28

    text f"{current_phone_Character.petname}" anchor (1.0, 0.5) pos (0.613, 0.697):
        size 30

    add At("images/interface/phone/humhum_bar.webp", interface)

    imagebutton:
        idle At("images/interface/phone/humhum_home.webp", interface)
        hover At("images/interface/phone/humhum_home.webp", interface)

        if phone_interactable and not phone_disabled:
            action SetVariable("current_phone_screen", "humhum_home")
        else:
            action None

    # imagebutton:
    #     idle At("images/interface/phone/humhum_gallery_idle.webp", interface)
    #     hover At("images/interface/phone/humhum_gallery.webp", interface)

    #     if phone_interactable and not phone_disabled:
    #         action SetVariable("current_phone_screen", "humhum_gallery")
    #     else:
    #         action None

    imagebutton:
        idle At("images/interface/phone/humhum_friends.webp", interface)
        hover At("images/interface/phone/humhum_friends.webp", interface)

        if phone_interactable and not phone_disabled:
            action SetVariable("current_phone_screen", "humhum_choice")
        else:
            action None

screen news_screen():
    style_prefix "phone"

    add At("images/interface/phone/daily_bungle_background.webp", interface)

    text "THE DAILY BUNGLE" anchor (0.0, 0.5) pos (0.402, 0.118):
        size 50

        color "#ffffff"

    add At("images/interface/phone/daily_bungle_ad[daily_bungle_ad].webp", interface)

    if daily_bungle_Article is not None:
        add At("images/interface/phone/daily_bungle_article.webp", interface) anchor (0.5, 0.0) pos (0.49, 0.41)

        frame anchor (0.5, 0.5) pos (0.49, 0.456) ysize 0.075:
            text daily_bungle_Article.headline xalign 0.0:
                font "agency_fb_bold.ttf"

                size 36

                color "#000000"

                text_align 0.0

        viewport id "news_screen_viewport" anchor (0.5, 0.0) pos (0.49, 0.51) xysize (0.222, 0.3):
            draggable True
            mousewheel True

            frame:
                text daily_bungle_Article.body xalign 0.0:
                    font "agency_fb_bold.ttf"

                    size 26

                    color "#403f3f"

                    text_align 0.0

        button anchor (0.5, 1.0) pos (0.49, 0.857) xysize (int(520*interface_adjustment), int(89*interface_adjustment)):
            idle_background At("images/interface/phone/daily_bungle_button_idle.webp", interface)
            hover_background At("images/interface/phone/daily_bungle_button.webp", interface)

            text "CLOSE ARTICLE":
                size 28

                color "#403f3f"

                text_align 0.5
            
            action SetVariable("daily_bungle_Article", None)
    else:
        vpgrid id "news_screen_viewport" anchor (0.5, 0.0) pos (0.49, 0.41) xysize (int(887*interface_adjustment), int(990*interface_adjustment)):
            cols 1

            spacing 15

            draggable True
            mousewheel True

            for article_name in NewsPool.Articles.keys():
                fixed xysize (1.0, int(495*interface_adjustment)):
                    add "images/interface/phone/daily_bungle_article_panel.webp" zoom interface_adjustment

                    frame anchor (0.0, 0.0) pos (0.04, 0.06) xysize (int(520*interface_adjustment), 0.33):
                        text NewsPool.Articles[article_name].headline xalign 0.0:
                            font "agency_fb_bold.ttf"

                            size 36

                            color "#000000"

                            text_align 0.0

                    frame anchor (0.0, 0.5) pos (0.04, 0.57) xysize (int(520*interface_adjustment), 0.33):
                        text NewsPool.Articles[article_name].subheadline xalign 0.0:
                            font "agency_fb_bold.ttf"

                            size 26

                            color "#403f3f"

                            text_align 0.0

                    add f"images/interface/phone/daily_bungle_{NewsPool.Articles[article_name].photo}.webp" anchor (0.5, 0.5) pos (0.835, 0.3) zoom interface_adjustment

                    text "BY" anchor (0.5, 0.5) pos (0.835, 0.65):
                        font "agency_fb_bold.ttf"

                        size 26

                        color "#000000"

                        text_align 0.5

                    frame anchor (0.5, 0.5) pos (0.835, 0.85) xsize 0.35:
                        text NewsPool.Articles[article_name].author xalign 0.5:
                            font "agency_fb_bold.ttf"

                            size 26

                            color "#403f3f"

                            text_align 0.5

                    button anchor (0.0, 1.0) pos (0.04, 0.94) xysize (int(520*interface_adjustment), int(89*interface_adjustment)):
                        idle_background At("images/interface/phone/daily_bungle_button_idle.webp", interface)
                        hover_background At("images/interface/phone/daily_bungle_button.webp", interface)

                        text "READ ARTICLE":
                            size 28

                            color "#403f3f"

                            text_align 0.5
                        
                        action SetVariable("daily_bungle_Article", NewsPool.Articles[article_name])

    vbar value YScrollValue("news_screen_viewport") anchor (0.0, 0.0) pos (0.608, 0.41) xysize (int(32*interface_adjustment), int(990*interface_adjustment)):
        base_bar At("images/interface/phone/daily_bungle_scrollbar.webp", interface)

        thumb At("images/interface/phone/daily_bungle_scrollbar_thumb.webp", interface)
        thumb_offset int(72*interface_adjustment/2/3)

        # unscrollable "hide"

screen remote_screen():
    style_prefix "phone"

    $ vibrator_Characters = []

    for C in all_Companions:
        if C.location != "hold":
            if C.remote_vibrator is not None:
                $ vibrator_Characters.append(C)

    if current_vibrator_index > len(vibrator_Characters) - 1:
        $ current_vibrator_index = 0

    add At("images/interface/phone/hot_control_background.webp", interface)

    text "HOT CONTROL" anchor (0.0, 0.5) pos (0.402, 0.118):
        size 50

        color "#ffffff"

    if vibrator_Characters and vibrator_Characters[current_vibrator_index].remote_vibrator > 0.0:
        bar value VariableValue(f"{vibrator_Characters[current_vibrator_index].tag}.remote_vibrator", 1.0) anchor (0.5, 0.5) pos (0.495, 0.618) xysize (int(397*interface_adjustment), int(63*interface_adjustment)):
            left_bar At("images/interface/phone/hot_control_intensity.webp", interface)
            right_bar At("images/interface/phone/hot_control_intensity.webp", interface)

            thumb Frame(At("images/interface/phone/hot_control_selector.webp", interface))
            thumb_offset int(22*interface_adjustment)
    else:
        bar value 0.0 range 1.0 anchor (0.5, 0.5) pos (0.495, 0.618) xysize (int(397*interface_adjustment), int(63*interface_adjustment)):
            left_bar At("images/interface/phone/hot_control_intensity.webp", interface)
            right_bar At("images/interface/phone/hot_control_intensity.webp", interface)

            thumb Frame(At("images/interface/phone/hot_control_selector.webp", interface))
            thumb_offset int(22*interface_adjustment)

    imagebutton:
        idle At("images/interface/phone/hot_control_off.webp", interface)
        hover At("images/interface/phone/hot_control_on.webp", interface)
        selected_idle At("images/interface/phone/hot_control_on.webp", interface)

        selected vibrator_Characters[current_vibrator_index].remote_vibrator > 0.0

        if vibrator_Characters and phone_interactable and not phone_disabled:
            if vibrator_Characters[current_vibrator_index].remote_vibrator == 0.0:
                action [
                    SetField(vibrator_Characters[current_vibrator_index], "remote_vibrator", 0.1),
                    Function(renpy.call_in_new_context, f"{vibrator_Characters[current_vibrator_index].tag}_remote_vibrator_on")]
            else:
                action [
                    SetField(vibrator_Characters[current_vibrator_index], "remote_vibrator", 0.0),
                    Function(renpy.call_in_new_context, f"{vibrator_Characters[current_vibrator_index].tag}_remote_vibrator_off")]
        else:
            action None

    imagebutton:
        idle At("images/interface/phone/hot_control_left_idle.webp", interface)
        hover At("images/interface/phone/hot_control_left.webp", interface)

        if vibrator_Characters and phone_interactable and not phone_disabled:
            action SetVariable("current_vibrator_index", (current_vibrator_index - 1) % len(vibrator_Characters))
        else:
            action None

    if vibrator_Characters:
        text vibrator_Characters[current_vibrator_index].name anchor (0.5, 0.5) pos (0.495, 0.228):
            size 50

    imagebutton:
        idle At("images/interface/phone/hot_control_right_idle.webp", interface)
        hover At("images/interface/phone/hot_control_right.webp", interface)

        if vibrator_Characters and phone_interactable and not phone_disabled:
            action SetVariable("current_vibrator_index", (current_vibrator_index + 1) % len(vibrator_Characters))
        else:
            action None

screen achievements_home_screen():
    style_prefix "phone"

    if renpy.music.get_playing() != "sounds/music/Achievements.ogg":
        timer 0.01 action Play("music", "sounds/music/Achievements.ogg", fadeout = 0.5, fadein = 0.1, loop = True)

    timer 1.0 action SetVariable("loading", False)

    if loading:
        add At("achievements_animation", interface)
    else:
        add At("images/interface/phone/achievements_home_background.webp", interface)

        add At("images/interface/phone/achievements_top.webp", interface)

        text "ACHIEVEMENTS" anchor (0.0, 0.5) pos (0.402, 0.118):
            size 50

            color "#ffffff"

        add At("images/interface/phone/achievements_total_box.webp", interface)

        text "TOTAL ACHIEVEMENTS" anchor (0.5, 0.5) pos (0.496, 0.71):
            font "agency_fb_bold.ttf"

            size 40

            color "#801a48"

        $ completed_achievements = 0

        for a in achievements.keys():
            if achievement.has(a):
                $ completed_achievements += 1

        text f"{completed_achievements}/{len(achievements)}" anchor (0.5, 0.5) pos (0.496, 0.77):
            font "agency_fb_bold.ttf"

            size 70

            color "#ffffff"

        if completed_achievements == len(achievements):
            add "images/interface/phone/achievements_trophy_foil.webp" anchor (0.5, 0.5) pos (0.57, 0.775) zoom interface_adjustment

            add At("images/interface/phone/achievements_trophy_sparkle.webp", pulse(1.0)) anchor (0.5, 0.5) pos (0.57, 0.775) zoom interface_adjustment
        elif completed_achievements/len(achievements) >= 0.75:
            add "images/interface/phone/achievements_trophy_gold.webp" anchor (0.5, 0.5) pos (0.57, 0.775) zoom interface_adjustment
        elif completed_achievements/len(achievements) >= 0.50:
            add "images/interface/phone/achievements_trophy_silver.webp" anchor (0.5, 0.5) pos (0.57, 0.775) zoom interface_adjustment
        elif completed_achievements/len(achievements) >= 0.25:
            add "images/interface/phone/achievements_trophy_bronze.webp" anchor (0.5, 0.5) pos (0.57, 0.775) zoom interface_adjustment

        button anchor (0.5, 0.5) pos (0.558, 0.233) xysize (int(458*interface_adjustment), int(367*interface_adjustment)):
            idle_background At("images/interface/phone/achievements_button_idle.webp", interface)
            hover_background At("images/interface/phone/achievements_button.webp", interface)

            text "LIST":
                font "agency_fb_bold.ttf"

                size 120

                idle_color "#801a48"
                hover_color "#16172b"

            if phone_interactable and not phone_disabled:
                action SetVariable("current_phone_screen", "achievements_list")
            else:
                action None

screen achievements_list_screen():
    style_prefix "phone"

    add At("images/interface/phone/achievements_list_background.webp", interface)

    add At("images/interface/phone/achievements_top.webp", interface)

    text "ACHIEVEMENTS" anchor (0.0, 0.5) pos (0.402, 0.118):
        size 50

        color "#ffffff"

    vpgrid id "achievements_list_screen_viewport" anchor (0.5, 0.0) pos (0.49, 0.165) xysize (int(927*interface_adjustment), int(1491*interface_adjustment)):
        cols 1

        spacing 15

        draggable True
        mousewheel True

        for a in achievements.keys():
            fixed xysize (1.0, int(202*interface_adjustment)):
                add "images/interface/phone/achievements_list_box.webp" zoom interface_adjustment

                if achievement.has(a):
                    if achievements[a]["points"] == 5:
                        add "images/interface/phone/achievements_trophy_bronze.webp" anchor (0.5, 0.5) pos (0.115, 0.53) zoom interface_adjustment
                    elif achievements[a]["points"] == 10:
                        add "images/interface/phone/achievements_trophy_silver.webp" anchor (0.5, 0.5) pos (0.115, 0.53) zoom interface_adjustment
                    elif achievements[a]["points"] == 20:
                        add "images/interface/phone/achievements_trophy_gold.webp" anchor (0.5, 0.5) pos (0.115, 0.53) zoom interface_adjustment
                    elif achievements[a]["points"] == 40:
                        add "images/interface/phone/achievements_trophy_foil.webp" anchor (0.5, 0.5) pos (0.115, 0.53) zoom interface_adjustment
                else:
                    add "images/interface/phone/achievements_locked.webp" anchor (0.5, 0.5) pos (0.118, 0.505) zoom interface_adjustment

                if achievement.has(a) or not achievements[a]["secret"]:
                    frame anchor (0.5, 0.0) pos (0.6, 0.1) xysize (0.7, 0.4):
                        background None

                        text a:
                            size 28

                            color "#ffffff"

                    frame anchor (0.5, 1.0) pos (0.6, 0.9) xysize (0.7, 0.4):
                        background None

                        text achievements[a]["description"]:
                            size 18

                            color "#ffffff"

    vbar value YScrollValue("achievements_list_screen_viewport") anchor (0.0, 0.0) pos (0.614, 0.165) xysize (int(28*interface_adjustment), int(1491*interface_adjustment)):
        base_bar At("images/interface/phone/achievements_scrollbar.webp", interface)

        thumb At("images/interface/phone/achievements_scrollbar_thumb.webp", interface)
        thumb_offset int(72*interface_adjustment/2/3)

        unscrollable "hide"

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

    add At("images/interface/phone/music_background.webp", interface)

    text "MUSIC PLAYER" anchor (0.0, 0.5) pos (0.402, 0.118):
        size 50

        color "#ffffff"

    if renpy.music.get_playing():
        text renpy.music.get_playing().split("/")[-1].split(".")[0] anchor (0.0, 0.5) pos (0.46, 0.19):
            size 45

        bar value AudioPositionValue(channel = 'music') anchor (0.0, 0.5) pos (0.46, 0.22) xysize (int(576*interface_adjustment), int(16*interface_adjustment)):
            left_bar At("images/interface/phone/music_bar.webp", interface)
            right_bar At("images/interface/phone/music_bar_empty.webp", interface)

            thumb None
            thumb_offset 0

    imagebutton:
        idle At("images/interface/phone/music_shuffle_idle.webp", interface)
        hover At("images/interface/phone/music_shuffle.webp", interface)

        if phone_interactable and not phone_disabled:
            action Play("music", song_list[(renpy.random.randint(0, len(song_list))) % len(song_list)], loop = music_repeating)
        else:
            action None

    imagebutton:
        idle At("images/interface/phone/music_left_idle.webp", interface)
        hover At("images/interface/phone/music_left.webp", interface)
        
        if phone_interactable and not phone_disabled:
            action Play("music", song_list[(current_song - 1) % len(song_list)], loop = music_repeating)
        else:
            action None

    if renpy.music.get_pause():
        imagebutton:
            idle At("images/interface/phone/music_play.webp", interface)
            hover At("images/interface/phone/music_pause.webp", interface)
            
            if phone_interactable and not phone_disabled:
                action PauseAudio("music", value = False)
            else:
                action None
    else:
        imagebutton:
            idle At("images/interface/phone/music_pause.webp", interface)
            hover At("images/interface/phone/music_play.webp", interface)
            
            if phone_interactable and not phone_disabled:
                action PauseAudio("music", value = True)
            else:
                action None

    imagebutton:
        idle At("images/interface/phone/music_right_idle.webp", interface)
        hover At("images/interface/phone/music_right.webp", interface)
        
        if phone_interactable and not phone_disabled:
            action Play("music", song_list[(current_song + 1) % len(song_list)], loop = music_repeating)
        else:
            action None

    imagebutton:
        idle At("images/interface/phone/music_repeat_idle.webp", interface)
        hover At("images/interface/phone/music_repeat.webp", interface)
        selected_idle At("images/interface/phone/music_repeat.webp", interface)
        
        selected music_repeating

        if phone_interactable and not phone_disabled:
            if music_repeating:
                action [
                    Play("music", song_list[current_song], loop = False),
                    SetVariable("music_repeating", False)]
            else:
                action [
                    Play("music", song_list[current_song], loop = True),
                    SetVariable("music_repeating", True)]
        else:
            action None

    viewport id "music_screen_viewport" anchor (0.5, 0.0) pos (0.487, 0.378) xysize (int(847*interface_adjustment), int(1035*interface_adjustment)):
        draggable True
        mousewheel True

        vbox xsize 1.0:
            spacing 10

            for file in song_list:
                button xalign 0.0 xysize (int(847*interface_adjustment), int(140*interface_adjustment)):
                    idle_background At("images/interface/phone/music_song_idle.webp", interface)
                    hover_background At("images/interface/phone/music_song.webp", interface)
                    selected_idle_background At("images/interface/phone/music_song.webp", interface)

                    selected file == renpy.music.get_playing()

                    text file.split("/")[-1].split(".")[0] anchor (0.0, 0.5) pos (0.1, 0.5):
                        size 32

                    if phone_interactable and not phone_disabled:
                        action Play("music", file, loop = music_repeating)
                    else:
                        action None

    vbar value YScrollValue("music_screen_viewport") anchor (0.0, 0.0) pos (0.605, 0.378) xysize (int(29*interface_adjustment), int(1035*interface_adjustment)):
        base_bar At("images/interface/phone/music_scrollbar.webp", interface)

        thumb At("images/interface/phone/music_scrollbar_thumb.webp", interface)
        thumb_offset int(72*interface_adjustment/2/3)

        unscrollable "hide"

screen config_screen():
    style_prefix "phone"

    add At("images/interface/phone/config_background.webp", interface)

    text "CONFIGURATION" anchor (0.0, 0.5) pos (0.402, 0.118):
        size 50

        color "#ffffff"

    vbox anchor (0.5, 0.0) pos (0.496, 0.15) xysize (int(930*interface_adjustment), int(1299*interface_adjustment)):
        xfill True

        fixed xysize (1.0, 57):
            add At("images/interface/phone/config_box.webp", interface)

            text "Cellphone Frame":
                size 32

        fixed xysize (0.7, 64):
            imagebutton anchor (0.0, 0.5) pos (0.0, 0.5):
                idle At("images/interface/Player_customization/left_idle.webp", interface)
                hover At("images/interface/Player_customization/left.webp", interface)

                action SetVariable("Player.phone_frame", (Player.phone_frame - 1) % 7)

            text f"TYPE {Player.phone_frame + 1}":
                size 32

            imagebutton anchor (1.0, 0.5) pos (1.0, 0.5):
                idle At("images/interface/Player_customization/right_idle.webp", interface)
                hover At("images/interface/Player_customization/right.webp", interface)

                action SetVariable("Player.phone_frame", (Player.phone_frame + 1) % 7)

        fixed xysize (1.0, 57):
            add At("images/interface/phone/config_box.webp", interface)

            text "Cellphone Wallpaper":
                size 32

        $ wallpaper_types = [1, 2, 3, 4]

        for C in Partners:
            $ wallpaper_types.append(f"{C.name}")

        fixed xysize (0.7, 64):
            imagebutton anchor (0.0, 0.5) pos (0.0, 0.5):
                idle At("images/interface/Player_customization/left_idle.webp", interface)
                hover At("images/interface/Player_customization/left.webp", interface)

                action [
                    SetVariable("Player.phone_wallpaper", wallpaper_types[(wallpaper_index - 1) % len(wallpaper_types)]),
                    SetVariable("wallpaper_index", (wallpaper_index - 1) % len(wallpaper_types))]

            if wallpaper_index < 4:
                text f"{wallpaper_types[wallpaper_index]}":
                    size 32
            else:
                text f"TYPE {wallpaper_types[wallpaper_index]}":
                    size 32

            imagebutton anchor (1.0, 0.5) pos (1.0, 0.5):
                idle At("images/interface/Player_customization/right_idle.webp", interface)
                hover At("images/interface/Player_customization/right.webp", interface)

                action [
                    SetVariable("Player.phone_wallpaper", wallpaper_types[(wallpaper_index + 1) % len(wallpaper_types)]),
                    SetVariable("wallpaper_index", (wallpaper_index + 1) % len(wallpaper_types))]

        fixed xysize (1.0, 57):
            add At("images/interface/phone/config_box.webp", interface)

            text "Hide HumHum Home Widget":
                size 32

        fixed xysize (0.7, 64):
            imagebutton anchor (0.0, 0.5) pos (0.0, 0.5):
                idle At("images/interface/Player_customization/left_idle.webp", interface)
                hover At("images/interface/Player_customization/left.webp", interface)

                action ToggleVariable("humhum_hidden")

            if humhum_hidden:
                text "YES":
                    size 32
            else:
                text "NO":
                    size 32

            imagebutton anchor (1.0, 0.5) pos (1.0, 0.5):
                idle At("images/interface/Player_customization/right_idle.webp", interface)
                hover At("images/interface/Player_customization/right.webp", interface)

                action ToggleVariable("humhum_hidden")

        fixed xysize (1.0, 57):
            add At("images/interface/phone/config_box.webp", interface)

            text "Cellphone Ringtone":
                size 32

        fixed xysize (0.7, 64):
            imagebutton anchor (0.0, 0.5) pos (0.0, 0.5):
                idle At("images/interface/Player_customization/left_idle.webp", interface)
                hover At("images/interface/Player_customization/left.webp", interface)

                action [
                    Play("sound", f"sounds/ringtones/{(Player.ringtone - 1) % len(available_ringtones)}.ogg"),
                    SetVariable("Player.ringtone", (Player.ringtone - 1) % len(available_ringtones))]

            text f"TYPE {Player.ringtone + 1}":
                size 32

            imagebutton anchor (1.0, 0.5) pos (1.0, 0.5):
                idle At("images/interface/Player_customization/right_idle.webp", interface)
                hover At("images/interface/Player_customization/right.webp", interface)

                action [
                    Play("sound", f"sounds/ringtones/{(Player.ringtone + 1) % len(available_ringtones)}.ogg"),
                    SetVariable("Player.ringtone", (Player.ringtone + 1) % len(available_ringtones))]