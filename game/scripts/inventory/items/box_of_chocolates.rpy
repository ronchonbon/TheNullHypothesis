init -1 python:

    def box_of_chocolates(Owner):
        name = "box of chocolates"
        string = "box_of_chocolates"

        shop_type = "gift"
        filter_type = "gifts"

        description = "A box of handmade, gourmet chocolates. An assortment of delicious flavors without any of that crappy fruity filling."
        
        price = 0.5
        
        return ItemClass(
            Owner, 
            name, string,
            shop_type, 
            filter_type,
            description,
            price = int(price*work_unit*min(max(renpy.random.gauss(1.0, 0.15), 0.85), 1.15)))