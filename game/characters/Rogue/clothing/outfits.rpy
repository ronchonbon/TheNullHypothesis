init python:

    def default_Rogue_Outfits():
        Outfits = []
        
        Outfits.append(OutfitClass("Casual 1", wear_in_public = True))

        Outfits[-1].Clothes.update({
            "hair": Rogue_asymmetric_hair(),
            "bra": Rogue_black_tanktop(), "underwear": Rogue_yellow_panties()})
                
        return Outfits