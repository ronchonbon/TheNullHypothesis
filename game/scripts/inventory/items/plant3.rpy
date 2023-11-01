init -1 python:

    def plant3(Owner):
        name = "big plant"
        string = "plant3"

        shop_type = "gift"
        filter_type = "gifts"

        threshold = [200, 200]
        criteria = []

        description = "Sure to make any room feel more vibrant and alive."
        
        price = 1.5
        
        return ItemClass(
            Owner, 
            name, string,
            shop_type, 
            filter_type,
            threshold,
            criteria,
            description,
            price = int(price*work_unit*min(max(renpy.random.gauss(1.0, 0.15), 0.85), 1.15)))