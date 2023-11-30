init python:

    def all_Items():
        Items = [
            barbell_labia_piercings(None),
            barbell_nipple_piercings(None),
            belly_piercing(None),
            box_of_chocolates(None),
            candle(None),
            # coffee(None),
            combat_manual(None),
            designer_purse(None),
            dildo(None),
            # flowers(None),
            # flowery_perfume(None),
            # fruity_perfume(None),
            heart_anal_plug(None),
            horror_novel(None),
            # journal(None),
            mystery_novel(None),
            plant1(None),
            plant2(None),
            plant3(None),
            remote_vibrator(None),
            ring_labia_piercings(None),
            ring_nipple_piercings(None),
            round_anal_plug(None),
            # spicy_perfume(None),
            steamy_romance_novel(None),
            # tea(None),
            teddy_bear(None),
            vibrator(None),
            # watercolors(None),
            wholesome_romance_novel(None)]

        return Items

    def register_Items():
        global shop_inventory

        Items = all_Items()

        for I in Items:
            if I.string not in shop_inventory[I.shop_type].keys():
                unlocked = True

                for criterion in I.criteria:
                    if not eval(criterion):
                        unlocked = False

                if unlocked:
                    shop_inventory[I.shop_type][I.string] = I
                    unrestricted_shop_inventory[I.shop_type][I.string] = I

        for C in all_Companions:
            Items = eval(f"{C.tag}_special_Items()")

            for I in Items:
                if I.string in Player.inventory.keys() and Player.inventory[I.string][0].Owner == C:
                    continue

                if I.string in C.inventory.keys():
                    continue

                if I.string not in shop_inventory[I.shop_type].keys():
                    unlocked = True

                    for criterion in I.criteria:
                        if not eval(criterion):
                            unlocked = False

                    if unlocked:
                        shop_inventory[I.shop_type][I.string] = I
                        unrestricted_shop_inventory[I.shop_type][I.string] = I

        return