init -4:

    default quick_location_1 = False
    default quick_location_2 = False
    default quick_location_3 = False
    
    default current_Player_menu_page = "database"

    default current_database_page = 0
    default current_database_filter = "info"
    default current_database_section = "personal"
    default current_database_Entry = None

    default current_mutant_ability = None

    default current_inventory_page = 0
    default current_inventory_filter = "gift"
    default current_inventory_list = []
    default current_inventory_Item = None

    default current_journal_filter = None
    default current_journal_chapter = None
    default current_journal_Quest = None
    default show_completed_Quests = False

    define location_groups = {
        "Institute": {
            "Basement": [
                "bg_danger",
                "bg_lockers"],
            "First Floor": [
                "bg_campus",
                "bg_classroom",
                "bg_entrance",
                "bg_pool",
                "bg_study"],
            "Second Floor": [
                "bg_door",
                "bg_girls_hallway",
                "bg_hallway",
                "bg_Jean",
                "bg_Kurt",
                "bg_Laura",
                "bg_Player",
                "bg_Rogue",
                "bg_Charles"],
            "Attic": [
                "bg_Ororo"]},

        "Mall": {
            "First Floor": [
                "bg_mall",
                "bg_movies"]},

        # "Town": {
        #     "Main Street": [
        #         "bg_town"]}
        }

    default current_group = "Institute"
    default current_subgroup = "Second Floor"
    
    default unlocked_locations = {
        "bg_Player": "renpy.call('travel', 'bg_Player')"}
        
    default available_locations = {}

    default marked_locations = {
        "bg_campus": [],
        "bg_classroom": [],
        "bg_danger": [],
        "bg_entrance": [],
        "bg_girls_hallway": [],
        "bg_hallway": [],
        "bg_Jean": [],
        "bg_Kurt": [],
        "bg_Laura": [],
        "bg_mall": [],
        "bg_movies": [],
        "bg_Player": [],
        "bg_pool": [],
        "bg_Rogue": [],
        "bg_lockers": [],
        "bg_study": [],
        "bg_Charles": [],
        "bg_Ororo": []}

init -1 python:

    import math

    def return_last_name(Character):
        return Character.full_name.split(" ")[-1]

style Player_menu is default

screen Player_menu():
    layer "interface"

    modal True

    style_prefix "Player_menu"

    on "show" action [
        Hide("say"),
        Hide("phone_screen"),
        SetVariable("current_inventory_filter", "gift"),
        SetVariable("choice_disabled", True),
        Function(EventScheduler.update_conditions)]
    on "hide" action [
        SetVariable("giving_gift", False),
        SetVariable("current_inventory_Item", None),
        SetVariable("choice_disabled", False)]

    timer 0.5 repeat True action ToggleVariable("blinking")

    if not black_screen and not renpy.get_screen("say"):
        add "images/interface/main_menu/blank_background.webp" zoom interface_adjustment

        add At("images/interface/preferences/spin.webp", spinning_element) anchor (0.5, 0.5) pos (0.502, 0.502) zoom interface_adjustment

        add "images/interface/Player_menu/top.webp" zoom interface_adjustment

        for page in ["database", "skills", "inventory", "journal", "map"]:
            button:
                idle_background At(f"images/interface/Player_menu/{page}_idle.webp", interface)
                hover_background At(f"images/interface/Player_menu/{page}.webp", interface)
                selected_idle_background At(f"images/interface/Player_menu/{page}.webp", interface)
                selected_hover_background At(f"images/interface/Player_menu/{page}.webp", interface)

                selected current_Player_menu_page == page

                action SetVariable("current_Player_menu_page", page)

                focus_mask True

        text "DATABASE" anchor (0.5, 0.5) pos (0.147, 0.064):
            size 55

        text "SKILLS" anchor (0.5, 0.5) pos (0.28, 0.064):
            size 50

        text "INVENTORY" anchor (0.5, 0.5) pos (0.425, 0.064):
            size 55

        text "JOURNAL" anchor (0.5, 0.5) pos (0.586, 0.064):
            size 55

        text "MAP" anchor (0.5, 0.5) pos (0.711, 0.064):
            size 55

        imagebutton:
            idle At("images/interface/Player_menu/preferences_idle.webp", interface)
            hover At("images/interface/Player_menu/preferences.webp", interface)

            action ShowMenu("preferences")

        imagebutton:
            idle At("images/interface/Player_menu/exit_idle.webp", interface)
            hover At("images/interface/Player_menu/exit.webp", interface)

            if not sandbox:
                action [
                    Hide("Player_menu"),
                    Return()]
            else:
                action Hide("Player_menu")

        if current_Player_menu_page == "database":
            use database_screen
        elif current_Player_menu_page == "skills":
            use skills_screen
        elif current_Player_menu_page == "inventory":
            use inventory_screen
        elif current_Player_menu_page == "journal":
            use journal_screen
        elif current_Player_menu_page == "map":
            use map_screen

    if black_screen or renpy.get_screen("say"):
        button xysize (1.0, 1.0):
            background None
            
            if not renpy.get_screen("choice"):
                action Return()
            else:
                action NullAction()

    use quick_menu

