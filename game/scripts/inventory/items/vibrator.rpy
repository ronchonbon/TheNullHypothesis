init -1 python:

    def vibrator(Owner):
        name = "vibrator"
        string = "vibrator"

        shop_type = "sex"
        filter_type = "gifts"

        threshold = [600, 600]
        criteria = []

        description = "A simple-to-use handheld vibrator. For that special someone who could use a more personal massage."
        
        price = 5
        
        return ItemClass(
            Owner, 
            name, string,
            shop_type, 
            filter_type,
            threshold,
            criteria,
            description,
            price = int(price*work_unit*min(max(renpy.random.gauss(1.0, 0.15), 0.85), 1.15)))