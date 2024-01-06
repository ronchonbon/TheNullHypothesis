label Laura_dirty_talk:
    if hookup_length < max_hookup_length*math.sqrt(Laura.max_stamina) or Laura.desire > 75:
        $ dice_pool = [1, 2]

        if Laura.desire > 50:
            $ dice_pool.append(3)

        if Laura.desire > 75:
            $ dice_pool.append(4)
            $ dice_pool.append(5)

        if Laura.desire > 90:
            $ dice_pool.append(6)

        $ dice_roll = renpy.random.choice(dice_pool)

        if dice_roll == 1:
            ch_Laura "Hmmm. . ."
        elif dice_roll == 2:
            ch_Laura "That's. . . mmm."
        elif dice_roll == 3:
            ch_Laura "I like that. . ."
        elif dice_roll == 4:
            ch_Laura "{i}Grrrrrr{/i}. . ."
        elif dice_roll == 5:
            ch_Laura "Hnnng. . ."
        elif dice_roll == 6:
            ch_Laura "I'm. . . gonna. . ."
    else:
        if renpy.random.random() > 0.75:
            if renpy.random.random() > 0.5:
                ch_Laura "I'm getting bored."
            else:
                ch_Laura "Does this normally take this long?"

    return