init -1 python:

    def acoustic_guitar(Owner):
        name = "acoustic guitar"
        string = "acoustic_guitar"

        shop_type = "gift"
        filter_type = "key_gifts"

        threshold = [0, 0]
        criteria = []

        description = "A gorgeous acoustic guitar with mahogany body and ebony fretboard."
        
        price = 10
        
        return ItemClass(
            Owner, 
            name, string,
            shop_type, 
            filter_type,
            threshold,
            criteria,
            description,
            price = int(price*work_unit*min(max(renpy.random.gauss(1.0, 0.15), 0.85), 1.15)))