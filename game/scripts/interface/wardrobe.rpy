init -1 python:

    import math

init -1:

    default Wardrobe_tab = "default"
    default current_Wardrobe_screen = None
    default current_Wardrobe_Outfit_page = 0
    default current_Wardrobe_filter = []

    default current_input = ""
    default current_Outfit_color = "yellow"
    default current_flags = []

    default Wardrobe_animation_time = 0.0
    default Wardrobe_anchor = [0.0, 0.0]
    default Wardrobe_position = [0.0, 0.0]
    default Wardrobe_zoom = 0.0

    default changed_body_hair = False

    default Wardrobe_magazine = True

style Wardrobe is default

screen Wardrobe_screen(Character):
    layer "interface"

    style_prefix "Wardrobe"

    on "show" action [
        Function(check_predicted_images),
        SetVariable("belt_hidden", True),
        SetVariable("say_obscured", True), 
        SetVariable("choice_disabled", True), 
        SetVariable("Character_picker_disabled", True),
        SetVariable("tab", "default"),
        SetVariable("Wardrobe_animation_time", 0.0),
        SetVariable("Wardrobe_anchor", [eval(f"{Character.tag}_standing_anchor")[0], eval(f"{Character.tag}_standing_bottom")]),
        SetVariable("Wardrobe_position", [0.5, 0.95]),
        SetVariable("Wardrobe_zoom", 0.6),
        SetVariable("changed_body_hair", False),
        SetField(Character, "previous_Outfit", Character.Outfit.name)]
    on "hide" action [
        SetVariable("current_Wardrobe_screen", None),
        SetVariable("current_Wardrobe_Outfit_page", 0)]

    timer 0.5 repeat True action ToggleVariable("blinking")

    $ Outfit_list = []

    for O in Character.Wardrobe.Outfits.values():
        if O.Outfit_type == Wardrobe_tab:
            $ filtered_out = False

            for filter in current_Wardrobe_filter:
                if filter not in O.flags:
                    $ filtered_out = True

            if not filtered_out:
                $ Outfit_list.append(O)

    add "images/interface/main_menu/blank_background.webp" zoom interface_adjustment

    add At("images/interface/preferences/spin.webp", spinning_element) anchor (0.5, 0.5) pos (0.502, 0.502) zoom interface_adjustment

    add "images/interface/wardrobe/background.webp" zoom interface_adjustment

    imagebutton:
        idle At("images/interface/wardrobe/exit_idle.webp", interface)
        hover At("images/interface/wardrobe/exit.webp", interface)
        
        action [
            SetVariable("Wardrobe_animation_time", 1.0),
            SetVariable("Wardrobe_position", [0.5, 0.95]),
            SetVariable("Wardrobe_zoom", 0.6),
            Call("review_Outfit", Character, from_current = True)]

        tooltip "Exit"

    add "images/interface/wardrobe/outfit_box.webp" zoom interface_adjustment

    if Wardrobe_magazine:
        add "images/interface/wardrobe/magazine.webp" zoom interface_adjustment

    imagebutton:
        idle At("images/interface/wardrobe/type_idle.webp", interface)
        hover At("images/interface/wardrobe/type.webp", interface)

        if Wardrobe_tab == "default":
            action [
                SetScreenVariable("current_Wardrobe_Outfit_page", 0),
                SetVariable("Wardrobe_tab", "custom")]
        else:
            action [
                SetScreenVariable("current_Wardrobe_Outfit_page", 0),
                SetVariable("Wardrobe_tab", "default")]

        tooltip "Change Outfit Types"

    if Wardrobe_tab == "default":
        text "DEFAULT" anchor (0.5, 0.5) pos (0.579, 0.055):
            font "agency_fb.ttf"

            size 28
    else:
        text "CUSTOM" anchor (0.5, 0.5) pos (0.579, 0.055):
            font "agency_fb.ttf"

            size 28

    imagebutton:
        idle At("images/interface/wardrobe/left_idle.webp", interface) 
        hover At("images/interface/wardrobe/left.webp", interface)
        
        if len(Outfit_list) > 7:
            action SetScreenVariable("current_Wardrobe_Outfit_page", (current_Wardrobe_Outfit_page - 1) % math.ceil(len(Outfit_list)/7))    
        else:
            action None

    imagebutton:
        idle At("images/interface/wardrobe/right_idle.webp", interface) 
        hover At("images/interface/wardrobe/right.webp", interface)

        if len(Outfit_list) > 7:
            action SetScreenVariable("current_Wardrobe_Outfit_page", (current_Wardrobe_Outfit_page + 1) % math.ceil(len(Outfit_list)/7))    
        else:
            action None

    hbox anchor (0.0, 0.0) pos (0.664, 0.025) xysize (0.267, 0.06):
        spacing 0

        $ flag = are_Characters_in_Partners(Present)

        for i in range(7*current_Wardrobe_Outfit_page, 7*current_Wardrobe_Outfit_page + 7):
            if i <= len(Outfit_list) - 1:
                button xysize (int(147*game_resolution), int(131*game_resolution)):
                    background At(f"images/interface/wardrobe/{Outfit_list[i].color}.webp", interface)

                    hover_foreground At("images/interface/wardrobe/outfit_selector.webp", interface)

                    selected_foreground At("images/interface/wardrobe/outfit_selector.webp", interface)
                    
                    selected Character.Outfit.name == Outfit_list[i].name

                    text Outfit_list[i].name:
                        font "agency_fb.ttf"

                        if len(Outfit_list[i].name) > 10:
                            size 12
                        elif len(Outfit_list[i].name) > 8:
                            size 16
                        elif len(Outfit_list[i].name) > 6:
                            size 20
                        else:
                            size 24

                    if Character.Outfit.name != Outfit_list[i].name and approval_check(Character, threshold = 0.4*Outfit_list[i].shame):
                        action Call("ask_Character_to_change_Outfit", Character, Outfit_list[i].name, instant = True, from_current = True)
                    else:
                        action NullAction()
            else:
                null width int(147*game_resolution)

    if blinking:
        text Character.Outfit.name.upper() + "{alpha=0.0}_{/alpha}" anchor (0.0, 0.5) pos (0.242, 0.063):
            size 32
    else:
        text Character.Outfit.name.upper() + "_" anchor (0.0, 0.5) pos (0.242, 0.063):
            size 32

    # if blinking:
    text "FILTERS" + "{alpha=0.0}_{/alpha}" anchor (0.0, 0.5) pos (0.242, 0.129):
        size 28
    # else:
    #     text "FILTERS" + "_" anchor (0.0, 0.5) pos (0.242, 0.129):
    #         size 28

    vpgrid id "Wardrobe_filter_viewport" anchor (0.5, 0.0) pos (0.4, 0.109) xysize (0.22, int(180*game_resolution)):
        cols 4

        draggable True
        mousewheel True
        
        spacing -17

        for filter in ["public", "winter", "day", "date", "exercise", "hero", "swim", "empty", "private", "sexy", "sleep"]:
            if filter in ["public", "day"]:
                $ color = "blue"
            elif filter in ["exercise", "hero", "swim"]:
                $ color = "red"
            elif filter in ["private", "sexy", "sleep"]:
                $ color = "pink"

            if filter != "empty":
                button xysize (int(240*game_resolution), int(115*game_resolution)):
                    idle_background At(f"images/interface/wardrobe/tag_{color}.webp", interface)
                    hover_background At(f"images/interface/wardrobe/tag_{color}.webp", interface)

                    selected_foreground At(At("images/interface/wardrobe/tag_selector.webp", interface), Transform(anchor = (0.5, 0.5), pos = (0.504, 0.515)))

                    selected filter in current_Wardrobe_filter

                    text filter.upper() anchor (0.5, 0.5) pos (0.504, 0.515):
                        size 26

                    if filter in current_Wardrobe_filter:
                        action RemoveFromSet(current_Wardrobe_filter, filter)
                    else:
                        action [
                            SetVariable("current_Wardrobe_Outfit_page", 0),
                            AddToSet(current_Wardrobe_filter, filter)]
            else:
                null width int(240*game_resolution) height int(115*game_resolution)

    vbar value YScrollValue("Wardrobe_filter_viewport") anchor (0.5, 0.0) pos (0.52, 0.109) xysize (int(29*game_resolution), int(180*game_resolution)):
        base_bar At("images/interface/wardrobe/tag_scrollbar.webp", interface)

        thumb At("images/interface/wardrobe/tag_scrollbar_thumb.webp", interface)
        thumb_offset int(74*game_resolution/2/3)

        unscrollable "hide"

    viewport anchor (0.0, 0.0) pos (0.234, 0.211) xysize (0.295, 0.733):
        fixed align (0.5, 0.5) xysize (1.0, 1.0):
            add f"{Character.tag}_sprite standing" at Wardrobe_transform(Wardrobe_animation_time, Wardrobe_anchor, Wardrobe_position, Wardrobe_zoom*eval(f"{Character.tag}_standing_zoom"))

    imagebutton:
        idle At("images/interface/wardrobe/accessory_idle.webp", interface)
        hover At("images/interface/wardrobe/accessory.webp", interface)
        selected_idle At("images/interface/wardrobe/accessory.webp", interface)
        
        selected current_Wardrobe_screen == "accessory"
        
        action [
            SetVariable("current_Wardrobe_screen", "accessory"),
            SetVariable("Wardrobe_animation_time", 1.0),
            SetVariable("Wardrobe_position", [0.5, 0.95]),
            SetVariable("Wardrobe_zoom", 0.6)]

    imagebutton:
        idle At("images/interface/wardrobe/hair_idle.webp", interface)
        hover At("images/interface/wardrobe/hair.webp", interface)
        selected_idle At("images/interface/wardrobe/hair.webp", interface)
        
        selected current_Wardrobe_screen == "hair"
        
        action [
            SetVariable("current_Wardrobe_screen", "hair"),
            SetVariable("Wardrobe_animation_time", 1.0),
            SetVariable("Wardrobe_position", [0.5, 2.65]),
            SetVariable("Wardrobe_zoom", 1.0/eval(f"{Character.tag}_standing_zoom"))]

    imagebutton:
        idle At("images/interface/wardrobe/upper_idle.webp", interface)
        hover At("images/interface/wardrobe/upper.webp", interface)
        selected_idle At("images/interface/wardrobe/upper.webp", interface)
        
        selected current_Wardrobe_screen == "upper"
        
        action [
            SetVariable("current_Wardrobe_screen", "upper"),
            SetVariable("Wardrobe_animation_time", 1.0),
            SetVariable("Wardrobe_position", [0.5, 2.25]),
            SetVariable("Wardrobe_zoom", 0.9/eval(f"{Character.tag}_standing_zoom"))]
        
    imagebutton:
        idle At("images/interface/wardrobe/lower_idle.webp", interface)
        hover At("images/interface/wardrobe/lower.webp", interface)
        selected_idle At("images/interface/wardrobe/lower.webp", interface)
        
        selected current_Wardrobe_screen == "lower"
        
        action [
            SetVariable("current_Wardrobe_screen", "lower"),
            SetVariable("Wardrobe_animation_time", 1.0),
            SetVariable("Wardrobe_position", [0.5, 0.95]),
            SetVariable("Wardrobe_zoom", 0.55/eval(f"{Character.tag}_standing_zoom"))]

    text "ACCESSORIES" anchor (0.5, 0.5) pos (0.685, 0.13):
        size 30

    text "HAIR" anchor (0.5, 0.5) pos (0.769, 0.13):
        size 36

    text "UPPER" anchor (0.5, 0.5) pos (0.852, 0.13):
        size 36

    text "LOWER" anchor (0.5, 0.5) pos (0.936, 0.13):
        size 36

    if current_Wardrobe_screen == "accessory":
        use accessory_screen(Character)
    elif current_Wardrobe_screen == "hair":
        use hair_screen(Character)
    elif current_Wardrobe_screen == "upper":
        use upper_screen(Character)
    elif current_Wardrobe_screen == "lower":
        use lower_screen(Character)

    imagebutton:
        if Character.Outfit.disabled:
            idle At("images/interface/wardrobe/disabled_idle.webp", interface)
            hover At("images/interface/wardrobe/disabled.webp", interface)

            tooltip "Enable Outfit"
        else:
            idle At("images/interface/wardrobe/enabled_idle.webp", interface)
            hover At("images/interface/wardrobe/enabled.webp", interface)

            tooltip "Disable Outfit"
        
        action ToggleField(Character.Outfit, "disabled")

    if Character.Outfit.Outfit_type == "custom":
        imagebutton:
            idle At("images/interface/wardrobe/edit_idle.webp", interface) 
            hover At("images/interface/wardrobe/edit.webp", interface)
            
            action [
                SetVariable("current_input", Character.Outfit.name),
                Show("edit_Outfit_screen", Character = Character)]

            tooltip "Rename Outfit"

    imagebutton:
        idle At("images/interface/wardrobe/save_idle.webp", interface)
        hover At("images/interface/wardrobe/save.webp", interface)
        
        action Show("save_Outfit_screen", Character = Character)

        tooltip "Save Outfit"
        
    if Character.Outfit.Outfit_type == "custom":
        imagebutton:
            idle At("images/interface/wardrobe/delete_idle.webp", interface)
            hover At("images/interface/wardrobe/delete.webp", interface)
            
            action Show("delete_Outfit_screen", Character = Character, name = Character.Outfit.name)

            tooltip "Delete Outfit"

    button anchor (1.0, 0.5) pos (0.109, 0.062):
        background None

        hover_sound None
        activate_sound None

        text f"{int(0.25*(Character.love + Character.trust))}" align (1.0, 0.5):
            size 36

        action NullAction()

        tooltip "Shame Limit for Public Outfits"

    button anchor (1.0, 0.5) pos (0.214, 0.062):
        background None

        hover_sound None
        activate_sound None

        text f"{int(0.4*(Character.love + Character.trust))}" align (1.0, 0.5):
            size 36

        action NullAction()

        tooltip "Shame Limit for Exercise, Swimming, and Private Outfits"

    text "SHAME" anchor (0.5, 0.5) pos (0.595, 0.13):
        font "agency_fb.ttf"

        size 40

    text "TOTAL" anchor (0.5, 0.5) pos (0.595, 0.838):
        font "agency_fb.ttf"

        size 26

    button anchor (0.5, 0.5) pos (0.595, 0.793):
        background None

        hover_sound None
        activate_sound None

        text f"{Character.Outfit.shame}":
            size 36

            color "#000000"

        action NullAction()

        tooltip "Current Outfit Shame"

    if black_screen or renpy.get_screen("say"):
        button xysize (1.0, 1.0):
            background None

            hover_sound None
            activate_sound None
            
            if not renpy.get_screen("choice"):
                action Return()
            else:
                action NullAction()

    use quick_menu

    if tooltips_enabled:
        use tooltips

