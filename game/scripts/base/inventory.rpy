init python:

    class ItemClass(object):
        def __init__(self, Owner, name, string, criteria, shop_type, filter_type, description, **properties):
            self.Owner = Owner

            self.name = name
            self.string = string

            self.criteria = criteria

            self.shop_type = shop_type
            self.filter_type = filter_type

            self.description = description

            self.price = properties.get("price", 0)