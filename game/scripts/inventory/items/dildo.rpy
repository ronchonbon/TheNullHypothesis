init -1 python:

    def dildo(Owner):
        name = "dildo"
        string = "dildo"

        criteria = []

        shop_type = "sex"
        filter_type = "gifts"

        description = "Simple and easy-to-use with a smooth, inviting texture. Don't worry, it can't replace you. Yet."
        
        price = 1
        
        return ItemClass(
            Owner, 
            name, string,
            criteria,
            shop_type, 
            filter_type,
            description,
            price = int(price*work_unit*min(max(renpy.random.gauss(1.0, 0.15), 0.85), 1.15)))