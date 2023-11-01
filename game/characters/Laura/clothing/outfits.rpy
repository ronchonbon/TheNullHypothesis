init python:

    def default_Laura_Outfits():
        Outfits = []
        
        Outfits.append(OutfitClass("Casual 1", wear_in_public = True))

        Outfits[-1].Clothes.update({
            "hair": Laura_straight_hair(),
            "underwear": Laura_grey_panties(),
            "pants": Laura_leather_pants(),
            "top": Laura_yellow_tanktop(),
            "neck": Laura_cross_choker(), "gloves": Laura_black_long_gloves()})

        Outfits.append(OutfitClass("Casual 2", wear_in_public = True))

        Outfits[-1].Clothes.update({
            "hair": Laura_straight_hair(),
            "bra": Laura_yellow_sports_bra(), "underwear": Laura_grey_panties(),
            "pants": Laura_black_jeans(),
            "top": Laura_striped_shirt(),
            "neck": Laura_cross_necklace(),
            "jacket": Laura_denim_jacket()})

        Clothes = {
            "hair": Laura_straight_hair(),
            "bra": Laura_blackred_corset(), "underwear": Laura_black_lace_panties(), 
            "skirt": Laura_red_skirt(), "boots": Laura_thighhigh_boots(),
            "neck": Laura_cross_necklace(), "gloves": Laura_black_long_gloves()}

        if check_if_Clothes_in_Wardrobe(Laura, Clothes):
            Outfits.append(OutfitClass("Casual 3", wear_in_public = True, datewear = True))

            Outfits[-1].Clothes.update(Clothes)

        Clothes = {
            "hair": Laura_straight_hair(),
            "underwear": Laura_black_lace_panties(),
            "pants": Laura_black_shorts(),
            "top": Laura_yellow_tanktop(),
            "neck": Laura_cross_choker()}

        if check_if_Clothes_in_Wardrobe(Laura, Clothes):
            Outfits.append(OutfitClass("Casual 4", wear_in_public = True, datewear = True))

            Outfits[-1].Clothes.update(Clothes)

        Clothes = {
            "hair": Laura_straight_hair(),
            "underwear": Laura_black_lace_panties(),
            "pants": Laura_black_jeans(),
            "top": Laura_yellow_tanktop(),
            "jacket": Laura_leather_jacket()}

        if check_if_Clothes_in_Wardrobe(Laura, Clothes):
            Outfits.append(OutfitClass("Dressed Up 1", wear_in_public = True, datewear = True))

            Outfits[-1].Clothes.update(Clothes)

            Outfits[-1].Clothes["jacket"].state = 1
            Outfits[-1].Clothes["jacket"].selected_state = 1

        Clothes = {
            "hair": Laura_straight_hair(),
            "bra": Laura_white_tanktop(), "underwear": Laura_black_lace_panties(),
            "skirt": Laura_red_skirt(), "boots": Laura_thighhigh_boots(),
            "jacket": Laura_leather_jacket()}

        if check_if_Clothes_in_Wardrobe(Laura, Clothes):
            Outfits.append(OutfitClass("Dressed Up 2", datewear = True))

            Outfits[-1].Clothes.update(Clothes)

            Outfits[-1].Clothes["jacket"].state = 1
            Outfits[-1].Clothes["jacket"].selected_state = 1

        Clothes = {
            "hair": Laura_straight_hair(),
            "bra": Laura_blackred_corset(), "underwear": Laura_black_boyshorts(),
            "pants": Laura_leather_pants(),
            "neck": Laura_cross_necklace(),
            "jacket": Laura_leather_jacket()}

        if check_if_Clothes_in_Wardrobe(Laura, Clothes):
            Outfits.append(OutfitClass("Dressed Up 3", datewear = True))

            Outfits[-1].Clothes.update(Clothes)

            Outfits[-1].Clothes["jacket"].state = 1
            Outfits[-1].Clothes["jacket"].selected_state = 1

        Clothes = {
            "hair": Laura_straight_hair(),
            "underwear": Laura_black_lace_panties(),
            "dress": Laura_black_dress()}

        if check_if_Clothes_in_Wardrobe(Laura, Clothes):
            Outfits.append(OutfitClass("Dressed Up 4", datewear = True))

            Outfits[-1].Clothes.update(Clothes)

        Outfits.append(OutfitClass("Winter 1 (Indoor)", wear_in_public = True))

        Outfits[-1].Clothes.update({
            "hair": Laura_straight_hair(),
            "bra": Laura_yellow_sports_bra(), "underwear": Laura_grey_panties(),
            "pants": Laura_leather_pants(),
            "top": Laura_white_sweater()})

        Outfits.append(OutfitClass("Winter 1 (Outdoor)", wear_in_public = True, winterwear = True))

        Outfits[-1].Clothes.update({
            "hair": Laura_straight_hair(),
            "bra": Laura_yellow_sports_bra(), "underwear": Laura_grey_panties(),
            "pants": Laura_leather_pants(),
            "top": Laura_white_sweater(),
            "neck": Laura_grey_scarf(),
            "jacket": Laura_winter_coat()})

        Clothes = {
            "hair": Laura_straight_hair(),
            "underwear": Laura_grey_panties(),
            "pants": Laura_black_jeans(),
            "top": Laura_yellow_tanktop()}

        if check_if_Clothes_in_Wardrobe(Laura, Clothes):
            Outfits.append(OutfitClass("Winter 2 (Indoor)", wear_in_public = True))

            Outfits[-1].Clothes.update(Clothes)

        Clothes = {
            "hair": Laura_straight_hair(),
            "underwear": Laura_grey_panties(),
            "pants": Laura_black_jeans(),
            "top": Laura_yellow_tanktop(),
            "neck": Laura_grey_scarf(),
            "jacket": Laura_winter_coat()}

        if check_if_Clothes_in_Wardrobe(Laura, Clothes):
            Outfits.append(OutfitClass("Winter 2 (Outdoor)", wear_in_public = True, winterwear = True))

            Outfits[-1].Clothes.update(Clothes)

        Clothes = {
            "hair": Laura_straight_hair(), 
            "underwear": Laura_grey_panties(),
            "pants": Laura_black_athletic_shorts(),
            "top": Laura_yellow_tanktop()}

        if check_if_Clothes_in_Wardrobe(Laura, Clothes):
            Outfits.append(OutfitClass("Workout 1", activewear = True))

            Outfits[-1].Clothes.update(Clothes)

        Clothes = {
            "hair": Laura_straight_hair(), 
            "bra": Laura_yellow_sports_bra(), "underwear": Laura_grey_panties(),
            "pants": Laura_black_athletic_shorts()}

        if check_if_Clothes_in_Wardrobe(Laura, Clothes):
            Outfits.append(OutfitClass("Workout 2", activewear = True))

            Outfits[-1].Clothes.update(Clothes)

        Outfits.append(OutfitClass("Hero (Chapter I)", activewear = True))

        Outfits[-1].Clothes.update({
            "hair": Laura_straight_hair(),
            "bra": Laura_yellow_sports_bra(), "underwear": Laura_grey_panties(),
            "bodysuit": Laura_blackyellow_Wolverine_suit(),
            "boots": Laura_blackyellow_Wolverine_boots(),
            "gloves": Laura_blackyellow_Wolverine_gloves(), "belt": Laura_Wolverine_belt()})

        Clothes = {
            "hair": Laura_straight_hair(), "face_outer_accessory": Laura_blackyellow_Wolverine_mask(),
            "bra": Laura_yellow_sports_bra(), "underwear": Laura_grey_panties(),
            "bodysuit": Laura_blackyellow_Wolverine_suit(),
            "boots": Laura_blackyellow_Wolverine_boots(),
            "gloves": Laura_blackyellow_Wolverine_gloves(), "belt": Laura_Wolverine_belt()}

        if check_if_Clothes_in_Wardrobe(Laura, Clothes):
            Outfits.append(OutfitClass("Hero (Masked) (Chapter I)", activewear = True))

            Outfits[-1].Clothes.update(Clothes)

        Clothes = {
            "hair": Laura_straight_hair(),
            "bra": Laura_yellow_sports_bra(), "underwear": Laura_grey_panties(),
            "bodysuit": Laura_blueyellow_Wolverine_suit(),
            "boots": Laura_blueyellow_Wolverine_boots(),
            "gloves": Laura_blueyellow_Wolverine_gloves(), "belt": Laura_Wolverine_belt()}

        if check_if_Clothes_in_Wardrobe(Laura, Clothes):
            Outfits.append(OutfitClass("Hero Alt (Chapter I)", activewear = True))

            Outfits[-1].Clothes.update(Clothes)

        Clothes = {
            "hair": Laura_straight_hair(), "face_outer_accessory": Laura_blueyellow_Wolverine_mask(),
            "bra": Laura_yellow_sports_bra(), "underwear": Laura_grey_panties(),
            "bodysuit": Laura_blueyellow_Wolverine_suit(),
            "boots": Laura_blueyellow_Wolverine_boots(),
            "gloves": Laura_blueyellow_Wolverine_gloves(), "belt": Laura_Wolverine_belt()}

        if check_if_Clothes_in_Wardrobe(Laura, Clothes):
            Outfits.append(OutfitClass("Hero Alt (Masked) (Chapter I)", activewear = True))

            Outfits[-1].Clothes.update(Clothes)

        Outfits.append(OutfitClass("Swimsuit (One-Piece)", swimwear = True))

        Outfits[-1].Clothes.update({
            "hair": Laura_straight_hair(),
            "bodysuit": Laura_black_swimsuit()})

        Clothes = {
            "hair": Laura_straight_hair(),
            "bra": Laura_black_bikini_top(), "underwear": Laura_black_bikini_bottoms()}

        if check_if_Clothes_in_Wardrobe(Laura, Clothes):
            Outfits.append(OutfitClass("Swimsuit (Bikini)", swimwear = True))

            Outfits[-1].Clothes.update(Clothes)

        Clothes = {
            "hair": Laura_straight_hair(),
            "bra": Laura_black_corset(), "underwear": Laura_black_lace_panties(), "hose": Laura_blackred_garterbelt(),
            "socks": Laura_blackred_ripped_stockings()}

        if check_if_Clothes_in_Wardrobe(Laura, Clothes):
            Outfits.append(OutfitClass("Lingerie 1", sexwear = True))

            Outfits[-1].Clothes.update(Clothes)

        Clothes = {
            "hair": Laura_straight_hair(),
            "bodysuit": Laura_leather_teddy(),
            "boots": Laura_thighhigh_boots()}

        if check_if_Clothes_in_Wardrobe(Laura, Clothes):
            Outfits.append(OutfitClass("Lingerie 2", sexwear = True))

            Outfits[-1].Clothes.update(Clothes)

        Outfits.append(OutfitClass("Pajamas 1", sleepwear = True))

        Outfits[-1].Clothes.update({
            "hair": Laura_straight_hair(),
            "underwear": Laura_grey_panties(),
            "top": Laura_yellow_tanktop()})

        Clothes = {
            "hair": Laura_straight_hair(),
            "bra": Laura_white_tanktop(), "underwear": Laura_black_boyshorts()}

        if check_if_Clothes_in_Wardrobe(Laura, Clothes):
            Outfits.append(OutfitClass("Pajamas 2", sleepwear = True))

            Outfits[-1].Clothes.update(Clothes)

        Outfits.append(OutfitClass("Nude"))

        Outfits[-1].Clothes.update({
            "hair": Laura_straight_hair()})
                
        return Outfits