screen accessory_screen(Character):
    style_prefix "Wardrobe"

    viewport id "accessory_screen_viewport" anchor (1.0, 0.0) pos (0.984, 0.172) xysize (0.425, int(1249*game_resolution)):
        draggable True
        mousewheel True

        xfill True

        vbox align (0.0, 0.0):
            spacing -10

            for I in Character.Wardrobe.Clothes.values():
                if I.Clothing_type in accessory_Clothing_types:
                    hbox:
                        spacing -10
                        
                        if Character.Clothes[I.Clothing_type].string == I.string and Character.Clothes[I.Clothing_type].covered or (("swimsuit" in I.name or "bikini" in I.name) and Character.location == "bg_pool"):
                            frame xysize (int(0.0344*config.screen_width), int(240*game_resolution)):
                                text f"{I.shame[0]}":
                                    size 36

                                    text_align 0.5

                            null width int(0.0171*config.screen_width)

                            null width int(0.0344*config.screen_width)
                        else:
                            null width int(0.0344*config.screen_width)

                            null width int(0.0171*config.screen_width)

                            frame xysize (int(0.0344*config.screen_width), int(240*game_resolution)):
                                text f"{I.shame[1]}":
                                    size 36

                                    text_align 0.5

                        null width int(0.0145*config.screen_width)

                        button xysize (int(1062*game_resolution), int(240*game_resolution)):
                            idle_background At("images/interface/wardrobe/clothing_idle.webp", interface)
                            hover_background At("images/interface/wardrobe/clothing.webp", interface)
                            selected_background At("images/interface/wardrobe/clothing.webp", interface)
                    
                            selected Character.Clothes[I.Clothing_type].string == I.string

                            text I.name:
                                font "agency_fb.ttf"
                            
                                size 36

                            if Character.Clothes[I.Clothing_type].string != I.string:
                                action Call("ask_Character_to_try_on", I, instant = True, from_current = True)
                            else:
                                action Call("ask_Character_to_take_off", I, instant = True, from_current = True)
                        
                        if Character.Clothes[I.Clothing_type].string == I.string and len(Character.Clothes[I.Clothing_type].available_states["standing"]) > 1 and not Character.Clothes[I.Clothing_type].covered:
                            imagebutton:
                                idle At("images/interface/wardrobe/undressed_idle.webp", interface)
                                hover At("images/interface/wardrobe/undressed.webp", interface)
                                selected_idle At("images/interface/wardrobe/undressed.webp", interface)
                    
                                selected Character.Clothes[I.Clothing_type].state != 0

                                if Character.Clothes[I.Clothing_type].state < len(Character.Clothes[I.Clothing_type].available_states["standing"]) - 1:
                                    action Call("ask_Character_to_undress", I, state = Character.Clothes[I.Clothing_type].state + 1, instant = True, from_current = True)
                                else:
                                    action Call("ask_Character_to_redress", I, instant = True, from_current = True)
                        else:
                            null width int(260*game_resolution)

            for body_part in ["nipple", "labia"]:
                for piercing_type in ["barbell", "ring"]:
                    if f"{piercing_type}_{body_part}_piercings" in Character.inventory.keys() or f"{piercing_type}_{body_part}_piercings" in Player.inventory.keys():
                        hbox:
                            spacing -10
                            
                            null width int(0.0344*config.screen_width)

                            null width int(0.0171*config.screen_width)

                            null width int(0.0344*config.screen_width)

                            null width int(0.0145*config.screen_width)

                            button xysize (int(1062*game_resolution), int(240*game_resolution)):
                                idle_background At("images/interface/wardrobe/clothing_idle.webp", interface)
                                hover_background At("images/interface/wardrobe/clothing.webp", interface)
                                selected_background At("images/interface/wardrobe/clothing.webp", interface)
                        
                                text f"{piercing_type} {body_part} piercings":
                                    font "agency_fb.ttf"

                                    size 36
                        
                                selected Character.piercings[body_part] in [piercing_type, "both"]

                                if Character.piercings[body_part] == piercing_type:
                                    action SetDict(Character.piercings, body_part, False)
                                elif Character.piercings[body_part] == "both":
                                    if piercing_type == "barbell":
                                        action SetDict(Character.piercings, body_part, "ring")
                                    elif piercing_type == "ring":
                                        action SetDict(Character.piercings, body_part, "barbell")
                                else:
                                    action Call("give_Character_piercing", Character, Character.inventory[f"{piercing_type}_{body_part}_piercings"], from_current = True)
                                
                            null width int(260*game_resolution)

            if "belly_piercing" in Character.inventory.keys() or "belly_piercing" in Player.inventory.keys():
                hbox:
                    spacing -10
                    
                    null width int(0.0344*config.screen_width)

                    null width int(0.0171*config.screen_width)

                    null width int(0.0344*config.screen_width)

                    null width int(0.0145*config.screen_width)

                    button xysize (int(1062*game_resolution), int(240*game_resolution)):
                        idle_background At("images/interface/wardrobe/clothing_idle.webp", interface)
                        hover_background At("images/interface/wardrobe/clothing.webp", interface)
                        selected_background At("images/interface/wardrobe/clothing.webp", interface)
                    
                        text "belly piercing":
                            font "agency_fb.ttf"
                            
                            size 36

                        selected Character.piercings["belly"]

                        if Character.piercings["belly"]:
                            action SetDict(Character.piercings, "belly", False)
                        else:
                            action Call("give_Character_piercing", Character, Character.inventory["belly_piercing"], from_current = True)

                    null width int(260*game_resolution)

            if "remote_vibrator" in Character.inventory.keys():
                hbox:
                    spacing -10
                    
                    null width int(0.0344*config.screen_width)

                    null width int(0.0171*config.screen_width)

                    null width int(0.0344*config.screen_width)

                    null width int(0.0145*config.screen_width)

                    button xysize (int(1062*game_resolution), int(240*game_resolution)):
                        idle_background At("images/interface/wardrobe/clothing_idle.webp", interface)
                        hover_background At("images/interface/wardrobe/clothing.webp", interface)
                        selected_background At("images/interface/wardrobe/clothing.webp", interface)
                    
                        selected Character.remote_vibrator is not None

                        text "remote vibrator":
                            font "agency_fb.ttf"
                            
                            size 36

                        if Character.remote_vibrator is not None:
                            action SetField(Character, "remote_vibrator", None)
                        else:
                            action Call("ask_Character_to_use_Toy", Character, Character.inventory["remote_vibrator"][0], from_current = True)

                    null width int(260*game_resolution)

            for buttplug in ["heart_anal_plug", "round_anal_plug"]:
                if buttplug in Character.inventory.keys():
                    $ temp = Character.inventory[buttplug][0].name

                    for plug_size in ["XS", "S", "M", "L"]:
                        hbox:
                            spacing -10
                            
                            null width int(0.0344*config.screen_width)

                            null width int(0.0171*config.screen_width)

                            null width int(0.0344*config.screen_width)

                            null width int(0.0145*config.screen_width)

                            button xysize (int(1062*game_resolution), int(240*game_resolution)):
                                idle_background At("images/interface/wardrobe/clothing_idle.webp", interface)
                                hover_background At("images/interface/wardrobe/clothing.webp", interface)
                                selected_background At("images/interface/wardrobe/clothing.webp", interface)

                                text f"{temp}, {plug_size}":
                                    font "agency_fb.ttf"
                            
                                    size 36

                                if plug_size == "XS":
                                    selected Character.buttplug == Character.inventory[buttplug][0] and Character.buttplug_size == 0

                                    if Character.buttplug == Character.inventory[buttplug][0] and Character.buttplug_size == 0:
                                        action [
                                            SetField(Character, "buttplug", None),
                                            SetField(Character, "buttplug_size", None)]
                                    else:
                                        action Call("ask_Character_to_use_Toy", Character, Character.inventory[buttplug][0], 0, from_current = True)
                                elif plug_size == "S":
                                    selected Character.buttplug == Character.inventory[buttplug][0] and Character.buttplug_size == 1

                                    if Character.buttplug == Character.inventory[buttplug][0] and Character.buttplug_size == 1:
                                        action [
                                            SetField(Character, "buttplug", None),
                                            SetField(Character, "buttplug_size", None)]
                                    else:
                                        action Call("ask_Character_to_use_Toy", Character, Character.inventory[buttplug][0], 1, from_current = True)
                                elif plug_size == "M":
                                    selected Character.buttplug == Character.inventory[buttplug][0] and Character.buttplug_size == 2

                                    if Character.buttplug == Character.inventory[buttplug][0] and Character.buttplug_size == 2:
                                        action [
                                            SetField(Character, "buttplug", None),
                                            SetField(Character, "buttplug_size", None)]
                                    else:
                                        action Call("ask_Character_to_use_Toy", Character, Character.inventory[buttplug][0], 2, from_current = True)
                                elif plug_size == "L":
                                    selected Character.buttplug == Character.inventory[buttplug][0] and Character.buttplug_size == 3

                                    if Character.buttplug == Character.inventory[buttplug][0] and Character.buttplug_size == 3:
                                        action [
                                            SetField(Character, "buttplug", None),
                                            SetField(Character, "buttplug_size", None)]
                                    else:
                                        action Call("ask_Character_to_use_Toy", Character, Character.inventory[buttplug][0], 3, from_current = True)

                            null width int(260*game_resolution)

            if False:
                if Character in [Rogue]:
                    $ left_arms = [
                        "bra", "crossed", "extended", "fight", "fist", "grope", "hip", "neutral", "rub_neck", "touch_ass"]
                elif Character in [Laura]:
                    $ left_arms = [
                        "bra", "claws", "crossed", "extended", "fight", "fist", "grope", "hip", "neutral", "rub_neck", "touch_ass", "X"]
                elif Character in [Jean]:
                    $ left_arms = [
                        "bra", "crossed", "extended", "fight", "fist", "grope", "hip", "neutral", "psychic1", "psychic2", "rub_neck", "touch_ass"]
                elif Character in [Ororo]:
                    $ left_arms = [
                        "bra", "crossed", "extended", "fight", "fist", "grope", "hip", "neutral", "rub_neck", "storm1", "storm2", "touch_ass"]

                for left_arm in left_arms:
                    hbox:
                        spacing -10
                        
                        null width int(0.0344*config.screen_width)

                        null width int(0.0171*config.screen_width)

                        null width int(0.0344*config.screen_width)

                        null width int(0.0145*config.screen_width)

                        button xysize (int(1062*game_resolution), int(240*game_resolution)):
                            idle_background At("images/interface/wardrobe/clothing_idle.webp", interface)
                            hover_background At("images/interface/wardrobe/clothing.webp", interface)

                            text f"left arm: {left_arm}":
                                font "agency_fb.ttf"
                            
                                size 36

                            if left_arm == "crossed":
                                action [
                                    SetField(Character, "left_arm", left_arm),
                                    SetField(Character, "right_arm", left_arm)]
                            elif Character.right_arm == "crossed":
                                action [
                                    SetField(Character, "left_arm", left_arm),
                                    SetField(Character, "right_arm", "neutral")]
                            else:
                                action SetField(Character, "left_arm", left_arm)

                        null width int(260*game_resolution)

                if Character in [Rogue]:
                    $ right_arms = [
                        "bra", "crossed", "extended", "fight", "fist", "hip", "neutral", "touch_pussy"]
                elif Character in [Laura]:
                    $ right_arms = [
                        "bra", "claws", "crossed", "extended", "fight", "fist", "hip", "neutral", "touch_pussy", "X"]
                elif Character in [Jean]:
                    $ right_arms = [
                        "bra", "crossed", "extended", "fight", "fist", "hip", "neutral", "psychic1", "psychic2", "touch_pussy"]
                elif Character in [Ororo]:
                    $ right_arms = [
                        "bra", "crossed", "extended", "fight", "fist", "hip", "neutral", "storm1", "storm2", "touch_pussy"]

                for right_arm in right_arms:
                    hbox:
                        spacing -10
                        
                        null width int(0.0344*config.screen_width)

                        null width int(0.0171*config.screen_width)

                        null width int(0.0344*config.screen_width)

                        null width int(0.0145*config.screen_width)

                        button xysize (int(1062*game_resolution), int(240*game_resolution)):
                            idle_background At("images/interface/wardrobe/clothing_idle.webp", interface)
                            hover_background At("images/interface/wardrobe/clothing.webp", interface)

                            text f"right arm: {right_arm}":
                                font "agency_fb.ttf"
                            
                                size 36

                            if right_arm == "crossed":
                                action [
                                    SetField(Character, "left_arm", right_arm),
                                    SetField(Character, "right_arm", right_arm)]
                            elif Character.left_arm == "crossed":
                                action [
                                    SetField(Character, "left_arm", "neutral"),
                                    SetField(Character, "right_arm", right_arm)]
                            else:
                                action SetField(Character, "right_arm", right_arm)

                        null width int(260*game_resolution)

    vbar value YScrollValue("accessory_screen_viewport") anchor (0.5, 0.0) pos (0.982, 0.172) xysize (int(29*game_resolution), int(1249*game_resolution)):
        base_bar At("images/interface/wardrobe/clothing_scrollbar.webp", interface)

        thumb At("images/interface/wardrobe/clothing_scrollbar_thumb.webp", interface)
        thumb_offset int(212*game_resolution/2/10)

        unscrollable "hide"

