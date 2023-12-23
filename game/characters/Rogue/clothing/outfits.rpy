init python:

    def default_Rogue_Outfits():
        Outfits = []
        
        Outfits.append(OutfitClass("Casual 1", wear_in_public = True))

        Outfits[-1].Clothes.update({
            "hair": Rogue_asymmetric_hair(),
            "bra": Rogue_black_tanktop(), "underwear": Rogue_yellow_panties(),
            "pants": Rogue_black_jeans(), "footwear": Rogue_black_strap_pumps(),
            "top": Rogue_black_lowcut_top(),
            "gloves": Rogue_black_gloves(), "sleeves": Rogue_black_spiked_bracelets()})

        Outfits.append(OutfitClass("Hero (Chapter I)", superwear = True))

        Outfits[-1].Clothes.update({
            "face_inner_accessory": Rogue_green_headband(), "hair": Rogue_asymmetric_hair(),
            "bra": Rogue_black_sports_bra(), "underwear": Rogue_yellow_panties(),
            "bodysuit": Rogue_greenyellow_classic_suit(),
            "footwear": Rogue_yellow_classic_boots(),
            "gloves": Rogue_yellow_gloves(), "belt": Rogue_brown_utility_belt(),
            "jacket": Rogue_brown_classic_jacket()})

        Outfits.append(OutfitClass("Swimsuit (Bikini)", swimwear = True))

        Outfits[-1].Clothes.update({
            "hair": Rogue_asymmetric_hair(),
            "bra": Rogue_green_bikini_top(), "underwear": Rogue_green_bikini_bottoms()})

        Outfits.append(OutfitClass("Pajamas 1", sleepwear = True))

        Outfits[-1].Clothes.update({
            "hair": Rogue_asymmetric_hair(),
            "bra": Rogue_black_tanktop(), "underwear": Rogue_yellow_panties()})

        Outfits.append(OutfitClass("Nude"))

        Outfits[-1].Clothes.update({
            "hair": Rogue_asymmetric_hair()})
                
        return Outfits