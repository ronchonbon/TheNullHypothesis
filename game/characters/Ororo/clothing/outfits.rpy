init python:

    def default_Ororo_Outfits():
        Outfits = []
        
        Outfits.append(OutfitClass("Casual 1", wear_in_public = True))

        Outfits[-1].Clothes.update({
            "hair": Ororo_ponytail(),
            "underwear": Ororo_grey_panties(),
            "skirt": Ororo_red_skirt(),
            "top": Ororo_white_frilly_top(),
            "sleeves": Ororo_ring_bracelets()})

        Outfits.append(OutfitClass("Casual 2", wear_in_public = True))

        Outfits[-1].Clothes.update({
            "hair": Ororo_ponytail(),
            "underwear": Ororo_grey_panties(),
            "pants": Ororo_grey_pants(),
            "bra": Ororo_grey_bra(), "top": Ororo_white_shirt(),
            "sleeves": Ororo_ring_bracelets()})

        Outfits.append(OutfitClass("Winter 1 (Indoor)", wear_in_public = True))

        Outfits[-1].Clothes.update({
            "hair": Ororo_ponytail(),
            "underwear": Ororo_grey_panties(),
            "pants": Ororo_grey_pants(),
            "bra": Ororo_grey_bra(), "top": Ororo_beige_shirt()})

        Outfits.append(OutfitClass("Winter 1 (Outdoor)", wear_in_public = True, winterwear = True))

        Outfits[-1].Clothes.update({
            "hair": Ororo_ponytail(),
            "underwear": Ororo_grey_panties(),
            "pants": Ororo_grey_pants(),
            "bra": Ororo_grey_bra(), "top": Ororo_beige_shirt(),
            "jacket": Ororo_grey_peacoat()})

        Outfits.append(OutfitClass("Hero (Chapter I)", activewear = True))

        Outfits[-1].Clothes.update({
            "face_inner_accessory": Ororo_black_mask(), "hair": Ororo_ponytail(),
            "underwear": Ororo_grey_panties(),
            "bodysuit": Ororo_Storm_suit(),
            "gloves": Ororo_black_gloves(),
            "cloak": Ororo_black_cape()})

        Outfits.append(OutfitClass("Swimsuit (One-Piece)", swimwear = True))

        Outfits[-1].Clothes.update({
            "hair": Ororo_ponytail(),
            "bodysuit": Ororo_black_swimsuit()})

        Outfits.append(OutfitClass("Pajamas 1", sleepwear = True))

        Outfits[-1].Clothes.update({
            "hair": Ororo_ponytail(),
            "underwear": Ororo_grey_panties(),
            "bra": Ororo_grey_bra(), "top": Ororo_white_shirt()})

        Outfits.append(OutfitClass("Nude"))

        Outfits[-1].Clothes.update({
            "hair": Ororo_ponytail()})

        return Outfits