screen database_screen():
    style_prefix "Player_menu"

    $ database_Entries = []

    $ database_Characters = unlocked_Characters[:]
    $ database_Characters.sort(key = return_last_name)
    $ database_Characters.insert(0, Player)

    for C in database_Characters:
        $ database_Entries.append(C)

    add "images/interface/Player_menu/database_background.webp" zoom interface_adjustment

    for filter in ["enemy", "info", "ally"]:
        imagebutton:
            idle At(f"images/interface/Player_menu/database_filter_{filter}_idle.webp", interface)
            hover At(f"images/interface/Player_menu/database_filter_{filter}.webp", interface)
            selected_idle At(f"images/interface/Player_menu/database_filter_{filter}_selected.webp", interface)
            selected_hover At(f"images/interface/Player_menu/database_filter_{filter}_selected.webp", interface)

            selected current_database_filter == filter

            if current_database_filter == filter:
                action SetVariable("current_database_filter", None)
            else:
                action [
                    SetVariable("current_database_filter", None),
                    SetVariable("current_database_filter", filter)]

    text "ENEMY" anchor (0.5, 0.5) pos (0.096, 0.244):
        size 35

        color "#000000"

    text "INFO" anchor (0.5, 0.5) pos (0.19, 0.244):
        size 35

        color "#000000"

    text "ALLY" anchor (0.5, 0.5) pos (0.283, 0.244):
        size 35

        color "#000000"

    # if blinking:
    text "CEREBRO DATABASE" + "{alpha=0.0}_{/alpha}" anchor (0.0, 0.5) pos (0.065, 0.335):
        size 35
    # else:
    #     text "CEREBRO DATABASE" + "_" anchor (0.0, 0.5) pos (0.065, 0.335):
    #         size 35

    viewport id "database_viewport" anchor (0.5, 0.0) pos (0.176, 0.405) xysize (int(911*interface_adjustment), int(1114*interface_adjustment)):
        draggable True
        mousewheel True

        vbox:
            for D in database_Entries:
                if hasattr(D, "database_type") and D.database_type and D.database_type and (not current_database_filter or D.database_type == current_database_filter):
                    button xysize (int(911*interface_adjustment), int(191*interface_adjustment)):
                        idle_background At(f"images/interface/Player_menu/database_{D.database_type}_idle.webp", interface)
                        hover_background At(f"images/interface/Player_menu/database_{D.database_type}.webp", interface)
                        selected_idle_background At(f"images/interface/Player_menu/database_{D.database_type}.webp", interface)
                        
                        selected current_database_Entry == D

                        if D in all_Characters or current_database_Entry == Player:
                            text D.call_sign anchor (0.0, 0.5) pos (0.1, 0.5):
                                font "agency_fb.ttf"

                                size 36

                                color "#000000"

                        action SetVariable("current_database_Entry", D)

    vbar value YScrollValue("database_viewport") anchor (0.5, 0.0) pos (0.315, 0.405) xysize (int(40*interface_adjustment), int(1114*interface_adjustment)):
        base_bar At("images/interface/Player_menu/database_scrollbar.webp", interface)

        thumb At("images/interface/Player_menu/database_scrollbar_thumb.webp", interface)
        thumb_offset int(276*interface_adjustment/2/10)

        unscrollable "hide"

    if current_database_Entry:
        add "images/interface/Player_menu/database_profile.webp" zoom interface_adjustment

        if current_database_section in ["personal", "mutiefan"]:
            add "images/interface/Player_menu/database_profile_box.webp" zoom interface_adjustment
        
        if current_database_Entry in all_Characters or current_database_Entry == Player:
            $ Entry_name = current_database_Entry.call_sign
        else:
            $ Entry_name = current_database_Entry.title

        if blinking:
            text Entry_name.upper() + "{alpha=0.0}_{/alpha}" anchor (0.0, 0.5) pos (0.364, 0.247):
                size 35
        else:
            text Entry_name.upper() + "_" anchor (0.0, 0.5) pos (0.364, 0.247):
                size 35

        for section in ["personal", "combat", "mutiefan"]:
            imagebutton:
                idle At(f"images/interface/Player_menu/database_{section}_idle.webp", interface)
                hover At(f"images/interface/Player_menu/database_{section}.webp", interface)
                selected_idle At(f"images/interface/Player_menu/database_{section}.webp", interface)

                selected current_database_section == section

                if current_database_section == section:
                    action NullAction()
                else:
                    action [
                        SetVariable("current_database_section", None),
                        SetVariable("current_database_section", section)]

        text "PERSONAL" anchor (0.5, 0.5) pos (0.693, 0.247):
            size 35

        text "COMBAT" anchor (0.5, 0.5) pos (0.79, 0.247):
            size 35

        $ database_length = 0

        if "description" in current_database_Entry.database.keys() and current_database_section == "personal":
            $ database_length += len(current_database_Entry.database["description"])

        if "wiki" in current_database_Entry.database.keys() and current_database_section == "mutiefan":
            $ database_length += 1

        if database_length > 1:
            imagebutton:
                idle At("images/interface/Player_menu/database_left_idle.webp", interface)
                hover At("images/interface/Player_menu/database_left.webp", interface)

                action SetVariable("current_database_page", (current_database_page - 1) % database_length)

            text f"{current_database_page + 1} / {database_length}" anchor (0.5, 0.5) pos (0.777, 0.875):
                size 36

            imagebutton:
                idle At("images/interface/Player_menu/database_right_idle.webp", interface)
                hover At("images/interface/Player_menu/database_right.webp", interface)

                action SetVariable("current_database_page", (current_database_page + 1) % database_length)
        
        if database_length >= 1:
            if current_database_section == "personal" and current_database_page < len(current_database_Entry.database["description"]):
                if current_database_Entry in all_Characters or current_database_Entry == Player:
                    frame anchor (0.0, 0.0) pos (0.375, 0.345) xysize (0.543, 0.55):
                        frame align (0.0, 0.0) xsize 0.4:
                            text current_database_Entry.database["stats"] xalign 0.0:
                                font "agency_fb.ttf"
                                        
                                size 24

                                text_align 0.0

                        frame align (0.0, 1.0) xsize 0.4:
                            text current_database_Entry.database["study_materials"] xalign 0.0:
                                font "agency_fb.ttf"

                                size 28

                                text_align 0.0

                        frame align (1.0, 0.0) xsize 0.58:
                            text current_database_Entry.database["description"][current_database_page] xalign 1.0:
                                font "agency_fb.ttf"

                                if len(current_database_Entry.database["description"][current_database_page]) < 800:
                                    size 30
                                elif len(current_database_Entry.database["description"][current_database_page]) < 1500:
                                    size 24
                                else:
                                    size 20

                                text_align 1.0
            elif current_database_section == "mutiefan" and "wiki" in current_database_Entry.database.keys():
                frame anchor (0.0, 0.0) pos (0.375, 0.345) xysize (0.543, 0.55):
                    text current_database_Entry.database["wiki"] align (0.0, 0.0):
                        font "agency_fb.ttf"

                        size 36

                        text_align 0.0

                    frame align (0.0, 1.0) xsize 0.4:
                        vbox xsize 1.0:
                            for comment in current_database_Entry.database["comments"]:
                                text comment xalign 0.0:
                                    font "agency_fb.ttf"

                                    size 24

                                    text_align 0.0

