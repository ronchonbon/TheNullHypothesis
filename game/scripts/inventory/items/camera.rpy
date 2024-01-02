init -1 python:

    def camera(Owner):
        name = "DLSR"
        string = "camera"

        shop_type = "gift"
        filter_type = "key_gifts"

        description = "Capture your most precious moments like a pro!"
        
        price = 7
        
        return ItemClass(
            Owner, 
            name, string,
            shop_type, 
            filter_type,
            description,
            price = int(price*work_unit*min(max(renpy.random.gauss(1.0, 0.15), 0.85), 1.15)))