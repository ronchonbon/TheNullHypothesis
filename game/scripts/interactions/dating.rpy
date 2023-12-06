default eating_dinner = False
default ordered_food = False
default food_arrived = False
default drinking_wine = False

default chosen_meal = {}
default restaurant_bill = {}

label restaurant_menu(menu_Characters, cuisine):
    if menu_Characters == Player or menu_Characters in all_Companions:
        $ menu_Characters = [menu_Characters]

    while menu_Characters:
        while menu_Characters[0] not in chosen_meal.keys():
            if cuisine == "steakhouse":
                menu:
                    extend ""
                    "Steak ($45)":
                        menu:
                            extend ""
                            "Filet Mignon":
                                $ chosen_meal[menu_Characters[0]] = "filet mignon"
                                $ restaurant_bill[menu_Characters[0]] = 45
                            "Ribeye":
                                $ chosen_meal[menu_Characters[0]] = "ribeye"
                                $ restaurant_bill[menu_Characters[0]] = 45
                            "Back":
                                pass
                    "Chilean Sea Bass ($35)":
                        $ chosen_meal[menu_Characters[0]] = "Chilean sea bass"
                        $ restaurant_bill[menu_Characters[0]] = 35
                    "Penne alla Vodka ($30)":
                        $ chosen_meal[menu_Characters[0]] = "penne alla vodka"
                        $ restaurant_bill[menu_Characters[0]] = 30
                    "Chicken Parmesan ($25)":
                        $ chosen_meal[menu_Characters[0]] = "chicken parmesan"
                        $ restaurant_bill[menu_Characters[0]] = 25
                    "Chopped Salad ($15)" if menu_Characters[0] != Laura:
                        $ chosen_meal[menu_Characters[0]] = "chopped salad"
                        $ restaurant_bill[menu_Characters[0]] = 15
                    "Chopped Salad ($15) (locked)" if menu_Characters[0] == Laura:
                        pass
            elif cuisine == "seafood":
                menu:
                    extend ""
                    "Twin Lobster Tails ($45)":
                        $ chosen_meal[menu_Characters[0]] = "lobster tails"
                        $ restaurant_bill[menu_Characters[0]] = 45
                    "Crab-Stuffed Sole ($35)":
                        $ chosen_meal[menu_Characters[0]] = "crab-stuffed sole"
                        $ restaurant_bill[menu_Characters[0]] = 35
                    "Jumbo Lump Crab Cakes ($30)":
                        $ chosen_meal[menu_Characters[0]] = "crab cakes"
                        $ restaurant_bill[menu_Characters[0]] = 30
                    "Pan-seared Salmon ($25)":
                        $ chosen_meal[menu_Characters[0]] = "salmon"
                        $ restaurant_bill[menu_Characters[0]] = 25
                    "Garden Salad ($15)" if menu_Characters[0] != Laura:
                        $ chosen_meal[menu_Characters[0]] = "garden salad"
                        $ restaurant_bill[menu_Characters[0]] = 15
                    "Garden Salad ($15) (locked)" if menu_Characters[0] == Laura:
                        pass
            elif cuisine == "southern":
                menu:
                    extend ""
                    "Braised Short Ribs ($45)":
                        $ chosen_meal[menu_Characters[0]] = "short ribs"
                        $ restaurant_bill[menu_Characters[0]] = 45
                    "Catfish ($35)":
                        $ chosen_meal[menu_Characters[0]] = "catfish"
                        $ restaurant_bill[menu_Characters[0]] = 35
                    "Jambalaya ($30)":
                        $ chosen_meal[menu_Characters[0]] = "jambalaya"
                        $ restaurant_bill[menu_Characters[0]] = 30
                    "Fried Chicken ($25)":
                        $ chosen_meal[menu_Characters[0]] = "fried chicken"
                        $ restaurant_bill[menu_Characters[0]] = 25
                    "Wild Greens Salad ($15)" if menu_Characters[0] != Laura:
                        $ chosen_meal[menu_Characters[0]] = "salad"
                        $ restaurant_bill[menu_Characters[0]] = 15
                    "Wild Greens Salad ($15) (locked)" if menu_Characters[0] == Laura:
                        pass

        $ menu_Characters.remove(menu_Characters[0])

    return