label makeout_initiations(Action):
    $ renpy.dynamic(temp_Characters = get_Action_Characters(Action))

    while temp_Characters:
        if renpy.random.random() > 0.5:
            $ subject = temp_Characters[0].name
            $ object = temp_Characters[0].name
            $ owner = temp_Characters[0].name + "'s"
        else:
            $ subject = "she"
            $ object = "her"
            $ owner = "her"
        
        $ dice_pool = [1, 2]

        if temp_Characters[0].desire >= 50:
            $ dice_pool.append(3)

        if temp_Characters[0].desire >= 75:
            $ dice_pool.append(4)

        if temp_Characters[0] in [Rogue]:
            $ dice_pool.append(5)

        if temp_Characters[0] in [Rogue, Jean]:
            $ dice_pool.append(6)

        if temp_Characters[0] in [Laura]:
            $ dice_pool.append(7)

        $ dice_roll = renpy.random.choice(dice_pool)

        if dice_roll == 1:
            $ temp_Characters[0].change_face("kiss2", blush = 1)

            $ renpy.say(None, f"You pull {object} in close, your lips eagerly coming together.")
        elif dice_roll == 2:
            $ temp_Characters[0].change_face("sexy")
            
            pause 1.0
            
            $ temp_Characters[0].change_face("kiss2", blush = 1)

            $ renpy.say(None, "You look at each other for a moment before pressing your lips together.")
        elif dice_roll == 3:
            $ temp_Characters[0].change_face("kiss2", blush = 1)

            $ renpy.say(None, f"{subject.capitalize()} moves in to kiss you, her tongue hungrily gliding across your lips.")
        elif dice_roll == 4:
            $ temp_Characters[0].change_face("kiss2", blush = 1)

            $ renpy.say(None, f"{subject.capitalize()} pulls you in tightly and eagerly pushes her tongue into your mouth.")
        elif dice_roll == 5:
            $ temp_Characters[0].change_face("sexy", mouth = "smirk")
            
            pause 1.0
            
            $ temp_Characters[0].change_face("kiss2", blush = 1)

            $ renpy.say(None, f"{subject.capitalize()} flashes a coy smile before nestling her body against you, her lips meeting yours.")
        elif dice_roll == 6:
            $ temp_Characters[0].change_face("kiss2", blush = 1)

            $ renpy.say(None, f"{subject.capitalize()} pulls you into her arms and kisses you, her lips soft and teasing.")
        elif dice_roll == 7:
            $ temp_Characters[0].change_face("kiss2", blush = 1)

            $ renpy.say(None, f"{subject.capitalize()} drags you in close, her lips firm against yours.")

        $ temp_Characters.remove(temp_Characters[0])

    return

label choke_initiations(Action):
    $ renpy.dynamic(temp_Characters = get_Action_Characters(Action))

    while temp_Characters:
        if renpy.random.random() > 0.5:
            $ subject = temp_Characters[0].name
            $ object = temp_Characters[0].name
            $ owner = temp_Characters[0].name + "'s"
        else:
            $ subject = "she"
            $ object = "her"
            $ owner = "her"
        
        $ dice_pool = [2]

        if temp_Characters[0].desire >= 75:
            $ dice_pool.append(3)

        if temp_Characters[0] in [Rogue, Jean]:
            $ dice_pool.append(4)

        if temp_Characters[0] in [Laura] and temp_Characters[0].desire >= 90:
            $ dice_pool.append(5)

        $ dice_roll = renpy.random.choice(dice_pool)

        if temp_Characters[0].desire < eval(f"{temp_Characters[0].tag}_Action_desire_thresholds['{Action.Action_type}']"):
            $ dice_pool = [1]

        if dice_roll == 1:
            $ temp_Characters[0].change_face("angry1", blush = 1)

            $ renpy.say(None, f"{subject.capitalize()} doesn't seem super enthused as your fingers wrap around her neck.")
        elif dice_roll == 2:
            $ temp_Characters[0].change_face("surprised1")
            $ temp_Characters[0].blush += 1 if temp_Characters[0].blush < 3 else 0

            $ renpy.say(None, f"You gently wrap your fingers around {owner} neck.")
        elif dice_roll == 3:
            $ temp_Characters[0].change_face("surprised1", eyes = "sexy")
            $ temp_Characters[0].blush += 1 if temp_Characters[0].blush < 3 else 0

            $ renpy.say(None, f"{subject.capitalize()} moans softly as your fingers encircle her throat.")
        elif dice_roll == 4:
            $ temp_Characters[0].change_face("surprised1")

            pause 1.0

            $ temp_Characters[0].change_face("surprised1", mouth = "smirk")

            $ temp_Characters[0].blush += 1 if temp_Characters[0].blush < 3 else 0

            $ renpy.say(None, f"{subject.capitalize()} gasps as you touch her neck, then flashes you a smirk.")
        elif dice_roll == 5:
            $ temp_Characters[0].change_face("snarl", mouth = "lipbite")

            $ renpy.say(None, f"{subject.capitalize()} lets out a feral moan.")

            $ temp_Characters[0].change_face("snarl")
            $ temp_Characters[0].blush += 1 if temp_Characters[0].blush < 3 else 0

            $ renpy.say(temp_Characters[0].voice, "Harder.")

        $ temp_Characters.remove(temp_Characters[0])

    return

label touch_thighs_over_clothes_initiations(Action):
    $ renpy.dynamic(temp_Characters = get_Action_Characters(Action))

    while temp_Characters:
        if renpy.random.random() > 0.5:
            $ subject = temp_Characters[0].name
            $ object = temp_Characters[0].name
            $ owner = temp_Characters[0].name + "'s"
        else:
            $ subject = "she"
            $ object = "her"
            $ owner = "her"

        $ dice_pool = [1]

        $ dice_roll = renpy.random.choice(dice_pool)

        if dice_roll == 1:
            $ renpy.say(None, f"You reach over to stroke {owner} thigh just above her knee, relishing the small contact even through her clothes.")

        $ temp_Characters.remove(temp_Characters[0])

    return

label touch_thighs_higher_over_clothes_initiations(Action):
    $ renpy.dynamic(temp_Characters = get_Action_Characters(Action))

    while temp_Characters:
        if renpy.random.random() > 0.5:
            $ subject = temp_Characters[0].name
            $ object = temp_Characters[0].name
            $ owner = temp_Characters[0].name + "'s"
        else:
            $ subject = "she"
            $ object = "her"
            $ owner = "her"

        $ dice_pool = [1]

        $ dice_roll = renpy.random.choice(dice_pool)

        if dice_roll == 1:
            $ renpy.say(None, f"Your fingertips trace out circles on {owner} thigh, edging closer and closer to her crotch.")
            $ renpy.say(None, f"You swear you can feel her warmth even through her clothes.")

        $ temp_Characters.remove(temp_Characters[0])

    return

label touch_thighs_initiations(Action):
    $ renpy.dynamic(temp_Characters = get_Action_Characters(Action))

    while temp_Characters:
        if renpy.random.random() > 0.5:
            $ subject = temp_Characters[0].name
            $ object = temp_Characters[0].name
            $ owner = temp_Characters[0].name + "'s"
        else:
            $ subject = "she"
            $ object = "her"
            $ owner = "her"

        $ dice_pool = [1]

        $ dice_roll = renpy.random.choice(dice_pool)

        if dice_roll == 1:
            $ renpy.say(None, f"You reach over to stroke {owner} thigh just above her knee, relishing the feel of her smooth, warm skin.")

        $ temp_Characters.remove(temp_Characters[0])

    return

label touch_thighs_higher_initiations(Action):
    $ renpy.dynamic(temp_Characters = get_Action_Characters(Action))

    while temp_Characters:
        if renpy.random.random() > 0.5:
            $ subject = temp_Characters[0].name
            $ object = temp_Characters[0].name
            $ owner = temp_Characters[0].name + "'s"
        else:
            $ subject = "she"
            $ object = "her"
            $ owner = "her"

        $ dice_pool = [1]

        $ dice_roll = renpy.random.choice(dice_pool)

        if dice_roll == 1:
            $ renpy.say(None, f"Your fingertips trace out circles on {owner} thigh, edging closer and closer to her crotch.")
            $ renpy.say(None, f"You can feel the warmth radiating from her pussy.")

        $ temp_Characters.remove(temp_Characters[0])

    return

label touch_breasts_over_clothes_initiations(Action):
    $ renpy.dynamic(temp_Characters = get_Action_Characters(Action))

    while temp_Characters:
        if renpy.random.random() > 0.5:
            $ subject = temp_Characters[0].name
            $ object = temp_Characters[0].name
            $ owner = temp_Characters[0].name + "'s"
        else:
            $ subject = "she"
            $ object = "her"
            $ owner = "her"

        if renpy.random.random() > 0.5:
            $ noun = "breasts"
        else:
            $ noun = "tits"

        $ dice_pool = [1, 2]

        if temp_Characters[0].desire >= 50:
            $ dice_pool.append(3)

        if temp_Characters[0] in [Rogue]:
            $ dice_pool.append(4)

        if temp_Characters[0] in [Laura]:
            $ dice_pool.append(5)

        if temp_Characters[0] in [Jean]:
            $ dice_pool.append(6)

        $ dice_roll = renpy.random.choice(dice_pool)

        if dice_roll == 1:
            $ renpy.say(None, f"You reach for {owner} {noun}, appreciating their perfect shape and weight even through her clothes.")
        elif dice_roll == 2:
            $ renpy.say(None, f"You start to fondle {owner} {noun}, her nipples firm against the palm of your hand even through her clothes.")
        elif dice_roll == 3:
            $ renpy.say(None, f"{subject.capitalize()} moans as you reach out to cup her clothed {noun}.")
        elif dice_roll == 4:
            $ renpy.say(None, f"You marvel as you reach out to cup {owner} supple {noun} - how are they still so perky?")
        elif dice_roll == 5:
            $ renpy.say(None, f"You reach out to fondle {owner} small and perky {noun} through her clothes.")
        elif dice_roll == 6:
            $ renpy.say(None, f"{subject.capitalize()} lets out a sigh as you take her perky {noun} in your hands.")

        $ temp_Characters.remove(temp_Characters[0])

    return

label touch_breasts_initiations(Action):
    $ renpy.dynamic(temp_Characters = get_Action_Characters(Action))

    while temp_Characters:
        if renpy.random.random() > 0.5:
            $ subject = temp_Characters[0].name
            $ object = temp_Characters[0].name
            $ owner = temp_Characters[0].name + "'s"
        else:
            $ subject = "she"
            $ object = "her"
            $ owner = "her"

        if renpy.random.random() > 0.5:
            $ noun = "breasts"
        else:
            $ noun = "tits"

        $ dice_pool = [1, 2]

        if temp_Characters[0].desire >= 50:
            $ dice_pool.append(3)

        if temp_Characters[0] in [Rogue]:
            $ dice_pool.append(4)

        if temp_Characters[0] in [Laura]:
            $ dice_pool.append(5)

        if temp_Characters[0] in [Jean]:
            $ dice_pool.append(6)

        $ dice_roll = renpy.random.choice(dice_pool)

        if dice_roll == 1:
            $ renpy.say(None, f"You reach for {owner} {noun}, appreciating their perfect shape and weight.")
        elif dice_roll == 2:
            $ renpy.say(None, f"You start to fondle {owner} {noun}, her nipples firm against the palm of your hand.")
        elif dice_roll == 3:
            $ renpy.say(None, f"{subject.capitalize()} moans as you reach out to cup her {noun}.")
        elif dice_roll == 4:
            $ renpy.say(None, f"You marvel as you reach out to cup {owner} supple {noun} - how are they still so perky?")
        elif dice_roll == 5:
            $ renpy.say(None, f"You reach out to fondle {owner} small and perky {noun}.")
        elif dice_roll == 6:
            $ renpy.say(None, f"{subject.capitalize()} lets out a sigh as you take her perky {noun} in your hands.")

        $ temp_Characters.remove(temp_Characters[0])

    return

