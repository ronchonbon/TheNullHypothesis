label chapter_1_swimming_narrations(swimming_Characters = None):
    if len(swimming_Characters) > 1:
        "You and the girls laugh and splash around a bit before lazily floating around while asking each other questions both silly and deep."
    elif len(swimming_Characters) == 1:
        "You and [swimming_Characters[0].name] laugh and splash around a bit before lazily floating around while asking each other questions both silly and deep."
    else:
        $ dice_roll = renpy.random.randint(1, 4)

        if dice_roll == 1:
            "There are a few people hanging around the pool, but it's fairly quiet. You decide to just get some exercise swimming laps."
            
            if chapter > 1 or season > 1:
                "You notice how much further you can swim before tiring."
        elif dice_roll == 2:
            "You relax in the hot tub, letting the water jet massage away all the aches and pains you've accumulated from training."
        elif dice_roll == 3:
            "The water is calm and warm, the pool is empty. You enjoy the water, trying to relax and shut your brain off for a while."
        elif dice_roll == 4:
            "You use the diving board, trying to perfect your cannonball. You've heard tales about the last time Colossus showed off {i}his{/i} cannonball."

    return