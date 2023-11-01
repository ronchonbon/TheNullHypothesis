init python:

    def default_Rogue_Outfits():
        Outfits = []
        
        Outfits.append(OutfitClass("Casual 1", wear_in_public = True))

        Outfits[-1].Clothes.update({
            "makeup": Rogue_purple_eyeshadow(),
            "hair": Rogue_asymmetric_hair(),
            "bra": Rogue_black_bra(), "underwear": Rogue_yellow_panties(), "hose": Rogue_black_tights(), 
            "pants": Rogue_black_shorts(),
            "top": Rogue_black_fishnet_top(),
            "neck": Rogue_spiked_collar(), "gloves": Rogue_black_gloves(), "sleeves": Rogue_spiked_bracelets(),
            "jacket": Rogue_NIN_shirt()})

        Outfits.append(OutfitClass("Casual 2", wear_in_public = True))

        Outfits[-1].Clothes.update({
            "makeup": Rogue_purple_eyeshadow(),
            "hair": Rogue_asymmetric_hair(),
            "bra": Rogue_black_tanktop(), "underwear": Rogue_yellow_panties(),
            "pants": Rogue_black_jeans(),
            "top": Rogue_black_top(),
            "gloves": Rogue_black_gloves()})

        Clothes = {
            "makeup": Rogue_purple_eyeshadow(),
            "hair": Rogue_asymmetric_hair(),
            "bra": Rogue_black_tanktop(), "underwear": Rogue_green_panties(), "hose": Rogue_black_tights(), 
            "skirt": Rogue_leather_skirt(),
            "top": Rogue_green_mesh_top(),
            "gloves": Rogue_black_gloves()}

        if check_if_Clothes_in_Wardrobe(Rogue, Clothes):
            Outfits.append(OutfitClass("Casual 3", wear_in_public = True, datewear = True))

            Outfits[-1].Clothes.update(Clothes)

        Clothes = {
            "makeup": Rogue_purple_eyeshadow(),
            "hair": Rogue_asymmetric_hair(),
            "bra": Rogue_black_tanktop(), "underwear": Rogue_greenyellow_boyshorts(),
            "pants": Rogue_black_jeans(),
            "top": Rogue_black_fishnet_top(),
            "neck": Rogue_spiked_collar(), "gloves": Rogue_black_gloves(), "sleeves": Rogue_spiked_bracelets(),
            "jacket": Rogue_brown_jacket()}

        if check_if_Clothes_in_Wardrobe(Rogue, Clothes):
            Outfits.append(OutfitClass("Casual 4", wear_in_public = True))

            Outfits[-1].Clothes.update(Clothes)

        Clothes = {
            "makeup": Rogue_purple_eyeshadow(),
            "hair": Rogue_asymmetric_hair(),
            "bra": Rogue_black_tanktop(), "underwear": Rogue_black_lace_panties(),
            "pants": Rogue_black_jeans(),
            "top": Rogue_green_mesh_top(),
            "gloves": Rogue_black_gloves()}

        if check_if_Clothes_in_Wardrobe(Rogue, Clothes):
            Outfits.append(OutfitClass("Casual 5", wear_in_public = True))

            Outfits[-1].Clothes.update(Clothes)

        Clothes = {
            "makeup": Rogue_purple_eyeshadow(),
            "hair": Rogue_asymmetric_hair(),
            "underwear": Rogue_black_cage_thong(),
            "socks": Rogue_black_tall_socks(),
            "dress": Rogue_green_dress(),
            "gloves": Rogue_black_gloves()}

        if check_if_Clothes_in_Wardrobe(Rogue, Clothes):
            Outfits.append(OutfitClass("Dressed Up 1", datewear = True))

            Outfits[-1].Clothes.update(Clothes)

        Clothes = {
            "makeup": Rogue_purple_eyeshadow(),
            "hair": Rogue_asymmetric_hair(),
            "bra": Rogue_black_lace_bra(), "underwear": Rogue_black_lace_panties(),
            "socks": Rogue_black_tall_socks(), "skirt": Rogue_leather_skirt(),
            "top": Rogue_black_top(),
            "gloves": Rogue_black_gloves()}

        if check_if_Clothes_in_Wardrobe(Rogue, Clothes):
            Outfits.append(OutfitClass("Dressed Up 2", wear_in_public = True, datewear = True))

            Outfits[-1].Clothes.update(Clothes)

        Outfits.append(OutfitClass("Winter 1 (Indoor)", wear_in_public = True))

        Outfits[-1].Clothes.update({
            "makeup": Rogue_purple_eyeshadow(),
            "hair": Rogue_asymmetric_hair(),
            "bra": Rogue_black_bra(), "underwear": Rogue_yellow_panties(), "hose": Rogue_black_tights(), 
            "boots": Rogue_thighhigh_boots(),
            "dress": Rogue_sweater_dress(),
            "gloves": Rogue_black_gloves()})

        Outfits.append(OutfitClass("Winter 1 (Outdoor)", wear_in_public = True, winterwear = True))

        Outfits[-1].Clothes.update({
            "makeup": Rogue_purple_eyeshadow(),
            "hair": Rogue_asymmetric_hair(),
            "bra": Rogue_black_bra(), "underwear": Rogue_yellow_panties(), "hose": Rogue_black_tights(), 
            "boots": Rogue_thighhigh_boots(),
            "dress": Rogue_sweater_dress(),
            "neck": Rogue_maroon_scarf(), "gloves": Rogue_black_gloves(),
            "jacket": Rogue_plaid_coat()})

        Clothes = {
            "makeup": Rogue_purple_eyeshadow(),
            "hair": Rogue_asymmetric_hair(),
            "bra": Rogue_black_tanktop(), "underwear": Rogue_green_panties(),
            "pants": Rogue_black_jeans(),
            "dress": Rogue_sweater_dress(),
            "gloves": Rogue_black_gloves()}

        if check_if_Clothes_in_Wardrobe(Rogue, Clothes):
            Outfits.append(OutfitClass("Winter 2 (Indoor)", wear_in_public = True))

            Outfits[-1].Clothes.update(Clothes)

        Clothes = {
            "makeup": Rogue_purple_eyeshadow(),
            "hair": Rogue_asymmetric_hair(),
            "bra": Rogue_black_tanktop(), "underwear": Rogue_green_panties(),
            "pants": Rogue_black_jeans(),
            "dress": Rogue_sweater_dress(),
            "gloves": Rogue_black_gloves(),
            "jacket": Rogue_plaid_coat()}

        if check_if_Clothes_in_Wardrobe(Rogue, Clothes):
            Outfits.append(OutfitClass("Winter 2 (Outdoor)", wear_in_public = True, winterwear = True))

            Outfits[-1].Clothes.update(Clothes)

        Clothes = {
            "makeup": Rogue_purple_eyeshadow(),
            "hair": Rogue_asymmetric_hair(),
            "bra": Rogue_greenyellow_sports_bra(), "underwear": Rogue_greenyellow_boyshorts(),
            "pants": Rogue_green_athletic_shorts(),
            "gloves": Rogue_black_gloves()}

        if check_if_Clothes_in_Wardrobe(Rogue, Clothes):
            Outfits.append(OutfitClass("Workout 1", activewear = True))

            Outfits[-1].Clothes.update(Clothes)

        Outfits.append(OutfitClass("Hero (Chapter I)", activewear = True))

        Outfits[-1].Clothes.update({
            "makeup": Rogue_purple_eyeshadow(),
            "face_inner_accessory": Rogue_green_headband(), "hair": Rogue_asymmetric_hair(),
            "bra": Rogue_greenyellow_sports_bra(), "underwear": Rogue_yellow_panties(),
            "bodysuit": Rogue_Rogue_suit(),
            "boots": Rogue_yellow_boots(),
            "gloves": Rogue_yellow_gloves(), "belt": Rogue_Rogue_belt(),
            "jacket": Rogue_brown_jacket()})

        Outfits.append(OutfitClass("Swimsuit (One-Piece)", swimwear = True))

        Outfits[-1].Clothes.update({
            "makeup": Rogue_purple_eyeshadow(),
            "hair": Rogue_asymmetric_hair(),
            "bodysuit": Rogue_pink_swimsuit()})

        Clothes = {
            "makeup": Rogue_purple_eyeshadow(),
            "hair": Rogue_asymmetric_hair(),
            "bra": Rogue_green_bikini_top(), "underwear": Rogue_green_bikini_bottoms()}

        if check_if_Clothes_in_Wardrobe(Rogue, Clothes):
            Outfits.append(OutfitClass("Swimsuit (Bikini)", swimwear = True))

            Outfits[-1].Clothes.update(Clothes)

        Clothes = {
            "makeup": Rogue_purple_eyeshadow(),
            "hair": Rogue_asymmetric_hair(),
            "bra": Rogue_black_lace_bra(), "underwear": Rogue_black_lace_panties(), "hose": Rogue_black_garterbelt(),
            "socks": Rogue_black_stockings()}

        if check_if_Clothes_in_Wardrobe(Rogue, Clothes):
            Outfits.append(OutfitClass("Lingerie 1", sexwear = True))

            Outfits[-1].Clothes.update(Clothes)

        Clothes = {
            "makeup": Rogue_purple_eyeshadow(),
            "hair": Rogue_asymmetric_hair(),
            "bra": Rogue_black_cage_bra(), "underwear": Rogue_black_cage_thong(),
            "socks": Rogue_black_tall_socks()}

        if check_if_Clothes_in_Wardrobe(Rogue, Clothes):
            Outfits.append(OutfitClass("Lingerie 2", sexwear = True))

            Outfits[-1].Clothes.update(Clothes)

        Clothes = {
            "makeup": Rogue_purple_eyeshadow(),
            "hair": Rogue_asymmetric_hair(),
            "underwear": Rogue_black_cage_thong(),
            "dress": Rogue_green_nighty()}

        if check_if_Clothes_in_Wardrobe(Rogue, Clothes):
            Outfits.append(OutfitClass("Lingerie 3", sexwear = True))

            Outfits[-1].Clothes.update(Clothes)

        Outfits.append(OutfitClass("Pajamas 1", sleepwear = True))

        Outfits[-1].Clothes.update({
            "hair": Rogue_asymmetric_hair(),
            "bra": Rogue_black_tanktop(), "underwear": Rogue_yellow_panties()})

        Clothes = {
            "hair": Rogue_asymmetric_hair(),
            "bra": Rogue_black_tanktop(), "underwear": Rogue_greenyellow_boyshorts()}

        if check_if_Clothes_in_Wardrobe(Rogue, Clothes):
            Outfits.append(OutfitClass("Pajamas 2", sleepwear = True))

            Outfits[-1].Clothes.update(Clothes)

        Clothes = {
            "hair": Rogue_asymmetric_hair(),
            "bra": Rogue_black_bra(), "underwear": Rogue_green_panties()}

        if check_if_Clothes_in_Wardrobe(Rogue, Clothes):
            Outfits.append(OutfitClass("Pajamas 3", sleepwear = True))

            Outfits[-1].Clothes.update(Clothes)

        Outfits.append(OutfitClass("Nude"))

        Outfits[-1].Clothes.update({
            "hair": Rogue_asymmetric_hair()})
                
        return Outfits