label Charles_arrives:
    $ Charles.change_face("happy")

    ch_Charles "Hello, [Player.first_name]."

    return
    
label Charles_leaves:
    ch_Charles "I will leave you to it, [Player.first_name]."

    return
    
label Charles_greets_Player:
    $ Charles.change_face("happy")
    
    ch_Charles "Hello, [Player.first_name]."

    return