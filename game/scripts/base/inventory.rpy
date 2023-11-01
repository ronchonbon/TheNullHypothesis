init python:

    class ItemClass(object):
        def __init__(self, Owner, name, string, shop_type, filter_type, threshold, criteria, description, **properties):
            self.Owner = Owner

            self.name = name
            self.string = string

            self.shop_type = shop_type
            self.filter_type = filter_type

            self.threshold = threshold
            self.criteria = criteria

            self.description = description

            self.price = properties.get("price", 0)