label pinch_nipples_initiations(Action):
    $ renpy.dynamic(temp_Characters = get_Action_Characters(Action))

    while temp_Characters:
        if renpy.random.random() > 0.5:
            $ subject = temp_Characters[0].name
            $ object = temp_Characters[0].name
            $ owner = temp_Characters[0].name + "'s"
        else:
            $ subject = "she"
            $ object = "her"
            $ owner = "her"

        if renpy.random.random() > 0.75:
            $ adjective = "stiff "
        elif renpy.random.random() > 0.5:
            $ adjective = "sensitive "
        elif renpy.random.random() > 0.25:
            $ adjective = "firm "
        else:
            $ adjective = ""

        $ dice_pool = [1, 2, 3]

        if temp_Characters[0].desire >= 50:
            $ dice_pool.append(4)

        $ dice_roll = renpy.random.choice(dice_pool)

        if dice_roll == 1:
            $ renpy.say(None, f"You reach for {owner} breasts, your fingers closing in on her {adjective}nipples.")
        elif dice_roll == 2:
            $ renpy.say(None, f"You start to gently pinch and twist on {owner} {adjective}nipples.")
        elif dice_roll == 3:
            $ renpy.say(None, f"{owner.capitalize()} nipples stiffen against your fingers as you start to gently pinch them.")
        elif dice_roll == 4:
            $ renpy.say(None, f"{subject.capitalize()} moans and shudders as your fingers pinch her {adjective}nipples.")

        $ temp_Characters.remove(temp_Characters[0])

    return

label suck_nipples_initiations(Action):
    $ renpy.dynamic(temp_Characters = get_Action_Characters(Action))

    while temp_Characters:
        if renpy.random.random() > 0.5:
            $ subject = temp_Characters[0].name
            $ object = temp_Characters[0].name
            $ owner = temp_Characters[0].name + "'s"
        else:
            $ subject = "she"
            $ object = "her"
            $ owner = "her"

        if renpy.random.random() > 0.75:
            $ adjective = "stiff "
        elif renpy.random.random() > 0.5:
            $ adjective = "sensitive "
        elif renpy.random.random() > 0.25:
            $ adjective = "firm "
        else:
            $ adjective = ""

        $ dice_pool = [1, 2, 3]

        if temp_Characters[0].desire >= 50:
            $ dice_pool.append(4)

        $ dice_roll = renpy.random.choice(dice_pool)

        if dice_roll == 1:
            $ renpy.say(None, f"You pull {owner} breast to your face and delight in suckling on her {adjective}nipples, drawing them eagerly into your mouth.")
        elif dice_roll == 2:
            $ renpy.say(None, f"You hungrily lean down to lick and suck on {owner} {adjective}nipples.")
        elif dice_roll == 3:
            $ renpy.say(None, f"{owner.capitalize()} nipples are already firm as you begin to suck on them tenderly.")
        elif dice_roll == 4:
            $ renpy.say(None, f"{subject.capitalize()} moans in appreciating as you start to nurse on her {adjective}nipples.")

        $ temp_Characters.remove(temp_Characters[0])

    return

label touch_pussy_over_clothes_initiations(Action):
    $ renpy.dynamic(temp_Characters = get_Action_Characters(Action))

    while temp_Characters:
        if renpy.random.random() > 0.5:
            $ subject = temp_Characters[0].name
            $ object = temp_Characters[0].name
            $ owner = temp_Characters[0].name + "'s"
        else:
            $ subject = "she"
            $ object = "her"
            $ owner = "her"

        if renpy.random.random() > 0.5:
            $ noun = "pussy"
        else:
            $ noun = "crotch"

        $ dice_pool = [1]

        $ dice_roll = renpy.random.choice(dice_pool)

        if dice_roll == 1:
            $ renpy.say(None, f"You caress {owner} {noun} through her clothes, tenderly tracing out the fold of her labia.")

        $ temp_Characters.remove(temp_Characters[0])

    return

label touch_pussy_initiations(Action):
    $ renpy.dynamic(temp_Characters = get_Action_Characters(Action))

    while temp_Characters:
        if renpy.random.random() > 0.5:
            $ subject = temp_Characters[0].name
            $ object = temp_Characters[0].name
            $ owner = temp_Characters[0].name + "'s"
        else:
            $ subject = "she"
            $ object = "her"
            $ owner = "her"

        if renpy.random.random() > 0.66:
            $ noun = "folds"
        elif renpy.random.random() > 0.33:
            $ noun = "cunt"
        else:
            $ noun = "pussy"

        if renpy.random.random() > 0.75 and temp_Characters[0].desire >= 75:
            $ adjective = "soaking wet "
        elif renpy.random.random() > 0.5:
            if temp_Characters[0].body_hair["pubic"] in ["bush", "hairy"]:
                $ adjective = "hairy "
            else:
                $ adjective = "smooth "
        elif renpy.random.random() > 0.25:
            $ adjective = "inviting "
        else:
            $ adjective = ""

        $ dice_pool = [1]

        $ dice_roll = renpy.random.choice(dice_pool)

        if dice_roll == 1:
            $ renpy.say(None, f"You caress {owner} {adjective}{noun} as she sighs in contentment.")

        $ temp_Characters.remove(temp_Characters[0])

    return

label finger_pussy_initiations(Action):
    $ renpy.dynamic(temp_Characters = get_Action_Characters(Action))

    while temp_Characters:
        if renpy.random.random() > 0.5:
            $ subject = temp_Characters[0].name
            $ object = temp_Characters[0].name
            $ owner = temp_Characters[0].name + "'s"
        else:
            $ subject = "she"
            $ object = "her"
            $ owner = "her"

        if renpy.random.random() > 0.66:
            $ noun = "hole"
        elif renpy.random.random() > 0.33:
            $ noun = "folds"
        else:
            $ noun = "pussy"

        if renpy.random.random() > 0.75 and temp_Characters[0].desire >= 75:
            $ adjective = "soaking wet "
        elif renpy.random.random() > 0.5:
            if temp_Characters[0].body_hair["pubic"] in ["bush", "hairy"]:
                $ adjective = "hairy "
            else:
                $ adjective = "smooth "
        elif renpy.random.random() > 0.25:
            $ adjective = "glistening "
        else:
            $ adjective = ""

        $ dice_pool = [2, 3]

        if temp_Characters[0].desire >= 75:
            $ dice_pool.append(4)

        if temp_Characters[0].desire < eval(f"{temp_Characters[0].tag}_Action_desire_thresholds['{Action.Action_type}']"):
            if renpy.random.random() > 0.5:
                $ temp_Characters[0].change_face("confused1", eyes = "left")
            else:
                $ temp_Characters[0].change_face("confused1", eyes = "right")

            $ dice_pool = [1]
        else:
            if renpy.random.random() > 0.66:
                $ temp_Characters[0].change_face("sexy")
            elif renpy.random.random() > 0.33:
                $ temp_Characters[0].change_face("sexy", mouth = "lipbite")
            else:
                $ temp_Characters[0].change_face("sexy", mouth = "open") 

        $ dice_roll = renpy.random.choice(dice_pool)

        if dice_roll == 1:
            $ renpy.say(None, f"{subject.capitalize()} seems a little uncomfortable as you start pushing your fingers into her {adjective}{noun}.")
        elif dice_roll == 2:
            $ renpy.say(None, f"Your fingers glide across {owner} {adjective}{noun}, already slick and inviting, and you start gently pushing them inside.")
        elif dice_roll == 3:
            $ renpy.say(None, f"{subject.capitalize()} gasps as you enter her {adjective}{noun}, and you feel her tense around your fingers.")
        elif dice_roll == 4:
            $ renpy.say(None, f"{subject.capitalize()} seems desperate for you to push your fingers deep into her{adjective}{noun}.")

        $ temp_Characters.remove(temp_Characters[0])

    return

label eat_pussy_initiations(Action):
    $ renpy.dynamic(temp_Characters = get_Action_Characters(Action))

    while temp_Characters:
        if renpy.random.random() > 0.5:
            $ subject = temp_Characters[0].name
            $ object = temp_Characters[0].name
            $ owner = temp_Characters[0].name + "'s"
        else:
            $ subject = "she"
            $ object = "her"
            $ owner = "her"

        if renpy.random.random() > 0.66:
            $ noun = "folds"
        elif renpy.random.random() > 0.33:
            $ noun = "labia"
        else:
            $ noun = "pussy"

        if renpy.random.random() > 0.75 and temp_Characters[0].desire >= 75:
            $ adjective = "soaking wet "
        elif renpy.random.random() > 0.5:
            if temp_Characters[0].body_hair["pubic"] in ["bush", "hairy"]:
                $ adjective = "hairy "
            else:
                $ adjective = "smooth "
        elif renpy.random.random() > 0.25:
            $ adjective = "glistening "
        else:
            $ adjective = ""

        if renpy.random.random() > 0.66:
            $ temp_Characters[0].change_face("sexy", eyes = "down", blush = 2)
        elif renpy.random.random() > 0.33:
            $ temp_Characters[0].change_face("sexy", eyes = "down", mouth = "lipbite", blush = 2)
        else:
            $ temp_Characters[0].change_face("sexy", eyes = "down", mouth = "agape", blush = 2) 

        $ dice_pool = [1, 2, 3, 4]

        if temp_Characters[0].desire >= 75:
            $ dice_pool.append(5)
            $ dice_pool.append(6)
            $ dice_pool.append(7)

        $ dice_roll = renpy.random.choice(dice_pool)
        
        if dice_roll == 1:
            $ renpy.say(None, f"You bring your lips up to {owner} {adjective}{noun}, giving it a gentle kiss before slowly teasing her with your tongue.")
        elif dice_roll == 2:
            $ renpy.say(None, f"{subject.capitalize()} shudders as your tongue makes contact with her {adjective}{noun}, gliding back and forth.")
        elif dice_roll == 3:
            $ renpy.say(None, f"You let out an appreciative sigh as you taste {owner} {adjective}{noun} - delicious.")
        elif dice_roll == 4:
            $ renpy.say(None, f"{subject.capitalize()} gasps and twitches as you draw your tongue in circles around her {adjective}{noun}.")
        elif dice_roll == 5:
            $ renpy.say(None, f"{subject.capitalize()} moans and eagerly pulls your face against her {adjective}{noun}, grinding back and forth on your tongue.")
        elif dice_roll == 6:
            $ renpy.say(None, f"{owner.capitalize()} {noun} is dripping with grool as you bring your face in close and take a deep breath.")
        elif dice_roll == 7:
            $ renpy.say(None, f"As you pull in close, you lovingly lick at {owner} sopping wet {noun}, her heady aroma making you dizzy.")

        $ temp_Characters.remove(temp_Characters[0])

    return

label grab_ass_over_clothes_initiations(Action):
    $ renpy.dynamic(temp_Characters = get_Action_Characters(Action))

    while temp_Characters:
        if renpy.random.random() > 0.5:
            $ subject = temp_Characters[0].name
            $ object = temp_Characters[0].name
            $ owner = temp_Characters[0].name + "'s"
        else:
            $ subject = "she"
            $ object = "her"
            $ owner = "her"

        $ dice_pool = []

        if temp_Characters[0] in [Rogue]:
            $ dice_pool.append(1)
        
        if temp_Characters[0] in [Laura]:
            $ dice_pool.append(2)

        if temp_Characters[0] in [Jean]:
            $ dice_pool.append(3)

        $ dice_roll = renpy.random.choice(dice_pool)

        if dice_roll == 1:
            $ renpy.say(None, f"You wrap your hand around {owner} voluptuous ass. It spills through your fingers, soft and inviting even through her clothes.")
        elif dice_roll == 2:
            $ renpy.say(None, f"You wrap your hand around {owner} muscular ass. You trace the firmness of her glutes, palpable even through her clothes.")
        elif dice_roll == 3:
            $ renpy.say(None, f"You wrap your hand around {owner} tight ass. It comfortably fits in your hand, supple yet firm, even through her clothes.")

        $ temp_Characters.remove(temp_Characters[0])

    return

