init python:

    def Laura_seeing_penis():
        label = "Laura_seeing_penis"

        conditions = [
            "False"]

        return EventClass(label, conditions)

label Laura_seeing_penis:
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
    
    return