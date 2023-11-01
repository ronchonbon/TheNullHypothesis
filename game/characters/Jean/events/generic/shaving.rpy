init python:

    def Jean_shaving():
        label = "Jean_shaving"

        conditions = [
            'Jean.pubes_to_shave or Jean.pubes_to_shave is None',
            'Jean.location in bedrooms']

        repeatable = True
        automatic = True

        return EventClass(label, conditions, repeatable = repeatable, automatic = automatic)

label Jean_shaving:
    $ Jean.pubes_growing = False
    $ Jean.pubes = Jean.pubes_to_shave
    $ Jean.pubes_to_shave = False

    return

init python:

    def Jean_growing_back():
        label = "Jean_growing_back"

        conditions = [
            "Jean.pubes_to_grow or Jean.pubes_to_grow is None"]

        automatic = True

        return EventClass(label, conditions, automatic = automatic)

label Jean_growing_back:

    return

init python:

    def Jean_grown_back():
        label = "Jean_grown_back"

        conditions = [
            "EventScheduler.Events['Jean_growing_back'].completed",
            "day - EventScheduler.Events['Jean_growing_back'].completed >= 2"]

        repeatable = True
        automatic = True

        return EventClass(label, conditions, repeatable = repeatable, automatic = automatic)

label Jean_grown_back:
    if day - EventScheduler.Events["Jean_growing_back"].completed >= 7:
        $ Jean.pubes_growing = False
        $ Jean.pubes = Jean.pubes_to_grow
        $ Jean.pubes_to_grow = False

        $ EventScheduler.Events["Jean_growing_back"].completed = 0
    else:
        $ Jean.pubes_growing = True

    return
