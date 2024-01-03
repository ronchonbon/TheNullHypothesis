label Kurt_arrives:
    if Kurt.History.check("seen_Player", tracker = "recent") or Kurt.History.check("seen_Player", tracker = "last"):
        $ modifier = " again"
    else:
        $ modifier = ""

    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        $ Kurt.change_face("happy") 
        
        ch_Kurt "Hallo[modifier]!"
    elif dice_roll == 2:
        $ Kurt.change_face("pleased1")

        ch_Kurt "Ah, good to see you[modifier], [Player.first_name]!"
    elif dice_roll == 3:
        $ Kurt.change_face("pleased1")

        ch_Kurt "Oh, hallo[modifier]!"

    return

label Kurt_leaves:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        $ Kurt.change_face("happy") 
        
        ch_Kurt "Auf Wiedersehen!"
    elif dice_roll == 2:
        $ Kurt.change_face("pleased1")

        ch_Kurt "Talk to you later, ja?"
    elif dice_roll == 3:
        $ Kurt.change_face("neutral", mouth = "happy")

        ch_Kurt "See you later, [Player.first_name]."

    return
    
label Kurt_greets_Player:
    if Kurt.History.check("seen_Player", tracker = "recent") or Kurt.History.check("seen_Player", tracker = "last"):
        $ modifier = " again"
    else:
        $ modifier = ""
        
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        $ Kurt.change_face("happy") 
        
        ch_Kurt "Hallo[modifier]!"
    elif dice_roll == 2:
        $ Kurt.change_face("pleased1")

        ch_Kurt "Ah, good to see you[modifier], [Player.first_name]!"
    elif dice_roll == 3:
        $ Kurt.change_face("pleased1")

        ch_Kurt "Oh, hallo[modifier]!"

    return