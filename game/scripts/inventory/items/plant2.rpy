init -1 python:

    def plant2(Owner):
        name = "tall plant"
        string = "plant2"

        criteria = []

        shop_type = "gift"
        filter_type = "gifts"

        description = "Sure to make any room feel more vibrant and alive."
        
        price = 1
        
        return ItemClass(
            Owner, 
            name, string,
            criteria,
            shop_type, 
            filter_type,
            description,
            price = int(price*work_unit*min(max(renpy.random.gauss(1.0, 0.15), 0.85), 1.15)))