screen skills_screen():
    style_prefix "Player_menu"

    add "images/interface/Player_menu/skills_background.webp" zoom interface_adjustment

    if blinking:
        text "X-EVOLUTION" + "{alpha=0.0}_{/alpha}" anchor (0.0, 0.5) pos (0.066, 0.238):
            size 35
    else:
        text "X-EVOLUTION" + "_" anchor (0.0, 0.5) pos (0.066, 0.238):
            size 35

    add At("Player_portrait", customization_portrait) pos (0.738, 0.459)

    add f"images/interface/Player_menu/skills_{Player.scholarship}.webp" zoom interface_adjustment

    if Player.scholarship == "athletic":
        text "ATHLETICS" anchor (0.5, 0.5) pos (0.89, 0.352):
            font "agency_fb.ttf"

            size 30
    elif Player.scholarship == "academic":
        text "ACADEMICS" anchor (0.5, 0.5) pos (0.89, 0.352):
            font "agency_fb.ttf"

            size 30
    elif Player.scholarship == "artistic":
        text "ARTS" anchor (0.5, 0.5) pos (0.89, 0.352):
            font "agency_fb.ttf"

            size 30

    text "LVL" anchor (0.0, 0.5) pos (0.818, 0.421):
        font "agency_fb.ttf"

        size 30

    text f"{Player.level}" anchor (1.0, 0.5) pos (0.87, 0.421):
        font "agency_fb.ttf"
        
        size 30

    text f"{Player.ability_points}" anchor (0.5, 0.5) pos (0.898, 0.421):
        font "agency_fb.ttf"
        
        size 30

    text "XP" anchor (0.0, 0.5) pos (0.818, 0.465):
        font "agency_fb.ttf"
        
        size 30

    bar value Player.XP range Player.XP_goal anchor (0.5, 0.5) pos (0.878, 0.465) xysize (int(277*interface_adjustment), int(24*interface_adjustment)):
        left_bar At("images/interface/Player_menu/skills_xp.webp", interface)
        right_bar At("images/interface/Player_menu/skills_xp_empty.webp", interface)

        thumb None
        thumb_offset 0

    text "MUTANT RANK" anchor (0.0, 0.5) pos (0.818, 0.513):
        font "agency_fb.ttf"
        
        size 25

    text Player.mutant_rank.upper() anchor (1.0, 0.5) pos (0.921, 0.513):
        font "agency_fb.ttf"
        
        size 25

    $ mutant_abilities = [
        "nullify",
        "stamina_boost1", 
        "stamina_boost2", 
        "stamina_boost3",
        "orgasm_control"]

    if "regen" in Player.mutant_abilities:
        $ mutant_abilities.append("regen")

    for ability in mutant_abilities:
        if ability == "nullify":
            $ x = 0.11
            $ y = 0.4
        elif ability == "regen":
            $ x = 0.149
            $ y = 0.36
        elif ability == "stamina_boost1":
            $ x = 0.11
            $ y = 0.6
        elif ability == "stamina_boost2":
            $ x = 0.149
            $ y = 0.56
        elif ability == "stamina_boost3":
            $ x = 0.188
            $ y = 0.6
        elif ability == "orgasm_control":
            $ x = 0.11
            $ y = 0.8

        button anchor (0.5, 0.5) pos (x, y) xysize (int(209*interface_adjustment), int(193*interface_adjustment)):
            if ability in Player.mutant_abilities:
                idle_background At("images/interface/Player_menu/skills_node_purchased.webp", interface)
                hover_background At("images/interface/Player_menu/skills_node_selected.webp", interface)
                selected_idle_background At("images/interface/Player_menu/skills_node_selected.webp", interface)
            else:
                idle_background At("images/interface/Player_menu/skills_node_idle.webp", interface)
                hover_background At("images/interface/Player_menu/skills_node.webp", interface)
                selected_idle_background At("images/interface/Player_menu/skills_node.webp", interface)

            selected current_mutant_ability == ability

            if "stamina" in ability:
                add "images/interface/Player_menu/skills_stamina.webp" anchor (0.5, 0.5) pos (0.48, 0.47) zoom interface_adjustment
            else:
                add f"images/interface/Player_menu/skills_{ability}.webp" anchor (0.5, 0.5) pos (0.48, 0.47) zoom interface_adjustment

            action SetVariable("current_mutant_ability", ability)

    if current_mutant_ability:
        add "images/interface/Player_menu/skills_box.webp" zoom interface_adjustment

        text ability_names[current_mutant_ability].upper() anchor (0.0, 0.5) pos (0.679, 0.68):
            size 30

        frame anchor (0.5, 0.5) pos (0.801, 0.805) xysize (0.245, 0.202):
            text ability_descriptions[current_mutant_ability] xalign 0.5:
                font "agency_fb.ttf"
                
                size 30

                text_align 0.5

        if current_mutant_ability not in Player.mutant_abilities and current_mutant_ability in ability_costs.keys() and Player.ability_points >= ability_costs[current_mutant_ability]:
            imagebutton:
                idle At("images/interface/Player_menu/skills_purchase.webp", interface)
                hover At("images/interface/Player_menu/skills_purchased.webp", interface)

                if "stamina" in current_mutant_ability:
                    action [
                        SetVariable("Player.ability_points", Player.ability_points - ability_costs[current_mutant_ability]),
                        AddToSet(Player.mutant_abilities, current_mutant_ability),
                        SetVariable("Player.max_stamina", Player.max_stamina + 1)]
                else:
                    action [
                        SetVariable("Player.ability_points", Player.ability_points - ability_costs[current_mutant_ability]),
                        AddToSet(Player.mutant_abilities, current_mutant_ability)]

            text "AWAKEN" anchor (0.5, 0.5) pos (0.825, 0.68):
                font "agency_fb.ttf"
                
                size 25
        elif current_mutant_ability not in Player.mutant_abilities:
            add "images/interface/Player_menu/skills_purchase.webp" zoom interface_adjustment

            text "AWAKEN" anchor (0.5, 0.5) pos (0.825, 0.68):
                font "agency_fb.ttf"
                
                size 25
        else:
            add "images/interface/Player_menu/skills_purchased.webp" zoom interface_adjustment

            text "ACTIVE" anchor (0.5, 0.5) pos (0.825, 0.68):
                font "agency_fb.ttf"
                
                size 25

        text "COST" anchor (0.0, 0.5) pos (0.8725, 0.68):
            font "agency_fb.ttf"
            
            size 24

        if current_mutant_ability not in Player.mutant_abilities and current_mutant_ability in ability_costs.keys():
            text f"{ability_costs[current_mutant_ability]}" anchor (1.0, 0.5) pos (0.902, 0.68):
                font "agency_fb.ttf"
                
                size 24
        else:
            text "0" anchor (1.0, 0.5) pos (0.902, 0.68):
                font "agency_fb.ttf"
                
                size 24

