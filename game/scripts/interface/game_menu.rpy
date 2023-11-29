init -1:

    default preferences_tab = "graphics"
    default preferences_label = "GRAPHIC OPTIONS"
    default blinking = True

    default cinematic_bars = True

    default comic_filter = False

    default flashing_lights = True

    default scrolling_rollback = False

    default tooltips_enabled = True

style game_menu is default
    
style game_menu_button:
    idle_background Frame("images/interface/box2.webp", 30, 30)
    hover_background Frame("images/interface/box1.webp", 30, 30)

    minimum (int(config.screen_width*0.15), int(config.screen_height*0.07))
    xmaximum int(config.screen_width*0.15)

    # hover_sound "sounds/interface/hover.ogg"
    activate_sound "sounds/interface/press.ogg"

style game_menu_image_button:
    # hover_sound "sounds/interface/hover.ogg"
    activate_sound "sounds/interface/press.ogg"

style files is default

style files_button:
    idle_background Frame("images/interface/box2.webp", 30, 30)
    hover_background Frame("images/interface/box1.webp", 30, 30)

    minimum (int(config.screen_width*0.01), int(config.screen_height*0.07))

    # hover_sound "sounds/interface/hover.ogg"
    activate_sound "sounds/interface/press.ogg"

screen navigation():
    style_prefix "game_menu"

    frame align (0.995, 0.985):
        background None

        vbox:
            spacing 2

            textbutton _("Return"):
                action Return() 
                
                text_size 40

            textbutton _("Options"):
                action ShowMenu("preferences") 
                
                text_size 40

            textbutton _("Save Game"):
                action ShowMenu("save") 
                
                text_size 40

            textbutton _("Load Game"):
                action ShowMenu("load") 
                
                text_size 40
            
            textbutton _("Main Menu"):
                action MainMenu() 
                
                text_size 40

            textbutton _("Quit"):
                action Quit() 
                
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

    add At("images/interface/preferences/background.webp", interface)

    add At(At("images/interface/preferences/spin.webp", interface), spinning_element) anchor (0.5, 0.5) pos (0.502, 0.502)

    vbox anchor (0.0, 0.0) pos (0.011, 0.01):
        spacing 2

        hbox:
            style_prefix "files"

            spacing 2

            textbutton _("Previous"):
                xpadding 30

                action FilePagePrevious() 
                
                text_size 32

            textbutton _("Auto"):
                xpadding 30

                action FilePage("auto") 
                
                text_size 32

            textbutton _("Quick"):
                xpadding 30

                action FilePage("quick") 
                
                text_size 32

            for i in range(1, 9):
                textbutton str(i):
                    xpadding 30

                    action FilePage(i)
                    
                    text_size 32
                
            textbutton _("Next"):
                xpadding 30
                
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
                $ file_time = FileTime(i, empty = _("Empty Slot."))
                $ save_name = FileSaveName(i)
                
                button ysize 0.15:
                    xfill True

                    hbox align (0.0, 0.5):
                        spacing 15

                        add FileScreenshot(i) yalign 0.5

                        text "[save_name!t]\n[file_time!t]" xalign 0.5 yalign 0.5 text_align 0.0:
                            size 28

                        key "save_delete" action FileDelete(i)

                    action FileAction(i)