screen hair_screen(Character):
    style_prefix "Wardrobe"

    viewport id "hair_screen_viewport" anchor (1.0, 0.0) pos (0.984, 0.172) xysize (0.425, int(1249*game_resolution)):
        draggable True
        mousewheel True

        xfill True

        vbox align (0.0, 0.0):
            spacing -10

            for I in Character.Wardrobe.Clothes.values():
                if I.Clothing_type == "hair":
                    hbox:
                        spacing -10
                        
                        null width int(0.0344*config.screen_width)

                        null width int(0.0171*config.screen_width)

                        null width int(0.0344*config.screen_width)

                        null width int(0.0145*config.screen_width)

                        button xysize (int(1062*game_resolution), int(240*game_resolution)):
                            idle_background At("images/interface/wardrobe/clothing_idle.webp", interface)
                            hover_background At("images/interface/wardrobe/clothing.webp", interface)
                            selected_background At("images/interface/wardrobe/clothing.webp", interface)
                    
                            selected Character.Clothes["hair"].string == I.string

                            text f"hair: {I.string}":
                                font "agency_fb.ttf"
                            
                                size 36

                            if Character.Clothes["hair"].string != I.string:
                                action Call("ask_Character_to_try_on", I, instant = True, from_current = True)
                            else:
                                action NullAction()

                        null width int(260*game_resolution)

            if Character.check_traits("customizable_pubes"):
                for hair_style in ["bush", "growing", "hairy", "null", "shaven", "strip", "strip_thick", "triangle", "triangle_large"]:
                    hbox:
                        spacing -10
                        
                        null width int(0.0344*config.screen_width)

                        null width int(0.0171*config.screen_width)

                        null width int(0.0344*config.screen_width)

                        null width int(0.0145*config.screen_width)

                        button xysize (int(1062*game_resolution), int(240*game_resolution)):
                            idle_background At("images/interface/wardrobe/clothing_idle.webp", interface)
                            hover_background At("images/interface/wardrobe/clothing.webp", interface)
                            selected_background At("images/interface/wardrobe/clothing.webp", interface)
                    
                            if hair_style == "shaven":
                                selected Character.desired_body_hair["pubic"] == None
                            else:
                                selected Character.desired_body_hair["pubic"] == hair_style

                            if "_" in hair_style:
                                text f"pubic hair: {hair_style.split('_')[1]} {hair_style.split('_')[0]}":
                                    font "agency_fb.ttf"
                            
                                    size 36
                            else:
                                text f"pubic hair: {hair_style}":
                                    font "agency_fb.ttf"
                            
                                    size 36
            
                            if Character.desired_body_hair["pubic"] == hair_style:
                                action NullAction()
                            else:
                                if hair_style == "shaven":
                                    action [
                                        SetDict(Character.body_hair, "pubic", None),
                                        SetVariable("Wardrobe_animation_time", 1.0),
                                        SetVariable("Wardrobe_position", [0.5, 1.8]),
                                        SetVariable("Wardrobe_zoom", 1.0/eval(f"{Character.tag}_standing_zoom"))]
                                else:
                                    action [
                                        SetDict(Character.body_hair, "pubic", hair_style),
                                        SetVariable("Wardrobe_animation_time", 1.0),
                                        SetVariable("Wardrobe_position", [0.5, 1.8]),
                                        SetVariable("Wardrobe_zoom", 1.0/eval(f"{Character.tag}_standing_zoom"))]
                                # action [
                                #     SetVariable("changed_body_hair", True),
                                #     Call("ask_Character_to_shave", Character, hair_style, from_current = True)]

                        null width int(260*game_resolution)
                        
            if False:
                $ brows = [
                    "neutral", "cocked", "furrowed", "raised", "wink", "worried"]

                for brow in brows:
                    hbox:
                        spacing -10
                        
                        null width int(0.0344*config.screen_width)

                        null width int(0.0171*config.screen_width)

                        null width int(0.0344*config.screen_width)

                        null width int(0.0145*config.screen_width)

                        button xysize (int(1062*game_resolution), int(240*game_resolution)):
                            idle_background At("images/interface/wardrobe/clothing_idle.webp", interface)
                            hover_background At("images/interface/wardrobe/clothing.webp", interface)

                            action SetField(Character, "brows", brow)

                            text f"brows: {brow}":
                                font "agency_fb.ttf"
                            
                                size 36

                        null width int(260*game_resolution)

                $ eyes = [
                    "neutral", "blink1", "blink2", "closed", "down", "left", "right", "sexy", "squint", "up", "wide", "wink"]

                for eye in eyes:
                    hbox:
                        spacing -10
                        
                        null width int(0.0344*config.screen_width)

                        null width int(0.0171*config.screen_width)

                        null width int(0.0344*config.screen_width)

                        null width int(0.0145*config.screen_width)

                        button xysize (int(1062*game_resolution), int(240*game_resolution)):
                            idle_background At("images/interface/wardrobe/clothing_idle.webp", interface)
                            hover_background At("images/interface/wardrobe/clothing.webp", interface)

                            action SetField(Character, "eyes", eye)

                            text f"eyes: {eye}":
                                font "agency_fb.ttf"

                                size 36

                        null width int(260*game_resolution)

                if Character in [Laura]:
                    $ mouths = [
                        "neutral", "agape", "frown", "happy", "kiss", "lipbite", "open", "smile", "smirk", "snarl", "tongue"]
                else:
                    $ mouths = [
                        "neutral", "agape", "frown", "happy", "kiss", "lipbite", "open", "smile", "smirk", "tongue"]

                for mouth in mouths:
                    hbox:
                        spacing -10
                        
                        null width int(0.0344*config.screen_width)

                        null width int(0.0171*config.screen_width)

                        null width int(0.0344*config.screen_width)

                        null width int(0.0145*config.screen_width)

                        button xysize (int(1062*game_resolution), int(240*game_resolution)):
                            idle_background At("images/interface/wardrobe/clothing_idle.webp", interface)
                            hover_background At("images/interface/wardrobe/clothing.webp", interface)

                            action SetField(Character, "mouth", mouth)

                            text f"mouth: {mouth}":
                                font "agency_fb.ttf"

                                size 36

                        null width int(260*game_resolution)

                if Character in [Laura]:
                    $ faces = [
                        "neutral", "angry1", "angry2", "appalled1", "appalled2", "appalled3", 
                        "confused1", "confused2", "confused3", "devious",
                        "furious", "grimace", "happy", "kiss1", "kiss2", "manic",
                        "perplexed", "pleased1", "pleased2", "sad",
                        "sexy", "sly", "smirk1", "smirk2", "snarl", "surprised1", "surprised2", "surprised3",
                        "suspicious1", "suspicious2", "wink", "worried1", "worried2", "worried3", "worried4"]
                else:
                    $ faces = [
                        "neutral", "angry1", "angry2", "appalled1", "appalled2", "appalled3", 
                        "confused1", "confused2", "confused3", "devious",
                        "furious", "grimace", "happy", "kiss1", "kiss2", "manic",
                        "perplexed", "pleased1", "pleased2", "sad",
                        "sexy", "sly", "smirk1", "smirk2", "surprised1", "surprised2", "surprised3",
                        "suspicious1", "suspicious2", "wink", "worried1", "worried2", "worried3", "worried4"]

                for face in faces:
                    hbox:
                        spacing -10
                        
                        null width int(0.0344*config.screen_width)

                        null width int(0.0171*config.screen_width)

                        null width int(0.0344*config.screen_width)

                        null width int(0.0145*config.screen_width)

                        button xysize (int(1062*game_resolution), int(240*game_resolution)):
                            idle_background At("images/interface/wardrobe/clothing_idle.webp", interface)
                            hover_background At("images/interface/wardrobe/clothing.webp", interface)

                            action Function(Character.change_face, face)

                            text f"face: {face}":
                                font "agency_fb.ttf"
                                
                                size 36

                        null width int(260*game_resolution)

    vbar value YScrollValue("hair_screen_viewport") anchor (0.5, 0.0) pos (0.982, 0.172) xysize (int(29*game_resolution), int(1249*game_resolution)):
        base_bar At("images/interface/wardrobe/clothing_scrollbar.webp", interface)

        thumb At("images/interface/wardrobe/clothing_scrollbar_thumb.webp", interface)
        thumb_offset int(212*game_resolution/2/10)

        unscrollable "hide"

