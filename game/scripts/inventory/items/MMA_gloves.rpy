init -1 python:

    def MMA_gloves(Owner):
        name = "MMA gloves"
        string = "MMA_gloves"

        shop_type = "gift"
        filter_type = "key_gifts"

        description = "Professional quality 4-ounce MMA gloves. Sturdy leather with comfortable knuckle protection."
        
        price = 5
        
        return ItemClass(
            Owner, 
            name, string,
            shop_type, 
            filter_type,
            description,
            price = int(price*work_unit*min(max(renpy.random.gauss(1.0, 0.15), 0.85), 1.15)))