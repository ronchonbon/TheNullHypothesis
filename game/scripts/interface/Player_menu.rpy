init -4:

    default quick_location_1 = False
    default quick_location_2 = False
    default quick_location_3 = False
    
    default current_Player_menu_page = "database"

    default current_database_Character = None
    default current_database_page = 0

    default current_inventory_page = 0
    default current_inventory_filter = "gifts"
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

style Player_menu_button:
    # hover_sound "sounds/interface/hover.ogg"
    activate_sound "sounds/interface/press.ogg"

style Player_menu_image_button:
    # hover_sound "sounds/interface/hover.ogg"
    activate_sound "sounds/interface/press.ogg"

screen Player_menu():
    layer "interface"

    modal True

    style_prefix "Player_menu"

    on "show" action [
        Hide("say"),
        Hide("phone_screen"),
        SetVariable("current_inventory_filter", "gifts"),
        SetVariable("choice_disabled", True),
        Function(EventScheduler.update_conditions)]
    on "hide" action [
        SetVariable("giving_gift", False),
        SetVariable("current_inventory_Item", None),
        SetVariable("choice_disabled", False)]

    if not black_screen and not renpy.get_screen("say"):
        add "images/interface/Player_menu/background.webp" align (0.5, 0.5)

        for page in ["database", "inventory", "journal", "map"]:
            imagebutton align (0.5, 0.5):
                idle f"images/interface/Player_menu/{page}_idle.webp" hover f"images/interface/Player_menu/{page}.webp" selected_idle f"images/interface/Player_menu/{page}.webp" selected_hover f"images/interface/Player_menu/{page}.webp"

                selected current_Player_menu_page == page

                action SetVariable("current_Player_menu_page", page)

                focus_mask True

        imagebutton align (0.5, 0.5):
            idle "images/interface/Player_menu/preferences_idle.webp" hover "images/interface/Player_menu/preferences.webp"

            action ShowMenu("preferences")

            focus_mask True

        imagebutton align (0.5, 0.5):
            idle "images/interface/Player_menu/exit_idle.webp" hover "images/interface/Player_menu/exit.webp"

            if not sandbox:
                action [
                    Hide("Player_menu"),
                    Return()]
            else:
                action Hide("Player_menu")

            focus_mask True

        if current_Player_menu_page == "database":
            use database_screen
        elif current_Player_menu_page == "inventory":
            use inventory_screen
        elif current_Player_menu_page == "journal":
            use journal_screen
        elif current_Player_menu_page == "map":
            use map_screen

    if black_screen or renpy.get_screen("say"):
        button align (0.5, 0.5) xysize (config.screen_width, config.screen_height):
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

    add "images/interface/Player_menu/database_background.webp" align (0.5, 0.5)

    viewport id "database_viewport" anchor (0.5, 0.0) pos (0.1435, 0.192) xysize (int(450*2*interface_sampling), int(803*2*interface_sampling)):
        draggable True
        mousewheel True

        vbox xalign 0.5:
            for C in database_Characters:
                button xysize (int(453*2*interface_sampling), int(114*2*interface_sampling)):
                    idle_background "images/interface/Player_menu/database_name_idle.webp" hover_background f"images/interface/Player_menu/database_name.webp" selected_idle_background f"images/interface/Player_menu/database_name.webp"
                    
                    selected current_database_Character == C

                    text C.call_sign anchor (0.5, 0.5) pos (0.5, 0.5):
                        size 36

                        color "#000000"

                    action SetVariable("current_database_Character", C)

    vbar value YScrollValue("database_viewport") anchor (0.5, 0.0) pos (0.2693, 0.19) xysize (int(22*2*interface_sampling), int(803*2*interface_sampling)):
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
                idle "images/interface/Player_menu/database_previous_idle.webp" hover "images/interface/Player_menu/database_previous.webp"

                action SetVariable("current_database_page", (current_database_page - 1) % database_length)

                focus_mask True

            text f"{current_database_page + 1} / {database_length}" anchor (0.5, 0.5) pos (0.735, 0.1995):
                size 36

                color "#000000"

            imagebutton:
                idle "images/interface/Player_menu/database_next_idle.webp" hover "images/interface/Player_menu/database_next.webp"

                action SetVariable("current_database_page", (current_database_page + 1) % database_length)

                focus_mask True
        
        if current_database_Character in all_Companions or current_database_Character in all_NPCs:
            add At(f"images/interface/phone/photos/{current_database_Character.tag}.webp", database_photo) anchor (0.0, 0.0) pos (0.33, 0.24)
        elif current_database_Character == Player:
            add At("Player_portrait", database_photo) anchor (0.0, 0.0) pos (0.33, 0.24)

        if database_length >= 1:
            if current_database_page < len(current_database_Character.database["description"]):
                frame anchor (0.5, 0.0) pos (0.5825, 0.25) xsize 0.25:
                    background Frame("images/interface/Player_menu/database_text_frame.webp", 30, 30)

                    text current_database_Character.database["stats"]:
                        size 24

                        color "#000000"

                        text_align 0.0

                frame anchor (0.5, 0.0) pos (0.8375, 0.25) xsize 0.225:
                    background Frame("images/interface/Player_menu/database_text_frame.webp", 30, 30)

                    text current_database_Character.database["study_materials"]:
                        size 28

                        color "#000000"

                        text_align 0.0

                frame anchor (0.0, 0.0) pos (0.33, 0.55) xsize 0.62:
                    background Frame("images/interface/Player_menu/database_text_frame.webp", 30, 30)

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
                    background Frame("images/interface/Player_menu/database_text_frame.webp", 30, 30)

                    text current_database_Character.database["wiki"]:
                        size 36

                        color "#000000"

                        text_align 0.0

                vbox anchor (0.0, 1.0) pos (0.33, 0.9) xsize 0.62:
                    for comment in current_database_Character.database["comments"]:
                        frame xalign 0.0 xsize 0.62:
                            background Frame("images/interface/Player_menu/database_text_frame.webp", 30, 30)

                            text comment:
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
        if current_inventory_filter == "gifts" and not isinstance(Player.inventory[Item_string], list):
            $ current_inventory_list.append(Item_string)

        if isinstance(Player.inventory[Item_string], list):
            for I in Player.inventory[Item_string]:
                if current_inventory_filter in I.filter_type:
                    if Item_string not in current_inventory_list:
                        if I.Owner == Player and current_inventory_filter == "key":
                            $ current_inventory_list.append(Item_string)
                        elif I.Owner != Player and current_inventory_filter == "gifts":
                            $ current_inventory_list.append(Item_string)

    add "images/interface/Player_menu/inventory_background.webp" anchor (0.5, 0.5) pos (0.5, 0.5)

    if math.floor(len(current_inventory_list)/15) > 0:
        imagebutton:
            idle "images/interface/Player_menu/inventory_left_arrow_idle.webp" hover "images/interface/Player_menu/inventory_left_arrow.webp"

            action SetVariable("current_inventory_page", (current_inventory_page - 1) % math.ceil(len(current_inventory_list)/15))

            focus_mask True

    if math.floor(len(current_inventory_list)/15) > 0:
        imagebutton:
            idle "images/interface/Player_menu/inventory_right_arrow_idle.webp" hover "images/interface/Player_menu/inventory_right_arrow.webp"

            action SetVariable("current_inventory_page", (current_inventory_page + 1) % math.ceil(len(current_inventory_list)/15))

            focus_mask True

    if math.floor(len(current_inventory_list)/15):
        for i in range(math.ceil(len(current_inventory_list)/15)):
            add "images/interface/Player_menu/inventory_page_empty.webp" anchor (0.5, 0.5) pos (0.05 + 0.05*i, 0.26)

            if current_inventory_page == i:
                add "images/interface/Player_menu/inventory_page.webp" anchor (0.5, 0.5) pos (0.05 + 0.05*i, 0.26)

    grid 5 3 anchor (0.5, 0.5) pos (0.352, 0.628) xysize (int(1075*2*interface_sampling), int(640*2*interface_sampling)):
        xspacing 13
        yspacing 11

        for i in range(15*current_inventory_page, min(15*(current_inventory_page + 1), len(current_inventory_list))):
            $ Item_string = current_inventory_list[i]
            
            if isinstance(Player.inventory[Item_string], list):
                $ Item = None

                for I in Player.inventory[Item_string]:
                    if not Item:
                        if I.Owner == Player and current_inventory_filter == "key":
                            $ Item = I
                        elif I.Owner != Player and current_inventory_filter == "gifts":
                            $ Item = I

                if giving_gift and Item.Owner == Player:
                    continue
                    
                button xysize (int(205*2*interface_sampling), int(205*2*interface_sampling)):
                    if current_inventory_Item == Item_string:
                        background "images/interface/Player_menu/inventory_selector.webp"
                    else:
                        background None

                    hover_sound None

                    add f"images/interface/items/{Item_string}.webp" anchor (0.5, 0.5) pos (0.5, 0.5) zoom item_adjustment

                    text f"x{len(Player.inventory[Item_string])}" anchor (1.0, 1.0) pos (1.05, 1.0) size 32:
                        color "#000000"

                    if giving_gift:
                        action [
                            SetVariable("current_inventory_Item", Item_string),
                            Show("confirm_gift_screen", Girl = focused_Girl, Item = Item)]
                    else:
                        action SetVariable("current_inventory_Item", Item_string)
            else:
                $ Clothing = Player.inventory[Item_string]
                
                button xysize (int(205*2*interface_sampling), int(205*2*interface_sampling)):
                    if current_inventory_Item == Clothing:
                        background "images/interface/Player_menu/inventory_selector.webp"
                    else:
                        background None

                    hover_sound None

                    if Clothing.shop_type == "clothing":
                        add "images/interface/items/mutant_couture.webp" anchor (0.5, 0.5) pos (0.5, 0.5) zoom 0.5
                    elif Clothing.shop_type == "lingerie":
                        add "images/interface/items/xtreme_intimates.webp" anchor (0.5, 0.5) pos (0.5, 0.5) zoom 0.5

                    add At(f"images/interface/phone/icons/{Clothing.Owner.tag}.webp", humhum_icon) anchor (0.5, 0.5) pos (0.93, 0.89)

                    if giving_gift and focused_Girl == Clothing.Owner:
                        action [
                            SetVariable("current_inventory_Item", Clothing),
                            Show("confirm_gift_screen", Girl = focused_Girl, Item = Clothing)]
                    else:
                        action SetVariable("current_inventory_Item", Clothing)

    for filter in ["gifts", "key", "cards"]:
        imagebutton:
            idle f"images/interface/Player_menu/inventory_{filter}_idle.webp" hover f"images/interface/Player_menu/inventory_{filter}.webp" selected_idle f"images/interface/Player_menu/inventory_{filter}_selected.webp"

            selected current_inventory_filter == filter

            action [
                SetVariable("current_inventory_Item", None),
                SetVariable("current_inventory_filter", filter)]

            focus_mask True

    text "NAME" anchor (0.0, 0.5) pos (0.6925, 0.235):
        size 50

        color "#512908"

    if isinstance(current_inventory_Item, str):
        $ Item = eval(f"{current_inventory_Item}(None)")

        text f"{Item.name.upper()}" anchor (0.5, 0.5) pos (0.833, 0.295):
            size 40

            color "#512908"

        text "DESCRIPTION" anchor (0.0, 0.5) pos (0.6925, 0.385):
            size 50

            color "#512908"

        text f"{Item.description}" anchor (0.5, 0.5) pos (0.831, 0.585) xysize (int(500*2*interface_sampling), int(500*2*interface_sampling)):
            size 40

            color "#512908"

        text "Quantity" anchor (0.0, 0.5) pos (0.6925, 0.787):
            size 40

            color "#512908"

        if isinstance(Player.inventory[Item.string], list):
            text f"{len(Player.inventory[Item.string])}" anchor (1.0, 0.5) pos (0.96, 0.787):
                size 40

                color "#512908"
        else:
            text "1" anchor (1.0, 0.5) pos (0.96, 0.787):
                size 40

                color "#512908"
    elif current_inventory_Item:
        text f"{current_inventory_Item.name.upper()}" anchor (0.5, 0.5) pos (0.833, 0.295):
            size 40

            color "#512908"

    text "Money" anchor (0.0, 0.5) pos (0.6925, 0.898):
        size 50

        color "#512908"

    text f"$ {Player.cash}" anchor (1.0, 0.5) pos (0.96, 0.898):
        size 50

        color "#512908"