screen preferences():
    tag menu

    style_prefix "game_menu"

    timer 0.5 repeat True action ToggleVariable("blinking")

    add At("images/interface/preferences/background.webp", interface)

    add At(At("images/interface/preferences/spin.webp", interface), spinning_element) anchor (0.5, 0.5) pos (0.502, 0.502)

    add At("images/interface/preferences/frame.webp", interface)

    imagebutton:
        idle At("images/interface/preferences/graphics_idle.webp", interface) hover At("images/interface/preferences/graphics.webp", interface) selected_idle At("images/interface/preferences/graphics.webp", interface)

        action [
            SetVariable("preferences_tab", "graphics"),
            SetVariable("preferences_label", "GRAPHICS OPTIONS")]

        focus_mask True

    imagebutton:
        idle At("images/interface/preferences/audio_idle.webp", interface) hover At("images/interface/preferences/audio.webp", interface) selected_idle At("images/interface/preferences/audio.webp", interface)

        action [
            SetVariable("preferences_tab", "audio"),
            SetVariable("preferences_label", "AUDIO OPTIONS")]

        focus_mask True

    imagebutton:
        idle At("images/interface/preferences/hotkeys_idle.webp", interface) hover At("images/interface/preferences/hotkeys.webp", interface) selected_idle At("images/interface/preferences/hotkeys.webp", interface)

        action [
            SetVariable("preferences_tab", "hotkeys"),
            SetVariable("preferences_label", "HOTKEYS")]

        focus_mask True

    imagebutton:
        idle At("images/interface/preferences/gameplay_idle.webp", interface) hover At("images/interface/preferences/gameplay.webp", interface) selected_idle At("images/interface/preferences/gameplay.webp", interface)

        action [
            SetVariable("preferences_tab", "gameplay"),
            SetVariable("preferences_label", "GAMEPLAY OPTIONS")]

        focus_mask True

    if blinking:
        text preferences_label + "{alpha=0.0}_{/alpha}" anchor (0.5, 0.5) pos (0.123, 0.336):
            font "agency_fb_bold.ttf"

            size 30

            color "#ffffff"
    else:
        text preferences_label + "_" anchor (0.5, 0.5) pos (0.123, 0.336):
            font "agency_fb_bold.ttf"

            size 30

            color "#ffffff"

    if preferences_tab == "graphics":
        hbox anchor (0.5, 0.5) pos (0.431, 0.643) xysize (int(2800*interface_new_adjustment), int(1150*interface_new_adjustment)):
            spacing 50

            vbox:
                spacing 5

                text "Fullscreen" xalign 0.5:
                    size 36 
                    
                    color "#ffffff" 

                imagebutton xalign 0.5:
                    idle At("images/interface/preferences/off.webp", interface) hover At("images/interface/preferences/off.webp", interface) selected_idle At("images/interface/preferences/on.webp", interface) selected_hover At("images/interface/preferences/on.webp", interface)

                    hover_sound None
                    
                    selected preferences.fullscreen

                    if preferences.fullscreen:
                        action Preference("display", "window")
                    else:
                        action Preference("display", "fullscreen")

                    focus_mask True

            vbox:
                spacing 20
                
                vbox:
                    spacing 5

                    text "Comic Filter" xalign 0.5:
                        size 36 
                        
                        color "#ffffff" 

                    imagebutton xalign 0.5:
                        idle At("images/interface/preferences/off.webp", interface) hover At("images/interface/preferences/off.webp", interface) selected_idle At("images/interface/preferences/on.webp", interface) selected_hover At("images/interface/preferences/on.webp", interface)

                        hover_sound None
                        
                        selected comic_filter

                        action ToggleVariable("comic_filter")

                        focus_mask True

                vbox:
                    spacing 5

                    text "Cinematic Bars" xalign 0.5:
                        size 36 
                        
                        color "#ffffff" 

                    imagebutton xalign 0.5:
                        idle At("images/interface/preferences/off.webp", interface) hover At("images/interface/preferences/off.webp", interface) selected_idle At("images/interface/preferences/on.webp", interface) selected_hover At("images/interface/preferences/on.webp", interface)

                        hover_sound None

                        selected cinematic_bars

                        action ToggleVariable("cinematic_bars")

                        focus_mask True

            vbox:
                spacing 5

                text "Flashing Lights" xalign 0.5:
                    size 36 
                    
                    color "#ffffff" 

                imagebutton xalign 0.5:
                    idle At("images/interface/preferences/off.webp", interface) hover At("images/interface/preferences/off.webp", interface) selected_idle At("images/interface/preferences/on.webp", interface) selected_hover At("images/interface/preferences/on.webp", interface)

                    hover_sound None

                    selected flashing_lights

                    action ToggleVariable("flashing_lights")

                    focus_mask True

            vbox:
                spacing 20

                vbox:
                    spacing 5

                    text "Body Visible" xalign 0.5:
                        size 36 
                        
                        color "#ffffff" 

                    imagebutton xalign 0.5:
                        idle At("images/interface/preferences/off.webp", interface) hover At("images/interface/preferences/off.webp", interface) selected_idle At("images/interface/preferences/on.webp", interface) selected_hover At("images/interface/preferences/on.webp", interface)

                        hover_sound None

                        selected Player.body_visible

                        action ToggleVariable("Player.body_visible")

                        focus_mask True

                vbox:
                    spacing 5

                    text "UI Visible" xalign 0.5:
                        size 36 
                        
                        color "#ffffff" 

                    imagebutton xalign 0.5:
                        idle At("images/interface/preferences/off.webp", interface) hover At("images/interface/preferences/off.webp", interface) selected_idle At("images/interface/preferences/on.webp", interface) selected_hover At("images/interface/preferences/on.webp", interface)

                        hover_sound None

                        selected (not dialogue_hidden or not belt_hidden or not Action_screen_hidden)

                        action [
                            ToggleVariable("dialogue_hidden"),
                            ToggleVariable("belt_hidden"),
                            ToggleVariable("Action_screen_hidden")]

                        focus_mask True
    elif preferences_tab == "audio":
        hbox anchor (0.5, 0.5) pos (0.431, 0.643) xysize (int(2800*interface_new_adjustment), int(1150*interface_new_adjustment)):
            spacing 50

            vbox:
                spacing 25

                text "Interface Volume":
                    size 36 
                    
                    color "#ffffff" 

                bar value Preference("sound volume") xysize (int(1114*interface_new_adjustment), int(40*interface_new_adjustment)):
                    base_bar At("images/interface/preferences/scrollbar.webp", interface)

                    thumb At("images/interface/preferences/scrollbar_thumb.webp", interface)
                    thumb_offset 10
                    
                    unscrollable "hide"

                text "Music Volume":
                    size 36 
                    
                    color "#ffffff" 

                bar value Preference("music volume") xysize (int(1114*interface_new_adjustment), int(40*interface_new_adjustment)):
                    base_bar At("images/interface/preferences/scrollbar.webp", interface)

                    thumb At("images/interface/preferences/scrollbar_thumb.webp", interface)
                    thumb_offset 10
                    
                    unscrollable "hide"

            vbox:
                spacing 5

                text "Mute" xalign 0.5:
                    size 36 
                    
                    color "#ffffff" 

                imagebutton xalign 0.5:
                    idle At("images/interface/preferences/off.webp", interface) hover At("images/interface/preferences/off.webp", interface) selected_idle At("images/interface/preferences/on.webp", interface) selected_hover At("images/interface/preferences/on.webp", interface)

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

                    focus_mask True
    elif preferences_tab == "hotkeys":
        hbox anchor (0.5, 0.5) pos (0.431, 0.77) xysize (int(2800*interface_new_adjustment), int(1150*interface_new_adjustment)):
            spacing 10

            vbox yalign 0.0:
                spacing 5

                hbox xalign 0.0:
                    spacing 5

                    fixed xysize (int(158*interface_new_adjustment), int(150*interface_new_adjustment)):
                        add At("images/interface/preferences/hotkey.webp", interface)

                        text "I" align (0.5, 0.5):
                            size 36

                            color "#000000"

                    text "Inventory" align (0.0, 0.5):
                        size 36

                        color "#ffffff"

                hbox xalign 0.0:
                    spacing 5

                    fixed xysize (int(158*interface_new_adjustment), int(150*interface_new_adjustment)):
                        add At("images/interface/preferences/hotkey.webp", interface)

                        text "J" align (0.5, 0.5):
                            size 36

                            color "#000000"
                            
                    text "Journal" align (0.0, 0.5):
                        size 36

                        color "#ffffff"

                hbox xalign 0.0:
                    spacing 5
                    
                    fixed xysize (int(158*interface_new_adjustment), int(150*interface_new_adjustment)):
                        add At("images/interface/preferences/hotkey.webp", interface)

                        text "M" align (0.5, 0.5):
                            size 36

                            color "#000000"

                    text "Map" align (0.0, 0.5):
                        size 36

                        color "#ffffff"

                hbox xalign 0.0:
                    spacing 5
                    
                    fixed xysize (int(158*interface_new_adjustment), int(150*interface_new_adjustment)):
                        add At("images/interface/preferences/hotkey.webp", interface)

                        text "P" align (0.5, 0.5):
                            size 36

                            color "#000000"

                    text "Phone" align (0.0, 0.5):
                        size 36

                        color "#ffffff"

            vbox yalign 0.0:
                spacing 5

                hbox xalign 0.0:
                    spacing 5
                    
                    fixed xysize (int(158*interface_new_adjustment), int(150*interface_new_adjustment)):
                        add At("images/interface/preferences/hotkey.webp", interface)

                        text "R" align (0.5, 0.5):
                            size 36

                            color "#000000"

                    text "Go to Your Room" align (0.0, 0.5):
                        size 36

                        color "#ffffff"

                hbox xalign 0.0:
                    spacing 5
                    
                    fixed xysize (int(158*interface_new_adjustment), int(150*interface_new_adjustment)):
                        add At("images/interface/preferences/hotkey.webp", interface)

                        text "C" align (0.5, 0.5):
                            size 36

                            color "#000000"

                    text "Go to Classroom" align (0.0, 0.5):
                        size 36

                        color "#ffffff"
                        
                hbox xalign 0.0:
                    spacing 5
                    
                    fixed xysize (int(158*interface_new_adjustment), int(150*interface_new_adjustment)):
                        add At("images/interface/preferences/hotkey.webp", interface)

                        text "G" align (0.5, 0.5):
                            size 36

                            color "#000000"

                    text "Go to Danger Room" align (0.0, 0.5):
                        size 36

                        color "#ffffff"

            vbox yalign 0.0:
                spacing 5

                hbox xalign 0.0:
                    spacing 5
                    
                    fixed xysize (int(158*interface_new_adjustment), int(150*interface_new_adjustment)):
                        add At("images/interface/preferences/hotkey.webp", interface)

                        text "Q" align (0.5, 0.5):
                            size 36

                            color "#000000"

                    text "Skip Day" align (0.0, 0.5):
                        size 36

                        color "#ffffff"

                hbox xalign 0.0:
                    spacing 5
                    
                    fixed xysize (int(158*interface_new_adjustment), int(150*interface_new_adjustment)):
                        add At("images/interface/preferences/hotkey.webp", interface)

                        text "-" align (0.5, 0.5):
                            size 36

                            color "#000000"

                    text "Toggle Mute" align (0.0, 0.5):
                        size 36

                        color "#ffffff"
    elif preferences_tab == "gameplay":
        hbox anchor (0.5, 0.5) pos (0.431, 0.643) xysize (int(2800*interface_new_adjustment), int(1150*interface_new_adjustment)):
            spacing 5

            if config.rollback_enabled:
                vbox:
                    spacing 5

                    text "Scrolling Rollback" xalign 0.5:
                        size 36 
                        
                        color "#ffffff" 

                    imagebutton xalign 0.5:
                        idle At("images/interface/preferences/off.webp", interface) hover At("images/interface/preferences/off.webp", interface) selected_idle At("images/interface/preferences/on.webp", interface) selected_hover At("images/interface/preferences/on.webp", interface)

                        hover_sound None

                        selected scrolling_rollback

                        if scrolling_rollback:
                            if "mousedown_4" in config.keymap["rollback"]:
                                action [
                                    Function(config.keymap["rollback"].remove, "mousedown_4"),
                                    SetVariable("scrolling_rollback", False),
                                    Function(renpy.clear_keymap_cache)]
                            else:
                                action SetVariable("scrolling_rollback", False)
                        else:
                            action [
                                Function(config.keymap["rollback"].append, "mousedown_4"),
                                SetVariable("scrolling_rollback", True),
                                Function(renpy.clear_keymap_cache)]

                        focus_mask True

            vbox:
                spacing 5

                text "Tooltips" xalign 0.5:
                    size 36 
                    
                    color "#ffffff" 

                imagebutton xalign 0.5:
                    idle At("images/interface/preferences/off.webp", interface) hover At("images/interface/preferences/off.webp", interface) selected_idle At("images/interface/preferences/on.webp", interface) selected_hover At("images/interface/preferences/on.webp", interface)

                    hover_sound None

                    selected tooltips_enabled

                    action ToggleVariable("tooltips_enabled")

                    focus_mask True

    use navigation