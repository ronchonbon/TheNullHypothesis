init -1 python:

    def ring_nipple_piercings(Owner):
        name = "ring nipple piercings"
        string = "ring_nipple_piercings"

        shop_type = "sex"
        filter_type = None

        threshold = [750, 750]
        criteria = []

        description = "All piercings are done in house by a certified body piercer. Don't worry, she's very gentle."
        
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