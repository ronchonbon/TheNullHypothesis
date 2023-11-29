init -1 python:

    import math

init -1:

    default Wardrobe_tab = "default"
    default current_Wardrobe_screen = None
    default current_Wardrobe_Outfit_page = 0

    default hovered_Outfit_name = None

    default current_input = ""
    default current_Outfit_color = "yellow"
    default current_flags = {
        "wear_in_public": False,
        "wear_in_private": False,
        "activewear": False,
        "swimwear": False,
        "datewear": False,
        "sexwear": False,
        "sleepwear": False,
        "winterwear": False}

    default changed_pubes = False

image Wardrobe_selector:
    "images/interface/wardrobe/selector.webp" 
    
    anchor (0.5, 0.5)
    pos (0.5, 0.4)

image small_save:
    "images/interface/wardrobe/save.webp"

    zoom 0.67

image small_save_idle:
    "images/interface/wardrobe/save_idle.webp"

    zoom 0.67

image small_delete:
    "images/interface/wardrobe/delete.webp"

    zoom 0.67

image small_delete_idle:
    "images/interface/wardrobe/delete_idle.webp"

    zoom 0.67

style Wardrobe is default

style Wardrobe_button:
    idle_background Frame("images/interface/wardrobe/clothing_idle.webp", 30, 30)
    hover_background Frame("images/interface/wardrobe/clothing.webp", 30, 30)

    padding (10, 10, 10, 10)

    minimum (int(config.screen_width*0.2), int(config.screen_height*0.07))
    xmaximum int(config.screen_width*0.2)

    # hover_sound "sounds/interface/hover.ogg"
    activate_sound "sounds/interface/press.ogg"

style Wardrobe_image_button:
    # hover_sound "sounds/interface/hover.ogg"
    activate_sound "sounds/interface/press.ogg"