screen inventory_screen():
    style_prefix "Player_menu"

    $ current_inventory_list = []
    
    for Item_string in Player.inventory.keys():
        if current_inventory_filter == "gift" and not isinstance(Player.inventory[Item_string], list):
            $ current_inventory_list.append(Item_string)

        if isinstance(Player.inventory[Item_string], list):
            for I in Player.inventory[Item_string]:
                if current_inventory_filter in I.filter_type:
                    if Item_string not in current_inventory_list:
                        if I.Owner == Player and current_inventory_filter == "key":
                            $ current_inventory_list.append(Item_string)
                        elif I.Owner != Player and current_inventory_filter == "gift":
                            $ current_inventory_list.append(Item_string)

    add "images/interface/Player_menu/inventory_background.webp" zoom interface_adjustment

    if math.floor(len(current_inventory_list)/15) > 0:
        imagebutton:
            idle At("images/interface/Player_menu/inventory_left_idle.webp", interface)
            hover At("images/interface/Player_menu/inventory_left.webp", interface)

            action SetVariable("current_inventory_page", (current_inventory_page - 1) % math.ceil(len(current_inventory_list)/15))

    if math.floor(len(current_inventory_list)/15) > 0:
        imagebutton:
            idle At("images/interface/Player_menu/inventory_right_idle.webp", interface)
            hover At("images/interface/Player_menu/inventory_right.webp", interface)

            action SetVariable("current_inventory_page", (current_inventory_page + 1) % math.ceil(len(current_inventory_list)/15))

    if current_inventory_page < 9:
        if blinking:
            text "TAB{alpha=0.0}_{/alpha}" + f"0{current_inventory_page + 1}" anchor (0.5, 0.5) pos (0.086, 0.808):
                size 35
        else:
            text f"TAB_0{current_inventory_page + 1}" anchor (0.5, 0.5) pos (0.086, 0.808):
                size 35
    else:
        if blinking:
            text "TAB{alpha=0.0}_{/alpha}" + f"{current_inventory_page + 1}" anchor (0.5, 0.5) pos (0.086, 0.808):
                size 35
        else:
            text f"TAB_{current_inventory_page + 1}" anchor (0.5, 0.5) pos (0.086, 0.808):
                size 35

    grid 5 3 anchor (0.0, 0.0) pos (0.146, 0.4) xysize (0.492, 0.524):
        xspacing 15
        yspacing 16

        for i in range(15*current_inventory_page, min(15*(current_inventory_page + 1), len(current_inventory_list))):
            $ Item_string = current_inventory_list[i]
            
            if isinstance(Player.inventory[Item_string], list):
                $ Item = None

                for I in Player.inventory[Item_string]:
                    if not Item:
                        if I.Owner == Player and current_inventory_filter == "key":
                            $ Item = I
                        elif I.Owner != Player and current_inventory_filter == "gift":
                            $ Item = I

                if giving_gift and Item.Owner == Player:
                    continue
                    
                button xysize (int(355*interface_adjustment), int(355*interface_adjustment)):
                    if current_inventory_Item == Item_string:
                        background At("images/interface/Player_menu/inventory_selector.webp", interface)
                    else:
                        background None

                    hover_sound None

                    if "piercing" in Item_string:
                        add "images/interface/items/xtreme_intimates.webp" anchor (0.5, 0.5) pos (0.5, 0.5) zoom 0.4
                    else:
                        add f"images/interface/items/{Item_string}.webp" anchor (0.5, 0.5) pos (0.5, 0.5) zoom item_adjustment

                    text f"x{len(Player.inventory[Item_string])}" anchor (1.0, 1.0) pos (1.05, 1.0):
                        size 32

                    if giving_gift:
                        action [
                            SetVariable("current_inventory_Item", Item_string),
                            Show("confirm_gift_screen", Character = focused_Character, Item = Item)]
                    else:
                        action SetVariable("current_inventory_Item", Item_string)
            else:
                $ Clothing = Player.inventory[Item_string]
                
                button xysize (int(355*interface_adjustment), int(355*interface_adjustment)):
                    if current_inventory_Item == Clothing:
                        background At("images/interface/Player_menu/inventory_selector.webp", interface)
                    else:
                        background None

                    hover_sound None

                    if Clothing.shop_type == "clothing":
                        add "images/interface/items/mutant_couture.webp" anchor (0.5, 0.5) pos (0.5, 0.5) zoom 0.4
                    elif Clothing.shop_type == "lingerie":
                        add "images/interface/items/xtreme_intimates.webp" anchor (0.5, 0.5) pos (0.5, 0.5) zoom 0.4

                    add At(f"images/interface/phone/icons/{Clothing.Owner.tag}.webp", humhum_icon) anchor (0.5, 0.5) pos (0.93, 0.89)

                    if giving_gift and focused_Character == Clothing.Owner:
                        action [
                            SetVariable("current_inventory_Item", Clothing),
                            Show("confirm_gift_screen", Character = focused_Character, Item = Clothing)]
                    else:
                        action SetVariable("current_inventory_Item", Clothing)

    for filter in ["gift", "key"]:
        imagebutton:
            idle At(f"images/interface/Player_menu/inventory_{filter}_idle.webp", interface)
            hover At(f"images/interface/Player_menu/inventory_{filter}.webp", interface) 
            selected_idle At(f"images/interface/Player_menu/inventory_{filter}.webp", interface)

            selected current_inventory_filter == filter

            action [
                SetVariable("current_inventory_Item", None),
                SetVariable("current_inventory_filter", filter)]

    text "GIFT" anchor (0.5, 0.5) pos (0.51, 0.335):
        size 35

    text "KEY" anchor (0.5, 0.5) pos (0.602, 0.335):
        size 35

    # if blinking:
    text "ITEM NAME" + "{alpha=0.0}_{/alpha}" anchor (0.0, 0.5) pos (0.674, 0.335):
        size 35
    # else:
    #     text "ITEM NAME" + "_" anchor (0.0, 0.5) pos (0.674, 0.335):
    #         size 35

    if isinstance(current_inventory_Item, str):
        $ Item = eval(f"{current_inventory_Item}(None)")

        text f"{Item.name.upper()}" anchor (1.0, 0.5) pos (0.93, 0.335):
            if len(Item.name) > 20:
                size 25
            elif len(Item.name) > 15:
                size 30
            else:
                size 35

        text f"{Item.description}" anchor (0.5, 0.5) pos (0.8, 0.608) xysize (0.25, 0.44):
            size 40
    elif current_inventory_Item:
        text f"{current_inventory_Item.name.upper()}" anchor (1.0, 0.5) pos (0.93, 0.335):
            if len(current_inventory_Item.name) > 20:
                size 25
            elif len(current_inventory_Item.name) > 15:
                size 30
            else:
                size 35

    # if blinking:
    text "CASH" + "{alpha=0.0}_{/alpha}" anchor (0.0, 0.5) pos (0.674, 0.907):
        size 45
    # else:
    #     text "CASH" + "_" anchor (0.0, 0.5) pos (0.674, 0.907):
    #         size 45

    text f"$ {Player.cash}" anchor (1.0, 0.5) pos (0.93, 0.907):
        size 45

