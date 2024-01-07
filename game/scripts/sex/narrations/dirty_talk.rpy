init python:

    import math

label sex_talk(Character):
    if Character.mouth_Actions and ((Character.mouth_Actions[0].Action_type == "blowjob" and Character.mouth_Actions[0].mode == 3) or Character.mouth_Actions[0].Action_type == "deepthroat"):
        $ dice_pool = [1]

        if Character.desire >= 50:
            $ dice_pool.append(2)
        
        if Character.History.check(Character.mouth_Actions[0].Action_type) >= 10:
            $ dice_pool.append(3)
        else:
            $ dice_pool.append(4)

        $ dice_roll = renpy.random.choice(dice_pool)

        if dice_roll == 1:
            $ renpy.say(Character.voice, "*gag*")
        elif dice_roll == 2:
            $ renpy.say(Character.voice, "Mmmmm.")
        elif dice_roll == 3:
            $ renpy.say(Character.voice, "*hum*")
        elif dice_roll == 4:
            $ renpy.say(Character.voice, "*cough*")
    else:
        call expression f"{Character.tag}_dirty_talk" from _call_expression_138

    return