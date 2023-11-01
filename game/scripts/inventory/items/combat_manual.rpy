init -1 python:

    def combat_manual(Owner):
        name = "hand-to-hand combat manual"
        string = "combat_manual"

        shop_type = "gift"
        filter_type = "gifts"

        threshold = [25, 25]
        criteria = []

        description = "A no-frills guide to assessing and disabling (almost) any threat to your personhood. Erm, mutanthood?"
        
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