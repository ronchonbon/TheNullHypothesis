init -1 python:

    def occult_posters(Owner):
        name = "occult posters"
        string = "occult_posters"

        shop_type = "gift"
        filter_type = "key_gifts"

        description = "You're not like the rest of them, huh?"
        
        price = 0.25
        
        return ItemClass(
            Owner, 
            name, string,
            shop_type, 
            filter_type,
            description,
            price = int(price*work_unit*min(max(renpy.random.gauss(1.0, 0.15), 0.85), 1.15)))