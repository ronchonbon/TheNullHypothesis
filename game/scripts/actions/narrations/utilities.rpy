init python:

    import math

    def sex_faces(Characters):
        for C in Characters:
            if hookup_length >= max_hookup_length*math.sqrt(C.max_stamina) and C.desire <= 75:
                brows = None
                eyes = None
                mouth = None

                dice_roll = renpy.random.randint(1, 2)

                if dice_roll == 1:
                    brows = "neutral"
                elif dice_roll == 2:
                    brows = "cocked"

                dice_roll = renpy.random.randint(1, 3)

                if dice_roll == 1:
                    eyes = "left"
                elif dice_roll == 2:
                    eyes = "right"
                elif dice_roll == 3:
                    eyes = "neutral"

                if not C.mouth_Actions:
                    dice_roll = renpy.random.randint(1, 2)

                    if dice_roll == 1:
                        mouth = "frown"
                    elif dice_roll == 2:
                        mouth = "neutral"

                C.change_face(brows = brows, eyes = eyes, mouth = mouth)
            elif C.desire >= 90:
                eyes = None
                mouth = None

                dice_roll = renpy.random.randint(1, 3)

                if dice_roll == 1:
                    eyes = "down"
                elif dice_roll == 2:
                    eyes = "up"
                elif dice_roll == 3:
                    eyes = "sexy"

                if not C.mouth_Actions:
                    dice_roll = renpy.random.randint(1, 3)

                    if dice_roll == 1:
                        mouth = "lipbite"
                    elif dice_roll == 2:
                        mouth = "open"
                    elif dice_roll == 3:
                        mouth = "agape"

                C.change_face(brows = "worried", eyes = eyes, mouth = mouth, blush = 3)
            elif C.desire >= 75:
                eyes = None
                mouth = None

                dice_roll = renpy.random.randint(1, 2)

                if dice_roll == 1:
                    eyes = "down"
                elif dice_roll == 2:
                    eyes = "sexy"

                if not C.mouth_Actions:
                    dice_roll = renpy.random.randint(1, 2)

                    if dice_roll == 1:
                        mouth = "lipbite"
                    elif dice_roll == 2:
                        mouth = "open"

                C.change_face(brows = "worried", eyes = eyes, mouth = mouth, blush = 2)
            elif C.desire >= 50:
                eyes = None
                mouth = None

                dice_roll = renpy.random.randint(1, 2)

                if dice_roll == 1:
                    eyes = "down"
                elif dice_roll == 2:
                    eyes = "sexy"

                if not C.mouth_Actions:
                    dice_roll = renpy.random.randint(1, 3)

                    if dice_roll == 1:
                        mouth = "lipbite"
                    elif dice_roll == 2:
                        mouth = "open"
                    elif dice_roll == 3:
                        mouth = "smirk"

                C.change_face(brows = "neutral", eyes = eyes, mouth = mouth, blush = 1)
            else:
                eyes = None
                mouth = None

                dice_roll = renpy.random.randint(1, 2)

                if dice_roll == 1:
                    eyes = "neutral"
                elif dice_roll == 2:
                    eyes = "sexy"

                if not C.mouth_Actions:
                    dice_roll = renpy.random.randint(1, 3)

                    if dice_roll == 1:
                        mouth = "lipbite"
                    elif dice_roll == 2:
                        mouth = "smirk"
                    elif dice_roll == 3:
                        mouth = "happy"

                C.change_face(brows = "neutral", eyes = eyes, mouth = mouth)

        return

    def orgasm_faces(Characters):
        for C in Characters:
            if C.History.check("orgasmed_with_Player", tracker = "recent") >= 2:
                brows = None
                eyes = None
                mouth = None

                dice_roll = renpy.random.randint(1, 2)

                if dice_roll == 1:
                    brows = "raised"
                elif dice_roll == 2:
                    brows = "worried"

                dice_roll = renpy.random.randint(1, 2)

                if dice_roll == 1:
                    eyes = "wide"
                elif dice_roll == 2:
                    eyes = "up"

                if not C.mouth_Actions:
                    dice_roll = renpy.random.randint(1, 2)

                    if dice_roll == 1 and brows == "worried" and eyes == "up":
                        mouth = "tongue"
                    else:
                        mouth = "agape"

                C.change_face(brows = brows, eyes = eyes, mouth = mouth, blush = 3)
            elif C.History.check("orgasmed_with_Player", tracker = "recent"):
                brows = None
                eyes = None
                mouth = None

                dice_roll = renpy.random.randint(1, 2)

                if dice_roll == 1:
                    brows = "raised"
                elif dice_roll == 2:
                    brows = "worried"

                dice_roll = renpy.random.randint(1, 2)

                if dice_roll == 1:
                    eyes = "closed"
                elif dice_roll == 2:
                    eyes = "sexy"

                if not C.mouth_Actions:
                    dice_roll = renpy.random.randint(1, 2)

                    if dice_roll == 1:
                        mouth = "open"
                    elif dice_roll == 2:
                        mouth = "agape"

                C.change_face(brows = brows, eyes = eyes, mouth = mouth, blush = 2)
            else:
                brows = None
                eyes = None
                mouth = None

                dice_roll = renpy.random.randint(1, 2)

                if dice_roll == 1:
                    brows = "raised"
                elif dice_roll == 2:
                    brows = "worried"

                dice_roll = renpy.random.randint(1, 2)

                if dice_roll == 1:
                    eyes = "closed"
                elif dice_roll == 2:
                    eyes = "sexy"

                if not C.mouth_Actions:
                    dice_roll = renpy.random.randint(1, 2)

                    if dice_roll == 1:
                        mouth = "open"
                    elif dice_roll == 2:
                        mouth = "lipbite"

                C.change_face(brows = brows, eyes = eyes, mouth = mouth, blush = 1)

        return

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

    def desire_increases(Characters):
        for C in Characters:
            if not C.stamina:
                if C == Player and C.cock_Actions:
                    renpy.say(None, "Looks like you're running on empty - maybe give yourself a break.")
            
                continue
            elif hookup_length < max_hookup_length*math.sqrt(C.max_stamina) or C.desire > 75:
                pass
            else:
                continue

            for A in C.all_Actions:
                base = eval(f"{C.tag}_base_Action_desire")*eval(f"{C.tag}_Action_desires['{A.Action_type}'][{int(C.desire/20 % 5)}]")

                modifier = 1.0

                if len(A.modes) > 1:
                    modifier *= (A.modes.index(A.mode) + 1)/len(A.modes)

                if A.speed:
                    modifier *= speed

                if C.History.check(A.Action_type, tracker = "weekly") >= boredom_threshold:
                    modifier *= boredom_penalty

                C.desire += base*modifier

            if C.remote_vibrator is not None:
                C.desire += int(2*C.remote_vibrator)

            C.check_statuses()

        return