label Rogue_dirty_talk:
    if hookup_length < max_hookup_length*math.sqrt(Rogue.max_stamina) or Rogue.desire > 75:
        $ dice_pool = [1, 2]

        if Rogue.desire > 50:
            $ dice_pool.append(3)

        if Rogue.desire > 75:
            $ dice_pool.append(4)
            $ dice_pool.append(5)

        if Rogue.desire > 90:
            $ dice_pool.append(6)

        $ dice_roll = renpy.random.choice(dice_pool)

        if dice_roll == 1:
            ch_Rogue "Mmmmh. . ."
        elif dice_roll == 2:
            ch_Rogue "That's nice. . ."
        elif dice_roll == 3:
            ch_Rogue "Ohhh. . ."
        elif dice_roll == 4:
            ch_Rogue "*gasp*"
        elif dice_roll == 5:
            ch_Rogue "Oh lord. . . [Rogue.Player_petname], please don't stop."
        elif dice_roll == 6:
            ch_Rogue f"Ah'm so close. . ."
    else:
        if renpy.random.random() > 0.75:
            if renpy.random.random() > 0.5:
                ch_Rogue "Mmmm, ready for a break soon, [Rogue.Player_petname]?"
            else:
                ch_Rogue "Ah could really use a break. . ."

    return