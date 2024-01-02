init -1 python:

    def candle(Owner):
        name = "scented candle"
        string = "candle"

        shop_type = "gift"
        filter_type = "gifts"

        description = "An aesthetically-pleasing decoration with a subtle and balanced scent. Show them you really know their unique tastes."
        
        price = 1
        
        return ItemClass(
            Owner, 
            name, string,
            shop_type, 
            filter_type,
            description,
            price = int(price*work_unit*min(max(renpy.random.gauss(1.0, 0.15), 0.85), 1.15)))