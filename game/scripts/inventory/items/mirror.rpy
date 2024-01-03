init -1 python:

    def mirror(Owner):
        name = "stand-up mirror"
        string = "mirror"

        criteria = []

        shop_type = "gift"
        filter_type = "key_gifts"

        description = "Everyone loves a gift that's just the right amount of suggestive."
        
        price = 4
        
        return ItemClass(
            Owner, 
            name, string,
            criteria,
            shop_type, 
            filter_type,
            description,
            price = int(price*work_unit*min(max(renpy.random.gauss(1.0, 0.15), 0.85), 1.15)))