init python:

    def Rogue_gifts():
        label = "Rogue_gifts"

        conditions = [
            "False"]

        return EventClass(label, conditions)

label Rogue_gifts:
    $ ongoing_Event = True

    $ Rogue.change_face("worried2", blush = 1)

    ch_Player "Hey, I've been wondering. . ."
    ch_Player "I feel like you'd be the kind of person who decorates their room a lot, but it's pretty barren."

    $ Rogue.change_face("worried1", eyes = "right", blush = 1)

    ch_Rogue "Ah usually am. . ."
    ch_Rogue "Just wasn't sure how long ah'd be welcome here."
    ch_Rogue "Didn't want to get too attached, ah guess. . ."

    $ Rogue.change_face("worried2", blush = 1)

    ch_Player "Maybe I can pick some stuff out for you?"
    ch_Player "Because I'm gonna make sure you always feel welcome."

    $ Rogue.change_face("worried1", mouth = "smirk", blush = 1)

    ch_Rogue "Ah'd like that, thank you."

    $ temp = Rogue.chat_options[:]

    python:
        for chat_option in temp:
            if "decorated" in chat_option:
                Rogue.chat_options.remove(chat_option)

    $ ongoing_Event = False

    return