label grab_ass_initiations(Action):
    $ renpy.dynamic(temp_Characters = get_Action_Characters(Action))

    while temp_Characters:
        if renpy.random.random() > 0.5:
            $ subject = temp_Characters[0].name
            $ object = temp_Characters[0].name
            $ owner = temp_Characters[0].name + "'s"
        else:
            $ subject = "she"
            $ object = "her"
            $ owner = "her"

        $ dice_pool = []

        if temp_Characters[0] in [Rogue]:
            $ dice_pool.append(1)
        
        if temp_Characters[0] in [Laura]:
            $ dice_pool.append(2)

        if temp_Characters[0] in [Jean]:
            $ dice_pool.append(3)

        $ dice_roll = renpy.random.choice(dice_pool)

        if dice_roll == 1:
            $ renpy.say(None, f"You wrap your hand around {owner} voluptuous ass. It spills through your fingers, soft and inviting, her skin warm to the touch.")
        elif dice_roll == 2:
            $ renpy.say(None, f"You wrap your hand around {owner} muscular ass. You trace the firmness of her glutes, her skin soft and warm.")
        elif dice_roll == 3:
            $ renpy.say(None, f"You wrap your hand around {owner} tight ass. It comfortably fits in your hand, supple yet firm, her skin soft and warm.")

        $ temp_Characters.remove(temp_Characters[0])

    return

label finger_ass_initiations(Action):
    $ renpy.dynamic(temp_Characters = get_Action_Characters(Action))

    while temp_Characters:
        if renpy.random.random() > 0.5:
            $ subject = temp_Characters[0].name
            $ object = temp_Characters[0].name
            $ owner = temp_Characters[0].name + "'s"
        else:
            $ subject = "she"
            $ object = "her"
            $ owner = "her"

        if renpy.random.random() > 0.66:
            $ noun = "asshole"
        elif renpy.random.random() > 0.33:
            $ noun = "hole"
        else:
            $ noun = "ass"

        if renpy.random.random() > 0.75 and temp_Characters[0].desire >= 75:
            $ adjective = "hungry "
        elif renpy.random.random() > 0.5:
            if temp_Characters[0].body_hair["anus"] in ["hairy"]:
                $ adjective = "hairy "
            else:
                $ adjective = "smooth "
        elif renpy.random.random() > 0.25:
            $ adjective = "tight "
        else:
            $ adjective = ""

        $ dice_pool = [2, 3, 4, 5]

        if temp_Characters[0].desire >= 75:
            $ dice_pool.append(6)

        if temp_Characters[0].History.check("finger_ass") >= 2:
            $ dice_pool.append(7)

        if temp_Characters[0].History.check("finger_ass") >= 5:
            $ dice_pool.append(8)

        if temp_Characters[0].desire < eval(f"{temp_Characters[0].tag}_Action_desire_thresholds['{Action.Action_type}']"):
            if renpy.random.random() > 0.5:
                $ temp_Characters[0].change_face("grimace", eyes = "left")
            else:
                $ temp_Characters[0].change_face("grimace", eyes = "right")

            $ dice_pool = [1]
        else:
            if renpy.random.random() > 0.66:
                $ temp_Characters[0].change_face("surprised1", blush = 2)
            elif renpy.random.random() > 0.33:
                $ temp_Characters[0].change_face("surprised1", mouth = "lipbite", blush = 2)
            else:
                $ temp_Characters[0].change_face("surprised1", mouth = "agape", blush = 2)

        $ dice_roll = renpy.random.choice(dice_pool)

        if dice_roll == 1:
            $ renpy.say(None, f"{subject.capitalize()} squirms uncomfortably as you put pressure on her {adjective}{noun}.")
        elif dice_roll == 2:
            $ renpy.say(None, f"You press your finger up against {owner} {adjective}{noun}, slowly pressing it inside against the resistance. She involuntarily tightens around your finger, but manages to relax as it slides in all the way.")
        elif dice_roll == 3:
            $ renpy.say(None, f"You tease {owner} {adjective}{noun} before exerting enough pressure to slip your finger past her resistance.")
        elif dice_roll == 4:
            $ renpy.say(None, f"{subject.capitalize()} gasps as you circle her {adjective}{noun} with your finger.")
        elif dice_roll == 5:
            $ renpy.say(None, f"You enjoy the feeling of {owner} {adjective}{noun} on the tips of your fingers before pressing a digit through the barrier.")
        elif dice_roll == 6:
            $ renpy.say(None, f"{subject.capitalize()} moans appreciatively as you push two fingers inside her {adjective}{noun}.")
        elif dice_roll == 7:
            $ renpy.say(None, f"{subject.capitalize()} is still not used to putting anything up there, and you encounter some resistance as your press your finger up against her {adjective}{noun}. Eventually it slides in, and she tightens around you.")
        elif dice_roll == 8:
            $ renpy.say(None, f"As you press your finger up against her {adjective}{noun}, {subject} leans back into you, inviting it inside. Your finger slides in easily, eliciting a soft moan.")

        $ temp_Characters.remove(temp_Characters[0])

    return

label eat_ass_initiations(Action):
    $ renpy.dynamic(temp_Characters = get_Action_Characters(Action))

    while temp_Characters:
        if renpy.random.random() > 0.5:
            $ subject = temp_Characters[0].name
            $ object = temp_Characters[0].name
            $ owner = temp_Characters[0].name + "'s"
        else:
            $ subject = "she"
            $ object = "her"
            $ owner = "her"

        if renpy.random.random() > 0.66:
            $ noun = "asshole"
        elif renpy.random.random() > 0.33:
            $ noun = "hole"
        else:
            $ noun = "ass"

        if renpy.random.random() > 0.66:
            if temp_Characters[0].body_hair["anus"] in ["hairy"]:
                $ adjective = "hairy "
            else:
                $ adjective = "smooth "
        elif renpy.random.random() > 0.33:
            $ adjective = "perfect "
        else:
            $ adjective = ""

        if renpy.random.random() > 0.66:
            $ temp_Characters[0].change_face("sexy", eyes = "down", blush = 2)
        elif renpy.random.random() > 0.33:
            $ temp_Characters[0].change_face("sexy", eyes = "down", mouth = "lipbite", blush = 2)
        else:
            $ temp_Characters[0].change_face("sexy", eyes = "down", mouth = "agape", blush = 2) 

        $ dice_pool = [1, 2, 3, 4]

        if temp_Characters[0].desire >= 75:
            $ dice_pool.append(5)

        if temp_Characters[0] in [Rogue]:
            $ dice_pool.append(6)

        if temp_Characters[0] in [Laura]:
            $ dice_pool.append(7)

        if temp_Characters[0] in [Jean]:
            $ dice_pool.append(8)

        $ dice_roll = renpy.random.choice(dice_pool)

        if dice_roll == 1:
            $ renpy.say(None, f"Spreading {owner} cheeks with your hands, you slowly drag your tongue along her crack, circling around, licking anywhere but her {adjective}{noun}.")
        elif dice_roll == 2:
            $ renpy.say(None, f"{subject.capitalize()} shudders as you give her {adjective}{noun} a kiss before fully diving in with your tongue.")
        elif dice_roll == 3:
            $ renpy.say(None, f"You bury your face in {owner} ass and dart your tongue out at her {adjective}{noun}.")
        elif dice_roll == 4:
            $ renpy.say(None, f"You lick a straight line from {owner} taint to her ass before eagerly lapping at her {adjective}hole.")
        elif dice_roll == 5:
            $ renpy.say(None, f"{subject.capitalize()} moans eagerly as you tongue her {adjective}{noun}.")
        elif dice_roll == 6:
            $ renpy.say(None, f"{owner.capitalize()} full ass envelops your face as your tongue darts out to lick her {adjective}asshole.")
        elif dice_roll == 7:
            $ renpy.say(None, f"You enjoy the feeling of {owner} muscular ass against your face as your tongue darts out to lick her {adjective}asshole.")
        elif dice_roll == 8:
            $ renpy.say(None, f"You caress {owner} perky ass as your tongue darts out to lick her {adjective}asshole.")

        $ temp_Characters.remove(temp_Characters[0])

    return

label handjob_initiations(Action):
    $ renpy.dynamic(temp_Characters = get_Action_Characters(Action))

    while temp_Characters:
        if renpy.random.random() > 0.5:
            $ subject = temp_Characters[0].name
            $ object = temp_Characters[0].name
            $ owner = temp_Characters[0].name + "'s"
        else:
            $ subject = "she"
            $ object = "her"
            $ owner = "her"

        if temp_Characters[0].History.check("handjob") >= 2:
            if temp_Characters[0] in [Rogue]:
                $ temp_Characters[0].change_face("sexy", eyes = "down", blush = 2)
            elif temp_Characters[0] in [Laura]:
                $ temp_Characters[0].change_face("sly", mouth = "lipbite", blush = 2)
            elif temp_Characters[0] in [Jean]:
                $ temp_Characters[0].change_face("sexy", eyes = "down", blush = 2) 

            $ dice_pool = [1, 2]

            if temp_Characters[0] in [Jean]:
                $ dice_pool.append(3)

            $ dice_roll = renpy.random.choice(dice_pool)

            if dice_roll == 1:
                $ renpy.say(None, f"{subject.capitalize()} reaches out excitedly, wrapping her fingers around you and relishing the sensation of you in her hand.")
            elif dice_roll == 2:
                $ renpy.say(None, f"{subject.capitalize()} doesn't waste any time and grabs you as if she's been waiting for this all day, her gaze locked onto yours with a glint of desire.")
            elif dice_roll == 3:
                $ renpy.say(None, f"{subject.capitalize()} teases you a bit with some light touches, enjoying how you involuntarily twitch, before finally wrapping her fingers around you.")
        else:
            if temp_Characters[0] in [Rogue]:
                $ temp_Characters[0].change_face("worried1", eyes = "down", mouth = "lipbite", blush = 2) 
                
                $ renpy.say(None, f"{subject.capitalize()} tentatively reaches out, slowly wrapping her fingers around you. She relishes the feeling of you between her fingers, before starting to move.")
                
                $ temp_Characters[0].change_face("worried1", mouth = "lipbite", blush = 2) 
                
                $ renpy.say(temp_Characters[0].voice, "Let me know if ah do anythin' wrong. . .")
            elif temp_Characters[0] in [Laura]:
                $ temp_Characters[0].change_face("confused1", eyes = "down", mouth = "lipbite", blush = 2) 
                
                $ renpy.say(None, f"{subject.capitalize()} reaches out, grabbing you as if she expects it to run off. Her grip is tight, and she spends a moment marveling at the sensation before starting to move.")
                
                $ temp_Characters[0].change_face("confused1", mouth = "lipbite", blush = 2) 
                
                $ renpy.say(temp_Characters[0].voice, "It feels. . . interesting. . .")
            elif temp_Characters[0] in [Jean]:
                $ temp_Characters[0].change_face("worried1", eyes = "down", mouth = "lipbite", blush = 2) 
                
                $ renpy.say(None, f"{subject.capitalize()} reaches out, dragging a finger across your length, feeling the novel texture. She gently wraps her fingers around you, a bit too gently, before starting to move.")
                
                $ temp_Characters[0].change_face("worried1", mouth = "smirk", blush = 2) 
                
                $ renpy.say(temp_Characters[0].voice, "This is how you do it, right?")

        $ temp_Characters.remove(temp_Characters[0])

    return

