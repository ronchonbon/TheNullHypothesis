init -1 python:

    def record_player(Owner):
        name = "record player"
        string = "record_player"

        shop_type = "gift"
        filter_type = "key_gifts"

        threshold = [0, 0]
        criteria = []

        description = "You're not sure you can hear a difference in sound quality, but you sure can feel the admiration of everyone around you."
        
        price = 4
        
        return ItemClass(
            Owner, 
            name, string,
            shop_type, 
            filter_type,
            threshold,
            criteria,
            description,
            price = int(price*work_unit*min(max(renpy.random.gauss(1.0, 0.15), 0.85), 1.15)))