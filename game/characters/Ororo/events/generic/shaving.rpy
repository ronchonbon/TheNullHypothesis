init python:

    def Ororo_shaving():
        label = "Ororo_shaving"

        conditions = [
            "Ororo.pubes_to_shave or Ororo.pubes_to_shave is None",

            "Ororo.location in bedrooms"]

        repeatable = True
        automatic = True

        return EventClass(label, conditions, repeatable = repeatable, automatic = automatic)

label Ororo_shaving:
    $ Ororo.pubes_growing = False
    $ Ororo.pubes = Ororo.pubes_to_shave
    $ Ororo.pubes_to_shave = False

    return

init python:

    def Ororo_growing_back():
        label = "Ororo_growing_back"

        conditions = [
            "Ororo.pubes_to_grow or Ororo.pubes_to_grow is None"]

        automatic = True

        return EventClass(label, conditions, automatic = automatic)

label Ororo_growing_back:

    return

init python:

    def Ororo_grown_back():
        label = "Ororo_grown_back"

        conditions = [
            "EventScheduler.Events['Ororo_growing_back'].completed",
            "day - EventScheduler.Events['Ororo_growing_back'].completed_when >= 2"]

        repeatable = True
        automatic = True

        return EventClass(label, conditions, repeatable = repeatable, automatic = automatic)

label Ororo_grown_back:
    if day - EventScheduler.Events['Ororo_growing_back'].completed_when >= 7:
        $ Ororo.pubes_growing = False
        $ Ororo.pubes = Ororo.pubes_to_grow
        $ Ororo.pubes_to_grow = False

        $ EventScheduler.Events["Ororo_growing_back"].completed_when = 1e8
    else:
        $ Ororo.pubes_growing = True

    return
