init -1 python:

    def belly_piercing(Owner):
        name = "belly piercing"
        string = "belly_piercing"

        shop_type = "sex"
        filter_type = "gifts"

        threshold = [500, 500]
        criteria = []

        # description = "All piercings are done in house by a certified body piercer. Don't worry, she's very gentle."
        description = "Non-toxic and made to last: the perfect gift to spice up that special someone's look."

        price = 3
        
        return ItemClass(
            Owner, 
            name, string,
            shop_type, 
            filter_type,
            threshold,
            criteria,
            description,
            price = int(price*work_unit*min(max(renpy.random.gauss(1.0, 0.15), 0.85), 1.15)))