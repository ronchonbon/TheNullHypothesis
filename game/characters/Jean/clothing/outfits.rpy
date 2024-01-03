init python:

    def default_Jean_Outfits():
        Outfits = []
        
        Outfits.append(OutfitClass("Casual 1", flags = ["public", "day"]))

        Outfits[-1].Clothes.update({
            "hair": Jean_straight_hair(),
            "bra": Jean_pink_bra(), "underwear": Jean_pink_boyshorts(),
            "pants": Jean_khaki_pants(), "footwear": Jean_black_sandals(),
            "top": Jean_pink_top()})

        Outfits.append(OutfitClass("Hero (Chapter I)", flags = ["hero"]))

        Outfits[-1].Clothes.update({
            "face_inner_accessory": Jean_blue_mask(), "hair": Jean_straight_hair(),
            "bra": Jean_pink_bra(), "underwear": Jean_pink_boyshorts(),
            "bodysuit": Jean_blueyellow_classic_suit(),
            "footwear": Jean_blue_boots(),
            "gloves": Jean_blue_gloves(), "sleeves": Jean_blue_gauntlets()})

        Outfits.append(OutfitClass("Swimsuit (One-Piece)", flags = ["swim"]))

        Outfits[-1].Clothes.update({
            "hair": Jean_straight_hair(),
            "bodysuit": Jean_red_swimsuit()})

        Outfits.append(OutfitClass("Pajamas 1", flags = ["sleep"]))

        Outfits[-1].Clothes.update({
            "hair": Jean_straight_hair(),
            "bra": Jean_pink_bra(), "underwear": Jean_pink_boyshorts()})

        Outfits.append(OutfitClass("Nude"))

        Outfits[-1].Clothes.update({
            "hair": Jean_straight_hair()})

        return Outfits