screen Wardrobe_screen(Girl):
    layer "interface"

    style_prefix "Wardrobe"

    on "show" action [
        Function(check_predicted_images),
        SetVariable("belt_hidden", True),
        SetVariable("say_obscured", True), 
        SetVariable("choice_disabled", True), 
        SetVariable("Character_picker_disabled", True),
        SetVariable("tab", "default"),
        SetVariable("changed_pubes", False),
        SetField(Girl, "previous_Outfit", Girl.Outfit.name)]
    on "hide" action [
        SetVariable("current_Wardrobe_screen", None),
        SetVariable("current_Wardrobe_Outfit_page", 0)]

    $ Outfit_list = []

    for O in Girl.Wardrobe.Outfits.values():
        if O.Outfit_type == Wardrobe_tab:
            $ Outfit_list.append(O)

    add "images/interface/wardrobe/background.webp" align (0.5, 0.5)

    add At(f"{Girl.tag}_sprite standing", color_shade(eval(f"{Girl.tag}_color"))) anchor (Girl.sprite_anchor[0], Girl.sprite_anchor[1]) pos (0.4, eval(f"{Girl.tag}_standing_height")) zoom Girl.sprite_zoom

    imagebutton align (0.5, 0.5):
        idle "images/interface/wardrobe/default_idle.webp" hover "images/interface/wardrobe/default.webp" selected_idle "images/interface/wardrobe/default_selected.webp" selected_hover "images/interface/wardrobe/default_selected.webp"

        selected "Wardrobe_tab" == "default"

        action [
            SetScreenVariable("current_Wardrobe_Outfit_page", 0),
            SetVariable("Wardrobe_tab", "default")]

        focus_mask True

        tooltip "Default Outfits"

    imagebutton align (0.5, 0.5):
        idle "images/interface/wardrobe/custom_idle.webp" hover "images/interface/wardrobe/custom.webp" selected_idle "images/interface/wardrobe/custom_selected.webp" selected_hover "images/interface/wardrobe/custom_selected.webp"

        selected "Wardrobe_tab" == "custom"

        action [
            SetScreenVariable("current_Wardrobe_Outfit_page", 0),
            SetVariable("Wardrobe_tab", "custom")]

        focus_mask True

        tooltip "Custom Outfits"

    imagebutton align (0.5, 0.5):
        idle "images/interface/wardrobe/left_idle.webp" hover "images/interface/wardrobe/left.webp"
        
        if len(Outfit_list) > 0:
            action SetScreenVariable("current_Wardrobe_Outfit_page", (current_Wardrobe_Outfit_page - 1) % math.ceil(len(Outfit_list)/3))    
        else:
            action None

        focus_mask True

    imagebutton align (0.5, 0.5):
        idle "images/interface/wardrobe/right_idle.webp" hover "images/interface/wardrobe/right.webp"

        if len(Outfit_list) > 0:
            action SetScreenVariable("current_Wardrobe_Outfit_page", (current_Wardrobe_Outfit_page + 1) % math.ceil(len(Outfit_list)/3))    
        else:
            action None

        focus_mask True

    hbox anchor (0.5, 0.5) pos (0.718, 0.11):
        spacing 5

        $ flag = are_Characters_in_Partners(Present)

        for i in range(3*current_Wardrobe_Outfit_page, 3*current_Wardrobe_Outfit_page + 3):
            if i <= len(Outfit_list) - 1 and approval_check(Girl, threshold = 0.4*Outfit_list[i].shame):
                imagebutton:
                    idle f"images/interface/wardrobe/{Outfit_list[i].color}_idle.webp" hover f"images/interface/wardrobe/{Outfit_list[i].color}.webp" selected_idle "images/interface/wardrobe/outfit_selected.webp"
                    
                    selected Girl.Outfit.name == Outfit_list[i].name

                    hovered SetScreenVariable("hovered_Outfit_name", Outfit_list[i].name)
                    unhovered SetScreenVariable("hovered_Outfit_name", False)

                    if Girl.Outfit.name != Outfit_list[i].name:
                        action Call("ask_Girl_to_change_Outfit", Girl, Outfit_list[i].name, instant = True, from_current = True)
                    else:
                        action NullAction()

                    tooltip "Change Outfits"
            elif i <= len(Outfit_list) - 1 and not approval_check(Girl, threshold = 0.4*Outfit_list[i].shame):
                add f"images/interface/wardrobe/{Outfit_list[i].color}_idle.webp"
            else:
                null width 108

    grid 3 3 anchor (0.5, 0.5) pos (0.935, 0.09):
        spacing 5

        for i in range(math.ceil(len(Outfit_list)/3)):
            if i == current_Wardrobe_Outfit_page:
                add "images/interface/wardrobe/page.webp"
            else:
                add "images/interface/wardrobe/page_empty.webp"

    text "OUTFIT NAME:" anchor (0.0, 0.5) pos (0.6, 0.205):
        size 42

        color "#512908"

    if hovered_Outfit_name:
        text hovered_Outfit_name anchor (1.0, 0.5) pos (0.85, 0.258):
            size 46
    else:
        text Girl.Outfit.name anchor (1.0, 0.5) pos (0.85, 0.258):
            size 46

    add f"{Girl.tag}_sprite standing" anchor (Girl.sprite_anchor[0], Girl.sprite_anchor[1]) pos (0.36, eval(f"{Girl.tag}_standing_height")) zoom Girl.sprite_zoom

    imagebutton align (0.5, 0.5):
        idle "images/interface/wardrobe/accessories_idle.webp" hover "images/interface/wardrobe/accessories.webp" selected_idle "images/interface/wardrobe/accessories_selected.webp"
        
        selected current_Wardrobe_screen == "accessory"
        
        action SetVariable("current_Wardrobe_screen", "accessory")

        focus_mask True

        tooltip "Accessories"

    imagebutton align (0.5, 0.5):
        idle "images/interface/wardrobe/head_idle.webp" hover "images/interface/wardrobe/head.webp" selected_idle "images/interface/wardrobe/head_selected.webp"
        
        selected current_Wardrobe_screen == "head"
        
        action SetVariable("current_Wardrobe_screen", "head")

        focus_mask True

        tooltip "Hair"

    imagebutton align (0.5, 0.5):
        idle "images/interface/wardrobe/upper_idle.webp" hover "images/interface/wardrobe/upper.webp" selected_idle "images/interface/wardrobe/upper_selected.webp"
        
        selected current_Wardrobe_screen == "upper"
        
        action SetVariable("current_Wardrobe_screen", "upper")

        focus_mask True

        tooltip "Upper Body"
        
    imagebutton align (0.5, 0.5):
        idle "images/interface/wardrobe/lower_idle.webp" hover "images/interface/wardrobe/lower.webp" selected_idle "images/interface/wardrobe/lower_selected.webp"
        
        selected current_Wardrobe_screen == "lower"
        
        action SetVariable("current_Wardrobe_screen", "lower")

        focus_mask True

        tooltip "Lower Body"

    imagebutton align (0.5, 0.5):
        idle "images/interface/wardrobe/exit_idle.webp" hover "images/interface/wardrobe/exit.webp"
        
        action Call("review_Outfit", Girl, from_current = True)

        focus_mask True

        tooltip "Exit"

    if current_Wardrobe_screen == "accessory":
        use accessory_screen(Girl)
    elif current_Wardrobe_screen == "head":
        use head_screen(Girl)
    elif current_Wardrobe_screen == "upper":
        use upper_screen(Girl)
    elif current_Wardrobe_screen == "lower":
        use lower_screen(Girl)

    hbox anchor (0.5, 0.5) pos (0.715, 0.915):
        spacing 10
                
        imagebutton:
            if Girl.Outfit.disabled:
                idle "images/interface/wardrobe/disabled_idle.webp" hover "images/interface/wardrobe/disabled.webp"

                tooltip "Enable Outfit"
            else:
                idle "images/interface/wardrobe/enabled_idle.webp" hover "images/interface/wardrobe/enabled.webp"

                tooltip "Disable Outfit"
            
            action ToggleField(Girl.Outfit, "disabled")

        if Girl.Outfit.Outfit_type == "custom":
            imagebutton:
                idle "images/interface/wardrobe/rename_idle.webp" hover "images/interface/wardrobe/rename.webp"
                
                action [
                    SetVariable("current_input", Girl.Outfit.name),
                    Show("edit_Outfit_screen", Girl = Girl)]

                tooltip "Rename Outfit"
        else:
            null width 132

        imagebutton:
            idle "images/interface/wardrobe/save_idle.webp" hover "images/interface/wardrobe/save.webp"
            
            action Show("save_Outfit_screen", Girl = Girl)

            tooltip "Save Outfit"
            
        if Girl.Outfit.Outfit_type == "custom":
            imagebutton:
                idle "images/interface/wardrobe/delete_idle.webp" hover "images/interface/wardrobe/delete.webp"
                
                action Show("delete_Outfit_screen", Girl = Girl, name = Girl.Outfit.name)

                tooltip "Delete Outfit"
        else:
            null width 132

    button anchor (1.0, 0.5) pos (0.225, 0.73):
        background None

        hover_sound None
        activate_sound None

        text f"{int(0.25*(Girl.love + Girl.trust))}" align (1.0, 0.5):
            size 36

            color "#000000"

        action NullAction()

        tooltip "Shame Limit for Public Outfits"

    button anchor (1.0, 0.5) pos (0.225, 0.812):
        background None

        hover_sound None
        activate_sound None

        text f"{int(0.4*(Girl.love + Girl.trust))}" align (1.0, 0.5):
            size 36

            color "#000000"

        action NullAction()

        tooltip "Shame Limit for Private Outfits"

    text "CURRENT" anchor (0.0, 0.5) pos (0.066, 0.884):
        size 36

        color "#000000"

    button anchor (1.0, 0.5) pos (0.22, 0.884):
        background None

        hover_sound None
        activate_sound None

        text f"{Girl.Outfit.shame}" align (1.0, 0.5):
            size 36

            color "#000000"

        action NullAction()

        tooltip "Current Outfit Shame"

    if black_screen or renpy.get_screen("say"):
        button align (0.5, 0.5) xysize (config.screen_width, config.screen_height):
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

