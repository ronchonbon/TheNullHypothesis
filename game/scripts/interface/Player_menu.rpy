init -4:

    default quick_location_1 = False
    default quick_location_2 = False
    default quick_location_3 = False
    
    default current_Player_menu_page = "database"

    default current_database_Character = None
    default current_database_page = 0

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
                "bg_Ororo",
                "bg_Charles"],
            "Attic": []},

        "Mall": {
            "First Floor": [
                "bg_mall",
                "bg_movies"]},

        "Town": {
            "Main Street": [
                "bg_town"]}}

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
        "bg_Charles": []}

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
        add "images/interface/main_menu/blank_background.webp" zoom interface_new_adjustment

        add At("images/interface/preferences/spin.webp", spinning_element) anchor (0.5, 0.5) pos (0.502, 0.502) zoom interface_new_adjustment

        add "images/interface/Player_menu/top.webp" zoom interface_new_adjustment

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

        # if current_Player_menu_page == "database":
        #     use database_screen
        # elif current_Player_menu_page == "skills":
        #     use skills_screen
        if current_Player_menu_page == "inventory":
            use inventory_screen
        # elif current_Player_menu_page == "journal":
        #     use journal_screen
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

    $ database_Characters = unlocked_Characters[:]
    $ database_Characters.sort(key = return_last_name)
    $ database_Characters.insert(0, Player)

    add "images/interface/Player_menu/database_background.webp"

    viewport id "database_viewport" anchor (0.5, 0.0) pos (0.1435, 0.192) xysize (int(450*interface_new_sampling), int(803*interface_new_sampling)):
        draggable True
        mousewheel True

        vbox:
            for C in database_Characters:
                button xysize (int(453*interface_new_sampling), int(114*interface_new_sampling)):
                    idle_background "images/interface/Player_menu/database_name_idle.webp" 
                    hover_background f"images/interface/Player_menu/database_name.webp" 
                    selected_idle_background f"images/interface/Player_menu/database_name.webp"
                    
                    selected current_database_Character == C

                    text C.call_sign anchor (0.5, 0.5) pos (0.5, 0.5):
                        size 36

                        color "#000000"

                    action SetVariable("current_database_Character", C)

    vbar value YScrollValue("database_viewport") anchor (0.5, 0.0) pos (0.2693, 0.19) xysize (int(22*interface_new_sampling), int(803*interface_new_sampling)):
        base_bar Frame("images/interface/Player_menu/database_scrollbar.webp")

        thumb "images/interface/Player_menu/database_scrollbar_thumb.webp"
        thumb_offset 10

        unscrollable "hide"

    if current_database_Character:
        $ database_length = 0

        if "description" in current_database_Character.database.keys():
            $ database_length += len(current_database_Character.database["description"])

        if "wiki" in current_database_Character.database.keys():
            $ database_length += 1

        if database_length > 1:
            imagebutton:
                idle "images/interface/Player_menu/database_previous_idle.webp" 
                hover "images/interface/Player_menu/database_previous.webp"

                action SetVariable("current_database_page", (current_database_page - 1) % database_length)

            text f"{current_database_page + 1} / {database_length}" anchor (0.5, 0.5) pos (0.735, 0.1995):
                size 36

                color "#000000"

            imagebutton:
                idle "images/interface/Player_menu/database_next_idle.webp" 
                hover "images/interface/Player_menu/database_next.webp"

                action SetVariable("current_database_page", (current_database_page + 1) % database_length)
        
        if current_database_Character in all_Companions or current_database_Character in all_NPCs:
            add At(f"images/interface/phone/photos/{current_database_Character.tag}.webp", database_photo) anchor (0.0, 0.0) pos (0.33, 0.24)
        elif current_database_Character == Player:
            add At("Player_portrait", database_photo) anchor (0.0, 0.0) pos (0.33, 0.24)

        if database_length >= 1:
            if current_database_page < len(current_database_Character.database["description"]):
                frame anchor (0.5, 0.0) pos (0.5825, 0.25) xsize 0.25:
                    background Frame("images/interface/Player_menu/database_text_frame.webp", 10, 10)

                    text current_database_Character.database["stats"]:
                        size 24

                        color "#000000"

                        text_align 0.0

                frame anchor (0.5, 0.0) pos (0.8375, 0.25) xsize 0.225:
                    background Frame("images/interface/Player_menu/database_text_frame.webp", 10, 10)

                    text current_database_Character.database["study_materials"]:
                        size 28

                        color "#000000"

                        text_align 0.0

                frame anchor (0.0, 0.0) pos (0.33, 0.55) xsize 0.62:
                    background Frame("images/interface/Player_menu/database_text_frame.webp", 10, 10)

                    text current_database_Character.database["description"][current_database_page]:
                        if len(current_database_Character.database["description"][current_database_page]) < 800:
                            size 36
                        elif len(current_database_Character.database["description"][current_database_page]) < 1500:
                            size 30
                        else:
                            size 24

                        color "#000000"

                        text_align 0.0
            elif "wiki" in current_database_Character.database.keys():
                frame anchor (0.0, 0.0) pos (0.4575, 0.25) xsize 0.475:
                    background Frame("images/interface/Player_menu/database_text_frame.webp", 10, 10)

                    text current_database_Character.database["wiki"]:
                        size 36

                        color "#000000"

                        text_align 0.0

                vbox anchor (0.0, 1.0) pos (0.33, 0.9) xsize 0.62:
                    for comment in current_database_Character.database["comments"]:
                        frame xalign 0.0 xsize 0.62:
                            background Frame("images/interface/Player_menu/database_text_frame.webp", 10, 10)

                            text comment xalign 0.0:
                                size 24

                                color "#000000"

                                text_align 0.0

        text f"CODENAME: {current_database_Character.call_sign}" anchor (0.5, 0.5) pos (0.415, 0.2):
            size 36

            color "#512908"

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

    add "images/interface/Player_menu/inventory_background.webp" zoom interface_new_adjustment

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
            text "TAB{alpha=0.0}_{/alpha}" + f" 0{current_inventory_page + 1}" anchor (0.5, 0.5) pos (0.086, 0.808):
                size 35
        else:
            text f"TAB_ 0{current_inventory_page + 1}" anchor (0.5, 0.5) pos (0.086, 0.808):
                size 35
    else:
        if blinking:
            text "TAB{alpha=0.0}_{/alpha}" + f" {current_inventory_page + 1}" anchor (0.5, 0.5) pos (0.086, 0.808):
                size 35
        else:
            text f"TAB_ {current_inventory_page + 1}" anchor (0.5, 0.5) pos (0.086, 0.808):
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
                    
                button xysize (int(355*interface_new_adjustment), int(355*interface_new_adjustment)):
                    if current_inventory_Item == Item_string:
                        background At("images/interface/Player_menu/inventory_selector.webp", interface)
                    else:
                        background None

                    hover_sound None

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
                
                button xysize (int(355*interface_new_adjustment), int(355*interface_new_adjustment)):
                    if current_inventory_Item == Clothing:
                        background At("images/interface/Player_menu/inventory_selector.webp", interface)
                    else:
                        background None

                    hover_sound None

                    if Clothing.shop_type == "clothing":
                        add "images/interface/items/mutant_couture.webp" anchor (0.5, 0.5) pos (0.5, 0.5) zoom 0.5
                    elif Clothing.shop_type == "lingerie":
                        add "images/interface/items/xtreme_intimates.webp" anchor (0.5, 0.5) pos (0.5, 0.5) zoom 0.5

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

    if blinking:
        text "ITEM NAME" + "{alpha=0.0}_{/alpha}" anchor (0.0, 0.5) pos (0.674, 0.335):
            size 35
    else:
        text "ITEM NAME" + "_" anchor (0.0, 0.5) pos (0.674, 0.335):
            size 35

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

    if blinking:
        text "CASH" + "{alpha=0.0}_{/alpha}" anchor (0.0, 0.5) pos (0.674, 0.907):
            size 50
    else:
        text "CASH" + "_" anchor (0.0, 0.5) pos (0.674, 0.907):
            size 50

    text f"$ {Player.cash}" anchor (1.0, 0.5) pos (0.93, 0.907):
        size 50

