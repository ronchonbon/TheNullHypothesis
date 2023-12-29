init -1:

    default shop_inventory = {
        "clothing": {},
        "gift": {},
        "lingerie": {},
        "sex": {}}
    default unrestricted_shop_inventory = {
        "clothing": {},
        "gift": {},
        "lingerie": {},
        "sex": {}}

    default current_shop_page = 0
    default current_shop_Item = None
    
    default shopping_cart = []

    default something_bought = False

init python:

    import copy

style shop is default

screen shop_screen(shop_type, discount = False, restricted = True):
    layer "interface"
    
    style_prefix "shop"

    on "show" action [
        SetVariable("current_shop_page", 0),
        SetVariable("current_shop_Item", None),
        SetVariable("shopping_cart", []),
        SetVariable("belt_hidden", True),
        SetVariable("say_obscured", True),
        SetVariable("choice_disabled", True),
        SetVariable("Character_picker_disabled", True)]
    on "hide" action [
        SetVariable("belt_hidden", False),
        SetVariable("say_obscured", False),
        SetVariable("choice_disabled", False),
        SetVariable("Character_picker_disabled", False)]

    timer 0.5 repeat True action ToggleVariable("blinking")

    if discount:
        $ modifier = 0.5
    else:
        $ modifier = 1.0

    add "images/interface/main_menu/blank_background.webp" zoom interface_new_adjustment

    add At("images/interface/preferences/spin.webp", spinning_element) anchor (0.5, 0.5) pos (0.502, 0.502) zoom interface_new_adjustment

    add "images/interface/shop/background.webp" zoom interface_new_adjustment

    if shop_type == "clothing":
        add "images/interface/shop/mutant_couture.webp" zoom interface_new_adjustment
    elif shop_type == "gift":
        add "images/interface/shop/bear_with_me.webp" zoom interface_new_adjustment
    elif shop_type == "lingerie":
        add "images/interface/shop/xtreme_intimates.webp" zoom interface_new_adjustment
    elif shop_type == "sex":
        add "images/interface/shop/moaning_of_life.webp" zoom interface_new_adjustment

    add "images/interface/shop/tab.webp" zoom interface_new_adjustment

    if restricted:
        $ shopping_list = list(shop_inventory[shop_type].values())
    else:
        $ shopping_list = list(unrestricted_shop_inventory[shop_type].values())

    imagebutton:
        idle At("images/interface/shop/left_idle.webp", interface) 
        hover At("images/interface/shop/left.webp", interface)
        
        if len(shopping_list) > 7:
            action SetScreenVariable("current_shop_page", (current_shop_page - 1) % math.ceil(len(shopping_list)/7))    
        else:
            action None

    if current_shop_page < 9:
        if blinking:
            text "TAB{alpha=0.0}_{/alpha}" + f"0{current_shop_page + 1}" anchor (0.5, 0.5) pos (0.186, 0.661):
                size 35
        else:
            text f"TAB_0{current_shop_page + 1}" anchor (0.5, 0.5) pos (0.186, 0.661):
                size 35
    else:
        if blinking:
            text "TAB{alpha=0.0}_{/alpha}" + f"{current_shop_page + 1}" anchor (0.5, 0.5) pos (0.186, 0.661):
                size 35
        else:
            text f"TAB_{current_shop_page + 1}" anchor (0.5, 0.5) pos (0.186, 0.661):
                size 35

    imagebutton:
        idle At("images/interface/shop/right_idle.webp", interface) 
        hover At("images/interface/shop/right.webp", interface)

        if len(shopping_list) > 7:
            action SetScreenVariable("current_shop_page", (current_shop_page + 1) % math.ceil(len(shopping_list)/7))    
        else:
            action None

    vbox anchor (0.5, 0.0) pos (0.546, 0.315) xysize (0.41, 0.6):
        spacing -5

        for i in range(7*current_shop_page, 7*current_shop_page + 7):
            if i <= len(shopping_list) - 1:
                $ I = shopping_list[i]
                
                $ quantity = 0
                $ removable_Item = None

                for I_temp in shopping_cart:
                    if I.Owner == I_temp.Owner and I.string == I_temp.string:
                        $ quantity += 1
                        $ removable_Item = I_temp

                fixed xysize (1.0, int(177*interface_new_adjustment)):
                    button anchor (0.0, 0.5) pos (0.0, 0.5) xysize (int(925*interface_new_adjustment), int(177*interface_new_adjustment)):
                        idle_background At("images/interface/shop/item_idle.webp", interface)
                        hover_background At("images/interface/shop/item.webp", interface) 
                        selected_idle_background At("images/interface/shop/item.webp", interface)

                        selected current_shop_Item and current_shop_Item.Owner == I.Owner and current_shop_Item.string == I.string

                        action SetScreenVariable("current_shop_Item", copy.copy(I))

                        text f"{I.name.upper()}" anchor (0.0, 0.5) pos (0.02, 0.5):
                            font "agency_fb.ttf"

                            size 30

                    add "images/interface/shop/price.webp" anchor (0.5, 0.5) pos (0.6735, 0.53) zoom interface_new_adjustment

                    if discount:
                        $ temp = int(modifier*I.price)

                        text "${s}[I.price]{/s} [temp]" anchor (0.5, 0.5) pos (0.6735, 0.53):
                            size 30
                    else:
                        text f"${I.price}" anchor (0.5, 0.5) pos (0.6735, 0.53):
                            size 30

                    imagebutton anchor (0.5, 0.5) pos (0.8068, 0.52):
                        idle At("images/interface/shop/plus_idle.webp", interface)
                        hover At("images/interface/shop/plus.webp", interface)

                        action AddToSet(shopping_cart, copy.copy(I))

                    add "images/interface/shop/quantity.webp" anchor (0.5, 0.5) pos (0.88, 0.53) zoom interface_new_adjustment

                    text f"{quantity}" anchor (0.5, 0.5) pos (0.88, 0.53):
                        size 30

                    imagebutton anchor (1.0, 0.5) pos (1.0, 0.52):
                        idle At("images/interface/shop/minus_idle.webp", interface)
                        hover At("images/interface/shop/minus.webp", interface)

                        if removable_Item:
                            action RemoveFromSet(shopping_cart, removable_Item)
                        else:
                            action None

    # if blinking:
    text "CASH" + "{alpha=0.0}_{/alpha}" anchor (0.0, 0.5) pos (0.065, 0.586):
        size 36
    # else:
    #     text Character.Outfit.name.upper() + "_" anchor (0.0, 0.5) pos (0.242, 0.063):
    #         size 32

    text f"${Player.cash}" anchor (1.0, 0.5) pos (0.318, 0.586):
        size 36

    $ total_cost = 0

    for I in shopping_cart:
        $ total_cost += I.price

    $ total_cost = int(total_cost*modifier)

    # if blinking:
    text "TOTAL" + "{alpha=0.0}_{/alpha}" anchor (0.0, 0.5) pos (0.505, 0.91):
        size 36
    # else:
    #     text Character.Outfit.name.upper() + "_" anchor (0.0, 0.5) pos (0.242, 0.063):
    #         size 32

    text f"${total_cost}" anchor (1.0, 0.5) pos (0.745, 0.91):
        size 36

    imagebutton:
        idle At("images/interface/shop/buy_idle.webp", interface)
        hover At("images/interface/shop/buy.webp", interface)

        if shopping_cart and Player.cash >= total_cost:
            action [
                SetVariable("something_bought", True),
                SetVariable("Player.cash", Player.cash - total_cost),
                Function(buy_shopping_cart, cart = shopping_cart),
                SetVariable("shopping_cart", []),
                SetVariable("inventory_alert", True)]
        else:
            action None

        tooltip "Buy Cart"

    text "BUY" anchor (0.5, 0.5) pos (0.367, 0.91):
        size 36

    imagebutton:
        idle At("images/interface/shop/clear_idle.webp", interface)
        hover At("images/interface/shop/clear.webp", interface)

        action SetVariable("shopping_cart", [])

        tooltip "Clear Cart"

    text "CLEAR" anchor (0.5, 0.5) pos (0.445, 0.91):
        size 36

    imagebutton:
        idle At("images/interface/shop/quit_idle.webp", interface)
        hover At("images/interface/shop/quit.webp", interface)

        action [
            Hide("shop_screen"),
            Return(something_bought)]

        tooltip "Exit"

    text "DONE" anchor (0.0, 0.5) pos (0.065, 0.738):
        size 36

    # if blinking:
    text "ITEM DESCRIPTION" + "{alpha=0.0}_{/alpha}" anchor (0.0, 0.5) pos (0.776, 0.336):
        size 36
    # else:
    #     text Character.Outfit.name.upper() + "_" anchor (0.0, 0.5) pos (0.242, 0.063):
    #         size 32

    # if blinking:
    text "FAVORITE" + "{alpha=0.0}_{/alpha}" anchor (0.0, 0.5) pos (0.776, 0.683):
        size 36
    # else:
    #     text Character.Outfit.name.upper() + "_" anchor (0.0, 0.5) pos (0.242, 0.063):
    #         size 32

    # if blinking:
    text "OWNED" + "{alpha=0.0}_{/alpha}" anchor (0.0, 0.5) pos (0.776, 0.91):
        size 36
    # else:
    #     text Character.Outfit.name.upper() + "_" anchor (0.0, 0.5) pos (0.242, 0.063):
    #         size 32

    if current_shop_Item:
        if hasattr(current_shop_Item, "description"):
            text f"{current_shop_Item.description}" anchor (0.5, 0.5) pos (0.851, 0.507) xysize (0.159, 0.235):
                size 30

        if shop_type in ["clothing", "lingerie"] or current_shop_Item.filter_type == "key_gifts":
            add f"images/interface/phone/icons/{current_shop_Item.Owner.tag}.webp" anchor (0.5, 0.5) pos (0.851, 0.797) zoom 0.5

        if current_shop_Item.string in Player.inventory.keys():
            text f"{len(Player.inventory[current_shop_Item.string])}" anchor (1.0, 0.5) pos (0.926, 0.91):
                size 36
        else:
            text "0" anchor (1.0, 0.5) pos (0.926, 0.91):
                size 36

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