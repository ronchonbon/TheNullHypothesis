label Laura_seeing_penis(proper_subject = True, undressing = True):
    if not Laura.History.check("seen_Player_naked"):
        "You remove your pants, exposing yourself to her."

        $ Laura.change_face("surprised1", eyes = "down", mouth = "lipbite", blush = 1)

        ch_Laura "Interesting. . ." 

        $ Laura.change_face("surprised1", eyes = "down", mouth = "lipbite", blush = 2)

        "Her nostrils flare slightly." 
        ch_Laura "Hmmm. . ." 

        $ Laura.change_face("confused1", eyes = "down", mouth = "lipbite", blush = 1)

        ch_Laura "Are they all. . . this large. . . ?"

        $ Laura.change_face("sexy", blush = 2)

        ch_Laura "Looking at it makes me feel. . . interesting."
    elif renpy.random.random() > 0.5:
        if proper_subject:
            $ subject = Laura.name
            $ object = Laura.name
            $ owner = Laura.name + "'s"
        else:
            $ subject = "she"
            $ object = "her"
            $ owner = "her"
            
        $ pool = seeing_penis_narrations(Laura, proper_subject = proper_subject, undressing = undressing)

        $ dialogue = renpy.random.choice(pool)

        "[dialogue]"
    
    return