screen accessory_screen(Girl):
    style_prefix "Wardrobe"

    viewport id "accessory_screen_viewport" anchor (0.5, 0.0) pos (0.71, 0.3) xysize (int(591*2*interface_sampling), int(548*2*interface_sampling)):
        draggable True
        mousewheel True

        xfill True

        vbox align (0.0, 0.0):
            spacing 5

            for i, Item in enumerate(Girl.Wardrobe.Clothes.values()):
                if Item.Clothing_type in accessory_Clothing_types:
                    hbox align (0.5, 0.5):
                        spacing 5

                        fixed xysize (85, 85):
                            if Girl.Clothes[Item.Clothing_type].string == Item.string and Girl.Clothes[Item.Clothing_type].covered or (("swimsuit" in Item.name or "bikini" in Item.name) and Girl.location == "bg_pool"):
                                text f"{Item.shame[0]}" anchor (0.5, 0.5) pos (0.37, 0.5):
                                    size 36

                                    color "#000000"
                            else:
                                text f"{Item.shame[1]}" anchor (0.5, 0.5) pos (0.37, 0.5):
                                    size 36

                                    color "#000000"

                        button xysize (411, 85) xalign 0.5:
                            idle_background "images/interface/wardrobe/clothing_idle.webp" hover_background "images/interface/wardrobe/clothing.webp" selected_background "images/interface/wardrobe/clothing_selected.webp"
                            selected Girl.Clothes[Item.Clothing_type].string == Item.string

                            if Girl.Clothes[Item.Clothing_type].string != Item.string:
                                action Call("ask_Girl_to_try_on", Item, instant = True, from_current = True)
                            else:
                                action Call("ask_Girl_to_take_off", Item, instant = True, from_current = True)

                            text Item.name align (0.5, 0.5) size 36

                        if Girl.Clothes[Item.Clothing_type].string == Item.string and len(Girl.Clothes[Item.Clothing_type].available_states["standing"]) > 1 and not Girl.Clothes[Item.Clothing_type].covered:
                            imagebutton yoffset 1:
                                idle "images/interface/wardrobe/undress_idle.webp" hover "images/interface/wardrobe/undress.webp" selected_idle "images/interface/wardrobe/undress_selected.webp"

                                selected Girl.Clothes[Item.Clothing_type].state != 0

                                if Girl.Clothes[Item.Clothing_type].state == 0:
                                    action Call("ask_Girl_to_undress", Item, instant = True, from_current = True)
                                else:
                                    action Call("ask_Girl_to_redress", Item, instant = True, from_current = True)
                        else:
                            null width 85

            for body_part in ["nipple", "labia"]:
                for piercing_type in ["barbell", "ring"]:
                    if f"{piercing_type}_{body_part}_piercings" in Girl.inventory.keys():
                        hbox align (0.5, 0.5):
                            spacing 5
                            
                            null width 85
                            
                            button xysize (411, 85) xalign 0.5:
                                idle_background "images/interface/wardrobe/clothing_idle.webp" hover_background "images/interface/wardrobe/clothing.webp" selected_background "images/interface/wardrobe/clothing_selected.webp"
                    
                                selected Girl.piercings[body_part] in [piercing_type, "both"]

                                if Girl.piercings[body_part] == piercing_type:
                                    action SetDict(Girl.piercings, body_part, False)
                                elif Girl.piercings[body_part] == "both":
                                    if piercing_type == "barbell":
                                        action SetDict(Girl.piercings, body_part, "ring")
                                    elif piercing_type == "ring":
                                        action SetDict(Girl.piercings, body_part, "barbell")
                                else:
                                    action Call("give_Girl_piercing", Girl, Girl.inventory[f"{piercing_type}_{body_part}_piercings"], from_current = True)

                                text f"{piercing_type} {body_part} piercings" align (0.5, 0.5) size 36
                            
                            null width 85

            if "belly_piercing" in Girl.inventory.keys():
                hbox align (0.5, 0.5):
                    spacing 5
                    
                    null width 85

                    button xysize (411, 85) xalign 0.5:
                        idle_background "images/interface/wardrobe/clothing_idle.webp" hover_background "images/interface/wardrobe/clothing.webp" selected_background "images/interface/wardrobe/clothing_selected.webp"
                    
                        selected Girl.piercings["belly"]

                        if Girl.piercings["belly"]:
                            action SetDict(Girl.piercings, "belly", False)
                        else:
                            action Call("give_Girl_piercing", Girl, Girl.inventory["belly_piercing"], from_current = True)

                        text "belly piercing" align (0.5, 0.5) size 36
                            
                    null width 85

            if "remote_vibrator" in Girl.inventory.keys():
                hbox align (0.5, 0.5):
                    spacing 5
                    
                    null width 85

                    button xysize (411, 85) xalign 0.5:
                        idle_background "images/interface/wardrobe/clothing_idle.webp" hover_background "images/interface/wardrobe/clothing.webp" selected_background "images/interface/wardrobe/clothing_selected.webp"
                    
                        selected Girl.remote_vibrator

                        if Girl.remote_vibrator:
                            action SetField(Girl, "remote_vibrator", None)
                        else:
                            action Call("ask_Girl_to_use_Toy", Girl, Girl.inventory["remote_vibrator"][0], from_current = True)

                        text "remote vibrator" align (0.5, 0.5) size 36
                            
                    null width 85

            for buttplug in ["heart_anal_plug", "round_anal_plug"]:
                if buttplug in Girl.inventory.keys():
                    for plug_size in ["XS", "S", "M", "L"]:
                        hbox align (0.5, 0.5):
                            spacing 5
                            
                            null width 85

                            button xysize (411, 85) xalign 0.5:
                                idle_background "images/interface/wardrobe/clothing_idle.webp" hover_background "images/interface/wardrobe/clothing.webp" selected_background "images/interface/wardrobe/clothing_selected.webp"
                    
                                if plug_size == "XS":
                                    selected Girl.buttplug == Girl.inventory[buttplug][0] and Girl.buttplug_size == 0

                                    if Girl.buttplug == Girl.inventory[buttplug][0] and Girl.buttplug_size == 0:
                                        action [
                                            SetField(Girl, "buttplug", None),
                                            SetField(Girl, "buttplug_size", None)]
                                    else:
                                        action Call("ask_Girl_to_use_Toy", Girl, Girl.inventory[buttplug][0], 0, from_current = True)
                                elif plug_size == "S":
                                    selected Girl.buttplug == Girl.inventory[buttplug][0] and Girl.buttplug_size == 1

                                    if Girl.buttplug == Girl.inventory[buttplug][0] and Girl.buttplug_size == 1:
                                        action [
                                            SetField(Girl, "buttplug", None),
                                            SetField(Girl, "buttplug_size", None)]
                                    else:
                                        action Call("ask_Girl_to_use_Toy", Girl, Girl.inventory[buttplug][0], 1, from_current = True)
                                elif plug_size == "M":
                                    selected Girl.buttplug == Girl.inventory[buttplug][0] and Girl.buttplug_size == 2

                                    if Girl.buttplug == Girl.inventory[buttplug][0] and Girl.buttplug_size == 2:
                                        action [
                                            SetField(Girl, "buttplug", None),
                                            SetField(Girl, "buttplug_size", None)]
                                    else:
                                        action Call("ask_Girl_to_use_Toy", Girl, Girl.inventory[buttplug][0], 2, from_current = True)
                                elif plug_size == "L":
                                    selected Girl.buttplug == Girl.inventory[buttplug][0] and Girl.buttplug_size == 3

                                    if Girl.buttplug == Girl.inventory[buttplug][0] and Girl.buttplug_size == 3:
                                        action [
                                            SetField(Girl, "buttplug", None),
                                            SetField(Girl, "buttplug_size", None)]
                                    else:
                                        action Call("ask_Girl_to_use_Toy", Girl, Girl.inventory[buttplug][0], 3, from_current = True)

                                $ temp = Girl.inventory[buttplug][0].name

                                text f"{temp}, {plug_size}" align (0.5, 0.5) size 36
                                    
                            null width 85

    vbar value YScrollValue("accessory_screen_viewport") anchor (0.5, 0.0) pos (0.875, 0.288) xysize (22, 575):
        base_bar Frame("images/interface/wardrobe/scrollbar.webp")

        thumb "images/interface/wardrobe/scrollbar_thumb.webp"
        thumb_offset 10

        unscrollable "hide"

