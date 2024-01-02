init -1 python:

    def electric_guitar(Owner):
        name = "electric guitar"
        string = "electric_guitar"

        shop_type = None
        filter_type = "key_gifts"

        description = "A candy-red Stratocaster. Enough said."
        
        price = 15
        
        return ItemClass(
            Owner, 
            name, string,
            shop_type, 
            filter_type,
            description,
            price = int(price*work_unit*min(max(renpy.random.gauss(1.0, 0.15), 0.85), 1.15)))