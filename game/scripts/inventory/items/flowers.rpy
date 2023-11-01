init -1 python:

    def flowers(Owner):
        name = "bouqet of flowers"
        string = "flowers"

        shop_type = "gift"
        filter_type = "gifts"

        threshold = [100, 100]
        criteria = []

        description = "We guarantee that lucky someone will get the message!"
        
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