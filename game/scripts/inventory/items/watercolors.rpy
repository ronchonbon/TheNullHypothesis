init -1 python:

    def watercolors(Owner):
        name = "watercolor set"
        string = "watercolors"

        shop_type = "gift"
        filter_type = "gifts"

        threshold = [85, 85]
        criteria = []

        description = "A thoughtful and expressive gift - good choice!"
        
        price = 2
        
        return ItemClass(
            Owner, 
            name, string,
            shop_type, 
            filter_type,
            threshold,
            criteria,
            description,
            price = int(price*work_unit*min(max(renpy.random.gauss(1.0, 0.15), 0.85), 1.15)))