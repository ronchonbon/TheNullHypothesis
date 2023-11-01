init -1 python:

    def plant1(Owner):
        name = "short plant"
        string = "plant1"

        shop_type = "gift"
        filter_type = "gifts"

        threshold = [100, 100]
        criteria = []

        description = "Sure to make any room feel more vibrant and alive."
        
        price = 0.25
        
        return ItemClass(
            Owner, 
            name, string,
            shop_type, 
            filter_type,
            threshold,
            criteria,
            description,
            price = int(price*work_unit*min(max(renpy.random.gauss(1.0, 0.15), 0.85), 1.15)))