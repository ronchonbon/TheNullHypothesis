init -1 python:

    def remote_vibrator(Owner):
        name = "remote-control vibrator"
        string = "remote_vibrator"

        shop_type = "sex"
        filter_type = "gifts"

        threshold = [900, 900]
        criteria = []

        description = "A hands-free insertable vibrator. Perfect for wearing long-term, just control it with your smartphone!"
        
        price = 4
        
        return ItemClass(
            Owner, 
            name, string,
            shop_type, 
            filter_type,
            threshold,
            criteria,
            description,
            price = int(price*work_unit*min(max(renpy.random.gauss(1.0, 0.15), 0.85), 1.15)))