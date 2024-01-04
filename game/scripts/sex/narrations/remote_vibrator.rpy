label Character_remote_vibrator_on_narrations(Character, proper_subject = True):
    if proper_subject:
        $ subject = Character.name
        $ object = Character.name
        $ owner = Character.name + "'s"
    else:
        $ subject = "she"
        $ object = "her"
        $ owner = "her"

    $ sex_faces([Character])
    $ sex_poses([Character])

    $ dice_pool = []

    if "pussy_covered" in Character.traits:
        $ dice_pool.append(1)
        $ dice_pool.append(2)
    else:
        $ dice_pool.append(3)
        $ dice_pool.append(4)

    $ dice_roll = renpy.random.choice(dice_pool)

    if dice_roll == 1:
        $ renpy.say(None, f"You hear a very faint buzzing emerge from {owner} clothing.")
    elif dice_roll == 2:
        $ renpy.say(None, f"As you press the button, you listen closely for the barely audible sound of the vibrator buzzing through {owner} clothing.")
    elif dice_roll == 3:
        $ renpy.say(None, f"{owner.capitalize()} vibrator hums to life.")
    elif dice_roll == 4:
        $ renpy.say(None, f"The moment you press the button, {owner} vibrator starts buzzing noisely.")

    return

label Character_remote_vibrator_off_narrations(Character, proper_subject = True):
    if proper_subject:
        $ subject = Character.name
        $ object = Character.name
        $ owner = Character.name + "'s"
    else:
        $ subject = "she"
        $ object = "her"
        $ owner = "her"

    $ sex_faces([Character])
    $ sex_poses([Character])

    $ dice_pool = []

    if "pussy_covered" in Character.traits:
        $ dice_pool.append(1)
        $ dice_pool.append(2)
    else:
        $ dice_pool.append(3)
        $ dice_pool.append(4)

    $ dice_roll = renpy.random.choice(dice_pool)

    if dice_roll == 1:
        $ renpy.say(None, f"The faint buzzing from {owner} clothing stops.")
    elif dice_roll == 2:
        $ renpy.say(None, f"The vibrator hiding in {owner} clothing goes silent.")
    elif dice_roll == 3:
        $ renpy.say(None, f"{owner.capitalize()} vibrator's buzzing comes to a halt.")
    elif dice_roll == 4:
        $ renpy.say(None, f"The humming of {owner} vibrator goes quiet.")

    return

label Character_remote_vibrator_narrations(Character, proper_subject = True):
    if proper_subject:
        $ subject = Character.name
        $ object = Character.name
        $ owner = Character.name + "'s"
    else:
        $ subject = "she"
        $ object = "her"
        $ owner = "her"

    $ sex_faces([Character])
    $ sex_poses([Character])

    if renpy.random.random() > 0.5:
        $ noun = "folds"
    else:
        $ noun = "pussy"

    if renpy.random.random() > 0.75 and temp_Characters[0].desire >= 75:
        $ adjective = "soaking wet "
    elif renpy.random.random() > 0.5:
        if temp_Characters[0].body_hair["pubic"] in ["bush", "hairy"]:
            $ adjective = "hairy "
        elif not temp_Characters[0].body_hair["pubic"]:
            $ adjective = "smooth "
        else:
            $ adjective = "trimmed "
    elif renpy.random.random() > 0.25:
        $ adjective = "glistening "
    else:
        $ adjective = ""
    
    $ dice_pool = []

    if "pussy_covered" in Character.traits:
        if Character.remote_vibrator >= 0.9:
            $ dice_pool.append(1)
        else:
            $ dice_pool.append(2)
            $ dice_pool.append(3)
    else:
        if Character.remote_vibrator >= 0.9:
            $ dice_pool.append(4)
        else:
            $ dice_pool.append(5)
            $ dice_pool.append(6)

    $ dice_roll = renpy.random.choice(dice_pool)

    if dice_roll == 1:
        $ renpy.say(None, f"The vibrator audibly buzzes, even through {owner} clothing.")
    elif dice_roll == 2:
        $ renpy.say(None, f"You can hear the faint buzzing of the vibrator through {owner} clothing.")
    elif dice_roll == 3:
        $ renpy.say(None, f"{owner.capitalize()} vibrator hums from within her clothing, barely audible except for when the room goes quiet.")
    elif dice_roll == 4:
        $ renpy.say(None, f"{owner.capitalize()} vibrator fills the room with the sound of its buzzing.")
    elif dice_roll == 5:
        $ renpy.say(None, f"The tail of {owner} vibrator peeks out from her {adjective}{noun}, steadily buzzing away.")
    elif dice_roll == 6:
        $ renpy.say(None, f"The vibrator melodically hums along from inside {owner} {adjective}{noun}.")

    return