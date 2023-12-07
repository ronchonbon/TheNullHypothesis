init -1:

    default shop_inventory = {
        "clothing": {},
        "gift": {},
        "lingerie": {},
        "sex": {}}
    default current_shop_Item = None
    
    default unrestricted_shop_inventory = {
        "clothing": {},
        "gift": {},
        "lingerie": {},
        "sex": {}}

init python:

    import copy

style shop is default

style shop_button:
    idle_background Frame("images/interface/box1.webp", 10, 10)
    hover_background Frame("images/interface/box2.webp", 10, 10)

    padding (20, 20, 20, 20)

    xsize 0.2
    yminimum 0.07

style shop_text:
    font "agency_fb.ttf"

    color "#000000"

screen shop_screen(shop_type, discount = False, restricted = True):
    layer "interface"
    
    style_prefix "shop"

    on "show" action [
        SetVariable("belt_hidden", True),
        SetVariable("say_obscured", True),
        SetVariable("choice_disabled", True),
        SetVariable("Character_picker_disabled", True)]
    on "hide" action [
        SetVariable("belt_hidden", False),
        SetVariable("say_obscured", False),
        SetVariable("choice_disabled", False),
        SetVariable("Character_picker_disabled", False)]

    if discount:
        $ modifier = 0.5
    else:
        $ modifier = 1.0

    frame xysize (1041, 888) anchor (0.5, 0.5) pos (0.5, 0.55):
        background "images/interface/shop/shop.webp"

        if shop_type == "clothing":
            add "images/interface/shop/mutant_couture.webp" pos (0.03, -0.15)
        elif shop_type == "gift":
            add "images/interface/shop/bear_with_me.webp" pos (0.03, -0.15)
        elif shop_type == "lingerie":
            add "images/interface/shop/xtreme_intimates.webp" pos (0.03, -0.15)
        elif shop_type == "sex":
            add "images/interface/shop/moaning_of_life.webp" pos (0.03, -0.15)

        viewport id "shop_screen_viewport" anchor (0.5, 0.0) pos (0.297, 0.18) xysize (500, 620):
            draggable True
            mousewheel True

            xfill True

            vbox align (0.0, 0.0):
                spacing 5

                if restricted:
                    for I in shop_inventory[shop_type].values():
                        if not "piercing" in I.string or focused_Character in Present:
                            button xysize (490, 93):
                                idle_background "images/interface/shop/Item.webp" 
                                hover_background "images/interface/shop/Item_selected.webp" 
                                selected_idle_background "images/interface/shop/Item_selected.webp"
                                
                                selected current_shop_Item and current_shop_Item.Owner == I.Owner and current_shop_Item.string == I.string

                                action SetScreenVariable("current_shop_Item", copy.copy(I))

                                text f"{I.name}" anchor (0.0, 0.5) pos (0.01, 0.5) size 30

                                if discount:
                                    $ temp = int(modifier*I.price)

                                    text "{s}[I.price]{/s} [temp]" anchor (1.0, 0.5) pos (0.99, 0.5) size 30
                                else:
                                    text f"{I.price}" anchor (1.0, 0.5) pos (0.99, 0.5) size 30
                else:
                    for I in unrestricted_shop_inventory[shop_type].values():
                        if not "piercing" in I.string or focused_Character in Present:
                            button xysize (490, 93):
                                idle_background "images/interface/shop/Item.webp" 
                                hover_background "images/interface/shop/Item_selected.webp" 
                                selected_idle_background "images/interface/shop/Item_selected.webp"
                                
                                selected current_shop_Item and current_shop_Item.Owner == I.Owner and current_shop_Item.string == I.string

                                action SetScreenVariable("current_shop_Item", copy.copy(I))

                                text f"{I.name}" anchor (0.0, 0.5) pos (0.01, 0.5) size 30

                                if discount:
                                    $ temp = int(modifier*I.price)

                                    text "{s}[I.price]{/s} [temp]" anchor (1.0, 0.5) pos (0.99, 0.5) size 30
                                else:
                                    text f"{I.price}" anchor (1.0, 0.5) pos (0.99, 0.5) size 30

        vbar value YScrollValue("shop_screen_viewport") anchor (0.0, 0.0) pos (0.538, 0.178) xysize (22, 626):
            base_bar Frame("images/interface/wardrobe/scrollbar.webp")

            thumb "images/interface/wardrobe/scrollbar_thumb.webp"
            thumb_offset 10

            unscrollable "hide"

        text f"{Player.cash}" anchor (1.0, 0.5) pos (0.9, 0.554) size 44 

        if current_shop_Item:
            if shop_type in ["gift", "sex"]: 
                if current_shop_Item.string in Player.inventory.keys():
                    $ quantities = len(Player.inventory[current_shop_Item.string])
                elif "piercing" in current_shop_Item.string:
                    $ quantities = None
                else:
                    $ quantities = 0

                if quantities is not None:
                    add "images/interface/shop/quantity.webp" anchor (0.5, 0.5) pos (0.739, 0.663)

                    text f"{quantities}" anchor (1.0, 0.5) pos (0.82, 0.66) size 44

            if hasattr(current_shop_Item, "description"):
                text f"{current_shop_Item.description}" anchor (0.5, 0.5) pos (0.807, 0.19) xysize (300, 250) size 30
            elif shop_type == "clothing":
                add "images/interface/items/mutant_couture.webp" anchor (0.5, 0.5) pos (0.805, 0.19) zoom 1.2*item_adjustment
            elif shop_type == "lingerie":
                add "images/interface/items/xtreme_intimates.webp" anchor (0.5, 0.5) pos (0.805, 0.19) zoom 1.2*item_adjustment
        else:
            if shop_type in ["gift", "sex"]: 
                add "images/interface/shop/quantity.webp" anchor (0.5, 0.5) pos (0.739, 0.663)

        if current_shop_Item and (shop_type in ["clothing", "lingerie"] or current_shop_Item.filter_type == "key_gifts"):
            add At(f"images/interface/phone/icons/{current_shop_Item.Owner.tag}.webp", humhum_icon) anchor (0.5, 0.5) pos (0.93, 0.435)

        if shop_type in ["clothing", "lingerie"]:
            imagebutton anchor (0.5, 0.5) pos (0.737, 0.671):
                idle "images/interface/shop/try_idle.webp" 
                hover "images/interface/shop/try.webp"
                
                if current_shop_Item and current_shop_Item.Owner in Present:
                    action Call("ask_Character_to_try_on", current_shop_Item, from_current = True)
                else:
                    action None
                
                tooltip "Try On"

        imagebutton anchor (0.5, 0.5) pos (0.737, 0.805):
            idle "images/interface/shop/buy_idle.webp" 
            hover "images/interface/shop/buy.webp"
            
            if current_shop_Item and Player.cash >= int(modifier*current_shop_Item.price):
                if ongoing_Event:
                    if shop_type in ["clothing", "lingerie"]:
                        if current_shop_Item.string in shop_inventory[shop_type].keys():
                            action [
                                SetDict(Player.inventory, current_shop_Item.string, current_shop_Item),
                                SetVariable("Player.cash", Player.cash - int(modifier*current_shop_Item.price)),
                                Function(exec, f"del shop_inventory['{shop_type}']['{current_shop_Item.string}']"),
                                Function(exec, f"del unrestricted_shop_inventory['{shop_type}']['{current_shop_Item.string}']"),
                                SetScreenVariable("current_shop_Item", None),
                                SetVariable("inventory_alert", True),
                                Return(True)]
                        else:
                            action [
                                SetDict(Player.inventory, current_shop_Item.string, current_shop_Item),
                                SetVariable("Player.cash", Player.cash - int(modifier*current_shop_Item.price)),
                                Function(exec, f"del unrestricted_shop_inventory['{shop_type}']['{current_shop_Item.string}']"),
                                SetScreenVariable("current_shop_Item", None),
                                SetVariable("inventory_alert", True),
                                Return(True)]
                    elif current_shop_Item.filter_type == "key_gifts":
                        if current_shop_Item.string in shop_inventory[shop_type].keys():
                            action [
                                SetDict(Player.inventory, current_shop_Item.string, [current_shop_Item]),
                                SetVariable("Player.cash", Player.cash - int(modifier*current_shop_Item.price)),
                                Function(exec, f"del shop_inventory['{shop_type}']['{current_shop_Item.string}']"),
                                Function(exec, f"del unrestricted_shop_inventory['{shop_type}']['{current_shop_Item.string}']"),
                                SetScreenVariable("current_shop_Item", None),
                                SetVariable("inventory_alert", True),
                                Return(True)]
                        else:
                            action [
                                SetDict(Player.inventory, current_shop_Item.string, [current_shop_Item]),
                                SetVariable("Player.cash", Player.cash - int(modifier*current_shop_Item.price)),
                                Function(exec, f"del unrestricted_shop_inventory['{shop_type}']['{current_shop_Item.string}']"),
                                SetScreenVariable("current_shop_Item", None),
                                SetVariable("inventory_alert", True),
                                Return(True)]
                    else:
                        if current_shop_Item.string in Player.inventory.keys():
                            action [
                                AddToSet(Player.inventory[current_shop_Item.string], current_shop_Item),
                                SetVariable("Player.cash", Player.cash - int(modifier*current_shop_Item.price)),
                                SetScreenVariable("current_shop_Item", copy.copy(current_shop_Item)),
                                SetVariable("inventory_alert", True),
                                Return(True)]
                        else:
                            action [
                                SetDict(Player.inventory, current_shop_Item.string, [current_shop_Item]),
                                SetVariable("Player.cash", Player.cash - int(modifier*current_shop_Item.price)),
                                SetScreenVariable("current_shop_Item", copy.copy(current_shop_Item)),
                                SetVariable("inventory_alert", True),
                                Return(True)]
                else:
                    if "piercing" in current_shop_Item.string:
                        action Show("piercings_screen", Characters = Present, Piercing = current_shop_Item, discount = discount)
                    elif shop_type in ["gift", "sex"]:
                        action [
                            Show("buy_gift_screen", Characters = Present, Item = current_shop_Item, discount = discount),
                            SetScreenVariable("current_shop_Item", None)]
                    elif current_shop_Item.Owner not in Present:
                        if shop_type in ["clothing", "lingerie"]:
                            if current_shop_Item.string in shop_inventory[shop_type].keys():
                                action [
                                    SetDict(Player.inventory, current_shop_Item.string, current_shop_Item),
                                    SetVariable("Player.cash", Player.cash - int(modifier*current_shop_Item.price)),
                                    Function(exec, f"del shop_inventory['{shop_type}']['{current_shop_Item.string}']"),
                                    Function(exec, f"del unrestricted_shop_inventory['{shop_type}']['{current_shop_Item.string}']"),
                                    SetScreenVariable("current_shop_Item", None),
                                    SetVariable("inventory_alert", True)]
                            else:
                                action [
                                    SetDict(Player.inventory, current_shop_Item.string, current_shop_Item),
                                    SetVariable("Player.cash", Player.cash - int(modifier*current_shop_Item.price)),
                                    Function(exec, f"del unrestricted_shop_inventory['{shop_type}']['{current_shop_Item.string}']"),
                                    SetScreenVariable("current_shop_Item", None),
                                    SetVariable("inventory_alert", True)]
                        elif current_shop_Item.filter_type == "key_gifts":
                            if current_shop_Item.string in shop_inventory[shop_type].keys():
                                action [
                                    SetDict(Player.inventory, current_shop_Item.string, [current_shop_Item]),
                                    SetVariable("Player.cash", Player.cash - int(modifier*current_shop_Item.price)),
                                    Function(exec, f"del shop_inventory['{shop_type}']['{current_shop_Item.string}']"),
                                    Function(exec, f"del unrestricted_shop_inventory['{shop_type}']['{current_shop_Item.string}']"),
                                    SetScreenVariable("current_shop_Item", None),
                                    SetVariable("inventory_alert", True)]
                            else:
                                action [
                                    SetDict(Player.inventory, current_shop_Item.string, [current_shop_Item]),
                                    SetVariable("Player.cash", Player.cash - int(modifier*current_shop_Item.price)),
                                    Function(exec, f"del unrestricted_shop_inventory['{shop_type}']['{current_shop_Item.string}']"),
                                    SetScreenVariable("current_shop_Item", None),
                                    SetVariable("inventory_alert", True)]
                        else:
                            if current_shop_Item.string in Player.inventory.keys():
                                action [
                                    AddToSet(Player.inventory[current_shop_Item.string], current_shop_Item),
                                    SetVariable("Player.cash", Player.cash - int(modifier*current_shop_Item.price)),
                                    SetScreenVariable("current_shop_Item", copy.copy(current_shop_Item)),
                                    SetVariable("inventory_alert", True)]
                            else:
                                action [
                                    SetDict(Player.inventory, current_shop_Item.string, [current_shop_Item]),
                                    SetVariable("Player.cash", Player.cash - int(modifier*current_shop_Item.price)),
                                    SetScreenVariable("current_shop_Item", copy.copy(current_shop_Item)),
                                    SetVariable("inventory_alert", True)]
                    else:
                        action [
                            Function(renpy.call_in_new_context, "buy_Character_Clothing", current_shop_Item, discounted = discount),
                            SetScreenVariable("current_shop_Item", None)]
            else:
                action None

            tooltip "Buy"

        imagebutton anchor (0.5, 0.5) pos (0.9105, 0.7505):
            idle "images/interface/shop/back_idle.webp" 
            hover "images/interface/shop/back.webp"

            if ongoing_Event:
                action Return(False)
            else:
                action Call("debrief_Outfit_change", Present, instant = True, from_current = True)

            tooltip "Exit"

    if current_shop_Item and current_shop_Item.Owner in Present:
        add f"{current_shop_Item.Owner.tag}_sprite standing" anchor (current_shop_Item.Owner.sprite_anchor[0], current_shop_Item.Owner.sprite_anchor[1]) pos (0.85, eval(f"{current_shop_Item.Owner.tag}_standing_height")) zoom eval(f"{current_shop_Item.Owner.tag}_standing_zoom")
        
    if black_screen or renpy.get_screen("say"):
        button xysize (1.0, 1.0):
            background None
            
            if not renpy.get_screen("choice"):
                action Return()
            else:
                action NullAction()

    use quick_menu

    if tooltips_enabled:
        use tooltips

