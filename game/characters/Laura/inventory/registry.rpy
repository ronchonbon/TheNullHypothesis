init python:

    def Laura_special_Items():
        Items = []

        if EventScheduler.Events["Laura_boyfriend"].completed:
            Items.append(boxing_kit(Laura))
            Items.append(MMA_gloves(Laura))

        if EventScheduler.Events["Laura_enjoying_being_girlfriend"].completed:
            Items.append(band_posters(Laura))
            Items.append(record_player(Laura))

        if EventScheduler.Events["Laura_penultimate_quirk"].completed:
            Items.append(motorcycle_helmet(Laura))
            Items.append(motorcycle_posters(Laura))
            Items.append(mirror(Laura))

        return Items