screen confirm_gift_screen(Character, Item):
    modal True

    style_prefix "confirm"

    frame anchor (0.5, 0.5) pos (0.5, 0.5):
        padding (25, 25, 25, 25)

        vbox:
            spacing 25

            text f"Give {Character.name} the {Item.name}?":
                size 40
                
            hbox:
                spacing 100

                textbutton _("Yes"): 
                    text_size 36

                    if hasattr(Item, "available_states"):
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

    add "images/interface/Player_menu/journal_background.webp" anchor (0.5, 0.5) pos (0.5, 0.5)

    hbox anchor (0.0, 0.5) pos (0.075, 0.185):
        spacing 10

        button xysize (int(225*interface_new_sampling), int(65*interface_new_sampling)):
            idle_background "images/interface/Player_menu/journal_filter_idle.webp" 
            hover_background "images/interface/Player_menu/journal_filter.webp" 
            selected_idle_background "images/interface/Player_menu/journal_filter_selected_main.webp" 
            selected_hover_background "images/interface/Player_menu/journal_filter_selected_main.webp"

            selected current_journal_filter == "main"

            text "Main" anchor (0.5, 0.5) pos (0.5, 0.5):
                size 36

                color "#000000"

            if current_journal_filter == "main":
                action SetVariable("current_journal_filter", None)
            else:
                action [
                    SetVariable("current_journal_Quest", None),
                    SetVariable("current_journal_filter", "main")]

        button xysize (int(225*interface_new_sampling), int(65*interface_new_sampling)):
            idle_background "images/interface/Player_menu/journal_filter_idle.webp" 
            hover_background "images/interface/Player_menu/journal_filter.webp" 
            selected_idle_background "images/interface/Player_menu/journal_filter_selected_side.webp" 
            selected_hover_background "images/interface/Player_menu/journal_filter_selected_side.webp"

            selected current_journal_filter == "side"

            text "Side" anchor (0.5, 0.5) pos (0.5, 0.5):
                size 36

                color "#000000"

            if current_journal_filter == "side":
                action SetVariable("current_journal_filter", None)
            else:
                action [
                    SetVariable("current_journal_Quest", None),
                    SetVariable("current_journal_filter", "side")]

        button xysize (int(225*interface_new_sampling), int(65*interface_new_sampling)):
            idle_background "images/interface/Player_menu/journal_filter_idle.webp" 
            hover_background "images/interface/Player_menu/journal_filter.webp" 
            selected_idle_background "images/interface/Player_menu/journal_filter_selected_dlc.webp" 
            selected_hover_background "images/interface/Player_menu/journal_filter_selected_dlc.webp"

            selected current_journal_filter == "dlc"

            text "Add-Ons" anchor (0.5, 0.5) pos (0.5, 0.5):
                size 36

                color "#000000"

            if current_journal_filter == "dlc":
                action SetVariable("current_journal_filter", None)
            else:
                action [
                    SetVariable("current_journal_Quest", None),
                    SetVariable("current_journal_filter", "dlc")]

    hbox anchor (0.0, 0.5) pos (0.07325, 0.283):
        spacing 10 
        
        button xysize (int(225*interface_new_sampling), int(65*interface_new_sampling)):
            idle_background "images/interface/Player_menu/journal_chapter_idle.webp" 
            hover_background "images/interface/Player_menu/journal_chapter.webp" 
            selected_idle_background "images/interface/Player_menu/journal_chapter_selected.webp" 
            selected_hover_background "images/interface/Player_menu/journal_chapter_selected.webp"

            selected not show_completed_Quests

            text "Current" anchor (0.5, 0.5) pos (0.55, 0.55):
                size 36

                color "#000000"

            if not show_completed_Quests:
                action SetVariable("show_completed_Quests", True)
            else:
                action [
                    SetVariable("current_journal_Quest", None),
                    SetVariable("show_completed_Quests", False)]

        for c in range(1, chapter + 1):
            button xysize (int(225*interface_new_sampling), int(65*interface_new_sampling)):
                idle_background "images/interface/Player_menu/journal_chapter_idle.webp" 
                hover_background "images/interface/Player_menu/journal_chapter.webp" 
                selected_idle_background "images/interface/Player_menu/journal_chapter_selected.webp" 
                selected_hover_background "images/interface/Player_menu/journal_chapter_selected.webp"

                selected current_journal_chapter == c

                text f"Chapter {chapter_names[c]}" anchor (0.5, 0.5) pos (0.53, 0.55):
                    size 36

                    color "#000000"

                if current_journal_chapter == c:
                    action SetVariable("current_journal_chapter", None)
                else:
                    action [
                        SetVariable("current_journal_Quest", None),
                        SetVariable("current_journal_chapter", c)]

    viewport id "journal_viewport" anchor (0.5, 0.0) pos (0.187, 0.378) xysize (int(456*interface_new_sampling), int(575*interface_new_sampling)):
        draggable True
        mousewheel True

        vbox:
            for Q in reversed(QuestPool.Quests.values()):
                if Q.unlocked and (not current_journal_filter or Q.Quest_type == current_journal_filter) and (not current_journal_chapter or Q.chapter == current_journal_chapter):
                    if show_completed_Quests or not Q.completed:
                        button xysize (int(456*interface_new_sampling), int(96*interface_new_sampling)):
                            idle_background f"images/interface/Player_menu/journal_quest_{Q.Quest_type}.webp" hover_background f"images/interface/Player_menu/journal_quest_{Q.Quest_type}_selected.webp" selected_idle_background f"images/interface/Player_menu/journal_quest_{Q.Quest_type}_selected.webp"
                            
                            selected current_journal_Quest == Q

                            text Q.name anchor (0.5, 0.5) pos (0.5, 0.5):
                                size 36

                                color "#000000"

                            if Q.completed:
                                add "images/interface/Player_menu/journal_quest_completed.webp" anchor (0.5, 0.5) pos (0.5, 0.49)

                                text "CLEAR" anchor (0.5, 0.5) pos (0.5, 0.75):
                                    size 24

                                    color "#ffc107"

                            action SetVariable("current_journal_Quest", Q)

    vbar value YScrollValue("journal_viewport") anchor (0.5, 0.0) pos (0.325, 0.364) xysize (int(22*interface_new_sampling), int(602*interface_new_sampling)):
        base_bar Frame("images/interface/Player_menu/journal_scrollbar.webp")

        thumb "images/interface/Player_menu/journal_scrollbar_thumb.webp"
        thumb_offset 10

        unscrollable "hide"

    if current_journal_Quest:
        if current_journal_Quest.completed:
            add "images/interface/Player_menu/journal_complete.webp"

        text "SUMMARY" anchor (0.0, 0.0) pos (0.37, 0.36):
            size 36

            color "#512908"

        text current_journal_Quest.description anchor (0.5, 0.0) pos (0.64, 0.365):
            if len(current_journal_Quest.description) >= 25:
                size 32
            else:
                size 36

            color "#000000"

        text "OBJECTIVES" anchor (0.0, 0.0) pos (0.37, 0.44):
            size 36

            color "#512908"

        vbox anchor (0.5, 0.0) pos (0.64, 0.445):
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
                            size 32

                            color "#000000"
                    else:
                        text "[objective]: [progress]/[target]" anchor (0.5, 0.5) pos (0.5, 0.5):
                            size 32

                            color "#000000"
                else:
                    if eval(current_journal_Quest.objectives[objective][0]):
                        $ objective = renpy.substitute(objective)

                        text "{s}[objective]{/s}" anchor (0.5, 0.5) pos (0.5, 0.5):
                            size 32

                            color "#000000"
                    else:
                        $ objective = renpy.substitute(objective)

                        text "[objective]" anchor (0.5, 0.5) pos (0.5, 0.5):
                            size 32

                            color "#000000"

            for optional_objective in current_journal_Quest.optional_objectives.keys():
                if current_journal_Quest.optional_objectives[optional_objective][1]:
                    $ progress = eval(current_journal_Quest.optional_objectives[optional_objective][0])
                    $ target = current_journal_Quest.optional_objectives[optional_objective][1]

                    $ optional_objective = renpy.substitute(optional_objective)

                    if current_journal_Quest.completed or progress > target:
                        $ progress = target

                    if progress == target:
                        text "{s}{i}[optional_objective]: [progress]/[target]{/i}{/s}" anchor (0.5, 0.5) pos (0.5, 0.5):
                            size 32

                            color "#000000"
                    else:
                        text "{i}[optional_objective]: [progress]/[target]{/i}" anchor (0.5, 0.5) pos (0.5, 0.5):
                            size 32

                            color "#000000"
                else:
                    if eval(current_journal_Quest.optional_objectives[optional_objective][0]):
                        $ optional_objective = renpy.substitute(optional_objective)

                        text "{s}{i}[optional_objective]{/i}{/s}" anchor (0.5, 0.5) pos (0.5, 0.5):
                            size 32

                            color "#000000"
                    else:
                        $ optional_objective = renpy.substitute(optional_objective)

                        text "{i}[optional_objective]{/i}" anchor (0.5, 0.5) pos (0.5, 0.5):
                            size 32

                            color "#000000"

        text "REWARDS" anchor (0.0, 0.0) pos (0.37, 0.8):
            size 36
            
            color "#512908"

        vbox anchor (0.5, 0.0) pos (0.64, 0.8025):
            spacing 5

            for reward in current_journal_Quest.rewards:
                text reward anchor (0.5, 0.5) pos (0.5, 0.5):
                    if len(current_journal_Quest.rewards) > 2:
                        size 28
                    else:
                        size 36

                    color "#000000"

