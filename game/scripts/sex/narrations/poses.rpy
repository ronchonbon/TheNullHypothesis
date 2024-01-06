init python:

    import math

    def sex_poses(Character):
        if hookup_length >= max_hookup_length*math.sqrt(Character.max_stamina) and Character.desire <= 75:
            dice_roll = renpy.random.randint(1, 4)
            
            if dice_roll == 1:
                Character.change_arms("crossed")
            elif dice_roll == 2:
                Character.change_arms("hips")
            elif dice_roll == 3:
                Character.change_arms("hips", left_arm = "neutral")
            elif dice_roll == 4:
                Character.change_arms("hips", right_arm = "neutral")
        elif Character.desire >= 90:
            dice_roll = renpy.random.randint(1, 3)
            
            if dice_roll == 1:
                Character.change_arms("neutral", left_arm = "grope")
            elif dice_roll == 2:
                Character.change_arms("neutral", right_arm = "touch_pussy")
            elif dice_roll == 3:
                Character.change_arms("touch_self")
        elif Character.desire >= 75:
            dice_roll = renpy.random.randint(1, 3)

            if dice_roll == 1:
                Character.change_arms("angry")
            elif dice_roll == 2:
                Character.change_arms("neutral", left_arm = "grope")
            elif dice_roll == 2:
                Character.change_arms("neutral", right_arm = "touch_pussy")
        elif Character.desire >= 50:
            dice_roll = renpy.random.randint(1, 3)

            if dice_roll == 1:
                Character.change_arms("neutral")
            elif dice_roll == 2:
                Character.change_arms("angry")
            elif dice_roll == 3:
                Character.change_arms("neutral", left_arm = "grope")
        else:
            dice_roll = renpy.random.randint(1, 2)

            if dice_roll == 1:
                Character.change_arms("neutral")
            elif dice_roll == 2:
                Character.change_arms("angry")

        return

    def orgasm_poses(Character):
        dice_roll = renpy.random.randint(1, 3)
        
        if dice_roll == 1:
            Character.change_arms("neutral", left_arm = "grope")
        elif dice_roll == 2:
            Character.change_arms("neutral", right_arm = "touch_pussy")
        elif dice_roll == 3:
            Character.change_arms("touch_self")

        return