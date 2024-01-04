init python:

    import math

    def sex_poses(Characters):
        for C in Characters:
            if hookup_length >= max_hookup_length*math.sqrt(C.max_stamina) and C.desire <= 75:
                dice_roll = renpy.random.randint(1, 4)
                
                if dice_roll == 1:
                    C.change_arms("crossed")
                elif dice_roll == 2:
                    C.change_arms("hips")
                elif dice_roll == 3:
                    C.change_arms("hips", left_arm = "neutral")
                elif dice_roll == 4:
                    C.change_arms("hips", right_arm = "neutral")
            elif C.desire >= 90:
                dice_roll = renpy.random.randint(1, 3)
                
                if dice_roll == 1:
                    C.change_arms("neutral", left_arm = "grope")
                elif dice_roll == 2:
                    C.change_arms("neutral", right_arm = "touch_self")
                elif dice_roll == 3:
                    C.change_arms("touch_self")
            elif C.desire >= 75:
                dice_roll = renpy.random.randint(1, 3)

                if dice_roll == 1:
                    C.change_arms("angry")
                elif dice_roll == 2:
                    C.change_arms("neutral", left_arm = "grope")
                elif dice_roll == 2:
                    C.change_arms("neutral", right_arm = "touch_self")
            elif C.desire >= 50:
                dice_roll = renpy.random.randint(1, 3)

                if dice_roll == 1:
                    C.change_arms("neutral")
                elif dice_roll == 2:
                    C.change_arms("angry")
                elif dice_roll == 3:
                    C.change_arms("neutral", left_arm = "grope")
            else:
                dice_roll = renpy.random.randint(1, 2)

                if dice_roll == 1:
                    C.change_arms("neutral")
                elif dice_roll == 2:
                    C.change_arms("angry")

        return

    def orgasm_poses(Characters):
        for C in Characters:
            dice_roll = renpy.random.randint(1, 3)
            
            if dice_roll == 1:
                C.change_arms("neutral", left_arm = "grope")
            elif dice_roll == 2:
                C.change_arms("neutral", right_arm = "touch_pussy")
            elif dice_roll == 3:
                C.change_arms("touch_self")

        return