screen head_screen(Girl):
    style_prefix "Wardrobe"

    viewport id "head_screen_viewport" anchor (0.5, 0.0) pos (0.71, 0.3) xysize (int(591*2*interface_sampling), int(548*2*interface_sampling)):
        draggable True
        mousewheel True

        xfill True

        vbox align (0.0, 0.0):
            spacing 5

            for I in Girl.Wardrobe.Clothes.values():
                if I.Clothing_type == "hair":
                    hbox align (0.5, 0.5):
                        spacing 5

                        null width 85

                        button xysize (411, 85) xalign 0.5:
                            idle_background "images/interface/wardrobe/clothing_idle.webp" hover_background "images/interface/wardrobe/clothing.webp" selected_background "images/interface/wardrobe/clothing_selected.webp"
                    
                            selected Girl.Clothes["hair"].string == I.string

                            if Girl.Clothes["hair"].string != I.string:
                                action Call("ask_Girl_to_try_on", I, instant = True, from_current = True)
                            else:
                                action NullAction()

                            text f"hair: {I.string}" align (0.5, 0.5) size 36

                        null width 85

            if Girl.customizable_pubes:
                for hair_style in ["bush", "growing", "hairy", "null", "shaven", "strip", "triangle"]:
                    hbox align (0.5, 0.5):
                        spacing 5

                        null width 85
                        
                        button xysize (411, 85) xalign 0.5:
                            idle_background "images/interface/wardrobe/clothing_idle.webp" hover_background "images/interface/wardrobe/clothing.webp" selected_background "images/interface/wardrobe/clothing_selected.webp"
                    
                            if hair_style == "shaven":
                                selected Girl.desired_pubes == None
                            else:
                                selected Girl.desired_pubes == hair_style

                            if Girl.desired_pubes == hair_style:
                                action NullAction()
                            else:
                                action [
                                    SetVariable("changed_pubes", True),
                                    Call("ask_Girl_to_shave", Girl, hair_style, from_current = True)]

                            text f"pubic hair: {hair_style}" align (0.5, 0.5) size 36
                        
                        null width 85

            if False:
                $ brows = [
                    "neutral", "cocked", "furrowed", "raised", "wink", "worried"]

                for brow in brows:
                    hbox align (0.5, 0.5):
                        spacing 5

                        null width 85

                        button xysize (411, 85) xalign 0.5:
                            idle_background "images/interface/wardrobe/clothing_idle.webp" hover_background "images/interface/wardrobe/clothing.webp" selected_background "images/interface/wardrobe/clothing_selected.webp"

                            action SetField(Girl, "brows", brow)

                            text f"brows: {brow}" align (0.5, 0.5) size 36

                        null width 85

                $ eyes = [
                    "neutral", "blink1", "blink2", "closed", "down", "left", "right", "sexy", "squint", "up", "wide", "wink"]

                for eye in eyes:
                    hbox align (0.5, 0.5):
                        spacing 5

                        null width 85

                        button xysize (411, 85) xalign 0.5:
                            idle_background "images/interface/wardrobe/clothing_idle.webp" hover_background "images/interface/wardrobe/clothing.webp" selected_background "images/interface/wardrobe/clothing_selected.webp"

                            action SetField(Girl, "eyes", eye)

                            text f"eyes: {eye}" align (0.5, 0.5) size 36

                        null width 85

                if Girl in [Laura]:
                    $ mouths = [
                        "neutral", "agape", "frown", "happy", "kiss", "lipbite", "open", "smile", "smirk", "snarl", "tongue"]
                else:
                    $ mouths = [
                        "neutral", "agape", "frown", "happy", "kiss", "lipbite", "open", "smile", "smirk", "tongue"]

                for mouth in mouths:
                    hbox align (0.5, 0.5):
                        spacing 5

                        null width 85

                        button xysize (411, 85) xalign 0.5:
                            idle_background "images/interface/wardrobe/clothing_idle.webp" hover_background "images/interface/wardrobe/clothing.webp" selected_background "images/interface/wardrobe/clothing_selected.webp"

                            action SetField(Girl, "mouth", mouth)

                            text f"mouth: {mouth}" align (0.5, 0.5) size 36

                        null width 85

                if Girl in [Laura]:
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
                    hbox align (0.5, 0.5):
                        spacing 5

                        null width 85

                        button xysize (411, 85) xalign 0.5:
                            idle_background "images/interface/wardrobe/clothing_idle.webp" hover_background "images/interface/wardrobe/clothing.webp" selected_background "images/interface/wardrobe/clothing_selected.webp"

                            action Function(Girl.change_face, face)

                            text f"face: {face}" align (0.5, 0.5) size 36

                        null width 85

                if Girl in [Rogue]:
                    $ left_arms = [
                        "bra", "crossed", "extended", "fight", "fist", "grope", "hip", "neutral", "rub_neck", "touch_ass"]
                elif Girl in [Laura]:
                    $ left_arms = [
                        "bra", "claws", "crossed", "extended", "fight", "fist", "grope", "hip", "neutral", "rub_neck", "touch_ass", "X"]
                elif Girl in [Jean]:
                    $ left_arms = [
                        "bra", "crossed", "extended", "fight", "fist", "grope", "hip", "neutral", "psychic1", "psychic2", "rub_neck", "touch_ass"]

                for left_arm in left_arms:
                    hbox align (0.5, 0.5):
                        spacing 5

                        null width 85

                        button xysize (411, 85) xalign 0.5:
                            idle_background "images/interface/wardrobe/clothing_idle.webp" hover_background "images/interface/wardrobe/clothing.webp" selected_background "images/interface/wardrobe/clothing_selected.webp"

                            if left_arm == "crossed":
                                action [
                                    SetField(Girl, "left_arm", left_arm),
                                    SetField(Girl, "right_arm", left_arm)]
                            elif Girl.right_arm == "crossed":
                                action [
                                    SetField(Girl, "left_arm", left_arm),
                                    SetField(Girl, "right_arm", "neutral")]
                            else:
                                action SetField(Girl, "left_arm", left_arm)

                            text f"left arm: {left_arm}" align (0.5, 0.5) size 36

                        null width 85

                if Girl in [Rogue]:
                    $ right_arms = [
                        "bra", "crossed", "extended", "fight", "fist", "hip", "neutral", "touch_pussy"]
                elif Girl in [Laura]:
                    $ right_arms = [
                        "bra", "claws", "extended", "fight", "fist", "hip", "neutral", "touch_pussy", "X"]
                elif Girl in [Jean]:
                    $ right_arms = [
                        "bra", "extended", "fight", "fist", "hip", "neutral", "psychic1", "psychic2", "touch_pussy"]

                for right_arm in right_arms:
                    hbox align (0.5, 0.5):
                        spacing 5

                        null width 85

                        button xysize (411, 85) xalign 0.5:
                            idle_background "images/interface/wardrobe/clothing_idle.webp" hover_background "images/interface/wardrobe/clothing.webp" selected_background "images/interface/wardrobe/clothing_selected.webp"

                            if right_arm == "crossed":
                                action [
                                    SetField(Girl, "left_arm", right_arm),
                                    SetField(Girl, "right_arm", right_arm)]
                            elif Girl.left_arm == "crossed":
                                action [
                                    SetField(Girl, "left_arm", "neutral"),
                                    SetField(Girl, "right_arm", right_arm)]
                            else:
                                action SetField(Girl, "right_arm", right_arm)

                            text f"right arm: {right_arm}" align (0.5, 0.5) size 36

                        null width 85

    vbar value YScrollValue("head_screen_viewport") anchor (0.5, 0.0) pos (0.875, 0.288) xysize (22, 575):
        base_bar Frame("images/interface/wardrobe/scrollbar.webp")

        thumb "images/interface/wardrobe/scrollbar_thumb.webp"
        thumb_offset 10

        unscrollable "hide"

