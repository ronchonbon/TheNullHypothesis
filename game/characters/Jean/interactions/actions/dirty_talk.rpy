label Jean_dirty_talk:
    if hookup_length < max_hookup_length*math.sqrt(Jean.max_stamina) or Jean.desire > 75:
        $ dice_pool = [1]

        if Jean.desire > 50:
            $ dice_pool.append(3)

        if Jean.desire > 75:
            $ dice_pool.append(4)
            $ dice_pool.append(5)

        if Jean.desire > 90:
            $ dice_pool.append(6)

        $ dice_roll = renpy.random.choice(dice_pool)

        if dice_roll == 1:
            ch_Jean "Oh. . ."
        elif dice_roll == 2:
            ch_Jean "Mmmm, [Jean.Player_petname], keep going."
        elif dice_roll == 3:
            ch_Jean "*gasp*"
        elif dice_roll == 4:
            ch_Jean "Oh god, that feels good."
        elif dice_roll == 5:
            ch_Jean "How did you get this good. . . ?"
        elif dice_roll == 6:
            ch_Jean "I'm so close, [Jean.Player_petname]. . ."
    else:
        if renpy.random.random() > 0.75:
            if renpy.random.random() > 0.5:
                ch_Jean "Maybe we could take a break soon?"
            else:
                ch_Jean "You're not tired at all?"

    return