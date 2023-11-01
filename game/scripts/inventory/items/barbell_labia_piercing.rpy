init -1 python:

    def barbell_labia_piercings(Owner):
        name = "barbell labia piercing"
        string = "barbell_labia_piercings"

        shop_type = "sex"
        filter_type = None

        threshold = [950, 950]
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