screen upper_screen(Girl):
    style_prefix "Wardrobe"

    viewport id "upper_screen_viewport" anchor (0.5, 0.0) pos (0.71, 0.3) xysize (int(591*2*interface_sampling), int(548*2*interface_sampling)):
        draggable True
        mousewheel True

        xfill True

        vbox align (0.0, 0.0):
            spacing 5

            for i, Item in enumerate(Girl.Wardrobe.Clothes.values()):
                if Item.Clothing_type in upper_Clothing_types:
                    hbox align (0.5, 0.5):
                        spacing 5

                        fixed xysize (85, 85):
                            if Girl.Clothes[Item.Clothing_type].string == Item.string and Girl.Clothes[Item.Clothing_type].covered or (("swimsuit" in Item.name or "bikini" in Item.name) and Girl.location == "bg_pool"):
                                text f"{Item.shame[0]}" anchor (0.5, 0.5) pos (0.37, 0.5):
                                    size 36

                                    color "#000000"
                            else:
                                text f"{Item.shame[1]}" anchor (0.5, 0.5) pos (0.37, 0.5):
                                    size 36

                                    color "#000000"

                        button xysize (411, 85) xalign 0.5:
                            idle_background "images/interface/wardrobe/clothing_idle.webp" hover_background "images/interface/wardrobe/clothing.webp" selected_background "images/interface/wardrobe/clothing_selected.webp"
                    
                            selected Girl.Clothes[Item.Clothing_type].string == Item.string

                            if Girl.Clothes[Item.Clothing_type].string != Item.string:
                                action Call("ask_Girl_to_try_on", Item, instant = True, from_current = True)
                            else:
                                action Call("ask_Girl_to_take_off", Item, instant = True, from_current = True)

                            text Item.name align (0.5, 0.5) size 36

                        if Girl.Clothes[Item.Clothing_type].string == Item.string and len(Girl.Clothes[Item.Clothing_type].available_states["standing"]) > 1 and not Girl.Clothes[Item.Clothing_type].covered:
                            imagebutton yoffset 1:
                                idle "images/interface/wardrobe/undress_idle.webp" hover "images/interface/wardrobe/undress.webp" selected_idle "images/interface/wardrobe/undress_selected.webp"
                    
                                selected Girl.Clothes[Item.Clothing_type].state != 0

                                if Girl.Clothes[Item.Clothing_type].state == 0:
                                    action Call("ask_Girl_to_undress", Item, instant = True, from_current = True)
                                else:
                                    action Call("ask_Girl_to_redress", Item, instant = True, from_current = True)
                        else:
                            null width 85

    vbar value YScrollValue("upper_screen_viewport") anchor (0.5, 0.0) pos (0.875, 0.288) xysize (22, 575):
        base_bar Frame("images/interface/wardrobe/scrollbar.webp")

        thumb "images/interface/wardrobe/scrollbar_thumb.webp"
        thumb_offset 10

        unscrollable "hide"