label fondle_balls_initiations(Action):
    $ renpy.dynamic(temp_Characters = get_Action_Characters(Action))

    while temp_Characters:
        if renpy.random.random() > 0.5:
            $ subject = temp_Characters[0].name
            $ object = temp_Characters[0].name
            $ owner = temp_Characters[0].name + "'s"
        else:
            $ subject = "she"
            $ object = "her"
            $ owner = "her"

        $ dice_pool = [1]

        $ dice_roll = renpy.random.choice(dice_pool)

        if dice_roll == 1:
            $ renpy.say(None, f"{subject.capitalize()} starts gingerly fondling and massaging your balls with her fingers.")

        $ temp_Characters.remove(temp_Characters[0])

    return

label blowjob_initiations(Action):
    $ renpy.dynamic(temp_Characters = get_Action_Characters(Action))

    while temp_Characters:
        if renpy.random.random() > 0.5:
            $ subject = temp_Characters[0].name
            $ object = temp_Characters[0].name
            $ owner = temp_Characters[0].name + "'s"
        else:
            $ subject = "she"
            $ object = "her"
            $ owner = "her"

        if Action.mode == 3:
            if temp_Characters[0].History.check("blowjob") >= 2:
                if temp_Characters[0] in [Rogue]:
                    $ temp_Characters[0].change_face("sexy", blush = 2) 
                elif temp_Characters[0] in [Laura]:
                    $ temp_Characters[0].change_face("sly", mouth = "lipbite", blush = 2) 
                elif temp_Characters[0] in [Jean]:
                    $ temp_Characters[0].change_face("sexy", blush = 2) 
                    
                $ dice_pool = [1, 2]

                if temp_Characters[0] in [Jean]:
                    $ dice_pool.append(3)

                $ dice_roll = renpy.random.choice(dice_pool)

                if dice_roll == 1:
                    $ renpy.say(None, f"{subject.capitalize()} eagerly wraps her lips around you and starts sucking with enthusiasm.")
                elif dice_roll == 2:
                    $ renpy.say(None, f"{subject.capitalize()} pulls you into her mouth without hesitation.")
                elif dice_roll == 3:
                    $ renpy.say(None, f"{subject.capitalize()} teases you a bit, thoroughly enjoying the look on your face, before finally wrapping her lips around you.")
            else:
                if temp_Characters[0] in [Rogue]:
                    $ temp_Characters[0].change_face("worried1", mouth = "lipbite", blush = 2) 
                    
                    $ renpy.say(temp_Characters[0].voice, "Ah'll try my best. . .")
                    
                    $ temp_Characters[0].change_face("worried1", eyes = "down", mouth = "lipbite", blush = 2) 
                    
                    $ renpy.say(None, f"{subject.capitalize()} tentatively laps her lips around the head, slowly bringing you inside her mouth.")
                elif temp_Characters[0] in [Laura]:
                    $ temp_Characters[0].change_face("confused1", mouth = "lipbite", blush = 2) 
                    
                    $ renpy.say(temp_Characters[0].voice, "I still don't fully understand how this works. . .")
                    
                    $ temp_Characters[0].change_face("sexy", eyes = "down", blush = 2) 
                    
                    $ renpy.say(temp_Characters[0].voice, "But it does taste good.")
                    
                    $ renpy.say(None, f"{subject.capitalize()} eagerly wraps her lips around you, but brings you in a bit too deep, causing her to gag and pull back a bit.")
                elif temp_Characters[0] in [Jean]:
                    $ temp_Characters[0].change_face("worried1", mouth = "lipbite", blush = 2) 
                    
                    $ renpy.say(temp_Characters[0].voice, "It really is that big. . .")
                    
                    $ temp_Characters[0].change_face("worried1", eyes = "down", mouth = "lipbite", blush = 2) 
                    
                    $ renpy.say(temp_Characters[0].voice, "Don't expect me to take it too deep.")

                    $ renpy.say(None, f"With some hesitation, {subject} wraps her lips around you, only bringing in a couple inches.")
        else:
            if temp_Characters[0].History.check("blowjob") >= 2:
                if temp_Characters[0] in [Rogue]:
                    $ temp_Characters[0].change_face("sexy", eyes = "down", blush = 2)
                elif temp_Characters[0] in [Laura]:
                    $ temp_Characters[0].change_face("sly", eyes = "down", mouth = "lipbite", blush = 2)
                elif temp_Characters[0] in [Jean]:
                    $ temp_Characters[0].change_face("sexy", eyes = "down", blush = 2) 
                    
                $ dice_pool = [1, 2]

                if temp_Characters[0] in [Jean]:
                    $ dice_pool.append(3)

                $ dice_roll = renpy.random.choice(dice_pool)

                if dice_roll == 1:
                    $ renpy.say(None, f"{subject.capitalize()} reaches out excitedly, pulling you up to her lips, hungry for the feeling of you in her mouth.")
                elif dice_roll == 2:
                    $ renpy.say(None, f"{subject.capitalize()} pulls you up to her mouth, not wasting a single second as her lips press into your cock.")
                elif dice_roll == 3:
                    $ renpy.say(None, f"{subject.capitalize()} teases you a bit with some gentle kissing, enjoying how you involuntarily twitch, before finally pressing her lips up against your cock.")
            else:
                if temp_Characters[0] in [Rogue]:
                    $ temp_Characters[0].change_face("worried2", mouth = "lipbite", blush = 2) 
                    
                    $ renpy.say(temp_Characters[0].voice, "It's still a bit dauntin'. . . how big it is. . .") 
                    
                    $ temp_Characters[0].change_face("worried1", eyes = "down", mouth = "kiss", blush = 2) 
                    
                    $ renpy.say(None, f"{subject.capitalize()} slowly brings her lips down to you, lightly brushing them against your cock. After the first touch, it seems like she can't help herself and goes in for more.") 
                    
                    $ temp_Characters[0].change_face("worried1", mouth = "lipbite", blush = 2) 
                    
                    $ renpy.say(temp_Characters[0].voice, "Ah love how it feels on my lips. . .")
                elif temp_Characters[0] in [Laura]:
                    $ temp_Characters[0].change_face("confused1", eyes = "down", mouth = "lipbite", blush = 2) 
                    
                    $ renpy.say(temp_Characters[0].voice, "I'm not certain. . . my mouth is big enough. . .")
                    
                    $ temp_Characters[0].change_face("confused1", eyes = "down", mouth = "kiss", blush = 2) 
                    
                    $ renpy.say(None, f"Despite her uncertainty, {subject} presses her lips up against you, inhaling your scent all the while.")
                    
                    $ temp_Characters[0].change_face("sly", mouth = "lipbite", blush = 2) 
                    
                    $ renpy.say(None, "After that first touch, she gets a feral gleam in her eye.")

                    $ renpy.say(temp_Characters[0].voice, "Hmmm. . .")
                elif temp_Characters[0] in [Jean]:
                    $ temp_Characters[0].change_face("worried1", eyes = "down", mouth = "lipbite", blush = 2) 
                    
                    $ renpy.say(temp_Characters[0].voice, "God, it's so big. . .")
                    
                    $ temp_Characters[0].change_face("worried1", eyes = "down", mouth = "kiss", blush = 2) 
                    
                    $ renpy.say(None, f"{subject.capitalize()} slowly pulls her lips down to you, touching them lightly to your cock causing you to involuntarily twitch. She still seems apprehensive, but seeing you twitch like that. . .") 
                    
                    $ temp_Characters[0].change_face("sly", mouth = "lipbite", blush = 2) 
                    
                    $ renpy.say(temp_Characters[0].voice, "You liked that?")

        $ temp_Characters.remove(temp_Characters[0])

    return

label suck_balls_initiations(Action):
    $ renpy.dynamic(temp_Characters = get_Action_Characters(Action))

    while temp_Characters:
        $ temp_Characters.remove(temp_Characters[0])

    return

