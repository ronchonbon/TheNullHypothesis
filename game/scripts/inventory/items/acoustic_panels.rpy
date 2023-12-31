init -1 python:

    def acoustic_panels(Owner):
        name = "acoustic panels"
        string = "acoustic_panels"

        shop_type = None
        filter_type = "key_gifts"

        threshold = [0, 0]
        criteria = []

        description = "Helps preserve the sonic integrity of any room."
        
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