screen lower_screen(Girl):
    style_prefix "Wardrobe"
    
    viewport id "lower_screen_viewport" anchor (0.5, 0.0) pos (0.71, 0.3) xysize (int(591*2*interface_sampling), int(548*2*interface_sampling)):
        draggable True
        mousewheel True

        xfill True

        vbox align (0.0, 0.0):
            spacing 5

            for i, Item in enumerate(Girl.Wardrobe.Clothes.values()):
                if Item.Clothing_type in lower_Clothing_types:
                    hbox align (0.5, 0.5):
                        spacing 5

                        fixed xysize (85, 85):
                            if Girl.Clothes[Item.Clothing_type].string == Item.string and Girl.Clothes[Item.Clothing_type].covered or (("swimsuit" in Item.name or "bikini" in Item.name) and Girl.location == "bg_pool"):
                                text f"{Item.shame[0]}" anchor (0.5, 0.5) pos (0.37, 0.5):
                                    size 36

                                    color "#000000"
                            else:
                                text f"{Item.shame[1]}" anchor (0.5, 0.5) pos (0.37, 0.5):
                                    size 36

                                    color "#000000"

                        button xysize (411, 85) xalign 0.5:
                            idle_background "images/interface/wardrobe/clothing_idle.webp" hover_background "images/interface/wardrobe/clothing.webp" selected_background "images/interface/wardrobe/clothing_selected.webp"
                    
                            selected Girl.Clothes[Item.Clothing_type].string == Item.string

                            if Girl.Clothes[Item.Clothing_type].string != Item.string:
                                action Call("ask_Girl_to_try_on", Item, instant = True, from_current = True)
                            else:
                                action Call("ask_Girl_to_take_off", Item, instant = True, from_current = True)

                            text Item.name align (0.5, 0.5) size 36

                        if Girl.Clothes[Item.Clothing_type].string == Item.string and len(Girl.Clothes[Item.Clothing_type].available_states["standing"]) > 1 and not Girl.Clothes[Item.Clothing_type].covered:
                            imagebutton yoffset 1:
                                idle "images/interface/wardrobe/undress_idle.webp" hover "images/interface/wardrobe/undress.webp" selected_idle "images/interface/wardrobe/undress_selected.webp"

                                selected Girl.Clothes[Item.Clothing_type].state != 0

                                if Girl.Clothes[Item.Clothing_type].state == 0:
                                    action Call("ask_Girl_to_undress", Item, instant = True, from_current = True)
                                else:
                                    action Call("ask_Girl_to_redress", Item, instant = True, from_current = True)
                        else:
                            null width 85

    vbar value YScrollValue("lower_screen_viewport") anchor (0.5, 0.0) pos (0.875, 0.288) xysize (22, 575):
        base_bar Frame("images/interface/wardrobe/scrollbar.webp")

        thumb "images/interface/wardrobe/scrollbar_thumb.webp"
        thumb_offset 10

        unscrollable "hide"