screen upper_screen(Character):
    style_prefix "Wardrobe"

    viewport id "upper_screen_viewport" anchor (1.0, 0.0) pos (0.984, 0.172) xysize (0.425, int(1249*game_resolution)):
        draggable True
        mousewheel True

        xfill True

        vbox align (0.0, 0.0):
            spacing -10

            for I in Character.Wardrobe.Clothes.values():
                if I.Clothing_type in upper_Clothing_types:
                    hbox:
                        spacing -10
                        
                        if Character.Clothes[I.Clothing_type].string == I.string and Character.Clothes[I.Clothing_type].covered or (("swimsuit" in I.name or "bikini" in I.name) and Character.location == "bg_pool"):
                            frame xysize (int(0.0344*config.screen_width), int(240*game_resolution)):
                                text f"{I.shame[0]}":
                                    size 36

                                    text_align 0.5

                            null width int(0.0171*config.screen_width)

                            null width int(0.0344*config.screen_width)
                        else:
                            null width int(0.0344*config.screen_width)

                            null width int(0.0171*config.screen_width)

                            frame xysize (int(0.0344*config.screen_width), int(240*game_resolution)):
                                text f"{I.shame[1]}":
                                    size 36

                                    text_align 0.5

                        null width int(0.0145*config.screen_width)

                        button xysize (int(1062*game_resolution), int(240*game_resolution)):
                            idle_background At("images/interface/wardrobe/clothing_idle.webp", interface)
                            hover_background At("images/interface/wardrobe/clothing.webp", interface)
                            selected_background At("images/interface/wardrobe/clothing.webp", interface)
                    
                            selected Character.Clothes[I.Clothing_type].string == I.string

                            text I.name:
                                font "agency_fb.ttf"
                            
                                size 36

                            if Character.Clothes[I.Clothing_type].string != I.string:
                                action Call("ask_Character_to_try_on", I, instant = True, from_current = True)
                            else:
                                action Call("ask_Character_to_take_off", I, instant = True, from_current = True)
                        
                        if Character.Clothes[I.Clothing_type].string == I.string and len(Character.Clothes[I.Clothing_type].available_states["standing"]) > 1 and not Character.Clothes[I.Clothing_type].covered:
                            imagebutton:
                                idle At("images/interface/wardrobe/undressed_idle.webp", interface)
                                hover At("images/interface/wardrobe/undressed.webp", interface)
                                selected_idle At("images/interface/wardrobe/undressed.webp", interface)
                    
                                selected Character.Clothes[I.Clothing_type].state != 0

                                if Character.Clothes[I.Clothing_type].state < len(Character.Clothes[I.Clothing_type].available_states["standing"]) - 1:
                                    action Call("ask_Character_to_undress", I, state = Character.Clothes[I.Clothing_type].state + 1, instant = True, from_current = True)
                                else:
                                    action Call("ask_Character_to_redress", I, instant = True, from_current = True)
                        else:
                            null width int(260*game_resolution)

    vbar value YScrollValue("upper_screen_viewport") anchor (0.5, 0.0) pos (0.982, 0.172) xysize (int(29*game_resolution), int(1249*game_resolution)):
        base_bar At("images/interface/wardrobe/clothing_scrollbar.webp", interface)

        thumb At("images/interface/wardrobe/clothing_scrollbar_thumb.webp", interface)
        thumb_offset int(212*game_resolution/2/10)

        unscrollable "hide"

