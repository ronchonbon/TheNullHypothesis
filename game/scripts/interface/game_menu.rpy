init -1:

    default preferences_tab = "graphics"
    default preferences_label = "GRAPHIC OPTIONS"
    default blinking = True

    default cinematic_bars = True

    default image_filter = None

    default flashing_lights = True

    default scrolling_rollback = False

    default tooltips_enabled = True

style game_menu is default

style game_menu_hbox:
    spacing 5

style game_menu_vbox:
    spacing 5
    
style game_menu_button:
    idle_background Frame(At("images/interface/box1.webp", interface), 10, 10)
    hover_background Frame(At("images/interface/box2.webp", interface), 10, 10)

    padding (15, 15, 15, 15)

    xsize 0.15

style game_menu_text:
    size 30

style files is default

style files_button:
    idle_background Frame(At("images/interface/box1.webp", interface), 10, 10)
    hover_background Frame(At("images/interface/box2.webp", interface), 10, 10)

    padding (30, 10, 30, 10)

screen navigation():
    style_prefix "game_menu"

    frame align (0.995, 0.985):
        background None

        vbox:
            spacing 2

            textbutton _("RETURN"):
                action Return() 
                
                text_size 40

            textbutton _("OPTIONS"):
                action ShowMenu("preferences") 
                
                text_size 40

            textbutton _("SAVE"):
                action ShowMenu("save") 
                
                text_size 40

            textbutton _("LOAD"):
                action ShowMenu("load") 
                
                text_size 40
            
            textbutton _("MAIN MENU"):
                action MainMenu() 
                
                text_size 40

            textbutton _("QUIT"):
                action Quit(confirm = True) 
                
                text_size 40

screen save():
    tag menu

    use file_picker
    use navigation

screen load():
    tag menu

    use file_picker
    use navigation

screen file_picker():
    style_prefix "game_menu"

    add "images/interface/main_menu/blank_background.webp" zoom interface_adjustment

    add At("images/interface/preferences/spin.webp", spinning_element) anchor (0.5, 0.5) pos (0.502, 0.502) zoom interface_adjustment

    vbox anchor (0.0, 0.0) pos (0.011, 0.01):
        spacing 2

        hbox:
            style_prefix "files"

            spacing 2

            textbutton _("PREVIOUS"):
                action FilePagePrevious()

                text_size 32

            textbutton _("AUTO"):
                action FilePage("auto") 

                text_size 32

            textbutton _("QUICK"):
                action FilePage("quick") 

                text_size 32

            for i in range(1, 9):
                textbutton str(i):
                    action FilePage(i)

                    text_size 32
                
            textbutton _("NEXT"):
                action FilePageNext() 

                text_size 32

        null height 8

        $ columns = 3
        $ rows = 6

        grid columns rows xsize 0.825:
            style_prefix "file_picker"

            transpose True
            xfill True

            spacing 5

            for i in range(1, columns*rows + 1):
                $ file_name = FileSlotName(i, columns*rows)
                $ file_time = FileTime(i, empty = _("EMPTY"))
                $ save_name = FileSaveName(i)
                
                button ysize 0.15:
                    xfill True

                    hbox align (0.0, 0.5):
                        spacing 15

                        add FileScreenshot(i) yalign 0.5

                        text "[save_name!t]\n[file_time!t]":
                            font "agency_fb.ttf"

                            size 28

                            color "#000000"

                            text_align 0.0

                        key "save_delete" action FileDelete(i)

                    action FileAction(i)