label deepthroat_initiations(Action):
    $ renpy.dynamic(temp_Characters = get_Action_Characters(Action))

    while temp_Characters:
        if renpy.random.random() > 0.5:
            $ subject = temp_Characters[0].name
            $ object = temp_Characters[0].name
            $ owner = temp_Characters[0].name + "'s"
        else:
            $ subject = "she"
            $ object = "her"
            $ owner = "her"

        if temp_Characters[0].History.check("deepthroat") >= 2:
            if temp_Characters[0].throat_training == 1:
                if temp_Characters[0] in [Rogue]:
                    $ temp_Characters[0].change_face("worried1", mouth = "lipbite", blush = 2) 
                elif temp_Characters[0] in [Laura]:
                    $ temp_Characters[0].change_face("angry1", mouth = "lipbite", blush = 2)
                elif temp_Characters[0] in [Jean]:
                    $ temp_Characters[0].change_face("worried1", mouth = "lipbite", blush = 2)

                $ dice_pool = [1, 2]
                
                if temp_Characters[0] in [Laura]:
                    $ dice_pool.append(3)

                $ dice_roll = renpy.random.choice(dice_pool)

                if dice_roll == 1:
                    $ temp_Characters[0].eyes = "down"

                    $ renpy.say(None, f"{owner.capitalize()} eyes are locked on your cock, sizing you up.")
                elif dice_roll == 2:
                    $ temp_Characters[0].eyes = "down"
                    
                    $ renpy.say(None, f"{subject.capitalize()} looks down at you, a bit apprehensive.")
                elif dice_roll == 3:
                    $ temp_Characters[0].eyes = "down"
                    
                    $ renpy.say(None, f"{subject.capitalize()} has a determined look on her face, as she gets ready to try and take you all in.")
                    $ renpy.say(None, "Her lips wrap around you, but it doesn't seem like she's learned much as she goes too deep too fast and gags.")

                if dice_roll in [1, 2]:
                    if renpy.random.random > 0.5:
                        $ renpy.say(None, "After a bit of hesitation, she finally takes you into her mouth.")
                    else:
                        $ renpy.say(None, "She tentatively wraps her lips around you, taking you in slowly.")
            elif temp_Characters[0].throat_training == 2:
                if temp_Characters[0] in [Rogue]:
                    $ temp_Characters[0].change_face("sexy", blush = 2) 
                elif temp_Characters[0] in [Laura]:
                    $ temp_Characters[0].change_face("angry1", mouth = "lipbite", blush = 2) 
                elif temp_Characters[0] in [Jean]:
                    $ temp_Characters[0].change_face("confused1", mouth = "lipbite", blush = 2) 
                    
                $ dice_pool = [1, 2]
                
                if temp_Characters[0] in [Laura]:
                    $ dice_pool.append(3)

                $ dice_roll = renpy.random.choice(dice_pool)

                if dice_roll == 1:
                    $ renpy.say(None, f"{subject.capitalize()} looks into your eyes, a gleam of excitement in her own.")
                elif dice_roll == 2:
                    $ temp_Characters[0].eyes = "down"

                    $ renpy.say(None, f"{subject.capitalize()} looks down at your cock with less apprehension than before.")
                elif dice_roll == 3:
                    $ temp_Characters[0].eyes = "down"

                    $ renpy.say(None, f"{subject.capitalize()} stares down at your cock for a while, like a predator sizing up its prey.")
                    $ renpy.say(None, "Her lips wrap around you, more cautiously this time, and she takes things slow.")

                if dice_roll in [1, 2]:
                    if renpy.random.random() > 0.5:
                        $ renpy.say(None, "She wraps her lips around you, taking you in with more confidence than before.")
                    else:
                        $ renpy.say(None, "You can tell she's starting to get a bit more confident as she takes you deeper into her mouth.")
            elif temp_Characters[0].throat_training == 3:
                if temp_Characters[0] in [Rogue]:
                    $ temp_Characters[0].change_face("sexy", blush = 2) 
                elif temp_Characters[0] in [Laura]:
                    $ temp_Characters[0].change_face("sexy", blush = 2) 
                elif temp_Characters[0] in [Jean]:
                    $ temp_Characters[0].change_face("sexy", blush = 2) 
                    
                $ dice_pool = [1, 2, 3]

                $ dice_roll = renpy.random.choice(dice_pool)

                if dice_roll == 1:
                    $ temp_Characters[0].eyes = "down"

                    $ renpy.say(None, f"{subject.capitalize()} looks down at your cock, ready to take you as deep as she can handle.")
                    $ renpy.say(None, "She wraps her lips around you with zero hesitation and nearly swallows your whole cock.")
                elif dice_roll == 2:
                    $ renpy.say(None, f"{subject.capitalize()} stares into your eyes, a gleam of excitement in them.")
                    
                    $ temp_Characters[0].eyes = "down"
                    
                    $ renpy.say(None, "She hungrily wraps her lips around you, taking you deeper down her throat and showing all the progress she's made so far.")
                elif dice_roll == 3:
                    $ renpy.say(None, f"{subject.capitalize()} doesn't hesitate to take you deep into her mouth, showing off all her progress.")
            elif temp_Characters[0].throat_training == 4:
                if temp_Characters[0] in [Rogue]:
                    $ temp_Characters[0].change_face("sexy", eyes = "down", blush = 2) 
                elif temp_Characters[0] in [Laura]:
                    $ temp_Characters[0].change_face("sly", mouth = "lipbite", blush = 2) 
                elif temp_Characters[0] in [Jean]:
                    $ temp_Characters[0].change_face("sly", mouth = "lipbite", blush = 2) 
                    
                $ dice_pool = [1, 2]

                if temp_Characters[0].desire >= 50:
                    $ dice_pool.append(3)

                $ dice_roll = renpy.random.choice(dice_pool)

                if dice_roll == 1:
                    $ renpy.say(None, f"{subject.capitalize()} stares into your eyes - you get a sense of self-satisfaction in them." )
                    
                    $ temp_Characters[0].eyes = "down"
                    
                    $ renpy.say(None, "She doesn't hesitate for a second, wrapping her lips around you, ready to take you all the way.")
                elif dice_roll == 2:
                    $ renpy.say(None, f"With more confidence than ever, {subject} wraps her lips around you, ready to take you in all the way.")
                elif dice_roll == 3:
                    $ temp_Characters[0].eyes = "down"

                    $ renpy.say(None, f"{subject.capitalize()} looks down at your cock with lustful eyes.")
                    $ renpy.say(None, "She starts taking you in like she's been waiting for this all day.")
        else:
            if temp_Characters[0] in [Rogue]:
                $ temp_Characters[0].change_face("worried1", eyes = "down", mouth = "lipbite", blush = 2) 
                
                $ renpy.say(None, f"{subject.capitalize()} stares down at your cock, a bit daunted by the task in front of her.")
                $ renpy.say(temp_Characters[0].voice, "Ah reckon it'll be a while before ah can take all of it. . .")
            elif temp_Characters[0] in [Laura]:
                $ temp_Characters[0].change_face("confused2", blush = 2) 
                
                $ renpy.say(temp_Characters[0].voice, "I am supposed to swallow all of it?")
                
                $ temp_Characters[0].change_face("confused1", eyes = "down", mouth = "lipbite", blush = 2) 
                
                pause 1.0

                $ temp_Characters[0].change_face("angry1", eyes = "down", mouth = "lipbite", blush = 2) 
            elif temp_Characters[0] in [Jean]:
                $ temp_Characters[0].change_face("worried1", mouth = "lipbite", blush = 2) 
                
                $ renpy.say(temp_Characters[0].voice, "I'm still not convinced this is even possible. . .")
                
                $ temp_Characters[0].change_face("worried1", eyes = "down", mouth = "lipbite", blush = 2) 
                
            $ dice_pool = [1, 2, 3]

            $ dice_roll = renpy.random.choice(dice_pool)

            if dice_roll == 1:
                $ temp_Characters[0].eyes = "down"
                
                $ renpy.say(None, f"{subject.capitalize()} wraps her lips around you and starts taking you in, slowly, one inch at a time.")
            elif dice_roll == 2:
                $ temp_Characters[0].eyes = "down"

                $ renpy.say(None, f"{subject.capitalize()} stares down at your cock, looking quite skeptical.")
            elif dice_roll == 3:
                $ temp_Characters[0].eyes = "down"
                
                $ renpy.say(None, f"{subject.capitalize()} looks down at your cock, clearly intimidated by its size.")

            if dice_roll in [2, 3]:
                if renpy.random.random() > 0.5:
                    $ renpy.say(None, "That doesn't stop her from trying to take you as deep into her mouth as possible.")
                else:
                    $ renpy.say(None, "That doesn't stop her from trying to slowly take you deep into her mouth.")

            $ speed = Action.max_speed[0]/2
            $ intensity = Action.max_intensity[0]/2

        $ temp_Characters.remove(temp_Characters[0])

    return

label titjob_initiations(Action):
    $ renpy.dynamic(temp_Characters = get_Action_Characters(Action))

    while temp_Characters:
        $ temp_Characters.remove(temp_Characters[0])

    return

label footjob_initiations(Action):
    $ renpy.dynamic(temp_Characters = get_Action_Characters(Action))

    while temp_Characters:
        $ temp_Characters.remove(temp_Characters[0])

    return

label self_touch_pussy_initiations(Action):
    $ renpy.dynamic(temp_Characters = get_Action_Characters(Action))

    while temp_Characters:
        if renpy.random.random() > 0.5:
            $ subject = temp_Characters[0].name
            $ object = temp_Characters[0].name
            $ owner = temp_Characters[0].name + "'s"
        else:
            $ subject = "she"
            $ object = "her"
            $ owner = "her"

        if renpy.random.random() > 0.5:
            $ noun = "pussy"
        else:
            $ noun = "crotch"

        $ dice_pool = [1]

        $ dice_roll = renpy.random.choice(dice_pool)

        if dice_roll == 1:
            $ renpy.say(None, f"{subject.capitalize()} reaches down to caress her {noun}.")

        $ temp_Characters.remove(temp_Characters[0])

    return

label self_finger_ass_initiations(Action):
    $ renpy.dynamic(temp_Characters = get_Action_Characters(Action))

    while temp_Characters:
        if renpy.random.random() > 0.5:
            $ subject = temp_Characters[0].name
            $ object = temp_Characters[0].name
            $ owner = temp_Characters[0].name + "'s"
        else:
            $ subject = "she"
            $ object = "her"
            $ owner = "her"

        if renpy.random.random() > 0.66:
            $ noun = "asshole"
        elif renpy.random.random() > 0.33:
            $ noun = "hole"
        else:
            $ noun = "ass"

        if renpy.random.random() > 0.75 and temp_Characters[0].desire >= 75:
            $ adjective = "hungry "
        elif renpy.random.random() > 0.5:
            if temp_Characters[0].body_hair["anus"] in ["hairy"]:
                $ adjective = "hairy "
            else:
                $ adjective = "smooth "
        elif renpy.random.random() > 0.25:
            $ adjective = "tight "
        else:
            $ adjective = ""

        $ dice_pool = [1]

        $ dice_roll = renpy.random.choice(dice_pool)

        if dice_roll == 1:
            $ renpy.say(None, f"{subject.capitalize()} gently presses her finger against her {adjective}{noun} and pushes it in.")

        $ temp_Characters.remove(temp_Characters[0])

    return

label self_vibrator_initiations(Action):
    $ renpy.dynamic(temp_Characters = get_Action_Characters(Action))

    while temp_Characters:
        if renpy.random.random() > 0.5:
            $ subject = temp_Characters[0].name
            $ object = temp_Characters[0].name
            $ owner = temp_Characters[0].name + "'s"
        else:
            $ subject = "she"
            $ object = "her"
            $ owner = "her"

        if renpy.random.random() > 0.5:
            $ noun = "clit"

            if renpy.random.random() > 0.66 and temp_Characters[0].desire >= 75:
                $ adjective = "pulsing "
            elif renpy.random.random() > 0.33 and temp_Characters[0].desire >= 75:
                $ adjective = "throbbing "
            else:
                $ adjective = ""
        else:
            $ noun = "pussy"

            if renpy.random.random() > 0.66 and temp_Characters[0].desire >= 75:
                $ adjective = "soaking wet "
            elif renpy.random.random() > 0.33:
                $ adjective = "glistening "
            else:
                $ adjective = ""
        
        $ dice_pool = [1, 2]

        if temp_Characters[0].desire >= 75:
            $ dice_pool.append(3)

        $ dice_roll = renpy.random.choice(dice_pool)

        if dice_roll == 1:
            $ temp_Characters[0].change_face("worried1", mouth = "open")

            $ renpy.say(None, f"{subject.capitalize()} shudders as the vibrator makes contact with her {adjective}{noun}.")
        elif dice_roll == 2:
            $ temp_Characters[0].change_face("worried1")

            $ renpy.say(None, f"{subject.capitalize()} slowly drags the vibrator across her skin before pressing the tip against her {adjective}{noun}.")
        elif dice_roll == 3:
            $ temp_Characters[0].change_face("worried1", mouth = "agape")

            $ renpy.say(None, f"{subject.capitalize()} cries out in pleasure as she grinds the vibrator against her {adjective}{noun}.")

        $ temp_Characters.remove(temp_Characters[0])

    return

label self_dildo_pussy_initiations(Action):
    $ renpy.dynamic(temp_Characters = get_Action_Characters(Action))

    while temp_Characters:
        if renpy.random.random() > 0.5:
            $ subject = temp_Characters[0].name
            $ object = temp_Characters[0].name
            $ owner = temp_Characters[0].name + "'s"
        else:
            $ subject = "she"
            $ object = "her"
            $ owner = "her"

        if renpy.random.random() > 0.66 and temp_Characters[0].desire >= 75:
            $ noun = "cunt"
        elif renpy.random.random() > 0.33:
            $ noun = "hole"
        else:
            $ noun = "pussy"

        if renpy.random.random() > 0.75 and temp_Characters[0].desire >= 75:
            $ adjective = "soaking wet "
        elif renpy.random.random() > 0.5:
            if temp_Characters[0].body_hair["pubic"] in ["bush", "hairy"]:
                $ adjective = "hairy "
            else:
                $ adjective = "smooth "
        elif renpy.random.random() > 0.25:
            $ adjective = "glistening "
        else:
            $ adjective = ""
        
        $ dice_pool = [2, 3]

        if temp_Characters[0].desire >= 75:
            $ dice_pool.append(4)

        if temp_Characters[0].desire < eval(f"{temp_Characters[0].tag}_Action_desire_thresholds['{Action.Action_type}']"):
            if renpy.random.random() > 0.5:
                $ temp_Characters[0].change_face("confused1", eyes = "left")
            else:
                $ temp_Characters[0].change_face("confused1", eyes = "right")

            $ dice_pool = [1]

        $ dice_roll = renpy.random.choice(dice_pool)

        if dice_roll == 1:
            $ renpy.say(None, f"{subject.capitalize()} looks somewhat uncomfortable and somewhat robotically pushes the dildo into herself.")
        elif dice_roll == 2:
            $ temp_Characters[0].change_face("worried1", mouth = "lipbite")

            $ renpy.say(None, f"{subject.capitalize()} bites her lip and runs the smooth tip of the dildo along her {adjective}{noun}.")
            $ renpy.say(None, f"She lets out a small gasp as she slides it inside herself.")
        elif dice_roll == 3:
            $ temp_Characters[0].change_face("worried1")

            $ renpy.say(None, f"{subject.capitalize()} teases her {noun} with the tip of the dildo before slowly pushing it in past her {adjective}folds.")
        elif dice_roll == 4:
            $ temp_Characters[0].change_face("worried1", mouth = "agape")

            $ renpy.say(None, f"{subject.capitalize()} moans and eagerly thrusts the dildo into her {adjective}{noun}.")

        $ temp_Characters.remove(temp_Characters[0])

    return

