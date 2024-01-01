init python:

    def default_Laura_Outfits():
        Outfits = []
        
        Outfits.append(OutfitClass("Casual 1", flags = ["public", "day"]))

        Outfits[-1].Clothes.update({
            "hair": Laura_straight_hair()})
                
        return Outfits