screen lower_screen(Character):
    style_prefix "Wardrobe"
    
    viewport id "lower_screen_viewport" anchor (1.0, 0.0) pos (0.984, 0.172) xysize (0.425, int(1249*game_resolution)):
        draggable True
        mousewheel True

        xfill True

        vbox align (0.0, 0.0):
            spacing -10

            for I in Character.Wardrobe.Clothes.values():
                if I.Clothing_type in lower_Clothing_types:
                    hbox:
                        spacing -10
                        
                        if Character.Clothes[I.Clothing_type].string == I.string and Character.Clothes[I.Clothing_type].covered or (("swimsuit" in I.name or "bikini" in I.name) and Character.location == "bg_pool"):
                            frame xysize (int(0.0344*config.screen_width), int(240*game_resolution)):
                                text f"{I.shame[0]}":
                                    size 36

                                    text_align 0.5

                            null width int(0.0171*config.screen_width)

                            null width int(0.0344*config.screen_width)
                        else:
                            null width int(0.0344*config.screen_width)

                            null width int(0.0171*config.screen_width)

                            frame xysize (int(0.0344*config.screen_width), int(240*game_resolution)):
                                text f"{I.shame[1]}":
                                    size 36

                                    text_align 0.5

                        null width int(0.0145*config.screen_width)

                        button xysize (int(1062*game_resolution), int(240*game_resolution)):
                            idle_background At("images/interface/wardrobe/clothing_idle.webp", interface)
                            hover_background At("images/interface/wardrobe/clothing.webp", interface)
                            selected_background At("images/interface/wardrobe/clothing.webp", interface)
                    
                            selected Character.Clothes[I.Clothing_type].string == I.string

                            text I.name:
                                font "agency_fb.ttf"
                            
                                size 36

                            if Character.Clothes[I.Clothing_type].string != I.string:
                                action Call("ask_Character_to_try_on", I, instant = True, from_current = True)
                            else:
                                action Call("ask_Character_to_take_off", I, instant = True, from_current = True)
                        
                        if Character.Clothes[I.Clothing_type].string == I.string and len(Character.Clothes[I.Clothing_type].available_states["standing"]) > 1 and not Character.Clothes[I.Clothing_type].covered:
                            imagebutton:
                                idle At("images/interface/wardrobe/undressed_idle.webp", interface)
                                hover At("images/interface/wardrobe/undressed.webp", interface)
                                selected_idle At("images/interface/wardrobe/undressed.webp", interface)
                    
                                selected Character.Clothes[I.Clothing_type].state != 0

                                if Character.Clothes[I.Clothing_type].state < len(Character.Clothes[I.Clothing_type].available_states["standing"]) - 1:
                                    action Call("ask_Character_to_undress", I, state = Character.Clothes[I.Clothing_type].state + 1, instant = True, from_current = True)
                                else:
                                    action Call("ask_Character_to_redress", I, instant = True, from_current = True)
                        else:
                            null width int(260*game_resolution)

    vbar value YScrollValue("lower_screen_viewport") anchor (0.5, 0.0) pos (0.982, 0.172) xysize (int(29*game_resolution), int(1249*game_resolution)):
        base_bar At("images/interface/wardrobe/clothing_scrollbar.webp", interface)

        thumb At("images/interface/wardrobe/clothing_scrollbar_thumb.webp", interface)
        thumb_offset int(212*game_resolution/2/10)

        unscrollable "hide"

