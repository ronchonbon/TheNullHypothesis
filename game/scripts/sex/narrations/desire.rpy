label desire_narrations(Character, proper_subject = True):
    if proper_subject:
        $ subject = Character.name
        $ object = Character.name
        $ owner = Character.name + "'s"
    else:
        $ subject = "she"
        $ object = "her"
        $ owner = "her"

    $ sex_faces(Character)
    $ sex_poses(Character)

    $ dice_pool = []

    if Character.desire >= 75:
        $ dice_pool.append(1)
        $ dice_pool.append(2)
    elif Character.desire >= 25:
        $ dice_pool.append(3)
        $ dice_pool.append(4)
    else:
        $ dice_pool.append(5)
        $ dice_pool.append(6)

    $ dice_roll = renpy.random.choice(dice_pool)

    if dice_roll == 1:
        $ renpy.say(None, f"{subject.capitalize()} is really squirming.")
    elif dice_roll == 2:
        $ renpy.say(None, f"{subject.capitalize()} crosses and uncrosses her legs.")
    elif dice_roll == 3:
        $ renpy.say(None, f"{subject.capitalize()} looks at you intensely.")
    elif dice_roll == 4:
        $ renpy.say(None, f"{subject.capitalize()} fidgets a little.")
    elif dice_roll == 5:
        $ renpy.say(None, f"{subject.capitalize()} seems a little distracted.")
    elif dice_roll == 6:
        $ renpy.say(None, f"{subject.capitalize()} shifts her body slightly.")

    return

label out_of_stamina_narrations(Character, proper_subject = True):
    if proper_subject:
        $ subject = Character.name
        $ object = Character.name
        $ owner = Character.name + "'s"
    else:
        $ subject = "she"
        $ object = "her"
        $ owner = "her"

    $ orgasm_faces(Character)
    $ orgasm_poses(Character)

    $ dice_roll = renpy.random.randint(1, 4)

    if dice_roll == 1:
        $ renpy.say(None, f"{subject.capitalize()} gasps, shifting back and forth as the pleasure becomes unbearable.")
    elif dice_roll == 2:
        $ renpy.say(None, f"{subject.capitalize()} squirms and fidgets uncomfortably as pleasure continues to wrack her sensitive body.")
    elif dice_roll == 3:
        $ renpy.say(None, f"{subject.capitalize()} looks desperate for relief from the pleasure bombarding her body.")
    elif dice_roll == 4:
        $ renpy.say(None, f"{subject.capitalize()} fights not to moan out, the waves of pleasure almost too much handle.")

    return