screen preferences():
    tag menu

    style_prefix "game_menu"

    timer 0.5 repeat True action ToggleVariable("blinking")

    add "images/interface/main_menu/blank_background.webp" zoom interface_adjustment

    add At("images/interface/preferences/spin.webp", spinning_element) anchor (0.5, 0.5) pos (0.502, 0.502) zoom interface_adjustment

    add "images/interface/preferences/frame.webp" zoom interface_adjustment

    imagebutton:
        idle At("images/interface/preferences/graphics_idle.webp", interface) 
        hover At("images/interface/preferences/graphics.webp", interface) 
        selected_idle At("images/interface/preferences/graphics.webp", interface)

        action [
            SetVariable("preferences_tab", "graphics"),
            SetVariable("preferences_label", "GRAPHICS OPTIONS")]

    text "GRAPHICS" anchor (0.5, 0.5) pos (0.256, 0.336)

    imagebutton:
        idle At("images/interface/preferences/audio_idle.webp", interface) 
        hover At("images/interface/preferences/audio.webp", interface) 
        selected_idle At("images/interface/preferences/audio.webp", interface)

        action [
            SetVariable("preferences_tab", "audio"),
            SetVariable("preferences_label", "AUDIO OPTIONS")]

    text "AUDIO" anchor (0.5, 0.5) pos (0.353, 0.336)

    imagebutton:
        idle At("images/interface/preferences/hotkeys_idle.webp", interface) 
        hover At("images/interface/preferences/hotkeys.webp", interface) 
        selected_idle At("images/interface/preferences/hotkeys.webp", interface)

        action [
            SetVariable("preferences_tab", "hotkeys"),
            SetVariable("preferences_label", "HOTKEYS")]

    text "HOTKEYS" anchor (0.5, 0.5) pos (0.45, 0.336)

    imagebutton:
        idle At("images/interface/preferences/gameplay_idle.webp", interface) 
        hover At("images/interface/preferences/gameplay.webp", interface) 
        selected_idle At("images/interface/preferences/gameplay.webp", interface)

        action [
            SetVariable("preferences_tab", "gameplay"),
            SetVariable("preferences_label", "GAMEPLAY OPTIONS")]

    text "GAMEPLAY" anchor (0.5, 0.5) pos (0.548, 0.336)

    if blinking:
        text preferences_label + "{alpha=0.0}_{/alpha}" anchor (0.0, 0.5) pos (0.065, 0.336)
    else:
        text preferences_label + "_" anchor (0.0, 0.5) pos (0.065, 0.336)

    if preferences_tab == "graphics":
        hbox anchor (0.5, 0.5) pos (0.431, 0.675) xysize (int(2800*interface_adjustment), int(1150*interface_adjustment)):
            spacing 50

            vbox:
                text "FULLSCREEN" anchor (0.5, 0.5) pos (0.47, 0.5)

                button xysize (int(321*interface_adjustment), int(190*interface_adjustment)):
                    idle_background At("images/interface/preferences/off.webp", interface) 
                    hover_background At("images/interface/preferences/off.webp", interface) 
                    selected_idle_background At("images/interface/preferences/on.webp", interface) 
                    selected_hover_background At("images/interface/preferences/on.webp", interface)

                    hover_sound None
                    
                    selected preferences.fullscreen

                    text "OFF" anchor (0.5, 0.5) pos (0.2, 0.461):
                        size 25

                    text "ON" anchor (0.5, 0.5) pos (0.7, 0.461):
                        size 25

                    if preferences.fullscreen:
                        action Preference("display", "window")
                    else:
                        action Preference("display", "fullscreen")

            vbox:
                spacing 50
                
                vbox:
                    text "IMAGE FILTER" anchor (0.5, 0.5) pos (0.5, 0.5)

                    fixed xysize (int(700*interface_adjustment), int(190*interface_adjustment)):
                        imagebutton anchor (0.0, 0.5) pos (0.0, 0.5):
                            idle At("images/interface/Player_customization/left_idle.webp", interface)
                            hover At("images/interface/Player_customization/left.webp", interface)

                            if image_filter == "comic":
                                action SetVariable("image_filter", None)
                            elif image_filter == "tv":
                                action SetVariable("image_filter", "comic")
                            else:
                                action SetVariable("image_filter", "tv")

                        if image_filter:
                            text image_filter.upper() anchor (0.5, 0.5) pos (0.5, 0.5)
                        else:
                            text "OFF" anchor (0.5, 0.5) pos (0.5, 0.5)

                        imagebutton anchor (1.0, 0.5) pos (1.0, 0.5):
                            idle At("images/interface/Player_customization/right_idle.webp", interface)
                            hover At("images/interface/Player_customization/right.webp", interface)

                            if image_filter == "comic":
                                action SetVariable("image_filter", "tv")
                            elif image_filter == "tv":
                                action SetVariable("image_filter", None)
                            else:
                                action SetVariable("image_filter", "comic")

                vbox:
                    text "CINEMATIC BARS" anchor (0.5, 0.5) pos (0.47, 0.5)

                    button xysize (int(321*interface_adjustment), int(190*interface_adjustment)):
                        idle_background At("images/interface/preferences/off.webp", interface) 
                        hover_background At("images/interface/preferences/off.webp", interface) 
                        selected_idle_background At("images/interface/preferences/on.webp", interface) 
                        selected_hover_background At("images/interface/preferences/on.webp", interface)

                        hover_sound None
                        
                        selected cinematic_bars

                        text "OFF" anchor (0.5, 0.5) pos (0.2, 0.461):
                            size 25

                        text "ON" anchor (0.5, 0.5) pos (0.7, 0.461):
                            size 25

                        action ToggleVariable("cinematic_bars")

            vbox:
                text "FLASHING LIGHTS" anchor (0.5, 0.5) pos (0.47, 0.5)

                button xysize (int(321*interface_adjustment), int(190*interface_adjustment)):
                    idle_background At("images/interface/preferences/off.webp", interface) 
                    hover_background At("images/interface/preferences/off.webp", interface) 
                    selected_idle_background At("images/interface/preferences/on.webp", interface) 
                    selected_hover_background At("images/interface/preferences/on.webp", interface)

                    hover_sound None
                    
                    selected flashing_lights

                    text "OFF" anchor (0.5, 0.5) pos (0.2, 0.461):
                        size 25

                    text "ON" anchor (0.5, 0.5) pos (0.7, 0.461):
                        size 25

                    action ToggleVariable("flashing_lights")

            vbox:
                spacing 50
                
                vbox:
                    text "PLAYER BODY VISIBLE" anchor (0.5, 0.5) pos (0.47, 0.5)

                    button xysize (int(321*interface_adjustment), int(190*interface_adjustment)):
                        idle_background At("images/interface/preferences/off.webp", interface) 
                        hover_background At("images/interface/preferences/off.webp", interface) 
                        selected_idle_background At("images/interface/preferences/on.webp", interface) 
                        selected_hover_background At("images/interface/preferences/on.webp", interface)

                        hover_sound None
                        
                        selected Player.body_visible

                        text "OFF" anchor (0.5, 0.5) pos (0.2, 0.461):
                            size 25

                        text "ON" anchor (0.5, 0.5) pos (0.7, 0.461):
                            size 25

                        action ToggleVariable("Player.body_visible")

                vbox:
                    text "UI VISIBLE" anchor (0.5, 0.5) pos (0.47, 0.5)

                    button xysize (int(321*interface_adjustment), int(190*interface_adjustment)):
                        idle_background At("images/interface/preferences/off.webp", interface) 
                        hover_background At("images/interface/preferences/off.webp", interface) 
                        selected_idle_background At("images/interface/preferences/on.webp", interface) 
                        selected_hover_background At("images/interface/preferences/on.webp", interface)

                        hover_sound None
                        
                        selected (not dialogue_hidden or not belt_hidden or not Action_screen_hidden)

                        text "OFF" anchor (0.5, 0.5) pos (0.2, 0.461):
                            size 25

                        text "ON" anchor (0.5, 0.5) pos (0.7, 0.461):
                            size 25

                        action [
                            ToggleVariable("dialogue_hidden"),
                            ToggleVariable("belt_hidden"),
                            ToggleVariable("Action_screen_hidden")]

                vbox:
                    text "WARDROBE MAGAZINE" anchor (0.5, 0.5) pos (0.47, 0.5)

                    button xysize (int(321*interface_adjustment), int(190*interface_adjustment)):
                        idle_background At("images/interface/preferences/off.webp", interface) 
                        hover_background At("images/interface/preferences/off.webp", interface) 
                        selected_idle_background At("images/interface/preferences/on.webp", interface) 
                        selected_hover_background At("images/interface/preferences/on.webp", interface)

                        hover_sound None
                        
                        selected wardrobe_magazine

                        text "OFF" anchor (0.5, 0.5) pos (0.2, 0.461):
                            size 25

                        text "ON" anchor (0.5, 0.5) pos (0.7, 0.461):
                            size 25

                        action ToggleVariable("wardrobe_magazine")
    elif preferences_tab == "audio":
        hbox anchor (0.5, 0.5) pos (0.431, 0.643) xysize (int(2800*interface_adjustment), int(1150*interface_adjustment)):
            spacing 50

            vbox:
                spacing 25

                text "INTERFACE VOLUME"

                bar value Preference("sound volume") xysize (int(1114*interface_adjustment), int(40*interface_adjustment)):
                    base_bar At("images/interface/preferences/scrollbar.webp", interface)

                    thumb At("images/interface/preferences/scrollbar_thumb.webp", interface)
                    thumb_offset 10
                    
                    unscrollable "hide"

                text "MUSIC VOLUME"

                bar value Preference("music volume") xysize (int(1114*interface_adjustment), int(40*interface_adjustment)):
                    base_bar At("images/interface/preferences/scrollbar.webp", interface)

                    thumb At("images/interface/preferences/scrollbar_thumb.webp", interface)
                    thumb_offset 10
                    
                    unscrollable "hide"

            vbox:
                text "MUTE" anchor (0.5, 0.5) pos (0.47, 0.5)

                imagebutton:
                    idle At("images/interface/preferences/off.webp", interface) 
                    hover At("images/interface/preferences/off.webp", interface) 
                    selected_idle At("images/interface/preferences/on.webp", interface) 
                    selected_hover At("images/interface/preferences/on.webp", interface)

                    hover_sound None

                    selected volume_muted

                    if volume_muted:
                        action [
                            SetVariable("volume_muted", False),
                            SetMute(["sound", "music"], False)]
                    else:
                        action [
                            SetVariable("volume_muted", True),
                            SetMute(["sound", "music"], True)]
    elif preferences_tab == "hotkeys":
        hbox anchor (0.5, 0.5) pos (0.431, 0.7) xysize (int(2800*interface_adjustment), int(1150*interface_adjustment)):
            spacing 10

            vbox yalign 0.0:
                hbox xalign 0.0:
                    fixed xysize (int(158*interface_adjustment), int(150*interface_adjustment)):
                        add At("images/interface/preferences/hotkey.webp", interface)

                        text "I":
                            size 36

                            color "#000000"

                    text "INVENTORY" align (0.0, 0.5)

                hbox xalign 0.0:
                    fixed xysize (int(158*interface_adjustment), int(150*interface_adjustment)):
                        add At("images/interface/preferences/hotkey.webp", interface)

                        text "J":
                            size 36

                            color "#000000"
                            
                    text "JOURNAL" align (0.0, 0.5)

                hbox xalign 0.0:
                    fixed xysize (int(158*interface_adjustment), int(150*interface_adjustment)):
                        add At("images/interface/preferences/hotkey.webp", interface)

                        text "M":
                            size 36

                            color "#000000"

                    text "MAP" align (0.0, 0.5)

                hbox xalign 0.0:
                    fixed xysize (int(158*interface_adjustment), int(150*interface_adjustment)):
                        add At("images/interface/preferences/hotkey.webp", interface)

                        text "P":
                            size 36

                            color "#000000"

                    text "PHONE" align (0.0, 0.5)

            vbox yalign 0.0:
                hbox xalign 0.0:
                    fixed xysize (int(158*interface_adjustment), int(150*interface_adjustment)):
                        add At("images/interface/preferences/hotkey.webp", interface)

                        text "R":
                            size 36

                            color "#000000"

                    text "PLAYER ROOM" align (0.0, 0.5)

                hbox xalign 0.0:
                    fixed xysize (int(158*interface_adjustment), int(150*interface_adjustment)):
                        add At("images/interface/preferences/hotkey.webp", interface)

                        text "C":
                            size 36

                            color "#000000"

                    text "CLASSROOM" align (0.0, 0.5)
                        
                hbox xalign 0.0:
                    fixed xysize (int(158*interface_adjustment), int(150*interface_adjustment)):
                        add At("images/interface/preferences/hotkey.webp", interface)

                        text "G":
                            size 36

                            color "#000000"

                    text "DANGER ROOM" align (0.0, 0.5)
                        
                hbox xalign 0.0:
                    fixed xysize (int(158*interface_adjustment), int(150*interface_adjustment)):
                        add At("images/interface/preferences/hotkey.webp", interface)

                        text "1":
                            size 36

                            color "#000000"

                    text "QUIKLOC 1" align (0.0, 0.5)
                        
                hbox xalign 0.0:
                    fixed xysize (int(158*interface_adjustment), int(150*interface_adjustment)):
                        add At("images/interface/preferences/hotkey.webp", interface)

                        text "2":
                            size 36

                            color "#000000"

                    text "QUIKLOC 2" align (0.0, 0.5)
                        
                hbox xalign 0.0:
                    fixed xysize (int(158*interface_adjustment), int(150*interface_adjustment)):
                        add At("images/interface/preferences/hotkey.webp", interface)

                        text "3":
                            size 36

                            color "#000000"

                    text "QUIKLOC 3" align (0.0, 0.5)

            vbox yalign 0.0:
                hbox xalign 0.0:
                    fixed xysize (int(158*interface_adjustment), int(150*interface_adjustment)):
                        add At("images/interface/preferences/hotkey.webp", interface)

                        text "Q":
                            size 36

                            color "#000000"

                    text "SKIP DAY" align (0.0, 0.5)

                hbox xalign 0.0:
                    fixed xysize (int(158*interface_adjustment), int(150*interface_adjustment)):
                        add At("images/interface/preferences/hotkey.webp", interface)

                        text "-":
                            size 36

                            color "#000000"

                    text "TOGGLE MUTE" align (0.0, 0.5)
    elif preferences_tab == "gameplay":
        hbox anchor (0.5, 0.5) pos (0.431, 0.643) xysize (int(2800*interface_adjustment), int(1150*interface_adjustment)):
            if config.rollback_enabled:
                vbox:
                    text "SCROLLING ROLLBACK" anchor (0.5, 0.5) pos (0.47, 0.5)

                    button xysize (int(321*interface_adjustment), int(190*interface_adjustment)):
                        idle_background At("images/interface/preferences/off.webp", interface) 
                        hover_background At("images/interface/preferences/off.webp", interface) 
                        selected_idle_background At("images/interface/preferences/on.webp", interface) 
                        selected_hover_background At("images/interface/preferences/on.webp", interface)

                        hover_sound None
                        
                        selected scrolling_rollback

                        text "OFF" anchor (0.5, 0.5) pos (0.2, 0.461):
                            size 25

                        text "ON" anchor (0.5, 0.5) pos (0.7, 0.461):
                            size 25

                        if scrolling_rollback:
                            action [
                                Function(config.keymap["rollback"].remove, "mousedown_4"),
                                SetVariable("scrolling_rollback", False),
                                Function(renpy.clear_keymap_cache)]
                        else:
                            action [
                                Function(config.keymap["rollback"].append, "mousedown_4"),
                                SetVariable("scrolling_rollback", True),
                                Function(renpy.clear_keymap_cache)]

            vbox:
                text "TOOLTIPS" anchor (0.5, 0.5) pos (0.47, 0.5)

                button xysize (int(321*interface_adjustment), int(190*interface_adjustment)):
                    idle_background At("images/interface/preferences/off.webp", interface) 
                    hover_background At("images/interface/preferences/off.webp", interface) 
                    selected_idle_background At("images/interface/preferences/on.webp", interface) 
                    selected_hover_background At("images/interface/preferences/on.webp", interface)

                    hover_sound None
                    
                    selected tooltips_enabled

                    text "OFF" anchor (0.5, 0.5) pos (0.2, 0.461):
                        size 25

                    text "ON" anchor (0.5, 0.5) pos (0.7, 0.461):
                        size 25

                    action ToggleVariable("tooltips_enabled")

    use navigation