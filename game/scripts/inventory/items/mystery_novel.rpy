init -1 python:

    def mystery_novel(Owner):
        name = "mystery novel"
        string = "mystery_novel"

        shop_type = "gift"
        filter_type = "gifts"

        description = "A novel featuring an intricate and suspenseful mystery that will leave readers second-guessing everything. A perfect gift for the more 'cerebral' reader."
        
        price = 0.5
        
        return ItemClass(
            Owner, 
            name, string,
            shop_type, 
            filter_type,
            description,
            price = int(price*work_unit*min(max(renpy.random.gauss(1.0, 0.15), 0.85), 1.15)))