init -1 python:

    def motorcycle_helmet(Owner):
        name = "motorcycle helmet"
        string = "motorcycle_helmet"

        shop_type = "gift"
        filter_type = "key_gifts"

        description = "Your brain will thank you - looking this good is just a bonus."
        
        price = 8
        
        return ItemClass(
            Owner, 
            name, string,
            shop_type, 
            filter_type,
            description,
            price = int(price*work_unit*min(max(renpy.random.gauss(1.0, 0.15), 0.85), 1.15)))