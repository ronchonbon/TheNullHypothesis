init -1 python:

    def tea(Owner):
        name = "imported tea"
        string = "tea"

        criteria = []

        shop_type = "gift"
        filter_type = "gifts"

        description = "Sophistication comes easy when you're paying this much for hot floral water."
        
        price = 2
        
        return ItemClass(
            Owner, 
            name, string,
            criteria,
            shop_type, 
            filter_type,
            description,
            price = int(price*work_unit*min(max(renpy.random.gauss(1.0, 0.15), 0.85), 1.15)))