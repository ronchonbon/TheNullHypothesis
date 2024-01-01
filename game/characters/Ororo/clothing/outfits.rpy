init python:

    def default_Ororo_Outfits():
        Outfits = []
        
        Outfits.append(OutfitClass("Casual 1", flags = ["public", "day"]))

        Outfits[-1].Clothes.update({
            "hair": Ororo_ponytail()})

        return Outfits