label self_dildo_ass_initiations(Action):
    $ renpy.dynamic(temp_Characters = get_Action_Characters(Action))

    while temp_Characters:
        if renpy.random.random() > 0.5:
            $ subject = temp_Characters[0].name
            $ object = temp_Characters[0].name
            $ owner = temp_Characters[0].name + "'s"
        else:
            $ subject = "she"
            $ object = "her"
            $ owner = "her"

        if renpy.random.random() > 0.66:
            $ noun = "asshole"
        elif renpy.random.random() > 0.33:
            $ noun = "hole"
        else:
            $ noun = "ass"

        if renpy.random.random() > 0.75 and temp_Characters[0].desire >= 75:
            $ adjective = "hungry "
        elif renpy.random.random() > 0.5:
            if temp_Characters[0].body_hair["anus"] in ["hairy"]:
                $ adjective = "hairy "
            else:
                $ adjective = "smooth "
        elif renpy.random.random() > 0.25:
            $ adjective = "tight "
        else:
            $ adjective = ""
        
        $ dice_pool = [2, 3]

        if temp_Characters[0].desire >= 75:
            $ dice_pool.append(4)

        if temp_Characters[0].desire < eval(f"{temp_Characters[0].tag}_Action_desire_thresholds['{Action.Action_type}']"):
            if renpy.random.random() > 0.5:
                $ temp_Characters[0].change_face("grimace", eyes = "left")
            else:
                $ temp_Characters[0].change_face("grimace", eyes = "right")

            $ dice_pool = [1]

        $ dice_roll = renpy.random.choice(dice_pool)

        if dice_roll == 1:
            $ renpy.say(None, f"{subject.capitalize()} looks quite uncomfortable as she tries to press the dildo into her {noun}.")
        elif dice_roll == 2:
            $ temp_Characters[0].change_face("grimace")

            $ renpy.say(None, f"{subject.capitalize()} tenses slightly as she presses the tip of the dildo against the rim of her {adjective}{noun}, relaxing as it slips in.")
        elif dice_roll == 3:
            $ temp_Characters[0].change_face("worried1")

            $ renpy.say(None, f"{subject.capitalize()} teases her {adjective}{noun} with the tip of the dildo before slowly pushing it in.")
        elif dice_roll == 4:
            $ temp_Characters[0].change_face("worried1", mouth = "agape")

            $ renpy.say(None, f"{subject.capitalize()} moans out as she eagerly pushes the dildo into her {adjective}{noun}.")

        $ temp_Characters.remove(temp_Characters[0])

    return

label jerk_off_initiations(Action):
    $ renpy.dynamic(temp_Characters = get_Action_Characters(Action))

    while temp_Characters:
        $ temp_Characters.remove(temp_Characters[0])

    return

label grind_pussy_initiations(Action):
    $ renpy.dynamic(temp_Characters = get_Action_Characters(Action))

    while temp_Characters:
        if renpy.random.random() > 0.5:
            $ subject = temp_Characters[0].name
            $ object = temp_Characters[0].name
            $ owner = temp_Characters[0].name + "'s"
        else:
            $ subject = "she"
            $ object = "her"
            $ owner = "her"

        $ dice_pool = [1, 2]

        if temp_Characters[0].desire >= 50:
            $ dice_pool.append(3)
        
        if temp_Characters[0].desire >= 75:
            $ dice_pool.append(4)

        $ dice_roll = renpy.random.choice(dice_pool)

        if dice_roll == 1:
            $ renpy.say(None, f"You press your cock against {owner} crotch, immediately feeling the heat radiating off of it.")
        elif dice_roll == 2:
            $ renpy.say(None, f"You relish the feeling of pushing your cock up against {owner} crotch.")
        elif dice_roll == 3:
            $ renpy.say(None, f"{subject.capitalize()} leans her hips into you, seeking to feel your cock pressed against her.")
        elif dice_roll == 4:
            $ renpy.say(None, f"{subject.capitalize()} moans at the feeling of your warm cock close to her warmth.")

        $ temp_Characters.remove(temp_Characters[0])

    return

label grind_ass_initiations(Action):
    $ renpy.dynamic(temp_Characters = get_Action_Characters(Action))

    while temp_Characters:
        if renpy.random.random() > 0.5:
            $ subject = temp_Characters[0].name
            $ object = temp_Characters[0].name
            $ owner = temp_Characters[0].name + "'s"
        else:
            $ subject = "she"
            $ object = "her"
            $ owner = "her"

        $ dice_pool = [1]

        if temp_Characters[0].desire >= 50:
            $ dice_pool.append(2)
        
        if temp_Characters[0].desire >= 75:
            $ dice_pool.append(3)

        if temp_Characters[0] in [Laura]:
            $ dice_pool.append(4)

        $ dice_roll = renpy.random.choice(dice_pool)

        if dice_roll == 1:
            $ renpy.say(None, f"You lay your cock in between {owner} cheeks and press up against her ass.")
        elif dice_roll == 2:
            $ renpy.say(None, f"{subject.capitalize()} leans her hips into you, seeking to feel your cock pressed against her.")
        elif dice_roll == 3:
            $ renpy.say(None, f"{subject.capitalize()} moans at the feeling of your warm cock close to her ass")
        elif dice_roll == 4:
            $ renpy.say(None, f"You relish the feeling of nestling your cock between {owner} muscular ass cheeks.")

        $ temp_Characters.remove(temp_Characters[0])

    return

label sex_initiations(Action):
    $ renpy.dynamic(temp_Characters = get_Action_Characters(Action))

    while temp_Characters:
        if renpy.random.random() > 0.5:
            $ subject = temp_Characters[0].name
            $ object = temp_Characters[0].name
            $ owner = temp_Characters[0].name + "'s"
        else:
            $ subject = "she"
            $ object = "her"
            $ owner = "her"

        if renpy.random.random() > 0.66 and temp_Characters[0].desire >= 75:
            $ noun = "cunt"
        elif renpy.random.random() > 0.33:
            $ noun = "hole"
        else:
            $ noun = "pussy"

        if renpy.random.random() > 0.75 and temp_Characters[0].desire >= 75:
            $ adjective = "soaking wet "
        elif renpy.random.random() > 0.5:
            if temp_Characters[0].body_hair["pubic"] in ["bush", "hairy"]:
                $ adjective = "hairy "
            else:
                $ adjective = "smooth "
        elif renpy.random.random() > 0.25:
            $ adjective = "glistening "
        else:
            $ adjective = ""

        if Action.mode == 2:
            $ dice_pool = [1, 2]

            if temp_Characters[0].desire >= 50:
                $ dice_pool.append(3)

            $ dice_roll = renpy.random.choice(dice_pool)
            
            if dice_roll == 1:
                $ renpy.say(None, f"You slide the tip inside {owner} {adjective}{noun}, and instead of pulling it back out, you start to move.")
            elif dice_roll == 2:
                $ renpy.say(None, f"You push deep inside {object} and start to thrust in and out.")
            elif dice_roll == 3:
                $ renpy.say(None, f"{subject.capitalize()} moans in pleasure as you start to thrust in and out of her {adjective}{noun}.")
        else:
            if temp_Characters[0].History.check("sex") >= 2:
                $ dice_pool = []

                if temp_Characters[0] in [Rogue, Jean]:
                    $ dice_pool.append(1)
                    $ dice_pool.append(2)
                
                if temp_Characters[0] in [Laura]:
                    $ dice_pool.append(3)

                $ dice_roll = renpy.random.choice(dice_pool)
                
                if dice_roll == 1:
                    $ temp_Characters[0].change_face("sexy", eyes = "down", blush = 2) 
                    
                    $ renpy.say(None, f"{subject.capitalize()} looks down excitedly, wiggling her hips at you, ready to take it in.")
                    $ renpy.say(None, f"You gently press yourself up against her {noun}, teasing it, feeling how wet she already is.")
                elif dice_roll == 2:
                    $ temp_Characters[0].change_face("sly", blush = 2) 
                    
                    $ renpy.say(None, f"{subject.capitalize()} teases you a bit, pulling her hips away.")
                    
                    $ temp_Characters[0].change_face("sexy", eyes = "down", blush = 2) 
                    
                    $ renpy.say(None, f"Finally, she lets you get close, and you press the tip up against her {adjective}{noun}.")
                elif dice_roll == 3:
                    $ temp_Characters[0].change_face("sly", mouth = "lipbite", blush = 2) 
                    
                    $ renpy.say(None, f"{subject.capitalize()} has a look in her eye that clearly says she wants you to fuck her already.")
                    $ renpy.say(None, f"You press the tip up against her already dripping wet {noun} as you prepare to slide it in.")
            else:
                if temp_Characters[0] in [Rogue]:
                    $ temp_Characters[0].change_face("worried2", mouth = "lipbite", blush = 2) 
                    
                    $ renpy.say(temp_Characters[0].voice, "The first time wasn't so bad. . . but it's just so big. . .")
                    
                    $ temp_Characters[0].change_face("worried1", eyes = "down", mouth = "lipbite", blush = 2) 
                    
                elif temp_Characters[0] in [Laura]:
                    $ temp_Characters[0].change_face("confused1", eyes = "down", mouth = "lipbite", blush = 2) 
                    
                    $ renpy.say(temp_Characters[0].voice, "The first time was only slightly painful at the start. . .")
                    
                    $ temp_Characters[0].change_face("sexy", mouth = "lipbite", blush = 2) 
                    
                    $ renpy.say(temp_Characters[0].voice, "And felt very good by the end.")
                    $ renpy.say(temp_Characters[0].voice, "Put it in already. . .")
                    
                    $ temp_Characters[0].change_face("sexy", eyes = "down", mouth = "lipbite", blush = 2)
                elif temp_Characters[0] in [Jean]:
                    $ temp_Characters[0].change_face("worried1", eyes = "down", mouth = "lipbite", blush = 2) 
                    
                    $ renpy.say(temp_Characters[0].voice, "It kinda hurt the first time. . .")
                    
                    $ temp_Characters[0].change_face("worried1", mouth = "lipbite", blush = 2) 
                    
                    $ renpy.say(temp_Characters[0].voice, "But I want to get used to it. . .")
                    
                    $ temp_Characters[0].change_face("worried1", eyes = "down", mouth = "lipbite", blush = 2) 
                    
                $ dice_pool = [1]

                if temp_Characters[0].desire >= 50:
                    $ dice_pool.append(2)

                if temp_Characters[0].desire >= 75:
                    $ dice_pool.append(3)

                $ dice_roll = renpy.random.choice(dice_pool)
                
                if dice_roll == 1:
                    $ renpy.say(None, f"You press the tip up against her, causing her to twitch as you prepare to slide it in.") 
                elif dice_roll == 2:
                    $ renpy.say(None, f"You gently press yourself up against her {noun}, teasing it, feeling how wet she already is.")
                elif dice_roll == 3:
                    $ renpy.say(None, f"You press the tip up against her already dripping wet {noun} as you prepare to slide it in.")

                if temp_Characters[0] in [Rogue]:
                    $ temp_Characters[0].change_face("worried1", mouth = "lipbite", blush = 2) 
                
                    $ renpy.say(temp_Characters[0].voice, "Ah'm ready. . .")
                elif temp_Characters[0] in [Jean]:
                    $ temp_Characters[0].change_face("worried1", mouth = "lipbite", blush = 2) 
                    
                    $ renpy.say(temp_Characters[0].voice, "You can start. . .")

        $ temp_Characters.remove(temp_Characters[0])

    return