screen map_screen():
    style_prefix "Player_menu"

    $ available_groups = []
    $ available_subgroups = []

    for possible_group in location_groups.keys():
        if possible_group in ["Institute"] or time_index < 3:
            if type(location_groups[possible_group]) is dict:
                for possible_subgroup in location_groups[possible_group].keys():
                    for possible_location in location_groups[possible_group][possible_subgroup]:
                        if possible_location in unlocked_locations.keys():
                            $ available_groups.append(possible_group)
                            $ available_subgroups.append(possible_subgroup)
            else:        
                for possible_location in location_groups[possible_group]:
                    if possible_location in unlocked_locations.keys():
                        $ available_groups.append(possible_group)

    add "images/interface/Player_menu/map_background.webp" zoom interface_new_adjustment

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

    if blinking:
        text "FLOORS" + "{alpha=0.0}_{/alpha}" anchor (0.0, 0.5) pos (0.065, 0.444):
            size 35
    else:
        text "FLOORS" + "_" anchor (0.0, 0.5) pos (0.065, 0.444):
            size 35

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

    if blinking:
        text "QUICK TRAVEL" + "{alpha=0.0}_{/alpha}" anchor (0.0, 0.5) pos (0.065, 0.801):
            size 30
    else:
        text "QUICK TRAVEL" + "_" anchor (0.0, 0.5) pos (0.065, 0.801):
            size 30

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
            
        add f"images/interface/Player_menu/map_institute_{map_to_show}.webp" zoom interface_new_adjustment
    elif current_group == "Mall":
        if current_subgroup == "First Floor":
            $ map_to_show = "mall"
            
        add "images/interface/Player_menu/map_mall.webp" zoom interface_new_adjustment
        
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
                        elif possible_location not in ["bg_Kurt", "bg_Charles"]:
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
                        if marked_locations[possible_location] or Player.location == possible_location or get_Present(location = possible_location)[0]:
                            text location_names[possible_location] xalign 0.0:
                                size 36

                                text_align 0.0

                            fixed xysize(1.0, int(44*interface_new_sampling)):
                                hbox xalign 0.0:
                                    spacing 5
                                    if marked_locations[possible_location]:
                                        add At("images/interface/Player_menu/event_alert.webp", phone_icon)

                                    if Player.location == possible_location:
                                        add At(f"images/interface/phone/icons/Player_{Player.background_color}.webp", map_icon)

                                    for C in all_Characters:
                                        if C.location == possible_location:
                                            add At(f"images/interface/phone/icons/{C.tag}.webp", map_icon)