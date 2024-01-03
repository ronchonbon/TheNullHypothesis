init -1 python:

    def barbell_nipple_piercings(Owner):
        name = "barbell nipple piercings"
        string = "barbell_nipple_piercings"

        criteria = []

        shop_type = "sex"
        filter_type = "gifts"

        # description = "All piercings are done in house by a certified body piercer. Don't worry, she's very gentle."
        description = "Non-toxic and made to last: the perfect gift to spice up that special someone's look."

        price = 4
        
        return ItemClass(
            Owner, 
            name, string,
            criteria,
            shop_type, 
            filter_type,
            description,
            price = int(price*work_unit*min(max(renpy.random.gauss(1.0, 0.15), 0.85), 1.15)))