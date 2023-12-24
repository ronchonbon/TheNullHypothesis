label Charles_arrives:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        $ Charles.change_face("happy")
    elif dice_roll == 2:
        $ Charles.change_face("pleased1")
    elif dice_roll == 2:
        $ Charles.change_face("neutral", brows = "cocked", mouth = "happy")

    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        ch_Charles "Hello, [Player.first_name]."
    elif dice_roll == 2:
        ch_Charles "[Player.first_name], good to see you."
    elif dice_roll == 3:
        ch_Charles "Ah, hello, [Player.first_name]."

    return
    
label Charles_leaves:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        ch_Charles "I will leave you to it, [Player.first_name]."
    elif dice_roll == 2:
        ch_Charles "Goodbye, [Player.first_name]."
    elif dice_roll == 3:
        ch_Charles "I believe I am needed elsewhere."

    return
    
label Charles_greets_Player:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        $ Charles.change_face("happy")
    elif dice_roll == 2:
        $ Charles.change_face("pleased1")
    elif dice_roll == 2:
        $ Charles.change_face("neutral", brows = "cocked", mouth = "happy")

    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        ch_Charles "Hello, [Player.first_name]."
    elif dice_roll == 2:
        ch_Charles "[Player.first_name], good to see you."
    elif dice_roll == 3:
        ch_Charles "Ah, hello, [Player.first_name]."

    return