screen save_Outfit_screen(Character):
    modal True

    style_prefix "Wardrobe"

    on "show" action [
        SetVariable("current_input", ""),
        SetVariable("current_Outfit_color", None),
        SetVariable("current_flags", [])]

    $ Outfit_list = []

    for O in Character.Wardrobe.Outfits.values():
        if O.Outfit_type == Wardrobe_tab:
            $ Outfit_list.append(O)

    add "images/interface/wardrobe/popup_background.webp" zoom interface_adjustment

    # if blinking:
    text "OUTFIT NAME" + "{alpha=0.0}_{/alpha}" anchor (0.0, 0.5) pos (0.242, 0.241):
        size 28
    # else:
    #     text "OUTFIT NAME" + "_" anchor (0.0, 0.5) pos (0.242, 0.241):
    #         size 28

    input id "input" value VariableInputValue("current_input", default = True) anchor (0.5, 0.5) pos (0.372, 0.294):
        font "agency_fb.ttf"

        size 28

        color "#ffffff"
                    
        length 20

    # if blinking:
    text "OUTFIT COLOR" + "{alpha=0.0}_{/alpha}" anchor (0.0, 0.5) pos (0.242, 0.344):
        size 28
    # else:
    #     text "OUTFIT COLOR" + "_" anchor (0.0, 0.5) pos (0.242, 0.344):
    #         size 28

    hbox anchor (0.5, 0.5) pos (0.374, 0.4) ysize int(114*game_resolution):
        spacing 15

        for Outfit_color in ["blue", "green", "pink", "purple", "red"]:
            imagebutton:
                idle At(f"images/interface/wardrobe/{Outfit_color}_icon.webp", interface)
                hover At(f"images/interface/wardrobe/{Outfit_color}_icon.webp", interface)

                selected_foreground At("images/interface/wardrobe/color_selector.webp", interface)

                selected current_Outfit_color == Outfit_color

                action SetVariable("current_Outfit_color", Outfit_color)

    # if blinking:
    text "OUTFIT FLAGS" + "{alpha=0.0}_{/alpha}" anchor (0.0, 0.5) pos (0.242, 0.455):
        size 28
    # else:
    #     text "OUTFIT FLAGS" + "_" anchor (0.0, 0.5) pos (0.242, 0.42):
    #         size 28

    vpgrid id "Wardrobe_save_flags_viewport" anchor (0.5, 0.0) pos (0.374, 0.475) xysize (0.22, int(646*game_resolution)):
        cols 4

        draggable True
        mousewheel True
        
        spacing -17

        for flag in ["public", "winter", "day", "date", "exercise", "hero", "swim", "empty", "private", "sexy", "sleep"]:
            if flag in ["public", "day"]:
                $ color = "blue"
            elif flag in ["exercise", "hero", "swim"]:
                $ color = "red"
            elif flag in ["private", "sexy", "sleep"]:
                $ color = "pink"

            if flag != "empty":
                button xysize (int(240*game_resolution), int(115*game_resolution)):
                    idle_background At(f"images/interface/wardrobe/tag_{color}.webp", interface)
                    hover_background At(f"images/interface/wardrobe/tag_{color}.webp", interface)

                    selected_foreground At(At("images/interface/wardrobe/tag_selector.webp", interface), Transform(anchor = (0.5, 0.5), pos = (0.504, 0.515)))

                    selected flag in current_flags

                    text flag.upper() anchor (0.5, 0.5) pos (0.504, 0.515):
                        size 26

                    if flag in current_flags:
                        action RemoveFromSet(current_flags, flag)
                    else:
                        action AddToSet(current_flags, flag)
            else:
                null width int(240*game_resolution) height int(115*game_resolution)

    vbar value YScrollValue("Wardrobe_save_flags_viewport") anchor (0.5, 0.0) pos (0.52, 0.475) xysize (int(29*game_resolution), int(646*game_resolution)):
        base_bar At("images/interface/wardrobe/popup_scrollbar.webp", interface)

        thumb At("images/interface/wardrobe/popup_scrollbar_thumb.webp", interface)
        thumb_offset int(212*game_resolution/2/10)

        unscrollable "hide"

    imagebutton:
        idle At("images/interface/wardrobe/continue_idle.webp", interface)
        hover At("images/interface/wardrobe/continue.webp", interface)

        if current_Outfit_color:
            if current_input in Character.Wardrobe.Outfits.keys() and Character.Wardrobe.Outfits[current_input].Outfit_type == "custom":
                action [
                    Hide("save_Outfit_screen"), 
                    SetVariable("Wardrobe_tab", "default"),
                    Show("confirm_overwrite_screen", Character = Character)]
            elif current_input in Character.Wardrobe.Outfits.keys() and Character.Wardrobe.Outfits[current_input].Outfit_type == "default":
                action [
                    Hide("save_Outfit_screen"), 
                    Show("cannot_overwrite_screen", Character = Character)]

                tooltip "Save Outfit"
            elif current_input:
                if len(Outfit_list) < 28:
                    action [
                        Hide("save_Outfit_screen"), 
                        SetVariable("Wardrobe_tab", "default"),
                        Call("save_new_Outfit", Character, current_input, current_Outfit_color, current_flags, from_current = True)]
                else:
                    action [
                        Hide("save_Outfit_screen"), 
                        Show("cannot_save_screen", Character = Character)]

    imagebutton:
        idle At("images/interface/wardrobe/cancel_idle.webp", interface)
        hover At("images/interface/wardrobe/cancel.webp", interface)

        action Hide("save_Outfit_screen")

        tooltip "Cancel"

    if tooltips_enabled:
        use tooltips