screen buy_gift_screen(Characters, Item, discount = False):
    style_prefix "shop"

    modal True

    if discount:
        $ modifier = 0.5
    else:
        $ modifier = 1.0

    frame xysize (0.25, 0.45):
        background Frame("images/interface/box1.webp", 10, 10)

        viewport id "buy_gift_screen_viewport" align (0.5, 0.5) xysize (0.8, 0.9):
            vbox align (0.5, 0.0) xsize 1.0:
                spacing 5

                text "Give to whom?" xsize 1.0:
                    size 36

                    color "#ffffff"

                if Item.string in Player.inventory.keys():
                    $ quantities = len(Player.inventory[Item.string])
                else:
                    $ quantities = 0

                for C in Characters:
                    if C in all_Companions and Item.string not in C.inventory.keys() and (not Item.Owner or Item.Owner == C):
                        textbutton f"{C.name}" xsize 1.0:
                            text_font "agency_fb.ttf"

                            action [
                                Hide("buy_gift_screen"),
                                Call("buy_Character_gift", C, Item, discounted = discount, from_current = True)]

                            text_size 36

                textbutton "Put in bag" xsize 1.0:
                    text_font "agency_fb.ttf"

                    if Item.filter_type == "key_gifts":
                        if Item.string in Player.inventory.keys():
                            action [
                                AddToSet(Player.inventory[Item.string], Item),
                                SetVariable("Player.cash", Player.cash - int(modifier*Item.price)),
                                Function(exec, f"del shop_inventory['{Item.shop_type}']['{Item.string}']"),
                                Function(exec, f"del unrestricted_shop_inventory['{Item.shop_type}']['{Item.string}']"),
                                SetVariable("inventory_alert", True),
                                Hide("buy_gift_screen")]
                        else:
                            action [
                                SetDict(Player.inventory, Item.string, [Item]),
                                SetVariable("Player.cash", Player.cash - int(modifier*Item.price)),
                                Function(exec, f"del shop_inventory['{Item.shop_type}']['{Item.string}']"),
                                Function(exec, f"del unrestricted_shop_inventory['{Item.shop_type}']['{Item.string}']"),
                                SetVariable("inventory_alert", True),
                                Hide("buy_gift_screen")]
                    else:
                        if Item.string in Player.inventory.keys():
                            action [
                                AddToSet(Player.inventory[Item.string], Item),
                                SetVariable("Player.cash", Player.cash - int(modifier*Item.price)),
                                SetVariable("inventory_alert", True),
                                Hide("buy_gift_screen")]
                        else:
                            action [
                                SetDict(Player.inventory, Item.string, [Item]),
                                SetVariable("Player.cash", Player.cash - int(modifier*Item.price)),
                                SetVariable("inventory_alert", True),
                                Hide("buy_gift_screen")]

                    text_size 36

                textbutton _("Cancel") xsize 1.0:
                    text_font "agency_fb.ttf"

                    action Hide("buy_gift_screen")

                    text_size 36

        vbar value YScrollValue("buy_gift_screen_viewport") anchor (0.0, 0.5) pos (0.925, 0.5) xsize 22 ysize 0.9:
            base_bar Frame("images/interface/wardrobe/scrollbar.webp")

            thumb "images/interface/wardrobe/scrollbar_thumb.webp"
            thumb_offset 10

            unscrollable "hide"

