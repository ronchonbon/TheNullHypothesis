init -1 python:

    def watercolors(Owner):
        name = "watercolor set"
        string = "watercolors"

        criteria = []

        shop_type = "gift"
        filter_type = "gifts"

        description = "A thoughtful and expressive gift - good choice!"
        
        price = 2
        
        return ItemClass(
            Owner, 
            name, string,
            criteria,
            shop_type, 
            filter_type,
            description,
            price = int(price*work_unit*min(max(renpy.random.gauss(1.0, 0.15), 0.85), 1.15)))