init -1 python:

    def coffee(Owner):
        name = "premium coffee beans"
        string = "coffee"

        shop_type = "gift"
        filter_type = "gifts"

        threshold = [50, 50]
        criteria = []

        description = "Who says waking up can't be luxurious?"
        
        price = 2
        
        return ItemClass(
            Owner, 
            name, string,
            shop_type, 
            filter_type,
            threshold,
            criteria,
            description,
            price = int(price*work_unit*min(max(renpy.random.gauss(1.0, 0.15), 0.85), 1.15)))