label anal_initiations(Action):
    $ renpy.dynamic(temp_Characters = get_Action_Characters(Action))

    while temp_Characters:
        if renpy.random.random() > 0.5:
            $ subject = temp_Characters[0].name
            $ object = temp_Characters[0].name
            $ owner = temp_Characters[0].name + "'s"
        else:
            $ subject = "she"
            $ object = "her"
            $ owner = "her"

        if renpy.random.random() > 0.66:
            $ noun = "asshole"
        elif renpy.random.random() > 0.33:
            $ noun = "hole"
        else:
            $ noun = "ass"

        if renpy.random.random() > 0.75 and temp_Characters[0].desire >= 75 and temp_Characters[0].anal_training >= 1:
            $ adjective = "hungry "
        elif renpy.random.random() > 0.7:
            if temp_Characters[0].body_hair["anus"] in ["hairy"]:
                $ adjective = "hairy "
            else:
                $ adjective = "smooth "
        elif renpy.random.random() > 0.25:
            $ adjective = "tight "
        else:
            $ adjective = ""

        if Action.mode < 2 or temp_Characters[0].anal_training >= 1:
            if temp_Characters[0].anal_training == 1:
                $ dice_roll = renpy.random.randint(1, 3)

                if temp_Characters[0] in [Rogue]:
                    if renpy.random.random() > 0.5:
                        $ temp_Characters[0].change_face("worried1", eyes = "down", mouth = "lipbite", blush = 2) 
                    else:
                        $ temp_Characters[0].change_face("worried1", eyes = "down", mouth = "open", blush = 2) 
                        
                    if dice_roll == 1:
                        $ renpy.say(temp_Characters[0].voice, "It doesn't hurt too bad. . .")
                        $ renpy.say(temp_Characters[0].voice, "So long as yer gentle.")
                    elif dice_roll == 2:
                        $ renpy.say(temp_Characters[0].voice, "Lord, ah always forget how big it is. . .")
                    elif dice_roll == 3:
                        $ renpy.say(temp_Characters[0].voice, f"Just. . . gently, {temp_Characters[0].Player_petname}, please.")
                        
                    if renpy.random.random() > 0.5:
                        $ temp_Characters[0].change_face("angry1", eyes = "closed", mouth = "lipbite", blush = 2)
                    else:
                        $ temp_Characters[0].change_face("grimace", eyes = "down", blush = 2)
                elif temp_Characters[0] in [Laura]:
                    if renpy.random.random() > 0.5:
                        $ temp_Characters[0].change_face("angry1", mouth = "lipbite", blush = 2) 
                    else:
                        $ temp_Characters[0].change_face("angry1", eyes = "down", mouth = "open", blush = 2) 
                        
                    if dice_roll == 1:
                        $ renpy.say(temp_Characters[0].voice, "The pain is not the issue. . .")
                        $ renpy.say(temp_Characters[0].voice, "You are just too big.")
                    elif dice_roll == 2:
                        $ renpy.say(temp_Characters[0].voice, "I don't think this would be possible without my healing factor.")

                        $ temp_Characters[0].change_face("angry1", eyes = "left", blush = 2) 

                        $ renpy.say(temp_Characters[0].voice, "Even still. . .")
                    elif dice_roll == 3:
                        $ renpy.say(temp_Characters[0].voice, "I can take you if you go slowly.")
                        
                    if renpy.random.random() > 0.5:
                        $ temp_Characters[0].change_face("angry1", eyes = "down", mouth = "lipbite", blush = 2) 
                    else:
                        $ temp_Characters[0].change_face("grimace", eyes = "down", blush = 2)
                elif temp_Characters[0] in [Jean]:
                    if renpy.random.random() > 0.5:
                        $ temp_Characters[0].change_face("worried1", eyes = "down", mouth = "lipbite", blush = 2) 
                    else:
                        $ temp_Characters[0].change_face("worried1", eyes = "down", mouth = "open", blush = 2) 
                        
                    if dice_roll == 1:
                        $ renpy.say(temp_Characters[0].voice, "It kinda hurts. . . a lot. . .")
                        $ renpy.say(temp_Characters[0].voice, "Just be careful.")
                    elif dice_roll == 2:
                        $ renpy.say(temp_Characters[0].voice, f"Slowly, {temp_Characters[0].Player_petname}. . .")
                    elif dice_roll == 3:
                        $ renpy.say(temp_Characters[0].voice, f"Jesus, {Player.first_name}. I can't believe I can fit any of that inside me.")
                        
                    if renpy.random.random() > 0.5:
                        $ temp_Characters[0].change_face("angry1", eyes = "closed", mouth = "lipbite", blush = 2)
                    else:
                        $ temp_Characters[0].change_face("grimace", eyes = "down", blush = 2)
                    
                $ dice_pool = []

                if temp_Characters[0] in [Rogue, Jean]:
                    $ dice_pool.append(1, 2)

                if temp_Characters[0] in [Laura]:
                    $ dice_pool.append(3)

                $ dice_roll = renpy.random.choice(dice_pool)

                if dice_roll == 1:
                    $ renpy.say(None, f"{owner.capitalize()} {adjective}{noun} provides a lot of resistance as you gently push your cock inside.")
                    $ renpy.say(None, f"Slowly, you manage to get the tip in, {subject} whimpering a little.")
                elif dice_roll == 2:
                    $ renpy.say(None, f"You gently press yourself up against {owner} {adjective}{noun}, slowly pushing the tip in as she whimpers a little.")
                elif dice_roll == 3:                    
                    $ renpy.say(None, f"You slowly press your cock into her, the {owner} {adjective}{noun} providing a lot of resistance as {subject} growls from the pain.")
            elif temp_Characters[0].anal_training == 2:
                if temp_Characters[0] in [Rogue]:
                    if renpy.random.random() > 0.5:
                        $ temp_Characters[0].change_face("worried1", mouth = "lipbite", blush = 2) 
                    else:
                        $ temp_Characters[0].change_face("worried1", mouth = "open", blush = 2) 
                elif temp_Characters[0] in [Laura]:
                    if renpy.random.random() > 0.5:
                        $ temp_Characters[0].change_face("angry1", mouth = "lipbite", blush = 2) 
                    else:
                        $ temp_Characters[0].change_face("angry1", mouth = "open", blush = 2) 
                elif temp_Characters[0] in [Jean]:
                    if renpy.random.random() > 0.5:
                        $ temp_Characters[0].change_face("worried1", mouth = "lipbite", blush = 2)
                    else:
                        $ temp_Characters[0].change_face("worried1", mouth = "open", blush = 2)

                $ dice_pool = [2, 3]

                if temp_Characters[0] in [Rogue, Jean]:
                    $ dice_pool.append(4)

                if temp_Characters[0].desire < eval(f"{temp_Characters[0].tag}_Action_desire_thresholds['{Action.Action_type}']"):
                    if renpy.random.random() > 0.5:
                        $ temp_Characters[0].change_face("grimace", eyes = "left")
                    else:
                        $ temp_Characters[0].change_face("grimace", eyes = "right")

                    $ dice_pool = [1]

                $ dice_roll = renpy.random.choice(dice_pool)

                if dice_roll == 1:
                    $ renpy.say(None, f"{subject.capitalize()} looks quite uncomfortable - she might appreciate being warmed up a little bit more.")
                elif dice_roll == 2:
                    $ temp_Characters[0].eyes = "down"

                    $ renpy.say(None, f"{subject.capitalize()} looks down at you, still a bit of apprehension in her eyes.")
                    $ renpy.say(None, f"You slowly press the tip into her, and she takes it without showing too much discomfort.")
                elif dice_roll == 3:
                    $ temp_Characters[0].eyes = "down"

                    $ renpy.say(None, f"{subject.capitalize()} is starting to get used to your size, but she still looks down at your cock with trepidation.")
                    $ renpy.say(None, f"You gently push your cock inside her {adjective}{noun}, and it goes in without too much difficulty.")
                elif dice_roll == 4:
                    $ temp_Characters[0].eyes = "down"

                    $ renpy.say(None, f"{subject.capitalize()} looks down at your cock, worry written across her face.")
                    $ renpy.say(None, "She's starting to get used to you, but has a long way to go.")
                    $ renpy.say(None, "You slowly press the tip inside her, and she manages not to whimper in pain.")
            elif temp_Characters[0].anal_training == 3:
                if temp_Characters[0] in [Rogue]:
                    if renpy.random.random() > 0.5:
                        $ temp_Characters[0].change_face("sexy", blush = 2)
                    else:
                        $ temp_Characters[0].change_face("sexy", mouth = "smirk", blush = 2)
                elif temp_Characters[0] in [Laura]:
                    if renpy.random.random() > 0.5:
                        $ temp_Characters[0].change_face("sly", mouth = "lipbite", blush = 2) 
                    else:
                        $ temp_Characters[0].change_face("sexy", mouth = "smirk", blush = 2)
                elif temp_Characters[0] in [Jean]:
                    if renpy.random.random() > 0.5:
                        $ temp_Characters[0].change_face("sexy", blush = 2) 
                        
                        $ renpy.say(temp_Characters[0].voice, "It doesn't hurt anymore. . .")
                        
                        $ temp_Characters[0].change_face("sexy", eyes = "down", blush = 2) 
                        
                        $ renpy.say(temp_Characters[0].voice, "It actually feels really good.")
                    else:
                        $ temp_Characters[0].change_face("sexy", mouth = "smirk", blush = 2)

                $ dice_pool = [2]

                if temp_Characters[0].desire >= 50:
                    $ dice_pool.append(3)

                if temp_Characters[0].desire >= 75:
                    $ dice_pool.append(4)

                if temp_Characters[0].desire < eval(f"{temp_Characters[0].tag}_Action_desire_thresholds['{Action.Action_type}']"):
                    if renpy.random.random() > 0.5:
                        $ temp_Characters[0].change_face("grimace", eyes = "left")
                    else:
                        $ temp_Characters[0].change_face("grimace", eyes = "right")

                    $ dice_pool = [1]

                $ dice_roll = renpy.random.choice(dice_pool)

                if dice_roll == 1:
                    $ renpy.say(None, f"{subject.capitalize()} squirms a little uncomfortably, but she takes you into her {noun} easily enough.")
                elif dice_roll == 2:
                    $ temp_Characters[0].eyes = "down"

                    $ renpy.say(None, f"{subject.capitalize()} looks down at your cock, ready to take you as deep as you can give her.")
                    $ renpy.say(None, "You press the tip into her {adjective}{noun} - it slides in like it was always meant to be there.")
                elif dice_roll == 3:
                    $ temp_Characters[0].eyes = "down"
                    
                    $ renpy.say(None, f"{subject.capitalize()} stares down at your cock, an air of excitement about her.") 
                    $ renpy.say(None, "Your cock slides into her {adjective}{noun} with ease, a perfect fit.")
                elif dice_roll == 4:
                    $ renpy.say(None, f"You cock slides into {owner} {adjective}{noun} like it's meant to be there, and she even lets out a moan as you push deeper inside.")
        else:
            $ Action.mode = 1

            if temp_Characters[0] in [Rogue]:
                if renpy.random.random() > 0.5:
                    $ temp_Characters[0].change_face("worried1", eyes = "down", mouth = "lipbite", blush = 2) 
                    
                    $ renpy.say(temp_Characters[0].voice, "It's real big. . .")
                else:
                    $ temp_Characters[0].change_face("worried2", mouth = "lipbite", blush = 2) 
                    
                    $ renpy.say(temp_Characters[0].voice, "Please don't force it.")
                
                if renpy.random.random() > 0.5:
                    $ temp_Characters[0].change_face("grimace", blush = 2)
                else:
                    $ temp_Characters[0].change_face("grimace", eyes = "down", blush = 2) 
            elif temp_Characters[0] in [Laura]:
                if renpy.random.random() > 0.5:
                    $ temp_Characters[0].change_face("confused2", blush = 2) 
                    
                    $ renpy.say(temp_Characters[0].voice, "I still do not understand how this would even be possible. . .")
                else:
                    $ temp_Characters[0].change_face("confused1", eyes = "down", mouth = "lipbite", blush = 2) 
                    
                    $ renpy.say(temp_Characters[0].voice, "Go slowly. . .")
                
                if renpy.random.random() > 0.5:
                    $ temp_Characters[0].change_face("grimace", blush = 2)
                else:
                    $ temp_Characters[0].change_face("grimace", eyes = "down", blush = 2) 
            elif temp_Characters[0] in [Jean]:
                if renpy.random.random() > 0.5:
                    $ temp_Characters[0].change_face("worried1", mouth = "lipbite", blush = 2) 
                    
                    $ renpy.say(temp_Characters[0].voice, "I still don't understand how all of you could fit back there. . .")
                else:
                    $ temp_Characters[0].change_face("worried1", eyes = "down", mouth = "lipbite", blush = 2) 
                    
                    $ renpy.say(temp_Characters[0].voice, "You better be gentle.")
                
                if renpy.random.random() > 0.5:
                    $ temp_Characters[0].change_face("grimace", blush = 2)
                else:
                    $ temp_Characters[0].change_face("grimace", eyes = "down", blush = 2) 

            $ dice_pool = [1]

            if temp_Characters[0] in [Rogue, Jean]:
                $ dice_pool.append(2)

            if temp_Characters[0] in [Laura]:
                $ dice_pool.append(3)

            $ dice_roll = renpy.random.choice(dice_pool)
                
            if dice_roll == 1:
                $ renpy.say(None, f"You press the tip up against {owner} {adjective}{noun}, easing it inside.")
                $ renpy.say(None, "She winces, and you're only able to fit the tip in before she gasps and forces you to stop.")
            elif dice_roll == 2:
                $ renpy.say(None, f"You press the tip up against {object}, {owner} {adjective}{noun} providing a lot of resistance.")
                $ renpy.say(None, "You manage to get the head in before she whimpers and stops you from going further.")
            elif dice_roll == 3:
                $ renpy.say(None, f"You press your cock up against her {adjective}{noun}, {owner} small stature not doing her any favors. . .")
                $ renpy.say(None, "It's a very tight fit, and you only manage to get the tip in before she growls from pain.")

            if temp_Characters[0] in [Rogue]:
                if renpy.random.random() > 0.5:
                    $ temp_Characters[0].change_face("worried1", mouth = "lipbite", blush = 2) 
                else:
                    $ temp_Characters[0].change_face("worried1", mouth = "agape", blush = 2) 
                    
                if renpy.random.random() > 0.5:
                    $ renpy.say(temp_Characters[0].voice, "Ah'm sorry, deeper than that hurts too much. . .")
                    $ renpy.say(temp_Characters[0].voice, "At least ah can handle the tip for now.")
                else:
                    $ renpy.say(temp_Characters[0].voice, "Ow!")
                    with small_screenshake

                    $ renpy.say(temp_Characters[0].voice, "Ah can't, ah'm sorry. . .")
                    
                if renpy.random.random() > 0.5:
                    $ temp_Characters[0].change_face("worried1", eyes = "down", mouth = "lipbite", blush = 2)
                else:
                    $ temp_Characters[0].change_face("worried1", mouth = "lipbite", blush = 2)
            elif temp_Characters[0] in [Laura]:
                if renpy.random.random() > 0.5:
                    $ temp_Characters[0].change_face("angry1", mouth = "lipbite", blush = 2) 
                else:
                    $ temp_Characters[0].change_face("angry1", mouth = "open", blush = 2) 
                
                if renpy.random.random() > 0.5:
                    $ renpy.say(temp_Characters[0].voice, "That is deep enough for now. . .")
                else:
                    $ renpy.say(temp_Characters[0].voice, "Stop.")
                
                if renpy.random.random() > 0.5:
                    $ temp_Characters[0].change_face("angry1", eyes = "down", mouth = "lipbite", blush = 2)
                else:
                    $ temp_Characters[0].change_face("angry1", mouth = "lipbite", blush = 2)
            elif temp_Characters[0] in [Jean]:
                if renpy.random.random() > 0.5:
                    $ temp_Characters[0].change_face("worried1", mouth = "lipbite", blush = 2) 
                else:
                    $ temp_Characters[0].change_face("worried1", mouth = "agape", blush = 2) 
                
                if renpy.random.random() > 0.5:
                    $ renpy.say(temp_Characters[0].voice, "That's as far as you're going. . .")
                    $ renpy.say(temp_Characters[0].voice, "It hurts too much.")
                else:
                    $ renpy.say(temp_Characters[0].voice, "Ow ow ow. . .")
                    $ renpy.say(temp_Characters[0].voice, f"Sorry, {temp_Characters[0].Player_petname}. . . not happening. . .")

                if renpy.random.random() > 0.5:
                    $ temp_Characters[0].change_face("worried1", eyes = "down", mouth = "lipbite", blush = 2) 
                else:
                    $ temp_Characters[0].change_face("worried1", mouth = "lipbite", blush = 2) 
                
            $ renpy.say(None, f"{subject.capitalize()} will have to practice before she can take it any deeper.")

            $ Action.counter += 1

            $ speed = 0.1
            $ intensity = 0.1

        $ temp_Characters.remove(temp_Characters[0])

    return