screen save_Outfit_screen(Girl):
    modal True

    style_prefix "Wardrobe"

    on "show" action [
        SetVariable("current_input", ""),
        SetDict(current_flags, "wear_in_public", False),
        SetDict(current_flags, "wear_in_private", False),
        SetDict(current_flags, "datewear", False),
        SetDict(current_flags, "activewear", False),
        SetDict(current_flags, "swimwear", False),
        SetDict(current_flags, "sexwear", False),
        SetDict(current_flags, "sleepwear", False),
        SetDict(current_flags, "winterwear", False)]

    $ Outfit_list = []

    for O in Girl.Wardrobe.Outfits.values():
        if O.Outfit_type == Wardrobe_tab:
            $ Outfit_list.append(O)

    window anchor (0.5, 0.5) pos (0.5, 0.6) xysize (607, 750):
        background "images/interface/wardrobe/save_background.webp"

        text "SAVE OUTFIT AS:" anchor (0.0, 0.0) pos (0.025, 0.0175):
            size 42

            color "#512908"

        input id "input" value VariableInputValue("current_input", default = True) anchor (0.5, 0.5) pos (0.5, 0.14):
            size 50
            color "#000000"
                        
            length 25

        text "OUTFIT COLOR:" anchor (0.0, 0.0) pos (0.025, 0.22):
            size 42

            color "#512908"

        hbox ysize 64 align (0.5, 0.395):
            spacing 15

            for Outfit_color in ["yellow", "pink", "brown", "blue", "green"]:
                imagebutton:
                    selected_background "Wardrobe_selector"

                    selected current_Outfit_color == Outfit_color

                    idle f"images/interface/wardrobe/{Outfit_color}_icon.webp" hover f"images/interface/wardrobe/{Outfit_color}_icon.webp"

                    action SetVariable("current_Outfit_color", Outfit_color)
                    
        text "OUTFIT TYPE:" anchor (0.0, 0.0) pos (0.025, 0.49):
            size 42

            color "#512908"

        hbox ysize 88 align (0.5, 0.65):
            spacing 5

            imagebutton:
                idle "images/interface/wardrobe/public_idle.webp" hover "images/interface/wardrobe/public.webp" selected_idle "images/interface/wardrobe/public_selected.webp" selected_hover "images/interface/wardrobe/public_selected.webp"

                selected current_flags["wear_in_public"]

                action ToggleDict(current_flags, "wear_in_public")

                tooltip "Public"

            imagebutton:
                idle "images/interface/wardrobe/private_idle.webp" hover "images/interface/wardrobe/private.webp" selected_idle "images/interface/wardrobe/private_selected.webp" selected_hover "images/interface/wardrobe/private_selected.webp"

                selected current_flags["wear_in_private"]

                action ToggleDict(current_flags, "wear_in_private")

                tooltip "Private"

        hbox ysize 88 align (0.5, 0.8):
            spacing 5

            for wear_type in ["activewear", "swimwear", "datewear", "sexwear", "sleepwear", "winterwear"]:
                imagebutton:
                    idle f"images/interface/wardrobe/{wear_type}_idle.webp" hover f"images/interface/wardrobe/{wear_type}.webp" selected_idle f"images/interface/wardrobe/{wear_type}_selected.webp" selected_hover f"images/interface/wardrobe/{wear_type}_selected.webp"

                    selected current_flags[wear_type]

                    action ToggleDict(current_flags, wear_type)

                    tooltip wear_type.capitalize()

        imagebutton anchor (1.0, 1.0) pos (0.79, 0.975):
            idle "small_save_idle" hover "small_save"

            if current_input in Girl.Wardrobe.Outfits.keys() and Girl.Wardrobe.Outfits[current_input].Outfit_type == "custom":
                action [
                    Hide("save_Outfit_screen"), 
                    Show("confirm_overwrite_screen", Girl = Girl)]
            elif current_input in Girl.Wardrobe.Outfits.keys() and Girl.Wardrobe.Outfits[current_input].Outfit_type == "default":
                action [
                    Hide("save_Outfit_screen"), 
                    Show("cannot_overwrite_screen", Girl = Girl)]

                tooltip "Save Outfit"
            elif current_input:
                if len(Outfit_list) < 27:
                    action [
                        Hide("save_Outfit_screen"), 
                        Call("save_new_Outfit", Girl, current_input, current_Outfit_color, current_flags, from_current = True)]
                else:
                    action [
                        Hide("save_Outfit_screen"), 
                        Show("cannot_save_screen", Girl = Girl)]

        imagebutton anchor (1.0, 1.0) pos (0.975, 0.975):
            idle "small_delete_idle" hover "small_delete"

            action Hide("save_Outfit_screen")

            tooltip "Cancel"

    if tooltips_enabled:
        use tooltips

