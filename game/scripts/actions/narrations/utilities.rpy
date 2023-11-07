label sex_faces(Characters):
    while Characters:
        if not Characters[0].mouth_Actions:
            if Characters[0] in [Rogue]:
                if Characters[0].desire >= 90:
                    $ Characters[0].change_face("worried2", mouth = "lipbite", blush = 3)
                elif Characters[0].desire >= 75:
                    $ Characters[0].change_face("worried1", mouth = "lipbite", blush = 3)
                elif Characters[0].desire >= 50:
                    $ Characters[0].change_face("sexy", blush = 2)
                else:
                    $ Characters[0].change_face("worried1", mouth = "smirk", blush = 1)
            elif Characters[0] in [Laura]:
                if Characters[0].desire >= 90:
                    $ Characters[0].change_face("worried2", mouth = "lipbite", blush = 3)
                elif Characters[0].desire >= 75:
                    $ Characters[0].change_face("sly", mouth = "lipbite", blush = 3)
                elif Characters[0].desire >= 50:
                    $ Characters[0].change_face("sexy", blush = 2)
                else:
                    $ Characters[0].change_face("sly", blush = 1)
            elif Characters[0] in [Jean]:
                if Characters[0].desire >= 90:
                    $ Characters[0].change_face("worried2", mouth = "lipbite", blush = 3)
                elif Characters[0].desire >= 75:
                    $ Characters[0].change_face("worried1", mouth = "lipbite", blush = 3)
                elif Characters[0].desire >= 50:
                    $ Characters[0].change_face("sexy", blush = 2)
                else:
                    $ Characters[0].change_face("confused1", mouth = "smirk", blush = 1)

        $ Characters.remove(Characters[0])

    return

label sex_talk(Characters):
    while Characters:
        if Characters[0] in [Rogue]:
            if Characters[0].mouth_Actions and ((Characters[0].mouth_Actions[0].animation_type == "blowjob" and Characters[0].mouth_Actions[0].mode == 3) or Characters[0].mouth_Actions[0].animation_type == "deepthroat"):
                $ dice_roll = renpy.random.randint(1, 2)

                if dice_roll == 1:
                    $ renpy.say(Characters[0].voice, "*gag*")
                elif dice_roll == 2:
                    $ renpy.say(Characters[0].voice, "*cough*")
            else:
                $ dice_roll = renpy.random.randint(1, 3)

                if dice_roll == 1:
                    $ renpy.say(Characters[0].voice, "*gasp*")
                elif dice_roll == 2:
                    $ renpy.say(Characters[0].voice, "Oh lord. . . [Characters[0].Player_petname], please don't stop.")
                elif dice_roll == 3:
                    $ renpy.say(Characters[0].voice, "Mmmmh. . .")
        elif Characters[0] in [Laura]:
            if Characters[0].mouth_Actions and Characters[0].mouth_Actions[0].animation_type in ["blowjob", "deepthroat"]:
                $ dice_roll = renpy.random.randint(1, 2)

                if dice_roll == 1:
                    $ renpy.say(Characters[0].voice, "*gag*")
                elif dice_roll == 2:
                    $ renpy.say(Characters[0].voice, "*cough*")
            else:
                $ dice_roll = renpy.random.randint(1, 3)

                if dice_roll == 1:
                    $ renpy.say(Characters[0].voice, "{i}Grrrrrr{/i}. . .")
                elif dice_roll == 2:
                    $ renpy.say(Characters[0].voice, "Hnnng. . .")
                elif dice_roll == 3:
                    $ renpy.say(Characters[0].voice, "Hmmm. . .")
        elif Characters[0] in [Jean]:
            if Characters[0].mouth_Actions and Characters[0].mouth_Actions[0].animation_type in ["blowjob", "deepthroat"]:
                $ dice_roll = renpy.random.randint(1, 2)

                if dice_roll == 1:
                    $ renpy.say(Characters[0].voice, "*gag*")
                elif dice_roll == 2:
                    $ renpy.say(Characters[0].voice, "*cough*")
            else:
                $ dice_roll = renpy.random.randint(1, 3)

                if dice_roll == 1:
                    $ renpy.say(Characters[0].voice, "Oh. . .")
                elif dice_roll == 2:
                    $ renpy.say(Characters[0].voice, "*gasp*")
                elif dice_roll == 3:
                    $ renpy.say(Characters[0].voice, "Mmmm, [Characters[0].Player_petname], keep going.")
            
        $ Characters.remove(Characters[0])

    return