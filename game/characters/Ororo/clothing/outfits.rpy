init python:

    def default_Ororo_Outfits():
        Outfits = []
        
        Outfits.append(OutfitClass("Casual 1", flags = ["public", "day"]))

        Outfits[-1].Clothes.update({
            "hair": Ororo_ponytail(),
            "pants": Ororo_black_pants(), "footwear": Ororo_black_pumps(),
            "top": Ororo_white_top()})

        Outfits.append(OutfitClass("Hero (Chapter I)", flags = ["hero"]))

        Outfits[-1].Clothes.update({
            "face_inner_accessory": Ororo_black_mask(), "hair": Ororo_ponytail(),
            "bodysuit": Ororo_black_classic_suit(),
            "footwear": Ororo_black_boots(),
            "gloves": Ororo_black_gloves(),
            "cloak": Ororo_black_cape()})

        return Outfits