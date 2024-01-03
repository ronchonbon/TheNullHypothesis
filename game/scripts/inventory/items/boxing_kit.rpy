init -1 python:

    def boxing_kit(Owner):
        name = "boxing kit"
        string = "boxing_kit"

        criteria = []

        shop_type = "gift"
        filter_type = "key_gifts"

        description = "Resilient against the most aggressive of routines or your money back!"
        
        price = 5
        
        return ItemClass(
            Owner, 
            name, string,
            criteria,
            shop_type, 
            filter_type,
            description,
            price = int(price*work_unit*min(max(renpy.random.gauss(1.0, 0.15), 0.85), 1.15)))