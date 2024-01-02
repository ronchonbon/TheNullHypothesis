init -1 python:

    def teddy_bear(Owner):
        name = "teddy bear"
        string = "teddy_bear"

        shop_type = "gift"
        filter_type = "gifts"

        description = "A plush brown teddy bear. Perfect for gifting or snuggling."
        
        price = 1
        
        return ItemClass(
            Owner, 
            name, string,
            shop_type, 
            filter_type,
            description,
            price = int(price*work_unit*min(max(renpy.random.gauss(1.0, 0.15), 0.85), 1.15)))