screen confirm_gift_screen(Character, Item):
    modal True

    style_prefix "confirm"

    frame anchor (0.5, 0.5) pos (0.5, 0.5):
        vbox:
            spacing 25

            text f"Give {Character.name} the {Item.name}?":
                size 40
                
            hbox:
                spacing 100

                textbutton _("Yes"): 
                    text_size 36

                    if "piercing" in Item.string:
                        action [
                            Hide("confirm_gift_screen"),
                            Call("give_Character_piercing", Character, Item, from_current = True)]
                    elif hasattr(Item, "available_states"):
                        action [
                            Hide("confirm_gift_screen"),
                            Call("give_Character_Clothing", Character, Item, from_current = True)]
                    else:
                        action [
                            Hide("confirm_gift_screen"),
                            Call("give_Character_gift", Character, Item, from_current = True)]

                textbutton _("No"): 
                    text_size 36

                    action Hide("confirm_gift_screen")

screen journal_screen():
    style_prefix "Player_menu"

    add "images/interface/Player_menu/journal_background.webp" zoom interface_adjustment

    for filter in ["main", "side", "addon"]:
        imagebutton:
            idle At(f"images/interface/Player_menu/journal_{filter}_idle.webp", interface)
            hover At(f"images/interface/Player_menu/journal_{filter}.webp", interface)
            selected_idle At(f"images/interface/Player_menu/journal_{filter}_selected.webp", interface)
            selected_hover At(f"images/interface/Player_menu/journal_{filter}_selected.webp", interface)

            selected current_journal_filter == filter

            if current_journal_filter == filter:
                action SetVariable("current_journal_filter", None)
            else:
                action [
                    SetVariable("current_journal_Quest", None),
                    SetVariable("current_journal_filter", filter)]

    text "MAIN" anchor (0.5, 0.5) pos (0.096, 0.244):
        size 35

        color "#000000"

    text "SIDE" anchor (0.5, 0.5) pos (0.19, 0.244):
        size 35

        color "#000000"

    text "ADD-ON" anchor (0.5, 0.5) pos (0.283, 0.244):
        size 35

        color "#000000"

    for c in range(1, chapter + 1):
        imagebutton:
            idle At(f"images/interface/Player_menu/journal_chapter{c}_idle.webp", interface)
            hover At(f"images/interface/Player_menu/journal_chapter{c}.webp", interface)
            selected_idle At(f"images/interface/Player_menu/journal_chapter{c}.webp", interface)

            selected current_journal_chapter == c

            if current_journal_chapter == c:
                action SetVariable("current_journal_chapter", None)
            else:
                action [
                    SetVariable("current_journal_Quest", None),
                    SetVariable("current_journal_chapter", c)]

    text "CHAPTER I" anchor (0.5, 0.5) pos (0.395, 0.242):
        size 35

    # if blinking:
    text "QUEST LIST" + "{alpha=0.0}_{/alpha}" anchor (0.0, 0.5) pos (0.065, 0.335):
        size 35
    # else:
    #     text "QUEST LIST" + "_" anchor (0.0, 0.5) pos (0.065, 0.335):
    #         size 35

    viewport id "journal_viewport" anchor (0.5, 0.0) pos (0.176, 0.405) xysize (int(911*interface_adjustment), int(1114*interface_adjustment)):
        draggable True
        mousewheel True

        vbox:
            for Q in reversed(QuestPool.Quests.values()):
                if Q.unlocked and (not current_journal_filter or Q.Quest_type == current_journal_filter) and (not current_journal_chapter or Q.chapter == current_journal_chapter):
                    if show_completed_Quests or not Q.completed:
                        button xysize (int(911*interface_adjustment), int(191*interface_adjustment)):
                            idle_background At(f"images/interface/Player_menu/journal_button_{Q.Quest_type}_idle.webp", interface)
                            hover_background At(f"images/interface/Player_menu/journal_button_{Q.Quest_type}.webp", interface)
                            selected_idle_background At(f"images/interface/Player_menu/journal_button_{Q.Quest_type}.webp", interface)
                            
                            selected current_journal_Quest == Q

                            text Q.name anchor (0.0, 0.5) pos (0.1, 0.5):
                                font "agency_fb.ttf"

                                size 36

                                color "#000000"

                            if Q.completed:
                                add At("images/interface/Player_menu/journal_clear.webp", interface) anchor (0.5, 0.5) pos (0.5, 0.49)

                            action SetVariable("current_journal_Quest", Q)

    vbar value YScrollValue("journal_viewport") anchor (0.5, 0.0) pos (0.315, 0.405) xysize (int(40*interface_adjustment), int(1114*interface_adjustment)):
        base_bar At("images/interface/Player_menu/journal_scrollbar.webp", interface)

        thumb At("images/interface/Player_menu/journal_scrollbar_thumb.webp", interface)
        thumb_offset int(276*interface_adjustment/2/10)

        unscrollable "hide"

    if current_journal_Quest:
        add "images/interface/Player_menu/journal_quest_box.webp" zoom interface_adjustment

        if current_journal_Quest.completed:
            add At("images/interface/Player_menu/journal_complete.webp", interface)
        else:
            add At("images/interface/Player_menu/journal_pending.webp", interface)

        if blinking:
            text "SUMMARY" + "{alpha=0.0}_{/alpha}" anchor (0.0, 0.5) pos (0.364, 0.335):
                size 35
        else:
            text "SUMMARY" + "_" anchor (0.0, 0.5) pos (0.364, 0.335):
                size 35

        text current_journal_Quest.description anchor (0.5, 0.0) pos (0.635, 0.402):
            if len(current_journal_Quest.description) >= 25:
                size 32
            else:
                size 36

        text "OBJECTIVES" anchor (0.0, 0.0) pos (0.364, 0.4):
            size 35

        vbox anchor (0.5, 0.0) pos (0.635, 0.48):
            spacing 5

            for objective in current_journal_Quest.objectives.keys():
                if current_journal_Quest.objectives[objective][1]:
                    $ progress = eval(current_journal_Quest.objectives[objective][0])
                    $ target = current_journal_Quest.objectives[objective][1]

                    $ objective = renpy.substitute(objective)

                    if current_journal_Quest.completed or progress > target:
                        $ progress = target

                    if progress == target:
                        text "{s}[objective]: [progress]/[target]{/s}" anchor (0.5, 0.5) pos (0.5, 0.5):
                            font "agency_fb.ttf"

                            size 32
                    else:
                        text "[objective]: [progress]/[target]" anchor (0.5, 0.5) pos (0.5, 0.5):
                            font "agency_fb.ttf"

                            size 32
                else:
                    if eval(current_journal_Quest.objectives[objective][0]):
                        $ objective = renpy.substitute(objective)

                        text "{s}[objective]{/s}" anchor (0.5, 0.5) pos (0.5, 0.5):
                            font "agency_fb.ttf"

                            size 32
                    else:
                        $ objective = renpy.substitute(objective)

                        text "[objective]" anchor (0.5, 0.5) pos (0.5, 0.5):
                            font "agency_fb.ttf"

                            size 32

            for optional_objective in current_journal_Quest.optional_objectives.keys():
                if current_journal_Quest.optional_objectives[optional_objective][1]:
                    $ progress = eval(current_journal_Quest.optional_objectives[optional_objective][0])
                    $ target = current_journal_Quest.optional_objectives[optional_objective][1]

                    $ optional_objective = renpy.substitute(optional_objective)

                    if current_journal_Quest.completed or progress > target:
                        $ progress = target

                    if progress == target:
                        text "{s}{i}[optional_objective]: [progress]/[target]{/i}{/s}" anchor (0.5, 0.5) pos (0.5, 0.5):
                            font "agency_fb.ttf"

                            size 32
                    else:
                        text "{i}[optional_objective]: [progress]/[target]{/i}" anchor (0.5, 0.5) pos (0.5, 0.5):
                            font "agency_fb.ttf"

                            size 32
                else:
                    if eval(current_journal_Quest.optional_objectives[optional_objective][0]):
                        $ optional_objective = renpy.substitute(optional_objective)

                        text "{s}{i}[optional_objective]{/i}{/s}" anchor (0.5, 0.5) pos (0.5, 0.5):
                            font "agency_fb.ttf"

                            size 32
                    else:
                        $ optional_objective = renpy.substitute(optional_objective)

                        text "{i}[optional_objective]{/i}" anchor (0.5, 0.5) pos (0.5, 0.5):
                            font "agency_fb.ttf"

                            size 32

        if current_journal_Quest.rewards:
            hbox anchor (0.0, 0.5) pos (0.436, 0.885) xysize (0.41, int(248*interface_adjustment)):
                spacing 0

                for reward_type in current_journal_Quest.rewards.keys():
                    for reward in current_journal_Quest.rewards[reward_type]:
                        fixed xysize (int(249*interface_adjustment), int(249*interface_adjustment)):
                            add At(f"images/interface/Player_menu/journal_{reward_type}.webp", interface)

                            text reward.upper() anchor (0.5, 0.5) pos (0.5, 0.81):
                                size 20