screen confirm_gift_screen(Girl, Item):
    modal True

    style_prefix "confirm"

    frame anchor (0.5, 0.5) pos (0.5, 0.5):
        padding (25, 25, 25, 25)

        vbox:
            spacing 25

            text f"Give {Girl.name} the {Item.name}?" xalign 0.5:
                size 40
                
            hbox:
                spacing 100

                textbutton _("Yes") xminimum int(config.screen_width*0.1) yminimum int(config.screen_height*0.07): 
                    text_size 36

                    if hasattr(Item, "available_states"):
                        action [
                            Hide("confirm_gift_screen"),
                            Call("give_Girl_Clothing", Girl, Item, from_current = True)]
                    else:
                        action [
                            Hide("confirm_gift_screen"),
                            Call("give_Girl_gift", Girl, Item, from_current = True)]

                textbutton _("No") xminimum int(config.screen_width*0.1) yminimum int(config.screen_height*0.07): 
                    text_size 36

                    action Hide("confirm_gift_screen")

screen journal_screen():
    style_prefix "Player_menu"

    add "images/interface/Player_menu/journal_background.webp" anchor (0.5, 0.5) pos (0.5, 0.5)

    hbox anchor (0.0, 0.5) pos (0.075, 0.185):
        spacing 10

        button xysize (int(225*2*interface_sampling), int(65*2*interface_sampling)):
            idle_background "images/interface/Player_menu/journal_filter_idle.webp" hover_background "images/interface/Player_menu/journal_filter.webp" selected_idle_background "images/interface/Player_menu/journal_filter_selected_main.webp" selected_hover_background "images/interface/Player_menu/journal_filter_selected_main.webp"

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

        button xysize (int(225*2*interface_sampling), int(65*2*interface_sampling)):
            idle_background "images/interface/Player_menu/journal_filter_idle.webp" hover_background "images/interface/Player_menu/journal_filter.webp" selected_idle_background "images/interface/Player_menu/journal_filter_selected_side.webp" selected_hover_background "images/interface/Player_menu/journal_filter_selected_side.webp"

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

        button xysize (int(225*2*interface_sampling), int(65*2*interface_sampling)):
            idle_background "images/interface/Player_menu/journal_filter_idle.webp" hover_background "images/interface/Player_menu/journal_filter.webp" selected_idle_background "images/interface/Player_menu/journal_filter_selected_dlc.webp" selected_hover_background "images/interface/Player_menu/journal_filter_selected_dlc.webp"

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
        
        button xysize (int(225*2*interface_sampling), int(65*2*interface_sampling)):
            idle_background "images/interface/Player_menu/journal_chapter_idle.webp" hover_background "images/interface/Player_menu/journal_chapter.webp" selected_idle_background "images/interface/Player_menu/journal_chapter_selected.webp" selected_hover_background "images/interface/Player_menu/journal_chapter_selected.webp"

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
            button xysize (int(225*2*interface_sampling), int(65*2*interface_sampling)):
                idle_background "images/interface/Player_menu/journal_chapter_idle.webp" hover_background "images/interface/Player_menu/journal_chapter.webp" selected_idle_background "images/interface/Player_menu/journal_chapter_selected.webp" selected_hover_background "images/interface/Player_menu/journal_chapter_selected.webp"

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

    viewport id "journal_viewport" anchor (0.5, 0.0) pos (0.187, 0.378) xysize (int(456*2*interface_sampling), int(575*2*interface_sampling)):
        draggable True
        mousewheel True

        vbox xalign 0.5:
            for Q in reversed(QuestPool.Quests.values()):
                if Q.unlocked and (not current_journal_filter or Q.Quest_type == current_journal_filter) and (not current_journal_chapter or Q.chapter == current_journal_chapter):
                    if show_completed_Quests or not Q.completed:
                        button xysize (int(456*2*interface_sampling), int(96*2*interface_sampling)):
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

    vbar value YScrollValue("journal_viewport") anchor (0.5, 0.0) pos (0.325, 0.364) xysize (int(22*2*interface_sampling), int(602*2*interface_sampling)):
        base_bar Frame("images/interface/Player_menu/journal_scrollbar.webp")

        thumb "images/interface/Player_menu/journal_scrollbar_thumb.webp"
        thumb_offset 10

        unscrollable "hide"

    if current_journal_Quest:
        if current_journal_Quest.completed:
            add "images/interface/Player_menu/journal_complete.webp" align (0.5, 0.5)

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

            if hasattr(current_journal_Quest, "optional_objectives"):
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

    if current_group == "Institute":
        add "images/interface/Player_menu/institute_background.webp" anchor (0.5, 0.5) pos (0.5, 0.5)
    elif current_group == "Mall":
        add "images/interface/Player_menu/mall_background.webp" anchor (0.5, 0.5) pos (0.5, 0.5)
    elif current_group == "Town":
        add "images/interface/Player_menu/town_background.webp" anchor (0.5, 0.5) pos (0.5, 0.5)

    vbox anchor (0.5, 0.0) pos (0.120, 0.17):
        spacing 5

        for location_group in location_groups.keys():
            if location_group in available_groups:
                button align (0.5, 0.5) xysize (int(348*2*interface_sampling), int(64*2*interface_sampling)):
                    idle_background "images/interface/Player_menu/map_location_idle.webp" hover_background "images/interface/Player_menu/map_location.webp"

                    if location_group == "Institute":
                        selected_idle_background "images/interface/Player_menu/map_location_institute.webp" selected_hover_background "images/interface/Player_menu/map_location_institute.webp"
                    elif location_group == "Mall":
                        selected_idle_background "images/interface/Player_menu/map_location_mall.webp" selected_hover_background "images/interface/Player_menu/map_location_mall.webp"
                    elif location_group == "Town":
                        selected_idle_background "images/interface/Player_menu/map_location_town.webp" selected_hover_background "images/interface/Player_menu/map_location_town.webp"


                    selected location_group == current_group

                    action [
                        SetVariable("current_group", location_group),
                        SetVariable("current_subgroup", "First Floor")]

                    text location_group align (0.5, 0.5):
                        size 36

                        color "#ffffff"

    if type(location_groups[current_group]) is dict:
        vbox anchor (0.5, 0.0) pos (0.120, 0.405):
            spacing 10

            for location_subgroup in location_groups[current_group].keys():
                if location_subgroup in available_subgroups:
                    button align (0.5, 0.5) xysize (int(247*2*interface_sampling), int(57*2*interface_sampling)):
                        idle_background "images/interface/Player_menu/map_sublocation_idle.webp" hover_background "images/interface/Player_menu/map_sublocation.webp" selected_idle_background "images/interface/Player_menu/map_sublocation_selected.webp" selected_hover_background "images/interface/Player_menu/map_sublocation_selected.webp"

                        action SetVariable("current_subgroup", location_subgroup)

                        text location_subgroup align (0.5, 0.5):
                            size 36

                            color "#000000"

    if sandbox:
        vbox anchor (0.5, 0.0) pos (0.120, 0.74):
            spacing 30

            button align (0.5, 0.5) xysize (int(247*2*interface_sampling), int(57*2*interface_sampling)):
                idle_background "images/interface/Player_menu/map_sublocation_idle.webp" hover_background "images/interface/Player_menu/map_sublocation.webp" selected_idle_background "images/interface/Player_menu/map_sublocation_selected.webp" selected_hover_background "images/interface/Player_menu/map_sublocation_selected.webp"

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

                text "Set QuikLoc I" align (0.5, 0.5):
                    size 36

                    color "#000000"

            button align (0.5, 0.5) xysize (int(247*2*interface_sampling), int(57*2*interface_sampling)):
                idle_background "images/interface/Player_menu/map_sublocation_idle.webp" hover_background "images/interface/Player_menu/map_sublocation.webp" selected_idle_background "images/interface/Player_menu/map_sublocation_selected.webp" selected_hover_background "images/interface/Player_menu/map_sublocation_selected.webp"

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

                text "Set QuikLoc 2" align (0.5, 0.5):
                    size 36

                    color "#000000"

            button align (0.5, 0.5) xysize (int(247*2*interface_sampling), int(57*2*interface_sampling)):
                idle_background "images/interface/Player_menu/map_sublocation_idle.webp" hover_background "images/interface/Player_menu/map_sublocation.webp" selected_idle_background "images/interface/Player_menu/map_sublocation_selected.webp" selected_hover_background "images/interface/Player_menu/map_sublocation_selected.webp"

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

                text "Set QuikLoc 3" align (0.5, 0.5):
                    size 36

                    color "#000000"

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
            
        add f"images/interface/Player_menu/map_institute_{map_to_show}.webp" align (0.5, 0.5)
    elif current_group == "Mall":
        if current_subgroup == "First Floor":
            $ map_to_show = "mall"
            
        add f"images/interface/Player_menu/map_mall.webp" align (0.5, 0.5)
        
    if map_to_show:
        if current_subgroup:
            for possible_location in location_groups[current_group][current_subgroup]:
                if possible_location in marked_locations.keys():
                    button anchor (0.5, 0.5):
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
                                        color "#000000" hover_color "#ffa903" selected_color "#ffa903"
                                    else:
                                        color "#bfbfbf"

                                    vertical True
                            elif possible_location in ["bg_mall"]:
                                text map_names[possible_location] anchor (0.5, 0.5) pos (0.65, 0.5):
                                    size 36

                                    if possible_location in available_locations.keys():
                                        color "#000000" hover_color "#ffa903" selected_color "#ffa903"
                                    else:
                                        color "#bfbfbf"

                                    vertical True
                            else:
                                text map_names[possible_location] align (0.5, 0.5):
                                    size 36

                                    if possible_location in available_locations.keys():
                                        color "#000000" hover_color "#ffa903" selected_color "#ffa903"
                                    else:
                                        color "#bfbfbf"
                        elif possible_location == "bg_Player":
                            idle_background f"images/interface/Player_menu/Player_{Player.background_color}_idle.webp" hover_background f"images/interface/Player_menu/Player_{Player.background_color}.webp" selected_idle_background f"images/interface/Player_menu/Player_{Player.background_color}.webp"
                        elif possible_location not in ["bg_Kurt", "bg_Charles"]:
                            if possible_location in available_locations.keys():
                                idle_background f"images/interface/Player_menu/{possible_location[3:]}_idle.webp" hover_background f"images/interface/Player_menu/{possible_location[3:]}.webp" selected_idle_background f"images/interface/Player_menu/{possible_location[3:]}.webp"
                            else:
                                background None
                        else:
                            background None

                            text map_names[possible_location] align (0.5, 0.5):
                                size 36

                                if possible_location in available_locations.keys():
                                    color "#000000" hover_color "#ffa903" selected_color "#ffa903"
                                else:
                                    color "#bfbfbf"

                        if possible_location == "bg_campus":
                            pos (0.622, 0.919) xysize (int(1000*2*interface_sampling), int(150*2*interface_sampling))
                        elif possible_location == "bg_classroom":
                            pos (0.83095, 0.3686) xysize (int(260*2*interface_sampling), int(210*2*interface_sampling))
                        elif possible_location == "bg_danger":
                            pos (0.414, 0.369) xysize (int(260*2*interface_sampling), int(215*2*interface_sampling))
                        elif possible_location == "bg_entrance":
                            pos (0.622, 0.7965) xysize (int(50*2*interface_sampling), int(50*2*interface_sampling))
                        elif possible_location == "bg_girls_hallway":
                            pos (0.4135, 0.561) xysize (int(50*2*interface_sampling), int(600*2*interface_sampling))
                        elif possible_location == "bg_hallway":
                            pos (0.8315, 0.561) xysize (int(50*2*interface_sampling), int(600*2*interface_sampling))
                        elif possible_location == Jean.home:
                            pos (0.370, 0.307) xysize (int(96*2*interface_sampling), int(71*2*interface_sampling))
                        elif possible_location == "bg_Kurt":
                            pos (0.788, 0.591) xysize (int(96*2*interface_sampling), int(71*2*interface_sampling))
                        elif possible_location == Laura.home:
                            pos (0.370, 0.591) xysize (int(96*2*interface_sampling), int(71*2*interface_sampling))
                        elif possible_location == "bg_lockers":
                            pos (0.497, 0.51) xysize (int(260*2*interface_sampling), int(150*2*interface_sampling))
                        elif possible_location == "bg_mall":
                            pos (0.51, 0.5915) xysize (int(80*2*interface_sampling), int(550*2*interface_sampling))
                        elif possible_location == "bg_movies":
                            pos (0.662, 0.48) xysize (int(150*2*interface_sampling), int(240*2*interface_sampling))
                        elif possible_location == "bg_Player":
                            pos (0.8735, 0.4495) xysize (int(96*2*interface_sampling), int(71*2*interface_sampling))
                        elif possible_location == "bg_pool":
                            pos (0.609, 0.306) xysize (int(450*2*interface_sampling), int(200*2*interface_sampling))
                        elif possible_location == Rogue.home:
                            pos (0.4555, 0.377) xysize (int(96*2*interface_sampling), int(71*2*interface_sampling))
                        elif possible_location == "bg_study":
                            pos (0.83095, 0.744) xysize (int(260*2*interface_sampling), int(240*2*interface_sampling))
                        elif possible_location == "bg_Charles":
                            pos (0.622, 0.475) xysize (int(350*2*interface_sampling), int(160*2*interface_sampling))

                        if possible_location in ["bg_girls_hallway", "bg_hallway"]:
                            vbox anchor (0.5, 1.0) pos (0.525, 0.9) xysize (int(44*2*interface_sampling), int(100*2*interface_sampling)):
                                for C in all_Characters:
                                    if C.location == possible_location:
                                        add At(f"images/interface/phone/icons/{C.tag}.webp", map_icon) align (0.5, 0.5)
                                    elif C.location == "nearby" and Player.location == possible_location:
                                        add At(f"images/interface/phone/icons/{C.tag}.webp", map_icon) align (0.5, 0.5)

                                if Player.location == possible_location:
                                    add At(f"images/interface/phone/icons/Player_{Player.background_color}.webp", map_icon) align (0.5, 0.5)

                            if marked_locations[possible_location]:
                                add At("images/interface/Player_menu/event_alert.webp", phone_icon) anchor (0.5, 0.0) pos (0.525, 0.25)
                        elif possible_location in ["bg_mall"]:
                            vbox anchor (0.5, 1.0) pos (0.55, 0.9) xysize (int(44*2*interface_sampling), int(100*2*interface_sampling)):
                                for C in all_Characters:
                                    if C.location == possible_location:
                                        add At(f"images/interface/phone/icons/{C.tag}.webp", map_icon) align (0.5, 0.5)
                                    elif C.location == "nearby" and Player.location == possible_location:
                                        add At(f"images/interface/phone/icons/{C.tag}.webp", map_icon) align (0.5, 0.5)

                                if Player.location == possible_location:
                                    add At(f"images/interface/phone/icons/Player_{Player.background_color}.webp", map_icon) align (0.5, 0.5)

                            if marked_locations[possible_location]:
                                add At("images/interface/Player_menu/event_alert.webp", phone_icon) anchor (0.5, 0.0) pos (0.55, 0.25)
                        else:
                            hbox anchor (0.5, 1.0) pos (0.5, 0.95):
                                if possible_location in bedrooms:
                                    xysize (int(60*2*interface_sampling), int(44*2*interface_sampling))

                                    spacing -25
                                else:
                                    xysize (int(100*2*interface_sampling), int(44*2*interface_sampling))

                                for C in all_Characters:
                                    if C.location == possible_location:
                                        add At(f"images/interface/phone/icons/{C.tag}.webp", map_icon) align (0.5, 0.5)
                                    elif C.location == "nearby" and Player.location == possible_location:
                                        add At(f"images/interface/phone/icons/{C.tag}.webp", map_icon) align (0.5, 0.5)

                                if Player.location == possible_location:
                                    add At(f"images/interface/phone/icons/Player_{Player.background_color}.webp", map_icon) align (0.5, 0.5)

                            if marked_locations[possible_location]:
                                add At("images/interface/Player_menu/event_alert.webp", phone_icon) anchor (0.5, 0.0) pos (0.5, 0.2)