screen edit_Outfit_screen(Character):
    modal True

    style_prefix "Wardrobe"

    on "show" action [
        SetVariable("current_input", Character.Outfit.name),
        SetVariable("current_Outfit_color", Character.Outfit.color),
        SetVariable("current_flags", Character.Outfit.flags)]

    add "images/interface/wardrobe/popup_background.webp" zoom interface_adjustment

    # if blinking:
    text "OUTFIT NAME" + "{alpha=0.0}_{/alpha}" anchor (0.0, 0.5) pos (0.242, 0.241):
        size 28
    # else:
    #     text "OUTFIT NAME" + "_" anchor (0.0, 0.5) pos (0.242, 0.241):
    #         size 28

    input id "input" value VariableInputValue("current_input", default = True) anchor (0.5, 0.5) pos (0.372, 0.294):
        font "agency_fb.ttf"

        size 28

        color "#ffffff"
                    
        length 20

    # if blinking:
    text "OUTFIT COLOR" + "{alpha=0.0}_{/alpha}" anchor (0.0, 0.5) pos (0.242, 0.344):
        size 28
    # else:
    #     text "OUTFIT COLOR" + "_" anchor (0.0, 0.5) pos (0.242, 0.344):
    #         size 28

    hbox anchor (0.5, 0.5) pos (0.374, 0.4) ysize int(114*game_resolution):
        spacing 15

        for Outfit_color in ["blue", "green", "pink", "purple", "red"]:
            imagebutton:
                idle At(f"images/interface/wardrobe/{Outfit_color}_icon.webp", interface)
                hover At(f"images/interface/wardrobe/{Outfit_color}_icon.webp", interface)

                selected_foreground At("images/interface/wardrobe/color_selector.webp", interface)

                selected current_Outfit_color == Outfit_color

                action SetVariable("current_Outfit_color", Outfit_color)
                    
    # if blinking:
    text "OUTFIT FLAGS" + "{alpha=0.0}_{/alpha}" anchor (0.0, 0.5) pos (0.242, 0.455):
        size 28
    # else:
    #     text "OUTFIT FLAGS" + "_" anchor (0.0, 0.5) pos (0.242, 0.42):
    #         size 28

    vpgrid id "Wardrobe_edit_flags_viewport" anchor (0.5, 0.0) pos (0.374, 0.475) xysize (0.22, int(646*game_resolution)):
        cols 4

        draggable True
        mousewheel True
        
        spacing -17

        for flag in ["public", "winter", "day", "date", "exercise", "hero", "swim", "empty", "private", "sexy", "sleep"]:
            if flag in ["public", "day"]:
                $ color = "blue"
            elif flag in ["exercise", "hero", "swim"]:
                $ color = "red"
            elif flag in ["private", "sexy", "sleep"]:
                $ color = "pink"

            if flag != "empty":
                button xysize (int(240*game_resolution), int(115*game_resolution)):
                    idle_background At(f"images/interface/wardrobe/tag_{color}.webp", interface)
                    hover_background At(f"images/interface/wardrobe/tag_{color}.webp", interface)

                    selected_foreground At(At("images/interface/wardrobe/tag_selector.webp", interface), Transform(anchor = (0.5, 0.5), pos = (0.504, 0.515)))

                    selected flag in current_flags

                    text flag.upper() anchor (0.5, 0.5) pos (0.504, 0.515):
                        size 26

                    if flag in current_flags:
                        action RemoveFromSet(current_flags, flag)
                    else:
                        action AddToSet(current_flags, flag)
            else:
                null width int(240*game_resolution) height int(115*game_resolution)

    vbar value YScrollValue("Wardrobe_edit_flags_viewport") anchor (0.5, 0.0) pos (0.52, 0.475) xysize (int(29*game_resolution), int(646*game_resolution)):
        base_bar At("images/interface/wardrobe/popup_scrollbar.webp", interface)

        thumb At("images/interface/wardrobe/popup_scrollbar_thumb.webp", interface)
        thumb_offset int(212*game_resolution/2/10)

        unscrollable "hide"
                    
    imagebutton:
        idle At("images/interface/wardrobe/continue_idle.webp", interface)
        hover At("images/interface/wardrobe/continue.webp", interface)

        if current_Outfit_color:
            if current_input in Character.Wardrobe.Outfits.keys() and Character.Wardrobe.Outfits[current_input].Outfit_type == "custom":
                action [
                    Hide("edit_Outfit_screen"), 
                    Show("confirm_overwrite_screen", Character = Character, editing = True)]
            elif current_input in Character.Wardrobe.Outfits.keys() and Character.Wardrobe.Outfits[current_input].Outfit_type == "default":
                action [
                    Hide("edit_Outfit_screen"), 
                    Show("cannot_overwrite_screen", Character = Character)]
            elif current_input:
                action [
                    Hide("edit_Outfit_screen"), 
                    Call("edit_Outfit", Character, Character.Outfit, current_input, current_Outfit_color, current_flags, from_current = True)]

        tooltip "Save Outfit"

    imagebutton:
        idle At("images/interface/wardrobe/cancel_idle.webp", interface)
        hover At("images/interface/wardrobe/cancel.webp", interface)

        action Hide("edit_Outfit_screen")

        tooltip "Cancel"

    if tooltips_enabled:
        use tooltips

