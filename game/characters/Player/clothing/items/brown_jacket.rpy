init -1 python:

    def Player_brown_jacket():
        name = "brown jacket"
        short_name = "jacket"
        string = "brown_jacket"
        
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
