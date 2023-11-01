label set_music:
    if Player.location == "bg_danger":
        if time_index < 3:
            play music "sounds/music/Danger Room.ogg" fadeout 1.0 fadein 1.0 if_changed
        else:
            play music "sounds/music/Investigation.ogg" fadeout 1.0 fadein 1.0 if_changed
    else:
        if weather == "rain":
            play music "sounds/music/Rain.ogg" fadeout 1.0 fadein 1.0 if_changed
        elif time_index < 3:
            play music "sounds/music/Day to Day.ogg" fadeout 1.0 fadein 1.0 if_changed
        else:
            if Player.location in bedrooms:
                play music "sounds/music/Evening.ogg" fadeout 1.0 fadein 1.0 if_changed
            else:
                play music "sounds/music/Investigation.ogg" fadeout 1.0 fadein 1.0 if_changed

    return