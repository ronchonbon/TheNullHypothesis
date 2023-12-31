label give_Character_gift(Character, Item):
    hide screen Player_menu

    $ temp_Character_picker_disabled = Character_picker_disabled

    $ Character_picker_disabled = True

    if Item.Owner and Item.Owner != Character:
        "Pretty sure you bought that with someone else in mind."

        show screen interactions_screen(Character)
        
        return

    if ("piercing" in Item.string or "plug" in Item.string) and Item.string in Character.inventory.keys():
        "She already owns this."

        show screen interactions_screen(Character)

        return

    if "plant" in Item.string:
        $ Item_string = "plant"
    else:
        $ Item_string = Item.string

    if (Item.shop_type in ["sex", "lingerie"] and approval_check(Character, threshold = Item.threshold, extra_condition = "sexy_gifts")) or approval_check(Character, threshold = Item.threshold):
        if Item.string not in Character.inventory.keys():
            call expression f"{Character.tag}_{Item_string}_gift_accept" from _call_expression_239
        else:
            $ _return = True

        if _return:
            $ Item.Owner = Character

            if Item.string in Character.inventory.keys():
                $ Character.inventory[Item.string].append(Item)
            else:
                $ Character.inventory[Item.string] = [Item]

            if len(Player.inventory[Item.string]) > 1:
                $ Player.inventory[Item.string].remove(Item)
            else:
                $ del Player.inventory[Item.string]
                
            $ Player.History.update("gave_gift")
            
            $ Character.History.update(f"given_{Item_string}")
        else:
            $ Character.History.update(f"said_no_to_{Item_string}")
    else:
        if Character.History.check(f"said_no_to_{Item_string}", tracker = "recent") >= 2:
            call change_Character_stat(Character, "love", -5) from _call_change_Character_stat_979
            call change_Character_stat(Character, "trust", -5) from _call_change_Character_stat_980

            call expression f"{Character.tag}_rejected_gift_twice" from _call_expression_241
        elif Character.History.check(f"said_no_to_{Item_string}", tracker = "recent") == 1:
            call change_Character_stat(Character, "love", -2) from _call_change_Character_stat_981

            call expression f"{Character.tag}_rejected_gift_once" from _call_expression_242
        else:
            call expression f"{Character.tag}_{Item_string}_gift_reject" from _call_expression_243

        $ Character.History.update(f"said_no_to_{Item_string}")

    $ Character_picker_disabled = temp_Character_picker_disabled

    if Character.location == Player.location:
        show screen interactions_screen(Character)

    return