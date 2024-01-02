init python:
    
    def buy_shopping_cart(cart):
        for I in cart:
            if I.shop_type in ["clothing", "lingerie"]:
                Player.inventory[I.string] = I

                if I.string in shop_inventory[I.shop_type].keys():
                    del shop_inventory[I.shop_type][I.string]

                del unrestricted_shop_inventory[I.shop_type][I.string]
            elif I.filter_type == "key_gifts":
                Player.inventory[I.string] = [I]

                if I.string in shop_inventory[I.shop_type].keys():
                    del shop_inventory[I.shop_type][I.string]

                del unrestricted_shop_inventory[I.shop_type][I.string]
            elif I.string in Player.inventory.keys():
                Player.inventory[I.string].append(I)
            else:
                Player.inventory[I.string] = [I]

        return

label buy_Character_gift(Character, Item, discounted = False):
    if "plant" in Item.string:
        $ Item_string = "plant"
    else:
        $ Item_string = Item.string

    if (Item.shop_type in ["sex", "lingerie"] and approval_check(Character, threshold = eval(f"{Character.tag}_gift_thresholds[Item.string]"), extra_condition = "sexy_gifts")) or approval_check(Character, threshold = eval(f"{Character.tag}_gift_thresholds[Item.string]")):
        $ Item.Owner = Character
            
        if Item.string not in Character.inventory.keys():
            call expression f"{Character.tag}_{Item_string}_shopping_accept" from _call_expression_234

            call change_Character_stat(Character, "love", eval(f"{Character.tag}_gift_bonuses[Item.string]")[0])
            call change_Character_stat(Character, "trust", eval(f"{Character.tag}_gift_bonuses[Item.string]")[1])
        else:
            $ _return = True

        if _return:
            if discounted:
                $ Player.cash -= int(0.5*Item.price)
            else:
                $ Player.cash -= Item.price

            if Item.string in Character.inventory.keys():
                $ Character.inventory[Item.string].append(Item)
            else:
                $ Character.inventory[Item.string] = [Item]

            if Item.filter_type == "key_gifts":
                $ del shop_inventory[Item.shop_type][Item.string]
                $ del unrestricted_shop_inventory[Item.shop_type][Item.string]

            $ Character.History.update(f"given_{Item_string}")
        else:
            $ Item.Owner = None
            
            $ Character.History.update(f"said_no_to_{Item_string}")
    else:
        if Character.History.check(f"said_no_to_{Item_string}", tracker = "recent") >= 2:
            call change_Character_stat(Character, "love", -5) from _call_change_Character_stat_976
            call change_Character_stat(Character, "trust", -5) from _call_change_Character_stat_977

            call expression f"{Character.tag}_rejected_gift_twice" from _call_expression_236
        elif Character.History.check(f"said_no_to_{Item_string}", tracker = "recent") == 1:
            call change_Character_stat(Character, "love", -2) from _call_change_Character_stat_978

            call expression f"{Character.tag}_rejected_gift_once" from _call_expression_237
        else:
            call expression f"{Character.tag}_{Item_string}_shopping_reject" from _call_expression_238

        $ Character.History.update(f"said_no_to_{Item_string}")

    return

label buy_Character_Clothing(Clothing, discounted = False):
    $ Character = Clothing.Owner

    if (Clothing.shop_type in ["sex", "lingerie"] and approval_check(Character, threshold = Clothing.thresholds["accept"], extra_condition = "sexy_gifts")) or approval_check(Character, threshold = Clothing.thresholds["accept"]):
        call expression f"{Character.tag}_{Clothing.string}_shopping_accept" from _call_expression_149

        if discounted:
            $ Player.cash -= int(0.5*Clothing.price)
        else:
            $ Player.cash -= Clothing.price

        $ Clothing.gift = True

        $ Character.give(Clothing)
            
        $ set_default_Outfits(Character, change = False)

        if Clothing.string in shop_inventory[Clothing.shop_type].keys():
            $ del shop_inventory[Clothing.shop_type][Clothing.string]
            $ del unrestricted_shop_inventory[Clothing.shop_type][Clothing.string]
    else:
        if Character.History.check(f"said_no_to_{Clothing.string}", tracker = "recent") >= 2:
            call change_Character_stat(Character, "love", -5) from _call_change_Character_stat_943
            call change_Character_stat(Character, "trust", -5) from _call_change_Character_stat_944

            call expression f"{Character.tag}_rejected_Clothing_twice" from _call_expression_151
        elif Character.History.check(f"said_no_to_{Clothing.string}", tracker = "recent") == 1:
            call change_Character_stat(Character, "love", -2) from _call_change_Character_stat_945

            call expression f"{Character.tag}_rejected_Clothing_once" from _call_expression_152
        else:
            call expression f"{Character.tag}_{Clothing.string}_shopping_reject" from _call_expression_153

        $ Character.History.update(f"said_no_to_{Clothing.string}")

    return