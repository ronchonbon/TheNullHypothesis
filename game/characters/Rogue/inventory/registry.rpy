init python:

    def Rogue_special_Items():
        Items = []

        if EventScheduler.Events["Rogue_gifts"].completed:
            Items.append(baseball_flag(Rogue))

        if EventScheduler.Events["Rogue_enjoying_being_girlfriend"].completed:
            Items.append(acoustic_guitar(Rogue))
            Items.append(mirror(Rogue))

        if EventScheduler.Events["Rogue_penultimate_penultimate_quirk"].completed:
            Items.append(camera(Rogue))
            Items.append(occult_posters(Rogue))

        return Items