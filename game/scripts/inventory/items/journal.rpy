init -1 python:

    def journal(Owner):
        name = "writing journal"
        string = "journal"

        shop_type = "gift"
        filter_type = "gifts"

        threshold = [50, 50]
        criteria = []

        description = "Simple but intimate."
        
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