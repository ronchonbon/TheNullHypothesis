init python:

    def Jean_seeing_penis():
        label = "Jean_seeing_penis"

        conditions = [
            "False"]

        return EventClass(label, conditions)

label Jean_seeing_penis:
    "As you remove your pants, [Jean.name] can't help but glue her eyes to your crotch."

    $ Jean.change_face("surprised1", eyes = "down", mouth = "lipbite", blush = 1)

    ch_Jean "Damn. . ."

    $ Jean.change_face("worried1", eyes = "down", mouth = "lipbite", blush = 1)

    ch_Jean "You're really. . . well endowed. . ."

    $ Jean.change_face("confused1", eyes = "down", mouth = "lipbite", blush = 2)

    ch_Jean "I didn't think they were supposed to be so. . . big. . ."

    $ Jean.change_face("worried1", mouth = "lipbite", blush = 1)

    ch_Jean "I guess we'll just have to put the work in. . ."

    $ Jean.change_face("sly", mouth = "lipbite", blush = 1)

    ch_Jean "So I can properly handle it."

    return