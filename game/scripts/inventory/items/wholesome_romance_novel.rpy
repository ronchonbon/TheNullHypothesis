init -1 python:

    def wholesome_romance_novel(Owner):
        name = "wholesome romance novel"
        string = "wholesome_romance_novel"

        shop_type = "gift"
        filter_type = "gifts"

        description = "A heartwarming story about true love persevering. Perfect gift for that special someone who enjoys a wholesome love story."
        
        price = 0.5
        
        return ItemClass(
            Owner, 
            name, string,
            shop_type, 
            filter_type,
            description,
            price = int(price*work_unit*min(max(renpy.random.gauss(1.0, 0.15), 0.85), 1.15)))