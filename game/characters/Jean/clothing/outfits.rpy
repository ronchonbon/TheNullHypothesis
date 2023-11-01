init python:

    def default_Jean_Outfits():
        Outfits = []
        
        Outfits.append(OutfitClass("Casual 1", wear_in_public = True))

        Outfits[-1].Clothes.update({
            "hair": Jean_long_hair(),
            "bra": Jean_pink_bra(), "underwear": Jean_pink_panties(),
            "pants": Jean_khaki_pants(),
            "top": Jean_pink_shirt()})

        Outfits.append(OutfitClass("Casual 2", wear_in_public = True))

        Outfits[-1].Clothes.update({
            "hair": Jean_long_hair(),
            "bra": Jean_pink_bra(), "underwear": Jean_pink_panties(),
            "socks": Jean_black_socks(), "skirt": Jean_blue_pleated_skirt(),
            "top": Jean_college_shirt(),
            "neck": Jean_white_necklace(),
            "jacket": Jean_denim_jacket()})

        Clothes = {
            "hair": Jean_long_hair(),
            "bra": Jean_pink_bra(), "underwear": Jean_pink_boyshorts(),
            "pants": Jean_khaki_pants(),
            "top": Jean_college_shirt(),
            "jacket": Jean_denim_jacket()}

        if check_if_Clothes_in_Wardrobe(Jean, Clothes):
            Outfits.append(OutfitClass("Casual 3", wear_in_public = True))

            Outfits[-1].Clothes.update(Clothes)

        Clothes = {
            "hair": Jean_long_hair(),
            "bra": Jean_black_balconette_bra(), "underwear": Jean_black_thong(),
            "pants": Jean_black_pants(),
            "top": Jean_college_shirt()}

        if check_if_Clothes_in_Wardrobe(Jean, Clothes):
            Outfits.append(OutfitClass("Casual 4", wear_in_public = True))

            Outfits[-1].Clothes.update(Clothes)

        Clothes = {
            "hair": Jean_long_hair(),
            "bra": Jean_blue_lace_bra(), "underwear": Jean_blue_lace_panties(),
            "pants": Jean_black_pants(),
            "top": Jean_white_cami(),
            "jacket": Jean_denim_jacket()}

        if check_if_Clothes_in_Wardrobe(Jean, Clothes):
            Outfits.append(OutfitClass("Casual 5", wear_in_public = True))

            Outfits[-1].Clothes.update(Clothes)

        Outfits.append(OutfitClass("Winter 1 (Indoor)", wear_in_public = True))

        Outfits[-1].Clothes.update({
            "hair": Jean_long_hair(),
            "bra": Jean_pink_bra(), "underwear": Jean_pink_panties(),
            "pants": Jean_khaki_pants(),
            "top": Jean_white_sweater()})

        Outfits.append(OutfitClass("Winter 1 (Outdoor)", wear_in_public = True, winterwear = True))

        Outfits[-1].Clothes.update({
            "hair": Jean_long_hair(), "face_outer_accessory": Jean_white_hat(),
            "bra": Jean_pink_bra(), "underwear": Jean_pink_panties(),
            "pants": Jean_khaki_pants(),
            "top": Jean_white_sweater(),
            "neck": Jean_maroon_scarf(),
            "jacket": Jean_puffy_jacket()})

        Clothes = {
            "hair": Jean_long_hair(),
            "bra": Jean_pink_bra(), "underwear": Jean_pink_boyshorts(),
            "pants": Jean_black_pants(),
            "top": Jean_black_shirt()}

        if check_if_Clothes_in_Wardrobe(Jean, Clothes):
            Outfits.append(OutfitClass("Winter 2 (Indoor)", wear_in_public = True))

            Outfits[-1].Clothes.update(Clothes)

        Clothes = {
            "hair": Jean_long_hair(), "face_outer_accessory": Jean_white_hat(),
            "bra": Jean_pink_bra(), "underwear": Jean_pink_boyshorts(),
            "pants": Jean_black_pants(),
            "top": Jean_black_shirt(),
            "jacket": Jean_puffy_jacket()}

        if check_if_Clothes_in_Wardrobe(Jean, Clothes):
            Outfits.append(OutfitClass("Winter 2 (Outdoor)", wear_in_public = True, winterwear = True))

            Outfits[-1].Clothes.update(Clothes)

        Clothes = {
            "hair": Jean_long_hair(),
            "bra": Jean_red_corset(), "underwear": Jean_black_thong(),
            "pants": Jean_black_pants(),
            "neck": Jean_white_necklace(),
            "jacket": Jean_denim_jacket()}

        if check_if_Clothes_in_Wardrobe(Jean, Clothes):
            Outfits.append(OutfitClass("Dressed Up 1", datewear = True))

            Outfits[-1].Clothes.update(Clothes)

        Clothes = {
            "hair": Jean_long_hair(),
            "underwear": Jean_black_thong(),
            "dress": Jean_yellow_dress()}

        if check_if_Clothes_in_Wardrobe(Jean, Clothes):
            Outfits.append(OutfitClass("Dressed Up 2", datewear = True))

            Outfits[-1].Clothes.update(Clothes)

        Clothes = {
            "hair": Jean_long_hair(),
            "bra": Jean_yellow_sports_bra(), "underwear": Jean_pink_panties(),
            "pants": Jean_blue_athletic_shorts()}

        if check_if_Clothes_in_Wardrobe(Jean, Clothes):
            Outfits.append(OutfitClass("Workout 1", activewear = True))

            Outfits[-1].Clothes.update(Clothes)

        Clothes = {
            "hair": Jean_long_hair(),
            "bra": Jean_yellow_sports_bra(), "underwear": Jean_pink_panties(),
            "pants": Jean_blue_athletic_shorts(),
            "top": Jean_black_shirt()}

        if check_if_Clothes_in_Wardrobe(Jean, Clothes):
            Outfits.append(OutfitClass("Workout 2", activewear = True))

            Outfits[-1].Clothes.update(Clothes)

        Outfits.append(OutfitClass("Hero (Chapter I)", activewear = True))

        Outfits[-1].Clothes.update({
            "face_inner_accessory": Jean_blue_mask(), "hair": Jean_long_hair(),
            "bra": Jean_yellow_sports_bra(), "underwear": Jean_pink_panties(),
            "bodysuit": Jean_Jean_suit(),
            "boots": Jean_blue_boots(),
            "belt": Jean_Jean_belt(),
            "gloves": Jean_blue_gloves(), "sleeves": Jean_blue_gauntlets()})

        Outfits.append(OutfitClass("Swimsuit (One-Piece)", swimwear = True))

        Outfits[-1].Clothes.update({
            "hair": Jean_long_hair(),
            "bodysuit": Jean_red_swimsuit()})

        Clothes = {
            "hair": Jean_long_hair(),
            "bra": Jean_yellow_bikini_top(), "underwear": Jean_yellow_bikini_bottoms()}

        if check_if_Clothes_in_Wardrobe(Jean, Clothes):
            Outfits.append(OutfitClass("Swimsuit (Bikini)", swimwear = True))

            Outfits[-1].Clothes.update(Clothes)

        Clothes = {
            "hair": Jean_long_hair(),
            "underwear": Jean_black_thong(),
            "dress": Jean_blue_nighty()}

        if check_if_Clothes_in_Wardrobe(Jean, Clothes):
            Outfits.append(OutfitClass("Lingerie 1", sexwear = True))

            Outfits[-1].Clothes.update(Clothes)

        Clothes = {
            "hair": Jean_long_hair(),
            "bra": Jean_blue_lace_bra(), "underwear": Jean_blue_lace_panties(), "hose": Jean_black_garterbelt(),
            "socks": Jean_black_stockings()}

        if check_if_Clothes_in_Wardrobe(Jean, Clothes):
            Outfits.append(OutfitClass("Lingerie 2", sexwear = True))

            Outfits[-1].Clothes.update(Clothes)

        Clothes = {
            "hair": Jean_long_hair(),
            "bra": Jean_black_balconette_bra(), "underwear": Jean_black_thong()}

        if check_if_Clothes_in_Wardrobe(Jean, Clothes):
            Outfits.append(OutfitClass("Lingerie 3", sexwear = True))

            Outfits[-1].Clothes.update(Clothes)

        Outfits.append(OutfitClass("Pajamas 1", sleepwear = True))

        Outfits[-1].Clothes.update({
            "hair": Jean_long_hair(),
            "bra": Jean_pink_bra(), "underwear": Jean_pink_panties(),
            "top": Jean_college_shirt()})

        Clothes = {
            "hair": Jean_long_hair(),
            "bra": Jean_pink_bra(), "underwear": Jean_pink_boyshorts()}

        if check_if_Clothes_in_Wardrobe(Jean, Clothes):
            Outfits.append(OutfitClass("Pajamas 2", sexwear = True, sleepwear = True))

            Outfits[-1].Clothes.update(Clothes)

        Outfits.append(OutfitClass("Nude"))

        Outfits[-1].Clothes.update({
            "hair": Jean_long_hair()})

        return Outfits