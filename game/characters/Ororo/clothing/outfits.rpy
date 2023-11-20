init python:

    def default_Ororo_Outfits():
        Outfits = []
        
        Outfits.append(OutfitClass("Casual 1", wear_in_public = True))

        Outfits[-1].Clothes.update({
            "hair": Ororo_ponytail()})

        return Outfits