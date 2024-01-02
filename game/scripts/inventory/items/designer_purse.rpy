init -1 python:

    def designer_purse(Owner):
        name = "designer purse"
        string = "designer_purse"

        shop_type = "gift"
        filter_type = "gifts"

        description = "Fine craftsmanship operating on the cutting edge of fashion. Show that special someone that you know they're an icon."
        
        price = 10
        
        return ItemClass(
            Owner, 
            name, string,
            shop_type, 
            filter_type,
            description,
            price = int(price*work_unit*min(max(renpy.random.gauss(1.0, 0.15), 0.85), 1.15)))
