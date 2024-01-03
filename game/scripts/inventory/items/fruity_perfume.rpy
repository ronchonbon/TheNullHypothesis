init -1 python:

    def fruity_perfume(Owner):
        name = "fruity perfume"
        string = "fruity_perfume"

        criteria = []

        shop_type = "gift"
        filter_type = "gifts"

        description = "Nothing says you know someone like the gift of their favorite scent."
        
        price = 7
        
        return ItemClass(
            Owner, 
            name, string,
            criteria,
            shop_type, 
            filter_type,
            description,
            price = int(price*work_unit*min(max(renpy.random.gauss(1.0, 0.15), 0.85), 1.15)))