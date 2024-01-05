label Charles_arrives:
    if Charles.History.check("seen_Player", tracker = "recent") > 1 or Charles.History.check("seen_Player", tracker = "last"):
        $ modifier = " again"
    else:
        $ modifier = ""

    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        $ Charles.change_face("smirk1")

        ch_Charles "Hello[modifier], [Player.first_name]."
    elif dice_roll == 2:
        $ Charles.change_face("pleased1")

        ch_Charles "[Player.first_name], good to see you[modifier]."
    elif dice_roll == 3:
        $ Charles.change_face("smirk1", brows = "cocked")

        ch_Charles "Ah, hello[modifier], [Player.first_name]."

    return
    
label Charles_leaves:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        $ Charles.change_face("smirk1")

        ch_Charles "I will leave you to it, [Player.first_name]."
    elif dice_roll == 2:
        $ Charles.change_face("pleased1")

        ch_Charles "Goodbye, [Player.first_name]."
    elif dice_roll == 3:
        $ Charles.change_face("neutral", brows = "raised")

        ch_Charles "I believe I am needed elsewhere."

    return
    
label Charles_greets_Player:
    if Charles.History.check("seen_Player", tracker = "recent") > 1 or Charles.History.check("seen_Player", tracker = "last"):
        $ modifier = " again"
    else:
        $ modifier = ""

    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        $ Charles.change_face("smirk1")

        ch_Charles "Hello[modifier], [Player.first_name]."
    elif dice_roll == 2:
        $ Charles.change_face("pleased1")

        ch_Charles "[Player.first_name], good to see you[modifier]."
    elif dice_roll == 3:
        $ Charles.change_face("smirk1", brows = "cocked")

        ch_Charles "Ah, hello[modifier], [Player.first_name]."

    return