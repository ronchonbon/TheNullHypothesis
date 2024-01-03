init -1 python:

    def baseball_flag(Owner):
        name = "Mississipi Braves flag"
        string = "baseball_flag"

        criteria = []

        shop_type = "gift"
        filter_type = "key_gifts"

        description = "Show your team spirit!"
        
        price = 0.5
        
        return ItemClass(
            Owner, 
            name, string,
            criteria,
            shop_type, 
            filter_type,
            description,
            price = int(price*work_unit*min(max(renpy.random.gauss(1.0, 0.15), 0.85), 1.15)))