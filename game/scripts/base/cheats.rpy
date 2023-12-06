init -1:

    default cheats_unlocked = False

label enter_cheat_code(code):
    $ parsed_code = code.split("_")

    if parsed_code[0] == "give" and len(parsed_code) > 1:
        if parsed_code[1] == "cash" and len(parsed_code) == 3:
            $ Player.cash += eval("parsed_code[2]")

            if Player.cash < 0:
                $ Player.cash = 0 
        elif parsed_code[1] in Cast and len(parsed_code) == 4:
            if parsed_code[2] == "all" and parsed_code[3] == "Clothes":
                $ Character = None

                python:
                    for C in all_Companions:
                        if C.tag == parsed_code[1]:
                            Character = C
                
                if Character:
                    python:
                        Clothing_list = eval(f"all_{parsed_code[1]}_Clothes()")

                        for I in Clothing_list:
                            Character.give(I)

                            if I.shop_type in shop_inventory.keys() and I in shop_inventory[I.shop_type]:
                                shop_inventory[I.shop_type].remove(I)
                                unrestricted_shop_inventory[I.shop_type].remove(I)
            
                    $ set_default_Outfits(Character, change = False)
    elif parsed_code[0] == "change" and len(parsed_code) > 1:
        if parsed_code[1] in Cast and len(parsed_code) == 4:
            if parsed_code[2] in ["love", "trust", "desire"]:
                $ Character = None

                python:
                    for C in all_Companions:
                        if C.tag == parsed_code[1]:
                            Character = C

                if Character:
                    call change_Character_stat(Character, parsed_code[2], int(parsed_code[3])) from _call_change_Character_stat_834
    elif parsed_code[0] == "max" and parsed_code[1] == "Character" and parsed_code[2] == "stats":
        $ renpy.dynamic(temp_Characters = active_Companions[:])

        while temp_Characters:
            call change_Character_stat(temp_Characters[0], "love", 1000) from _call_change_Character_stat_835
            call change_Character_stat(temp_Characters[0], "trust", 1000) from _call_change_Character_stat_836

            $ temp_Characters.remove(temp_Characters[0])

    return