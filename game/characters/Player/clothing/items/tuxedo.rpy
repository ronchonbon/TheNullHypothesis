init -1 python:

    def Player_tuxedo():
        name = "tuxedo"
        short_name = "tuxedo"
        string = "tuxedo"
        
        Clothing_type = "Player"

        shop_type = "Player"
        chapter = 0
        season = 0
        
        thresholds = {
            "accept": [0, 0],
            "wear_in_private": [0, 0],
            "wear_in_public": [0, 0]}
        
        return ClothingClass(
            Player, 
            name, short_name, string, Clothing_type, 
            shop_type, chapter, season,
            thresholds)
