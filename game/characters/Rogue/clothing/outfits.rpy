init python:

    def default_Rogue_Outfits():
        Outfits = []
        
        Outfits.append(OutfitClass("Casual 1", wear_in_public = True))

        Outfits[-1].Clothes.update({
            "hair": Rogue_asymmetric_hair(),
            "bra": Rogue_black_tanktop(), "underwear": Rogue_yellow_panties(),
            "pants": Rogue_black_jeans(),
            "top": Rogue_black_lowcut_top()})

        Outfits.append(OutfitClass("Workout 1", activewear = True))

        Outfits[-1].Clothes.update({
            "hair": Rogue_asymmetric_hair(),
            "bra": Rogue_black_sports_bra(), "underwear": Rogue_yellow_panties(),
            "pants": Rogue_green_athletic_shorts()})

        Outfits.append(OutfitClass("Swimsuit (Bikini)", swimwear = True))

        Outfits[-1].Clothes.update({
            "hair": Rogue_asymmetric_hair(),
            "bra": Rogue_green_bikini_top(), "underwear": Rogue_green_bikini_bottoms()})

        Outfits.append(OutfitClass("Pajamas 1", sleepwear = True))

        Outfits[-1].Clothes.update({
            "hair": Rogue_asymmetric_hair(),
            "bra": Rogue_black_tanktop(), "underwear": Rogue_yellow_panties()})
                
        return Outfits