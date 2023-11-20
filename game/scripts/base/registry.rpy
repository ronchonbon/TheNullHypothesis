init python:

    def register_Characters():
        global all_Characters
        global all_Girls

        global chapter
        global season

        global shop_inventory
        global unrestricted_shop_inventory

        test = eval(f"PlayerClass('John', 'Doe', voice = ch_Player)")

        for attribute in test.__dict__.keys():
            if attribute not in Player.__dict__.keys():
                setattr(Player, attribute, test.__dict__[attribute])

        for C in all_Characters:
            if C in all_Girls:
                test = eval(f"GirlClass('{C.tag}', voice = ch_{C.tag}, love = 0, trust = 0, desire = 0)")

                for attribute in test.__dict__.keys():
                    if attribute not in C.__dict__.keys():
                        setattr(C, attribute, test.__dict__[attribute])

                if game_started:
                    set_default_Outfits(C, change = False)
                else:
                    set_default_Outfits(C, change = True)

                Clothing_list = eval(f"all_{C.tag}_Clothes()")

                temp_Clothing_list = list(C.Wardrobe.Clothes.keys())

                for I in temp_Clothing_list:
                    found = False

                    for I_A in Clothing_list:
                        if I == I_A.name:
                            found = True

                            break

                    if not found:
                        del C.Wardrobe.Clothes[I]

                for I in Clothing_list:
                    if I.name in C.Wardrobe.Clothes.keys() or "hair" in I.name:
                        if "hair" not in I.name:
                            I.selected_state = C.Wardrobe.Clothes[I.name].selected_state

                        C.Wardrobe.Clothes[I.name] = copy.copy(I)

                        for O in C.Wardrobe.Outfits.values():
                            if I.string == O.Clothes[I.Clothing_type].string:
                                if "hair" not in I.name:
                                    I.selected_state = O.Clothes[I.Clothing_type].selected_state
                                    
                                O.Clothes[I.Clothing_type] = copy.copy(I)

                Clothing_list = eval(f"{C.tag}_shopping_list()")

                for I in Clothing_list:
                    if I.name not in C.Wardrobe.Clothes.keys() and I.string not in Player.inventory:
                        if chapter >= I.chapter and season >= I.season:
                            shop_inventory[I.shop_type][I.string] = copy.copy(I)

                        unrestricted_shop_inventory[I.shop_type][I.string] = copy.copy(I)
            elif C in all_NPCs:
                test = eval(f"NPCClass('{C.tag}', voice = ch_{C.tag})")

                for attribute in test.__dict__.keys():
                    if attribute not in C.__dict__.keys():
                        setattr(C, attribute, test.__dict__[attribute])

        return

    def register_Events():
        global Cast

        global EventScheduler
        
        Events = []

        for C in Cast:
            Character_Events = eval(f"all_{C}_Events()")

            for E in Character_Events:
                Events.append(E)

        additional_Events = all_Events()

        for E in additional_Events:
            Events.append(E)

        for E in Events:
            EventScheduler.add_Event(E)

        return

    def register_Quests():
        global QuestPool
        
        Quests = []

        for C in Cast:
            Character_Quests = eval(f"all_{C}_Quests()")

            for Q in Character_Quests:
                Quests.append(Q)

        additional_Quests = all_Quests()

        for Q in additional_Quests:
            Quests.append(Q)

        Quest_strings = list(QuestPool.Quests.keys())

        for Q_string in Quest_strings:
            absent = True

            for Q in Quests:
                if Q_string == Q.string:
                    absent = False

                    break

            if absent:
                del QuestPool.Quests[Q_string]

        for Q in Quests:
            QuestPool.add_Quest(Q)

        return