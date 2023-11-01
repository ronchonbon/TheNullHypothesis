init python:

    def Laura_shaving():
        label = "Laura_shaving"

        conditions = [
            'Laura.pubes_to_shave or Laura.pubes_to_shave is None',
            'Laura.location in bedrooms']

        repeatable = True
        automatic = True

        return EventClass(label, conditions, repeatable = repeatable, automatic = automatic)

label Laura_shaving:
    $ Laura.pubes_growing = False
    $ Laura.pubes = Laura.pubes_to_shave
    $ Laura.pubes_to_shave = False

    return

init python:

    def Laura_growing_back():
        label = "Laura_growing_back"

        conditions = [
            "Laura.pubes_to_grow or Laura.pubes_to_grow is None"]

        automatic = True

        return EventClass(label, conditions, automatic = automatic)

label Laura_growing_back:

    return

init python:

    def Laura_grown_back():
        label = "Laura_grown_back"

        conditions = [
            "EventScheduler.Events['Laura_growing_back'].completed",
            "day - EventScheduler.Events['Laura_growing_back'].completed >= 2"]

        repeatable = True
        automatic = True

        return EventClass(label, conditions, repeatable = repeatable, automatic = automatic)

label Laura_grown_back:
    if day - EventScheduler.Events['Laura_growing_back'].completed >= 7:
        $ Laura.pubes_growing = False
        $ Laura.pubes = Laura.pubes_to_grow
        $ Laura.pubes_to_grow = False

        $ EventScheduler.Events["Laura_growing_back"].completed = 0
    else:
        $ Laura.pubes_growing = True

    return