screen map_screen():
    style_prefix "Player_menu"

    $ available_groups = []
    $ available_subgroups = []

    for possible_group in location_groups.keys():
        if possible_group in ["Institute"] or time_index < 3:
            if type(location_groups[possible_group]) is dict:
                for possible_subgroup in location_groups[possible_group].keys():
                    for possible_location in location_groups[possible_group][possible_subgroup]:
                        # if possible_location in unlocked_locations.keys():
                        $ available_groups.append(possible_group)
                        $ available_subgroups.append(possible_subgroup)
            else:        
                for possible_location in location_groups[possible_group]:
                    # if possible_location in unlocked_locations.keys():
                    $ available_groups.append(possible_group)

    add "images/interface/Player_menu/map_background.webp" zoom interface_adjustment

    for location_group in location_groups.keys():
        if location_group in available_groups:
            imagebutton:
                idle At(f"images/interface/Player_menu/map_selection_{location_group}_idle.webp", interface)
                hover At(f"images/interface/Player_menu/map_selection_{location_group}.webp", interface)
                selected_idle At(f"images/interface/Player_menu/map_selection_{location_group}.webp", interface)

                selected location_group == current_group

                action [
                    SetVariable("current_group", location_group),
                    SetVariable("current_subgroup", "First Floor")]

            if location_group == "Institute":
                text "INSTITUTE" anchor (0.5, 0.5) pos (0.107, 0.251):
                    size 36
            elif location_group == "Mall":
                text "MALL" anchor (0.5, 0.5) pos (0.107, 0.331):
                    size 36

    if type(location_groups[current_group]) is dict:
        for location_subgroup in location_groups[current_group].keys():
            if location_subgroup in available_subgroups:
                imagebutton:
                    idle At(f"images/interface/Player_menu/map_floor_{location_subgroup.replace(' ', '_')}_idle.webp", interface)
                    hover At(f"images/interface/Player_menu/map_floor_{location_subgroup.replace(' ', '_')}.webp", interface)
                    selected_idle At(f"images/interface/Player_menu/map_floor_{location_subgroup.replace(' ', '_')}.webp", interface)

                    action SetVariable("current_subgroup", location_subgroup)

    # if blinking:
    text "FLOORS" + "{alpha=0.0}_{/alpha}" anchor (0.0, 0.5) pos (0.065, 0.444):
        size 35
    # else:
    #     text "FLOORS" + "_" anchor (0.0, 0.5) pos (0.065, 0.444):
    #         size 35

    if sandbox:
        imagebutton:
            idle At("images/interface/Player_menu/map_quikloc1_idle.webp", interface)
            hover At("images/interface/Player_menu/map_quikloc1.webp", interface)
            selected_idle At("images/interface/Player_menu/map_quikloc1.webp", interface)

            selected quick_location_1 is None

            if quick_location_2 is None:
                action [
                    SetVariable("quick_location_2", False),
                    SetVariable("quick_location_1", None)]
            elif quick_location_3 is None:
                action [
                    SetVariable("quick_location_3", False),
                    SetVariable("quick_location_1", None)]
            else:
                if quick_location_1 is None:
                    action SetVariable("quick_location_1", False)
                else:
                    action SetVariable("quick_location_1", None)

        imagebutton:
            idle At("images/interface/Player_menu/map_quikloc2_idle.webp", interface)
            hover At("images/interface/Player_menu/map_quikloc2.webp", interface)
            selected_idle At("images/interface/Player_menu/map_quikloc2.webp", interface)

            selected quick_location_2 is None

            if quick_location_1 is None:
                action [
                    SetVariable("quick_location_1", False),
                    SetVariable("quick_location_2", None)]
            elif quick_location_3 is None:
                action [
                    SetVariable("quick_location_3", False),
                    SetVariable("quick_location_2", None)]
            else:
                if quick_location_2 is None:
                    action SetVariable("quick_location_2", False)
                else:
                    action SetVariable("quick_location_2", None)

        imagebutton:
            idle At("images/interface/Player_menu/map_quikloc3_idle.webp", interface)
            hover At("images/interface/Player_menu/map_quikloc3.webp", interface)
            selected_idle At("images/interface/Player_menu/map_quikloc3.webp", interface)

            selected quick_location_3 is None

            if quick_location_1 is None:
                action [
                    SetVariable("quick_location_1", False),
                    SetVariable("quick_location_3", None)]
            elif quick_location_2 is None:
                action [
                    SetVariable("quick_location_2", False),
                    SetVariable("quick_location_3", None)]
            else:
                if quick_location_3 is None:
                    action SetVariable("quick_location_3", False)
                else:
                    action SetVariable("quick_location_3", None)

        text "1" anchor (0.5, 0.5) pos (0.073, 0.892):
            size 36

        text "2" anchor (0.5, 0.5) pos (0.107, 0.892):
            size 36

        text "3" anchor (0.5, 0.5) pos (0.14, 0.892):
            size 36

    # if blinking:
    text "QUICK TRAVEL" + "{alpha=0.0}_{/alpha}" anchor (0.0, 0.5) pos (0.065, 0.801):
        size 30
    # else:
    #     text "QUICK TRAVEL" + "_" anchor (0.0, 0.5) pos (0.065, 0.801):
    #         size 30

    $ map_to_show = None

    if current_group == "Institute":
        if current_subgroup == "Basement":
            $ map_to_show = "basement"
        elif current_subgroup == "First Floor":
            $ map_to_show = "first_floor"
        elif current_subgroup == "Second Floor":
            $ map_to_show = "second_floor"
        elif current_subgroup == "Attic":
            $ map_to_show = "attic"
            
        add f"images/interface/Player_menu/map_institute_{map_to_show}.webp" zoom interface_adjustment
    elif current_group == "Mall":
        if current_subgroup == "First Floor":
            $ map_to_show = "mall"
            
        add "images/interface/Player_menu/map_mall.webp" zoom interface_adjustment
        
    if map_to_show:
        if current_subgroup:
            for possible_location in location_groups[current_group][current_subgroup]:
                if possible_location in marked_locations.keys():
                    button:
                        selected Player.location == possible_location

                        if possible_location in available_locations.keys():
                            if quick_location_1 is None:
                                action SetVariable("quick_location_1", available_locations[possible_location])
                            elif quick_location_2 is None:
                                action SetVariable("quick_location_2", available_locations[possible_location])
                            elif quick_location_3 is None:
                                action SetVariable("quick_location_3", available_locations[possible_location])
                            elif Player.location != possible_location:
                                action Function(exec, available_locations[possible_location])
                            else:
                                action NullAction()
                        else:
                            hover_sound None

                            action NullAction()

                        if possible_location not in bedrooms:
                            background None

                            if possible_location in ["bg_girls_hallway", "bg_hallway"]:
                                text map_names[possible_location] anchor (0.5, 0.5) pos (0.8, 0.5):
                                    size 36

                                    if possible_location in available_locations.keys():
                                        color "#000000" 
                                        hover_color "#aa4b14" 
                                        selected_color "#aa4b14"
                                    else:
                                        color "#bfbfbf"

                                    vertical True
                            elif possible_location in ["bg_mall"]:
                                text map_names[possible_location] anchor (0.5, 0.5) pos (0.65, 0.5):
                                    size 36

                                    if possible_location in available_locations.keys():
                                        color "#000000" 
                                        hover_color "#aa4b14" 
                                        selected_color "#aa4b14"
                                    else:
                                        color "#bfbfbf"

                                    vertical True
                            else:
                                text map_names[possible_location]:
                                    size 36

                                    if possible_location in available_locations.keys():
                                        color "#000000" 
                                        hover_color "#aa4b14" 
                                        selected_color "#aa4b14"
                                    else:
                                        color "#bfbfbf"
                        elif possible_location == "bg_Player":
                            idle_background At(f"images/interface/Player_menu/Player_{Player.background_color}_idle.webp", interface)
                            hover_background At(f"images/interface/Player_menu/Player_{Player.background_color}.webp", interface)
                            selected_idle_background At(f"images/interface/Player_menu/Player_{Player.background_color}.webp", interface)
                        elif possible_location not in ["bg_Charles", "bg_Kurt"]:
                            if possible_location in available_locations.keys():
                                idle_background At(f"images/interface/Player_menu/{possible_location[3:]}_idle.webp", interface)
                                hover_background At(f"images/interface/Player_menu/{possible_location[3:]}.webp", interface)
                                selected_idle_background At(f"images/interface/Player_menu/{possible_location[3:]}.webp", interface)
                            else:
                                background None
                        else:
                            background None

                            text map_names[possible_location]:
                                size 36

                                if possible_location in available_locations.keys():
                                    color "#000000" hover_color "#ffa903" selected_color "#ffa903"
                                else:
                                    color "#bfbfbf"

                        if possible_location == "bg_campus":
                            pos (0.445, 0.89) xysize (0.49, 0.11)
                        elif possible_location == "bg_Charles":
                            pos (0.445, 0.503) xysize (0.1, 0.135)
                        elif possible_location == "bg_classroom":
                            pos (0.628, 0.408) xysize (0.12, 0.166)
                        elif possible_location == "bg_danger":
                            pos (0.2615, 0.408) xysize (0.125, 0.169)
                        elif possible_location == "bg_entrance":
                            pos (0.445, 0.7965) xysize (0.01, 0.01)
                        elif possible_location == "bg_girls_hallway":
                            pos (0.2615, 0.578) xysize (0.0274, 0.51)
                        elif possible_location == "bg_hallway":
                            pos (0.6285, 0.578) xysize (0.0274, 0.51)
                        elif possible_location == "bg_Kurt":
                            pos (0.589, 0.604) xysize (0.05, 0.05)
                        elif possible_location == "bg_lockers":
                            pos (0.336, 0.534) xysize (0.118, 0.075)
                        elif possible_location == "bg_mall":
                            pos (0.347, 0.5765) xysize (0.038, 0.533)
                        elif possible_location == "bg_movies":
                            pos (0.485, 0.477) xysize (0.074, 0.2)
                        elif possible_location == "bg_pool":
                            pos (0.445, 0.352) xysize (0.243, 0.157)
                        elif possible_location == "bg_study":
                            pos (0.628, 0.739) xysize (0.12, 0.183)
                        else:
                            focus_mask True

    if blinking:
        text "X-TRACKER" + "{alpha=0.0}_{/alpha}" anchor (0.0, 0.5) pos (0.733, 0.237):
            size 35
    else:
        text "X-TRACKER" + "_" anchor (0.0, 0.5) pos (0.733, 0.237):
            size 35

    vpgrid anchor (0.5, 0.0) pos (0.828, 0.294) xysize (0.19, 0.63):
        cols 1

        spacing 15

        draggable True
        mousewheel True

        xfill True

        for possible_group in location_groups.keys():
            for possible_subgroup in location_groups[possible_group].keys():
                for possible_location in location_groups[possible_group][possible_subgroup]:
                    if possible_location in marked_locations.keys():
                        if marked_locations[possible_location] or Player.location == possible_location or get_Present(location = possible_location, include_Party = False)[0]:
                            text location_names[possible_location] xalign 0.0:
                                size 36

                                text_align 0.0

                            fixed xysize(1.0, int(88*interface_adjustment)):
                                hbox xalign 0.0:
                                    spacing 5
                                    if marked_locations[possible_location]:
                                        add At("images/interface/Player_menu/event_alert.webp", phone_icon)

                                    if Player.location == possible_location:
                                        add At(f"images/interface/phone/icons/Player_{Player.background_color}.webp", map_icon)

                                    for C in all_Characters:
                                        if C.location == possible_location:
                                            add At(f"images/interface/phone/icons/{C.tag}.webp", map_icon)