screen edit_Outfit_screen(Girl):
    modal True

    style_prefix "Wardrobe"

    on "show" action [
        SetVariable("current_input", Girl.Outfit.name),
        SetDict(current_flags, "wear_in_public", Girl.Outfit.wear_in_public),
        SetDict(current_flags, "wear_in_private", Girl.Outfit.wear_in_private),
        SetDict(current_flags, "activewear", Girl.Outfit.activewear),
        SetDict(current_flags, "superwear", Girl.Outfit.superwear),
        SetDict(current_flags, "swimwear", Girl.Outfit.swimwear),
        SetDict(current_flags, "datewear", Girl.Outfit.datewear),
        SetDict(current_flags, "sexwear", Girl.Outfit.sexwear),
        SetDict(current_flags, "sleepwear", Girl.Outfit.sleepwear),
        SetDict(current_flags, "winterwear", Girl.Outfit.winterwear)]

    window anchor (0.5, 0.5) pos (0.5, 0.6) xysize (607, 750):
        background "images/interface/wardrobe/save_background.webp"
        
        text "SAVE OUTFIT AS:" anchor (0.0, 0.0) pos (0.025, 0.0175):
            size 42

            color "#512908"

        input id "input" value VariableInputValue("current_input", default = True) anchor (0.5, 0.5) pos (0.5, 0.14):
            size 50
            color "#000000"
                        
            length 25

        text "OUTFIT COLOR:" anchor (0.0, 0.0) pos (0.025, 0.22):
            size 42

            color "#512908"

        hbox ysize 64 align (0.5, 0.395):
            spacing 15

            for Outfit_color in ["yellow", "pink", "brown", "blue", "green"]:
                imagebutton:
                    selected_background "Wardrobe_selector"

                    selected current_Outfit_color == Outfit_color

                    idle f"images/interface/wardrobe/{Outfit_color}_icon.webp" hover f"images/interface/wardrobe/{Outfit_color}_icon.webp"

                    action SetVariable("current_Outfit_color", Outfit_color)
                    
        text "OUTFIT TYPE:" anchor (0.0, 0.0) pos (0.025, 0.49):
            size 42

            color "#512908"

        hbox ysize 88 align (0.5, 0.65):
            spacing 5

            imagebutton:
                idle "images/interface/wardrobe/public_idle.webp" hover "images/interface/wardrobe/public.webp" selected_idle "images/interface/wardrobe/public_selected.webp" selected_hover "images/interface/wardrobe/public_selected.webp"

                selected current_flags["wear_in_public"]

                action ToggleDict(current_flags, "wear_in_public")

                tooltip "Public"

            imagebutton:
                idle "images/interface/wardrobe/private_idle.webp" hover "images/interface/wardrobe/private.webp" selected_idle "images/interface/wardrobe/private_selected.webp" selected_hover "images/interface/wardrobe/private_selected.webp"

                selected current_flags["wear_in_private"]

                action ToggleDict(current_flags, "wear_in_private")

                tooltip "Private"

        hbox ysize 88 align (0.5, 0.8):
            spacing 5

            for wear_type in ["activewear", "swimwear", "datewear", "sexwear", "sleepwear", "winterwear"]:
                imagebutton:
                    idle f"images/interface/wardrobe/{wear_type}_idle.webp" hover f"images/interface/wardrobe/{wear_type}.webp" selected_idle f"images/interface/wardrobe/{wear_type}_selected.webp" selected_hover f"images/interface/wardrobe/{wear_type}_selected.webp"

                    selected current_flags[wear_type]

                    action ToggleDict(current_flags, wear_type)

                    tooltip wear_type.capitalize()
                    
        imagebutton anchor (1.0, 1.0) pos (0.79, 0.975):
            idle "small_save_idle" hover "small_save"

            if current_input in Girl.Wardrobe.Outfits.keys() and Girl.Wardrobe.Outfits[current_input].Outfit_type == "custom":
                action [
                    Hide("edit_Outfit_screen"), 
                    Show("confirm_overwrite_screen", Girl = Girl, editing = True)]
            elif current_input in Girl.Wardrobe.Outfits.keys() and Girl.Wardrobe.Outfits[current_input].Outfit_type == "default":
                action [
                    Hide("edit_Outfit_screen"), 
                    Show("cannot_overwrite_screen", Girl = Girl)]
            elif current_input:
                action [
                    Hide("edit_Outfit_screen"), 
                    Call("edit_Outfit", Girl, Girl.Outfit, current_input, current_Outfit_color, current_flags, from_current = True)]

            tooltip "Save Outfit"

        imagebutton anchor (1.0, 1.0) pos (0.98, 0.975):
            idle "small_delete_idle" hover "small_delete"

            action Hide("edit_Outfit_screen")

            tooltip "Cancel"

    if tooltips_enabled:
        use tooltips

screen delete_Outfit_screen(Girl, name):
    modal True

    style_prefix "confirm"

    frame anchor (0.5, 0.5) pos (0.5, 0.75):
        padding (25, 25, 25, 25)

        vbox:
            spacing 25

            text f"Delete outfit?" size 36

            hbox:
                spacing 100

                textbutton _("Yes"):
                    action [
                        Hide("delete_Outfit_screen"),
                        SetField(Girl, "Outfit", Girl.Wardrobe.indoor_Outfit),
                        Function(Girl.Wardrobe.remove_Outfit, name),
                        SetVariable("current_Wardrobe_Outfit_page", 0)] 
                        
                    text_size 36

                textbutton _("No"):
                    action Hide("delete_Outfit_screen") 
                    
                    text_size 36

screen confirm_overwrite_screen(Girl, editing = False):
    modal True

    style_prefix "confirm"

    frame anchor (0.5, 0.5) pos (0.5, 0.5):
        padding (25, 25, 25, 25)

        vbox:
            spacing 25

            text f"Overwrite {current_input}?" xalign 0.5:
                size 40
                
            hbox:
                spacing 100

                textbutton _("Yes") xminimum int(config.screen_width*0.1) yminimum int(config.screen_height*0.07): 
                    text_size 36

                    if editing:
                        action [
                            Hide("confirm_overwrite_screen"),
                            Call("edit_Outfit", Girl, Girl.Outfit, current_input, current_Outfit_color, current_flags, from_current = True)]
                    else:
                        action [
                            Hide("confirm_overwrite_screen"),
                            Call("save_new_Outfit", Girl, current_input, current_Outfit_color, current_flags, from_current = True)]

                textbutton _("No") xminimum int(config.screen_width*0.1) yminimum int(config.screen_height*0.07): 
                    text_size 36

                    action Hide("confirm_overwrite_screen")
                    
screen cannot_overwrite_screen(Girl):
    modal True

    style_prefix "confirm"

    frame anchor (0.5, 0.5) pos (0.5, 0.5):
        padding (25, 25, 25, 25)

        vbox:
            spacing 25

            text f"Cannot overwrite default outfit {current_input}.":
                size 40

            textbutton _("Back") xminimum int(config.screen_width*0.1) yminimum int(config.screen_height*0.07):
                text_size 36

                action [
                    Hide("cannot_overwrite_screen"), 
                    Show("save_Outfit_screen", Girl = Girl)]
                    
screen cannot_save_screen(Girl):
    modal True

    style_prefix "confirm"

    frame anchor (0.5, 0.5) pos (0.5, 0.5):
        padding (25, 25, 25, 25)

        vbox:
            spacing 25

            text f"Wardrobe is full - delete custom outfits to save more.":
                size 40

            textbutton _("Back") xminimum int(config.screen_width*0.1) yminimum int(config.screen_height*0.07):
                text_size 36

                action [
                    Hide("cannot_save_screen"), 
                    Show("save_Outfit_screen", Girl = Girl)]