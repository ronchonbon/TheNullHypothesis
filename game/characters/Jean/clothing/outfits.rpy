init python:

    def default_Jean_Outfits():
        Outfits = []
        
        Outfits.append(OutfitClass("Casual 1", wear_in_public = True))

        Outfits[-1].Clothes.update({
            "hair": Jean_straight_hair(),
            "bra": Jean_pink_bra(), "underwear": Jean_pink_boyshorts(),
            "pants": Jean_khaki_pants(),
            "top": Jean_pink_top()})

        Outfits.append(OutfitClass("Hero (Chapter I)", superwear = True))

        Outfits[-1].Clothes.update({
            "face_inner_accessory": Jean_blue_mask(), "hair": Jean_straight_hair(),
            "bra": Jean_pink_bra(), "underwear": Jean_pink_boyshorts(),
            "bodysuit": Jean_blueyellow_classic_suit(),
            "boots": Jean_blue_boots(),
            "gloves": Jean_blue_gloves(), "sleeves": Jean_blue_gauntlets()})

        Outfits.append(OutfitClass("Swimsuit (One-Piece)", swimwear = True))

        Outfits[-1].Clothes.update({
            "hair": Jean_straight_hair(),
            "bodysuit": Jean_red_swimsuit()})

        Outfits.append(OutfitClass("Pajamas 1", sleepwear = True))

        Outfits[-1].Clothes.update({
            "hair": Jean_straight_hair(),
            "bra": Jean_pink_bra(), "underwear": Jean_pink_boyshorts()})

        Outfits.append(OutfitClass("Nude"))

        Outfits[-1].Clothes.update({
            "hair": Jean_straight_hair()})

        return Outfits