screen piercings_screen(Characters, Piercing, discount = False):
    style_prefix "shop"

    modal True

    frame xysize (0.25, 0.45):
        background Frame("images/interface/box1.webp", 10, 10)

        viewport id "piercings_screen_viewport" align (0.5, 0.5) xysize (0.8, 0.9):
            vbox align (0.5, 0.0) xsize 1.0:
                spacing 5

                text "Who should get a piercing?" xsize 1.0:
                    size 36

                    color "#ffffff"

                for C in Characters:
                    if C in all_Companions:
                        if Piercing.string not in C.inventory.keys():
                            textbutton f"{C.name}" xsize 1.0:
                                text_font "agency_fb.ttf"

                                action Call("give_Character_piercing", C, Piercing, mall = True, discounted = discount, from_current = True)

                                text_size 36

                textbutton _("Cancel") xsize 1.0:
                    text_font "agency_fb.ttf"

                    action Hide("piercings_screen")

                    text_size 36

        vbar value YScrollValue("piercings_screen_viewport") anchor (0.0, 0.5) pos (0.925, 0.5) xsize 22 ysize 0.9:
            base_bar Frame("images/interface/wardrobe/scrollbar.webp")

            thumb "images/interface/wardrobe/scrollbar_thumb.webp"
            thumb_offset 10

            unscrollable "hide"