init python:

    def Rogue_shaving():
        label = "Rogue_shaving"

        conditions = [
            'Rogue.pubes_to_shave or Rogue.pubes_to_shave is None',
            'Rogue.location in bedrooms']

        repeatable = True
        automatic = True

        return EventClass(label, conditions, repeatable = repeatable, automatic = automatic)

label Rogue_shaving:
    $ Rogue.pubes_growing = False
    $ Rogue.pubes = Rogue.pubes_to_shave
    $ Rogue.pubes_to_shave = False

    return

init python:

    def Rogue_growing_back():
        label = "Rogue_growing_back"

        conditions = [
            "Rogue.pubes_to_grow or Rogue.pubes_to_grow is None"]

        automatic = True

        return EventClass(label, conditions, automatic = automatic)

label Rogue_growing_back:

    return

init python:

    def Rogue_grown_back():
        label = "Rogue_grown_back"

        conditions = [
            "EventScheduler.Events['Rogue_growing_back'].completed",
            "day - EventScheduler.Events['Rogue_growing_back'].completed >= 2"]

        repeatable = True
        automatic = True

        return EventClass(label, conditions, repeatable = repeatable, automatic = automatic)

label Rogue_grown_back:
    if day - EventScheduler.Events['Rogue_growing_back'].completed >= 7:
        $ Rogue.pubes_growing = False
        $ Rogue.pubes = Rogue.pubes_to_grow
        $ Rogue.pubes_to_grow = False

        $ EventScheduler.Events["Rogue_growing_back"].completed = 0
    else:
        $ Rogue.pubes_growing = True

    return
