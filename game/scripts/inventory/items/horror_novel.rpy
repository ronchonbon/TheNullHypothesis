init -1 python:

    def horror_novel(Owner):
        name = "horror novel"
        string = "horror_novel"

        shop_type = "gift"
        filter_type = "gifts"

        threshold = [25, 25]
        criteria = []

        description = "A grisly tale that will leave your skin crawling. Don't read under any circumstance. Unless. . ."
        
        price = 0.5
        
        return ItemClass(
            Owner, 
            name, string,
            shop_type, 
            filter_type,
            threshold,
            criteria,
            description,
            price = int(price*work_unit*min(max(renpy.random.gauss(1.0, 0.15), 0.85), 1.15)))