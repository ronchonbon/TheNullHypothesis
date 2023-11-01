init python:

    def Jean_gifts():
        label = "Jean_gifts"

        conditions = [
            "False"]

        return EventClass(label, conditions)

label Jean_gifts:
    $ ongoing_Event = True

    $ Jean.change_face("confused1", mouth = "smirk")

    ch_Player "Hey, so. . ."
    ch_Player "I know you've been at the school for a while."
    ch_Player "Years, right?"
    ch_Jean "Mhm."

    $ Jean.change_face("worried2", blush = 1)

    ch_Player "I've noticed. . . your dorm room doesn't really have any decorations."
    ch_Player "Or anything 'fun' for that matter."
    ch_Player "Unless you have fun doing schoolwork on that big whiteboard. . ." 

    $ Jean.change_face("worried1", eyes = "right", blush = 1)

    ch_Jean "Schoolwork can be fun. . ."

    $ Jean.change_face("worried1", blush = 1)

    ch_Jean "You know how focused I've been on my grades."

    $ Jean.change_face("worried1", eyes = "right", blush = 1)

    ch_Jean "Decorating my room was never really a priority."

    $ Jean.change_face("worried2", mouth = "smirk", blush = 1)

    ch_Player "Maybe I can pick some stuff out for you?"
    ch_Player "Because now that I'm here, I'm gonna make sure fun becomes one of your priorities."

    $ Jean.change_face("worried1", mouth = "smirk", blush = 1)

    ch_Jean "You'd do that?"

    $ Jean.change_face("worried1", eyes = "right", mouth = "smirk", blush = 1)

    ch_Jean "That would be nice. . ."

    $ Jean.change_face("confused1", mouth = "smirk", blush = 1)

    ch_Jean "But I don't want much."
    ch_Jean "Maybe just some interesting books and plants to put around."

    $ temp = Jean.chat_options[:]

    python:
        for chat_option in temp:
            if "decorated" in chat_option:
                Jean.chat_options.remove(chat_option)

    $ ongoing_Event = False

    return