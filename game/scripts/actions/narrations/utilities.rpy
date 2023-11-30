init python:

    def sex_faces(Characters):
        for C in Characters:
            if not C.mouth_Actions:
                if C in [Rogue]:
                    if C.desire >= 90:
                        C.change_face("worried2", mouth = "lipbite", blush = 3)
                    elif C.desire >= 75:
                        C.change_face("worried1", mouth = "lipbite", blush = 3)
                    elif C.desire >= 50:
                        C.change_face("sexy", blush = 2)
                    else:
                        C.change_face("worried1", mouth = "smirk", blush = 1)
                elif C in [Laura]:
                    if C.desire >= 90:
                        C.change_face("worried2", mouth = "lipbite", blush = 3)
                    elif C.desire >= 75:
                        C.change_face("sly", mouth = "lipbite", blush = 3)
                    elif C.desire >= 50:
                        C.change_face("sexy", blush = 2)
                    else:
                        C.change_face("sly", blush = 1)
                elif C in [Jean]:
                    if C.desire >= 90:
                        C.change_face("worried2", mouth = "lipbite", blush = 3)
                    elif C.desire >= 75:
                        C.change_face("worried1", mouth = "lipbite", blush = 3)
                    elif C.desire >= 50:
                        C.change_face("sexy", blush = 2)
                    else:
                        C.change_face("confused1", mouth = "smirk", blush = 1)

        return

    def sex_talk(Characters):
        for C in Characters:
            if C in [Rogue]:
                if C.mouth_Actions and ((C.mouth_Actions[0].animation_type == "blowjob" and C.mouth_Actions[0].mode == 3) or C.mouth_Actions[0].animation_type == "deepthroat"):
                    dice_roll = renpy.random.randint(1, 2)

                    if dice_roll == 1:
                        renpy.say(C.voice, "*gag*")
                    elif dice_roll == 2:
                        renpy.say(C.voice, "*cough*")
                else:
                    dice_roll = renpy.random.randint(1, 3)

                    if dice_roll == 1:
                        renpy.say(C.voice, "*gasp*")
                    elif dice_roll == 2:
                        renpy.say(C.voice, f"Oh lord. . . {C.Player_petname}, please don't stop.")
                    elif dice_roll == 3:
                        renpy.say(C.voice, "Mmmmh. . .")
            elif C in [Laura]:
                if C.mouth_Actions and C.mouth_Actions[0].animation_type in ["blowjob", "deepthroat"]:
                    dice_roll = renpy.random.randint(1, 2)

                    if dice_roll == 1:
                        renpy.say(C.voice, "*gag*")
                    elif dice_roll == 2:
                        renpy.say(C.voice, "*cough*")
                else:
                    dice_roll = renpy.random.randint(1, 3)

                    if dice_roll == 1:
                        renpy.say(C.voice, "{i}Grrrrrr{/i}. . .")
                    elif dice_roll == 2:
                        renpy.say(C.voice, "Hnnng. . .")
                    elif dice_roll == 3:
                        renpy.say(C.voice, "Hmmm. . .")
            elif C in [Jean]:
                if C.mouth_Actions and C.mouth_Actions[0].animation_type in ["blowjob", "deepthroat"]:
                    dice_roll = renpy.random.randint(1, 2)

                    if dice_roll == 1:
                        renpy.say(C.voice, "*gag*")
                    elif dice_roll == 2:
                        renpy.say(C.voice, "*cough*")
                else:
                    dice_roll = renpy.random.randint(1, 3)

                    if dice_roll == 1:
                        renpy.say(C.voice, "Oh. . .")
                    elif dice_roll == 2:
                        renpy.say(C.voice, "*gasp*")
                    elif dice_roll == 3:
                        renpy.say(C.voice, f"Mmmm, {C.Player_petname}, keep going.")

        return