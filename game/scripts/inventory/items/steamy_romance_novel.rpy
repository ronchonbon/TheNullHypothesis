init -1 python:

    def steamy_romance_novel(Owner):
        name = "steamy romance novel"
        string = "steamy_romance_novel"

        criteria = []

        shop_type = "gift"
        filter_type = "gifts"

        description = "An erotic love story filled to the brim with passion. Perfect gift for that special someone who enjoys things to be more explicit."
        
        price = 0.5
        
        return ItemClass(
            Owner, 
            name, string,
            criteria,
            shop_type, 
            filter_type,
            description,
            price = int(price*work_unit*min(max(renpy.random.gauss(1.0, 0.15), 0.85), 1.15)))