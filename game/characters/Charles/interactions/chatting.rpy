label Charles_chatting(line):
        
    return

label Charles_busy:

    return

label Charles_busy_asked_once:

    return

label Charles_busy_asked_twice:

    return

label Charles_busy_late:

    return

label Charles_busy_late_asked_once:

    return

label Charles_busy_late_asked_twice:

    return

label Charles_talk_later:

    return

label Charles_answering_phone:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        ch_Charles "Yes, [Player.first_name]?"
    elif dice_roll == 2:
        ch_Charles "Hello, [Player.first_name]."
    elif dice_roll == 3:
        ch_Charles "[Player.first_name], how can I help you?"

    return