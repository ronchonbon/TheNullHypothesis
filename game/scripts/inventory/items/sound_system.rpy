init -1 python:

    def sound_system(Owner):
        name = "Hi-Fi sound system"
        string = "sound_system"

        shop_type = None
        filter_type = "key_gifts"

        description = "Stop being the butt of all your audiophile friends' jokes - upgrade today!"
        
        price = 8
        
        return ItemClass(
            Owner, 
            name, string,
            shop_type, 
            filter_type,
            description,
            price = int(price*work_unit*min(max(renpy.random.gauss(1.0, 0.15), 0.85), 1.15)))