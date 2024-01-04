init python:

    import math

    def sex_talk(Characters):
        for C in Characters:
            if C.mouth_Actions and ((C.mouth_Actions[0].Action_type == "blowjob" and C.mouth_Actions[0].mode == 3) or C.mouth_Actions[0].Action_type == "deepthroat"):
                dice_pool = [1]

                if C.desire >= 50:
                    dice_pool.append(2)
                
                if C.History.check(C.mouth_Actions[0].Action_type) >= 10:
                    dice_pool.append(3)
                else:
                    dice_pool.append(4)

                dice_roll = renpy.random.choice(dice_pool)

                if dice_roll == 1:
                    renpy.say(C.voice, "*gag*")
                elif dice_roll == 2:
                    renpy.say(C.voice, "Mmmmm.")
                elif dice_roll == 3:
                    renpy.say(C.voice, "*hum*")
                elif dice_roll == 4:
                    renpy.say(C.voice, "*cough*")
            elif C in [Rogue]:
                if hookup_length < max_hookup_length*math.sqrt(C.max_stamina) or C.desire > 75:
                    dice_pool = [1, 2]

                    if C.desire > 50:
                        dice_pool.append(3)

                    if C.desire > 75:
                        dice_pool.append(4)
                        dice_pool.append(5)

                    if C.desire > 90:
                        dice_pool.append(6)

                    dice_roll = renpy.random.choice(dice_pool)

                    if dice_roll == 1:
                        renpy.say(C.voice, "Mmmmh. . .")
                    elif dice_roll == 2:
                        renpy.say(C.voice, "That's nice. . .")
                    elif dice_roll == 3:
                        renpy.say(C.voice, "Ohhh. . .")
                    elif dice_roll == 4:
                        renpy.say(C.voice, "*gasp*")
                    elif dice_roll == 5:
                        renpy.say(C.voice, f"Oh lord. . . {C.Player_petname}, please don't stop.")
                    elif dice_roll == 6:
                        renpy.say(C.voice, f"Ah'm so close. . .")
                else:
                    if renpy.random.random() > 0.75:
                        if renpy.random.random() > 0.5:
                            renpy.say(C.voice, f"Mmmm, ready for a break soon, {C.Player_petname}?")
                        else:
                            renpy.say(C.voice, "Ah could really use a break. . .")
            elif C in [Laura]:
                if hookup_length < max_hookup_length*math.sqrt(C.max_stamina) or C.desire > 75:
                    dice_pool = [1, 2]

                    if C.desire > 50:
                        dice_pool.append(3)

                    if C.desire > 75:
                        dice_pool.append(4)
                        dice_pool.append(5)

                    if C.desire > 90:
                        dice_pool.append(6)

                    dice_roll = renpy.random.choice(dice_pool)

                    if dice_roll == 1:
                        renpy.say(C.voice, "Hmmm. . .")
                    elif dice_roll == 2:
                        renpy.say(C.voice, "That's. . . mmm.")
                    elif dice_roll == 3:
                        renpy.say(C.voice, "I like that. . .")
                    elif dice_roll == 4:
                        renpy.say(C.voice, "{i}Grrrrrr{/i}. . .")
                    elif dice_roll == 5:
                        renpy.say(C.voice, "Hnnng. . .")
                    elif dice_roll == 6:
                        renpy.say(C.voice, "I'm. . . gonna. . .")
                else:
                    if renpy.random.random() > 0.75:
                        if renpy.random.random() > 0.5:
                            renpy.say(C.voice, "I'm getting bored.")
                        else:
                            renpy.say(C.voice, "Does this normally take this long?")
            elif C in [Jean]:
                if hookup_length < max_hookup_length*math.sqrt(C.max_stamina) or C.desire > 75:
                    dice_pool = [1]

                    if C.desire > 50:
                        dice_pool.append(3)

                    if C.desire > 75:
                        dice_pool.append(4)
                        dice_pool.append(5)

                    if C.desire > 90:
                        dice_pool.append(6)

                    dice_roll = renpy.random.choice(dice_pool)

                    if dice_roll == 1:
                        renpy.say(C.voice, "Oh. . .")
                    elif dice_roll == 2:
                        renpy.say(C.voice, f"Mmmm, {C.Player_petname}, keep going.")
                    elif dice_roll == 3:
                        renpy.say(C.voice, "*gasp*")
                    elif dice_roll == 4:
                        renpy.say(C.voice, "Oh god, that feels good.")
                    elif dice_roll == 5:
                        renpy.say(C.voice, "How did you get this good. . . ?")
                    elif dice_roll == 6:
                        renpy.say(C.voice, f"I'm so close, {C.Player_petname}. . .")
                else:
                    if renpy.random.random() > 0.75:
                        if renpy.random.random() > 0.5:
                            renpy.say(C.voice, "Maybe we could take a break soon?")
                        else:
                            renpy.say(C.voice, "You're not tired at all?")

        return