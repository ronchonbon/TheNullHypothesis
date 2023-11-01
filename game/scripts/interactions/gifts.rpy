label buy_Girl_gift(Girl, Item, discounted = False):
    if "plant" in Item.string:
        $ Item_string = "plant"
    else:
        $ Item_string = Item.string

    if (Item.shop_type in ["sex", "lingerie"] and approval_check(Girl, threshold = Item.threshold, extra_condition = "sexy_gifts")) or approval_check(Girl, threshold = Item.threshold):
        $ Item.Owner = Girl
            
        if Item.string not in Girl.inventory.keys():
            call expression f"{Girl.tag}_{Item_string}_shopping_accept" from _call_expression_234
        else:
            $ _return = True

        if _return:
            if discounted:
                $ Player.cash -= int(0.5*Item.price)
            else:
                $ Player.cash -= Item.price

            if Item.string in Girl.inventory.keys():
                $ Girl.inventory[Item.string].append(Item)
            else:
                $ Girl.inventory[Item.string] = [Item]

            if Item.filter_type == "key_gifts":
                $ del shop_inventory[Item.shop_type][Item.string]
                $ del unrestricted_shop_inventory[Item.shop_type][Item.string]

            $ Girl.History.update(f"given_{Item_string}")
        else:
            $ Item.Owner = None
            
            $ Girl.History.update(f"said_no_to_{Item_string}")
    else:
        if Girl.History.check(f"said_no_to_{Item_string}", tracker = "recent") >= 2:
            call change_Girl_stat(Girl, "love", -5) from _call_change_Girl_stat_976
            call change_Girl_stat(Girl, "trust", -5) from _call_change_Girl_stat_977

            call expression f"{Girl.tag}_rejected_gift_twice" from _call_expression_236
        elif Girl.History.check(f"said_no_to_{Item_string}", tracker = "recent") == 1:
            call change_Girl_stat(Girl, "love", -2) from _call_change_Girl_stat_978

            call expression f"{Girl.tag}_rejected_gift_once" from _call_expression_237
        else:
            call expression f"{Girl.tag}_{Item_string}_shopping_reject" from _call_expression_238

        $ Girl.History.update(f"said_no_to_{Item_string}")

    return

label give_Girl_gift(Girl, Item):
    hide screen Player_menu

    $ temp_Character_picker_disabled = Character_picker_disabled

    $ Character_picker_disabled = True

    if Item.Owner and Item.Owner != Girl:
        "Pretty sure you bought that with someone else in mind."

        show screen interactions_screen(Girl)
        
        return

    if ("piercing" in Item.string or "plug" in Item.string) and Item.string in Girl.inventory.keys():
        "She already owns this."

        show screen interactions_screen(Girl)

        return

    if "plant" in Item.string:
        $ Item_string = "plant"
    else:
        $ Item_string = Item.string

    if (Item.shop_type in ["sex", "lingerie"] and approval_check(Girl, threshold = Item.threshold, extra_condition = "sexy_gifts")) or approval_check(Girl, threshold = Item.threshold):
        if Item.string not in Girl.inventory.keys():
            call expression f"{Girl.tag}_{Item_string}_gift_accept" from _call_expression_239
        else:
            $ _return = True

        if _return:
            $ Item.Owner = Girl

            if Item.string in Girl.inventory.keys():
                $ Girl.inventory[Item.string].append(Item)
            else:
                $ Girl.inventory[Item.string] = [Item]

            if len(Player.inventory[Item.string]) > 1:
                $ Player.inventory[Item.string].remove(Item)
            else:
                $ del Player.inventory[Item.string]
                
            $ Girl.History.update(f"given_{Item_string}")
        else:
            $ Girl.History.update(f"said_no_to_{Item_string}")
    else:
        if Girl.History.check(f"said_no_to_{Item_string}", tracker = "recent") >= 2:
            call change_Girl_stat(Girl, "love", -5) from _call_change_Girl_stat_979
            call change_Girl_stat(Girl, "trust", -5) from _call_change_Girl_stat_980

            call expression f"{Girl.tag}_rejected_gift_twice" from _call_expression_241
        elif Girl.History.check(f"said_no_to_{Item_string}", tracker = "recent") == 1:
            call change_Girl_stat(Girl, "love", -2) from _call_change_Girl_stat_981

            call expression f"{Girl.tag}_rejected_gift_once" from _call_expression_242
        else:
            call expression f"{Girl.tag}_{Item_string}_gift_reject" from _call_expression_243

        $ Girl.History.update(f"said_no_to_{Item_string}")

    $ Character_picker_disabled = temp_Character_picker_disabled

    if Girl.location == Player.location:
        show screen interactions_screen(Girl)

    return