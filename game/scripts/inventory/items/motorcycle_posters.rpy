init -1 python:

    def motorcycle_posters(Owner):
        name = "motorcycle posters"
        string = "motorcycle_posters"

        shop_type = "gift"
        filter_type = "key_gifts"

        description = "Gain respect and admiration for your appreciation of the classics!"
        
        price = 0.25
        
        return ItemClass(
            Owner, 
            name, string,
            shop_type, 
            filter_type,
            description,
            price = int(price*work_unit*min(max(renpy.random.gauss(1.0, 0.15), 0.85), 1.15)))