screen delete_Outfit_screen(Character, name):
    modal True

    style_prefix "confirm"

    frame anchor (0.5, 0.5) pos (0.5, 0.75):
        vbox:
            spacing 25

            text f"Delete outfit?":
                size 36

            hbox:
                spacing 100

                textbutton _("Yes"):
                    action [
                        Hide("delete_Outfit_screen"),
                        SetField(Character, "Outfit", Character.Wardrobe.indoor_Outfit),
                        Function(Character.Wardrobe.remove_Outfit, name),
                        SetVariable("current_Wardrobe_Outfit_page", 0)] 
                        
                    text_size 36

                textbutton _("No"):
                    action Hide("delete_Outfit_screen") 
                    
                    text_size 36

screen confirm_overwrite_screen(Character, editing = False):
    modal True

    style_prefix "confirm"

    frame anchor (0.5, 0.5) pos (0.5, 0.5):
        vbox:
            spacing 25

            text f"Overwrite {current_input}?":
                size 40
                
            hbox:
                spacing 100

                textbutton _("Yes"): 
                    text_size 36

                    if editing:
                        action [
                            Hide("confirm_overwrite_screen"),
                            Call("edit_Outfit", Character, Character.Outfit, current_input, current_Outfit_color, current_flags, from_current = True)]
                    else:
                        action [
                            Hide("confirm_overwrite_screen"),
                            Call("save_new_Outfit", Character, current_input, current_Outfit_color, current_flags, from_current = True)]

                textbutton _("No"): 
                    text_size 36

                    action Hide("confirm_overwrite_screen")
                    
screen cannot_overwrite_screen(Character):
    modal True

    style_prefix "confirm"

    frame anchor (0.5, 0.5) pos (0.5, 0.5):
        vbox:
            spacing 25

            text f"Cannot overwrite default outfit {current_input}.":
                size 40

            textbutton _("Back"):
                text_size 36

                action [
                    Hide("cannot_overwrite_screen"), 
                    Show("save_Outfit_screen", Character = Character)]
                    
screen cannot_save_screen(Character):
    modal True

    style_prefix "confirm"

    frame anchor (0.5, 0.5) pos (0.5, 0.5):
        vbox:
            spacing 25

            text f"Wardrobe is full - delete custom outfits to save more.":
                size 40

            textbutton _("Back"):
                text_size 36

                action [
                    Hide("cannot_save_screen"), 
                    Show("save_Outfit_screen", Character = Character)]