init -1 python:

    def round_anal_plug(Owner):
        name = "round gem anal plug"
        string = "round_anal_plug"

        shop_type = "sex"
        filter_type = "gifts"

        threshold = [800, 800]
        criteria = []

        description = "A set of polished aluminum anal plugs. The set comes with 4 different sizes and a variety of different gem colors."
        
        price = 1
        
        return ItemClass(
            Owner, 
            name, string,
            shop_type, 
            filter_type,
            threshold,
            criteria,
            description,
            price = int(price*work_unit*min(max(renpy.random.gauss(1.0, 0.15), 0.85), 1.15)))