label vibrator_initiations(Action):
    $ renpy.dynamic(temp_Characters = get_Action_Characters(Action))

    while temp_Characters:
        if renpy.random.random() > 0.5:
            $ subject = temp_Characters[0].name
            $ object = temp_Characters[0].name
            $ owner = temp_Characters[0].name + "'s"
        else:
            $ subject = "she"
            $ object = "her"
            $ owner = "her"

        if renpy.random.random() > 0.5:
            $ noun = "clit"

            if renpy.random.random() > 0.66 and temp_Characters[0].desire >= 75:
                $ adjective = "pulsing "
            elif renpy.random.random() > 0.33 and temp_Characters[0].desire >= 75:
                $ adjective = "throbbing "
            else:
                $ adjective = ""
        else:
            $ noun = "pussy"

            if renpy.random.random() > 0.66 and temp_Characters[0].desire >= 75:
                $ adjective = "soaking wet "
            elif renpy.random.random() > 0.33:
                $ adjective = "glistening "
            else:
                $ adjective = ""
        
        $ dice_pool = [1, 2]

        if temp_Characters[0].desire >= 75:
            $ dice_pool.append(3)

        $ dice_roll = renpy.random.choice(dice_pool)

        if dice_roll == 1:
            $ temp_Characters[0].change_face("worried1", mouth = "open")

            $ renpy.say(None, f"{subject.capitalize()} shudders as the vibrator makes contact with her {adjective}{noun}.")
        elif dice_roll == 2:
            $ temp_Characters[0].change_face("worried1")

            $ renpy.say(None, f"You slowly drag the vibrator across {owner} skin before touching her {adjective}{noun}.")
        elif dice_roll == 3:
            $ temp_Characters[0].change_face("worried1", mouth = "agape")

            $ renpy.say(None, f"{subject.capitalize()} cries out in pleasure as you press the vibrator against her {adjective}{noun}.")

        $ temp_Characters.remove(temp_Characters[0])

    return

label dildo_pussy_initiations(Action):
    $ renpy.dynamic(temp_Characters = get_Action_Characters(Action))

    while temp_Characters:
        if renpy.random.random() > 0.5:
            $ subject = temp_Characters[0].name
            $ object = temp_Characters[0].name
            $ owner = temp_Characters[0].name + "'s"
        else:
            $ subject = "she"
            $ object = "her"
            $ owner = "her"

        if renpy.random.random() > 0.66 and temp_Characters[0].desire >= 75:
            $ noun = "cunt"
        elif renpy.random.random() > 0.33:
            $ noun = "hole"
        else:
            $ noun = "pussy"

        if renpy.random.random() > 0.75 and temp_Characters[0].desire >= 75:
            $ adjective = "soaking wet "
        elif renpy.random.random() > 0.5:
            if temp_Characters[0].body_hair["pubic"] in ["bush", "hairy"]:
                $ adjective = "hairy "
            else:
                $ adjective = "smooth "
        elif renpy.random.random() > 0.25:
            $ adjective = "glistening "
        else:
            $ adjective = ""
        
        $ dice_pool = [2, 3]

        if temp_Characters[0].desire >= 75:
            $ dice_pool.append(4)

        if temp_Characters[0].desire < eval(f"{temp_Characters[0].tag}_Action_desire_thresholds['{Action.Action_type}']"):
            if renpy.random.random() > 0.5:
                $ temp_Characters[0].change_face("confused1", eyes = "left")
            else:
                $ temp_Characters[0].change_face("confused1", eyes = "right")

            $ dice_pool = [1]

        $ dice_roll = renpy.random.choice(dice_pool)

        if dice_roll == 1:
            $ renpy.say(None, f"{subject.capitalize()} looks a bit uncomfortable as you push the cold tip of the dildo into her.")
        elif dice_roll == 2:
            $ temp_Characters[0].change_face("worried1", mouth = "lipbite")

            $ renpy.say(None, f"{subject.capitalize()} bites her lip as you press the smooth tip of the dildo against her {adjective}folds.")
            $ renpy.say(None, f"She then gasps as you slide it into her {noun}.")
        elif dice_roll == 3:
            $ temp_Characters[0].change_face("worried1")

            $ renpy.say(None, f"You tease around {owner} {noun} with the tip of the dildo before slowly pushing it in past her {adjective}folds.")
        elif dice_roll == 4:
            $ temp_Characters[0].change_face("worried1", mouth = "agape")

            $ renpy.say(None, f"{subject.capitalize()} moans and nods eagerly as you glide the dildo into her {adjective}{noun}.")

        $ temp_Characters.remove(temp_Characters[0])

    return

label dildo_ass_initiations(Action):
    $ renpy.dynamic(temp_Characters = get_Action_Characters(Action))

    while temp_Characters:
        if renpy.random.random() > 0.5:
            $ subject = temp_Characters[0].name
            $ object = temp_Characters[0].name
            $ owner = temp_Characters[0].name + "'s"
        else:
            $ subject = "she"
            $ object = "her"
            $ owner = "her"

        if renpy.random.random() > 0.66:
            $ noun = "asshole"
        elif renpy.random.random() > 0.33:
            $ noun = "hole"
        else:
            $ noun = "ass"

        if renpy.random.random() > 0.75 and temp_Characters[0].desire >= 75:
            $ adjective = "hungry "
        elif renpy.random.random() > 0.7:
            if temp_Characters[0].body_hair["anus"] in ["hairy"]:
                $ adjective = "hairy "
            else:
                $ adjective = "smooth "
        elif renpy.random.random() > 0.25:
            $ adjective = "tight "
        else:
            $ adjective = ""
        
        $ dice_pool = [2, 3]

        if temp_Characters[0].desire >= 75:
            $ dice_pool.append(4)

        if temp_Characters[0].desire < eval(f"{temp_Characters[0].tag}_Action_desire_thresholds['{Action.Action_type}']"):
            if renpy.random.random() > 0.5:
                $ temp_Characters[0].change_face("grimace", eyes = "left")
            else:
                $ temp_Characters[0].change_face("grimace", eyes = "right")

            $ dice_pool = [1]

        $ dice_roll = renpy.random.choice(dice_pool)

        if dice_roll == 1:
            $ renpy.say(None, f"{subject.capitalize()} flinches uncomfortably as you press the cold tip of the dildo against her {adjective}{noun}.")
        elif dice_roll == 2:
            $ temp_Characters[0].change_face("grimace")

            $ renpy.say(None, f"{subject.capitalize()} tenses slightly as you press the tip of the dildo against the rim of her {adjective}{noun}, relaxing as it slips in.")
        elif dice_roll == 3:
            $ temp_Characters[0].change_face("worried1")

            $ renpy.say(None, f"You tease {owner} {adjective}{noun} with the tip of the dildo before slowly pushing it in.")
        elif dice_roll == 4:
            $ temp_Characters[0].change_face("worried1", mouth = "agape")

            $ renpy.say(None, f"{subject.capitalize()} moans out as you push the dildo into her {adjective}{noun}.")

        $ temp_Characters.remove(temp_Characters[0])

    return