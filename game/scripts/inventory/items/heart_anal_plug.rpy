init -1 python:

    def heart_anal_plug(Owner):
        name = "heart gem anal plug"
        string = "heart_anal_plug"

        criteria = []

        shop_type = "sex"
        filter_type = "gifts"

        description = "A set of polished aluminum anal plugs. The set comes with 4 different sizes and a variety of different gem colors."
        
        price = 3
        
        return ItemClass(
            Owner, 
            name, string,
            criteria,
            shop_type, 
            filter_type,
            description,
            price = int(price*work_unit*min(max(renpy.random.gauss(1.0, 0.15), 0.85), 1.15)))